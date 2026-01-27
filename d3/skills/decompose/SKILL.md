---
name: decompose
description: Decompose feature specifications into INVEST-compliant user stories through conversational planning. Creates workflow-based stories that are Independent, Negotiable, Valuable, Estimable, Small, and Testable.
---

## Philosophy: INVEST-Driven Decomposition

Every story must follow INVEST principles:

- **Independent**: Minimize dependencies, enable parallel development
- **Negotiable**: Discuss scope based on real constraints (size, uncertainty, risk)
- **Valuable**: Deliver complete user workflows, demonstrable outcomes
- **Estimable**: Clear scope with 3-12 acceptance criteria
- **Small**: 1-10 days of work (split if larger)
- **Testable**: Given-When-Then acceptance criteria

**Default Strategy:** Decompose by user workflow (one workflow = one story, full-stack)
**Team Assumption:** Cross-functional teams that can deliver full-stack stories are the modern standard. Stories default to full-stack (Backend + Frontend + Infrastructure) unless size or risk requires splitting.

---

## Workflow

1. Detect providers (spec + story)
2. Fetch specification with Product + Technical specs
3. Ask for project key
4. Ask if decomposition meeting transcript exists (optional)
5. Propose workflow-based story breakdown (full-stack by default)
6. Ask clarifying questions (only if: stories >10 days, spec uncertainties, or non-obvious dependencies)
7. Create Epic
8. Create user stories linked to Epic
9. Provide implementation-ready summary

---

## Step 0: Detect Providers

**Provider Detection:**
1. Read `CLAUDE.md` and look for D3 Configuration section
2. If configuration found:
   - Extract **Spec Provider** name (e.g., "d3-atlassian:atlassian-spec-provider")
   - Extract **Story Provider** name (e.g., "d3-atlassian:atlassian-story-provider")
3. If not found, use defaults:
   - Spec Provider: "d3-atlassian:atlassian-spec-provider"
   - Story Provider: "d3-atlassian:atlassian-story-provider"

**If configuration is missing or incomplete:**

Show this guidance to the user:
```markdown
⚠️ D3 Configuration Not Found

I couldn't find D3 provider configuration in CLAUDE.md.

Please add this to your CLAUDE.md file:

## D3 Configuration

### Spec Provider
**Skill:** d3-atlassian:atlassian-spec-provider
**Configuration:**
- Cloud ID: your-atlassian-cloud-id
- Default Location: YOUR-SPACE-KEY
- Default parent page: (optional) parent-page-url

### Story Provider
**Skill:** d3-atlassian:atlassian-story-provider
**Configuration:**
- Cloud ID: your-atlassian-cloud-id
- Default Project: YOUR-PROJECT-KEY

---

**How to find your Cloud ID:**
Visit your Atlassian site and check the URL or use the Atlassian MCP tools.

**Other providers available:**
- Notion, Linear, GitHub, or create your own custom provider

See README.md for full details and alternative provider options.
```

Then stop and wait for the user to update their configuration.

**Store provider names** for use in Steps 1, 2, 7, and 8.

---

## Step 1: Fetch Specification & Verify

**Use Skill Tool to invoke spec provider:**
```
Skill(skill="[spec-provider-name]", args="get_spec page_id=\"[PAGE-ID]\"")
```

Parse page ID from `$ARGUMENTS` (can be ID, URL, or title).

Display:
```markdown
I found Specification: [Page Title]

**Specification:** [Page Title]
**URL:** [Page URL]
**Location:** [Location name/key]

**Product Spec:** [✅ Found / ❌ Not found]
**Technical Spec:** [✅ Found / ⏳ Minimal / ❌ Not found]

✅ Ready to decompose into user stories.
```

**If no Product Spec:** Warn but continue with page content
**If no Technical Spec:** Note it's optional, continue

---

## Step 2: Get Project

**If user needs list of projects:**
Use Skill Tool to invoke story provider:
```
Skill(skill="[story-provider-name]", args="list_projects")
```

```markdown
Which project should I create the user stories in?

**Project Key:** [e.g., "PROJ", "BOOT", "ENG"]
```

**Verify project and get issue types:**
```
Skill(skill="[story-provider-name]", args="get_issue_types project_key=\"[PROJECT-KEY]\"")
```

Confirm Epic and Story issue types are available.

---

## Step 3: Request Decomposition Input

```markdown
Before I decompose this feature, did you have a story decomposition meeting?

**Option A: Yes, I have a transcript** - Paste your meeting transcript
**Option B: No, let's decompose it together** - I'll break it down conversationally

Which would you prefer?
```

**If Option A:** Extract proposed stories, boundaries, priorities, concerns
**If Option B:** Proceed to Step 4

---

## Step 4: Propose Workflow-Based Stories (INVEST)

Analyze user workflows from Product Spec. **Default: One workflow = one full-stack story**

```markdown
Based on the feature spec, here's my INVEST-compliant decomposition:

**Story 1: [Workflow Name from spec]**
- **Value**: [What user capability this delivers]
- **Scope**: Full-stack (Backend + Frontend)
- **Size**: [Small/Medium/Large] - [Est. days based on AC count]
- **Key ACs**: [3-8 main scenarios]
- **INVEST Check**:
  - ✅ Independent: [Can be built standalone]
  - ✅ Valuable: [Delivers complete workflow]
  - ✅ Estimable: [Clear scope, X ACs]
  - ✅ Small: [1-X days]
  - ✅ Testable: [Observable user behavior]

**Story 2: [Workflow Name]**
[Same structure]

[Continue for all workflows]

Each story delivers complete user value and can be demoed independently.
```

---

## Step 5: Ask Clarifying Questions (Only When Needed)

**Only ask questions about genuine uncertainties that affect story boundaries.**

Ask ONLY if applicable:

**1. Size (if any story >10 days):**
```markdown
Story [N] seems large (>10 days). Should I split it?
- Option A: Split by [technical boundary, e.g., "infrastructure" vs "feature"]
- Option B: Split by [functional step, e.g., "basic" vs "advanced"]
- Option C: Keep it together - team can handle the size
```

**2. Spec Uncertainties (if [OPEN QUESTION] or [DECISION PENDING] markers affect story boundaries):**
```markdown
The spec has open questions about [topic]:
- [OPEN QUESTION from spec]

Should I:
- Option A: Create story with assumption [X], flag for clarification
- Option B: Wait to decompose until question is resolved
- Option C: Create separate investigation story first
```

**3. Dependencies (only if non-obvious):**
```markdown
Story [X] and Story [Y] could be:
- Option A: Sequential (Y depends on X)
- Option B: Parallel (independent)

Which approach fits your workflow?
```

**DO NOT ask about:**
- ❌ Team structure (assume cross-functional full-stack)
- ❌ Whether to include error handling (always include in ACs)
- ❌ Priority order (obvious from workflow sequence)
- ❌ Edge cases as separate stories (include in story ACs unless genuinely complex)

---

## Step 6: Finalize & Confirm

```markdown
Perfect! Here's the final decomposition:

**Story 1: [Title]**
- Focus: [User value]
- Scope: [Full-stack / Backend / Frontend]
- ACs: [N] scenarios (happy path, errors, edge cases)
- Dependencies: [None / "Needs Story X"]
- Size: [Small/Medium/Large]

[Continue for all stories]

**INVEST Compliance:**
✅ Independent: [X stories have no dependencies]
✅ Negotiable: [Adapted to your team structure]
✅ Valuable: [Each story delivers user workflow]
✅ Estimable: [Clear ACs, 3-12 per story]
✅ Small: [All stories 1-10 days]
✅ Testable: [Gherkin format ACs]

**Total:** [N] stories

Does this look good, or would you like adjustments?
```

Wait for confirmation before creating.

---

## Step 7: Create Epic

**Use Skill Tool to invoke story provider:**
```
Skill(
  skill="[story-provider-name]",
  args="create_epic project_key=\"[PROJECT-KEY]\" summary=\"[Feature name from spec title]\" description=\"[Epic description]\" labels=\"feature,epic\""
)
```

**Epic Description:**
```markdown
Feature specification: [Spec Page Title]

[Brief overview from Product Spec]

## Reference
- Specification: [Page URL]
- Location: [Location name]

## User Stories
This Epic contains [N] INVEST-compliant user stories.
```

Store Epic key/ID for linking stories.

```markdown
✅ Created Epic [EPIC-KEY]: [Feature Name]

Now creating [N] user stories under this Epic...
```

---

## Step 8: Create User Stories

**CRITICAL - Check for Uncertainties:**
Before creating, review specs for `[OPEN QUESTION]`, `[DECISION PENDING]`, `[CLARIFICATION NEEDED]` markers.
- If critical uncertainties exist, warn user
- Add note in story description linking to specification
- Flag with "needs-clarification" label

**Use Skill Tool to invoke story provider for each story:**
```
Skill(
  skill="[story-provider-name]",
  args="create_story project_key=\"[PROJECT-KEY]\" epic_id=\"[EPIC-KEY]\" story_data=\"{summary: '...', description: '...', acceptance_criteria: '...', labels: [...], ...}\""
)
```

**Story Format:**
- **Title:** Clear, action-oriented, 3-7 words
- **Description:** Use template from `../../templates/user-story.md`

**Story Structure:**
```markdown
**User Story:** As a [persona], I want [capability], so that [benefit]

**Value:** [What this delivers to users/business]

**Specification:** [Link to specification]

---

## Acceptance Criteria

**AC1: [Scenario name - e.g., "Happy path - successful search"]**
**Given** [context]
**When** [action]
**Then** [expected outcome]

**AC2: [Scenario name - e.g., "Error - no results found"]**
**Given** [context]
**When** [action]
**Then** [expected outcome]

[Continue with 3-12 ACs covering: happy path, errors, edge cases, empty states]

---

## Technical Notes

[Technical considerations from spec]

**Dependencies:** [List story keys if dependencies exist]

**References:**
- Confluence Spec: [Page URL]
```

**Epic-Story Linking:**
```javascript
{
  cloudId: "[CLOUD-ID]",
  projectKey: "[PROJECT-KEY]",
  issueTypeName: "Task", // or "Story" depending on project
  summary: "[Story Title]",
  description: "[Story Description in Markdown]",
  additional_fields: {
    parent: {
      key: "[EPIC-KEY]"
    }
  },
  labels: ["user-story", "frontend", "backend", ...]
}
```

**If linking fails:** Inform user and provide manual linking instructions.

---

## Step 9: Provide Summary

```markdown
✅ Feature decomposed successfully!

**Epic:** [EPIC-KEY]: [Feature Name] - [URL]
**Stories:** [N] INVEST-compliant stories

**Story Breakdown:**

1. **[ISSUE-KEY]: [Title]** - [URL]
   - Scope: [Full-stack/Backend/Frontend]
   - ACs: [N] scenarios
   - Dependencies: [None / "Blocked by [KEY]"]
   - INVEST: ✅ All criteria met

[Continue for all stories]

**Implementation Order:**
1. [ISSUE-KEY]: [Title] - Start here (no dependencies)
2. [ISSUE-KEY]: [Title] - Depends on #1
3. [ISSUE-KEY]: [Title] - Can run parallel

**INVEST Compliance:**
✅ Independent: [X/N stories] have no blocking dependencies
✅ Negotiable: Adapted to [team structure]
✅ Valuable: Each story delivers complete workflow
✅ Estimable: [N] total ACs, [avg] per story
✅ Small: All stories sized 1-10 days
✅ Testable: All stories have Given-When-Then ACs

**Next Steps:**
1. Review stories in Jira
2. Create dependency links manually (if any)
3. Estimate and prioritize
4. Start implementation with [ISSUE-KEY]
```

---

## INVEST Guidelines

### Independent (Minimize Dependencies)
- Default to workflow-based decomposition (naturally independent)
- Ask about dependencies explicitly
- Document dependencies in story descriptions
- Aim for parallel development

### Negotiable (Flexible Scope)
- Default to full-stack workflow stories (modern cross-functional teams)
- Only ask about splitting if story is >10 days or has high technical risk
- Confirm breakdown before creating
- Adapt based on size, uncertainty, and dependencies (not team structure)

### Valuable (User Outcomes)
- Each story = one complete user workflow
- Every story must be demostrable
- Focus on user-facing capabilities
- Map stories to Product Spec workflows

### Estimable (Clear Scope)
- **Small**: 1-3 days, 3-5 ACs
- **Medium**: 3-5 days, 5-8 ACs
- **Large**: 5-10 days, 8-12 ACs
- **Too Large**: >10 days → split it

### Small (One Iteration)
- Maximum 10 days per story
- If larger, ask how to split
- Consistent sizing across stories
- Split large workflows into steps if needed

### Testable (Clear Acceptance)
- Gherkin format (Given-When-Then)
- Specific values, not placeholders
- Cover happy path, errors, edge cases
- Observable behavior only
- Map ACs to spec requirements

---

## Error Handling

- **No specs:** Warn, continue with page content
- **Project not found:** List available projects
- **Epic linking fails:** Provide manual instructions
- **Unclear boundaries:** Ask clarifying questions

---

## Example: Conversational Decomposition

```
User: /decompose https://site.atlassian.net/wiki/pages/123456

Agent: ✅ Found page with Product + Technical specs
       Which Jira project?

User: ENG

Agent: Did you have a decomposition meeting?
       Option A/B?

User: B

Agent: Based on the spec, here's my INVEST decomposition:

       Story 1: User Login Workflow
       - Value: Users can authenticate and access their account
       - Scope: Full-stack (API + UI)
       - Size: Medium (5 days, 7 ACs)
       - INVEST: ✅ All criteria met

       Story 2: Password Reset Workflow
       - Value: Users can recover forgotten passwords
       - Scope: Full-stack (API + UI + Email)
       - Size: Medium (4 days, 6 ACs)
       - INVEST: ✅ All criteria met

       Both stories are independent and can be developed in parallel.

       Does this look good?

User: Yes, create them

Agent: ✅ Created Epic ENG-42: User Authentication
       ✅ Created ENG-43: User Login Workflow
       ✅ Created ENG-44: Password Reset Workflow

       Both stories are INVEST-compliant and ready to implement.
       Start with either story.
```

---

## Key Principles

1. **INVEST First**: Every decision guided by INVEST principles
2. **Workflow-Based**: Default to complete user journeys (Valuable + Independent)
3. **Full-Stack Default**: Assume cross-functional teams, stories include Backend + Frontend + Infrastructure
4. **Size Appropriately**: 1-10 days maximum, split if larger (not by layer, by scope or risk)
5. **Minimal Questions**: Only ask when genuinely uncertain (>10 day stories, spec gaps, complex dependencies)
6. **Test Everything**: Comprehensive Given-When-Then ACs
7. **Link to Specs**: Always reference specification for context
