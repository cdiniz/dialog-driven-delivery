---
name: d3-templates
description: Provides standard templates for Dialog-Driven Delivery (D3) artifacts — specifications, user stories, architectural decision records, and meeting transcripts. Use when creating or refining any D3 artifact. Contains templates for Product Specs, Technical Specs, User Stories, ADRs, and Meeting Transcripts following D3 methodology.
---

# D3 Standard Templates

This skill provides canonical templates for D3 artifact creation. These templates are used by d3:create, d3:refine, d3:decompose, and d3:create-template commands.

## Default Template Lookup

When no custom template path is configured in the artifact's `template` field in `d3.config.yaml`, commands resolve templates by artifact type name:

| Artifact Type | Template File |
|---------------|---------------|
| Product Spec | `references/feature-product-spec.md` |
| Tech Spec | `references/feature-tech-spec.md` |
| User Story | `references/user-story.md` |
| ADR | `references/adr.md` |
| Meeting Transcript | `references/meeting-transcript.md` |

Commands match the artifact type name against this table (case-insensitive). If no match is found, the command asks the user to provide a template path.

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

### 4. Architectural Decision Record (ADR) Template
- **File:** `references/adr.md`
- **Purpose:** Capture architectural decisions as immutable records following [MADR v4](https://adr.github.io/madr/) format
- **Sections:** (MADR v4 standard + D3 extension)
  - Context and Problem Statement (Situation and problem driving the decision)
  - Decision Drivers (Forces, concerns, and constraints)
  - Considered Options (List of options evaluated)
  - Decision Outcome (Chosen option with justification + Consequences + Confirmation)
  - Pros and Cons of the Options (Detailed per-option analysis using "Good/Bad/Neutral, because..." format)
  - More Information (Additional evidence, team agreements, links)
- **Metadata:** Title with ADR number, Date, Status, Decision-makers, Consulted, Informed, Supersedes

### 5. Meeting Transcript Template
- **File:** `references/meeting-transcript.md`
- **Purpose:** Structured capture of meeting transcripts with extracted insights
- **Sections:** 5 main sections
  - Summary (2-3 sentence overview of the meeting)
  - Key Decisions (Numbered decisions with bold titles)
  - Action Items (Numbered items with Owner and Due fields)
  - Open Questions (Numbered questions with context)
  - Raw Transcript (Full unedited transcript)
- **Metadata:** Title, Date, Type (Planning/Technical/Standup/Retro/Other), Participants

## How D3 Commands Use These Templates

### d3:create
1. Reads artifact type from config's `artifacts` section
2. Resolves template: artifact's `template` field or default from this skill's lookup table
3. Uses template structure to ensure all sections present in the generated artifact
4. Fills only what was discussed, marks uncertainties

### d3:refine
1. Detects artifact type from the existing artifact's adapter
2. Resolves template for that type (same lookup as create)
3. Uses template to validate structure is maintained during updates
4. Ensures non-greedy updates — only sections with new information change

### d3:decompose
1. Loads user story template from config or this skill
2. Creates stories following template structure
3. Ensures consistent Given-When-Then acceptance criteria format

### d3:create-template
1. Uses existing templates as starting points for new template creation
2. Ensures Open Questions section is included (required for uncertainty markers)

## Template Loading Pattern

D3 commands follow this loading pattern:

```
1. Read `d3.config.yaml` for artifact configuration
2. Determine artifact type
3. Check artifact's `template` field for a custom path
4. If custom path found → Read that file
5. If no custom path → Look up artifact type in this skill's Default Template Lookup table
6. If no default match → Ask user for template path
```
