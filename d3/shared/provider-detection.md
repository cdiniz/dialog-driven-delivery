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

## Template Configuration Detection

After detecting providers, check for optional template configuration in CLAUDE.md.

### Template Configuration Format

Look for an optional Templates section under `## D3 Configuration`:

```markdown
## D3 Configuration

### Templates (optional)
- Feature Spec: ./custom-templates/feature-spec.md
- Technical Spec: ./custom-templates/technical-spec.md
- User Story: ./custom-templates/user-story.md

### Spec Provider
...
```

### Template Loading Logic

For each template type (Feature Spec, Technical Spec, User Story):

1. **Check for custom path** in Templates section
2. **If custom path found:**
   - Use Read tool to load template from the custom path (relative to project root)
   - If Read fails, show error: "Cannot read template at [path]. Please check the path in CLAUDE.md Templates section."
3. **If no custom path (default behavior):**
   - Use Read tool to load from `d3/templates/[template-name].md`:
     - Feature Spec → `d3/templates/feature-spec.md`
     - Technical Spec → `d3/templates/technical-spec.md`
     - User Story → `d3/templates/user-story.md`
   - If Read fails, show error: "Cannot find default template at d3/templates/[template-name].md"

### Store Template Paths

After loading, store these for use by skills:

```markdown
**Template Configuration:**
- feature_spec_template: [path-used]
- technical_spec_template: [path-used]
- user_story_template: [path-used]
```

Skills will use these paths to load template content when needed.

### Example: Templates Section Present

```markdown
## D3 Configuration

### Templates
- Feature Spec: ./my-templates/custom-feature.md
- Technical Spec: ./my-templates/custom-technical.md
- User Story: ./my-templates/custom-story.md

### Spec Provider
**Skill:** d3-markdown:markdown-spec-provider
...
```

**Result:** Use custom templates from `./my-templates/`

### Example: Templates Section Absent

```markdown
## D3 Configuration

### Spec Provider
**Skill:** d3-markdown:markdown-spec-provider
...
```

**Result:** Use default templates from `d3/templates/`

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
