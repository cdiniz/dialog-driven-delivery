# Dialog Driven Delivery (D3) — Tooling

[D3](https://dialogdrivendelivery.com/) is a methodology for AI-enabled software delivery, built from real engagements by practitioners at Equal Experts. It helps teams—not just individuals—work effectively with AI by focusing on collaboration and context, not tooling.

**This repository provides the tooling that implements D3's workflow as Claude Code plugins.** It turns the methodology's principles into a concrete, repeatable process: capture conversations, create structured specifications, and decompose features into implementable stories.

Works with your existing tools. Built-in providers for Atlassian (Confluence + Jira) and Markdown (local files + git). Expandable to any specification storage or work tracking system through pluggable provider skills.

---

## Quick Start

### Initial Setup (One-Time)

```bash
# 1. Install D3 (see Installation section)
claude plugin install d3@d3-marketplace
claude plugin install d3-atlassian@d3-marketplace  # or d3-markdown

# 2. Configure provider in CLAUDE.md (see Configuration section)
# Add provider config to CLAUDE.md

# 3. (Optional) Customize templates for your team
# Copy default templates to your repo and configure custom paths
# See Template Customization section below
```

### Complete Feature Development Flow

```bash
# 0. Capture Phase (optional)
/d3:capture-transcript                 # Capture and structure a meeting transcript

# 1. Planning Phase
/d3:create-spec                        # Create feature spec (can reference transcripts)
/d3:create-adr                         # Record architectural decisions
/d3:refine-spec PAGE-ID                # Refine based on discussions + ADRs

# 2. Decomposition Phase
/d3:decompose PAGE-ID                  # Break into user stories

# 3. Implementation Phase
# Use your team's existing development workflow

# 4. Merge and repeat for next story
```

---

## Methodology

D3 is grounded in [three principles](https://dialogdrivendelivery.com/) observed across real engagements:

1. **Cross-functional dialogue is the source** — Product, engineering, and design conversations create context that documentation alone cannot. Capture the dialogue, not just the outcome.
2. **Context engineering is the core skill** — AI follows context. The richer and more structured that context, the better the output. Structuring specifications and curating decisions determines AI effectiveness.
3. **Human accountability is non-negotiable** — AI drafts. Humans review. Every specification, every story, every decision passes through human judgment.

This tooling applies those principles through a concrete workflow:

- **Feature-centric**: Specifications at feature level, not task level
- **Transcript-first**: Commands accept meeting transcripts as primary input
- **Incremental delivery**: Features decompose into independently deliverable stories
- **Explicit over implicit**: Uncertainties are marked, not assumed — prevents AI hallucination
- **Tool-agnostic**: Provider architecture works with whatever tools your team already uses

---

## Prerequisites

### Required
- **Claude Code or Claude Cowork** installed and configured
- **Git** for version control

### Provider-Specific (choose one or more)

**Built-in Providers:**

**Option 1: Atlassian (Enterprise-Ready)**
- **Confluence** for feature specifications
- **Jira** for user stories and tracking
- **Atlassian MCP Server** configured for Claude Code

**Option 2: Markdown (Lightweight, Git-Native)**
- **Local markdown files** for feature specifications (`./specs/`)
- **Local markdown files** for user stories (organized by feature)
- **Git** for version control
- No external services required

**Expandable to Other Tools:**
- **Notion + Linear:** Create custom provider plugins
- **GitHub Issues:** Create custom provider plugin
- **Mix & Match:** Use different tools for specs and stories

**Next Step:** After installation, configure your chosen provider(s) - see the **Configuration** section below for detailed setup instructions.

---

## Installation

### From Marketplace (Recommended)

```bash
# Add the D3 marketplace
claude plugin marketplace add cdiniz/dialog-driven-delivery

# Install the core D3 plugin
claude plugin install d3@d3-marketplace

# Install provider plugins (choose one or both):
# - Atlassian provider (Confluence + Jira)
claude plugin install d3-atlassian@d3-marketplace
# - Markdown provider (local files + git)
claude plugin install d3-markdown@d3-marketplace
```

### Post-Installation Setup

After installing D3, configure your project:

**1. Configure your provider:**
See the **Configuration** section below for detailed provider setup (Atlassian or Markdown).

**2. (Optional) Customize templates for your team:**

D3 includes default templates via the `d3-templates` skill. Teams can optionally customize templates for their specific needs.

```bash
# Create templates directory
mkdir -p .d3/templates

# Copy default templates from the d3-templates skill
cp -r ~/.claude/plugins/d3/skills/d3-templates/references/* .d3/templates/

# Templates copied (5 total):
# - feature-product-spec.md
# - feature-tech-spec.md
# - user-story.md
# - meeting-transcript.md
# - adr.md

# Configure custom paths in CLAUDE.md (see Template Customization section)

# Commit to your repo
git add .d3/
git commit -m "Add customized D3 templates"
```

**When to customize templates:**
- **Domain-specific sections**: Add sections specific to your industry (healthcare, finance, etc.)
- **Compliance requirements**: Add required sections for SOC2, HIPAA, GDPR, etc.
- **Team conventions**: Reflect your team's established patterns and practices
- **Tech stack specifics**: Add framework-specific sections (React patterns, API versioning, etc.)
- **Meeting transcript sections**: Add Risks, Parking Lot, Next Meeting Agenda, etc.
- **ADR customization**: Add custom metadata fields, alternative formats, team-specific decision criteria

**Default behavior (no customization needed):**
- D3 loads templates automatically from the `d3-templates` skill
- Works out of the box without any template configuration
- Templates are standard, pragmatic, and suitable for most teams

---

### Local Development

For development or testing the plugins locally:

```bash
# Test both plugins together
claude --plugin-dir ./d3 --plugin-dir ./d3-atlassian

# Or use local marketplace
claude plugin marketplace add ./path/to/dialog-driven-delivery
claude plugin install d3@d3-marketplace
```

---

## Configuration

D3 configuration lives in your project's `CLAUDE.md` file. This tells D3 which providers to use and how to connect to your tools.

### Quick Setup

**If configuration is not found:** D3 commands will automatically prompt you with setup instructions on first use.

**To configure manually:** Add a `## D3 Configuration` section to your `CLAUDE.md` as shown below.

---

### Atlassian Provider Configuration

For teams using Confluence (specs) and Jira (stories):

```markdown
## D3 Configuration

### Spec Provider
**Skill:** d3-atlassian:atlassian-spec-provider
**Configuration:**
- Cloud ID: your-cloud-id
- Default Location: PROJ
- spaceId: 1234567
- Default parent page: https://yoursite.atlassian.net/wiki/spaces/PROJ/pages/123456

### Story Provider
**Skill:** d3-atlassian:atlassian-story-provider
**Configuration:**
- Cloud ID: your-cloud-id
- Default Project: PROJ

### Transcript Provider
**Skill:** d3-atlassian:atlassian-transcript-provider
**Configuration:**
- Cloud ID: your-cloud-id
- Default Location: PROJ
- spaceId: 1234567
- Default parent page: https://yoursite.atlassian.net/wiki/spaces/PROJ/pages/123456/Transcripts
```

**Finding your values:**
- **Cloud ID**: Visit your Atlassian site URL - visible in URL or retrieve using Atlassian MCP tools
- **Space ID**: Found in Confluence space settings or URL
- **Default parent page**: URL of the Confluence page where specs should be created
- **Default Project**: Your Jira project key (e.g., "PROJ", "ENG", "PRODUCT")

**Prerequisites:**
- Atlassian MCP Server installed and configured for Claude Code
- Access to your Confluence space and Jira project

---

### Markdown Provider Configuration

For teams using local markdown files with git:

```markdown
## D3 Configuration

### Spec Provider
**Skill:** d3-markdown:markdown-spec-provider
**Configuration:**
- Specs Directory: ./specs

### Story Provider
**Skill:** d3-markdown:markdown-story-provider
**Configuration:**
- Stories Directory: ./stories

### Transcript Provider
**Skill:** d3-markdown:markdown-transcript-provider
**Configuration:**
- Transcripts Directory: ./transcripts
```

---

### ADR Provider Configuration (Optional)

By default, ADRs are stored using the same Spec Provider. To store ADRs in a separate location, add an `### ADR Provider` section to your D3 configuration.

**Atlassian (separate Confluence space for ADRs):**

```markdown
## D3 Configuration

### ADR Provider
**Skill:** d3-atlassian:atlassian-spec-provider
**Configuration:**
- Cloud ID: your-cloud-id
- Default Location: ADR
- spaceId: 9876543
- Default parent page: https://yoursite.atlassian.net/wiki/spaces/ADR/pages/123456
```

**Markdown (separate directory for ADRs):**

```markdown
## D3 Configuration

### ADR Provider
**Skill:** d3-markdown:markdown-spec-provider
**Configuration:**
- Specs Directory: ./docs/adrs
```

**No ADR Provider configured?** The `create-adr` command falls back to the Spec Provider automatically. ADRs are just documents — the same provider interface works for both.

---

### Template Customization (Optional)

D3 provides **default templates via the d3-templates skill** that work out of the box. Teams can optionally customize templates for their specific needs.

**Default Templates Included:**

**Feature Specification Template** (5 sections):
1. **Overview** - What, why, who, and success metrics
2. **User Journey** - Primary workflow with edge cases
3. **Requirements** - Must have, should have, out of scope, constraints
4. **Open Questions & Assumptions** - All uncertainties in one place
5. **References** - Related docs, design links

**Technical Specification Template** (8 sections):
1. **Technical Approach** - Solution approach overview
2. **System Changes** - New components, modifications to existing
3. **Architecture** - Optional mermaid diagrams
4. **Architectural Context** - Patterns, ADRs, guidelines
5. **Technical Specifications** - API Contracts, Data Models, Event Models (all optional)
6. **Integrations** - Internal/External systems, new dependencies
7. **Testing Requirements** - Test coverage, test scenarios, test data
8. **Open Questions** - Questions, assumptions

**User Story Template:**
- Story name and description
- Acceptance criteria (Given-When-Then format)
- Relevant documentation links

**Meeting Transcript Template** (5 sections):
1. **Summary** - 2-3 sentence overview of the meeting
2. **Key Decisions** - Numbered decisions with bold titles
3. **Action Items** - Numbered items with Owner and Due fields
4. **Open Questions** - Numbered questions with context
5. **Raw Transcript** - Full unedited transcript preserved

**Architectural Decision Record (ADR) Template** (MADR v4 format):
1. **Context and Problem Statement** - Situation and problem driving the decision
2. **Decision Drivers** - Forces, concerns, and constraints
3. **Considered Options** - List of options evaluated
4. **Decision Outcome** - Chosen option with justification + Consequences + Confirmation
5. **Pros and Cons of the Options** - Detailed per-option analysis
6. **More Information** - Additional evidence, team agreements, links

---

**How Template Loading Works:**

D3 commands automatically load templates using this priority:

1. **Custom templates** (if configured in CLAUDE.md) → Use your customized templates
2. **Default templates** (if no custom config) → Use d3-templates skill references

No configuration needed unless you want to customize.

---

**When to Customize Templates:**

Only customize if you need:
- **Domain-specific sections** (healthcare, finance, legal, etc.)
- **Compliance requirements** (SOC2, HIPAA, GDPR sections)
- **Team-specific conventions** (your code review checklist, deployment steps, etc.)
- **Technology-specific sections** (React patterns, API versioning, etc.)
- **Meeting transcript customization** (add sections for Risks, Parking Lot, Next Meeting Agenda, etc.)
- **ADR customization** (add custom metadata fields, alternative formats, team-specific decision criteria)

**Customization Workflow:**

1. **Copy default templates to your repository:**
   ```bash
   mkdir -p .d3/templates
   cp -r ~/.claude/plugins/d3/skills/d3-templates/references/* .d3/templates/

   # Templates copied:
   # - feature-product-spec.md
   # - feature-tech-spec.md
   # - user-story.md
   # - meeting-transcript.md
   # - adr.md
   ```

2. **Configure custom paths in CLAUDE.md:**
   ```markdown
   ## D3 Configuration

   ### Templates
     - Feature Product Spec: ./.d3/templates/feature-product-spec.md
     - Feature Technical Spec: ./.d3/templates/feature-tech-spec.md
     - User Story: ./.d3/templates/user-story.md
     - Meeting Transcript: ./.d3/templates/meeting-transcript.md
     - ADR: ./.d3/templates/adr.md
   ```

3. **Customize templates for your needs:**
   Edit files in `.d3/templates/` to match your team's requirements.

4. **Version control your templates:**
   ```bash
   git add .d3/
   git commit -m "Add customized D3 templates"
   ```

5. **Evolve over time:**
   Update templates as your product and practices mature.

**Benefits of Customization:**
- Templates reflect your team's domain and patterns
- Compliance requirements built into every spec
- Version controlled alongside your code
- Changes tracked and reviewable

---

## Core Workflow

### Simplified Development Flow

```
Cross-functional Meeting/Discussion
        ↓
/d3:capture-transcript (optional — capture and structure the meeting)
        ↓
/d3:create-spec (paste transcript/document/description)
        ↓
Specification with BOTH Product & Technical Specs
(fills what's known, leaves rest empty)
        ↓
[Progressive Refinement as information becomes available]
        ↓
/d3:refine-spec PAGE-ID (paste any new information)
        ↓
Updated Specification (product, technical, or both)
        ↓
[Continue refining until ready]
        ↓
/d3:decompose PAGE-ID (specify project, paste transcript or discuss)
        ↓
Epic + User Stories (linked to specification with dependencies)
        ↓
[Implementation using your team's workflow]
        ↓
Commit, Create PR, and Merge
```

### Architectural Decision Workflow

When architectural decisions arise (framework choices, database selections, event-driven vs synchronous, etc.), capture them as ADRs:

```
Architectural discussion (meeting/transcript)
        ↓
/d3:create-adr (paste transcript or describe decision)
        ↓
ADR created (Context, Decision, Alternatives, Consequences)
        ↓
/d3:refine-spec PAGE-ID (incorporate ADR into spec)
        ↓
Spec's "Architectural Context > Relevant ADRs" section updated
```

ADRs are immutable records. If a decision changes, create a new ADR that supersedes the old one.

**Tool Selection:** Configure providers in `CLAUDE.md` to use your preferred tools:
- **Specifications:** Confluence, Notion, Markdown files, etc.
- **Stories:** Jira, Linear, GitHub Issues, etc.
- **Mix & Match:** Use different tools for specs and stories

---

## Commands

### Available Commands

| Command | Phase | Purpose |
|---------|-------|---------|
| `/d3:capture-transcript` | Capture | Capture and structure a meeting transcript |
| `/d3:create-spec` | Planning | Create feature specification from conversation |
| `/d3:create-adr` | Planning | Record architectural decisions as immutable ADRs |
| `/d3:refine-spec` | Planning | Update specifications with new information |
| `/d3:decompose` | Planning | Break into implementable user stories |

### When to Use Each Command

- **Had a meeting?** → `/d3:capture-transcript`
- **Starting a feature?** → `/d3:create-spec`
- **Made an architectural decision?** → `/d3:create-adr`
- **Got new information?** → `/d3:refine-spec`
- **Ready to implement?** → `/d3:decompose`

After decomposition, implement using your team's existing workflow.

---

## Detailed Command Reference

### 1. `/d3:capture-transcript`

**Purpose**: Capture and structure a meeting transcript as a referenceable artifact

**Workflow**:
1. Command asks you to paste the meeting transcript
2. Command asks: "What type of meeting was this?" (Planning, Technical, Standup, Retro, Other)
3. Agent extracts decisions, action items, and open questions in one pass
4. Agent proposes a title and filename
5. Agent shows structured summary for review
6. You confirm
7. Transcript stored via provider with full raw transcript preserved
8. Shows next steps (create-spec, refine-spec)

**When to use**: After any meeting where decisions were made, actions were assigned, or context was generated

**Example**:
```
You: /d3:capture-transcript

Agent: Please paste your meeting transcript below.

You: [Paste transcript from planning meeting]

Agent: What type of meeting was this?
       A) Planning
       B) Technical
       C) Standup
       D) Retro
       E) Other

You: A

Agent: Here's the structured transcript:

       Summary: The team discussed building a search feature...

       Key Decisions: 3
       1. Phased rollout approach — Start with basic text search...
       2. Elasticsearch for search backend...
       3. Search results page as separate route...

       Action Items: 4
       1. Create feature specification — Owner: Alice, Due: Feb 5
       ...

       Open Questions: 3
       1. Should search include archived content?
       ...

       Proposed title: "Search Feature Kickoff"
       File: transcripts/2026-02/planning-search-feature-kickoff.md

       Ready to save?

You: Yes

Agent: ✅ Transcript captured: Search Feature Kickoff

       Extracted:
       - Decisions: 3
       - Action Items: 4
       - Open Questions: 3

       Next steps:
       - Create a spec: /d3:create-spec
       - Refine an existing spec: /d3:refine-spec PAGE-ID
```

**Output**:
- Structured transcript with summary, decisions, action items, open questions
- Full raw transcript preserved
- Stored as referenceable artifact
- Clear next steps for spec creation or refinement

---

### 2. `/d3:create-spec`

**Purpose**: Create a comprehensive feature specification from any input

**Workflow**:
1. Command asks: "How would you like to provide the feature information?"
2. You provide: transcript, document, or conversational description
3. Command asks: "Where would you like to create this specification?"
4. Agent proposes a page title
5. Agent creates specification with **BOTH Product & Technical Spec sections**
6. Agent fills what's available from input, leaves rest empty (no hallucination)
7. Shows clear summary of what was filled vs what remains empty

**When to use**: Starting any new feature

**Example**:
```
You: /d3:create-spec

Agent: How would you like to provide the feature information?
       Option A: Meeting Transcript
       Option B: Document
       Option C: Describe Conversationally

You: Option A
     [Paste any meeting transcript - product, technical, or both]

Agent: Where would you like to create this specification?
       Location: ?

You: PROJ

Agent: Based on your input, I found information about [summary].

       I propose creating a specification named: "Advanced Search with Filters"
       Should I create this specification in PROJ?

You: Yes

Agent: Feature specification created.

       Product Spec: 70% complete (requirements clear, metrics missing)
       Technical Spec: 10% complete (only basic approach mentioned)

       Missing information can be added later using /d3:refine-spec [PAGE-ID]
```

**Output**:
- Specification with both Product AND Technical spec sections
- Fills only what's available from input
- Empty sections clearly marked
- Shows coverage percentage
- Clear next steps

---

### 3. `/d3:create-adr`

**Purpose**: Record an architectural decision as an immutable ADR following [MADR v4](https://adr.github.io/madr/) format

**Workflow**:
1. Command asks: "How would you like to provide the architectural decision information?"
2. You provide: transcript, document, or conversational description
3. Command asks: "Where would you like to create this ADR?"
4. Agent auto-numbers the ADR based on existing ADRs
5. Agent extracts: context/problem, decision drivers, considered options, decision outcome, consequences, and pros/cons per option
6. Agent asks if this supersedes an existing ADR
7. Shows ADR preview with uncertainty markers for any undecided aspects
8. You confirm
9. ADR created via provider
10. Agent suggests using `/d3:refine-spec` to incorporate the decision into relevant specs

**When to use**:
- An architectural decision has been made (framework, database, messaging pattern, etc.)
- A decision is being proposed and needs to be documented
- A previous decision is being changed (superseding)

**Example**:
```
You: /d3:create-adr

Agent: How would you like to provide the architectural decision information?
       Option A: Meeting Transcript
       Option B: Document
       Option C: Describe Conversationally

You: Option A
     [Paste transcript from architecture meeting about choosing PostgreSQL vs MongoDB]

Agent: I found an architectural decision in this transcript.

       Proposed ADR: ADR-003: Use PostgreSQL for primary data storage
       Status: Accepted
       Decision Drivers: ACID compliance, team expertise, query complexity

       Does this supersede an existing ADR?

You: No

Agent: ADR ready:

       ADR-003: Use PostgreSQL for primary data storage
       Status: Accepted
       Decision: Chosen option: "PostgreSQL", because it meets ACID requirements
       Options analyzed: 2 (PostgreSQL, MongoDB)
       Uncertainty markers: 1

       Ready to create?

You: Yes

Agent: ✅ ADR created: ADR-003: Use PostgreSQL for primary data storage

       Next: Use /d3:refine-spec to incorporate this decision
       into relevant specifications' "Architectural Context > Relevant ADRs" section.
```

**Output**:
- ADR in MADR v4 format with context, decision drivers, options analysis, and consequences
- Auto-numbered sequentially
- Cross-references if superseding another ADR
- Clear next steps for spec integration

---

### 4. `/d3:refine-spec PAGE-ID`

**Purpose**: Refine any part of existing specifications based on new information

**Workflow**:
1. Fetches specification and shows current coverage
2. Asks: "How would you like to provide the new information?"
3. You provide: transcript, document, feedback, or description
4. Agent detects which sections need updating (product, technical, or both)
5. Agent shows before/after for each proposed change
6. You confirm changes
7. Agent updates relevant sections in specification
8. Shows comprehensive summary of what changed

**When to use**:
- Any new information becomes available
- Product requirements change or get clarified
- Technical decisions are made or revised
- Stakeholder feedback needs incorporation
- Open questions get answered
- Gaps in specs need filling

**Example**:
```
You: /d3:refine-spec 123456789

Agent: I found Specification: Advanced Search

       **Current Coverage:**
       Product Spec: ~70% complete
       Technical Spec: ~30% complete

       How would you like to provide the new information?

You: Option A
     [Paste any transcript - automatically detects what to update]

Agent: I've analyzed your input and found information affecting:

       Product Specification Updates:
       - Requirements: Adding 2 new requirements
       - Open Questions: Resolving 1 question

       Technical Specification Updates:
       - Architecture: Adding 2 diagrams
       - API Contracts: Adding 3 endpoints

       [Shows before/after for each change]

       Should I proceed?

You: Yes

Agent: Specifications refined.
       Product Spec: 70% → 85% complete
       Technical Spec: 30% → 75% complete
```

**Output**:
- Updates to Product Spec, Technical Spec, or both
- Clear before/after comparison
- Shows coverage improvement
- Resolution tracking for open questions

---

### 5. `/d3:decompose PAGE-ID`

**Purpose**: Break feature into user stories through conversational planning

**Workflow**:
1. Fetches specification and both specs
2. Asks: "Which project should I create stories in?"
3. Asks: "Did you have a decomposition meeting?"
4. You paste transcript (preferred) OR discuss conversationally
5. Agent proposes decomposition strategies with pros/cons
6. Agent asks clarifying questions about boundaries
7. Agent shows proposed story breakdown
8. You confirm
9. Agent creates Epic for the feature (with specification reference)
10. Agent creates user stories under the Epic with complete acceptance criteria
11. Agent creates issue links for dependencies (blocks/is blocked by)

**When to use**:
- Specs are sufficiently complete
- Ready for sprint planning
- Need to break work into implementable chunks

**Example**:
```
You: /d3:decompose 123456789

Agent: I found Specification: Advanced Search
       Product Spec: 85% complete
       Technical Spec: 75% complete

       Which project should I create the user stories in?

You: PROJ

Agent: Great! I'll create stories in project PROJ.

       Did you have a decomposition meeting?
       Option A: Yes, I have a transcript
       Option B: No, let's decompose it together

You: Option A
     [Paste story decomposition meeting transcript]

Agent: I've analyzed your transcript:
       Proposed stories: 5 stories
       Approach: Hybrid (minimal first story, then enhancements)

       Clarifying questions:
       1. Should Story 1 span frontend and backend?
       2. Where should error handling go?
       ...

You: [Answer questions]

Agent: Here's the proposed breakdown:

       Story 1: Basic text search (backend + frontend)
       - Focus: End-to-end minimal search
       - ACs: 5 scenarios
       - Dependencies: None

       Story 2: Add status filter
       ...

       Does this look good?

You: Yes

Agent: Creating Epic for this feature in Project PROJ...

       Created Epic PROJ-41: Advanced Search with Filters
          https://yourproject.example.com/browse/PROJ-41

       Now creating user stories under this Epic...

       Created PROJ-42: Basic text search (under Epic PROJ-41)
       Created PROJ-43: Add status filter (under Epic PROJ-41)
       ...

       Creating dependency links between stories...

       Linked PROJ-42 blocks PROJ-43
       ...
```

**Output**:
- Epic created with reference to specification
- User stories created under the Epic
- Complete acceptance criteria (Gherkin format)
- Dependencies mapped using issue links (blocks/is blocked by)
- Implementation order suggested

---

### After Decomposition: Implementation

After creating your user stories with `/d3:decompose`, implement them using your team's existing development workflow. D3 focuses on the planning phase — turning conversations into structured context. How you write the code is up to you.

---

## Key Features

### Pragmatic Templates

Feature specs use a **streamlined 5-section template** (vs traditional 10+ sections):
- **Section 1: Overview** — What, why, who, and success metrics
- **Section 2: User Journey** — Primary workflow with edge cases
- **Section 3: Requirements** — Must have, should have, out of scope, constraints
- **Section 4: Open Questions & Assumptions** — All uncertainties in one place
- **Section 5: References** — Related docs, design links

This produces 2-3 pages instead of 5-10. Faster to write, faster to review, still captures everything that matters.

### Specification Storage

**Both Product and Technical specifications** are stored in your configured specification provider:

**Page Structure:**
```markdown
# Feature: [Feature Name]

## Product Specification
[Complete product/feature spec]

## Technical Specification
[Complete technical implementation spec]
```

One page holds both specs. Product and engineering collaborate in one place. Specs link to stories, stories link back. No context switching.

### Work Tracking for Stories

Features are decomposed into a hierarchical structure in your configured story provider:

**Epic/Feature Level:**
- One Epic (or equivalent) per feature
- Contains reference to specification
- Summary matches feature name
- All stories linked as children

**Story Level:**
- User stories created under the Epic
- Complete acceptance criteria (Gherkin format)
- Links back to spec
- Proper labels for categorization
- Dependencies tracked via issue links (blocks/is blocked by)
- Full workflow support

This creates a clear hierarchy: **Epic → Stories → Tasks** (if needed)

### Conversational Workflow

Commands work the way teams actually work:
- Ask for meeting transcripts (preferred input)
- Work conversationally if no transcript available
- Show what was found before asking questions
- Propose options with pros/cons
- Confirm before creating artifacts

### Transcript-First

Designed for real team meetings. Paste planning transcripts, technical discussion recordings, decomposition sessions, or refinement notes. The agent extracts information and fills gaps conversationally.

### Uncertainty Markers: Preventing AI Hallucination

One of the most critical features of this workflow is **explicit uncertainty management**:

**The Problem:** When AI generates specifications, it can "hallucinate" plausible-sounding details that were never discussed. This leads to incorrect assumptions becoming requirements.

**Our Solution:** Uncertainty markers make unknowns explicit:

- `[OPEN QUESTION: text]` - User decision needed, cannot proceed without answer
- `[DECISION PENDING: options]` - Valid choices exist, decision deferred
- `[ASSUMPTION: statement]` - Inference made from context, needs validation
- `[CLARIFICATION NEEDED: aspect]` - Requirement is vague, needs specificity

**How it works:**
1. Commands ask clarifying questions during generation
2. For unanswered questions → inline markers in spec body
3. All markers tracked in dedicated sections (Open Questions, Assumptions)
4. Quality gates prevent proceeding with too many unresolved uncertainties
5. User can resolve uncertainties immediately or mark for later

**Example:**
```markdown
BAD (silent hallucination):
Users authenticate via OAuth2 using Google provider

GOOD (explicit uncertainty):
Users authenticate via [OPEN QUESTION: OAuth2, password, or social login?]
```

**Benefits:**
- Prevents incorrect assumptions from becoming implementation requirements
- Makes knowledge gaps visible to stakeholders
- Creates clear decision points for product/tech teams
- Provides audit trail of what was decided vs assumed
- Enables better prioritization (can't implement stories with unresolved questions)

Use the `uncertainty-markers` skill for complete documentation and examples.

---

## Provider Architecture

D3 uses a **provider-based architecture** to work with any tools:

### How It Works

```
D3 Core Skills (Tool-Agnostic)
    ├── capture-transcript → Uses Transcript Provider
    ├── create-spec        → Uses Spec Provider
    ├── create-adr         → Uses ADR Provider (falls back to Spec Provider)
    ├── refine-spec        → Uses Spec Provider
    └── decompose          → Uses Spec Provider + Story Provider

Spec Providers (Pluggable)
    ├── atlassian-spec (Confluence) (built-in)
    ├── markdown-spec (Local files) (built-in)
    ├── notion-spec (Notion databases) [Expandable]
    └── [Your custom provider] [Expandable]

Story Providers (Pluggable)
    ├── atlassian-story (Jira) (built-in)
    ├── markdown-story (Local markdown files) (built-in)
    ├── linear-story (Linear) [Expandable]
    └── github-story (GitHub Issues) [Expandable]

Transcript Providers (Pluggable)
    ├── atlassian-transcript (Confluence) (built-in)
    ├── markdown-transcript (Local files) (built-in)
    └── [Your custom provider] [Expandable]
```

**Expandability:** The provider architecture makes it easy to add support for any tool. Built-in providers (Atlassian and Markdown) serve as reference implementations. Create custom providers by implementing the standard interfaces below.

### Provider Interfaces

**Spec Provider Operations:**
- `list_locations()` - List available storage locations
- `create_spec()` - Create new specification
- `get_spec()` - Retrieve specification
- `update_spec()` - Update specification
- `search_specs()` - Search specifications

**Story Provider Operations:**
- `list_projects()` - List available projects
- `get_issue_types()` - Get available issue types
- `create_epic()` - Create epic/feature container
- `create_story()` - Create user story
- `link_issues()` - Create dependencies (optional)

**Transcript Provider Operations:**
- `list_locations()` - List available storage locations
- `store_transcript()` - Store structured transcript
- `get_transcript()` - Retrieve transcript
- `list_transcripts()` - List transcripts (filter by type/month)
- `search_transcripts()` - Search transcript content

### Creating Custom Providers

To create a provider for a different tool (Notion, Linear, GitHub, etc.):

1. **Review existing provider**: See `d3-atlassian/skills/atlassian-spec-provider/SKILL.md` or `d3-atlassian/skills/atlassian-story-provider/SKILL.md`
2. **Create provider skill**: Implement operations as a new Claude Code plugin
3. **Map operations to your tool's MCP/API**: Each operation should call the appropriate tool
4. **Configure**: Update `CLAUDE.md` to reference your provider skill
5. **Use D3 commands**: They work automatically with any provider

---

## Best Practices

### For Feature Planning

1. **Record your meetings**: Transcripts are the best input
2. **Be specific**: Discuss concrete examples and scenarios
3. **Define boundaries**: What's in scope and out of scope
4. **Consider compliance early**: Security, privacy, accessibility

### For Technical Design

1. **Discuss trade-offs**: Capture pros/cons of approaches
2. **Reference patterns**: Mention existing similar features
3. **Be concrete**: Use real names, not placeholders
4. **Think about edge cases**: Error handling, performance, security

### For Story Decomposition

1. **Natural boundaries**: Break at logical workflow points
2. **Independent stories**: Minimize dependencies
3. **Consistent size**: Aim for similar-sized stories
4. **Complete ACs**: Cover happy path, errors, edge cases

### For Refinement

1. **Learn and adapt**: Refine based on development learnings
2. **Split when needed**: Don't force large stories
3. **Track reasons**: Document why stories changed
4. **Update dependencies**: Keep dependency graph current

---

## Typical Weekly Workflow

```
Monday: Feature Planning
├─ /d3:capture-transcript (capture meeting transcript)
├─ /d3:create-spec (create spec from transcript)
└─ Specification created

Tuesday-Wednesday: Refinement
├─ /d3:create-adr (record architectural decisions)
├─ /d3:refine-spec (add technical details + ADR references)
└─ Specifications complete

Thursday: Story Decomposition
├─ /d3:decompose
└─ User stories created

Next Sprint: Implementation
├─ Implement using your team's workflow
└─ Commit, PR, and merge
```

---

## Success Metrics

### Planning Phase
- Specs completed before coding
- All open questions resolved
- Stories have clear acceptance criteria
- Dependencies mapped in work tracker

### Implementation Phase
- All tests passing before PR
- All acceptance criteria covered by tests
- Code follows architecture guidelines

---

## Troubleshooting

### "I don't have meeting transcripts"

All commands work conversationally:
- Select "Option B: Describe conversationally" or "Option C"
- Answer the agent's questions
- Same quality output, just more interactive

### "My implementation is different from the spec"

Use `/d3:refine-spec` to update the specification with learnings from implementation.

### "My stories need to change during development"

That's expected. You can:
- Update stories directly in your story provider using native editing
- Split stories using your tool's split/clone features
- Create new stories and link them to the Epic
- Update dependencies using your tool's link functionality
- Use `/d3:refine-spec` to update the specification if requirements changed

### "Can I use this with other tools?"

Yes. D3 is tool-agnostic through its provider architecture:
- Configure providers in `CLAUDE.md`
- Use Confluence + Jira (default), Notion + Linear, Markdown + GitHub, or any combination
- Create custom providers for your specific tools
- See "Creating Custom Providers" section above

### "How do I implement the stories?"

Use your team's existing development workflow. D3 focuses on the planning phase — turning conversations into structured context and implementable stories. How you write the code is up to you.

---

## Benefits of This Approach

### 1. Tool Flexibility

- Use the tools your team already knows (Confluence, Notion, Jira, Linear, GitHub, etc.)
- Provider-based architecture adapts to your workflow
- Rich integration ecosystems available
- Familiar to your team members

### 2. Clear Separation of Concerns

- Spec provider for long-form documentation and specifications
- Story provider for actionable work items and tracking
- Natural workflow that matches team mental models

### 3. Native Integration

- Specs can reference stories
- Stories can link to specs
- Bidirectional linking supported
- Comments and collaboration built-in

### 4. Reflects Real Workflow

- Features defined through meetings (not documents first)
- Story decomposition happens separately from feature planning
- Refinement is an expected, separate step
- Transcripts capture context and discussion

### 5. Conversational, Not Automated

Commands ask questions, propose options, and confirm before creating artifacts. This feels like collaboration, not automation.

### 6. Team-Friendly

- Async-friendly — paste recorded meeting transcripts
- Clear traceability — spec to stories to tasks
- Supports iteration as the team learns

---

## Plugin Architecture

D3 is distributed as **Claude Code plugins** for easy installation and updates.

### Plugin Structure

**Built-in Plugins:**
- **`d3`** - Core plugin containing main skills and commands
- **`d3-atlassian`** - Atlassian provider (Confluence + Jira)
- **`d3-markdown`** - Markdown provider (local files + git)

**Expandable:**
- Create custom provider plugins for Notion, Linear, GitHub Issues, etc.
- See "Creating Custom Providers" section for implementation guide

### Repository Structure

```
dialog-driven-delivery/
├── README.md                  # This file - main documentation
├── d3/                        # Core D3 plugin
│   ├── .claude-plugin/
│   │   └── plugin.json       # Plugin manifest
│   ├── commands/             # Thin command triggers
│   │   ├── capture-transcript.md  # Capture meeting transcripts
│   │   ├── create-spec.md   # Create feature specs
│   │   ├── create-adr.md    # Create architectural decision records
│   │   ├── refine-spec.md   # Refine existing specs
│   │   └── decompose.md     # Decompose into user stories
│   ├── skills/               # Main workflow skills
│   ├── templates/            # Spec templates
│   └── README.md             # Plugin-specific docs
├── d3-atlassian/             # Atlassian provider plugin (built-in)
│   ├── .claude-plugin/
│   │   └── plugin.json       # Plugin manifest
│   ├── skills/               # Provider skills
│   │   ├── atlassian-spec-provider/    # Confluence specs
│   │   ├── atlassian-story-provider/   # Jira stories
│   │   └── atlassian-transcript-provider/  # Confluence transcripts
│   └── README.md             # → points to this file
├── d3-markdown/              # Markdown provider plugin (built-in)
│   ├── .claude-plugin/
│   │   └── plugin.json       # Plugin manifest
│   ├── skills/               # Provider skills
│   │   ├── markdown-spec-provider/       # Local file specs
│   │   ├── markdown-story-provider/      # Local file stories
│   │   └── markdown-transcript-provider/ # Local file transcripts
│   └── README.md             # → points to this file
└── .claude/                  # Original structure (deprecated)
```

### Local Testing

Test plugins locally before publishing:

```bash
# Test all built-in plugins together
claude --plugin-dir ./d3 --plugin-dir ./d3-atlassian --plugin-dir ./d3-markdown

# Test with specific provider
claude --plugin-dir ./d3 --plugin-dir ./d3-atlassian  # Atlassian only
claude --plugin-dir ./d3 --plugin-dir ./d3-markdown   # Markdown only

# Test core plugin only
claude --plugin-dir ./d3
```

### Plugin Marketplaces

To distribute these plugins:

1. Create a marketplace repository
2. Add plugin entries to `marketplace.json`
3. Users install via `/plugin install d3@your-marketplace`

See [Claude Code Plugin Marketplaces](https://code.claude.com/docs/en/plugin-marketplaces) for details.

---

## Integration

D3 integrates with:
- **Atlassian Confluence** - Feature specifications
- **Atlassian Jira** - User stories and tracking
- **GitHub** - Pull requests and code review
- **Git** - Version control and branching
- **Testing Frameworks** - Vitest, Pytest, etc.

---

## License

Open methodology, openly shared. Modify to fit your team's needs.

---

## Support

- Review individual skill files for detailed documentation
- [D3 Methodology](https://dialogdrivendelivery.com/) — principles and approach
- [Report issues](https://github.com/cdiniz/dialog-driven-delivery/issues)

---

*Built from real engagements. Designed for how teams actually work.*

*[Learn more about the D3 methodology](https://dialogdrivendelivery.com/) | Developed with [Equal Experts](https://www.equalexperts.com/)*
