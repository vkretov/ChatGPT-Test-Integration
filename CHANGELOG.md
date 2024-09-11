

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

## Changelog

### Added
- Implemented support for cities in the weather forecast feature.
  - Introduced a new static array for cities, including major cities like New York, Los Angeles, and Chicago.
  - Updated the `WeatherForecast` model to include a `City` property.
  - Modified `WeatherForecastController` to generate a random city along with the weather forecast data.

### Improvements
- Changed the HTTP GET method name in `WeatherForecastController` from `GetWeatherForecast` to `GetWeatherForecastByCity` for clearer functionality indication.

### Configuration
- Updated `.gitignore` to exclude the `bin` directory in addition to the `obj` directory for better build hygiene.

### Changelog Update - New Feature: More Specific Prompts

#### Enhancements
- **Feature Addition**: Updated the `generate_update_content` function to accept an additional parameter (`additional_prompt`) that allows for the inclusion of more specific prompts when generating updates.
  
#### Changes
- **File Modification**: 
  - Updated `.github/actions/generate_and_update_changelog.py` to incorporate enhanced prompt capabilities.
    - The function `generate_update_content` now includes an `additional_prompt` argument to provide more context during the generation of changelog and README entries.
    - Existing functionality remains intact, ensuring backward compatibility while enriching the prompt generation process. 

#### Usage
- The README updates now include a specific prompt indicating the desired Markdown format, ensuring consistent output that meets the documentation standards. 

#### Code Diff
```diff
@@ -26,12 +26,13 @@ def get_pr_diffs(pr):
         diff_text += f"### {filename}\n```\n{patch}\n```\n"
     return diff_text
 
-def generate_update_content(pr_details, pr_diffs, existing_content, update_type):
+def generate_update_content(pr_details, pr_diffs, existing_content, update_type, additional_prompt):
     prompt = (f"Generate an update for the {update_type} based on the following:\n"
               f"Title: {pr_details.title}\n"
               f"Body: {pr_details.body}\n"
               f"Differences:\n{pr_diffs}\n"
-              f"Existing Content:\n{existing_content}\n")
+              f"Existing Content:\n{existing_content}\n"
+              f"Additional Prompt:\n{additional_prompt}\n")
     openai.api_key = OPENAI_API_KEY
     response = openai.chat.completions.create(
         model='gpt-4o-mini',
@@ -62,11 +63,11 @@ def update_file(file_path, content):
         pr_diffs = get_pr_diffs(pr_details)
         
         # Update CHANGELOG.md
-        changelog_entry = generate_update_content(pr_details, pr_diffs, "", "changelog")
+        changelog_entry = generate_update_content(pr_details, pr_diffs, "", "changelog", "")
         update_file('CHANGELOG.md', changelog_entry)
         
         # Update README.md
-        readme_entry = generate_update_content(pr_details, pr_diffs, "", "README")
+        readme_entry = generate_update_content(pr_details, pr_diffs, "", "README", "This should be in md format. The output is a replacement of this file and should not have any place holders")
         update_file('README.md', readme_entry)
         
     except Exception as e:
```

This update is aimed at improving the ability to generate more relevant documentation changes and to streamline the update process, making it easier to maintain quality and consistency in project documentation.