---
type: decision
aliases: ["catalog grid", "browse pagination"]
last_updated: 2026-04-15
status: active
---

# Catalog browse: grid + pagination + newest-first

## Decision
For the catalog browse story in the [Browse and Buy MVP epic](../concepts/browse-and-buy-mvp-epic.md):

- **Grid view only** (no list view in v1). 4 cols desktop / 2 tablet / 1 mobile.
- **Pagination, 20 per page**, classic numbered pager. Page reflected in URL (deep-linkable, back-button friendly).
- **Newest-first** default sort, secondary sort by ID (deterministic on bulk-ingest tie).
- No user-facing sort options in v1.
- Tile content: cover image, title (truncate 2 lines), author (truncate 1 line), price, condition.
- Missing image → placeholder. Broken image at runtime → swap to placeholder onerror. Loading → skeleton tile. Above-fold eager, below-fold lazy.

## Rationale
Pagination beat infinite scroll on testability, cacheability, and deep-linkability — over [Maya](../people/maya.md)'s preference for infinite scroll.

## Sources
- [2026-03-23 Backlog Refinement](../summaries/2026-03-23-backlog-refinement.md)
- [2026-04-06 Three Amigos — Catalog Browse](../summaries/2026-04-06-three-amigos-catalog-browse.md)
