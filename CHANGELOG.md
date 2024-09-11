

## 2024-09-11
### Changelog Entry

**Added**: Step to automate the opening of a pull request for updating the changelog.

- Enhanced the `.github/workflows/update_changelog.yml` workflow by adding a new job that:
  - Creates a unique branch for changelog updates.
  - Configures Git user credentials for the GitHub Actions environment.
  - Stages and commits changes to `CHANGELOG.md`.
  - Pushes the new branch to the repository.
  - Opens a pull request with a title and body indicating it serves to update the changelog with the latest entries.

This automation streamlines the process of updating the changelog and ensures that changes are properly reviewed through the conventional pull request workflow.
