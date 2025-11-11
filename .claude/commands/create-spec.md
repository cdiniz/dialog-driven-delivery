---
description: Create comprehensive project specification from any input context
---

You are tasked with creating a comprehensive project specification in Linear from any input context (product discussion, technical design, or both).

## Philosophy

This command creates a **single Linear project** containing BOTH Product and Technical specifications. Fill only what you know from the context - empty sections are better than hallucinated content. The specs will grow progressively as more information becomes available through `/refine-spec`.

## Conversational Workflow

1. Ask user for input context
2. Analyze and extract all available information
3. Propose project name
4. Create Linear Project with both spec sections
5. Fill sections based on what's actually discussed
6. Show clear summary of what was filled vs what remains empty

## Steps

### Step 1: Request Input Context

Start by asking the user for context:

```markdown
I'll help you create a comprehensive project specification in Linear.

How would you like to provide the project information?

**Option A: Meeting Transcript** - Paste a transcript from any planning or design meeting
**Option B: Document** - Paste an existing document or specification
**Option C: Describe Conversationally** - We'll discuss the project together

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

### Step 3: Propose Project Name

Based on the analyzed content:

```markdown
Based on your input, I found information about [brief summary of what was discussed].

I propose creating a Linear project named: **"[Proposed Name]"**

This project will contain both Product and Technical specifications, with sections filled based on what was discussed.

Should I create this Linear project?
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

### Step 5: Apply Uncertainty Markers

**CRITICAL - Non-Greedy Filling Policy:**

1. **Only fill what was explicitly discussed** - Leave other sections empty with placeholders
2. **Mark all uncertainties** using the standard markers:
   - `[OPEN QUESTION: text]` - User decision needed
   - `[CLARIFICATION NEEDED: aspect]` - Vague requirement
   - `[ASSUMPTION: statement]` - Inference made
   - `[DECISION PENDING: options]` - Choice deferred

3. **Empty sections get explicit placeholders:**
   ```markdown
   ❌ BAD (generic filler):
   "We will use industry best practices for authentication"

   ✅ GOOD (honest empty):
   "_Authentication approach to be determined_"

   ✅ GOOD (partial with uncertainty):
   "Users authenticate via [OPEN QUESTION: SSO, password, or social login?]"
   ```

### Step 6: Create Linear Project

Create the Linear project with the complete specification:

**Project Settings:**
- **Name:** [Confirmed project name]
- **Description:** Full combined specification (both Product and Technical sections)
- **Team:** [Ask user to confirm team]
- **State:** "Planned"
- **Summary:** [Brief 1-2 sentence summary]

### Step 7: Provide Comprehensive Summary

After creating the project:

```markdown
✅ Project specification created successfully!

**Linear Project:** [PROJECT-KEY] - [Project URL]

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

1. Review the specification in Linear: [URL]
2. [If gaps exist] Schedule sessions to discuss:
   - [Missing product aspects]
   - [Missing technical aspects]
3. Use `/refine-spec [PROJECT-KEY]` to add information as it becomes available
4. Once specs are complete, use `/decompose-feature [PROJECT-KEY]` to create user stories

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

1. **Ambiguous project scope**: Ask clarifying questions about the project's purpose
2. **No concrete information**: Warn that spec will be mostly empty, confirm creation
3. **Conflicting information**: Create uncertainties and note conflicts in Open Questions
4. **Linear creation fails**: Provide full specification text for manual creation

## Examples

### Example 1: Product-Focused Input

```
User: /create-spec

Agent: How would you like to provide the project information?

User: Option A
      [Pastes product planning meeting transcript]

Agent: Based on your input, I found information about an advanced search feature
       with filters for project managers.

       I propose creating a Linear project named: "Advanced Search with Filters"

       Should I create this Linear project?

User: Yes

Agent: ✅ Project specification created successfully!

       **Linear Project:** PROJ-42

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

       The technical aspects can be added later using `/refine-spec PROJ-42`
```

### Example 2: Technical-Focused Input

```
User: /create-spec

Agent: How would you like to provide the project information?

User: Option C
      We need to implement Elasticsearch for full-text search with <100ms response

Agent: Based on your input, I found information about implementing full-text
       search using Elasticsearch.

       I propose creating a Linear project named: "Full-Text Search Implementation"

       Should I create this Linear project?

User: Name it "Smart Search" instead

Agent: I'll create a Linear project named: "Smart Search"

       Should I proceed?

User: Yes

Agent: ✅ Project specification created successfully!

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

       Product requirements can be added later using `/refine-spec PROJ-XX`
```

### Example 3: Comprehensive Input

```
User: /create-spec
      Option A
      [Pastes transcript covering both product and technical discussions]

Agent: Based on your input, I found comprehensive information about a reporting
       dashboard feature including user needs, workflows, and technical architecture.

       I propose creating a Linear project named: "Analytics Reporting Dashboard"

       Should I create this Linear project?

User: Yes

Agent: ✅ Project specification created successfully!

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
       using `/refine-spec PROJ-XX`
```

## Important Notes

- **Always creates both specs**: Every project gets Product AND Technical sections
- **Progressive filling**: Start with what you have, grow over time
- **Honest gaps**: Empty sections clearly marked, not filled with fluff
- **Uncertainty markers**: Prevent hallucination by marking unknowns
- **Single source of truth**: Everything in Linear project description
- **Natural workflow**: Accepts any type of input without forcing structure

This unified approach simplifies the workflow while maintaining quality and preventing AI hallucination through explicit gap acknowledgment.