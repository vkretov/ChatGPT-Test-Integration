

## 2024-09-11
## Changelog Entry

### Added
- Added a basic README.md file to the repository, providing an overview of the project.
  - Describes that the repository contains a test API.
  - Mentions the inclusion of GitHub Actions for automatic code reviews and changelog generation.
  - Notes that API documentation is forthcoming (TBD).


## 2024-09-11
## Changelog Entry

### Revert Changes
- **Reverted**: Pull request [#17](https://github.com/vkretov/ChatGPT-Test-Integration/pull/17) "test - delete workflows"
  
### Updated Workflows
- **Restored Workflows**:
  - Readded the **Code Review with ChatGPT** workflow in `.github/workflows/code_review.yml`:
    - This workflow triggers on pull request events (`opened`, `synchronize`, `reopened`) and pushes to the main branch.
    - It includes steps to check out the code, set up Python, install dependencies, and execute a code review using ChatGPT.
  
  - Readded the **Update Changelog** workflow in `.github/workflows/update_changelog.yml`:
    - This workflow triggers on pushes to the main branch.
    - It includes steps for checking out the code, setting up Python, installing dependencies, fetching the pull request number, generating and updating the changelog, and finally creating a new branch with the changes and opening a pull request for the updates. 

These changes restore the workflows that were previously removed, enhancing automation and maintaining a proper changelog.


# Changelog Update

## Version [Insert Version Here] - [Insert Date Here]

### Changes
- Updated workflow to now not only update the `CHANGELOG.md` file but also the `README.md` file based on the details of pull requests.

### Details
- The script has been modified to include a new function `generate_update_content`, which generates update content based on the type (changelog or README) along with the pull request differences.
- The `update_file` function now handles updates for both `CHANGELOG.md` and `README.md`. It checks if the files exist, creates them if they do not, and appends the new content read from the pull request.
- The existing content of `CHANGELOG.md` and `README.md` is retained, ensuring no information is lost during the update process.

### Code Changes
- The function for generating changelog entries has been replaced with a more generalized approach for handling updates.
- Separate update logic for `CHANGELOG.md` and `README.md` has been introduced.

This update enhances the workflow by automating the documentation process related to pull requests more comprehensively. All relevant changes in code should now be reflected in both the changelog and the README file, keeping project documentation up to date effortlessly.