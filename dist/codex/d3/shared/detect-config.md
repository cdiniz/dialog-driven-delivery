# D3 Config Detection

Shared step used by `create-spec`, `refine-spec`, and `decompose`.

## Instructions

- Read `d3.config.md` for D3 config
- Search for `### D3 Config` and `### Templates` sections
- Detect spec mode from provider configuration:
  - If `### Product Spec Provider` AND `### Tech Spec Provider` both exist → **separated mode**. Store each provider's skill and configuration independently.
  - If only `### Spec Provider` exists → **combined mode**. Store single provider config.
- Read `Quiet Mode` from Settings (default: `false` when absent)
- Store detected mode, providers, and quiet mode setting for later steps
