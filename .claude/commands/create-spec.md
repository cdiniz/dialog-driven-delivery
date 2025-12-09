---
description: Create comprehensive feature specification from any input context
---

You are tasked with creating a comprehensive feature specification as a markdown file from any input context (product discussion, technical design, or both).

## Philosophy

This command creates a **single markdown file** in `docs/[feature-name]/spec.md` containing BOTH Product and Technical specifications. Fill only what you know from the context - empty sections are better than hallucinated content. The specs will grow progressively as more information becomes available through `/refine-spec`.

## Conversational Workflow

1. Ask user for input context
2. Analyze and extract all available information
3. Propose feature name (will be used for directory name)
4. Create `docs/[feature-name]/spec.md` with both spec sections
5. Fill sections based on what's actually discussed
6. Show clear summary of what was filled vs what remains empty

## Steps

### Step 1: Request Input Context

Start by asking the user for context:

```markdown
I'll help you create a comprehensive feature specification as a markdown file.

How would you like to provide the feature information?

**Option A: Meeting Transcript** - Paste a transcript from any planning or design meeting
**Option B: Document** - Paste an existing document or specification
**Option C: Describe Conversationally** - We'll discuss the feature together

Which would you prefer?
```

### Step 2: Analyze Input

**For any input type:**
- Extract all available information
- Don't force categorization into "product" or "technical"
- Identify what's present vs what's missing
- Note any uncertainties or assumptions

**Information to extract:**
- **Product aspects**: Users, workflows, requirements, business value, success metrics, scope
- **Technical aspects**: Architecture, technologies, APIs, data models, integrations, performance
- **General**: Project goals, constraints, dependencies, risks, timeline
- **Uncertainties**: Questions, pending decisions, assumptions

### Step 3: Propose Feature Name

Based on the analyzed content:

```markdown
Based on your input, I found information about [brief summary of what was discussed].

I propose creating a feature directory named: **[proposed-kebab-case-name]**

This will create:
- docs/[proposed-name]/spec.md - containing both Product and Technical specifications

The spec file will contain sections filled based on what was discussed.

Should I create this feature spec with this name?
```

Wait for confirmation before proceeding.

### Step 4: Generate Combined Specification

Create a specification using the template structure from:
- **Product Spec Template**: @.claude/templates/feature-spec.md
- **Technical Spec Template**: @.claude/templates/technical-spec.md

**Structure:**
```markdown
# Feature: [Feature Name]

## 📋 Product Specification
[Use feature-spec.md template structure - fill only sections with available information]

---

## 🔧 Technical Specification
[Use technical-spec.md template structure - fill only sections with available information]
```

**Filling Guidelines:**
1. **Read both template files** to understand the complete section structure
2. **Map extracted information** to appropriate template sections
3. **Fill only what you know** - don't invent content to fill templates
4. **Use explicit placeholders** for empty sections:
   - `_To be defined - not yet discussed_`
   - `_[Section name] to be determined during [product/technical] design_`
5. **Preserve template section numbering** from the original templates
6. **Include all template sections** but leave empty ones with placeholders

**CRITICAL - Uncertainty Marker Policy:**

Before generating the spec, review the documentation in `.claude/uncertainty-markers.md`.

When generating the specification, you MUST follow these rules:

1. **If user didn't answer a question** → Use uncertainty markers:
   - `[OPEN QUESTION: specific question]` - for user decisions
   - `[CLARIFICATION NEEDED: what needs defining]` - for vague requirements

2. **If you make a reasonable inference** → Mark it explicitly:
   - `[ASSUMPTION: statement of what you're assuming]`

3. **If multiple valid approaches exist** → Mark the choice:
   - `[DECISION PENDING: option A vs option B - see Open Questions QX]`

4. **NEVER make silent assumptions.** If you infer something, mark it with `[ASSUMPTION]`.

5. **Link all markers** → Every inline marker must have corresponding entry in:
   - Section (Open Questions & Assumptions) for all uncertainty markers

**Examples:**

❌ BAD (silent assumption):
```
Users can authenticate via OAuth2 using Google provider
```

✅ GOOD (explicit uncertainty):
```
Users can authenticate via [OPEN QUESTION: OAuth2, password, or social login?]
```

❌ BAD (unmarked inference):
```
API response time should be fast
```

✅ GOOD (explicit clarification needed):
```
API response time should be [CLARIFICATION NEEDED: define threshold - <500ms, <1s, <3s?]
```

Now create a pragmatic, streamlined feature spec using the template from @.claude/templates/feature-spec.md

Fill in all sections of the template with the information gathered, applying the uncertainty marker policy described above.

### Step 5: Uncertainty Validation 

**CRITICAL STEP - Do not skip this!**

Before creating the spec, scan the generated specification and validate uncertainty markers:

1. **Count all uncertainty markers:**
   ```
   Uncertainty Marker Summary:
   - [OPEN QUESTION]: X occurrences
   - [CLARIFICATION NEEDED]: Y occurrences
   - [ASSUMPTION]: Z occurrences
   - [DECISION PENDING]: W occurrences

   Total uncertainties: [X+Y+Z+W]
   ```

2. **Verify each marker is tracked:**
   - Check that all uncertainty markers have corresponding entries in (Open Questions & Assumptions)
   - List any markers that are NOT properly tracked

3. **Present summary to user:**
   ```markdown
   I've generated the feature specification with [N] uncertainty markers:

   **Open Questions:** [X] items requiring user decisions
   **Clarifications Needed:** [Y] items requiring more specific definitions
   **Assumptions:** [Z] items inferred from context that need validation

   [If uncertainties exist:]
   These uncertainties should be resolved before implementation. Would you like to:

   **Option A:** Resolve them now - I'll ask follow-up questions
   **Option B:** Leave them marked for later resolution
   **Option C:** Review the spec first, then resolve

   Which would you prefer?
   ```

4. **If user chooses Option A (Resolve now):**
   - Go through each `[OPEN QUESTION]` and `[CLARIFICATION NEEDED]`
   - Ask the user for answers
   - Update the spec to replace markers with actual values
   - Mark resolved questions as checked in Section 4

5. **If user chooses Option B or C:**
   - Proceed to next step
   - Include uncertainty count in final summary

**Quality Gates:**

⚠️ **Warning if:**
- More than 10 `[OPEN QUESTION]` markers exist (spec may be too incomplete)
- Critical functional requirements have `[OPEN QUESTION]` markers (blocks implementation)

✅ **Acceptable:**
- A few `[ASSUMPTION]` markers (can validate during implementation)
- `[CLARIFICATION NEEDED]` on non-functional requirements (can refine later)

### Step 6: Create Markdown File

Create the markdown file with the complete specification:

**Use Write Tool:** Create the file at `docs/[feature-name]/spec.md`

**File Structure:**
```markdown
# Feature: [Feature Name]

**Status:** Draft
**Created:** [YYYY-MM-DD]
**Last Updated:** [YYYY-MM-DD]

---

## 📋 Product Specification
[Product spec content following feature-spec.md template]

---

## 🔧 Technical Specification
[Technical spec content following technical-spec.md template]
```

**Important Notes:**
- Create the `docs/` directory if it doesn't exist
- Create the `docs/[feature-name]/` subdirectory
- Use clean kebab-case for directory names
- The spec file is named `spec.md`

### Step 7: Provide Comprehensive Summary

After creating the page:

```markdown
✅ Feature specification created successfully!

**Feature:** [Feature Name]
**File:** docs/[feature-name]/spec.md

## What Was Created

**📋 Product Specification:**
- ✅ Overview: [Filled/Partial/Empty]
- ✅ User Journey: [X workflows defined / Empty]
- ✅ Requirements: [Y requirements captured / Empty]
- ⚠️ Open Questions: [Z questions need answers]

**🔧 Technical Specification:**
- ✅ Technical Approach: [Filled/Partial/Empty]
- ✅ Architecture: [X diagrams / Empty]
- ✅ API Contracts: [Y endpoints defined / Empty]
- ✅ Data Models: [Z models defined / Empty]
- ⚠️ Open Questions: [W technical decisions pending]

## Information Coverage

**What we captured from your input:**
[List what was successfully extracted and documented]

**What still needs to be defined:**
[List major gaps that need filling]

**Uncertainties requiring resolution:** [Total count]
- [X] product questions
- [Y] technical questions
- [Z] assumptions to validate

## Next Steps

1. Review the specification: docs/[feature-name]/spec.md
2. [If gaps exist] Schedule sessions to discuss:
   - [Missing product aspects]
   - [Missing technical aspects]
3. Use `/refine-spec [feature-name]` to add information as it becomes available
4. Once specs are complete, use `/create-user-stories-from-spec [feature-name]` to create user stories

The specification will grow progressively as more information becomes available.
```

## Guidelines

### Non-Greedy Filling Principles

1. **Empty is honest**: Better to show "_To be defined_" than make something up
2. **Partial is fine**: Can have complete Product Spec with empty Technical Spec (or vice versa)
3. **Progressive enhancement**: Specs grow over multiple refinement cycles
4. **Explicit gaps**: Make it clear what's missing so team knows what to discuss

### Smart Context Detection

Analyze the input to understand what's available:

**Product-heavy indicators:**
- User stories, personas, journeys
- Business value, ROI, success metrics
- Requirements, features, capabilities
- UI/UX discussions

**Technical-heavy indicators:**
- Architecture, design patterns
- Technology choices, frameworks
- APIs, data models, schemas
- Performance, scalability, security

**Don't force categorization** - just fill what's there!

## Error Handling

1. **Ambiguous feature scope**: Ask clarifying questions about the feature's purpose
2. **No concrete information**: Warn that spec will be mostly empty, confirm creation
3. **Conflicting information**: Create uncertainties and note conflicts in Open Questions
4. **File creation fails**: Provide full specification text for manual creation
5. **Invalid feature name**: Suggest alternative valid kebab-case names

## Examples

### Example 1: Product-Focused Input

```
User: /create-spec

Agent: How would you like to provide the feature information?

User: Option A
      [Pastes product planning meeting transcript]

Agent: Based on your input, I found information about an advanced search feature
       with filters for project managers.

       I propose creating a feature directory named: **advanced-search-with-filters**

       This will create: docs/advanced-search-with-filters/spec.md

       Should I create this feature spec with this name?

User: Yes

Agent: ✅ Feature specification created successfully!

       **Feature:** Advanced Search with Filters
       **File:** docs/advanced-search-with-filters/spec.md

       **📋 Product Specification:**
       - ✅ Overview: Filled (target users, success metrics defined)
       - ✅ User Journey: 3 workflows defined
       - ✅ Requirements: 8 must-haves, 3 out of scope
       - ⚠️ Open Questions: 5 questions need answers

       **🔧 Technical Specification:**
       - ⚪ Technical Approach: Empty - not discussed
       - ⚪ Architecture: Empty - not discussed
       - ⚪ API Contracts: Empty - not discussed
       - ⚠️ Open Questions: 8 technical decisions pending

       The technical aspects can be added later using `/refine-spec advanced-search-with-filters`
```

### Example 2: Technical-Focused Input

```
User: /create-spec

Agent: How would you like to provide the feature information?

User: Option C
      We need to implement Elasticsearch for full-text search with <100ms response

Agent: Based on your input, I found information about implementing full-text
       search using Elasticsearch.

       I propose creating a feature directory named: **full-text-search-implementation**

       This will create: docs/full-text-search-implementation/spec.md

       Should I create this feature spec with this name?

User: Name it "smart-search" instead

Agent: I'll create a feature directory named: **smart-search**

       Should I proceed?

User: Yes

Agent: ✅ Feature specification created successfully!

       **Feature:** Smart Search
       **File:** docs/smart-search/spec.md

       **📋 Product Specification:**
       - ⚠️ Overview: Minimal (inferred purpose only)
       - ⚪ User Journey: Empty - user workflows not discussed
       - ⚪ Requirements: Empty - functional requirements not discussed
       - ⚠️ Open Questions: 7 product questions added

       **🔧 Technical Specification:**
       - ✅ Technical Approach: Filled (Elasticsearch implementation)
       - ✅ Architecture: 1 diagram added
       - ✅ Technical Specifications: Search API defined
       - ✅ Integrations: Elasticsearch details documented

       Product requirements can be added later using `/refine-spec smart-search`
```

### Example 3: Comprehensive Input

```
User: /create-spec
      Option A
      [Pastes transcript covering both product and technical discussions]

Agent: Based on your input, I found comprehensive information about a reporting
       dashboard feature including user needs, workflows, and technical architecture.

       I propose creating a feature directory named: **analytics-reporting-dashboard**

       This will create: docs/analytics-reporting-dashboard/spec.md

       Should I create this feature spec with this name?

User: Yes

Agent: ✅ Feature specification created successfully!

       **Feature:** Analytics Reporting Dashboard
       **File:** docs/analytics-reporting-dashboard/spec.md

       **📋 Product Specification:**
       - ✅ Overview: Filled
       - ✅ User Journey: 2 workflows defined
       - ✅ Requirements: 6 must-haves captured

       **🔧 Technical Specification:**
       - ✅ Technical Approach: Filled
       - ✅ Architecture: 2 diagrams added
       - ✅ API Contracts: 4 endpoints defined
       - ⚠️ Data Models: Partial (mentioned but not detailed)

       Both specifications have good coverage. Missing details can be added
       using `/refine-spec analytics-reporting-dashboard`
```

## Important Notes

- **Always creates both specs**: Every file gets Product AND Technical sections
- **Progressive filling**: Start with what you have, grow over time
- **Honest gaps**: Empty sections clearly marked, not filled with fluff
- **Uncertainty markers**: Prevent hallucination by marking unknowns
- **Single source of truth**: Everything in markdown files under docs/[feature-name]/
- **Natural workflow**: Accepts any type of input without forcing structure
- **Git-tracked**: All specs are version controlled alongside code
- **Portable**: Markdown files work everywhere, no platform lock-in

This unified approach simplifies the workflow while maintaining quality and preventing AI hallucination through explicit gap acknowledgment.
