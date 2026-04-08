---
name: uncertainty-markers
description: Standards for marking uncertainties in specifications to prevent AI hallucination. Use when creating or refining specifications to ensure unknowns, assumptions, and pending decisions are explicitly marked rather than silently assumed. Provides four marker types (OPEN QUESTION, DECISION PENDING, ASSUMPTION, CLARIFICATION NEEDED) with usage guidelines and validation checklist.
---

# Uncertainty Marker Standards

Artifacts should be **honest about what is unknown**. The most dangerous failure mode when generating any artifact is silently deciding something that was never discussed — it looks authoritative but is actually hallucinated. When information is missing, ambiguous, or deferred, use inline uncertainty markers to make this explicit.

It is better to mark something as uncertain than to make a plausible but potentially incorrect assumption.

## The Four Markers

### `[OPEN QUESTION: text]`

Use when user input is needed and you cannot proceed without an answer. This captures gaps where you asked but didn't get an answer, or where a critical decision was never discussed.

```markdown
Users authenticate via [OPEN QUESTION: SSO, password-based, or social login?]
```

### `[DECISION PENDING: options]`

Use when multiple valid approaches exist and the decision has been explicitly deferred. List the options being considered so stakeholders can make an informed choice.

```markdown
Task data will be stored in [DECISION PENDING: PostgreSQL vs MongoDB - see Open Questions Q3]
```

### `[ASSUMPTION: statement]`

Use when you make an inference based on context, industry standards, or reasonable deduction — but it hasn't been explicitly validated. Stating assumptions openly lets stakeholders correct wrong inferences before they become embedded in the implementation.

```markdown
We assume [ASSUMPTION: users have stable internet connectivity for real-time features]
```

### `[CLARIFICATION NEEDED: aspect]`

Use when a requirement exists but is vague, ambiguous, or lacks measurable criteria. This prevents hand-wavy requirements from slipping through as if they were well-defined.

```markdown
API response time should be [CLARIFICATION NEEDED: define 'fast' - <1s, <3s, <5s?]
```

## Choosing the Right Marker

The most common mistake is using ASSUMPTION when OPEN QUESTION or CLARIFICATION NEEDED would be more appropriate. The key distinction:

- **ASSUMPTION** is for things *you* are inferring silently — nobody raised the topic, but you need to fill in a gap with a reasonable default. Example: assuming UTC timezone storage when nobody mentioned timezones.
- **OPEN QUESTION** is for things that were *never discussed* or where someone *asked but got no clear answer*. Example: nobody mentioned how users authenticate.
- **CLARIFICATION NEEDED** is for things that *were discussed but left vague, contradictory, or only tentatively accepted*. If a stakeholder expresses concern or the group gives a lukewarm "I think it'll be fine" rather than a firm decision, that's a clarification needed — not an assumption. Example: a stakeholder worries about data quality but the team moves on without a concrete resolution.
- **DECISION PENDING** is for things where the group *explicitly acknowledged* a choice needs to be made and *deferred it*. List the options being considered.

When in doubt between ASSUMPTION and CLARIFICATION NEEDED, prefer CLARIFICATION NEEDED — it's better to surface a concern for stakeholder review than to quietly treat it as settled.

## Usage Guidance

**When to mark:** Contradictory information from different stakeholders, unanswered questions, vague requirements ("fast", "user-friendly"), multiple valid technical approaches, stakeholder concerns that were acknowledged but not fully resolved, and any inference you're making that wasn't explicitly stated.

**When NOT to mark:** Don't mark things that were clearly and firmly decided — that creates noise and undermines trust in the markers. If the transcript or user clearly stated a requirement with confidence, capture it as a firm decision. The purpose of markers is signal, not coverage.

## Tracking Markers

How markers are tracked depends on the artifact type and its template structure:

**Specs (Product & Tech):** Every inline marker needs a corresponding entry in a tracking section — this lets stakeholders scan what needs resolution without reading the entire artifact:
- `[OPEN QUESTION]` and `[CLARIFICATION NEEDED]` → tracked in the **Open Questions** section
- `[ASSUMPTION]` → tracked in the **Assumptions** section
- `[DECISION PENDING]` → tracked in the **Open Questions** section (technical decisions)
- Each tracking entry should include context about why it matters and who should resolve it

**User Stories:** Markers appear inline in acceptance criteria or the description. Stories are small and self-contained, so no separate tracking section is needed — the markers are visible at a glance. If a story has critical uncertainties, flag it with a "needs-clarification" label.

**ADRs:** Markers naturally fit in "Decision Drivers", "Considered Options", or "Consequences" sections. An ADR with too many markers may signal the decision isn't ready to be recorded yet.

**Transcripts:** Markers appear inline when distilled content is ambiguous. No tracking sections — the markers surface ambiguity for downstream artifact creation.

## Examples

### In a Spec

```markdown
## Requirements

* **FR1:** Users can create tasks with title, description, and due date
  - Title: Required, [CLARIFICATION NEEDED: max length? 100 chars, 255 chars, unlimited?]
  - Description: Optional, supports [OPEN QUESTION: plain text only or rich text/Markdown?]
  - Due date: Optional, [ASSUMPTION: timezone handling uses user's local timezone]

* **FR2:** Users can assign tasks to [OPEN QUESTION: single user or multiple users?]
  - Notification sent to assignee via [DECISION PENDING: email, in-app, or both - see Q2]

## Open Questions

**Q1:** Should task description support plain text only or rich text/Markdown?
  - Owner: Product/Engineering
  - Context: Affects editor component selection and data storage

**Q2:** How should we notify assignees - email, in-app, or both?
  - Owner: Product
  - Context: Affects notification service requirements

**Q3:** What is the maximum length for task titles?
  - Owner: Engineering
  - Context: Affects database column definition and UI validation

## Assumptions

1. **Timezone Handling:** Due dates use the user's local timezone. Standard practice for task management apps — needs validation with international users.

2. **Date Validation:** Due dates cannot be set in the past. Prevents data entry errors but needs validation with workflow requirements.
```

### In a User Story

```markdown
### AC2: Checkout payment
- **Given** a user with items in cart
- **When** they click "Pay"
- **Then** payment is processed via [DECISION PENDING: Stripe vs Adyen - see tech spec Q4]
- **And** a confirmation email is sent [ASSUMPTION: within 30 seconds of successful payment]
```

## Summary

| Marker | Use Case | Tracked In | Blocking? |
|--------|----------|------------|-----------|
| `[OPEN QUESTION]` | User decision needed | Open Questions | Yes |
| `[DECISION PENDING]` | Technical choice deferred | Open Questions | Yes |
| `[ASSUMPTION]` | Inference made, needs validation | Assumptions | No, but validate before implementation |
| `[CLARIFICATION NEEDED]` | Vague requirement | Open Questions | Yes |
