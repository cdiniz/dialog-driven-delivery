# D3 Plugin - Dialog Driven Delivery

A pragmatic, streamlined methodology for building software products through **conversational, transcript-first** documentation and development.

## What is D3?

D3 (Dialog Driven Delivery) helps teams create feature specifications and user stories through natural conversation, meeting transcripts, and progressive refinement. It prevents AI hallucination through explicit uncertainty markers and works with any specification/work tracking tools through a provider architecture.

## Installation

```bash
# Install the core D3 plugin
claude plugin install d3

# Install the Atlassian provider (if using Confluence + Jira)
claude plugin install d3-atlassian
```

## Quick Start

```bash
# 1. Create a feature specification
/d3:create-spec

# 2. Refine it as you learn more
/d3:refine-spec PAGE-ID

# 3. Decompose into user stories
/d3:decompose PAGE-ID
```

## Commands

### `/d3:create-spec`
Create a comprehensive feature specification from meeting transcripts, documents, or conversational input. Creates both Product and Technical specifications in one unified document.

**Input options:**
- Meeting transcripts (recommended)
- Existing documents
- Conversational description

**Output:**
- Specification with Product & Technical sections
- Fills only what's known (no hallucination)
- Uncertainty markers for unknowns
- Coverage percentage

### `/d3:refine-spec PAGE-ID`
Update existing specifications based on new information. Automatically detects whether changes are product-focused, technical, or both.

**When to use:**
- New information becomes available
- Requirements change or get clarified
- Technical decisions are made
- Open questions get answered

### `/d3:decompose PAGE-ID`
Break features into user stories through conversational planning. Creates Epic and stories with complete acceptance criteria and dependency mapping.

**Output:**
- Epic for the feature
- User stories with Gherkin acceptance criteria
- Dependency links between stories
- Implementation order

## Implementation

**D3 focuses on planning and decomposition.** Implementation is flexible - use whatever development method works best for your team:

- **Your existing workflow** - D3 provides specs and stories, you handle implementation
- **Superpowers skills** (optional) - AI-assisted development with brainstorming, TDD, code review, etc.
- **Mix and match** - Use different approaches for different features

D3 doesn't enforce any particular development methodology.

## Key Features

### Uncertainty Markers
Prevent AI hallucination with explicit uncertainty management:
- `[OPEN QUESTION: ...]` - User decisions needed
- `[ASSUMPTION: ...]` - Inferences that need validation
- `[CLARIFICATION NEEDED: ...]` - Vague requirements
- `[DECISION PENDING: ...]` - Deferred choices

### Conversational & Transcript-First
- Paste meeting transcripts for best results
- Works conversationally without transcripts
- Agent asks clarifying questions
- Proposes options with pros/cons

### Tool-Agnostic Provider Architecture
Works with any specification and work tracking tools:
- **Specifications:** Confluence, Notion, Markdown, etc.
- **Stories:** Jira, Linear, GitHub Issues, etc.

Configure providers in your project's `CLAUDE.md` file

## Prerequisites

### Required
- Claude Code installed
- Git for version control

### Provider-Specific
Install a provider plugin for your tools:
- **Atlassian (Confluence + Jira):** Install `d3-atlassian` plugin
- **Other tools:** Create custom provider (see documentation)

## Configuration

Add this to your project's `CLAUDE.md` file:

```markdown
## D3 Configuration

### Spec Provider
**Skill:** d3-atlassian:atlassian-spec-provider
**Configuration:**
- Cloud ID: your-cloud-id
- Default Location: PROJ
- spaceId: 1234567

### Story Provider
**Skill:** d3-atlassian:atlassian-story-provider
**Configuration:**
- Cloud ID: your-cloud-id
- Default Project: PROJ
```

If configuration is not found, D3 will prompt you with setup instructions and example configuration.

## Typical Workflow

```
Monday: Feature Planning
├─ /d3:create-spec (paste meeting transcript)
└─ Specification created

Tuesday-Wednesday: Refinement
├─ /d3:refine-spec PAGE-ID (add details)
└─ Specifications complete

Thursday: Story Decomposition
├─ /d3:decompose PAGE-ID
└─ User stories created

Next Sprint: Implementation
├─ Use your team's development workflow
├─ OR optionally use superpowers skills for AI assistance
└─ Commit, PR, and merge
```

## Templates

D3 uses streamlined templates (2-3 pages instead of 5-10):

### Product Specification (5 sections)
1. Overview - What, why, who, success metrics
2. User Journey - Primary workflow with edge cases
3. Requirements - Must have, should have, out of scope
4. Open Questions & Assumptions - All uncertainties
5. Risks - High/medium risks with mitigations

### Technical Specification
Adaptive sections based on feature type:
- Technical Approach
- Architecture
- API Contracts
- Data Models
- Integrations
- And more...

## Skills Included

- **create-spec** - Main skill for specification creation
- **refine-spec** - Main skill for specification refinement
- **decompose** - Main skill for story decomposition
- **uncertainty-markers** - Standards for marking unknowns

## Philosophy

1. **Feature-Centric** - Most teams work on features
2. **Conversational** - Commands work like collaboration
3. **Incremental** - Progressive refinement over time
4. **Explicit** - Mark uncertainties, don't assume
5. **Tool-Agnostic** - Works with your existing tools

## Documentation

For complete documentation, examples, and best practices, see the [main README](https://github.com/cdiniz/dialog-driven-delivery/blob/main/README.md).

## Support

- **Issues:** [GitHub Issues](https://github.com/cdiniz/dialog-driven-delivery/issues)
- **Documentation:** See repository README.md
- **Custom Providers:** See provider documentation

## License

MIT
