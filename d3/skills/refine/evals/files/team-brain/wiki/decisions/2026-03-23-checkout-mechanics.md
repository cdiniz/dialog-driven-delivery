---
type: decision
aliases: ["checkout reservation", "VAT", "currency"]
last_updated: 2026-04-17
status: active
---

# Checkout mechanics: reservation, VAT, currency, retry

## Decisions
- **Reservation:** on checkout start, reserve the item for ~~15 minutes~~ **10 minutes** (superseded 2026-04-13 — see [reservation window decision](2026-04-13-checkout-reservation-window.md)). If buyer doesn't complete, release.
- **Reservation expired mid-checkout:** show "your reservation expired, start again" and dump back to the book detail page.
- **VAT:** inclusive — listed price *is* the price (UK norm). Fee percentage is on the inclusive price.
- **Currency:** GBP only in v1.
- **Payment failure:** retry on same page, up to **3 attempts**, then show support contact and exit. Payments service handles retry semantics; we surface results.
- **Confirmation email failure** (after payment success): log + alert + retry. Do **not** roll back the payment. User still sees the confirmation screen.
- **Account:** guest-style (email + delivery address). Email stored in order record. No marketing without consent.

## Sources
- [2026-03-23 Backlog Refinement](../summaries/2026-03-23-backlog-refinement.md)
- [2026-04-13 Checkout Reservation Follow-up](../summaries/2026-04-13-checkout-reservation-follow-up.md)
