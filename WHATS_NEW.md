# What's New in D3

## Config schema overhaul

The configuration format has changed from markdown (`d3.config.md`) to YAML (`d3.config.yaml`) with a flatter, cleaner structure.

### Before (old format — `d3.config.md`)

```markdown
## D3 Configuration

### Settings
- Quiet Mode: false

### Spec Provider
**Skill:** d3-markdown:markdown-spec-provider
**Configuration:**
- Specs Directory: ./specs

### Story Provider
**Skill:** d3-markdown:markdown-story-provider
**Configuration:**
- Stories Directory: ./stories

### Transcript Provider
**Skill:** d3-markdown:markdown-transcript-provider
**Configuration:**
- Transcripts Directory: ./transcripts

### Templates
- feature_spec_template: ./templates/custom-product-spec.md
- technical_spec_template: ./templates/custom-tech-spec.md
```

### After (new format)

```yaml
adapters:
  confluence:
    base_url: https://yoursite.atlassian.net
    email: you@example.com
    space_key: PROJ

artifacts:
  product_spec:
    adapter: markdown
    directory: ./specs
    template: ./templates/custom-product-spec.md
  tech_spec:
    adapter: confluence
    location_id: "123456789"
    template: ./templates/custom-tech-spec.md

settings:
  quiet_mode: false
```

### Migration checklist

1. **Rename** `d3.config.md` → `d3.config.yaml` and convert to YAML syntax
2. **Map provider sections** (`### Spec Provider`, `### Story Provider`, etc.) → `artifacts:` entries with artifact type keys (`product_spec`, `user_story`, etc.)
3. **Map `**Skill:**` values** → `adapter:` field (`d3-markdown:markdown-spec-provider` → `adapter: markdown`, `d3-atlassian:atlassian-spec-provider` → `adapter: confluence`)
4. **Map `**Configuration:**` bullet points** → flat YAML fields under each artifact (`Specs Directory: ./specs` → `directory: ./specs`)
5. **Extract shared Atlassian connection details** (Cloud ID, space key, etc.) into a top-level `adapters.confluence:` section
6. **Map `Default parent page`** (URL) → `location_id` (page ID only)
7. **Add `template:` field** per artifact if using custom templates (replaces the `### Templates` section)

### Quick reference

| Old (markdown) | New (YAML) |
|---|---|
| `### Spec Provider` section | `product_spec:` under `artifacts:` |
| `**Skill:** d3-markdown:...` | `adapter: markdown` |
| `**Configuration:**` bullet list | Flat YAML fields under artifact |
| `### Templates` section | `template:` field per artifact |
| `Default parent page: <URL>` | `location_id: "<page-id>"` |
| Connection details per provider | Shared `adapters:` section |
