# D3 Atlassian Provider Plugin

Atlassian provider for D3 (Dialog Driven Delivery). Enables D3 to work with Confluence for specifications and Jira for user stories.

## What is This?

This plugin provides provider skills that allow D3 to:
- Create and manage specifications in **Confluence**
- Create and manage user stories in **Jira**
- Link specifications to stories bidirectionally

## Installation

```bash
# First, install the core D3 plugin
claude plugin install d3

# Then install this Atlassian provider
claude plugin install d3-atlassian
```

## Prerequisites

- **Confluence** workspace with appropriate permissions
- **Jira** project with appropriate permissions
- **Atlassian MCP Server** configured in Claude Code

## Configuration

Add this to your project's `CLAUDE.md` file:

```markdown
## D3 Configuration

### Spec Provider
**Skill:** d3-atlassian:atlassian-spec-provider
**Configuration:**
- Cloud ID: your-cloud-id
- Default Location: PROJ
- spaceId: 1234567
- Default parent page: https://yoursite.atlassian.net/wiki/spaces/PROJ/pages/123456

### Story Provider
**Skill:** d3-atlassian:atlassian-story-provider
**Configuration:**
- Cloud ID: your-cloud-id
- Default Project: PROJ
```

If configuration is not found, D3 will prompt you with setup instructions.

## How It Works

When you run D3 commands (`/d3:create-spec`, `/d3:refine-spec`, `/d3:decompose`), the core D3 skills automatically detect and invoke the Atlassian provider skills:

### Provider Skills Included

#### atlassian-spec-provider
Manages specifications in Confluence:
- `list_locations()` - List available Confluence spaces
- `create_spec()` - Create specification page
- `get_spec()` - Retrieve specification
- `update_spec()` - Update specification
- `search_specs()` - Search specifications

#### atlassian-story-provider
Manages user stories in Jira:
- `list_projects()` - List available Jira projects
- `get_issue_types()` - Get available issue types
- `create_epic()` - Create Epic for feature
- `create_story()` - Create user story
- `link_issues()` - Create dependencies (blocks/is blocked by)

## What Gets Created

### In Confluence
- Feature specification pages with both Product and Technical specs
- Organized in your configured space
- Can be nested under parent pages
- Full markdown support with automatic conversion

### In Jira
- Epic for each feature (linked to Confluence spec)
- User stories under the Epic
- Complete acceptance criteria in Gherkin format
- Story dependencies via issue links
- Proper labels and organization

## Finding Your Cloud ID

Use the Atlassian MCP tool:
```bash
# In Claude Code
mcp__atlassian__getAccessibleAtlassianResources
```

Or extract from any Atlassian URL:
- `https://your-domain.atlassian.net/...` → Cloud ID is for `your-domain`

## Troubleshooting

### "Cloud ID not found"
- Verify Atlassian MCP Server is configured
- Check you have access to the workspace
- Use `getAccessibleAtlassianResources` to list available Cloud IDs

### "Space not found"
- Ensure the space key is correct (case-sensitive)
- Verify you have permissions in that space
- Try using space ID instead of space key

### "Project not found"
- Check the project key is correct
- Verify you have create permissions in that project
- Ensure project exists and is accessible

### "Page creation fails"
- Check parent page ID is valid (if specified)
- Verify space permissions
- Ensure you're not hitting Confluence limits

## Provider Interface

This plugin implements the D3 provider interface. To create providers for other tools (Notion, Linear, GitHub, etc.), see the [provider documentation](https://github.com/cdiniz/dialog-driven-delivery#creating-custom-providers).

## Support

- **Issues:** [GitHub Issues](https://github.com/cdiniz/dialog-driven-delivery/issues)
- **D3 Documentation:** See main D3 plugin README
- **Atlassian MCP:** [Atlassian MCP Documentation](https://github.com/modelcontextprotocol/servers)

## License

MIT
