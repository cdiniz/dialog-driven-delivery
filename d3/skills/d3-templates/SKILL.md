---
name: d3-templates
description: Provides standard templates for Dialog-Driven Delivery (D3) specifications and user stories. Use when creating or refining feature specifications (product or technical) or decomposing features into user stories. Contains templates for Product Specs, Technical Specs, and User Stories following D3 methodology.
---

# D3 Standard Templates

This skill provides canonical templates for D3 specification and story creation. These templates are used by d3:create-spec, d3:refine-spec, and d3:decompose commands.

## Available Templates

Templates are located in this skill's `references/` directory:

### 1. Feature Product Specification Template
- **File:** `references/feature-product-spec.md`
- **Purpose:** Product requirements and business context
- **Sections:** 5 main sections
  - Overview (What, Why, Target Users, Success Metrics)
  - User Journey (Primary workflow with steps, success criteria, edge cases)
  - Requirements (Must Have, Out of Scope, Constraints & Dependencies)
  - Open Questions (Questions needing answers, assumptions made)
  - References (Related docs, design links)

### 2. Feature Technical Specification Template
- **File:** `references/feature-tech-spec.md`
- **Purpose:** Implementation details and technical decisions
- **Sections:** 8 adaptive sections
  - Technical Approach (1 paragraph on solution approach)
  - System Changes (New components, modifications to existing)
  - Architecture (Optional mermaid diagrams)
  - Architectural Context (Patterns, ADRs, guidelines)
  - Technical Specifications (API Contracts, Data Models, Event Models - all optional)
  - Integrations (Internal/External systems, new dependencies)
  - Testing Requirements (Test coverage, test scenarios, test data)
  - Open Questions (Questions, assumptions)

### 3. User Story Template
- **File:** `references/user-story.md`
- **Purpose:** Individual implementable user stories
- **Structure:**
  - Story Name (title)
  - Description (1-2 sentences)
  - Acceptance Criteria (Given-When-Then format with 2+ scenarios)
  - Relevant docs (Feature spec link, other references)

## How D3 Commands Use These Templates

### d3:create-spec
1. Loads user spec templates feature-product-spec and feature-tech-spec from CLAUDE.md config or this skill
2. Creates unified spec with both Product and Technical sections
3. Uses template structure to ensure all sections present

### d3:refine-spec
1. Loads user spec templates feature-product-spec and feature-tech-spec from CLAUDE.md config or this skill
2. Loads existing spec
3. Uses templates to validate structure
4. Ensures all required sections present when updating

### d3:decompose
1. Loads user story template from CLAUDE.md config or this skill
2. Creates stories following template structure
3. Ensures consistent Given-When-Then acceptance criteria format

## Template Loading Pattern

D3 commands follow this loading pattern:

```
1. Read CLAUDE.md for D3 Configuration section
2. Extract template paths:
   - feature_spec_template
   - technical_spec_template
   - user_story_template
3. For each template:
   - If custom path specified → Read that file
   - If no custom path → Read from this skill's references/
```