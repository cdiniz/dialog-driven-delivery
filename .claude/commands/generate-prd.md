---
description: Generate comprehensive PRD from description, transcript, or interactive discussion
---

You are tasked with creating a comprehensive Product Requirements Document (PRD) based on the user's input.

## Instructions

1. **Analyze Input**:
   - If $ARGUMENTS provided: This could be a product description, meeting transcript, or planning discussion notes
   - If no $ARGUMENTS: Proceed with interactive questions

2. **Extract Information**:
   - If transcript/description provided: Extract as much as possible from the input
   - Only ask clarifying questions for critical missing information:
     - Product vision and goals
     - Target users and market
     - Core problems being solved
     - MVP scope (key capabilities)
     - Out of scope items
     - Strategic risks and concerns

3. **Generate PRD**: Create a comprehensive PRD following this exact structure:

```markdown
# Product Requirements Document (PRD)

## [Product Name] - [Brief Tagline]

### "[Memorable Slogan/Mission Statement]"

**Version:** 1.0
**Date:** [Current Date]
**Market:** [Target Market/Region]

---

## 1. Executive Summary

### 1.1 Product Vision
[Clear, compelling vision statement describing what the product aims to achieve]

### 1.2 Problem Statement
[Detailed description of the problem, including data/statistics if available]

### 1.3 Solution
[How the product solves the problem, key differentiators, core value proposition]

### 1.4 Success Metrics
* [Metric 1]
* [Metric 2]
* [Metric 3]
* [Metric 4]
* [Metric 5]

---

## 2. Scope

### 2.1 MVP Scope
* [Feature/capability 1]
* [Feature/capability 2]
* [Feature/capability 3]
* [Continue listing all MVP features]

### 2.2 Out of Scope
* [Feature/capability deferred to future releases]
* [Feature/capability explicitly excluded]
* [Continue listing out-of-scope items]

---

## 3. User Personas

### Primary Users

1. **[Persona Name]** - [Brief role description]
   * [Key characteristic or need]
   * [Key characteristic or need]

2. **[Persona Name]** - [Brief role description]
   * [Key characteristic or need]
   * [Key characteristic or need]

[Add more personas as needed]

---

## 4. Risks & Mitigations

### Risk 1: [Risk Name]
**Mitigation:** [Mitigation strategy]

### Risk 2: [Risk Name]
**Mitigation:** [Mitigation strategy]

### Risk 3: [Risk Name]
**Mitigation:** [Mitigation strategy]

[Continue for all identified risks]
```

## Guidelines for PRD Creation

1. **Extract from Input**: If a transcript or description is provided, extract all relevant information before asking questions
2. **Be Comprehensive**: Fill in all sections with detailed, specific information
3. **Be Strategic**: Focus on high-level vision, problems, and scope - leave detailed feature specifications for `/create-feature-and-stories`
4. **Clear Scope**: Define MVP scope with key capabilities, not detailed features
5. **Define Clear Personas**: Create detailed user personas that will inform feature development
6. **Identify Risks Early**: Proactively identify strategic and business risks with mitigations
7. **Use Clear Language**: Write for both technical and non-technical stakeholders
8. **Infer When Reasonable**: For transcripts, make reasonable inferences about context and fill in details logically

**Note:** The PRD establishes strategic direction. Features will be created separately using `/create-feature-and-stories` with descriptions or meeting transcripts.

## Output

After gathering the necessary information, generate the complete PRD and save it to `docs/prd.md` in the project root (or ask where the user wants to save it).
