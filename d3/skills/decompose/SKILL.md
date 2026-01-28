---
name: decompose
description: Decompose feature specifications into INVEST-compliant user stories through conversational planning. Creates workflow-based stories that are Independent, Negotiable, Valuable, Estimable, Small, and Testable.
---

## Philosophy: INVEST-Driven Decomposition

Every story must follow INVEST principles:
- **Independent:** Minimize dependencies, enable parallel development
- **Negotiable:** Discuss scope based on real constraints (size, uncertainty, risk)
- **Valuable:** Deliver complete user workflows, demonstrable outcomes
- **Estimable:** Clear scope with 3-12 acceptance criteria
- **Small:** 1-10 days of work (split if larger)
- **Testable:** Given-When-Then acceptance criteria

**Default Strategy:** Decompose by user workflow (one workflow = one full-stack story)

**Team Assumption:** Cross-functional teams can deliver full-stack stories (Backend + Frontend + Infrastructure)

---

## Workflow Checklist

Copy this and track progress:

```
Story Decomposition Progress:
- [ ] Step 1: Detect providers (spec + story)
- [ ] Step 2: Fetch and verify specification
- [ ] Step 3: Get project key
- [ ] Step 4: Request decomposition input
- [ ] Step 5: Propose workflow-based stories
- [ ] Step 6: Ask clarifying questions (if needed)
- [ ] Step 7: Validate stories against INVEST
- [ ] Step 8: Create Epic
- [ ] Step 9: Create user stories
- [ ] Step 10: Provide summary
```

---

## Steps

### Step 1: Detect Providers

Detect both spec and story providers from CLAUDE.md. See [provider-detection.md](../../shared/provider-detection.md) for details.

Store provider names for later steps.

---

### Step 2: Fetch Specification

Parse spec identifier from `$ARGUMENTS` (ID, URL, or title).

Use spec provider's `get_spec` operation.

**Display:**
```markdown
I found Specification: [Spec Title]

**Specification:** [Title]
**URL:** [URL]
**Location:** [Location]

**Product Spec:** [✅ Found / ⏳ Minimal / ❌ Not found]
**Technical Spec:** [✅ Found / ⏳ Minimal / ❌ Not found]

✅ Ready to decompose into user stories.
```

If no Product Spec: Warn but continue.

---

### Step 3: Get Project

**If user needs list:** Use story provider's `list_projects` operation.

```markdown
Which project should I create user stories in?

**Project Key:** [e.g., "PROJ", "BOOT", "ENG"]
```

Verify project using `get_issue_types` - confirm Epic and Story types available.

---

### Step 4: Request Decomposition Input

```markdown
Before I decompose this feature, did you have a story decomposition meeting?

**Option A: Yes, I have a transcript** - Paste your meeting transcript
**Option B: No, let's decompose it together** - I'll break it down conversationally
```

**If Option A:** Extract proposed stories, boundaries, priorities, concerns from transcript.

---

### Step 5: Propose Workflow-Based Stories

Analyze user workflows from Product Spec. **Default: One workflow = one full-stack story**

```markdown
Based on the feature spec, here's my INVEST-compliant decomposition:

**Story 1: [Workflow Name]**
- **Value:** [What user capability this delivers]
- **Scope:** Full-stack (Backend + Frontend)
- **Size:** [Small/Medium/Large] - [Est. days based on AC count]
- **Key ACs:** [3-8 main scenarios]
- **INVEST Check:**
  - ✅ Independent: [Can be built standalone]
  - ✅ Valuable: [Delivers complete workflow]
  - ✅ Estimable: [Clear scope, X ACs]
  - ✅ Small: [1-X days]
  - ✅ Testable: [Observable user behavior]

[Continue for all workflows]

Each story delivers complete user value and can be demoed independently.
```

---

### Step 6: Ask Clarifying Questions (Only When Needed)

**Only ask about genuine uncertainties affecting story boundaries.**

**1. Size (if story >10 days):**
```markdown
Story [N] seems large (>10 days). Should I split it?
- Option A: Split by [technical boundary]
- Option B: Split by [functional step]
- Option C: Keep together - team can handle size
```

**2. Spec Uncertainties (if markers affect boundaries):**
```markdown
The spec has open questions about [topic]:
- [OPEN QUESTION from spec]

Should I:
- Option A: Create story with assumption, flag for clarification
- Option B: Wait until question resolved
- Option C: Create investigation story first
```

**3. Dependencies (only if non-obvious):**
```markdown
Story [X] and Story [Y] could be:
- Option A: Sequential (Y depends on X)
- Option B: Parallel (independent)
```

**DO NOT ask about:**
- ❌ Team structure (assume cross-functional)
- ❌ Error handling (always include in ACs)
- ❌ Priority order (obvious from workflow sequence)
- ❌ Edge cases (include in ACs unless genuinely complex)

---

### Step 7: Validate Stories Against INVEST

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
1. Independence: Does it have minimal dependencies?
2. Size: Is it 1-10 days? Count ACs (should be 3-12)
3. Value: Does it deliver complete workflow?
4. If any check fails:
   - Flag the story
   - Propose split or merge
   - Re-validate

**Only create stories that pass all INVEST checks.**

---

### Step 8: Create Epic

Use story provider's `create_epic` operation:

```
Skill(
  skill="[story-provider-name]",
  args="create_epic project_key=\"[PROJECT]\" summary=\"[Feature name]\" description=\"[Epic description]\" labels=\"feature,epic\""
)
```

**Epic Description:**
```markdown
Feature specification: [Spec Title]

[Brief overview from Product Spec]

## Reference
- Specification: [Spec URL]
- Location: [Location name]

## User Stories
This Epic contains [N] INVEST-compliant user stories.
```

Store Epic key for linking stories.

---

### Step 9: Create User Stories

**CRITICAL - Check Uncertainties:**

Before creating, scan specs for uncertainty markers. If critical uncertainties:
- Warn user
- Add note in story description linking to spec
- Flag with "needs-clarification" label

**Use story provider's `create_story` operation for each story:**

```
Skill(
  skill="[story-provider-name]",
  args="create_story project_key=\"[PROJECT]\" epic_id=\"[EPIC-KEY]\" story_data=\"{summary: '...', description: '...', labels: [...]}\""
)
```

**Story Structure:**

**Load Story Template:**

1. Use `user_story_template` path from provider detection (Step 0)
   - Default: `d3/templates/user-story.md`
2. Use Read tool to load template content
3. Use template structure for story content

**Provider Note:**
The template provides generic structure (Description, Acceptance Criteria, Technical Notes, etc.).
The story provider will transform this to its required format (e.g., YAML frontmatter for markdown,
Jira fields for Atlassian).

**Key sections to populate:**
- User Story: As [persona], I want [capability], so that [benefit]
- Value: What this delivers
- Acceptance Criteria: 3-12 Given-When-Then scenarios (happy path, errors, edge cases)
- Technical Notes: From technical spec
- Dependencies: List story keys if dependencies exist
- References: Link to specification

**For each story:**
- Populate template sections with story content
- Pass to story provider for format transformation and creation

---

### Step 10: Provide Summary

```markdown
✅ Feature decomposed successfully!

**Epic:** [EPIC-KEY]: [Feature Name] - [URL]
**Stories:** [N] INVEST-compliant stories

## Story Breakdown

1. **[ISSUE-KEY]: [Title]** - [URL]
   - Scope: [Full-stack/Backend/Frontend]
   - ACs: [N] scenarios
   - Dependencies: [None / "Blocked by [KEY]"]
   - INVEST: ✅ All criteria met

[Continue for all stories]

## Implementation Order

1. [ISSUE-KEY]: [Title] - Start here (no dependencies)
2. [ISSUE-KEY]: [Title] - Depends on #1
3. [ISSUE-KEY]: [Title] - Can run parallel

## INVEST Compliance

✅ Independent: [X/N stories] have no blocking dependencies
✅ Negotiable: Adapted to team structure
✅ Valuable: Each story delivers complete workflow
✅ Estimable: [N] total ACs, [avg] per story
✅ Small: All stories sized 1-10 days
✅ Testable: All stories have Given-When-Then ACs

**Total:** [N] stories

## Next Steps

1. Review stories in work tracker
2. Estimate and prioritize
3. Start implementation with [ISSUE-KEY]
```

---

## INVEST Guidelines (Quick Reference)

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

---

## Error Handling

- **No specs:** Warn, continue with spec content
- **Project not found:** List available projects
- **Epic linking fails:** Provide manual instructions
- **Unclear boundaries:** Ask clarifying questions
- **Provider fails:** Fall back to providing story content

---

## Example

**Quick reference** (see [examples.md](references/examples.md) for detailed scenarios):

```
User: /d3:decompose 123456789

Agent: Found spec. Which project?

User: ENG

Agent: Decomposition meeting?

User: Option B

Agent: Based on spec:
       Story 1: User Login Workflow (5 days, 7 ACs)
       Story 2: Password Reset Workflow (4 days, 6 ACs)
       Both independent, full-stack. Create?

User: Yes

Agent: ✅ Created Epic ENG-42
       ✅ Created ENG-43, ENG-44
       Both INVEST-compliant. Start with either.
```

---

## Key Principles

1. **INVEST First:** Every decision guided by INVEST principles
2. **Workflow-Based:** Default to complete user journeys
3. **Full-Stack Default:** Stories include Backend + Frontend + Infrastructure
4. **Size Appropriately:** 1-10 days maximum, split if larger
5. **Minimal Questions:** Only ask when genuinely uncertain
6. **Test Everything:** Comprehensive Given-When-Then ACs
7. **Link to Specs:** Always reference specification

See [examples.md](references/examples.md) for comprehensive scenarios and [user-story-template.md](references/user-story-template.md) for story format details.
