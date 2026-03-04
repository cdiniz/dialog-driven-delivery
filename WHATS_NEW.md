# What's New in D3

## Config schema overhaul

The configuration format has changed from markdown (`d3.config.md`) to YAML (`d3.config.yaml`) with a flatter, cleaner structure.

### Before (old format)

```yaml
artifacts:
  product_spec:
    adapter: markdown
    config:
      directory: ./specs
  tech_spec:
    adapter: confluence
    config:
      base_url: https://yoursite.atlassian.net
      email: you@example.com
      space_key: PROJ
      parent_page_id: "123456789"

templates:
  product_spec: ./templates/custom-product-spec.md
  tech_spec: ./templates/custom-tech-spec.md

settings:
  quiet_mode: false
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

1. **Rename** `d3.config.md` to `d3.config.yaml` (if still using the markdown format)
2. **Remove nested `config:` blocks** — move adapter-specific fields (`directory`, `location_id`, `mode`) directly under each artifact
3. **Move shared connection details** (`base_url`, `email`, `space_key`) into a top-level `adapters:` section
4. **Move templates into artifacts** — replace the separate `templates:` section with a `template:` field on each artifact that needs a custom template
5. **Rename `parent_page_id`** to `location_id` on Confluence artifacts
6. **Remove `api_token_env`** — the Confluence adapter now reads `CONFLUENCE_API_TOKEN` from the environment directly. Add it to a `.env` file in your project root if needed

### Quick reference

| Old | New |
|-----|-----|
| `config:` block under artifact | Fields directly under artifact |
| `templates:` top-level section | `template:` field per artifact |
| `parent_page_id` | `location_id` |
| `api_token_env: MY_VAR` | Set `CONFLUENCE_API_TOKEN` env var |
| Connection details per artifact | Shared `adapters:` section |
