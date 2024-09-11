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

def generate_changelog_entry(pr_details, pr_diffs):
    prompt = (f"Generate a changelog entry for the following pull request:\n"
              f"Title: {pr_details.title}\n"
              f"Body: {pr_details.body}\n"
              f"Differences:\n{pr_diffs}\n")
    openai.api_key = OPENAI_API_KEY
    response = openai.chat.completions.create(
        model='gpt-4o-mini',
        messages=[{'role': 'user', 'content': prompt}],
    )
    result = response.choices[0].message.content.strip()
    return result

def update_changelog(changelog_entry):
    changelog_path = 'CHANGELOG.md'
    
    print(f"Updating changelog at: {changelog_path}")  # Debugging line
    
    # Ensure the file exists or create it
    if not os.path.exists(changelog_path):
        print(f"File does not exist. Creating new file at {changelog_path}")  # Debugging line
        with open(changelog_path, 'w') as changelog_file:
            changelog_file.write('# Changelog\n')  # Initial header
    
    try:
        # Append new changelog entry
        with open(changelog_path, 'a') as changelog_file:
            changelog_file.write(f'\n\n## {datetime.datetime.now().strftime("%Y-%m-%d")}\n{changelog_entry}\n')
        print(f"Changelog entry written successfully")  # Debugging line
    except Exception as e:
        print(f"Error writing to changelog: {e}")  # Debugging line

if __name__ == '__main__':
    try:
        pr_details = get_pr_details()
        pr_diffs = get_pr_diffs(pr_details)
        changelog_entry = generate_changelog_entry(pr_details, pr_diffs)
        update_changelog(changelog_entry)
    except Exception as e:
        print(f"Script error: {e}")
