---
name: markdown-spec-provider
description: Create and manage specifications as local markdown files. Stores specs in ./specs/ directory as markdown files tracked by git.
---

## What This Does

Manages specifications as markdown files in the filesystem. Specs are stored in `./specs/` directory with git version control.

---

## Configuration

Reads from `CLAUDE.md`:
```markdown
### Spec Provider
**Skill:** d3-markdown:markdown-spec-provider
**Configuration:**
- Specs Directory: ./specs
- Default Location: .
```

**Defaults if not found:**
- Specs Directory: `./specs`
- Default Location: `.` (root)

---

## Operations

When invoked with operation in `$ARGUMENTS`:

### list_locations

Lists available directories for specifications.

**Implementation:**
Use Glob to find directories in specs/, or return root location.

**Returns:**
```json
{
  "locations": [
    {"id": ".", "name": "Root", "path": "./specs"},
    {"id": "subdirectory", "name": "Subdirectory", "path": "./specs/subdirectory"}
  ]
}
```

---

### create_spec

Creates a specification markdown file.

**Parse args:** location_id, title, body, parent_id (optional)

**Implementation:**
1. Sanitize title to filename: lowercase, spaces to hyphens, remove special chars
2. Determine filepath: `specs/{location_id}/{filename}.md`
3. Create directory if needed
4. Write body to file using Write tool
5. Return metadata

**Returns:**
```json
{
  "id": "specs/user-authentication.md",
  "title": "User Authentication",
  "url": "file:///absolute/path/to/specs/user-authentication.md",
  "path": "./specs/user-authentication.md"
}
```

---

### get_spec

Retrieves a specification markdown file.

**Parse args:** page_id (can be full path, partial path, or filename)

**Implementation:**
1. Find file using Read tool:
   - Try exact path
   - Try `specs/{page_id}`
   - Try `specs/{page_id}.md`
   - Use Glob pattern `specs/**/*{page_id}*.md` as fallback
2. Read file content
3. Extract title from first `# ` heading
4. Get last modified time from file stats
5. Return metadata

**Returns:**
```json
{
  "id": "specs/user-authentication.md",
  "title": "User Authentication",
  "body": "[full markdown content]",
  "url": "file:///absolute/path",
  "last_modified": "2026-01-27 10:30:00",
  "location_id": "."
}
```

---

### update_spec

Updates a specification markdown file.

**Parse args:** page_id, body, version_message (optional)

**Implementation:**
1. Find file (same logic as get_spec)
2. Backup current version to `.backup` file
3. Write updated body using Write tool
4. If version_message provided and in git repo: commit with message
5. Return metadata

**Returns:**
```json
{
  "id": "specs/user-authentication.md",
  "url": "file:///absolute/path",
  "version": "abc123f",
  "last_modified": "2026-01-27 12:00:00"
}
```

---

### search_specs

Searches specifications by content.

**Parse args:** query, location_id (optional)

**Implementation:**
1. Use Grep to search markdown files in specs/ (or specified location)
2. For each match, extract title and excerpt
3. Return list of results

**Returns:**
```json
{
  "results": [
    {
      "id": "specs/user-authentication.md",
      "title": "User Authentication",
      "excerpt": "...OAuth2 authentication...",
      "url": "file:///absolute/path",
      "location_id": "."
    }
  ]
}
```

---

## File Naming

- Titles converted to filenames: "User Auth" → `user-auth.md`
- Lowercase with hyphens
- Remove special characters (except hyphens)
- All files have `.md` extension

---

## Directory Structure

```
specs/
├── feature-1.md
├── feature-2.md
└── subdirectory/
    └── feature-3.md
```

---

## Notes

- Use Read/Write tools for file operations
- Use Glob for finding files
- Use Grep for searching content
- Git operations via Bash (optional, only if version_message provided)
- Always create parent directories as needed
- Backup files before updates
