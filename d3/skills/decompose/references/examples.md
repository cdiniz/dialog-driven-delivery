# Decompose Examples

Detailed examples showing story decomposition scenarios following INVEST principles.

---

## Example 1: Conversational Decomposition

**Scenario:** Decomposing without a meeting transcript.

```
User: /d3:decompose https://site.atlassian.net/wiki/pages/123456

Agent: ✅ Found page with Product + Technical specs
       Which Jira project?

User: ENG

Agent: Did you have a decomposition meeting?
       Option A: Yes, I have a transcript
       Option B: No, let's decompose it together

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

## Example 2: Transcript-Based Decomposition

**Scenario:** Using a meeting transcript to guide decomposition.

```
User: /d3:decompose 123456789

Agent: Found Specification: Advanced Search with Filters
       Product Spec: ✅ 85% complete
       Technical Spec: ✅ 75% complete

       Which project?

User: PROJ

Agent: Did you have a decomposition meeting?

User: Option A
      [Pastes decomposition meeting transcript]

Agent: Analyzing transcript...

       I found discussion about:
       - Starting with basic search, then adding filters
       - Concern about filter complexity
       - Decision to split filtering into categories

       Proposed stories:

       Story 1: Basic Text Search
       - Value: Users can search content by keywords
       - Scope: Full-stack (Backend + Frontend)
       - Size: Small (3 days, 5 ACs)
       - Dependencies: None
       - INVEST: ✅ Independent, valuable, estimable, small, testable

       Story 2: Category Filters
       - Value: Users can filter search by content category
       - Scope: Full-stack (Backend + Frontend)
       - Size: Small (3 days, 4 ACs)
       - Dependencies: Builds on Story 1
       - INVEST: ✅ All criteria met

       Story 3: Date Range Filters
       - Value: Users can filter search by date ranges
       - Scope: Full-stack (Backend + Frontend)
       - Size: Small (2 days, 4 ACs)
       - Dependencies: Builds on Story 1
       - INVEST: ✅ All criteria met

       Story 4: Status Filters
       - Value: Users can filter by item status
       - Scope: Full-stack (Backend + Frontend)
       - Size: Small (2 days, 3 ACs)
       - Dependencies: Builds on Story 1
       - INVEST: ✅ All criteria met

       Implementation order: Story 1 first, then 2-4 in parallel

       Clarifying questions:
       1. Should filters persist across sessions?
       2. Maximum results per page?

User: 1. Yes, persist filters
      2. 25 results per page

Agent: Updated stories with pagination and filter persistence.

       Create these 4 stories?

User: Yes

Agent: Creating Epic in PROJ...

       ✅ Created PROJ-41: Advanced Search with Filters
          Link: https://jira.example.com/browse/PROJ-41

       Creating user stories...

       ✅ PROJ-42: Basic Text Search
       ✅ PROJ-43: Category Filters (blocked by PROJ-42)
       ✅ PROJ-44: Date Range Filters (blocked by PROJ-42)
       ✅ PROJ-45: Status Filters (blocked by PROJ-42)

       All stories linked to Epic and dependencies set.

       Implementation order:
       1. PROJ-42 (start here)
       2. PROJ-43, 44, 45 (parallel after 42 completes)
```

---

## Example 3: Large Story Splitting

**Scenario:** Agent detects story is too large and proposes split.

```
User: /d3:decompose 123456789

Agent: [Analyzes spec]

       Story 1: Complete Dashboard with Analytics
       - Value: Users can view all metrics and reports
       - Scope: Full-stack with data pipeline
       - Size: Large (15 days, 18 ACs) ⚠️
       - INVEST Issue: Too large (>10 days)

       This story exceeds 10 days. Should I split it?

       **Option A:** Split by technical boundary (data pipeline vs UI)
       **Option B:** Split by functional step (basic metrics vs advanced analytics)
       **Option C:** Keep together - team can handle the size

User: Option B

Agent: Splitting by functional step:

       Story 1a: Basic Dashboard Metrics
       - Value: Users can view core metrics (views, users, sessions)
       - Scope: Full-stack
       - Size: Medium (7 days, 9 ACs)
       - INVEST: ✅ All criteria met

       Story 1b: Advanced Analytics Reports
       - Value: Users can generate detailed analytics reports
       - Scope: Full-stack
       - Size: Medium (8 days, 9 ACs)
       - Dependencies: Builds on Story 1a
       - INVEST: ✅ All criteria met

       Better? Both stories now 7-8 days each.

User: Yes, create both

Agent: ✅ Created both stories with dependency link
```

---

## Example 4: INVEST Validation Catching Issues

**Scenario:** Validation loop identifies non-independent stories.

```
User: /d3:decompose 123456789

Agent: [Proposes stories]

       Running INVEST validation...

       ⚠️ Independence Issue Detected:

       Story 2, 3, 4, and 5 all depend on Story 1.
       This creates a bottleneck - only 1 story can be worked on initially.

       Options:
       **Option A:** Accept bottleneck (Story 1 is foundation)
       **Option B:** Redesign Story 1 to be smaller foundation
       **Option C:** Find parallel work in other stories

User: Option B

Agent: Reducing Story 1 to minimal foundation:

       Story 1 (revised): Core Search Infrastructure
       - Value: Basic search capability (minimum viable)
       - Scope: Backend only, simple UI
       - Size: Small (2 days, 3 ACs)
       - Now other stories less dependent

       Story 2, 3, 4 now more independent with basic search in place.

       ✅ INVEST Check: 4/5 stories now independent

User: Much better, create them

Agent: ✅ Created with improved independence
```

---

## Example 5: Handling Spec Uncertainties

**Scenario:** Spec has open questions affecting story boundaries.

```
User: /d3:decompose 123456789

Agent: Found specification with 5 [OPEN QUESTION] markers:

       - [OPEN QUESTION: Real-time updates or batch?]
       - [OPEN QUESTION: Support mobile or desktop only?]

       These affect story boundaries. Options:

       **Option A:** Create stories with assumptions, flag for clarification
       **Option B:** Wait to decompose until questions resolved
       **Option C:** Create investigation story first

User: Option A

Agent: Creating stories with assumptions:

       Story 1: Desktop Search Interface
       - [ASSUMPTION: Desktop first, mobile later]
       - Labeled: needs-clarification
       - Note: Verify desktop-first approach before starting

       Story 2: Search Data Updates
       - [ASSUMPTION: Batch processing every 5 minutes]
       - Labeled: needs-clarification
       - Note: May need real-time implementation instead

       Create with assumptions flagged?

User: Yes

Agent: ✅ Created with "needs-clarification" label
       Review assumptions before implementation
```

---

## Example 6: Cross-Team Dependencies

**Scenario:** Stories have dependencies on other teams.

```
User: /d3:decompose 123456789

Agent: [Analyzes spec]

       Story 2 depends on: Authentication service (Platform team)
       Story 4 depends on: Payment gateway (Billing team)

       These are external dependencies. Options:

       **Option A:** Note dependencies in story descriptions
       **Option B:** Create stories anyway, flag as blocked
       **Option C:** Create investigation stories to clarify dependencies

User: Option A

Agent: Adding dependency notes:

       Story 2: User Profile Management
       - Dependencies: Requires Platform team's auth service (PLAT-156)
       - Coordination: Sync with Platform team before starting

       Story 4: Premium Features Checkout
       - Dependencies: Requires Billing team's gateway (BILL-89)
       - Coordination: Sync with Billing team before starting

       Create with dependency notes?

User: Yes

Agent: ✅ Created with external dependencies documented
       Coordinate with Platform and Billing teams before starting
```

---

## Tips for Effective Decomposition

1. **Use transcripts when available:** Captures team discussion and reasoning
2. **Follow INVEST:** Every story should meet all 6 criteria
3. **Default to full-stack:** Modern teams can deliver end-to-end
4. **Split by scope, not layers:** Split features, not frontend/backend
5. **Minimize dependencies:** Aim for parallel development
6. **Size consistently:** 1-10 days per story, similar sizing
7. **Complete acceptance criteria:** Cover happy path, errors, edge cases
8. **Link to spec:** Always reference source specification
9. **Validate before creating:** Use INVEST validation checklist
10. **Consider implementation order:** Dependencies affect sequence
