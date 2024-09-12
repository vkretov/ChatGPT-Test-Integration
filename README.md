# ChatGPT-Test-Integration
ChatGPT-Test-Integration

This repo contins a test api.
it also has github actions for chatgpt to do a code review and to generate changelogs automatically.

api doc: tbd

# Update for README

## Changes Made

### .github/actions/generate_and_update_changelog.py

- **Changelog Entry Update**: Modified the `changelog_entry` generation to include a specific summary of changes, providing clearer insights into the updates being documented.
  
- **README Entry Update**: Enhanced the `readme_entry` generation prompt to specify that the content should only include changes relevant to the API project. This ensures that any updates to the API documentation are reflected accurately.

### Details of the Updates

The following updates were made to improve the specificity of the prompts used in the changelog and README generation:

```python
-        changelog_entry = generate_update_content(pr_details, pr_diffs, "", "changelog", "")
+        changelog_entry = generate_update_content(pr_details, pr_diffs, "", "changelog", "This should be a brief summary of the changes.")
-        readme_entry = generate_update_content(pr_details, pr_diffs, "", "README", "This should be in md format. The output is a replacement of this file and should not have any place holders")
+        readme_entry = generate_update_content(pr_details, pr_diffs, "", "README", "This should be in md format. The output is a replacement of this file and should not have any place holders. this should only include changes to the api project. It needs to update the api docs when changed.")
```

These updates aim to enhance clarity and understanding of the documentation changes, ensuring they meet the specific requirements related to the API project.