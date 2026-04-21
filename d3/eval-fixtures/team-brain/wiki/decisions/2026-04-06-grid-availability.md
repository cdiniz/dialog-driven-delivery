---
type: decision
aliases: ["sold books grid", "reserved books grid", "grid availability"]
last_updated: 2026-04-15
status: active
---

# Catalog grid availability: exclude sold, include reserved

## Decision
On the catalog browse grid:
- **Sold** books are **excluded** from the grid.
- **Reserved** (mid-checkout, 15-min hold) books are **included**. The detail page handles the "currently reserved" state.

## Rationale
- Showing sold books and surfacing "unavailable" only on click is a bad experience. Filtering at query time is also simpler ([Maya](../people/maya.md)).
- Excluding reserved would hide them from other buyers if the reservation expires; including them keeps the catalog discoverable. Detail page must handle the edge case gracefully.

Supersedes the open question parked in [2026-03-23 Backlog Refinement](../summaries/2026-03-23-backlog-refinement.md).

Related: [checkout reservation mechanics](2026-03-23-checkout-mechanics.md).

## Sources
- [2026-04-06 Three Amigos — Catalog Browse](../summaries/2026-04-06-three-amigos-catalog-browse.md)
