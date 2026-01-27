# Changelog

All notable changes to the D3 project.

## [1.0.0] - 2026-01-25

### Major Changes - Plugin Architecture

#### Added
- **Plugin Structure**: Converted D3 from standalone `.claude` directory to proper Claude Code plugins
- **Two Plugins**:
  - `d3` - Core plugin with main skills and commands
  - `d3-atlassian` - Atlassian provider plugin for Confluence and Jira
- **Plugin Manifests**: Added `plugin.json` for both plugins with proper metadata
- **Plugin READMEs**: Created comprehensive documentation for each plugin
- **Migration Guide**: Added `MIGRATION.md` explaining the transformation
- **Consolidated Documentation**: Merged `README.md` and `SPEC_README.md` into single comprehensive README
- **Implementation Flexibility**: Clarified that D3 focuses on planning/decomposition; implementation method is flexible (superpowers is optional)

#### Changed
- **Command Namespacing**: Commands now use plugin namespace
  - `/create-spec` → `/d3:create-spec`
  - `/refine-spec` → `/d3:refine-spec`
  - `/decompose` → `/d3:decompose`
- **Repository Structure**: Organized into plugin directories
- **Installation Method**: Now installable via `claude plugin install`
- **Documentation**: Updated all examples and references to use namespaced commands

#### Removed
- `.claude/commands/README.md` - Merged into root README.md
- `.claude/commands/SPEC_README.md` - Merged into root README.md
- `brand-guidelines` skill - General-purpose, not D3-specific
- `skill-creator` skill - General-purpose, not D3-specific

#### Preserved
- `.claude/` directory - Kept for reference (deprecated)
- All core functionality - No features removed
- Provider architecture - Enhanced with cleaner separation
- Uncertainty markers - Maintained in core plugin
- Templates - Maintained in core plugin

### Plugin Details

#### d3 Plugin (Core)
**Version**: 1.0.0

**Contains**:
- Commands: `create-spec.md`, `refine-spec.md`, `decompose.md`
- Skills:
  - `create-spec` - Feature specification creation
  - `refine-spec` - Specification refinement
  - `decompose` - Story decomposition
  - `uncertainty-markers` - Standards for marking unknowns
- Templates:
  - `feature-spec.md` - Product specification template
  - `technical-spec.md` - Technical specification template
  - `user-story.md` - User story template
- Configuration: Configured in project's `CLAUDE.md` file

**Skills Provided**:
- `/d3:create-spec` - Create comprehensive feature specifications
- `/d3:refine-spec` - Refine existing specifications
- `/d3:decompose` - Decompose into user stories

#### d3-atlassian Plugin (Provider)
**Version**: 1.0.0

**Contains**:
- Skills:
  - `atlassian-spec-provider` - Confluence integration
  - `atlassian-story-provider` - Jira integration

**Provider Operations**:
- Spec Provider: list_locations, create_spec, get_spec, update_spec, search_specs
- Story Provider: list_projects, get_issue_types, create_epic, create_story, link_issues

### Migration Path

**For Existing Users**:
1. Old `.claude` directory structure still works
2. To migrate: Install plugins and remove old `.claude` directory
3. Update command references to use namespaced versions

**For New Users**:
1. Install `d3` plugin: `claude plugin install d3 --plugin-dir ./d3`
2. Install provider: `claude plugin install d3-atlassian --plugin-dir ./d3-atlassian`
3. Configure in project's `CLAUDE.md` file

### Documentation Updates

- **README.md**: Comprehensive documentation including philosophy, workflow, commands, and examples
- **d3/README.md**: Plugin-specific documentation for core D3
- **d3-atlassian/README.md**: Provider-specific documentation
- **MIGRATION.md**: Detailed migration guide from old to new structure
- **CHANGELOG.md**: This file

### Technical Details

**Plugin Format**: Claude Code Plugin (compliant with official spec)
**Namespacing**: Required for plugin system
**Modularity**: Core and providers can be versioned independently
**Extensibility**: Easy to create providers for other tools

### Future Plans

**Planned Providers**:
- `d3-notion` - Notion provider for specs and stories
- `d3-linear` - Linear provider for story tracking
- `d3-github` - GitHub provider for specs (markdown) and issues

**Planned Features**:
- Plugin marketplace setup
- Automated testing for plugins
- Provider SDK/template
- More templates and examples

### Breaking Changes

⚠️ **Command Names**: All commands now require the `d3:` prefix
- Users must update scripts and documentation
- Old `.claude` structure will continue to work without namespace

⚠️ **Installation Method**: Changed from copying `.claude` directory to plugin installation
- More convenient for users
- Better update mechanism

### Compatibility

- **Claude Code**: Requires version 1.0.33 or later
- **Atlassian MCP**: Required for d3-atlassian provider
- **Git**: Still required for version control
- **Providers**: Modular, install what you need

### Notes

This is the first official plugin release of D3. The previous `.claude` directory structure is deprecated but maintained for backward compatibility. Users are encouraged to migrate to the plugin structure for better maintainability and updates.

---

## Pre-Plugin History

Previous versions used the `.claude` directory structure and are not versioned separately.

**Key Milestones**:
- Initial development of D3 methodology
- Creation of create-spec, refine-spec, decompose skills
- Atlassian provider implementation
- Uncertainty markers system
- Template development
