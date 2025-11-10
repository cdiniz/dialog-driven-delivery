---
description: Create feature specification from meeting transcript or conversation
---

You are tasked with creating a comprehensive feature specification that will become a Linear Project.

## Conversational Workflow

This command uses an **engaging, conversational approach**:
1. Ask user for input (transcript or description)
2. Analyze input and extract key information
3. Ask clarifying questions
4. Generate feature spec
5. Create Linear Project
6. Provide clear summary

## Steps

### Step 1: Request Input

Start by asking the user how they want to provide information:

"I'll help you create a feature brief and Linear Project. How would you like to provide the feature information?

**Option A: Meeting Transcript** - Paste a transcript from your feature planning meeting
**Option B: Describe Conversationally** - We'll discuss the feature together

Which would you prefer?"

- If Option A: Ask user to paste the transcript
- If Option B: Start with conversational questions

### Step 2: Analyze Input

**If transcript provided:**
- Read and analyze the entire transcript
- Extract key information:
  - Feature name and description
  - Target users/personas
  - Key workflows and user journeys
  - Business value and success criteria
  - Technical constraints mentioned
  - Scope boundaries (in/out of scope)
  - Compliance or security considerations

**If conversational:**
- Ask structured questions to gather the same information

### Step 3: Summarize & Clarify

After analyzing the input, summarize what you found and ask clarifying questions, and extra information if the information is not present in the input:

"I've analyzed your [transcript/description]. Here's what I found:

**Feature:** [Feature name]
**Target Users:** [User personas]
**Key Workflows:**
- [Workflow 1]
- [Workflow 2]
**Business Value:** [Value statement]

Let me ask some clarifying questions to complete the feature brief:

1. What are the specific success criteria for this feature? (measurable outcomes)
2. What are the key functional requirements? (what must it do?)
3. Are there any technical constraints I should know about? (tech stack, performance, etc.)
4. What is explicitly OUT of scope for this feature?
5. Are there any compliance or security considerations? (GDPR, auth, etc.)
6. [Any other questions based on gaps in the input]"

**IMPORTANT - Track Question Responses:**
As you ask clarifying questions, keep track of which ones the user answered and which they skipped or deferred. This tracking is critical for Step 6.5 (Uncertainty Validation).

### Step 6: Generate Feature Specification

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
   - Section 4 (Open Questions & Assumptions) for all uncertainty markers

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

### Step 6.5: Uncertainty Validation (NEW)

**CRITICAL STEP - Do not skip this!**

Before creating the Linear Project, scan the generated specification and validate uncertainty markers:

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
   - Check that all uncertainty markers have corresponding entries in Section 4 (Open Questions & Assumptions)
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

### Step 7: Create Linear Project

Create a project in Linear with the feature spec.

**Note:** Include uncertainty count in project description:
```
[Feature description]

**Spec Status:** [N] open questions, [M] assumptions to validate
```

### Step 8: Save Feature Spec

Save the feature spec to the file system:

**Ask user for location preference:**
"Where would you like to save the feature spec?

**Option A:** `docs/features/[feature_name].md` (recommended)
**Option B:** Custom path

Which would you prefer?"

- Create directory structure if needed
- Save the spec
- Update the "Linear Project" field in the spec with the project URL

### Step 9: Provide Summary

After completing all steps, provide a comprehensive summary:

```markdown
✅ Feature brief created successfully!

**Feature:** [Feature Name]
**Linear Project:** [PROJECT-KEY] - [Project URL]
**Feature Spec:** `[path to feature spec]`

**Summary:**
- [N] user workflows defined
- [N] functional requirements specified
- [N] non-functional requirements documented
- [N] open questions to resolve
- [N] assumptions to validate
- [N] risks identified with mitigations

**Uncertainty Status:**
[If uncertainties exist:]
⚠️ This specification contains [N] uncertainties that should be resolved:
- [X] open questions requiring user decisions (Section 7)
- [Y] clarifications needed for vague requirements (Section 7)
- [Z] assumptions that need validation (Section 10)

[If no uncertainties:]
✅ No unresolved uncertainties - specification is complete and ready for technical design.

**What's in the feature spec:**
- Complete user workflows with actors and steps
- Detailed functional and non-functional requirements
- Clear scope boundaries (in/out of scope)
- Business rules and validation requirements
- Dependencies, constraints, and risks
- Explicit uncertainty markers for incomplete areas

**Next Steps:**
1. [If uncertainties exist:] Review and resolve uncertainties in Section 7 and validate assumptions in Section 10
2. Share with stakeholders for feedback
3. When ready for technical design: `/create-technical-spec [PROJECT-KEY]`
4. After technical spec: `/decompose-feature [PROJECT-KEY]`

**Open Questions to Resolve:**
[List the questions from section 7 that need answers]
```

## Guidelines

### Conversational Best Practices

1. **Be Engaging**: Use natural language, acknowledge input, ask follow-up questions
2. **Show Understanding**: Summarize what you found before asking questions
3. **Be Specific**: Ask concrete questions, not abstract ones
4. **Explain Reasoning**: When you need information, explain why
5. **Confirm Before Creating**: Show what you'll create and ask for confirmation
6. **Provide Context**: Explain what each artifact is for and how it fits in the workflow

### Transcript Analysis Tips

1. **Extract Implicit Info**: People don't always state things explicitly in meetings
2. **Note Disagreements**: If transcript shows debate, capture both perspectives in open questions
3. **Identify Speakers**: If transcript has speaker labels, note who made key decisions
4. **Capture Context**: Note the type of meeting (planning, brainstorm, review)
5. **Find Gaps**: Identify what wasn't discussed but is needed for the spec

### Feature Spec Quality

1. **Be Concrete**: Use specific examples, actual field names, exact error messages
2. **Be Complete**: Cover happy paths, error cases, edge cases, empty states
3. **Be Clear**: Write for both technical and non-technical stakeholders
4. **Define Boundaries**: Be explicit about what's in and out of scope
5. **Track Unknowns**: Capture open questions rather than making assumptions

### Linear Project Creation

1. **Meaningful Names**: Use clear, descriptive project names
2. **Good Descriptions**: Include enough context that someone can understand the project from Linear alone
3. **Link Documentation**: Always reference the feature spec in the project description
4. **Set Appropriate State**: Use "Planned" for new projects unless user specifies otherwise
5. **Choose Right Team**: Confirm team selection with user

## Error Handling

If something goes wrong:

1. **Can't Create Linear Project**: Provide the spec anyway and explain the issue
2. **Ambiguous Input**: Ask specific clarifying questions rather than making assumptions
4. **Incomplete Transcript**: Identify gaps and ask targeted questions to fill them
5. **No Team Access**: List available teams and ask user to select

## Examples

### Example: Transcript Input

```
User: /generate-feature-brief

Agent: I'll help you create a feature brief and Linear Project. How would you
       like to provide the feature information?

       **Option A: Meeting Transcript** - Paste a transcript from your feature
       planning meeting
       **Option B: Describe Conversationally** - We'll discuss the feature together

       Which would you prefer?

User: Option A
      [Pastes transcript: "Meeting notes from 2025-01-15..."]

Agent: I've analyzed your meeting transcript. Here's what I found:

       **Feature:** Advanced Search with Filters
       **Target Users:** Project managers and team leads
       **Key Workflows:**
       - Search tasks with text query
       - Apply filters (status, assignee, date)
       - Save filter presets
       **Business Value:** Reduce time to find tasks by 50%

       Let me ask some clarifying questions:

       1. What are the specific success criteria? I see "reduce time by 50%" -
          are there other metrics?
       2. Should saved filter presets be per-user or shareable across teams?
       3. Your transcript mentions Elasticsearch - is that a confirmed technical
          constraint?
       4. Is real-time search required or is a small delay acceptable?

       [Continues conversation...]
```

### Example: Conversational Input

```
User: /generate-feature-brief

Agent: I'll help you create a feature brief and Linear Project. How would you
       like to provide the feature information?

       **Option A: Meeting Transcript**
       **Option B: Describe Conversationally**

       Which would you prefer?

User: Option B

Agent: Great! Let's define this feature together.

       First, what is the feature you want to build? Give me a brief overview.

User: We want to add the ability to export reports as PDF with custom branding

Agent: Excellent! PDF export with custom branding. Let me understand this better:

       1. Who are the primary users of this feature?
       2. What types of reports need to be exported?
       3. What does "custom branding" include? (logo, colors, header/footer?)
       4. When/where will users trigger the export?
       5. What's the business value - why is this important?

       [Continues conversation...]
```

## Important Notes

- **No $ARGUMENTS**: This command does NOT accept arguments - it always asks for input
- **Transcript is Preferred**: Always offer transcript option first
- **Interactive Throughout**: Multiple interaction points, not just one question
- **Confirmation**: Show what you'll create before creating it
- **Clear Output**: Always provide summary with next steps

This conversational approach makes the process feel collaborative and ensures high-quality feature specs that capture both explicit and implicit requirements.
