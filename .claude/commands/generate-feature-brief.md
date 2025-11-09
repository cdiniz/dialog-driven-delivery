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

Before generating the spec, review the documentation in `docs/uncertainty-markers.md`.

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
   - Section 7 (Open Questions) for `[OPEN QUESTION]` and `[CLARIFICATION NEEDED]`
   - Section 10 (Appendix > Assumptions) for `[ASSUMPTION]`

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

Now create a comprehensive feature spec using this template:

<feature_template>
```markdown
# Feature: [Feature Name]

**Date:** [Current Date]
**Status:** Planning
**Linear Project:** [Will be filled after creation]

---

## 1. Feature Overview

### 1.1 Description
[Detailed description of what this feature does and why it's important. Include context from PRD if available.]

### 1.2 Business Value
[Clear explanation of the business value and strategic importance. Why are we building this?]

### 1.3 Target Users
[Which user personas will use this feature. Reference PRD personas if available, or define new ones.]

### 1.4 Success Criteria
* [Measurable criterion 1 - specific metric]
* [Measurable criterion 2 - specific metric]
* [Measurable criterion 3 - specific metric]
* [Continue as needed]

---

## 2. User Workflows

### Workflow 1: [Primary Workflow Name]
**Actors:** [User persona]
**Trigger:** [What initiates this workflow]

**Steps:**
1. User [action with specific details]
2. System [response with specific behavior]
3. User [action with specific details]
4. System [response with specific behavior]
5. [Continue with complete workflow]

**Success Outcome:** [What success looks like]
**Error Scenarios:** [What can go wrong]

### Workflow 2: [Secondary Workflow Name]
**Actors:** [User persona]
**Trigger:** [What initiates this workflow]

**Steps:**
1. User [action]
2. System [response]
3. [Continue with complete workflow]

**Success Outcome:** [What success looks like]
**Error Scenarios:** [What can go wrong]

[Add more workflows as needed - cover all major user journeys]

---

## 3. Functional Requirements

### 3.1 Core Functionality
* **FR1:** [Specific requirement with acceptance criteria]
* **FR2:** [Specific requirement with acceptance criteria]
* **FR3:** [Specific requirement with acceptance criteria]
* [Continue with all core requirements]

### 3.2 Input Requirements
* **Input 1:** [Name] - [Format, validation rules, constraints]
* **Input 2:** [Name] - [Format, validation rules, constraints]
* [All inputs users can provide]

### 3.3 Output Requirements
* **Output 1:** [Name] - [Format, content, when shown]
* **Output 2:** [Name] - [Format, content, when shown]
* [All outputs users will see]

### 3.4 Business Rules
* **BR1:** [Specific business rule with conditions and outcomes]
* **BR2:** [Specific business rule with conditions and outcomes]
* [All business logic and rules]

### 3.5 Validation Rules
* **VR1:** [Field/input] - [Validation rule and error message]
* **VR2:** [Field/input] - [Validation rule and error message]
* [All validation rules with exact error messages]

### 3.6 Data Requirements
* **DR1:** [What data is needed, where it comes from]
* **DR2:** [What data is needed, where it comes from]
* [All data requirements]

---

## 4. Non-Functional Requirements

### 4.1 Performance
* [Specific performance requirement with measurable criteria]
* [Example: Page load time < 2 seconds]
* [Example: API response time < 500ms]

### 4.2 Security
* [Specific security requirement]
* [Authentication/authorization requirements]
* [Data protection requirements]

### 4.3 Accessibility
* [WCAG compliance level]
* [Keyboard navigation requirements]
* [Screen reader requirements]

### 4.4 Usability
* [User experience requirements]
* [Error handling and feedback]
* [Loading states and progress indicators]

### 4.5 Scalability
* [Expected load/volume]
* [Scaling requirements]

### 4.6 Internationalization (if applicable)
* [Languages to support]
* [Localization requirements]
* [Date/time/currency formats]

---

## 5. Dependencies & Constraints

### 5.1 Technical Dependencies
* [Dependency 1: what depends on what]
* [Dependency 2: what depends on what]
* [Example: Requires user authentication system to be implemented first]

### 5.2 External Dependencies
* [Third-party services or APIs]
* [External data sources]

### 5.3 Technical Constraints
* [Constraint 1: limitation and impact]
* [Constraint 2: limitation and impact]
* [Example: Must work with existing PostgreSQL database]

### 5.4 Business Constraints
* [Timeline constraints]
* [Budget constraints]
* [Resource constraints]

### 5.5 Compliance Requirements
* [GDPR, HIPAA, SOC2, etc.]
* [Data retention policies]
* [Audit requirements]

---

## 6. Scope Boundaries

### 6.1 In Scope
* [Capability 1 - explicitly included]
* [Capability 2 - explicitly included]
* [Capability 3 - explicitly included]
* [Be specific about what IS included]

### 6.2 Out of Scope
* [Capability 1 - explicitly NOT included]
* [Capability 2 - explicitly NOT included]
* [Capability 3 - explicitly NOT included]
* [Be clear about what is deferred or excluded]

### 6.3 Future Considerations
* [Enhancement 1 - possible future work]
* [Enhancement 2 - possible future work]
* [Ideas mentioned but not in current scope]

---

## 7. Open Questions

Track unresolved questions that need answers before or during implementation.

**NOTE:** Every `[OPEN QUESTION]` and `[CLARIFICATION NEEDED]` marker in the spec body must have a corresponding entry here with:
- Clear question statement
- Owner (who will resolve it)
- Deadline (when it's needed)
- Context (where in the spec it's referenced)

Example format:

- [ ] **Q1:** [Question that needs resolution]
  - **Owner:** [Who will resolve - Product/Engineering/Design/etc.]
  - **Deadline:** [When needed - Before technical design/Before implementation/etc.]
  - **Context:** [Where this appears - Referenced in FR3, Section 2.1, etc.]
  - **Options:** [If applicable - list the choices being considered]

- [ ] **Q2:** [Question that needs resolution]
  - **Owner:** [Who will resolve]
  - **Deadline:** [When needed]
  - **Context:** [Where referenced]

[Continue with all open questions - ensure each inline marker has an entry here]

---

## 8. Risks & Mitigations

### Risk 1: [Risk Name]
**Probability:** [High/Medium/Low]
**Impact:** [High/Medium/Low]
**Mitigation Strategy:** [How to address this risk]

### Risk 2: [Risk Name]
**Probability:** [High/Medium/Low]
**Impact:** [High/Medium/Low]
**Mitigation Strategy:** [How to address this risk]

[Continue with all identified risks]

---

## 9. References

- **Meeting Transcript:** [Date and participants if from meeting]
- **Related Documentation:** [Links to any related docs]
- **Design Mockups:** [If available]

---

## 10. Appendix

### Meeting Notes
[If transcript was provided, summarize key discussion points]

### Assumptions

**NOTE:** Every `[ASSUMPTION]` marker in the spec body must have a corresponding entry here.

List all assumptions made during feature definition with full context:

Example format:

1. **[Assumption Name]:** [Full statement of the assumption]. [Why this assumption was made]. [Impact if assumption is wrong]. [How to validate].

Example:
1. **Browser Support:** We assume modern browsers (Chrome 90+, Firefox 88+, Safari 14+) based on typical SaaS user base. This affects which web APIs we can use. Needs validation with actual user analytics before implementation.

2. **Authentication Method:** We assume [ASSUMPTION content from spec]. [Continue with context and validation approach].

[List all assumptions - ensure each inline `[ASSUMPTION]` marker has an entry here]

### Glossary
[Define any domain-specific terms used in this document]
```
</feature_template>

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
   - Check that each `[OPEN QUESTION]` and `[CLARIFICATION NEEDED]` has a corresponding entry in Section 7 (Open Questions)
   - Check that each `[ASSUMPTION]` has a corresponding entry in Section 10 (Appendix > Assumptions)
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
   - Move resolved questions to a "Resolved Questions" subsection in Section 7

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
4. **Reference PRD**: When available, connect feature to product vision and personas
5. **Define Boundaries**: Be explicit about what's in and out of scope
6. **Track Unknowns**: Capture open questions rather than making assumptions

### Linear Project Creation

1. **Meaningful Names**: Use clear, descriptive project names
2. **Good Descriptions**: Include enough context that someone can understand the project from Linear alone
3. **Link Documentation**: Always reference the feature spec in the project description
4. **Set Appropriate State**: Use "Planned" for new projects unless user specifies otherwise
5. **Choose Right Team**: Confirm team selection with user

## Error Handling

If something goes wrong:

1. **Missing PRD**: It's optional - continue without it
2. **Can't Create Linear Project**: Provide the spec anyway and explain the issue
3. **Ambiguous Input**: Ask specific clarifying questions rather than making assumptions
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
