---
description: Refine existing technical spec based on meeting transcript or conversation
---

You are tasked with refining an existing technical specification in a Linear Project based on new discussions, decisions, or changes.

## Conversational Workflow

This command uses an **engaging, conversational approach**:
1. Accept Linear Project ID as argument
2. Fetch project and show current state
3. Read existing technical spec from Linear project description
4. Ask for refinement input (transcript or conversation)
5. Analyze what needs to be updated
6. Ask clarifying questions
7. Show proposed changes (before/after)
8. Update Linear project description
9. Provide clear summary

## Steps

### Step 1: Get Project ID from Arguments

The command accepts the Linear Project as `$ARGUMENTS`:
- Project Key (e.g., `PROJ-42`)
- Project Name (e.g., `Advanced Search`)
- Project ID (UUID)

### Step 2: Fetch and Analyze Project

Query Linear for the project and display current state:

```markdown
I found Linear Project $ARGUMENTS:

**Project:** [PROJECT-KEY] - [Project Name]
**URL:** [Linear Project URL]
**Status:** [Current status]
**Team:** [Team name]

**Current Documentation:**
- **Product Spec:** [✅ Found in Linear project description or ❌ Not found]
- **Technical Spec:** [✅ Found in Linear project description or ⏳ Placeholder or ❌ Not found]

**User Stories:** [N] stories
[If stories exist, list a few:]
- [ISSUE-1]: [Title] - [Status]
- [ISSUE-2]: [Title] - [Status]
```

### Step 3: Read Existing Technical Spec

Read the **Technical Specification** from the Linear project description.

The Linear project description should contain:

```markdown
## 📋 Product Specification
[Product spec content]

## 🔧 Technical Specification
[Technical spec content - THIS IS WHAT WE'LL REFINE]
```

**Extract from Technical Specification section:**
- Technical approach and architecture
- System changes (new components, modifications)
- Architecture diagrams
- Data models and database schema
- API contracts and endpoints
- UI components and interactions
- Integration points
- Testing requirements
- Open questions and assumptions

**If Technical Spec not found or is placeholder:**

Show clear error:
```markdown
❌ I couldn't find an existing Technical Specification in the Linear project description.

This command is for refining EXISTING technical specs. To create a new technical spec, use:
`/create-technical-spec [PROJECT-KEY]`

Would you like me to create a new technical spec instead?
```

### Step 4: Show Current Technical Spec Summary

Before asking for refinement input, show a summary of what exists:

```markdown
**Current Technical Specification Summary:**

**Sections Present:**
- ✅ Section 1: Technical Approach
- ✅ Section 2: System Changes
- ✅ Section 3: Architecture (with [N] diagrams)
- ✅ Section 4: Architectural Context
- ✅ Section 5: Technical Specifications
  - API Contracts: [N] endpoints
  - Data Models: [N] entities
  - Event Models: [N] events
- ✅ Section 6: Integrations
  - Internal: [N] integrations
  - External: [N] integrations
  - Dependencies: [N] new libraries
- ✅ Section 7: Testing Requirements
- ✅ Section 8: Open Questions
  - [N] open questions
  - [N] assumptions

**Key Technical Decisions:**
- [List 3-5 major technical decisions from the spec]

**Current Open Questions:**
[If any exist, list them:]
- [ ] Q1: [Question text]
- [ ] Q2: [Question text]

**Last Updated:** [If available from Linear metadata]
```

### Step 5: Request Refinement Input

Ask user what prompted the refinement and how they want to provide information:

```markdown
What prompted this technical spec refinement?

**Common Reasons:**
- New technical decisions were made
- Architecture needs to be updated based on learnings
- New integrations or dependencies discovered
- Performance or security concerns identified
- Implementation revealed gaps or issues
- Technical constraints changed

How would you like to provide the refinement information?

**Option A: Refinement Meeting Transcript** - Paste transcript from your technical discussion
**Option B: Describe Changes Conversationally** - We'll discuss the changes together

Which would you prefer?
```

### Step 6: Analyze Refinement Input

**If transcript provided (Option A):**

Analyze the transcript and extract:
- **What's Changing:** Specific sections or decisions being updated
- **Why It's Changing:** Reason for the change (new info, mistake, learning)
- **New Technical Decisions:** Any new technical choices made
- **Resolved Questions:** Any open questions now answered
- **New Questions:** Any new uncertainties discovered
- **Impact:** How this affects existing implementation or stories

Summarize findings:

```markdown
I've analyzed your refinement meeting transcript. Here's what I found:

**Changes Requested:**

1. **[Section/Topic]:** [What needs to change]
   - **Current State:** [What it says now]
   - **Requested Change:** [What it should say]
   - **Reason:** [Why this change is needed]

2. **[Section/Topic]:** [What needs to change]
   - **Current State:** [What it says now]
   - **Requested Change:** [What it should say]
   - **Reason:** [Why this change is needed]

[Continue for all identified changes]

**Questions Resolved:**
- ✅ [Previously open question that's now answered]
- ✅ [Previously open question that's now answered]

**New Questions Discovered:**
- ❓ [New question that emerged from discussion]
- ❓ [New question that emerged from discussion]

**Potential Impact:**
- [Impact on existing user stories]
- [Impact on implementation approach]
- [Impact on timeline or resources]
```

**If conversational (Option B):**

Ask structured questions:
```markdown
Let's discuss what needs to be refined in the technical spec.

1. Which sections need updating?
   - Technical Approach?
   - Architecture?
   - Data Models?
   - API Contracts?
   - Integrations?
   - Other?

2. What triggered this refinement?
   - New information discovered?
   - Implementation challenges?
   - Performance concerns?
   - Security issues?
   - Changed requirements?

3. What specifically needs to change?
```

### Step 7: Ask Clarifying Questions

Based on the identified changes, ask targeted questions:

```markdown
Let me clarify some details about these changes:

**For [Change 1]:**
1. [Specific question about the technical approach]
2. [Question about backward compatibility]
3. [Question about data migration if applicable]

**For [Change 2]:**
1. [Specific question about implementation details]
2. [Question about testing impact]
3. [Question about dependencies]

**General Questions:**
1. Should I update any architecture diagrams to reflect these changes?
2. Are there any new dependencies or integrations needed?
3. Do any existing open questions now have answers?
4. Are there new open questions or assumptions to add?
5. How does this affect existing user stories? Should they be flagged for review?
```

### Step 8: Review Codebase for Pattern Changes

If the refinement involves significant technical changes, review the codebase:

```markdown
Let me quickly review the codebase to ensure the refined spec aligns with current patterns...

[Review relevant code to understand:]
- Current architecture patterns
- Existing data models
- API conventions
- Testing patterns
- Integration approaches

I've reviewed the codebase. Here's what I found:
- [Relevant finding 1]
- [Relevant finding 2]
- [Any conflicts or alignment with proposed changes]
```

### Step 9: Show Proposed Changes (Before/After)

**CRITICAL - Present clear before/after for each change:**

```markdown
Here are the proposed changes to the Technical Specification:

---

### Change 1: [Section/Topic Name]

**BEFORE:**
```
[Current text from the spec - show enough context]
```

**AFTER:**
```
[Proposed updated text with changes highlighted in context]
```

**Rationale:** [Why this change is being made]
**Impact:** [How this affects implementation]

---

### Change 2: [Section/Topic Name]

**BEFORE:**
```
[Current text]
```

**AFTER:**
```
[Proposed text]
```

**Rationale:** [Why this change]
**Impact:** [How this affects implementation]

---

[Continue for all changes]

**Summary of Changes:**
- [N] sections updated
- [N] open questions resolved
- [N] new questions added
- [N] assumptions added/updated
- [N] architecture diagrams updated

**Sections Modified:**
- ✏️ Section X: [Section name]
- ✏️ Section Y: [Section name]
- ✏️ Section Z: [Section name]

Does this look correct? Should I proceed with updating the Linear project description?
```

### Step 10: Apply Uncertainty Markers to New/Updated Content

**CRITICAL - Uncertainty Marker Policy for Refinements:**

Review the documentation in `.claude/uncertainty-markers.md`.

When refining the specification, follow these rules:

1. **If new information is vague** → Use `[CLARIFICATION NEEDED: what needs defining]`
2. **If new technical decision is deferred** → Use `[DECISION PENDING: option A vs option B]`
3. **If you make new inferences** → Use `[ASSUMPTION: statement]`
4. **If new questions arise** → Use `[OPEN QUESTION: question]`
5. **If resolving an existing marker** → Remove the marker and add the resolved value

**Examples:**

❌ BAD (removes old marker but makes new silent assumption):
```
BEFORE: Database will use [DECISION PENDING: PostgreSQL vs MongoDB]
AFTER: Database will use PostgreSQL with connection pooling of 50 connections
```

✅ GOOD (resolves decision, marks new assumption):
```
BEFORE: Database will use [DECISION PENDING: PostgreSQL vs MongoDB]
AFTER: Database will use PostgreSQL with connection pooling of [ASSUMPTION: 50 connections - based on expected load, needs validation]
```

**Validation:**
- Count all new/updated uncertainty markers
- Link all markers to Section 8 (Open Questions & Assumptions)
- Show uncertainty summary to user

### Step 11: Update Linear Project Description

Update the Technical Specification section in the Linear project description:

```markdown
Updating Technical Specification in Linear Project [PROJECT-KEY]...

✅ Linear project description updated
✅ Technical Spec section modified
✅ [N] sections updated
✅ [N] uncertainties resolved
✅ [N] new uncertainties added (if any)

**Linear Project URL:** [URL to view updated spec]
```

### Step 12: Provide Comprehensive Summary

After updating, provide a detailed summary:

```markdown
✅ Technical specification refined successfully!

**Linear Project:** [PROJECT-KEY] - [Project Name]
**URL:** [Project URL]

**Refinement Summary:**

**Sections Modified:** [N] sections
- Section 1: Technical Approach - [✏️ Updated / ✅ No change]
- Section 2: System Changes - [✏️ Updated / ✅ No change]
- Section 3: Architecture - [✏️ Updated / ✅ No change / ➕ Added diagrams]
- Section 4: Architectural Context - [✏️ Updated / ✅ No change]
- Section 5: Technical Specifications - [✏️ Updated / ✅ No change]
  - API Contracts: [Changes made]
  - Data Models: [Changes made]
  - Event Models: [Changes made]
- Section 6: Integrations - [✏️ Updated / ✅ No change / ➕ Added integrations]
- Section 7: Testing Requirements - [✏️ Updated / ✅ No change]
- Section 8: Open Questions - [✏️ Updated / ✅ No change]

**Key Changes Made:**

1. **[Change 1 Title]**
   - What changed: [Brief description]
   - Why: [Reason]
   - Impact: [How this affects implementation]

2. **[Change 2 Title]**
   - What changed: [Brief description]
   - Why: [Reason]
   - Impact: [How this affects implementation]

[Continue for major changes]

**Questions Resolved:** [N] questions
- ✅ [Question that was resolved]
- ✅ [Question that was resolved]

**New Questions Added:** [N] questions
[If any:]
- ❓ [New question]
- ❓ [New question]

**Uncertainty Status:**
[If new uncertainties exist:]
⚠️ The refined spec contains [N] new/updated uncertainties:
- [X] open questions requiring decisions (Section 8)
- [Y] clarifications needed (Section 8)
- [Z] new assumptions that need validation (Section 8)

[If no new uncertainties:]
✅ No new unresolved uncertainties introduced.

**Impact on User Stories:**

[If stories might be affected:]
⚠️ These changes may impact existing user stories:
- [ISSUE-XX]: [Story Title] - [Why it might be affected]
- [ISSUE-YY]: [Story Title] - [Why it might be affected]

**Recommended Actions:**
1. Review the updated Technical Spec in Linear: [URL]
2. [If stories affected:] Review impacted user stories and update if needed
3. [If new questions:] Schedule follow-up discussion to resolve new open questions
4. [If assumptions:] Validate new assumptions with the team
5. Communicate changes to the development team

**What Changed vs What Stayed:**
- ✏️ Updated: [List key sections that changed]
- ✅ Unchanged: [List sections that stayed the same]
- ➕ Added: [List any new sections or content]

**Collaboration:**
- View refined spec in Linear: [Project URL]
- Both Product and Technical specs remain in the Linear project description
- Team members can comment on the updated spec directly in Linear

**Next Steps:**
1. [If uncertainties:] Resolve new open questions in Section 8
2. [If stories affected:] Update affected user stories with new technical guidance
3. Share updates with the team
4. [If needed:] Schedule another refinement session if more changes emerge
```

## Guidelines

### Conversational Best Practices

1. **Show What Exists First**: Always display current state before asking for changes
2. **Be Specific About Changes**: Show exact before/after for clarity
3. **Explain Impact**: Help user understand how changes affect implementation
4. **Confirm Before Updating**: Show all proposed changes and get approval
5. **Reference Codebase**: Align refined spec with actual code patterns
6. **Track Uncertainties**: Apply uncertainty markers to new/vague content
7. **Flag Story Impact**: Identify which user stories might need updates

### Transcript Analysis Tips for Refinement

1. **Identify Change Type**: Addition, modification, deletion, or clarification?
2. **Find Root Cause**: Why is this change needed? (learning, mistake, new requirement)
3. **Extract Decisions**: What technical decisions were made?
4. **Note Disagreements**: If discussion shows debate, capture both perspectives
5. **Spot Dependencies**: What else might need to change as a result?

### Refinement Quality

1. **Minimal Changes**: Only update what needs updating, preserve the rest
2. **Clear Rationale**: Document why each change is being made
3. **Consistency**: Ensure changes are consistent across all affected sections
4. **Architecture Alignment**: Update diagrams if architecture changes
5. **Complete Updates**: If changing data model, update related API contracts too
6. **Preserve History**: Document what changed and why in the summary

### Change Categories

**Common Refinement Types:**

1. **Clarification**: Making vague sections more specific
2. **Correction**: Fixing incorrect technical decisions or assumptions
3. **Addition**: Adding new technical details or sections
4. **Simplification**: Removing unnecessary complexity
5. **Update**: Changing approach based on new information
6. **Resolution**: Answering previously open questions
7. **Integration**: Adding new external or internal integrations

### Before/After Quality

**Good Before/After shows:**
- Enough context to understand what's changing
- Exact location in the spec (section number, heading)
- Complete content (not truncated mid-sentence)
- Clear highlighting of what's different
- Rationale for the change

**Example:**

✅ GOOD:
```
**BEFORE (Section 5.1 - API Contracts):**
POST /api/tasks
- Returns 201 on success
- Authentication required

**AFTER (Section 5.1 - API Contracts):**
POST /api/tasks
- Request body: {title: string, description?: string, dueDate?: ISO8601}
- Returns 201 with created task object on success
- Returns 400 if validation fails with error details
- Authentication required (JWT Bearer token)
- Rate limit: 100 requests/minute per user

**Rationale:** Implementation revealed we need explicit validation rules and rate limiting wasn't specified
```

### Uncertainty Marker Guidelines for Refinements

1. **Resolving Markers**: When refining, check if any existing markers can be resolved
2. **Adding Markers**: If new content is vague or uncertain, mark it explicitly
3. **Updating Markers**: If partially resolving, update the marker to reflect new status
4. **Removing Markers**: Only remove when uncertainty is fully resolved

## Error Handling

If something goes wrong:

1. **No Technical Spec Found**: Guide user to `/create-technical-spec` instead
2. **Technical Spec is Placeholder**: Guide user to `/create-technical-spec` instead
3. **Unclear Changes**: Ask specific questions about what needs updating
4. **Conflicting Changes**: Present the conflict and ask user to clarify
5. **Incomplete Transcript**: Identify gaps and work conversationally to fill them
6. **Linear Update Fails**: Provide the refined spec text so user can manually update

## Examples

### Example: Transcript-Based Refinement

```
User: /refine-technical-spec PROJ-42

Agent: I found Linear Project PROJ-42: Advanced Search with Filters

       **Current Documentation:**
       - Product Spec: ✅ In Linear project description
       - Technical Spec: ✅ In Linear project description

       **Current Technical Specification Summary:**

       **Sections Present:**
       - ✅ Section 1: Technical Approach (REST API with Elasticsearch)
       - ✅ Section 5: Technical Specifications
         - API Contracts: 3 endpoints
         - Data Models: 2 entities
       - ✅ Section 8: Open Questions: 2 questions

       **Key Technical Decisions:**
       - Using Elasticsearch for full-text search
       - REST API with JWT authentication
       - React frontend with Redux state management

       What prompted this technical spec refinement?

       **Option A: Refinement Meeting Transcript**
       **Option B: Describe Changes Conversationally**

User: Option A
      [Pastes transcript discussing switch from Elasticsearch to PostgreSQL
       full-text search due to infrastructure constraints]

Agent: I've analyzed your refinement meeting transcript. Here's what I found:

       **Changes Requested:**

       1. **Search Technology:** Switch from Elasticsearch to PostgreSQL full-text search
          - Current State: Uses Elasticsearch for indexing and search
          - Requested Change: Use PostgreSQL native full-text search with tsvector
          - Reason: Infrastructure team doesn't want to maintain Elasticsearch cluster;
                    PostgreSQL full-text search is sufficient for our needs

       2. **Architecture Diagram:** Update to remove Elasticsearch component
          - Current State: Shows separate Elasticsearch cluster
          - Requested Change: Show search happening within PostgreSQL
          - Reason: Reflect the new architecture

       3. **Performance Requirements:** Adjust performance expectations
          - Current State: Sub-100ms search response time
          - Requested Change: Sub-500ms acceptable given simpler architecture
          - Reason: PostgreSQL full-text search is slightly slower but acceptable

       **Questions Resolved:**
       - ✅ Q1: "Should we use Elasticsearch or Algolia?" → Resolved: PostgreSQL

       **Potential Impact:**
       - Existing user stories may need updated acceptance criteria for performance
       - Data model needs tsvector columns added
       - API implementation approach changes (simpler)

       Let me review the codebase patterns for PostgreSQL usage...

       I found you already use PostgreSQL with TypeORM. The full-text search can use
       native PostgreSQL features with generated tsvector columns.

       Here are the proposed changes:

       ---

       ### Change 1: Technical Approach (Section 1)

       **BEFORE:**
       ```
       We will implement search using Elasticsearch to provide fast, full-text search
       capabilities. Search requests will be proxied to the Elasticsearch cluster,
       which maintains synchronized indexes of task data.
       ```

       **AFTER:**
       ```
       We will implement search using PostgreSQL native full-text search with tsvector
       columns. This provides sufficient search performance (<500ms) without requiring
       additional infrastructure. The search uses PostgreSQL's GIN indexes for
       efficient text querying.
       ```

       **Rationale:** Infrastructure team preference + sufficient performance
       **Impact:** Simpler architecture, easier maintenance, slightly slower search

       ---

       ### Change 2: Architecture Diagram (Section 3)

       **BEFORE:**
       [Diagram showing: React -> API -> PostgreSQL + Elasticsearch]

       **AFTER:**
       [Diagram showing: React -> API -> PostgreSQL (with full-text search)]

       **Rationale:** Remove Elasticsearch component from architecture
       **Impact:** Simpler deployment and operations

       ---

       ### Change 3: Data Models (Section 5.2)

       **BEFORE:**
       ```typescript
       interface Task {
         id: string;
         title: string;
         description?: string;
         // ... other fields
       }
       ```

       **AFTER:**
       ```typescript
       interface Task {
         id: string;
         title: string;
         description?: string;
         searchVector: string; // tsvector - generated column for full-text search
         // ... other fields
       }
       ```

       **Rationale:** Need tsvector column for PostgreSQL full-text search
       **Impact:** Database migration required

       ---

       **Summary of Changes:**
       - 3 sections updated
       - 1 open question resolved
       - 1 architecture diagram updated
       - Database migration required

       Does this look correct? Should I proceed with updating the Linear project?

User: Yes, proceed

Agent: [Updates Linear and provides comprehensive summary]
```

### Example: Conversational Refinement

```
User: /refine-technical-spec PROJ-42

Agent: [Shows current state]

       What prompted this technical spec refinement?

       **Option A: Refinement Meeting Transcript**
       **Option B: Describe Changes Conversationally**

User: Option B
      We need to add rate limiting to the API endpoints

Agent: Got it - adding rate limiting. Let me understand the requirements:

       1. Which endpoints need rate limiting?
          - All endpoints?
          - Just write operations (POST, PUT, DELETE)?
          - Just specific endpoints?

       2. What rate limits are appropriate?
          - Per user?
          - Per IP address?
          - Both?

       3. What rate limit values?
          - Requests per minute?
          - Requests per hour?
          - Different limits for different endpoints?

       4. How should we handle rate limit exceeded?
          - Return 429 status code?
          - Include retry-after header?
          - Any specific error message?

User: All endpoints, per user, 100 req/min, standard 429 response

Agent: Perfect! Here are the proposed changes:

       [Shows before/after for affected sections]

       Does this look correct?

User: Yes

Agent: [Updates and provides summary]
```

## Important Notes

- **Requires $ARGUMENTS**: Must provide Linear Project ID
- **Reads from Linear**: Fetches existing Technical Spec from project description
- **Updates Linear**: Modifies the Technical Spec section in project description
- **Shows Before/After**: Clear comparison of what's changing
- **Tracks Impact**: Identifies affected user stories
- **Validates Uncertainties**: Applies uncertainty markers to new/vague content
- **Preserves Context**: Keeps Product Spec and other sections intact

This conversational approach ensures technical specs stay up-to-date with learnings and decisions, while maintaining clear traceability of what changed and why.
