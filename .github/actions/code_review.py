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

def generate_valid_inline_comments_for_file(filename, patch):
    # Prompt focused on giving feedback only where necessary
    prompt = f"Review the changes in the file {filename} and suggest any **important inline comments** " \
             f"where the code could be improved or there is a notable issue. **Avoid commenting on every line** and only give feedback when necessary:\n\n" \
             f"```diff\n{patch}\n```"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert code reviewer."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=2000,
        temperature=0.2
    )
    
    comments = response.choices[0].message['content'].strip()
    return comments

def post_inline_comment(pr, filename, comment_body, line_number):
    try:
        pr.create_review_comment(
            body=comment_body,
            commit_id=pr.head.sha,
            path=filename,
            position=line_number  # Inline comment position in the diff
        )
    except GithubException as e:
        print(f"Failed to post inline comment on {filename}: {e}")

def post_general_comment(pr, model_name):
    # General comment at the end of the review
    general_comment = f"This pull request was reviewed by {model_name}."
    try:
        pr.create_issue_comment(body=general_comment)
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

        # Generate inline comments for each file, only if there's a valid suggestion
        comments = generate_valid_inline_comments_for_file(filename, patch)

        # Parse and post inline comments for each line if meaningful
        lines = comments.split("\n")
        for line in lines:
            if line.startswith("Line"):
                # Assuming comments are in the format: "Line X: Comment"
                line_parts = line.split(":")
                line_number = int(line_parts[0].replace("Line", "").strip())
                comment_body = ":".join(line_parts[1:]).strip()

                # Post inline comment to GitHub only for valid comments
                if comment_body:
                    post_inline_comment(pr, filename, comment_body, line_number)

    # Post a general comment about the review
    model_name = "GPT-4"  # Adjust the model name here if needed
    post_general_comment(pr, model_name)

if __name__ == "__main__":
    main()
