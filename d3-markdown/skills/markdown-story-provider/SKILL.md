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
1. Determine spec directory from spec_id (e.g., "specs/user-authentication.md" → "user-authentication")
2. Use Glob to find existing stories in that directory to determine next ID
3. Sanitize summary to filename
4. Create story markdown file: `stories/{spec_dir}/{story_id}-{filename}.md`
5. File structure:
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
6. Return story metadata

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
1. Use Glob to find story files by ID
2. Read both story files
3. Update frontmatter based on link_type:
   - `blocks`: Add to_key to from_key's blocks array
   - `is_blocked_by`: Add to_key to from_key's dependencies array
4. Write updated files
5. Return success

**Returns:**
```json
{
  "success": true,
  "link_type": "blocks"
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
    ├── story-1-basic-search.md
    └── story-2-filters.md
```

---

## File Format Example

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

- No metadata file needed - all data lives in markdown frontmatter
- Use Glob to find stories: `stories/**/story-*.md`
- Use Grep to search by status: `rg "^status: todo"`
- Story IDs determined by counting existing files in directory
- Users update status by editing frontmatter directly
- Dependencies tracked in frontmatter arrays

### Tools to Use
- **Read/Write:** File operations
- **Glob:** Find story files
- **Grep:** Search by status, labels, dependencies
- **Bash:** Git operations
