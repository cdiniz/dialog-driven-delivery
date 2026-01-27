---
name: markdown-spec-provider
description: Create and manage specifications as local markdown files. Stores specs in git-tracked markdown files with full version control. Perfect for solo developers and small teams.
---

## What This Does

Handles all specification operations for D3 using local markdown files. Specs are stored in a `specs/` directory and fully version-controlled with git.

---

## Operations

When invoked with operation in `$ARGUMENTS`:

### list_locations

Lists available directories for specifications.

**Returns:** List of locations with id, name, path

**Implementation:**
```bash
# List subdirectories in specs/ or return root
if [ -d "specs" ]; then
  find specs -type d -maxdepth 1 -mindepth 1 -exec basename {} \; | \
    jq -R -s 'split("\n") | map(select(length > 0)) | map({id: ., name: ., path: ("specs/" + .)})'
else
  echo '[{"id": ".", "name": "Root", "path": "./specs"}]' | jq
fi
```

### create_spec

Creates a specification markdown file.

**Parse args:** location_id, title, body, parent_id (optional)

**Implementation:**
```bash
# Sanitize title to filename
filename=$(echo "$title" | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | sed 's/[^a-z0-9-]//g')

# Determine path
if [ "$location_id" = "." ]; then
  filepath="specs/${filename}.md"
else
  filepath="specs/${location_id}/${filename}.md"
  mkdir -p "specs/${location_id}"
fi

# Write content
echo "$body" > "$filepath"

# Return metadata
echo "{
  \"id\": \"$filepath\",
  \"title\": \"$title\",
  \"url\": \"file://$(pwd)/$filepath\",
  \"path\": \"$filepath\"
}" | jq
```

**Returns:** id, title, url, path

### get_spec

Retrieves a specification markdown file.

**Parse args:** page_id (can be full path, partial path, or filename)

**Implementation:**
```bash
# Find file - support multiple formats
if [ -f "$page_id" ]; then
  filepath="$page_id"
elif [ -f "specs/$page_id" ]; then
  filepath="specs/$page_id"
elif [ -f "specs/${page_id}.md" ]; then
  filepath="specs/${page_id}.md"
else
  # Search by partial match
  filepath=$(find specs -name "*${page_id}*.md" 2>/dev/null | head -1)
fi

if [ -z "$filepath" ] || [ ! -f "$filepath" ]; then
  echo "{\"error\": \"Specification not found: $page_id\"}" | jq
  exit 1
fi

# Extract title (first # heading)
title=$(grep -m 1 '^# ' "$filepath" | sed 's/^# //' || basename "$filepath" .md)

# Read full content
body=$(cat "$filepath")

# Get last modified date (works on both Linux and macOS)
if stat -f "%Sm" "$filepath" &>/dev/null; then
  # macOS
  modified=$(stat -f "%Sm" -t "%Y-%m-%d %H:%M:%S" "$filepath")
else
  # Linux
  modified=$(stat -c "%y" "$filepath" | cut -d'.' -f1)
fi

# Determine location
location_id=$(dirname "$filepath" | sed 's|^specs/||' | sed 's|^specs$|.|')

echo "{
  \"id\": \"$filepath\",
  \"title\": \"$title\",
  \"body\": $(echo "$body" | jq -Rs .),
  \"url\": \"file://$(pwd)/$filepath\",
  \"last_modified\": \"$modified\",
  \"location_id\": \"$location_id\"
}" | jq
```

**Returns:** id, title, body, url, last_modified, location_id

### update_spec

Updates a specification markdown file.

**Parse args:** page_id, body, version_message (optional)

**Implementation:**
```bash
# Find file (same logic as get_spec)
if [ -f "$page_id" ]; then
  filepath="$page_id"
elif [ -f "specs/$page_id" ]; then
  filepath="specs/$page_id"
elif [ -f "specs/${page_id}.md" ]; then
  filepath="specs/${page_id}.md"
else
  filepath=$(find specs -name "*${page_id}*.md" 2>/dev/null | head -1)
fi

if [ -z "$filepath" ] || [ ! -f "$filepath" ]; then
  echo "{\"error\": \"Specification not found: $page_id\"}" | jq
  exit 1
fi

# Backup current version
cp "$filepath" "${filepath}.backup"

# Write updated content
echo "$body" > "$filepath"

# Get new modified date
if stat -f "%Sm" "$filepath" &>/dev/null; then
  modified=$(stat -f "%Sm" -t "%Y-%m-%d %H:%M:%S" "$filepath")
else
  modified=$(stat -c "%y" "$filepath" | cut -d'.' -f1)
fi

# Optional: Git commit (if in git repo and version_message provided)
if [ -n "$version_message" ] && [ -d ".git" ]; then
  git add "$filepath" 2>/dev/null
  git commit -m "$version_message" "$filepath" 2>/dev/null || true
  version=$(git log -1 --format=%h "$filepath" 2>/dev/null || echo "local")
else
  version="local"
fi

echo "{
  \"id\": \"$filepath\",
  \"url\": \"file://$(pwd)/$filepath\",
  \"version\": \"$version\",
  \"last_modified\": \"$modified\"
}" | jq
```

**Returns:** id, url, version, last_modified

### search_specs

Searches specifications by content.

**Parse args:** query, location_id (optional)

**Implementation:**
```bash
# Determine search path
if [ -n "$location_id" ] && [ "$location_id" != "." ]; then
  search_path="specs/${location_id}"
else
  search_path="specs"
fi

# Use ripgrep if available, fallback to grep
if command -v rg &> /dev/null; then
  # Ripgrep: fast and modern
  results=$(rg --type md -l --heading "$query" "$search_path" 2>/dev/null)
else
  # Fallback: grep
  results=$(grep -r -l "$query" "$search_path"/*.md 2>/dev/null)
fi

# Format results as JSON array
echo "$results" | while read -r filepath; do
  if [ -n "$filepath" ]; then
    # Get title
    title=$(grep -m 1 '^# ' "$filepath" | sed 's/^# //' || basename "$filepath" .md)

    # Get excerpt (line containing match)
    if command -v rg &> /dev/null; then
      excerpt=$(rg -m 1 --no-heading "$query" "$filepath" 2>/dev/null | head -c 100)
    else
      excerpt=$(grep -m 1 "$query" "$filepath" 2>/dev/null | head -c 100)
    fi

    # Determine location
    location_id=$(dirname "$filepath" | sed 's|^specs/||' | sed 's|^specs$|.|')

    echo "{
      \"id\": \"$filepath\",
      \"title\": \"$title\",
      \"excerpt\": \"$excerpt...\",
      \"url\": \"file://$(pwd)/$filepath\",
      \"location_id\": \"$location_id\"
    }"
  fi
done | jq -s '.'
```

**Returns:** List of matching specs with id, title, excerpt, url, location_id

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

**Default values if not found:**
- Specs Directory: `./specs`
- Default Location: `.` (root)

---

## Notes

### File Naming
- Titles are converted to lowercase-hyphenated filenames
- Example: "User Authentication" → `user-authentication.md`
- Non-alphanumeric characters removed (except hyphens)

### Directory Structure
```
specs/
├── feature-1.md
├── feature-2.md
└── subdirectory/
    └── feature-3.md
```

### Git Integration
- Automatically commits if `version_message` provided
- Creates backup files before updates (`.backup` extension)
- Works with or without git repository

### Search Performance
- Uses `ripgrep` (rg) if available for fast search
- Falls back to standard `grep` if ripgrep not installed
- Searches only markdown files in specs directory

### Error Handling
- Returns JSON error object if file not found
- Creates directories as needed for create operations
- Handles both absolute and relative paths

---

## Example Usage

### Create Specification

```bash
# Via D3 command
/d3:create-spec
> Location: .
> Title: User Authentication
> [Provides body content]

# Skill invocation (internal)
Skill(
  skill="d3-markdown:markdown-spec-provider",
  args='create_spec location_id="." title="User Authentication" body="[markdown content]"'
)

# Result: specs/user-authentication.md created
```

### Get Specification

```bash
# By full path
args='get_spec page_id="specs/user-authentication.md"'

# By partial path
args='get_spec page_id="user-authentication"'

# By search term
args='get_spec page_id="authentication"'
```

### Update Specification

```bash
args='update_spec page_id="user-authentication" body="[updated content]" version_message="Add OAuth section"'

# Result: File updated and committed to git
```

### Search Specifications

```bash
args='search_specs query="OAuth" location_id="."'

# Returns all specs containing "OAuth"
```

---

## Best Practices

### File Organization
- Use subdirectories for different product areas
- Keep spec filenames descriptive and consistent
- Follow project naming conventions

### Version Control
- Commit specs regularly with meaningful messages
- Use branches for major spec updates
- Review spec changes in pull requests

### Maintenance
- Periodically clean up `.backup` files
- Archive old/deprecated specs to `specs/archive/`
- Keep spec directory structure flat when possible

---

## Comparison with Confluence Provider

| Feature | Confluence | Markdown | Notes |
|---------|-----------|----------|-------|
| Storage | Cloud | Local files | Markdown is git-based |
| Collaboration | Excellent | Good | Use PRs for markdown |
| Rich editing | Excellent | Basic | Markdown is simpler |
| Version control | Basic | Full (git) | Markdown has complete history |
| Offline | No | Yes | Markdown works offline |
| Search | Excellent | Good | Both support full-text search |
| Cost | $7-10/user/mo | Free | Markdown has no costs |
| Setup | 30 minutes | 2 minutes | Markdown is instant |

**Use Confluence when:** Enterprise features, rich editing, team collaboration tools needed

**Use Markdown when:** Solo developer, small team, want full git integration, prefer simplicity
