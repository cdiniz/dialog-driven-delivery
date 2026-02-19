---
name: d3-templates
description: Provides standard templates for Dialog-Driven Delivery (D3) specifications, user stories, architectural decision records, and meeting transcripts. Use when creating or refining feature specifications (product or technical), decomposing features into user stories, recording architectural decisions, or capturing meeting transcripts. Contains templates for Product Specs, Technical Specs, User Stories, ADRs, and Meeting Transcripts following D3 methodology.
---
<!-- DO NOT EDIT - Generated from canonical/ by generate.py -->

# D3 Standard Templates

This skill provides canonical templates for D3 specification, story, ADR, and transcript creation. These templates are used by d3:create-spec, d3:refine-spec, d3:decompose, d3:create-adr, and d3:capture-transcript commands.

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

### d3:create-spec
1. Loads user spec templates feature-product-spec and feature-tech-spec from AGENTS.md config or this skill
2. Creates unified spec with both Product and Technical sections
3. Uses template structure to ensure all sections present

### d3:refine-spec
1. Loads user spec templates feature-product-spec and feature-tech-spec from AGENTS.md config or this skill
2. Loads existing spec
3. Uses templates to validate structure
4. Ensures all required sections present when updating

### d3:decompose
1. Loads user story template from AGENTS.md config or this skill
2. Creates stories following template structure
3. Ensures consistent Given-When-Then acceptance criteria format

### d3:create-adr
1. Loads ADR template from AGENTS.md config or this skill
2. Extracts decision context, alternatives, rationale, and consequences from input
3. Auto-numbers by searching existing ADRs
4. Creates ADR using template structure
5. Handles superseding (cross-references old and new ADRs)

### d3:capture-transcript
1. Loads meeting transcript template from AGENTS.md config or this skill
2. Asks user to paste raw transcript
3. Extracts decisions, action items, and open questions
4. Generates structured summary using template
5. Stores via transcript provider

## Template Loading Pattern

D3 commands follow this loading pattern:

```
1. Read AGENTS.md for D3 Configuration section
2. Extract template paths:
   - feature_spec_template
   - technical_spec_template
   - user_story_template
   - adr_template
   - meeting_transcript_template
3. For each template:
   - If custom path specified → Read that file
   - If no custom path → Read from this skill's references/
```