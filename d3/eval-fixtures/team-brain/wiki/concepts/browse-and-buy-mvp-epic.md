---
type: concept
aliases: ["Browse and Buy MVP", "first epic", "MVP epic"]
last_updated: 2026-04-15
status: active
---

# Browse and Buy MVP (epic)

The first epic on [Pageturner](../projects/pageturner.md). Covers the full v1 buyer journey end-to-end.

## User journey
Land on site → see books → search/filter → click book → see detail → click buy → enter email + delivery address → pay → get confirmation.

## Stories
- **0 — Ingest partner catalog** — data pipeline; dependency for all UI work. Owner: [Maya](../people/maya.md).
- **1 — Home page with book listing** — grid from seeded catalog, no personalisation. Owner: [Maya](../people/maya.md). Refined 2026-03-23. ~3 days.
- **2 — Search and filters** — search box, basic filters (price, condition, author). Risky; needs spike before estimate.
- **3 — Book detail page** — title, author, condition, price, description, images, buy button.
- **4 — Checkout flow** — email + delivery address, price breakdown (fee, shipping), confirm. Refined 2026-03-23. ~1 week. Owner: [Raj](../people/raj.md).
- **5 — Payment integration** — wire existing payments service; depends on story 4.
- **6 — Order confirmation** — confirmation screen + transactional email.

Error/empty/slow-network states live inside each story (not a catch-all).

## Conventions
- Three amigos required before pickup for any story > ~½ day. See [ways of working](../decisions/2026-03-16-ways-of-working.md).

## Sources
- [2026-03-09 Roadmap & First Epic](../summaries/2026-03-09-roadmap-first-epic.md)
- [2026-03-23 Backlog Refinement — Browse & Checkout](../summaries/2026-03-23-backlog-refinement.md)
- [2026-04-06 Three Amigos — Catalog Browse](../summaries/2026-04-06-three-amigos-catalog-browse.md)
