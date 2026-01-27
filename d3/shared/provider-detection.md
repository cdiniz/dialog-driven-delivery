# Provider Detection

This guide explains how to detect and configure D3 providers from the project's CLAUDE.md file.

## Quick Reference

Read D3 Configuration from `CLAUDE.md`. Extract provider names or use defaults:
- **Spec Provider:** `d3-atlassian:atlassian-spec-provider`
- **Story Provider:** `d3-atlassian:atlassian-story-provider`

## Detection Steps

1. Read `CLAUDE.md` file
2. Look for "## D3 Configuration" section
3. Extract provider names from:
   - Spec Provider: Line starting with `**Skill:**`
   - Story Provider: Line starting with `**Skill:**`
4. If not found, use defaults above

## Configuration Not Found

If configuration is missing or incomplete, show this guidance to the user:

```markdown
⚠️ D3 Configuration Not Found

I couldn't find D3 provider configuration in CLAUDE.md.

Please add this to your CLAUDE.md file:

## D3 Configuration

### Spec Provider
**Skill:** d3-atlassian:atlassian-spec-provider
**Configuration:**
- Cloud ID: your-atlassian-cloud-id
- Default Location: YOUR-SPACE-KEY
- Default parent page: (optional) parent-page-url

### Story Provider
**Skill:** d3-atlassian:atlassian-story-provider
**Configuration:**
- Cloud ID: your-atlassian-cloud-id
- Default Project: YOUR-PROJECT-KEY

---

**How to find your Cloud ID:**
Visit your Atlassian site and check the URL or use the Atlassian MCP tools.

**Other providers available:**
- Notion, Linear, GitHub, or create your own custom provider

See README.md for full details and alternative provider options.
```

Then stop and wait for the user to update their configuration.

## Usage in Skills

In your skill, reference this guide:

```markdown
### Step 0: Detect Provider

Detect provider configuration. See [provider-detection.md](../../shared/provider-detection.md) for details.

Store provider name(s) for later use.
```

## Example CLAUDE.md Configuration

```markdown
## D3 Configuration

### Spec Provider
**Skill:** d3-atlassian:atlassian-spec-provider
**Configuration:**
- Cloud ID: 1234567890abcdef
- Default Location: PROJ
- spaceId: 98765432

### Story Provider
**Skill:** d3-atlassian:atlassian-story-provider
**Configuration:**
- Cloud ID: 1234567890abcdef
- Default Project: PROJ
```
