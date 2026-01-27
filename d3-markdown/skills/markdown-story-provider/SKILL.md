---
name: markdown-story-provider
description: Create and manage user stories as local markdown files or GitHub Issues. Supports local mode (markdown files) or github-issues mode (native GitHub Issues via gh CLI).
---

## What This Does

Manages user stories in two modes:
1. **Local Mode:** Stories as markdown files with YAML frontmatter in `./stories/`
2. **GitHub Issues Mode:** Stories as native GitHub Issues via `gh` CLI

---

## Configuration

### Local Mode (Default)

```markdown
### Story Provider
**Skill:** d3-markdown:markdown-story-provider
**Configuration:**
- Mode: local
- Stories Directory: ./stories
- Epic Prefix: epic-
- Story Prefix: story-
```

### GitHub Issues Mode

```markdown
### Story Provider
**Skill:** d3-markdown:markdown-story-provider
**Configuration:**
- Mode: github-issues
- GitHub Repo: username/repository-name
```

---

## Operations

Operations adapt based on configured mode.

### list_projects

**Local Mode:** Return single "local" project

**GitHub Mode:** Query repository using `gh repo view --json`

**Returns:**
```json
{
  "projects": [{
    "id": "local",
    "key": "LOCAL",
    "name": "Local Project",
    "url": "file:///path/to/stories"
  }]
}
```

---

### get_issue_types

**Both Modes:** Return Epic and Story types

**Returns:**
```json
{
  "issue_types": [
    {"id": "epic", "name": "Epic"},
    {"id": "story", "name": "Story"}
  ]
}
```

---

### create_epic

**Parse args:** project_key, summary, description, labels (optional)

**Local Mode Implementation:**
1. Read or initialize `.d3/metadata.json`
2. Get next epic ID from metadata (epic-1, epic-2, etc.)
3. Sanitize summary to filename
4. Create epic markdown file: `stories/epics/{epic_id}-{filename}.md`
5. File structure:
   ```markdown
   ---
   type: epic
   id: epic-1
   title: [summary]
   status: todo
   created: [date]
   labels: [labels]
   ---

   # Epic: [summary]

   [description]

   ## User Stories
   (will be updated as stories created)
   ```
6. Update metadata.json with epic info
7. Increment next_id.epic counter
8. Return epic metadata

**GitHub Mode Implementation:**
1. Use Bash to run: `gh issue create --title "Epic: {summary}" --body "{description}" --label "epic"`
2. Parse output for issue number
3. Return metadata

**Returns:**
```json
{
  "id": "epic-1",
  "key": "epic-1",
  "url": "file:///path/to/stories/epics/epic-1-authentication.md",
  "summary": "User Authentication"
}
```

---

### create_story

**Parse args:** project_key, epic_id, story_data (JSON object)

**story_data structure:**
```json
{
  "summary": "User Login",
  "description": "As a user...",
  "acceptance_criteria": "AC1: Given...\nWhen...\nThen...",
  "labels": ["frontend", "backend"]
}
```

**Local Mode Implementation:**
1. Read metadata.json
2. Get next story ID (story-1, story-2, etc.)
3. Sanitize summary to filename
4. Create story markdown file: `stories/{epic_id}/{story_id}-{filename}.md`
5. File structure:
   ```markdown
   ---
   type: story
   id: story-1
   epic: epic-1
   title: [summary]
   status: todo
   priority: medium
   size: medium
   created: [date]
   dependencies: []
   blocks: []
   labels: [labels]
   ---

   # Story: [summary]

   [description]

   ---

   ## Acceptance Criteria

   [acceptance_criteria]

   ---

   ## Technical Notes

   **References:**
   - Epic: [link to epic]
   ```
6. Update metadata.json:
   - Add story to stories object
   - Add story_id to epic's stories array
   - Increment next_id.story counter
7. Update epic file: Add story to list under "## User Stories"
8. Return story metadata

**GitHub Mode Implementation:**
1. Combine description and acceptance_criteria
2. Add reference to epic: "Part of #{epic_id}"
3. Use Bash: `gh issue create --title "{summary}" --body "{full_body}" --label "user-story" --label "{labels}"`
4. Return metadata

**Returns:**
```json
{
  "id": "story-1",
  "key": "story-1",
  "url": "file:///path/to/stories/epic-1/story-1-login.md",
  "summary": "User Login",
  "epic_link": "epic-1"
}
```

---

### link_issues (optional)

**Parse args:** from_key, to_key, link_type (blocks, is_blocked_by, relates_to)

**Local Mode Implementation:**
1. Read metadata.json
2. Update dependency graph based on link_type:
   - `blocks`: from_key blocks to_key
   - `is_blocked_by`: from_key is blocked by to_key
3. Update story frontmatter in both markdown files:
   - Update `blocks: []` array
   - Update `dependencies: []` array
4. Save metadata.json
5. Return success

**GitHub Mode Implementation:**
1. Add comments to issues referencing each other
2. Use Bash: `gh issue comment #{from_key} --body "Blocks #{to_key}"`
3. Return success (note: GitHub has no native API for issue links)

**Returns:**
```json
{
  "success": true,
  "link_type": "blocks"
}
```

---

## Metadata File

`.d3/metadata.json` structure (Local Mode only):

```json
{
  "version": "1.0",
  "next_id": {
    "epic": 3,
    "story": 8
  },
  "epics": {
    "epic-1": {
      "id": "epic-1",
      "path": "stories/epics/epic-1-authentication.md",
      "title": "User Authentication",
      "status": "in_progress",
      "stories": ["story-1", "story-2", "story-3"],
      "created": "2026-01-27",
      "url": "file:///absolute/path"
    }
  },
  "stories": {
    "story-1": {
      "id": "story-1",
      "path": "stories/epic-1/story-1-login.md",
      "title": "User Login",
      "epic": "epic-1",
      "status": "done",
      "dependencies": [],
      "blocks": ["story-2"],
      "created": "2026-01-27",
      "url": "file:///absolute/path"
    }
  }
}
```

---

## Directory Structure (Local Mode)

```
stories/
├── epics/
│   ├── epic-1-authentication.md
│   └── epic-2-search.md
├── epic-1/
│   ├── story-1-login.md
│   ├── story-2-signup.md
│   └── story-3-password-reset.md
└── epic-2/
    ├── story-4-basic-search.md
    └── story-5-filters.md

.d3/
└── metadata.json
```

---

## File Format Examples

### Epic File

```markdown
---
type: epic
id: epic-1
title: User Authentication
status: todo
created: 2026-01-27
spec: specs/user-authentication.md
labels: [authentication, security]
---

# Epic: User Authentication

[Description]

## User Stories

- [ ] story-1: User Login
- [ ] story-2: User Signup

## Progress

- Total Stories: 2
- Completed: 0
- Todo: 2
```

### Story File

```markdown
---
type: story
id: story-1
epic: epic-1
title: User Login
status: todo
size: medium
dependencies: []
blocks: []
labels: [backend, frontend]
---

# Story: User Login

**As a** registered user
**I want** to log in
**So that** I can access my account

---

## Acceptance Criteria

**AC1:** [Given-When-Then]

---

## Technical Notes

**References:**
- Epic: [../epics/epic-1-authentication.md]
```

---

## Notes

### Local Mode
- Use Read/Write tools for file operations
- Initialize `.d3/metadata.json` if not exists
- IDs are sequential integers (epic-1, story-1, etc.)
- Update epic file when adding stories
- Track dependencies in both frontmatter and metadata.json

### GitHub Issues Mode
- Requires `gh` CLI installed and authenticated
- Use Bash tool to run `gh` commands
- Epic and story types via labels
- Dependencies via issue comments (GitHub has no native link API)
- Issue numbers become IDs (#1, #2, etc.)

### Status Updates
- Status tracked in frontmatter: `status: todo|in_progress|done`
- Users update manually by editing file
- Future: CLI helper for status updates

### Tools to Use
- **Read/Write:** File operations
- **Glob:** Find files
- **Grep:** Search content
- **Bash:** Git operations, gh CLI commands
- **File stats:** Get modification times
