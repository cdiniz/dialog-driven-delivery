---
description: Decompose feature into user stories through conversational planning
---

Decompose a feature specification into independently deliverable user stories as markdown files using a conversational, engaging approach.

## Conversational Workflow

This command uses an **engaging, conversational approach**:
1. Accept feature name as argument
2. Read spec file and analyze specifications
3. Ask if there's a decomposition meeting transcript
4. Analyze transcript or work conversationally
5. Propose workflow-based story breakdown
6. Ask clarifying questions about boundaries
7. Create user story markdown files in docs/[feature-name]/
8. Provide clear summary

## Steps

### Step 1: Get Feature Name from Arguments

The command accepts the feature name as `$ARGUMENTS`:
- Feature directory name (e.g., `advanced-search-with-filters`)
- Will read from `docs/[feature-name]/spec.md`

**Use Read Tool:** Read the file at `docs/$ARGUMENTS/spec.md` to fetch the specification.

### Step 2: Read and Analyze Spec File

Read the spec file and display current state:

```markdown
I found feature specification: [Feature Name]

**Feature:** [Feature Name]
**File:** docs/[feature-name]/spec.md

**Product Spec:** [✅ Found or ❌ Not found]
**Technical Spec:** [✅ Found or ⏳ Minimal or ❌ Not found]

**Existing User Stories:** Checking for story files...
[List any existing .md files in docs/[feature-name]/ besides spec.md]

[If no specs found, show warning:]
⚠️ I couldn't find Product and Technical Specifications in this file.
I recommend ensuring the file contains both specs created by `/create-spec` before decomposing.

[If specs found:]
✅ Ready to decompose into user stories.
```

### Step 3: Read Both Specs from Spec File

Read **both Product and Technical specifications** from the spec file:

The spec file should contain both specs, structured as:

```markdown
## 📋 Product Specification
[Product spec content]

## 🔧 Technical Specification
[Technical spec content]
```

**Extract from Product Specification section:**
- Feature overview and business value
- Target users
- User workflows
- Functional requirements
- Non-functional requirements
- Business rules and validation
- Scope boundaries
- Open questions and assumptions

**Extract from Technical Specification section (if available):**
- Technical approach and architecture
- System changes (new components, modifications)
- Architecture diagrams
- Data models and database schema
- API contracts and endpoints
- UI components and interactions
- Integration points
- Testing requirements
- Technical open questions and assumptions

**If specs not found in spec file:**

If Product Spec not found:
- Warn: "⚠️ I couldn't find a Product Specification in the spec file. I recommend running `/create-spec` first. I'll proceed using the file content."

If Technical Spec is placeholder or not found:
- Note: "ℹ️ Technical Specification hasn't been created yet. I'll decompose based on Product Spec. For better technical guidance, consider running `/refine-spec [feature-name]` first."

### Step 4: Request Decomposition Meeting Input

Ask user if they have a decomposition meeting:

```markdown
Before I decompose this feature into user stories, did you have a story decomposition or planning meeting?

**Option A: Yes, I have a transcript** - Paste your decomposition meeting transcript
**Option B: No, let's decompose it together** - I'll help you break it down conversationally

Which would you prefer?
```

### Step 5: Analyze Decomposition Input

**If transcript provided (Option A):**

Analyze the transcript and extract:
- **Proposed Stories:** List of stories discussed
- **Story Boundaries:** How the team discussed breaking things down
- **Priority/Order:** Any mentioned priority or sequence
- **Open Questions:** Any unresolved decomposition questions
- **Concerns:** Any concerns about story size or dependencies

Summarize findings:

```markdown
I've analyzed your decomposition meeting transcript. Here's what I found:

**Proposed Stories ([N] stories):**
1. [Story 1 name/description]
2. [Story 2 name/description]
3. [Story 3 name/description]
4. [Continue with all stories]

**Decomposition Approach:**
[How the team discussed breaking things down - by workflow, by component, by layer, etc.]

**Priority Order:**
[If discussed: priority or sequence]

**Open Questions from Meeting:**
- [Question 1 about decomposition]
- [Question 2 about decomposition]

**Concerns Raised:**
- [Concern 1 about story size/complexity/dependencies]
- [Concern 2 about story size/complexity/dependencies]
```

**If conversational (Option B):**

Work through decomposition conversationally - see Step 6.

### Step 6: Propose Workflow-Based Decomposition

Based on the feature spec, technical spec, and transcript (if available), propose a workflow-based decomposition where each story delivers one complete user workflow end-to-end.

```markdown
Based on the feature spec and technical spec, here's how I propose to break this down by user workflow:

**Proposed Stories ([N] stories):**

**Story 1: [Workflow 1 from feature spec]**
- Delivers: [What user value this provides]
- Scope: [Frontend/Backend/Full-stack]
- Key ACs: [Main scenarios]

**Story 2: [Workflow 2 from feature spec]**
- Delivers: [What user value this provides]
- Scope: [Frontend/Backend/Full-stack]
- Key ACs: [Main scenarios]

**Story 3: [Workflow 3 from feature spec]**
- Delivers: [What user value this provides]
- Scope: [Frontend/Backend/Full-stack]
- Key ACs: [Main scenarios]

[Continue for all workflows]

Each story delivers complete user value and can be demoed independently.

Before I finalize these, I have a few questions about the boundaries...
```

[Proceed directly to clarifying questions]

### Step 7: Ask Clarifying Questions

Based on the proposed workflow-based decomposition, ask targeted questions:

**Questions About Story Boundaries:**
```markdown
Let me clarify the story boundaries:

1. **Story Scope:**
   [If stories are workflows:] Should "[Workflow Name]" be one story or split into multiple steps?

2. **Dependencies:**
   Can these stories be implemented independently, or do some depend on others?

   If there are dependencies, what's the required order?

3. **Story Size:**
   Looking at the acceptance criteria, does story "[Story Name]" seem too large?

   Should we split it further? If so, how?

4. **Edge Cases:**
   Should error handling, validation, and edge cases be:
   - Included in each story's acceptance criteria?
   - Separate stories for complex error scenarios?

5. **Non-Functional Requirements:**
   Should performance, security, accessibility be:
   - Included in relevant functional stories?
   - Separate "technical debt" or "NFR" stories?

6. **Priority/Order:**
   What's the priority order for these stories?

   Which story should be implemented first?
```

[Adjust questions based on the specific feature and decomposition approach]

### Step 8: Propose Story Breakdown

Based on all gathered information, propose the final story breakdown:

```markdown
Perfect! Based on our discussion, here's how I propose to break down this feature:

**Story 1: [Story Title]**
- **Focus:** [What this story delivers]
- **Scope:** [Frontend/Backend/Full-stack]
- **Acceptance Criteria:** [N] scenarios covering:
  - [Main scenario]
  - [Error scenario]
  - [Edge case scenario]
- **Dependencies:** [None or references to other stories]
- **Estimated Scope:** [Small/Medium/Large]

**Story 2: [Story Title]**
- **Focus:** [What this story delivers]
- **Scope:** [Frontend/Backend/Full-stack]
- **Acceptance Criteria:** [N] scenarios covering:
  - [Main scenario]
  - [Error scenario]
  - [Edge case scenario]
- **Dependencies:** [None or references to other stories]
- **Estimated Scope:** [Small/Medium/Large]

[Continue for all stories]

**Total:** [N] stories

**Implementation Order:**
1. [Story X] - Foundation
2. [Story Y] - Builds on X
3. [Story Z] - Enhancement
[Continue with recommended order]

Does this decomposition look good, or would you like to adjust any stories?
```

[Wait for user confirmation or adjustments]

### Step 9: Create User Story Files

Create individual markdown files for each user story in the feature directory:

```markdown
Creating user story files in docs/[feature-name]/...
```

**File Naming Convention:**
- `story-01-[kebab-case-title].md`
- `story-02-[kebab-case-title].md`
- etc.

**Use Write Tool:** Create each story file at `docs/[feature-name]/story-[NN]-[title].md`

For each approved story, show progress:
```markdown
✅ Created story-01-[title].md
✅ Created story-02-[title].md
[Continue for all stories]
```

### Step 10: Story File Format

**IMPORTANT - Uncertainty Handling in Stories:**

Before creating story files, review **both Product and Technical specs** from the spec file for any remaining uncertainty markers (`[OPEN QUESTION]`, `[DECISION PENDING]`, `[CLARIFICATION NEEDED]`). See @.claude/uncertainty-markers.md for complete marker definitions.

**If critical uncertainties still exist:**
- Warn the user that stories may need refinement once uncertainties are resolved
- Add a note in the story frontmatter: `blocked_by: "uncertainties in spec.md"`
- Include a reference to the uncertainty in the story description
- Link back to the spec file for full context

**For each story, create with these guidelines:**
- If an AC references an `[OPEN QUESTION]` from the Product Spec, note it in the story with link to spec.md
- If implementation depends on a `[DECISION PENDING]` from the Technical Spec, add to description with link
- Stories with unresolved uncertainties should be marked with `status: blocked`
- Always link back to `spec.md` for full context

For each approved story, create a markdown file with complete details:

**Use Write Tool:** Create markdown file using template from @.claude/templates/user-story.md

**Story File Structure:**
```markdown
---
title: [Clear, action-oriented title, 3-7 words]
status: todo
priority: medium
tags: [frontend, backend, api, etc.]
dependencies: []
blocked_by: ""
story_number: [NN]
---

# [Story Title]

**User Story:** As a [persona], I want [capability], so that [benefit]

**Value:** [What value this delivers to users/business]

**Feature Spec:** [../spec.md](../spec.md)

---

## Acceptance Criteria

**AC1: [Scenario name]**
**Given** [context]
**When** [action]
**Then** [expected outcome]

**AC2: [Scenario name]**
**Given** [context]
**When** [action]
**Then** [expected outcome]

[Continue with all ACs]

---

## Technical Notes

[Any technical considerations from technical spec]

**Dependencies:** [List other story filenames if dependencies exist, e.g., "story-01-*.md"]

**References:**
- Feature Spec: [spec.md](./spec.md)
- Related Technical Docs: [If applicable]
```

**Story Frontmatter Fields:**
- **title:** Story title (3-7 words)
- **status:** `todo`, `in_progress`, `done`, or `blocked`
- **priority:** `low`, `medium`, `high`
- **tags:** Array of tags like `["frontend", "backend", "api"]`
- **dependencies:** Array of story numbers this depends on (e.g., `[1, 2]`)
- **blocked_by:** Description of blocker if status is `blocked`
- **story_number:** Sequential number (1, 2, 3, etc.)

### Step 11: Provide Comprehensive Summary

After creating all stories, provide a detailed summary:

```markdown
✅ Feature decomposed successfully!

**Feature:** [Feature Name]
**Directory:** docs/[feature-name]/
**Spec File:** docs/[feature-name]/spec.md

**Stories Created:** [N] user stories

**Story Breakdown:**

1. **story-01-[title].md**
   - Status: todo
   - Scope: [Frontend/Backend/Full-stack]
   - Focus: [1-line description]
   - ACs: [N] acceptance criteria
   - Dependencies: [None or "Depends on story-XX"]
   - Tags: [Tags applied]

2. **story-02-[title].md**
   - Status: todo
   - Scope: [Frontend/Backend/Full-stack]
   - Focus: [1-line description]
   - ACs: [N] acceptance criteria
   - Dependencies: [None or "Depends on story-XX"]
   - Tags: [Tags applied]

[Continue for all stories]

**Decomposition Approach:**
[Summary of the decomposition strategy used: by workflow, by layer, hybrid, etc.]

**Implementation Order:**
Based on dependencies and value delivery, recommended order:
1. story-01-[title] - Foundation story, no dependencies
2. story-02-[title] - Builds on previous story
3. story-03-[title] - Enhancement, can be done in parallel
[Continue with recommended order]

**Coverage:**
- ✅ All user workflows from feature spec covered
- ✅ All functional requirements addressed
- ✅ Error handling and validation included
- ✅ Edge cases and empty states covered
- ✅ Non-functional requirements distributed across stories

**Next Steps:**

**Immediate:**
1. ✅ Review all story files in docs/[feature-name]/ and verify acceptance criteria
2. Update story status as you work on them (edit the `status` field in frontmatter)
3. Track dependencies between stories using the `dependencies` field

**For Implementation:**
1. Start with: story-01-[title].md
2. Implement story (optional): `/implement-story`
   - Provide story file path
   - Agent creates implementation plan and executes
   - See CODING_README.md for complete workflow

**For Refinement:**
If you need to adjust the decomposition (split, merge, add stories):
- Edit story markdown files directly
- Create new story files if needed
- Update the feature spec if requirements changed: `/refine-spec [feature-name]`

The feature is now fully decomposed and ready for implementation! 🎉
```

## Guidelines

### Conversational Best Practices

1. **Show Current State**: Always display page state before asking questions
2. **Propose Workflow-Based Breakdown**: Present stories based on user workflows from the feature spec
3. **Explain Reasoning**: When suggesting story boundaries, explain why
4. **Ask Clarifying Questions**: Adapt to team structure (split by layer if needed)
5. **Confirm Before Creating**: Show proposed breakdown and get approval
6. **Reference Documentation**: Connect stories to Confluence page
7. **Discuss Dependencies**: Make dependencies explicit

### Transcript Analysis Tips

1. **Extract Story Ideas**: Look for mentions of "story," "we should," "what if"
2. **Note Disagreements**: If team debated boundaries, capture both perspectives
3. **Identify Concerns**: Note concerns about story size, complexity, dependencies
4. **Find Priority**: Look for discussion about what to build first
5. **Spot Gaps**: Identify workflows or requirements not mentioned in decomposition

### Decomposition Best Practices

1. **Natural Boundaries**: Break at logical points (complete workflows, layers, entities)
2. **Independent Stories**: Minimize dependencies between stories
3. **End-to-End Value**: Each story should deliver visible value (especially first story)
4. **Consistent Size**: Aim for stories of similar size (adjust based on team velocity)
5. **Complete ACs**: Every story should have comprehensive acceptance criteria
6. **Cover All Cases**: Include happy path, errors, edge cases, empty states

### Acceptance Criteria Quality

1. **Use Gherkin Format**: Given-When-Then structure for clarity
2. **Descriptive Names**: AC titles should explain the scenario
3. **Specific Values**: Use actual data/values, not placeholders
4. **Exact Error Messages**: Include exact error text from feature spec
5. **Observable Behavior**: Focus on what users see/experience
6. **Complete Workflows**: Cover entire user journey, not just happy path
7. **Reference Requirements**: Map ACs back to feature spec requirements

### Story Size Guidelines

**Small Story (1-3 days):**
- Single UI component
- Single API endpoint
- Simple CRUD operation
- 3-5 acceptance criteria

**Medium Story (3-5 days):**
- Multiple related components
- Multiple related endpoints
- Complete workflow (simple)
- 5-8 acceptance criteria

**Large Story (5-10 days):**
- Complex workflow
- Multiple layers (frontend + backend + integration)
- Significant business logic
- 8-12 acceptance criteria

**Too Large (>10 days):**
- Should be split into smaller stories
- Ask user how to split

### Decomposition Strategy

**This command uses "By User Workflow" decomposition:**
- Each story = one complete user journey end-to-end
- Each story delivers user value independently
- Each story can be demoed to stakeholders
- Stories align naturally with the feature spec's user workflows

**Key Benefits:**
- Clear user value in every story
- Easy to prioritize by user impact
- Aligns with product requirements
- Natural mapping to feature spec workflows

**When workflows span multiple layers:**
If your team has separate frontend/backend teams, you can still split individual workflows by layer during the clarifying questions phase. The decomposition will adapt to your team structure while maintaining the workflow-based foundation.


## Error Handling

If something goes wrong:

1. **No Product Spec in file**: Warn but continue using spec file content
2. **No Technical Spec in file**: Note that it's optional, continue with Product Spec
3. **Spec file not found**: Verify feature name and check if docs/[feature-name]/spec.md exists
4. **File creation fails**: Provide story content for manual creation
5. **Unclear Boundaries**: Ask specific questions about how to split
6. **Incomplete Transcript**: Identify gaps and work conversationally to fill them
7. **Invalid feature name**: Verify the feature directory exists

## Examples

### Example: Transcript-Based Decomposition

```
User: /decompose-feature 123456789

Agent: I found Confluence Page: Advanced Search with Filters

       Product Spec: ✅ Found in page
       Technical Spec: ✅ Found in page

       Which Jira project should I create the user stories in?

User: PROJ

Agent: Great! I'll create stories in Jira project PROJ.

       Before I decompose this feature, did you have a story decomposition meeting?

       **Option A: Yes, I have a transcript**
       **Option B: No, let's decompose it together**

User: Option A
      [Pastes meeting transcript]

Agent: I've analyzed your decomposition meeting transcript. Here's what I found:

       **Proposed Stories (5 stories):**
       1. Basic text search backend API
       2. Basic text search frontend UI
       3. Add status filter (backend + frontend)
       4. Add assignee and date filters
       5. Save filter presets

       **Approach:**
       The team discussed splitting the first workflow (basic search) by layer
       since you have separate backend/frontend teams, then keeping subsequent
       filter workflows as full-stack stories.

       Let me clarify some boundaries:

       1. Should error handling be included in each story's ACs, or separate
          stories?

       2. Story 4 includes assignee AND date filters - should these be split
          into separate stories for smaller scope?

       3. What's the dependency order - does story 2 (frontend) need story 1
          (backend) completed first?

User: 1. Include error handling in each story
      2. Keep story 4 as is - both filters together is fine
      3. Yes, story 2 depends on story 1

Agent: Perfect! Here's the final decomposition:

       [Shows 5 stories with details]

       Does this look good?

User: Yes, create them

Agent: Creating Epic for this feature in Jira Project PROJ...

       ✅ Created Epic PROJ-41: Advanced Search with Filters
          https://yoursite.atlassian.net/browse/PROJ-41

       Now creating 5 user stories under this Epic...

       ✅ Created PROJ-42: Basic text search - Backend API (under Epic PROJ-41)
       ✅ Created PROJ-43: Basic text search - Frontend UI (under Epic PROJ-41)
       ✅ Created PROJ-44: Add status filter (under Epic PROJ-41)
       ✅ Created PROJ-45: Add assignee and date filters (under Epic PROJ-41)
       ✅ Created PROJ-46: Save filter presets (under Epic PROJ-41)

       ✅ Feature decomposed successfully!

       [Shows summary with Epic details and manual dependency linking instructions]
```

### Example: Conversational Decomposition

```
User: /decompose-feature Advanced Search

Agent: [Searches and finds Confluence page]
       I found Confluence Page: Advanced Search with Filters

       [Shows current state]

       Which Jira project should I create stories in?

User: ENG

Agent: Did you have a decomposition meeting?

       **Option A: Yes, I have a transcript**
       **Option B: No, let's decompose it together**

User: Option B

Agent: Based on the feature spec, here's how I propose to break this down by
       user workflow:

       **Proposed Stories (4 stories):**

       **Story 1: Basic text search**
       - Delivers: Users can search for items using text input
       - Scope: Full-stack (backend API + frontend UI)
       - Key ACs: Search input, results display, empty states, error handling

       **Story 2: Add filter by status**
       - Delivers: Users can filter search results by item status
       - Scope: Full-stack (backend filtering + frontend filter UI)
       - Key ACs: Status dropdown, filtered results, clear filters

       **Story 3: Add filter by assignee and date**
       - Delivers: Users can filter by assignee and date range
       - Scope: Full-stack (backend filtering + frontend filter UI)
       - Key ACs: Assignee selector, date pickers, multiple filters

       **Story 4: Save filter presets**
       - Delivers: Users can save and reuse their filter combinations
       - Scope: Full-stack (backend persistence + frontend preset UI)
       - Key ACs: Save preset, load preset, manage presets

       Each story delivers complete user value and can be demoed independently.

       Before I finalize these, a few questions:

       1. Story 1 spans both backend and frontend - should we split it into
          two stories (API + UI) or keep it as one end-to-end story?

       2. Should error handling and edge cases be included in each story's ACs?

       3. What's your preferred implementation order?

User: 1. Split story 1 into backend and frontend - we have separate teams
      2. Yes, include error handling in each story
      3. Backend first, then frontend, then the filter stories

Agent: Perfect! Here's the updated breakdown:

       1. Basic text search - Backend API
       2. Basic text search - Frontend UI (depends on story 1)
       3. Add filter by status (backend + frontend)
       4. Add filter by assignee and date (backend + frontend)
       5. Save filter presets (backend + frontend)

       [Shows details for each story with dependencies]

       Does this work for your team structure?

User: Yes, create them!

Agent: Creating Epic for this feature in Jira Project ENG...

       ✅ Created Epic ENG-100: Advanced Search with Filters
          https://yoursite.atlassian.net/browse/ENG-100

       Now creating 5 user stories under this Epic...

       ✅ Created ENG-101: Basic text search - Backend API
       ✅ Created ENG-102: Basic text search - Frontend UI
       ✅ Created ENG-103: Add filter by status
       ✅ Created ENG-104: Add filter by assignee and date
       ✅ Created ENG-105: Save filter presets

       ✅ Feature decomposed successfully!

       Epic: ENG-100
       Stories: 5 stories (ENG-101 to ENG-105)

       [Shows summary with manual dependency linking instructions]
```

## Important Notes

- **Requires $ARGUMENTS**: Must provide feature name (directory name)
- **Reads from markdown**: Fetches both Product and Technical specs from docs/[feature-name]/spec.md
- **Creates story files**: Creates individual markdown files for each user story in docs/[feature-name]/
- **File naming**: Uses `story-NN-[title].md` format for easy sorting
- **Frontmatter tracking**: Each story has structured frontmatter (status, priority, tags, dependencies)
- **Dependencies tracked**: Dependencies tracked via `dependencies` array in frontmatter
- **Git-tracked**: All stories are version controlled alongside code
- **Transcript is Optional**: Preferred but can work conversationally
- **Workflow-Based Decomposition**: Always decomposes by user workflow for maximum value delivery
- **Adapts to Team Structure**: Can split workflows by layer during clarifying questions if needed
- **Confirms Before Creating**: Shows proposed breakdown for approval
- **Complete ACs**: Every story gets comprehensive acceptance criteria
- **Maps to Specs**: References spec.md file in each story
- **Explicit Dependencies**: Dependencies tracked in frontmatter and documented in story descriptions
- **Suggests Order**: Recommends implementation order based on dependencies
- **Links Back**: Stories link back to spec.md for full context

This streamlined, opinionated approach ensures stories are well-thought-out, deliver user value, and have comprehensive acceptance criteria while being fast and collaborative.
