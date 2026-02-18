---
name: markdown-spec-provider
description: Create and manage specifications as local markdown files. Stores specs in a configurable directory (default ./specs/) as markdown files tracked by git.
---
## What This Does

Manages specifications as markdown files in the filesystem. Specs are stored in `{specs_dir}` directory with git version control.

---

## Configuration

This skill reads configuration from .github/copilot-instructions.md in the current working directory.

**Expected format in .github/copilot-instructions.md:**
```markdown
### Spec Provider
**Skill:** d3-markdown:markdown-spec-provider
**Configuration:**
- Specs Directory: ./specs
```

**Configuration values:**
- **Specs Directory**: Path to the directory containing specification files (default: `./specs`)
- **Default Location**: Default location ID for new specs (default: `.` meaning root)

**Important:** All operations read this configuration at runtime. If .github/copilot-instructions.md is not found or doesn't contain the configuration section, defaults are used

---

## Operations

When invoked with operation in `$ARGUMENTS`:

### list_locations

Lists available directories for specifications.

**Implementation:**
Use search to find directories in {specs_dir}/, or return root location.

**Returns:**
```json
{
  "locations": [
    { "id": ".", "name": "Root", "path": "{specs_dir}" },
    {
      "id": "subdirectory",
      "name": "Subdirectory",
      "path": "{specs_dir}/subdirectory"
    }
  ]
}
```

---

### create_spec

Creates a specification markdown file.

**Parse args:** location_id, title, body, parent_id (optional)

**Implementation:**
1. Sanitize title to filename: lowercase, spaces to hyphens, remove special chars
2. Determine filepath: `{specs_dir}/{location_id}/{filename}.md`
3. Create directory if needed
4. Write body to file using edit tool
5. Return metadata

**Returns:**
```json
{
  "id": "{specs_dir}/user-authentication.md",
  "title": "User Authentication",
  "url": "file:///absolute/path/to/{specs_dir}/user-authentication.md",
  "path": "./{specs_dir}/user-authentication.md"
}
```

---

### get_spec

Retrieves a specification markdown file.

**Parse args:** page_id (can be full path, partial path, or filename)

**Implementation:**
1. Find file using read tool (always scope to specs directory):
   - If page_id starts with `{specs_dir}/`: try exact path
   - Try `{specs_dir}/{page_id}`
   - Try `{specs_dir}/{page_id}.md`
   - Use search pattern `{specs_dir}/**/*{page_id}*.md` as fallback
2. Read file content
3. Extract title from first `# ` heading
4. Get last modified time from file stats
5. Return metadata

**Returns:**
```json
{
  "id": "{specs_dir}/user-authentication.md",
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
2. Write updated body using edit tool
3. If version_message provided and in git repo: commit with message
4. Return metadata

**Returns:**
```json
{
  "id": "{specs_dir}/user-authentication.md",
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
1. Use search to search markdown files in {specs_dir}/ (or specified location)
2. For each match, extract title and excerpt
3. Return list of results

**Returns:**
```json
{
  "results": [
    {
      "id": "{specs_dir}/user-authentication.md",
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

- Titles converted to filenames: "User Auth" -> `user-auth.md`
- Lowercase with hyphens
- Remove special characters (except hyphens)
- All files have `.md` extension

---

## Directory Structure

Example with default `Specs Directory: ./specs`:

```
specs/
  feature-1.md
  feature-2.md
  subdirectory/
    feature-3.md
```

Example with custom `Specs Directory: ./documentation/specs`:

```
documentation/
  specs/
    feature-1.md
    feature-2.md
```

---

## Notes

- Use read/edit tools for file operations
- Use search for finding files
- Use search for searching content
- Git operations via execute (optional, only if version_message provided)
- Always create parent directories as needed
