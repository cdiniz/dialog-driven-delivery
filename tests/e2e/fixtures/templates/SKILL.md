---
name: d3-templates
description: Provides templates for D3 artifacts.
---

# D3 Templates

Templates are in this skill's `references/` directory.

## Default Template Lookup

| Artifact Type | Template File |
|---------------|---------------|
| Product Spec | `references/feature-product-spec.md` |
| Tech Spec | `references/feature-tech-spec.md` |
| User Story | `references/user-story.md` |

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

### d3:create
1. Reads artifact type from config's `### Artifacts` section
2. Resolves template: custom path from `### Templates` or default from this skill's lookup table
3. Uses template structure to ensure all sections present

### d3:refine
1. Detects artifact type from the existing artifact's provider
2. Resolves template for that type
3. Uses template to validate structure

### d3:decompose
1. Loads user story template from config or this skill
2. Creates stories following template structure
