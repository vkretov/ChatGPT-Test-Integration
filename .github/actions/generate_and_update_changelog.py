import os
import datetime
from github import Github
import openai

# Configuration
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_NAME = os.getenv('GITHUB_REPOSITORY')
PR_NUMBER = os.getenv('PR_NUMBER')

# Initialize GitHub API client
github = Github(GITHUB_TOKEN)
repo = github.get_repo(REPO_NAME)

def get_pr_details():
    pr = repo.get_pull(int(PR_NUMBER))
    return pr

def get_pr_diffs(pr):
    diffs = pr.get_files()
    diff_text = ""
    for diff in diffs:
        filename = diff.filename
        patch = diff.patch
        diff_text += f"### {filename}\n```\n{patch}\n```\n"
    return diff_text

def generate_update_content(pr_details, pr_diffs, existing_content, update_type, additional_prompt):
    prompt = (f"Generate an update for the {update_type} based on the following:\n"
              f"Title: {pr_details.title}\n"
              f"Body: {pr_details.body}\n"
              f"Differences:\n{pr_diffs}\n"
              f"Existing Content:\n{existing_content}\n"
              f"Additional Prompt:\n{additional_prompt}\n")
    openai.api_key = OPENAI_API_KEY
    response = openai.chat.completions.create(
        model='gpt-4o-mini',
        messages=[{'role': 'user', 'content': prompt}],
    )
    result = response.choices[0].message.content.strip()
    print(response.choices[0].message.content.strip())
    return result

def update_file(file_path, content):
    print(f"Updating file: {file_path}")
    # Ensure the file exists or create it
    if not os.path.exists(file_path):
        print(f"File does not exist. Creating new file at {file_path}")
        with open(file_path, 'w') as file:
            file.write(content)
    else:
        with open(file_path, 'r') as file:
            existing_content = file.read()
        new_content = existing_content + "\n\n" + content
        with open(file_path, 'w') as file:
            file.write(new_content)
    print(f"File updated successfully: {file_path}")

if __name__ == '__main__':
    try:
        pr_details = get_pr_details()
        pr_diffs = get_pr_diffs(pr_details)
        
        # Update CHANGELOG.md
        changelog_entry = generate_update_content(pr_details, pr_diffs, "", "changelog", "")
        update_file('CHANGELOG.md', changelog_entry)
        
        # Update README.md
        readme_entry = generate_update_content(pr_details, pr_diffs, "", "README", "This should be in md format. The output is a replacement of this file and should not have any place holders")
        update_file('README.md', readme_entry)
        
    except Exception as e:
        print(f"Script error: {e}")
