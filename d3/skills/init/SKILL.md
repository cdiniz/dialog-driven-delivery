---
name: init
description: Bootstrap a D3 project by generating d3.config.md and copying default templates into .d3/templates/. Use whenever the user wants to set up D3, initialize D3 in a new repo, configure storage for D3 artifacts (local markdown, Atlassian/Confluence+Jira, Linear, or any custom backend), or says things like "d3 init", "set up d3 here", "configure d3", or asks where D3 will store specs/stories/ADRs. This is the entry point for every D3 project — other D3 skills (create, refine, decompose, align-spec, distill) depend on d3.config.md existing.
---

# D3 — Initialize Project

This skill bootstraps a D3 project: it generates `d3.config.md` at the repo root and copies the default artifact templates into `.d3/templates/`. Every other D3 skill reads `d3.config.md` to figure out where and how to store artifacts, so this is the first thing to run in a new project.

## Core idea

D3 is storage-agnostic. It doesn't hardcode Confluence or Jira or Notion — instead, a single table in `d3.config.md` tells every D3 skill *where* each artifact type lives and *how* to write it. This skill builds that table from a short interview, then copies the default templates into a location the user can customize.

## Workflow

### 1. Check for existing configuration

Check if `d3.config.md` already exists at the repo root.

- **If it exists:** show the current Storage table and ask whether the user wants to overwrite, edit in place, or abort. Default to aborting if unclear — overwriting a working config is costly.

### 2. Choose storage backend

Ask the user where D3 should store artifacts. The four common choices:

- **A) Local markdown files** — simplest. Everything goes in local directories under the repo. Great for solo work, open-source projects, or teams that want artifacts in version control alongside the code.
- **B) Atlassian** — Confluence for specs and ADRs, Jira for stories. Needs the `mcp__atlassian` MCP server.
- **C) Linear** — Linear project documents for specs/ADRs and Linear issues for stories. Needs the `mcp__linear` MCP server.
- **D) Custom** — any other tool (Notion, GitHub Issues, Google Drive, a bespoke CLI). Needs the corresponding MCP server or CLI on the user's path.

If the user already mentioned a backend in their request, skip the question and confirm briefly instead.

### 3. Ask about Quiet Mode

Quiet mode turns off D3's conversational prompts — titles are inferred, clarifying questions are skipped, and changes are applied immediately. It's for automated pipelines; interactive use should stay conversational.

Default: **false**. Only flip it on if the user explicitly asks for automation, scripted pipelines, or "no prompts".

### 4. Gather backend-specific details

**A) Local markdown:** no extra questions. Use these defaults:
- Product Specs → `./specs/product/`
- Tech Specs → `./specs/tech/`
- Stories → `./stories/`
- ADRs → `./adrs/`
- Transcripts → `./transcripts/`

**B) Atlassian:** before asking, warn:
```
Atlassian integration needs the Atlassian MCP server configured.
Make sure mcp__atlassian is available before using D3 skills.
See: https://github.com/sooperset/mcp-atlassian
```
Then ask for:
- Confluence space key (for specs and ADRs)
- Confluence parent page ID for specs
- Confluence parent page ID for ADRs
- Jira project key (for stories)

**C) Linear:** warn about the `mcp__linear` dependency, then ask for:
- Linear project name
- Linear team key

**D) Custom:** warn that the corresponding tool must be installed, then ask for:
- MCP or CLI tool name (e.g. `mcp__notion`, `mcp__github`, `gh`)
- Location for artifacts (project name, repository, folder, etc.)

Only ask the questions that are actually needed for the chosen backend — don't interview for fields that won't end up in the config.

### 5. Copy default templates

This skill bundles the canonical default templates in its own `references/` directory. Read them directly from there — don't search the filesystem or assume a path, just use the skill's `references/` subdirectory.

Copy each template file into `.d3/templates/` in the project root, preserving the filenames:

- `feature-product-spec.md`
- `feature-tech-spec.md`
- `user-story.md`
- `adr.md`
- `meeting-transcript.md`

Create `.d3/templates/` if it doesn't exist.

**If `.d3/templates/` already exists:** warn the user and ask whether to overwrite. If they decline, keep the existing templates. In quiet mode, always overwrite — the user opted into non-interactive behaviour.

### 6. Generate the configuration file

Write `d3.config.md` at the repo root using this exact structure:

```markdown
## D3 Configuration

### Settings
- Quiet Mode: false

### Storage

| Artifact       | Location          | Instructions                    | Template                                  |
|----------------|-------------------|---------------------------------|-------------------------------------------|
| Product Specs  | {location}        | {instructions}                  | .d3/templates/feature-product-spec.md     |
| Tech Specs     | {location}        | {instructions}                  | .d3/templates/feature-tech-spec.md        |
| Stories        | {location}        | {instructions}                  | .d3/templates/user-story.md               |
| ADRs           | {location}        | {instructions}                  | .d3/templates/adr.md                      |
| Transcripts    | {location}        | {instructions}                  | .d3/templates/meeting-transcript.md       |
```

Fill `{location}` and `{instructions}` based on the backend:

- **Local markdown** — Location is the default directory path from step 4. Instructions: `Write as markdown file. Filename from title in kebab-case.`
- **Atlassian** — Location is the Confluence space/parent page (for specs/ADRs) or Jira project key (for stories). Instructions reference the `mcp__atlassian` tool explicitly, e.g. `Create Confluence page under parent {pageId} using mcp__atlassian__createConfluencePage.`
- **Linear / custom** — analogous, referencing the relevant MCP server or CLI tool.

The Instructions column is read literally by other D3 skills, so it needs to be actionable — it should name the tool to use and any parameters that matter.

### 7. Confirm and write

Show the user the generated configuration and the list of templates that were copied. In non-quiet mode, confirm before writing. In quiet mode, write directly.

### 8. Report what happened

Tell the user:
- Which file was created (`d3.config.md`)
- Where templates were placed (`.d3/templates/`)
- Which D3 skills are now unlocked (create, refine, decompose, align-spec, distill)
- That templates can be customized in `.d3/templates/`
- That the default config separates Product Specs and Tech Specs into two rows — teams can merge them into a single "Specs" row with a combined template if they prefer

## Design notes

- The default config has **five** storage rows, not one catch-all. Forcing a single row hides the fact that specs, stories, ADRs, and transcripts often live in different systems (e.g., specs in Confluence, stories in Jira).
- Separating Product Specs and Tech Specs by default matches how most teams already write them — the Product Owner drafts the product spec, engineering drafts the tech spec. Teams that prefer one combined spec can merge the rows; it's easier to merge than to split.
- The `.d3/templates/` location is intentional: it's under the repo so templates can be version-controlled with the code, but under a dot-directory so it stays out of the main file listing.
- The Instructions column matters more than it looks. Other D3 skills read it verbatim and follow it, so it needs to be a *directive* ("Create a Confluence page using mcp__atlassian__createConfluencePage with parentId=12345"), not a description ("We store specs in Confluence").
