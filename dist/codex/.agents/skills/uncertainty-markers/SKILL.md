---
name: uncertainty-markers
description: Standards for marking uncertainties in specifications to prevent AI hallucination. Use when creating or refining specifications to ensure unknowns, assumptions, and pending decisions are explicitly marked rather than silently assumed. Provides four marker types (OPEN QUESTION, DECISION PENDING, ASSUMPTION, CLARIFICATION NEEDED) with usage guidelines and validation checklist.
---
# Uncertainty Marker Standards

**Version:** 1.0
**Purpose:** Prevent AI hallucination and make ambiguities explicit in specifications

## Philosophy

Specifications should be **honest about what is unknown**. When information is missing, ambiguous, or deferred, we use inline uncertainty markers to make this explicit. This prevents assumptions from being silently embedded in specifications and ensures stakeholders know what needs resolution.

**Key Principle:** It is better to mark something as uncertain than to make a plausible but potentially incorrect assumption.

## The Four Uncertainty Markers

### 1. `[OPEN QUESTION: text]`

**When to use:** User input is needed and cannot proceed without an answer.

**Example:**
```markdown
Users authenticate via [OPEN QUESTION: SSO, password-based, or social login?]
```

**Guidelines:**
- Use when you asked the user but didn't get an answer
- The question should be specific and actionable
- Must have corresponding entry in "Open Questions" section

**Template:**
```markdown
[OPEN QUESTION: specific question requiring user decision]
```

### 2. `[DECISION PENDING: options]`

**When to use:** Multiple valid technical approaches exist, and the decision has been explicitly deferred.

**Example:**
```markdown
Task data will be stored in [DECISION PENDING: PostgreSQL vs MongoDB - see Open Questions Q3]
```

**Guidelines:**
- Use when user acknowledges decision is needed but wants to defer it
- List the options being considered
- Reference the Open Question number for traceability
- Typically used in technical specs, not feature specs

**Template:**
```markdown
[DECISION PENDING: option A vs option B vs option C - see Open Questions QX]
```

### 3. `[ASSUMPTION: statement]`

**When to use:** You are making an assumption based on context, industry standards, or reasonable inference, but it needs validation.

**Example:**
```markdown
We assume [ASSUMPTION: users have stable internet connectivity for real-time features]
```

**Guidelines:**
- Use when you infer something reasonable but it wasn't explicitly stated
- State the assumption clearly and completely
- Must have corresponding entry in "Assumptions" section
- User should validate all assumptions before implementation

**Template:**
```markdown
[ASSUMPTION: clear statement of what is being assumed and why]
```

### 4. `[CLARIFICATION NEEDED: aspect]`

**When to use:** A requirement exists but is vague, ambiguous, or lacks measurable criteria.

**Example:**
```markdown
API response time should be [CLARIFICATION NEEDED: define 'fast' - <1s, <3s, <5s?]
```

**Guidelines:**
- Use when requirement is mentioned but lacks specificity
- Suggest what needs to be clarified (numbers, thresholds, exact behavior)
- Often appears in non-functional requirements
- Must have corresponding entry in "Open Questions" section

**Template:**
```markdown
[CLARIFICATION NEEDED: what specifically needs to be defined or measured]
```

## When to Use Uncertainty Markers

### ✅ DO Use Markers When:

1. **User doesn't answer your clarifying questions**
   - You asked but user skipped the question
   - Mark it explicitly rather than assuming

2. **Information is contradictory**
   - Meeting transcript shows disagreement
   - Different stakeholders said different things

3. **Requirement is vague**
   - "Fast response time" → `[CLARIFICATION NEEDED: define threshold]`
   - "User-friendly interface" → `[CLARIFICATION NEEDED: specific usability criteria]`

4. **Multiple valid approaches exist**
   - Technical decision not yet made
   - Business rule has edge cases not discussed

5. **You make a reasonable inference**
   - Common industry practice applied
   - Standard assumed based on context

### ❌ DON'T Use Markers When:

1. **Information was explicitly provided**
   - User clearly stated the requirement
   - Transcript contains the decision

2. **It's obvious from context**
   - Feature spec says "user authentication" and later mentions "login page"
   - Don't mark "login page" as assumption

3. **It's a template placeholder**
   - During draft stages, use normal placeholders
   - Add markers only in final spec generation

## Linking Markers to Open Questions

**Every uncertainty marker must be tracked in the appropriate section:**

### For `[OPEN QUESTION]` and `[CLARIFICATION NEEDED]`:

Add to **Open Questions** section:

```markdown
## Open Questions

### Needs Answer Before Implementation
**Q1:** Which authentication method should we use?
  - Owner: Product/Engineering
  - Needed by: Before technical design
  - Context: Referenced in authentication requirement
  - Options: SSO, password-based, social login
```

### For `[ASSUMPTION]`:

Add to **Assumptions** section:

```markdown
### Assumptions We're Making

1. **Internet Connectivity:** We assume users have stable internet connectivity for real-time features. This affects sync strategy and offline mode requirements.

2. **Browser Support:** We assume modern browsers (Chrome 90+, Firefox 88+, Safari 14+) based on typical user base. Needs validation with analytics.
```

### For `[DECISION PENDING]`:

Add to **Open Questions** section (technical specs):

```markdown
**Q3:** Should we use PostgreSQL or MongoDB for task storage?
  - Owner: Engineering
  - Context: Affects data model design and query patterns
  - Options:
    - PostgreSQL: Better for relational data, ACID guarantees
    - MongoDB: Better for flexible schemas, horizontal scaling
```

## Validation Checklist

Before finalizing any specification, run this checklist:

### Uncertainty Marker Validation

- [ ] **Count inline markers:** How many `[OPEN QUESTION]`, `[DECISION PENDING]`, `[ASSUMPTION]`, `[CLARIFICATION NEEDED]` exist?
- [ ] **All markers have tracking:** Every inline marker has corresponding entry in Open Questions or Assumptions section
- [ ] **Markers are specific:** Each marker clearly states what is unknown or assumed
- [ ] **No silent assumptions:** If you inferred something, it's marked with `[ASSUMPTION]`
- [ ] **User awareness:** User has been notified of all uncertainties and can choose to resolve or defer

## Examples in Context

### Example 1: Feature Spec with Uncertainty

```markdown
## Requirements

### Core Functionality

* **FR1:** Users can create tasks with title, description, and due date
  - Title: Required, [CLARIFICATION NEEDED: max length? 100 chars, 255 chars, unlimited?]
  - Description: Optional, supports [OPEN QUESTION: plain text only or rich text/Markdown?]
  - Due date: Optional, [ASSUMPTION: timezone handling uses user's local timezone]

* **FR2:** Users can assign tasks to [OPEN QUESTION: single user or multiple users?]
  - Assignees must be [ASSUMPTION: project members only, not external users]
  - Notification sent to assignee via [DECISION PENDING: email, in-app, or both - see Q2]

### Validation Rules

* **VR1:** Title - Required field, error: "Title is required"
  - Max length: [CLARIFICATION NEEDED: define max length]

* **VR2:** Due date - Must be [ASSUMPTION: today or future date, not past dates]
```

**Corresponding Open Questions:**

```markdown
## Open Questions

### Needs Answer Before Implementation

**Q1:** Should task description support plain text only or rich text/Markdown?
  - Context: Affects editor component selection and data storage
  - Referenced in: FR1

**Q2:** How should we notify assignees - email, in-app, or both?
  - Context: Affects notification service requirements
  - Referenced in: FR2

**Q3:** What is the maximum length for task titles?
  - Context: Affects database column definition and UI validation
  - Referenced in: FR1, VR1
```

**Corresponding Assumptions:**

```markdown
### Assumptions We're Making

1. **Timezone Handling:** We assume due dates use the user's local timezone. This is standard practice for task management apps. Needs validation with international users.

2. **Assignee Scope:** We assume only project members can be assigned tasks, not external users. This simplifies permission management but needs validation with use cases.

3. **Date Validation:** We assume due dates cannot be set in the past. This prevents data entry errors but needs validation with workflow requirements.
```

### Example 2: Technical Spec with Uncertainty

```markdown
## Data Models

### Task Entity

```typescript
interface Task {
  id: string;
  title: string; // Max length: [CLARIFICATION NEEDED: define based on FR1]
  description?: string; // [DECISION PENDING: string vs rich text object - see Q1]
  dueDate?: Date; // [ASSUMPTION: stored as UTC, displayed in user timezone]
  assigneeId: string | string[]; // [OPEN QUESTION: single or multiple - see Q2]
  status: TaskStatus;
  createdAt: Date;
  updatedAt: Date;
}
```

## API Contracts

### POST /api/tasks

**Request:**
```json
{
  "title": "string", // [CLARIFICATION NEEDED: max length validation]
  "description": "string", // [DECISION PENDING: format - plain vs markdown]
  "dueDate": "ISO8601", // Optional
  "assigneeId": "string" // [OPEN QUESTION: or array of strings?]
}
```

**Response:**
- Success: 201 Created
- Validation Error: 400 Bad Request
- [DECISION PENDING: Should we return 422 Unprocessable Entity for business rule violations?]
```

## Anti-Patterns: What NOT to Do

### ❌ Silent Assumption (BAD)

```markdown
* **FR1:** Users authenticate via OAuth2 using Google provider
```

**Problem:** User never mentioned OAuth2 or Google. This is a hallucination.

### ✅ Marked Uncertainty (GOOD)

```markdown
* **FR1:** Users authenticate via [OPEN QUESTION: OAuth2, password, or social login?]
  - If OAuth2: [OPEN QUESTION: which providers - Google, GitHub, Microsoft?]
```

---

### ❌ Vague Placeholder (BAD)

```markdown
* **NFR1:** API response time should be fast
```

**Problem:** "Fast" is meaningless without definition.

### ✅ Explicit Clarification (GOOD)

```markdown
* **NFR1:** API response time should be [CLARIFICATION NEEDED: define threshold - <500ms, <1s, <3s?]
```

---

### ❌ Unmarked Inference (BAD)

```markdown
* **FR3:** Users can filter tasks by status (Open, In Progress, Completed)
```

**Problem:** User said "filter by status" but never specified which statuses exist.

### ✅ Marked Assumption (GOOD)

```markdown
* **FR3:** Users can filter tasks by status
  - Statuses: [ASSUMPTION: Open, In Progress, Completed - validate with workflow requirements]
```

## Summary

| Marker | Use Case | Tracked In | Blocking? |
|--------|----------|------------|-----------|
| `[OPEN QUESTION]` | User decision needed | Open Questions | Yes - resolve before implementation |
| `[DECISION PENDING]` | Technical choice deferred | Open Questions | Yes - resolve during technical planning |
| `[ASSUMPTION]` | Inference made, needs validation | Assumptions | No - but validate before implementation |
| `[CLARIFICATION NEEDED]` | Vague requirement | Open Questions | Yes - clarify before implementation |

**Golden Rule:** When in doubt, mark it. Better to ask than to assume incorrectly.
