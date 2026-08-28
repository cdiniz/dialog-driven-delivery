# ADR-0001: Use Postgres for the events table

**Date:** 2026-03-15
**Status:** Proposed
**Decision-makers:** Backend team
**Consulted:** Platform team
**Informed:** Product, SRE

---

## Context and Problem Statement

We need to pick a primary store for the new events table that will hold order-lifecycle events (created, paid, fulfilled, refunded). Write volume is expected to peak at ~200 writes/second. Read patterns are still evolving — we will need point lookups by order ID and, in the near future, analytical queries joining events with orders and customers.

## Decision Drivers

* Operational familiarity — on-call and platform teams already run Postgres
* Transactional guarantees for billing-adjacent data
* Ability to join events with existing relational data
* Write throughput must comfortably clear 200 writes/second peak
* Access patterns are still unsettled; we want flexibility

## Considered Options

* Postgres
* DynamoDB

## Decision Outcome

Chosen option: "Postgres", because it satisfies all of the decision drivers at the current scale and preserves query flexibility while the access patterns settle.

### Consequences

_To be confirmed after implementation._

### Confirmation

_To be defined._

## Pros and Cons of the Options

### Postgres

* Good, because the team has deep operational experience
* Good, because transactional support fits billing-adjacent data
* Good, because it allows joining with the existing orders and customers tables
* Good, because projected write volume (~200 writes/sec) is well within Postgres capacity on our current instance class
* Neutral, because schema evolution will need migration discipline
* Bad, because horizontal scaling past a single primary requires additional work (read replicas, partitioning)

### DynamoDB

* Good, because it scales writes horizontally out of the box
* Bad, because the team has no production operational experience with it
* Bad, because cross-table joins with relational data are awkward
* Bad, because the projected scale does not require what DynamoDB offers

## More Information

_To be defined._
