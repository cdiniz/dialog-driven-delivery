---
description: Refine existing feature specifications based on new information
---

You are tasked with refining an existing feature specification markdown file based on new information, whether product-focused, technical, or both.

## Philosophy

This command updates ANY part of the existing specifications based on new input. It automatically detects which sections need updating - Product, Technical, or both. The key principle: update only what has new information, preserve everything else.

## Conversational Workflow

1. Accept feature name as argument
2. Read and analyze current specification file
3. Request new input (transcript, document, conversation)
4. Analyze what's new vs what exists
5. Show proposed changes (before/after)
6. Apply updates to relevant sections using **bold** for new changes
7. Provide comprehensive summary

## Steps

### Step 1: Get Feature Name from Arguments

The command accepts the feature name as `$ARGUMENTS`:
- Feature directory name (e.g., `advanced-search-with-filters`)
- Will read from `docs/[feature-name]/spec.md`

**Use Read Tool:** Read the file at `docs/$ARGUMENTS/spec.md` to fetch the current specification.

### Step 2: Read and Analyze Current State

Read the markdown file and display the current specification state:

```markdown
I found feature specification: [Feature Name]

**Feature:** [Feature Name]
**File:** docs/[feature-name]/spec.md
**Status:** [Draft/In Progress/Complete]
**Last Updated:** [Date from frontmatter]

## Current Specification Coverage

**📋 Product Specification:**
- Overview: [Complete/Partial/Empty - key points if filled]
- User Journey: [X workflows defined / Empty]
- Requirements: [Y requirements / Empty]
- Open Questions: [Z unresolved questions]

**🔧 Technical Specification:**
- Technical Approach: [Complete/Partial/Empty - key decisions if filled]
- Architecture: [X diagrams / Empty]
- API Contracts: [Y endpoints / Empty]
- Data Models: [Z models / Empty]
- Open Questions: [W unresolved questions]

**Overall Coverage:** [Rough percentage or status for each spec]
```

### Step 3: Request Refinement Input

Ask for new information:

```markdown
How would you like to provide the new information for refinement?

**Option A: Meeting Transcript** - Paste a transcript from a recent discussion
**Option B: Document Update** - Paste updated documentation or decisions
**Option C: Describe Changes** - Tell me what needs to be updated
**Option D: Feedback/Review Notes** - Paste review feedback or comments

Which would you prefer?
```

### Step 4: Analyze New Information

**Smart Detection - Don't force categorization:**

Analyze the input to identify:
1. **What's new** vs what already exists
2. **What's changing** vs what's being added
3. **Which sections** are affected (could be both Product and Technical)

**Product information indicators:**
- User stories, workflows, personas
- Requirements, features, scope
- Success metrics, business value
- UI/UX decisions

**Technical information indicators:**
- Architecture, design patterns
- Technology choices, frameworks
- APIs, data models, integrations
- Performance, security, testing

**Don't assume** - one transcript might update both specs!

### Step 5: Identify Changes

Categorize the changes:

```markdown
I've analyzed your input and found information affecting:

**📋 Product Specification Updates:**
[If any product changes found:]
- **Overview:** [Adding/Updating/No change] - [what specifically]
- **User Journey:** [Adding X workflows/Updating workflow Y/No change]
- **Requirements:** [Adding X requirements/Modifying Y/No change]
- **Open Questions:** [Resolving X questions/Adding Y new questions]

**🔧 Technical Specification Updates:**
[If any technical changes found:]
- **Technical Approach:** [Adding/Updating/No change] - [what specifically]
- **Architecture:** [Adding X diagrams/Updating/No change]
- **API Contracts:** [Adding X endpoints/Modifying Y/No change]
- **Data Models:** [Adding/Updating/No change]
- **Open Questions:** [Resolving X questions/Adding Y new questions]

[If uncertainties about categorization:]
I found information about [topic]. Should this update:
- The Product Specification (user-facing aspects)
- The Technical Specification (implementation details)
- Both specifications
```

### Step 6: Ask Clarifying Questions

Based on the new information, ask targeted questions:

```markdown
Let me clarify a few things about these updates:

[For each major change:]
1. [Specific question about the change]
2. [Question about impact on other sections]
3. [Question about resolving existing uncertainties]

[General questions:]
- Are there any existing open questions that this information resolves?
- Should I remove any sections that are now obsolete?
- Are there new uncertainties or decisions pending?
```

### Step 7: Show Proposed Changes

**CRITICAL - Present clear before/after for each change:**

```markdown
Here are the proposed changes to your specifications:

---

## 📋 Product Specification Changes

### Change 1: [Section Name - e.g., User Journey]

**BEFORE:**
```
[Current content - enough to show context]
```

**AFTER:**
```
[Proposed updated content with changes highlighted]
```

**Rationale:** [Why this change]
**Type:** [Addition/Modification/Clarification/Deletion]

---

### Change 2: [Section Name]
[Continue pattern]

---

## 🔧 Technical Specification Changes

### Change 1: [Section Name - e.g., API Contracts]

**BEFORE:**
```
[Current content]
```

**AFTER:**
```
[Proposed updated content]
```

**Rationale:** [Why this change]
**Type:** [Addition/Modification/Clarification/Deletion]

---

**Summary of All Changes:**
- 📋 Product Spec: [X sections updated, Y questions resolved]
- 🔧 Technical Spec: [X sections updated, Y questions resolved]
- ✅ Resolved Questions: [List any [OPEN QUESTION] markers being resolved]
- ⚠️ New Questions: [List any new uncertainties being added]

Does this look correct? Should I proceed with updating the Confluence page?
```

### Step 8: Apply Updates

Update the markdown file with the refined specifications:

**Use Edit Tool:** Update the file at `docs/[feature-name]/spec.md`

**Update Guidelines:**
- Update the `Last Updated` date in frontmatter to today's date
- Update the `Status` field if appropriate (Draft → In Progress, etc.)
- Apply all approved changes to the specification content
- Preserve all existing content that isn't being updated

```markdown
Updating specification file: docs/[feature-name]/spec.md...

✅ Specification file updated
✅ [X] Product Specification sections modified
✅ [Y] Technical Specification sections modified
✅ [Z] Open questions resolved
✅ [W] New questions/uncertainties added

**File:** docs/[feature-name]/spec.md
```

### Step 9: Provide Comprehensive Summary

```markdown
✅ Specifications refined successfully!

**Feature:** [Feature Name]
**File:** docs/[feature-name]/spec.md

## What Was Updated

**📋 Product Specification:**
[For each section, show status:]
- Overview: [✅ No change / ✏️ Updated / ➕ Filled previously empty]
- User Journey: [✅ No change / ✏️ Updated - added X workflows / ➕ Filled]
- Requirements: [✅ No change / ✏️ Updated - added Y requirements / ➕ Filled]
- Open Questions: [Resolved X, Added Y, Total now: Z]

**🔧 Technical Specification:**
- Technical Approach: [✅ No change / ✏️ Updated / ➕ Filled previously empty]
- Architecture: [✅ No change / ✏️ Added X diagrams / ✏️ Updated]
- API Contracts: [✅ No change / ➕ Added Y endpoints / ✏️ Modified]
- Data Models: [✅ No change / ➕ Added Z models / ✏️ Updated]
- Open Questions: [Resolved X, Added Y, Total now: Z]

## Key Changes Made

[List 3-5 most significant changes with rationale:]
1. **[Change title]**: [What changed and why]
2. **[Change title]**: [What changed and why]

## Coverage Improvement

**Before refinement:**
- Product Spec: ~[X]% complete
- Technical Spec: ~[Y]% complete

**After refinement:**
- Product Spec: ~[X]% complete
- Technical Spec: ~[Y]% complete

## Remaining Gaps

[If sections still empty:]
**Still need to define:**
- [Empty Product sections if any]
- [Empty Technical sections if any]

[If questions remain:]
**Open questions requiring resolution:** [Total count]
- Product questions: [X]
- Technical questions: [Y]

## Impact Assessment

[If applicable:]
**These changes may impact:**
- Jira stories (if created): [List stories that might need review]
- Timeline: [If scope changed significantly]
- Technical complexity: [If architecture changed]

## Next Steps

1. Review the updated specification: docs/[feature-name]/spec.md
2. [If gaps remain] Schedule sessions to discuss:
   - [Remaining product gaps]
   - [Remaining technical gaps]
3. [If ready] Create user stories: `/create-user-stories-from-spec [feature-name]`
4. Continue refinement as needed: `/refine-spec [feature-name]`

The specifications have been successfully updated with the new information.
```

## Guidelines

### Smart Update Detection

1. **Don't force categorization** - Let content determine which spec to update
2. **One input can update both** - Product and technical info often intermixed
3. **Preserve existing content** - Only change what needs changing
4. **Track resolution** - When [OPEN QUESTION] markers get answered, remove them
5. **Add new uncertainties** - New information might raise new questions

### Progressive Refinement Examples

**Refinement 1: Product feedback**
```
Input: "Users want batch operations and keyboard shortcuts"
Updates: Product Spec - Requirements section
Technical Spec: No changes
```

**Refinement 2: Architecture decision**
```
Input: "Switching from REST to GraphQL for better performance"
Updates: Technical Spec - Approach, Architecture, API sections
Product Spec: No changes (user experience unchanged)
```

**Refinement 3: Combined review**
```
Input: Meeting covering UX changes and database optimization
Updates: Product Spec - User Journey section
         Technical Spec - Data Models section
```

### Handling Different Input Types

**Meeting Transcript:**
- Extract all decisions and discussions
- Map to appropriate sections
- Note any disagreements as uncertainties

**Feedback/Review Notes:**
- Identify what's being corrected vs enhanced
- Show clear before/after
- Document rationale for changes

**Direct Updates:**
- User specifies exact changes
- Apply surgical updates
- Preserve everything else

### Change Types

1. **Addition** - New content in previously empty section
2. **Enhancement** - Adding to existing content
3. **Modification** - Changing existing content
4. **Clarification** - Resolving uncertainty markers
5. **Deletion** - Removing obsolete content (rare)

### Quality Checks

Before finalizing updates:
- ✓ All changes have clear rationale
- ✓ Before/after shows enough context
- ✓ Uncertainty markers updated appropriately (follow @.claude/uncertainty-markers.md)
- ✓ No hallucination - only documented changes applied
- ✓ Both specs remain internally consistent

## Error Handling

1. **No changes detected**: Inform user no new information found, ask for clarification
2. **Conflicting with existing**: Show conflict, ask how to resolve
3. **Ambiguous updates**: Ask which section should be updated
4. **Major scope change**: Warn about impact, confirm before proceeding
5. **File update fails**: Provide full updated text for manual update
6. **File not found**: Verify feature name and check if spec file exists at expected path

## Examples

### Example 1: Product Refinement

```
User: /refine-spec advanced-search-with-filters

Agent: I found feature specification: Advanced Search with Filters

       **Current Coverage:**
       📋 Product Spec: ~70% complete (missing success metrics)
       🔧 Technical Spec: ~30% complete (basic approach only)

       How would you like to provide new information?

User: Option A
      [Pastes product review meeting discussing success metrics and new requirements]

Agent: I found information affecting:

       **📋 Product Specification Updates:**
       - Overview: Adding success metrics
       - Requirements: Adding 3 new requirements
       - Open Questions: Resolving 2 questions

       **🔧 Technical Specification Updates:**
       - No changes detected

       [Shows before/after for each change]

       Should I proceed?

User: Yes

Agent: ✅ Specifications refined successfully!

       Product Spec: 70% → 85% complete
       Technical Spec: 30% (unchanged)
```

### Example 2: Technical Refinement

```
User: /refine-spec smart-search

Agent: [Shows current state]

       How would you like to provide new information?

User: Option C
      We decided to use PostgreSQL full-text search instead of Elasticsearch

Agent: I found information affecting:

       **🔧 Technical Specification Updates:**
       - Technical Approach: Updating search implementation
       - Architecture: Updating diagrams
       - Integrations: Removing Elasticsearch, updating PostgreSQL

       [Shows before/after]

User: Yes, update it

Agent: ✅ Technical Spec updated: 30% → 75% complete
```

### Example 3: Combined Refinement

```
User: /refine-spec advanced-search-with-filters

Agent: [Reads spec file]
       [Shows current state]

User: Option A
      [Pastes comprehensive review meeting covering both aspects]

Agent: I found information affecting both specifications:

       **📋 Product Updates:**
       - User Journey: Adding error recovery workflow
       - Requirements: Modifying 2 requirements

       **🔧 Technical Updates:**
       - API Contracts: Adding 3 new endpoints
       - Data Models: Adding audit log model

       [Shows all before/after changes]

User: Perfect, apply all changes

Agent: ✅ Both specifications updated successfully!
       Product: 85% → 92% complete
       Technical: 75% → 88% complete
```

## Important Notes

- **Smart detection**: Automatically determines which spec(s) to update
- **Preserves content**: Only modifies what needs changing
- **Progressive enhancement**: Specs grow with each refinement
- **No forced structure**: Natural information flow
- **Uncertainty tracking**: Resolves old questions, adds new ones
- **Single source of truth**: Everything stays in markdown files under docs/[feature-name]/
- **Version tracking**: Git tracks all changes to spec files with commit history

This unified refinement approach allows natural evolution of specifications without artificial boundaries between product and technical information.
