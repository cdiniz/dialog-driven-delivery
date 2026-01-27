---
name: markdown-story-provider
description: Create and manage user stories as local markdown files or GitHub Issues. Supports two modes - local (markdown files with frontmatter) or github-issues (native GitHub Issues via gh CLI). Perfect for solo developers and teams.
---

## What This Does

Handles all user story operations for D3. Two modes available:
1. **Local Mode:** Stories as markdown files with YAML frontmatter
2. **GitHub Issues Mode:** Stories as native GitHub Issues

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

All operations adapt based on configured mode.

### list_projects

**Local Mode:** Returns single "local" project

**GitHub Mode:** Returns repository info from `gh repo view`

**Implementation (Local):**
```bash
echo '{
  "projects": [{
    "id": "local",
    "key": "LOCAL",
    "name": "Local Project",
    "url": "file://'"$(pwd)/stories"'"
  }]
}' | jq
```

**Implementation (GitHub):**
```bash
gh repo view --json nameWithOwner,name,url | jq '{
  projects: [{
    id: .nameWithOwner,
    key: (.nameWithOwner | split("/")[1] | ascii_upcase),
    name: .name,
    url: .url
  }]
}'
```

### get_issue_types

**Local Mode:** Returns Epic and Story types

**GitHub Mode:** Returns GitHub label-based types

**Implementation (Local):**
```bash
echo '{
  "issue_types": [
    {"id": "epic", "name": "Epic"},
    {"id": "story", "name": "Story"}
  ]
}' | jq
```

**Implementation (GitHub):**
```bash
echo '{
  "issue_types": [
    {"id": "epic", "name": "Epic"},
    {"id": "story", "name": "Story"},
    {"id": "task", "name": "Task"}
  ]
}' | jq
```

### create_epic

**Parse args:** project_key, summary, description, labels (optional)

**Local Mode Implementation:**
```bash
# Load or initialize metadata
if [ ! -f ".d3/metadata.json" ]; then
  mkdir -p .d3
  echo '{"version": "1.0", "epics": {}, "stories": {}, "next_id": {"epic": 1, "story": 1}}' > .d3/metadata.json
fi

# Get next epic ID
next_id=$(jq -r '.next_id.epic' .d3/metadata.json)
epic_id="epic-${next_id}"

# Sanitize summary for filename
filename=$(echo "$summary" | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | sed 's/[^a-z0-9-]//g')
filepath="stories/epics/${epic_id}-${filename}.md"

# Create epics directory
mkdir -p stories/epics

# Create epic markdown file
cat > "$filepath" << EOF
---
type: epic
id: $epic_id
title: $summary
status: todo
created: $(date +%Y-%m-%d)
spec: ${spec_link:-}
labels: [${labels:-epic}]
---

# Epic: $summary

$description

## User Stories

This Epic contains 0 user stories (will be updated as stories are created).

## Progress

- Total Stories: 0
- Completed: 0
- In Progress: 0
- Todo: 0
EOF

# Update metadata
jq --arg id "$epic_id" \
   --arg path "$filepath" \
   --arg title "$summary" \
   --arg created "$(date +%Y-%m-%d)" \
   '.epics[$id] = {
     id: $id,
     path: $path,
     title: $title,
     status: "todo",
     stories: [],
     created: $created,
     url: ("file://'"$(pwd)"'/" + $path)
   } | .next_id.epic = (.next_id.epic + 1)' \
   .d3/metadata.json > .d3/metadata.json.tmp && \
   mv .d3/metadata.json.tmp .d3/metadata.json

# Return epic metadata
jq -r --arg id "$epic_id" '.epics[$id] | {
  id,
  key: .id,
  url,
  summary: .title
}' .d3/metadata.json
```

**GitHub Mode Implementation:**
```bash
# Create GitHub issue with epic label
result=$(gh issue create \
  --title "Epic: $summary" \
  --body "$description" \
  --label "epic" \
  --label "${labels}" \
  --json number,url,title)

# Format as provider response
echo "$result" | jq '{
  id: (.number | tostring),
  key: ("#" + (.number | tostring)),
  url,
  summary: .title
}'
```

### create_story

**Parse args:** project_key, epic_id, story_data (JSON with summary, description, acceptance_criteria, labels, etc.)

**Local Mode Implementation:**
```bash
# Parse story_data JSON
summary=$(echo "$story_data" | jq -r '.summary')
description=$(echo "$story_data" | jq -r '.description')
acceptance_criteria=$(echo "$story_data" | jq -r '.acceptance_criteria // ""')
labels=$(echo "$story_data" | jq -r '.labels // [] | join(", ")')

# Get next story ID
next_id=$(jq -r '.next_id.story' .d3/metadata.json)
story_id="story-${next_id}"

# Sanitize summary for filename
filename=$(echo "$summary" | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | sed 's/[^a-z0-9-]//g')

# Create epic subdirectory
mkdir -p "stories/${epic_id}"
filepath="stories/${epic_id}/${story_id}-${filename}.md"

# Combine description and acceptance criteria
full_description="$description

---

## Acceptance Criteria

$acceptance_criteria"

# Create story markdown file
cat > "$filepath" << EOF
---
type: story
id: $story_id
epic: $epic_id
title: $summary
status: todo
priority: medium
size: medium
created: $(date +%Y-%m-%d)
dependencies: []
blocks: []
labels: [${labels}]
---

# Story: $summary

$full_description

---

## Technical Notes

[To be filled during implementation]

**References:**
- Epic: [$(jq -r --arg id "$epic_id" '.epics[$id].title' .d3/metadata.json)](../epics/${epic_id}*.md)

---

## Progress

- [ ] Implementation started
- [ ] Tests written
- [ ] Code reviewed
- [ ] Merged
EOF

# Update metadata
jq --arg story_id "$story_id" \
   --arg epic_id "$epic_id" \
   --arg path "$filepath" \
   --arg title "$summary" \
   --arg created "$(date +%Y-%m-%d)" \
   '.stories[$story_id] = {
     id: $story_id,
     path: $path,
     title: $title,
     epic: $epic_id,
     status: "todo",
     dependencies: [],
     blocks: [],
     created: $created,
     url: ("file://'"$(pwd)"'/" + $path)
   } | .epics[$epic_id].stories += [$story_id] | .next_id.story = (.next_id.story + 1)' \
   .d3/metadata.json > .d3/metadata.json.tmp && \
   mv .d3/metadata.json.tmp .d3/metadata.json

# Update epic file with story reference
epic_file=$(find stories/epics -name "${epic_id}*.md" | head -1)
if [ -n "$epic_file" ]; then
  # Add story to epic's list (update markdown)
  sed -i.backup "/## User Stories/a\\
- [ ] ${story_id}: $summary" "$epic_file"

  # Update story count
  story_count=$(jq -r --arg id "$epic_id" '.epics[$id].stories | length' .d3/metadata.json)
  sed -i.backup "s/Total Stories: [0-9]*/Total Stories: $story_count/" "$epic_file"
  sed -i.backup "s/Todo: [0-9]*/Todo: $story_count/" "$epic_file"
fi

# Return story metadata
jq -r --arg id "$story_id" '.stories[$id] | {
  id,
  key: .id,
  url,
  summary: .title,
  epic_link: .epic
}' .d3/metadata.json
```

**GitHub Mode Implementation:**
```bash
# Parse story data
summary=$(echo "$story_data" | jq -r '.summary')
description=$(echo "$story_data" | jq -r '.description')
acceptance_criteria=$(echo "$story_data" | jq -r '.acceptance_criteria // ""')
labels=$(echo "$story_data" | jq -r '.labels // [] | join(",")')

# Combine description and acceptance criteria
full_body="$description

## Acceptance Criteria

$acceptance_criteria

---

Part of #${epic_id}"

# Create GitHub issue
result=$(gh issue create \
  --title "$summary" \
  --body "$full_body" \
  --label "user-story" \
  --label "$labels" \
  --json number,url,title)

# Format response
echo "$result" | jq --arg epic "$epic_id" '{
  id: (.number | tostring),
  key: ("#" + (.number | tostring)),
  url,
  summary: .title,
  epic_link: $epic
}'
```

### link_issues (optional)

**Parse args:** from_key, to_key, link_type (blocks, is_blocked_by, relates_to)

**Local Mode Implementation:**
```bash
# Update metadata dependency graph
case "$link_type" in
  "blocks")
    # from_key blocks to_key
    jq --arg from "$from_key" \
       --arg to "$to_key" \
       '.stories[$from].blocks += [$to] | .stories[$to].dependencies += [$from]' \
       .d3/metadata.json > .d3/metadata.json.tmp && \
       mv .d3/metadata.json.tmp .d3/metadata.json

    # Update story frontmatter
    from_file=$(jq -r --arg id "$from_key" '.stories[$id].path' .d3/metadata.json)
    to_file=$(jq -r --arg id "$to_key" '.stories[$id].path' .d3/metadata.json)

    # Add to blocks array in from_file
    sed -i.backup "/^blocks:/s/\[\]/[$to_key]/" "$from_file"
    # Add to dependencies array in to_file
    sed -i.backup "/^dependencies:/s/\[\]/[$from_key]/" "$to_file"
    ;;
  "is_blocked_by")
    # Inverse of blocks
    jq --arg from "$from_key" \
       --arg to "$to_key" \
       '.stories[$from].dependencies += [$to] | .stories[$to].blocks += [$from]' \
       .d3/metadata.json > .d3/metadata.json.tmp && \
       mv .d3/metadata.json.tmp .d3/metadata.json
    ;;
esac

echo '{"success": true, "link_type": "'"$link_type"'"}' | jq
```

**GitHub Mode Implementation:**
```bash
# GitHub doesn't have native issue linking API
# Use issue references in comments instead

from_issue="#${from_key}"
to_issue="#${to_key}"

case "$link_type" in
  "blocks")
    gh issue comment "$from_issue" --body "Blocks $to_issue"
    gh issue comment "$to_issue" --body "Blocked by $from_issue"
    ;;
  "is_blocked_by")
    gh issue comment "$from_issue" --body "Blocked by $to_issue"
    gh issue comment "$to_issue" --body "Blocks $from_issue"
    ;;
  "relates_to")
    gh issue comment "$from_issue" --body "Related to $to_issue"
    gh issue comment "$to_issue" --body "Related to $from_issue"
    ;;
esac

echo '{"success": true, "link_type": "'"$link_type"'", "note": "Added as comments"}' | jq
```

---

## Metadata Management

### Metadata File Structure

`.d3/metadata.json`:
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
      "spec": "specs/authentication.md",
      "created": "2026-01-27",
      "url": "file:///path/to/stories/epics/epic-1-authentication.md"
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
      "blocks": ["story-2", "story-3"],
      "created": "2026-01-27",
      "completed": "2026-01-29",
      "url": "file:///path/to/stories/epic-1/story-1-login.md"
    }
  }
}
```

---

## Notes

### File Structure (Local Mode)

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
```

### ID Generation (Local Mode)
- Epic IDs: `epic-1`, `epic-2`, etc. (sequential)
- Story IDs: `story-1`, `story-2`, etc. (sequential across all epics)
- IDs tracked in `.d3/metadata.json`

### GitHub Issues Mode
- Epic: GitHub issue with "epic" label
- Story: GitHub issue with "user-story" label
- Dependencies: Referenced in issue comments (no native API)
- IDs: GitHub issue numbers (#1, #2, etc.)

### Git Integration (Local Mode)
- Markdown files are git-tracked
- Metadata file is git-tracked
- Automatic backup files created (`.backup` extension)
- Supports manual git operations

### Status Updates (Local Mode)
- Update frontmatter manually: `status: todo → status: in_progress`
- Metadata syncs when file is read
- Future: CLI helper for status updates

---

## Best Practices

### Local Mode
1. **Regular commits:** Commit specs and stories together
2. **Branch strategy:** Use branches for different epics
3. **Code review:** Review stories in PRs before implementation
4. **Metadata backups:** Backup `.d3/metadata.json` regularly
5. **Status discipline:** Keep frontmatter status updated

### GitHub Issues Mode
1. **Use labels:** Epic, user-story, bug, enhancement
2. **Use milestones:** Group stories by sprint/release
3. **Use projects:** Kanban board for story tracking
4. **Reference issues:** Use #N syntax for cross-references
5. **Templates:** Create issue templates for stories

---

## Troubleshooting

### Local Mode

**Problem:** Metadata out of sync
```bash
# Rebuild metadata from markdown files
find stories -name "*.md" -exec grep -H "^id:" {} \; | \
  jq -R 'split(":") | {(.[1]): {path: .[0]}}' | jq -s 'add'
```

**Problem:** Story IDs conflict
```bash
# Edit .d3/metadata.json manually to fix IDs
# Or regenerate with sequential IDs
```

**Problem:** Can't find epic or story
```bash
# Search by content
rg "title: User Login" stories/

# List all stories
find stories -name "story-*.md"
```

### GitHub Issues Mode

**Problem:** gh CLI not installed
```bash
# Install gh CLI
brew install gh  # macOS
# Or see: https://cli.github.com/
```

**Problem:** Not authenticated
```bash
gh auth login
```

**Problem:** Wrong repository
```bash
# Check current repo
gh repo view

# Set in configuration
```

---

## Migration Between Modes

### Local to GitHub Issues
```bash
# For each story in metadata.json:
# 1. Create GitHub issue with gh CLI
# 2. Map local ID to GitHub issue number
# 3. Update references
```

### GitHub Issues to Local
```bash
# For each GitHub issue:
# 1. Download issue content with gh CLI
# 2. Convert to markdown file with frontmatter
# 3. Update metadata.json
```

---

## Future Enhancements

- [ ] CLI tool for status updates: `d3 story update story-1 --status done`
- [ ] Sync between local and GitHub modes
- [ ] Story board HTML generator
- [ ] Burndown charts from metadata
- [ ] Dependency visualization
- [ ] Automated metadata repair
- [ ] Story templates with custom fields

---

## Comparison

| Feature | Local Mode | GitHub Issues |
|---------|-----------|---------------|
| Storage | Markdown files | GitHub Issues |
| Offline | Yes | No |
| Git history | Full | Limited |
| Collaboration | Via PRs | Native GitHub |
| UI | Terminal/Editor | GitHub UI |
| Notifications | None | GitHub notifications |
| Search | grep/rg | GitHub search |
| Free | Yes | Yes (public repos) |
| Setup | 2 minutes | 5 minutes |

**Use Local Mode when:** Solo developer, want full git integration, prefer files

**Use GitHub Issues when:** Team collaboration, want GitHub UI, open source project
