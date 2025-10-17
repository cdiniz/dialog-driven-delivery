---
description: Generate comprehensive PRD from product description
---

You are tasked with creating a comprehensive Product Requirements Document (PRD) based on the user's product description.

## Instructions

1. **Gather Information**: Ask the user to describe their product idea, including:
   - Product vision and goals
   - Target users and market
   - Core problems being solved
   - Key features they envision
   - Any technical constraints or preferences
   - Compliance or regulatory requirements

2. **Generate PRD**: Create a comprehensive PRD following this exact structure:

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

## 4. Epics & Features

### Epic 1: [Epic Name]

*[Brief epic description focusing on the business value]*

#### Feature 1.1: [Feature Name]

[Feature description and purpose]

**Key Requirements:**

* [Requirement 1]
* [Requirement 2]
* [Nested sub-requirements as needed]
  * [Sub-requirement A]
  * [Sub-requirement B]

[Repeat feature structure for all features in the epic]

[Repeat epic structure for all epics]

---

## 5. Technical Requirements

### 5.1 Performance
* [Performance requirement 1]
* [Performance requirement 2]
* [Performance requirement 3]

### 5.2 Security & Compliance
* [Security requirement 1]
* [Security requirement 2]
* [Compliance requirement 1]
* [Compliance requirement 2]

### 5.3 Reliability
* [Reliability requirement 1]
* [Reliability requirement 2]
* [Backup/recovery requirements]

### 5.4 Usability
* [Accessibility requirement 1]
* [Accessibility requirement 2]
* [User experience requirement]

### 5.5 Platform Support
* [Platform/OS requirements]
* [Browser compatibility]
* [Device support]

---

## 6. Safety Requirements

[If applicable - remove section if not relevant]

### 6.1 [Safety Category]
* [Safety requirement 1]
* [Safety requirement 2]

### 6.2 [Safety Category]
* [Safety requirement 1]
* [Safety requirement 2]

---

## 7. Implementation Priority

### Pre-Launch Setup
* [Setup task 1]
* [Setup task 2]

### Phase 1: [Phase Name]
1. [Feature reference]
2. [Feature reference]
3. [Feature reference]

### Phase 2: [Phase Name]
1. [Feature reference]
2. [Feature reference]
3. [Feature reference]

### Phase 3: [Phase Name]
1. [Feature reference]
2. [Feature reference]
3. [Feature reference]

---

## 8. Success Criteria

### [Success Category 1]
* [Criterion 1]
* [Criterion 2]
* [Criterion 3]

### [Success Category 2]
* [Criterion 1]
* [Criterion 2]
* [Criterion 3]

### [Success Category 3]
* [Criterion 1]
* [Criterion 2]
* [Criterion 3]

---

## 9. Risks & Mitigations

### Risk 1: [Risk Name]
**Mitigation:** [Mitigation strategy]

### Risk 2: [Risk Name]
**Mitigation:** [Mitigation strategy]

### Risk 3: [Risk Name]
**Mitigation:** [Mitigation strategy]

[Continue for all identified risks]
```

## Guidelines for PRD Creation

1. **Be Comprehensive**: Fill in all sections with detailed, specific information
2. **Be Realistic**: Base success metrics and timelines on achievable goals
3. **Be Specific**: Avoid vague requirements; use concrete, measurable criteria
4. **Focus on MVP**: Clearly distinguish between MVP and future features
5. **Consider Compliance**: Include relevant regulatory/legal requirements
6. **Think Safety**: If applicable, address safety and risk management
7. **Prioritize Features**: Group features into logical implementation phases
8. **Define Success**: Create measurable criteria for success
9. **Identify Risks**: Proactively identify and mitigate potential risks
10. **Use Clear Language**: Write for technical and non-technical stakeholders

## Output

After gathering the necessary information, generate the complete PRD and save it to `docs/prd.md` in the project root (or ask where the user wants to save it).
