---
description: Decompose feature specifications into INVEST-compliant user stories through conversational planning. Creates workflow-based stories that are Independent, Negotiable, Valuable, Estimable, Small, and Testable.
---

## Core Principle: INVEST-Driven Decomposition

Every story must follow INVEST:
- **Independent:** Minimize dependencies, enable parallel development
- **Negotiable:** Discuss scope based on real constraints (size, uncertainty, risk)
- **Valuable:** Deliver complete user workflows, demonstrable outcomes
- **Estimable:** Clear scope with 3-12 acceptance criteria
- **Small:** 1-10 days of work (split if larger)
- **Testable:** Given-When-Then acceptance criteria

**Default Strategy:** One user workflow = one full-stack story (Backend + Frontend + Infrastructure)

**Team Assumption:** Cross-functional teams can deliver full-stack stories

---

## Workflow

### 1. Detect Provider and Templates
- Read `d3.config.md` for D3 config
- Search for ### D3 Config  ### Templates
- If user story template are not configure use skill d3-templates
- Store for later steps

### 2. Fetch Specification
Parse spec identifier from `$ARGUMENTS` (ID, URL, or title). Use spec provider's `get_spec`.

Display:
```
**Specification:** [Title] - [URL]
**Product Spec:** [✅ Found / ⏳ Minimal / ❌ Not found]
**Technical Spec:** [✅ Found / ⏳ Minimal / ❌ Not found]
```

If no Product Spec: Warn but continue.

### 3. Detect Project and Capabilities
Use story provider's `list_projects`:
- If single project returned → use it automatically (no prompt needed)
- If multiple projects → ask user to choose

Call `get_issue_types` for the chosen project. Store whether Epic type is available (used in step 8).

### 4. Request Decomposition Input
Ask user:
```
Did you have a story decomposition meeting?
A) Yes - Paste meeting transcript
B) No - Let's decompose it together conversationally
```

If Option A: Extract proposed stories, boundaries, priorities, concerns from transcript.

### 5. Propose Workflow-Based Stories

Analyze user workflows from Product Spec. **Default: One workflow = one full-stack story**

```
Based on the feature spec, here's my INVEST-compliant decomposition:

Story 1: [Workflow Name]
- Value: [What user capability this delivers]
- Scope: Full-stack (Backend + Frontend)
- Size: [Small/Medium/Large] - [Est. days based on AC count]
- Key ACs: [3-12 main scenarios]
- INVEST Check:
  ✅ Independent: [Can be built standalone]
  ✅ Valuable: [Delivers complete workflow]
  ✅ Estimable: [Clear scope, X ACs]
  ✅ Small: [1-X days]
  ✅ Testable: [Observable user behavior]

[Continue for all workflows]
```

### 6. Ask Clarifying Questions (Only When Needed)

**Only ask about genuine uncertainties affecting story boundaries.**

**Ask about:**
1. **Size (if story >10 days):** Should I split it? By what boundary?
2. **Spec uncertainties (if markers affect boundaries):** Create with assumption, wait, or create investigation story?
3. **Dependencies (only if non-obvious):** Sequential or parallel?

**DO NOT ask about:**
- ❌ Team structure (assume cross-functional)
- ❌ Error handling (always include in ACs)
- ❌ Priority order (obvious from workflow sequence)
- ❌ Edge cases (include in ACs unless genuinely complex)

### 7. Validate Stories Against INVEST

**CRITICAL - Run before creation:**

```
INVEST Validation Checklist:
- [ ] Independent: Count stories with no blocking dependencies
- [ ] Negotiable: Verify adapted to team structure
- [ ] Valuable: Each story delivers complete user workflow
- [ ] Estimable: Verify 3-12 ACs per story
- [ ] Small: Verify all stories 1-10 days
- [ ] Testable: Verify all have Given-When-Then ACs
```

**For each story:**
1. Independence: Minimal dependencies?
2. Size: 1-10 days? ACs count 3-12?
3. Value: Delivers complete workflow?
4. If any check fails: Flag, propose split/merge, re-validate

**Only create stories that pass all INVEST checks.**

### 8. Create Epic (if supported)

**Skip this step if Epic type was not available in step 3.**

If Epic type is available, invoke the [story-provider] skill (see platform reference for invocation syntax):
```
create_epic project_key="[PROJECT]" summary="[Feature name]" description="[Epic description]" labels="feature,epic"
```

**Epic Description:**
```
Feature specification: [Spec Title]

[Brief overview from Product Spec]

## Reference
- Specification: [Spec URL]
- Location: [Location name]

## User Stories
This Epic contains [N] INVEST-compliant user stories.
```

Store Epic key for linking stories.

### 9. Create User Stories

**CRITICAL - Check Uncertainties:**

Before creating, scan specs for uncertainty markers. If critical uncertainties:
- Warn user
- Add note in story description linking to spec
- Flag with "needs-clarification" label

**Load Story Template:**
1. Use `user_story_template` from config
2. Read template using the read tool
3. Use template structure for story content

**Story Structure:**
- User Story: As [persona], I want [capability], so that [benefit]
- Value: What this delivers
- Acceptance Criteria: 3-12 Given-When-Then scenarios (happy path, errors, edge cases)
- Technical Notes: From technical spec
- Dependencies: List story keys if dependencies exist
- References: Link to specification

**Create each story.** Invoke the [story-provider] skill (see platform reference for invocation syntax):
- If epic was created → pass `epic_id`
- If no epic → pass `spec_id` instead (lets provider group stories by spec)

```
create_story project_key="[PROJECT]" epic_id="[EPIC-KEY]" story_data="{summary: '...', description: '...', labels: [...]}"
```
or (when no epic):
```
create_story project_key="[PROJECT]" spec_id="[SPEC-ID]" story_data="{summary: '...', description: '...', labels: [...]}"
```

### 10. Provide Summary

Use whatever keys/URLs the provider returned (don't assume format). Only show Epic line if one was created.

```
✅ Feature decomposed successfully!

**Epic:** [EPIC-KEY]: [Feature Name] - [URL]  ← only if epic was created
**Stories:** [N] INVEST-compliant stories

Story Breakdown:
1. [Story Key/ID]: [Title] - [URL if available]
   - Scope: [Full-stack/Backend/Frontend]
   - ACs: [N] scenarios
   - Dependencies: [None / "Blocked by [KEY]"]
   - INVEST: ✅ All criteria met

Implementation Order:
1. [Story Key/ID]: [Title] - Start here (no dependencies)
2. [Story Key/ID]: [Title] - Depends on #1
3. [Story Key/ID]: [Title] - Can run parallel

INVEST Compliance:
✅ Independent: [X/N stories] have no blocking dependencies
✅ Negotiable: Adapted to team structure
✅ Valuable: Each story delivers complete workflow
✅ Estimable: [N] total ACs, [avg] per story
✅ Small: All stories sized 1-10 days
✅ Testable: All stories have Given-When-Then ACs

Next: Review stories → Estimate → Start with [Story Key/ID]
```

---

## INVEST Guidelines

### Size Guidelines
- **Small:** 1-3 days, 3-5 ACs
- **Medium:** 3-5 days, 5-8 ACs
- **Large:** 5-10 days, 8-12 ACs
- **Too Large:** >10 days → split it

### Story Scope
- Default to full-stack workflow stories
- Only split if >10 days or high technical risk
- Consistent sizing across stories
- Split by scope or risk, not by layer

### Acceptance Criteria
- 3-12 Given-When-Then scenarios per story
- Cover: Happy path, errors, edge cases
- Each AC must be testable
- Link to spec for technical details

---

## Error Handling

| Issue | Action |
|-------|--------|
| No specs | Warn, continue with available content |
| Project not found | List available projects |
| Epic linking fails | Provide manual instructions |
| Unclear boundaries | Ask clarifying questions |
| Provider fails | Fall back to providing story content |

---

## Key Principles

1. **INVEST First** - Every decision guided by INVEST principles
2. **Workflow-Based** - Default to complete user journeys
3. **Full-Stack Default** - Stories include Backend + Frontend + Infrastructure
4. **Size Appropriately** - 1-10 days maximum, split if larger
5. **Minimal Questions** - Only ask when genuinely uncertain
6. **Test Everything** - Comprehensive Given-When-Then ACs
7. **Link to Specs** - Always reference specification
