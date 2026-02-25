# D3 Provider Dispatch Convention

Defines how skills route operations to spec providers depending on the detected mode.

## Modes

**Combined mode** — a single `### Spec Provider` is configured. All spec operations go through one provider.

**Separated mode** — both `### Product Spec Provider` and `### Tech Spec Provider` are configured. Product and technical content live in separate documents.

## Title Suffix Convention (Separated Mode)

Specs created in separated mode use a consistent title suffix:

- Product spec: `[Feature Title] - Product Spec`
- Tech spec: `[Feature Title] - Tech Spec`

To derive the companion title, swap the suffix: `"Product Spec" ↔ "Tech Spec"`.

## Fetching Specs

- **Combined:** Use the single spec provider's `get_spec` with the given identifier.
- **Separated:** Detect whether the identifier refers to a product or tech spec (from title suffix, filename, or content). Use the matching provider's `get_spec`. Fetch the companion from the other provider via `search_specs` or `get_spec` only when needed.

## Creating Specs

- **Combined:** Single `create_spec` call with the full unified document.
- **Separated:** Split the content into two documents — product sections from the product template, technical sections from the tech template. Invoke each provider's `create_spec` with the appropriate suffix in the title.

## Updating Specs

- **Combined:** Single `update_spec` call with the full updated document.
- **Separated:** Invoke `update_spec` only for providers whose spec was affected. Skip the companion if its content was unchanged.
