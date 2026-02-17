---
name: atlassian-story-provider
description: Create and manage user stories in Jira using Atlassian MCP tools.
---

## What This Does

Handles all Jira operations for D3 user stories. Uses Atlassian MCP server to create epics, stories, and manage issues.

## Operations

When invoked with operation in `$ARGUMENTS`:

### list_projects
Lists available Jira projects where user can create issues.

**MCP:** `mcp__atlassian__getVisibleJiraProjects` with action: "create"
**Returns:** List of projects with id, key, name, url

### get_issue_types
Gets available issue types for a project.

**Parse args:** project_key
**MCP:** `mcp__atlassian__getJiraProjectIssueTypesMetadata`
**Returns:** List of issue types (Epic, Story, Task, etc.)

### create_epic
Creates an Epic in Jira.

**Parse args:** project_key, summary, description, labels (optional)
**MCP:** `mcp__atlassian__createJiraIssue` with issueTypeName: "Epic"
**Returns:** id, key, url, summary

### create_story
Creates a user story in Jira.

**Parse args:** project_key, epic_id, story_data (JSON with summary, description, acceptance_criteria, labels, etc.)
**Combines:** description + acceptance_criteria into one description field
**MCP:** `mcp__atlassian__createJiraIssue` with issueTypeName: "Story"
**Links to Epic:** Uses Epic Link field
**Returns:** id, key, url, summary, epic_link

### list_stories
Lists all stories/tasks under an epic matching a spec title.

**Parse args:** spec_title
**Steps:**
1. Search for epic: `mcp__atlassian__searchJiraIssuesUsingJql` with JQL `project = [PROJECT] AND issuetype = Epic AND summary ~ "[spec_title]"`
2. If epic found, fetch all child issues: `mcp__atlassian__searchJiraIssuesUsingJql` with JQL `parent = [EPIC-KEY] ORDER BY key ASC` (no issuetype filter — children may be Story, Task, or other types)
3. For each child issue, fetch full details including description
**Returns:** epic key, list of child issues with key, summary, status, description

### update_story
Updates an existing story/task description and fields.

**Parse args:** issue_key, description (optional), summary (optional)
**MCP:** `mcp__atlassian__editJiraIssue` with fields to update
**Returns:** key, url, summary

### link_issues (optional)
Creates dependency links between issues.

**Parse args:** from_key, to_key, link_type (blocks, is_blocked_by, relates_to)
**MCP:** Jira issue link API (if available)
**Returns:** link_id or error if not supported

## Configuration

Reads from `CLAUDE.md`:
- Cloud ID
- Default Project (project key)

## Notes

- Descriptions use Markdown format
- Epic linking uses Jira's Epic Link custom field
- Story points, priority, assignee are optional fields
- Labels are created automatically if they don't exist
