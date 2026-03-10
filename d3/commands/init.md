---
description: Generate a d3.config.md file in the project root. Asks the user about their storage preferences (local markdown, Atlassian, Linear, or custom backend) and creates the appropriate configuration.
---

## Workflow

### 1. Check for Existing Configuration

Check if `d3.config.md` already exists in the project root.

**If it exists:** Warn the user and ask if they want to overwrite it. Stop if they decline.

### 2. Choose Storage Backend

Ask the user:
```
Where do you want D3 to store artifacts?

A) Local markdown files (simplest — everything in local directories)
B) Atlassian (Confluence for specs/ADRs, Jira for stories)
C) Linear (project documents and issues)
D) Custom (any other MCP or CLI tool — GitHub Issues, Notion, Google Drive, etc.)
```

### 3. Choose Mode

Ask the user:
```
Do you want to enable Quiet Mode?

A) No (default) — D3 commands ask clarifying questions and confirm before creating artifacts
B) Yes — commands skip prompts, infer titles automatically, and apply changes immediately (for automated pipelines or scripted workflows)
```

### 4. Gather Backend-Specific Details

**A) Local markdown:**
No additional questions needed. Use default directories: `./specs/product/`, `./specs/tech/`, `./stories/`, `./adrs/`, `./transcripts/`.

**B) Atlassian:**
Before gathering details, warn the user:
```
⚠ Atlassian integration requires the Atlassian MCP server to be configured.
Make sure `mcp__atlassian` is available before using D3 commands.
See: https://github.com/sooperset/mcp-atlassian
```
Ask for:
- Confluence space key (for specs and ADRs)
- Confluence parent page ID for specs
- Confluence parent page ID for ADRs
- Jira project key (for stories)

**C) Linear:**
Before gathering details, warn the user:
```
⚠ Linear integration requires the Linear MCP server to be configured.
Make sure `mcp__linear` is available before using D3 commands.
See: https://github.com/jerhadf/linear-mcp-server
```
Ask for:
- Linear project name
- Linear team key

**D) Custom:**
Before gathering details, warn the user:
```
⚠ Custom integration requires the corresponding MCP or CLI tool to be available.
Make sure the tool is installed and accessible before using D3 commands.
```
Ask for:
- MCP or CLI tool name (e.g. `mcp__notion`, `mcp__github`, `gh`)
- Location for all artifacts (e.g. project name, repository, folder)

### 5. Copy Templates

**If `.d3/templates/` already exists:** Warn the user and ask if they want to overwrite the templates. If they decline, skip this step and keep existing templates. In quiet mode, always overwrite.

Read each template file from the d3-templates skill's `references/` directory and write it to `.d3/templates/` in the project root, preserving filenames. The skill's references are already available — read them directly, do not search the filesystem for them. Create the `.d3/templates/` directory if it doesn't exist.

### 6. Generate Configuration

Generate `d3.config.md` in the project root using the gathered details.

The file must follow this exact structure:

```markdown
## D3 Configuration

### Settings
- Quiet Mode: false

### Templates
- Product Spec Template: .d3/templates/feature-product-spec.md
- Tech Spec Template: .d3/templates/feature-tech-spec.md
- User Story Template: .d3/templates/user-story.md
- ADR Template: .d3/templates/adr.md
- Meeting Transcript Template: .d3/templates/meeting-transcript.md

### Storage

| Artifact       | Location          | Instructions                    |
|----------------|-------------------|---------------------------------|
| Product Specs  | {location}        | {instructions}                  |
| Tech Specs     | {location}        | {instructions}                  |
| Stories        | {location}        | {instructions}                  |
| ADRs           | {location}        | {instructions}                  |
| Transcripts    | {location}        | {instructions}                  |
```

Fill `{location}` and `{instructions}` based on the chosen backend and details gathered.

### 7. Confirm

Show the generated configuration and the list of copied templates to the user. Write `d3.config.md`.

Report what was created and suggest next steps: `/d3:create` to start creating artifacts. Mention that templates in `.d3/templates/` can be customized. Note that the default config separates Product Specs and Tech Specs into distinct rows — teams can merge them into a single "Specs" row with a combined template if preferred.
