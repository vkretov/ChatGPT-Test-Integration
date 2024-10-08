import os
import openai
from github import Github, GithubException

def get_pull_request():
    repo_name = os.getenv('GITHUB_REPOSITORY')
    pr_number = os.getenv('PR_NUMBER')
    g = Github(os.getenv('GITHUB_TOKEN'))
    repo = g.get_repo(repo_name)
    pr = repo.get_pull(int(pr_number))
    return pr

def get_file_diffs(pr):
    files = pr.get_files()
    diffs = []
    for file in files:
        if file.patch:  # Only process files with a diff
            diffs.append({
                "filename": file.filename,
                "patch": file.patch
            })
    return diffs

def generate_valid_comment_for_file(filename, patch):
    # Updated prompt to instruct GPT to give a single comment
    prompt = f"Review the changes in the file {filename} and suggest one important comment " \
             f"about the code. If there is nothing to improve, simply say 'This file looks good.'\n\n" \
             f"```diff\n{patch}\n```"

    response = openai.chat.completions.create(
        model="gpt-4o-mini",  # Use GPT-4 model
        messages=[
            {"role": "system", "content": "You are an expert code reviewer."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
        temperature=0.2
    )
    
    print(response.choices[0].message)
    comment = response.choices[0].message.content
    return comment if comment else "This file looks good."    

def generate_combined_review(diffs):
    # Combine all diffs into a single prompt for the entire PR
    combined_diff = "\n".join([f"### {diff['filename']}\n```diff\n{diff['patch']}\n```" for diff in diffs])
    
    prompt = f"Review the following changes in the pull request and provide comments or suggestions for improvement. " \
             f"Please give important feedback and identify any potential issues in the entire set of changes. " \
             f"**If everything looks good, mention that there are no improvements needed.**\n\n{combined_diff}"

    response = openai.chat.completions.create(
        model="gpt-4o-mini",  # Use GPT-4 model
        messages=[
            {"role": "system", "content": "You are an expert code reviewer."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=3000,  # Adjust based on your needs
        temperature=0.2
    )
    
    print(response.choices[0].message)
    comments = response.choices[0].message.content
    return comments

def post_inline_comment(pr, filename, comment_body):
    try:
        pr.create_review_comment(
            body=comment_body,
            commit=pr.get_commits()[pr.commits - 1],
            path=filename,
            line=1  # Posting a general comment at the start of the file
        )
    except GithubException as e:
        print(f"Failed to post inline comment on {filename}: {e}")

def post_general_comment(pr, comment_body):
    try:
        pr.create_issue_comment(body=comment_body)
    except GithubException as e:
        print(f"Failed to post general comment: {e}")

def main():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    pr = get_pull_request()
    diffs = get_file_diffs(pr)

    if not diffs:
        print("No file changes found in the pull request.")
        return

    
    for diff in diffs:
        filename = diff['filename']
        patch = diff['patch']

        comment = generate_valid_comment_for_file(filename, patch)
        print("possting file comment")
        # Post the single comment for this file
        post_inline_comment(pr, filename, comment)

    # Generate a combined review based on all file diffs
    review_comments = generate_combined_review(diffs)
    
    print("posting whole comment")
    # Post the review comments as a general comment on the PR
    post_general_comment(pr, review_comments)

if __name__ == "__main__":
    main()
