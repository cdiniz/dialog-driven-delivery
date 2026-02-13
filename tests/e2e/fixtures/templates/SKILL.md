---
name: d3-templates
description: Provides templates for D3 specifications and user stories.
---

# D3 Templates

Templates are in this skill's `references/` directory.

## Available Templates

### 1. Feature Product Specification Template
- **File:** `references/feature-product-spec.md`
- **Sections:** 3 sections
  - Overview
  - Requirements
  - Open Questions

### 2. Feature Technical Specification Template
- **File:** `references/feature-tech-spec.md`
- **Sections:** 2 sections
  - Technical Approach
  - Testing Requirements

### 3. User Story Template
- **File:** `references/user-story.md`
- **Structure:**
  - YAML frontmatter (type, id, spec, title, status)
  - Description
  - Acceptance Criteria (Given-When-Then)

## How D3 Commands Use These Templates

### d3:create-spec
1. Loads templates from CLAUDE.md config or this skill
2. Creates unified spec with both Product and Technical sections
3. Uses template structure to ensure all sections present

### d3:refine-spec
1. Loads templates from CLAUDE.md config or this skill
2. Uses templates to validate structure

### d3:decompose
1. Loads user story template from CLAUDE.md config or this skill
2. Creates stories following template structure
