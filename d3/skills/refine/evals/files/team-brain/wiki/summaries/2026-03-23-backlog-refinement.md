---
type: summary
last_updated: 2026-04-15
---

# Pageturner Backlog Refinement — Catalog Browse & Checkout

## TL;DR
- Refined two stories in the [Browse and Buy MVP epic](../concepts/browse-and-buy-mvp-epic.md): catalog browse (~3d, [Maya](../people/maya.md)) and checkout (~1 week, [Raj](../people/raj.md)).
- Browse: pagination 20/page, newest-first sort, grid-only.
- Checkout: fee display "Option B" (each line broken out); 15-minute reservation; VAT-inclusive prices; GBP only.

## Key points

### Catalog browse
- Responsive grid: 4 desktop / 2 tablet / 1 mobile. Tile = image, title, author, price, condition.
- **Pagination over infinite scroll** — easier to test/cache/link ([Raj](../people/raj.md) + [Lin](../people/lin.md) over [Maya](../people/maya.md)'s push for infinite).
- Default sort newest-first; sort options *not* user-controllable in v1.
- Filters live on same page but are a separate story.
- Long titles truncate (2 lines title / 1 line author). Missing/broken images → placeholder.
- Open question parked for three amigos: should sold books be removed from the grid entirely? → resolved at [2026-04-06 three amigos](2026-04-06-three-amigos-catalog-browse.md): yes.

### Checkout
- Fee breakdown: **Option B** — item, platform fee (8%), flat fee (£1.50), shipping, total. Transparency wins; revisit if it hurts conversion in beta.
- VAT-**inclusive** prices (UK norm). Listed price = price; fee % is on inclusive price.
- **GBP only** in v1.
- Reserve item for **15 minutes** on checkout start. Expired reservation → "start again" message back to detail page.
- Payment failures: retry on same page, up to 3 attempts, then support contact.
- Guest-style: email + delivery address only, no password. Email stored in order; no marketing without consent.
- Confirmation: screen + transactional email (existing service). If email fails post-payment: log/alert/retry, **don't** roll back payment.

## Decisions
- [Catalog browse: pagination, sort, grid](../decisions/2026-03-23-catalog-browse-grid.md)
- [Checkout fee display: Option B (broken-out lines)](../decisions/2026-03-23-checkout-fee-display.md)
- [Checkout mechanics: 15-min reservation, VAT-inclusive, GBP, retry policy](../decisions/2026-03-23-checkout-mechanics.md)

## Action items
- [ ] [Ben](../people/ben.md): schedule three amigos for browse + checkout with [Lin](../people/lin.md) and the picker-up
- [ ] [Alex](../people/alex.md): plan beta user test for checkout fee display

## Entities mentioned
- People: [Alex](../people/alex.md), [Tom](../people/tom.md), [Priya](../people/priya.md), [Maya](../people/maya.md), [Raj](../people/raj.md), [Ben](../people/ben.md), [Lin](../people/lin.md)
- Projects: [Pageturner](../projects/pageturner.md)
- Concepts: [Browse and Buy MVP epic](../concepts/browse-and-buy-mvp-epic.md)

## Source
[raw](../../raw/meetings/2026-03-23-backlog-refinement.md)
