---
name: markdown-story-provider
description: Create and manage user stories as local markdown files organized by feature/spec.
---

## What This Does

Manages user stories as markdown files with YAML frontmatter. Stories are organized in subdirectories by their related feature/spec.

---

## Configuration

```markdown
### Story Provider
**Skill:** d3-markdown:markdown-story-provider
**Configuration:**
- Stories Directory: ./stories
- Story Prefix: story-
```

---

## Operations

### list_projects

Returns single "local" project.

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

Returns Story type only.

**Returns:**
```json
{
  "issue_types": [
    {"id": "story", "name": "Story"}
  ]
}
```

---

### create_story

**Parse args:** project_key, spec_id, story_data (JSON object)

**story_data structure:**
```json
{
  "summary": "User Login",
  "description": "As a user...",
  "acceptance_criteria": "AC1: Given...\nWhen...\nThen...",
  "labels": ["frontend", "backend"]
}
```

**Implementation:**
1. Read or initialize `.d3/metadata.json`
2. Get next story ID (story-1, story-2, etc.)
3. Determine spec directory from spec_id (e.g., "specs/user-authentication.md" → "user-authentication")
4. Sanitize summary to filename
5. Create story markdown file: `stories/{spec_dir}/{story_id}-{filename}.md`
6. File structure:
   ```markdown
   ---
   type: story
   id: story-1
   spec: specs/user-authentication.md
   title: [summary]
   status: todo
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
   - Spec: [../../specs/user-authentication.md]
   ```
7. Update metadata.json:
   - Add story to stories object
   - Increment next_id.story counter
8. Return story metadata

**Returns:**
```json
{
  "id": "story-1",
  "key": "story-1",
  "url": "file:///path/to/stories/user-authentication/story-1-login.md",
  "summary": "User Login",
  "spec_link": "specs/user-authentication.md"
}
```

---

### link_issues (optional)

**Parse args:** from_key, to_key, link_type (blocks, is_blocked_by, relates_to)

**Implementation:**
1. Read metadata.json
2. Update dependency graph based on link_type:
   - `blocks`: from_key blocks to_key
   - `is_blocked_by`: from_key is blocked by to_key
3. Update story frontmatter in both markdown files:
   - Update `blocks: []` array
   - Update `dependencies: []` array
4. Save metadata.json
5. Return success

**Returns:**
```json
{
  "success": true,
  "link_type": "blocks"
}
```

---

## Metadata File

`.d3/metadata.json` structure:

```json
{
  "version": "1.0",
  "next_id": {
    "story": 5
  },
  "stories": {
    "story-1": {
      "id": "story-1",
      "path": "stories/user-authentication/story-1-login.md",
      "title": "User Login",
      "spec": "specs/user-authentication.md",
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

## Directory Structure

Stories are organized by their related feature/spec:

```
stories/
├── user-authentication/
│   ├── story-1-login.md
│   ├── story-2-signup.md
│   └── story-3-password-reset.md
└── search-feature/
    ├── story-4-basic-search.md
    └── story-5-filters.md

.d3/
└── metadata.json
```

---

## File Format Example

### Story File

```markdown
---
type: story
id: story-1
spec: specs/user-authentication.md
title: User Login
status: todo
size: medium
dependencies: []
blocks: []
labels: [backend, frontend]
created: 2026-01-27
---

# Story: User Login

**As a** registered user
**I want** to log in with my credentials
**So that** I can access my account

---

## Acceptance Criteria

**AC1: Successful login**
- **Given** a registered user with valid credentials
- **When** they enter email and password and click login
- **Then** they are redirected to dashboard
- **And** session is created with 24h expiry

**AC2: Invalid credentials**
- **Given** a user enters invalid credentials
- **When** they click login
- **Then** error message is displayed
- **And** login form remains visible

---

## Technical Notes

- Use bcrypt for password hashing
- Implement rate limiting: 5 attempts per 15 minutes
- Session token stored in httpOnly cookie

**References:**
- Spec: [../../specs/user-authentication.md]
```

---

## Notes

- Use Read/Write tools for file operations
- Initialize `.d3/metadata.json` if not exists
- IDs are sequential integers (story-1, story-2, etc.)
- Stories organized in subdirectories by spec/feature name
- Track dependencies in both frontmatter and metadata.json
- Status tracked in frontmatter: `status: todo|in_progress|done`
- Users update status manually by editing file

### Tools to Use
- **Read/Write:** File operations
- **Glob:** Find files
- **Grep:** Search content
- **Bash:** Git operations
