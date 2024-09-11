# ChatGPT-Test-Integration
ChatGPT-Test-Integration

This repo contins a test api.
it also has github actions for chatgpt to do a code review and to generate changelogs automatically.

api doc: tbd

# Update Log for README

## Recent Changes

### Added More Specific Prompts

- **Modifications Made**:
  - Updated the `generate_update_content` function to include an `additional_prompt` parameter. This allows for more tailored prompts when generating updates for the changelog and README files.
  - The README update process now specifies that the output should be in markdown format and serve as a complete replacement for the existing file with no placeholders.

### Code Snippet

```python
def generate_update_content(pr_details, pr_diffs, existing_content, update_type, additional_prompt):
    prompt = (f"Generate an update for the {update_type} based on the following:\n"
              f"Title: {pr_details.title}\n"
              f"Body: {pr_details.body}\n"
              f"Differences:\n{pr_diffs}\n"
              f"Existing Content:\n{existing_content}\n"
              f"Additional Prompt:\n{additional_prompt}\n")
```

### Implications

- The changes improve the clarity and specificity of updates generated for the README, enhancing the overall documentation quality.
- The additional prompt in the README generation ensures consistency and removes unnecessary placeholders, resulting in a cleaner documentation output.

### Testing

- Ensure the updates function correctly by running the relevant features and verifying that the generated README meets the specified requirements.

For further details, please refer to the project documentation or contact the development team.