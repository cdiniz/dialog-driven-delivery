# Project Configuration

## Spec-Driven Development Framework

This project uses a markdown-based approach for feature specifications and user stories.

### Directory Structure

All feature specs and stories are stored in `docs/[feature-name]/`:
- `docs/[feature-name]/spec.md` - Feature specification (Product + Technical)
- `docs/[feature-name]/story-01-*.md` - User story files
- `docs/[feature-name]/story-02-*.md` - User story files
- etc.

### Markdown Constraints

- Use standard markdown format for all specs and stories
- Story files must include YAML frontmatter with required fields: `title`, `status`, `priority`, `tags`, `dependencies`, `blocked_by`, `story_number`
- Status values: `todo`, `in_progress`, `done`, `blocked`
