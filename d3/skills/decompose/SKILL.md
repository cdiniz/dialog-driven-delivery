---
name: decompose
description: Break a feature specification into INVEST-compliant user stories — Independent, Negotiable, Valuable, Estimable, Small, Testable — with Given-When-Then acceptance criteria. Reads the spec from d3.config.md's Storage table, proposes workflow-based full-stack stories by default, validates each against INVEST before creating, and writes stories to the configured Stories location (creating a parent epic first if the backend supports epics). Use whenever the user wants to decompose/break/split a feature spec into stories, plan work from a spec, turn a spec into tickets, create an epic and stories for a feature, or says things like "break this feature into stories", "decompose the spec", "plan this for the team", "what stories do I need for this". The hallmark is an existing spec that needs to become actionable work items.
---

# D3 — Decompose Spec into Stories

This skill turns a feature specification into a set of INVEST-compliant user stories. It defaults to **one user workflow = one full-stack story**, trusting cross-functional teams to deliver complete slices rather than splitting by layer.

## Why INVEST matters here

The whole point of decomposition is to produce stories teams can actually deliver incrementally. A spec chopped up the wrong way — by layer (backend story, frontend story, infra story) or by function (all the API endpoints, then all the UI) — produces stories that nobody can ship in isolation because they don't deliver user value on their own. INVEST is the discipline that keeps the decomposition honest:

- **Independent** — minimize dependencies, enable parallel work
- **Negotiable** — scope is a discussion, not a contract
- **Valuable** — each story delivers a complete user-visible outcome
- **Estimable** — scope is clear enough to size (3–12 ACs is the sweet spot)
- **Small** — 1–10 days; split if larger
- **Testable** — Given-When-Then ACs that a tester can verify

**Default strategy:** one user workflow = one full-stack story (backend + frontend + infrastructure).

**Team assumption:** cross-functional teams can deliver full-stack stories. Don't split by layer just because the org is siloed — that's a different problem.

## Workflow

### 1. Load configuration

- Read `d3.config.md`. If missing, stop and ask the user to run **d3:init**.
- From the Storage table, find **all** rows whose Artifact name contains "Spec" (there may be more than one — Product Specs and Tech Specs are separate rows by default) and the row matching "Stories".
- Read Quiet Mode from `### Settings`.

### 2. Fetch the specification

The user's request will identify the spec by path, title, or description. Read the spec from the Location of each matched spec row — if there are both Product Specs and Tech Specs rows, read both.

Show the user what was found:

```
**Feature:** [Title]
**Product Spec:** [Found / Minimal / Not found] — [path]
**Tech Spec:**    [Found / Minimal / Not found] — [path]
```

If no spec content was found at all, warn the user but continue with whatever context they've provided.

### 3. Request decomposition input

Ask whether the user has a decomposition meeting transcript to draw from:

```
Did you have a story decomposition meeting?
A) Yes — paste the transcript
B) No — let's decompose it together conversationally
```

**Quiet mode:** default to B (conversational) without asking.

If A: extract the proposed stories, boundaries, priorities, and concerns from the transcript and use them as input to step 4.

### 4. Propose workflow-based stories

Analyze the user workflows described in the Product Spec. Default: **one workflow = one full-stack story**.

Present a decomposition proposal:

```
Based on the feature spec, here's my INVEST-compliant decomposition:

Story 1: [Workflow Name]
- Value: [what user capability this delivers]
- Scope: Full-stack (Backend + Frontend)
- Size: [Small/Medium/Large] — [est. days based on AC count]
- Key ACs: [3–12 main scenarios]
- INVEST check:
  Independent: [can be built standalone]
  Valuable:    [delivers a complete workflow]
  Estimable:   [clear scope, X ACs]
  Small:       [1–X days]
  Testable:    [observable user behavior]

[continue for all workflows]
```

### 5. Ask clarifying questions (only where genuinely needed)

Cross-functional teams, error handling, priority ordering, and routine edge cases are **not** worth interrupting the flow for — use reasonable defaults. Do ask about things that affect story boundaries:

1. **Size** — if a story looks >10 days, ask whether to split and on what boundary.
2. **Spec uncertainties** — if uncertainty markers in the spec affect story boundaries, ask whether to create with the assumption, wait for resolution, or create an investigation story.
3. **Non-obvious dependencies** — only if sequencing isn't obvious from the workflows.

Do **not** ask about:
- Team structure (assume cross-functional)
- Error handling (always include in ACs)
- Priority order (follow workflow sequence)
- Routine edge cases (include in ACs unless genuinely complex)

**Quiet mode:** skip all clarifying questions. Proceed with reasonable assumptions and mark any genuine uncertainties inline using the d3:uncertainty-markers skill.

### 6. Validate each story against INVEST

Run the validation before creating anything:

```
INVEST Validation Checklist:
- [ ] Independent: count of stories with no blocking dependencies
- [ ] Negotiable:  confirmed adapted to team structure
- [ ] Valuable:    each story delivers a complete user workflow
- [ ] Estimable:   3–12 ACs per story
- [ ] Small:       1–10 days per story
- [ ] Testable:    Given-When-Then ACs everywhere
```

For each story:
1. Independence: does it have minimal dependencies?
2. Size: is it 1–10 days? Are there 3–12 ACs?
3. Value: does it deliver a complete user workflow on its own?
4. If any check fails, flag it, propose a split or merge, and re-validate.

Only create stories that pass every INVEST check.

### 7. Create the epic (if the backend supports epics)

Read the Instructions column of the "Stories" row. If it indicates a backend that supports epics (Jira and Azure DevOps are the common cases), create an epic first and store its key for linking. In Azure DevOps, epics are work items of type "Epic" and stories are linked as children via parent-child relationships (not epic links).

Epic description template:

```
Feature specification: [Spec Title]

[Brief overview from the Product Spec]

## Reference
- Specification: [Spec path / URL]

## User Stories
This Epic contains [N] INVEST-compliant user stories.
```

If the backend doesn't support epics (local markdown, Linear documents, etc.), skip this step — the reference to the spec in each story is enough.

### 8. Create user stories

Before writing, scan the spec for critical uncertainty markers. If any affect stories you're about to create:
- Warn the user
- Add a note in the affected story descriptions linking back to the spec
- Flag them with a `needs-clarification` label (or equivalent in the target tool)

Load the story template from the Template column of the Stories row. Each story follows that structure:

- **User Story:** As [persona], I want [capability], so that [benefit]
- **Value:** what this delivers
- **Acceptance Criteria:** 3–12 Given-When-Then scenarios covering happy path, errors, and edge cases
- **Technical Notes:** pulled from the tech spec
- **Dependencies:** list story keys if genuine dependencies exist
- **References:** link back to the specification

Create each story following the Instructions column of the Stories row — treat that column literally, it names the tool and parameters to use. Link each story to the epic if one was created.

### 9. Provide a summary

```
Feature decomposed successfully!

Stories: [N] INVEST-compliant stories

Story Breakdown:
1. [Story Title]
   - Scope: [Full-stack/Backend/Frontend]
   - ACs: [N] scenarios
   - Dependencies: [None / "Blocked by [Story]"]
   - INVEST: all criteria met

Implementation Order:
1. [Story Title] — start here (no dependencies)
2. [Story Title] — depends on #1
3. [Story Title] — parallelizable

INVEST Compliance:
Independent: [X/N] stories have no blocking dependencies
Negotiable:  adapted to team structure
Valuable:    each story delivers a complete workflow
Estimable:   [N] total ACs, [avg] per story
Small:       all stories sized 1–10 days
Testable:    all stories have Given-When-Then ACs

Next: review stories → estimate → start with [Story Title]
```

## Sizing guidelines

- **Small:** 1–3 days, 3–5 ACs
- **Medium:** 3–5 days, 5–8 ACs
- **Large:** 5–10 days, 8–12 ACs
- **Too Large:** >10 days → split

## Story scope guidelines

- Default to full-stack workflow stories
- Only split if >10 days or high technical risk
- Keep sizing roughly consistent across stories in the same epic
- Split by scope or risk, not by layer — "backend API story" + "frontend UI story" is almost always wrong for the same workflow

## Acceptance criteria guidelines

- 3–12 Given-When-Then scenarios per story
- Cover: happy path, errors, edge cases
- Each AC must be testable
- Link back to the spec for technical details rather than duplicating them

## Error handling

| Issue | Action |
|-------|--------|
| `d3.config.md` missing | Stop. Ask the user to run **d3:init** first. |
| No spec content | Warn, continue with whatever context the user provides |
| Unclear workflow boundaries | Ask clarifying questions before proposing stories |
| Story creation fails (MCP error, etc.) | Provide the story content inline for manual creation |

## Related skills

- **d3:init** — prerequisite (creates `d3.config.md`)
- **d3:create** — creates the specs this skill decomposes
- **d3:refine** — iterate on the spec before decomposing (or on stories after)
- **d3:uncertainty-markers** — standards for marking uncertainties inline in story content
- **d3:align-spec** — use after implementation to detect drift between these stories, the spec, and the code

## Key principles

1. **INVEST first** — every decomposition decision goes through INVEST
2. **Workflow-based** — default to complete user journeys, not technical layers
3. **Full-stack default** — trust cross-functional teams
4. **Size appropriately** — 1–10 days max; split if larger
5. **Minimal questions** — only interrupt for genuine uncertainties
6. **Test everything** — comprehensive Given-When-Then ACs
7. **Link to specs** — always reference the source specification
