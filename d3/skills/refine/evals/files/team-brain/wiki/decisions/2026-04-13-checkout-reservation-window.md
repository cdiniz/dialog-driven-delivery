---
type: decision
aliases: ["checkout reservation window", "10-minute reservation"]
last_updated: 2026-04-17
status: active
---

# Checkout reservation window: 10 minutes

## Decision
- On checkout start, reserve the item for **10 minutes**. If the buyer doesn't complete, release.
- Supersedes the 15-minute value in [2026-03-23 checkout mechanics](2026-03-23-checkout-mechanics.md). All other mechanics (VAT-inclusive pricing, GBP-only, retry policy, confirmation-email handling, guest-style account) are unchanged.

## Rationale
- Single-copy inventory: an abandoned checkout locks a popular title for the full window and blocks other buyers.
- 10 minutes still covers a normal checkout, including a card decline and switch to a second card (~1–2 extra minutes).
- 10 minutes is the agreed floor — don't go lower without revisiting.

## Expired-reservation behaviour
- Unchanged: show "your reservation expired, start again" and send buyer back to the book detail page.

## Sources
- [2026-04-13 Checkout Reservation Follow-up](../summaries/2026-04-13-checkout-reservation-follow-up.md)
