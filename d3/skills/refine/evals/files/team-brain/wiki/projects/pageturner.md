---
type: project
aliases: ["Pageturner"]
last_updated: 2026-04-17
status: active
---

# Pageturner

Marketplace for used books. Positioning: between generic marketplaces and collector-focused niche sites — "feels like walking into a real secondhand bookshop, but online."

## Team
- PM: [Sara](../people/sara.md)
- PO: [Alex](../people/alex.md)
- UX: [Priya](../people/priya.md)
- Tech lead: [Tom](../people/tom.md)
- Devs: [Maya](../people/maya.md), [Raj](../people/raj.md)
- BA: [Ben](../people/ben.md)
- QA: [Lin](../people/lin.md)

## Scope (MVP)
Browse, detail, buy. No seller onboarding, no recommendations, no reviews, no full accounts (email + delivery address only). Catalog seeded from a partner via CSV ingest.

See [MVP scope decision](../decisions/2026-03-02-mvp-scope.md). First epic: [Browse and Buy MVP](../concepts/browse-and-buy-mvp-epic.md).

## Roadmap
Three phases: MVP → "sellers lite" (small partner sellers + accounts) → personalisation/trust (reviews, recommendations). See [roadmap decision](../decisions/2026-03-09-roadmap-three-phases.md).

## Ways of working
Two-week sprints, three amigos for any story > ½ day, QA in from refinement. See [ways of working](../decisions/2026-03-16-ways-of-working.md).

## Tech
Standard company stack: React frontend, Postgres, services on usual framework. Integrate existing payments service. See [tech stack decision](../decisions/2026-03-02-tech-stack.md).

## Business model
Platform fee on each transaction: **8% of sale price + £1.50 flat**, shipping shown as a separate line. See [fee structure](../decisions/2026-03-09-fee-structure.md).

## Timeline (rough, uncommitted)
- MVP internally usable: ~3 months from kickoff
- Beta: ~1 month after internal
- Firming up in roadmap session

## Known risks
- Search quality: book metadata is messy (title variants, editions, author spelling). Spike planned.

## Sources
- [2026-03-02 Kickoff](../summaries/2026-03-02-pageturner-kickoff.md)
- [2026-03-09 Roadmap & First Epic](../summaries/2026-03-09-roadmap-first-epic.md)
- [2026-03-16 Team Ceremonies](../summaries/2026-03-16-team-ceremonies.md)
- [2026-03-23 Backlog Refinement](../summaries/2026-03-23-backlog-refinement.md)
- [2026-04-06 Three Amigos — Catalog Browse](../summaries/2026-04-06-three-amigos-catalog-browse.md)
- [2026-04-13 Checkout Reservation Follow-up](../summaries/2026-04-13-checkout-reservation-follow-up.md)
