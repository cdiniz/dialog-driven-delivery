# Spec-Driven Product Development Workflow

A pragmatic, streamlined methodology for building software products through **conversational, transcript-first** documentation and development. Designed for real-world teams where features are defined through meetings, refined through discussion, and implemented incrementally.

---

## Philosophy

This workflow is built on **pragmatic principles** for ongoing product development:

1. **Feature-Centric**: Most teams work on features
2. **Conversational & Engaging**: Commands ask for meeting transcripts and work interactively
3. **Incremental Delivery**: Break features into independently deliverable user stories
4. **Iterative Refinement**: Story decomposition can be refined as the team learns
5. **Quality Through Design**: Thoughtful specs prevent issues before they occur
6. **Explicit Over Implicit**: Uncertainties are marked, not assumed (prevents AI hallucination)
7. **Flexibility**: Use what adds value, customize templates for your context

---

## Two Workflow Modes

### Ongoing Development Mode (Primary - 95% of teams)

For teams working on **existing products** who define features through planning meetings:

```
Feature Planning Meeting
        ↓
/generate-feature-brief (paste transcript)
        ↓
Feature Spec + Linear Project
        ↓
Technical Design Meeting
        ↓
/create-technical-spec PROJECT-42 (paste transcript)
        ↓
Technical Specification
        ↓
Story Decomposition Meeting
        ↓
/decompose-feature PROJECT-42 (paste transcript)
        ↓
User Stories in Linear
        ↓
[Refinement as needed]
        ↓
/refine-decomposition PROJECT-42 (paste refinement notes)
        ↓
Updated Stories
        ↓
[Optional TDD Workflow]
/plan-user-story ISSUE-42
/implement-story docs/specs/.../tdd_tasks.md
```

---

## Prerequisites

- **Claude Code** installed and configured
- **Linear** for managing projects and user stories
- **Git** for version control
- **Testing framework** (optional, only for TDD automation)

---

## Installation

Copy the commands directory to your project:

```bash
# From this repository
cp -r .claude/commands /path/to/your/project/.claude/

# Optional: Copy agents if using TDD automation (steps 4-5)
cp -r .claude/agents /path/to/your/project/.claude/
```

---

## Conversational Slash Commands

### Core Workflow (Steps 1-4)

#### 1. `/generate-feature-brief`

**Purpose**: Create feature specification from meeting transcript or conversation

**Workflow**:
1. Command asks: "Do you have a meeting transcript or want to discuss?"
2. You paste transcript (preferred) OR discuss conversationally
3. Agent analyzes transcript and asks clarifying questions
4. Agent generates feature spec
5. Agent creates Linear Project
6. Agent saves feature spec to `docs/features/[name].md`

**When to use**: When you have a feature idea or planning meeting transcript

**No arguments required** - the command asks for input

**Example**:
```
You: /generate-feature-brief

Agent: How would you like to provide feature information?
       Option A: Meeting Transcript
       Option B: Describe Conversationally

You: Option A
     [Paste meeting transcript from your feature planning session]

Agent: I've analyzed your transcript. Here's what I found:
       Feature: Advanced Search with Filters
       Target Users: Project managers
       Key Workflows: ...

       Let me ask some clarifying questions:
       1. What are the success criteria?
       2. What's explicitly out of scope?
       ...

You: [Answer questions]

Agent: [Generates feature spec and creates Linear Project]
       ✅ Feature spec: docs/features/advanced_search.md
       ✅ Linear Project: PROJ-42
```

**Output**:
- Feature specification document
- Linear Project created
- Clear next steps

---

#### 2. `/create-technical-spec PROJECT-KEY`

**Purpose**: Generate technical specification from project and optional technical discussion

**Workflow**:
1. Fetches Linear Project and feature spec
2. Asks: "Did you have a technical design meeting?"
3. You paste transcript (optional) OR discuss conversationally
4. Agent reviews your codebase patterns
5. Agent asks clarifying technical questions
6. Agent generates technical spec with smart section selection
7. Agent saves to `docs/specs/[project_key]/technical_spec.md`

**Requires**: Linear Project ID (e.g., `PROJ-42`)

**Example**:
```
You: /create-technical-spec PROJ-42

Agent: I found Linear Project PROJ-42: Advanced Search

       Current Documentation:
       - Feature Spec: ✅ docs/features/advanced_search.md
       - 5 user stories in project

       Did you have a technical design meeting?
       Option A: Yes, I have a transcript
       Option B: No, let's discuss it now

You: Option A
     [Paste technical discussion transcript]

Agent: I've analyzed your transcript:
       Architecture: REST API with Elasticsearch
       Frontend: React with Redux
       ...

       Let me review your codebase...

       I found: You use Elasticsearch 8.x, Redux Toolkit, ...

       Clarifying questions:
       1. Which Elasticsearch index?
       2. Should filters persist in URL?
       ...

You: [Answer questions]

Agent: [Generates technical spec]
       ✅ Technical spec: docs/specs/proj_42/technical_spec.md
       Sections included: Data Models, API Contracts, UI Components
```

**Output**:
- Technical specification with relevant sections only
- Architecture diagrams (Mermaid)
- API contracts, data models, UI components
- Clear implementation guidance

---

#### 3. `/decompose-feature PROJECT-KEY`

**Purpose**: Break feature into user stories through conversational planning

**Workflow**:
1. Fetches Linear Project and documentation
2. Asks: "Did you have a decomposition meeting?"
3. You paste transcript (preferred) OR discuss conversationally
4. Agent proposes decomposition strategies with pros/cons
5. Agent asks clarifying questions about boundaries
6. Agent shows proposed story breakdown
7. You confirm
8. Agent creates user stories in Linear with complete acceptance criteria

**Requires**: Linear Project ID

**Example**:
```
You: /decompose-feature PROJ-42

Agent: I found Linear Project PROJ-42: Advanced Search
       Current stories: 0
       ✅ Ready to decompose

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

Agent: [Creates stories in Linear]
       ✅ Created PROJ-42: Basic text search
       ✅ Created PROJ-43: Add status filter
       ...
```

**Output**:
- User stories created in Linear
- Complete acceptance criteria (Gherkin format)
- Dependencies mapped
- Implementation order suggested

---

#### 4. `/refine-decomposition PROJECT-KEY`

**Purpose**: Refine existing story decomposition - split, merge, add, or modify stories

**Workflow**:
1. Fetches ALL existing stories and shows current state
2. Asks: "What prompted this refinement?"
3. You paste refinement transcript OR discuss changes
4. Agent analyzes and proposes specific changes
5. Agent shows before/after for each change
6. You confirm
7. Agent executes changes in Linear

**Requires**: Linear Project ID

**Use when**:
- Stories are too large and need splitting
- Stories are too small and should be merged
- New stories discovered during development
- Acceptance criteria need modification

**Example**:
```
You: /refine-decomposition PROJ-42

Agent: I found Linear Project PROJ-42: Advanced Search

       Current User Stories: 5 stories

       Story 1: PROJ-42 - Basic text search
       - Status: In Progress
       - Brief: End-to-end search functionality
       - ACs: 5 acceptance criteria

       Story 2: PROJ-43 - Add status filter
       ...

       What prompted this refinement?
       Option A: Refinement meeting
       Option B: Discovered during development
       Option C: Sprint planning feedback

You: Option B
     During development, we realized PROJ-42 is too large.
     We need to split it into backend and frontend stories.

Agent: I understand. Let me clarify:
       - Should PROJ-42 become the backend story?
       - Should I create a new story for frontend?
       - How should ACs be distributed?

You: [Answer questions]

Agent: Here's the refinement plan:

       1. Split PROJ-42: Basic text search
          - PROJ-42: Backend API (keep original)
            Scope: API endpoints, database
            ACs: [Backend ACs]
          - PROJ-50: Frontend UI (new story)
            Scope: UI components, search input
            ACs: [Frontend ACs]
            Dependencies: Depends on PROJ-42

       Does this look good?

You: Yes

Agent: [Executes changes]
       ✅ Updated PROJ-42 (split into backend)
       ✅ Created PROJ-50 (frontend split)
       ✅ Updated dependencies
```

**Output**:
- Modified/new stories in Linear
- Clear change summary
- Updated dependencies
- Updated implementation order

---

### Optional TDD Automation (Steps 5-6)

These steps are **completely optional** for teams that want structured, automated TDD workflow:

#### 5. `/plan-user-story ISSUE-ID`

**Purpose**: Generate detailed TDD task list for a user story

**When to use**: When you want structured Red-Green-Refactor task breakdown

**Skip if**: You prefer manual development or direct Claude interaction

#### 6. `/implement-story path/to/tdd_tasks.md`

**Purpose**: Orchestrate automated implementation with specialized agents

**When to use**: When you want fully automated TDD workflow with review cycles

**Skip if**: You prefer manual implementation

See the original README sections for details on these optional commands.

---

## Typical Weekly Flow

### Ongoing Organization (Most Common)

```bash
# Monday: Feature Planning Meeting
/generate-feature-brief
# [Paste meeting transcript, answer questions]
# Output: Feature spec + Linear Project PROJ-42

# Tuesday: Technical Design Session
/create-technical-spec PROJ-42
# [Paste technical discussion, answer questions]
# Output: Technical spec with architecture

# Wednesday: Story Decomposition Meeting
/decompose-feature PROJ-42
# [Paste decomposition discussion, confirm breakdown]
# Output: 5 user stories created (PROJ-42 through PROJ-46)

# Thursday: Sprint starts - Developer realizes story is too big
/refine-decomposition PROJ-42
# [Explain issue, confirm split]
# Output: PROJ-42 split into PROJ-42 (backend) + PROJ-50 (frontend)

# Friday: Developer starts implementation
# Option A: Manual development using specs as guide
# Option B: Optional TDD automation
/plan-user-story PROJ-42
/implement-story docs/specs/proj_42/story_PROJ-42_tdd_tasks.md
```

---

## Command Summary

| Command | Purpose | Input | Output | Use Case |
|---------|---------|-------|--------|----------|
| `/generate-feature-brief` | Create feature spec | Transcript or conversation | Feature spec + Linear Project | Feature planning meeting |
| `/create-technical-spec PROJECT-KEY` | Technical design | Project + optional transcript | Technical spec | Technical design session |
| `/decompose-feature PROJECT-KEY` | Break into stories | Project + optional transcript | User stories in Linear | Story decomposition meeting |
| `/refine-decomposition PROJECT-KEY` | Modify stories | Project + refinement notes | Updated stories | Refinement/learning |
| `/plan-user-story ISSUE-ID` | TDD task list | Story ID | TDD task breakdown | Optional: TDD planning |
| `/implement-story PATH` | Automated impl | TDD task file | Implemented code | Optional: TDD automation |

---

## Key Features

### Simplified, Pragmatic Templates

Our feature specs use a **streamlined 5-section template** (vs traditional 10+ sections):
- **Section 1: Overview** - What, why, who, and success metrics
- **Section 2: User Journey** - Primary workflow with edge cases
- **Section 3: Requirements** - Must have, should have, out of scope, constraints
- **Section 4: Open Questions & Assumptions** - All uncertainties in one place
- **Section 5: Risks** - High/medium risks with mitigations

Benefits:
- ✅ 2-3 pages instead of 5-10 pages
- ✅ Faster to write and review
- ✅ Still captures all essentials
- ✅ Can expand sections for complex features

### Conversational & Engaging

All commands use **conversational workflow**:
- ✅ Ask for meeting transcripts (preferred input)
- ✅ Work conversationally if no transcript
- ✅ Show what was found before asking questions
- ✅ Propose options with pros/cons
- ✅ Confirm before creating artifacts
- ✅ Provide clear summaries with next steps

### Transcript-First

Commands are designed for **real team meetings**:
- Paste planning meeting transcripts
- Paste technical discussion transcripts
- Paste decomposition meeting transcripts
- Paste refinement session notes
- Agent extracts information and fills gaps conversationally

### Smart & Adaptive

Commands **adapt to your project**:
- Review codebase patterns and follow them
- Select only relevant technical spec sections
- Propose decomposition strategies based on feature type
- Reference existing documentation
- Match your team's workflow

### Iterative & Refinable

Workflow supports **team learning**:
- Initial decomposition in one meeting
- Refinement in separate meeting (`/refine-decomposition`)
- Can run refinement multiple times
- Stories can be split, merged, added, or modified
- Preserves history and tracks changes

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
❌ BAD (silent hallucination):
Users authenticate via OAuth2 using Google provider

✅ GOOD (explicit uncertainty):
Users authenticate via [OPEN QUESTION: OAuth2, password, or social login?]
```

**Benefits:**
- Prevents incorrect assumptions from becoming implementation requirements
- Makes knowledge gaps visible to stakeholders
- Creates clear decision points for product/tech teams
- Provides audit trail of what was decided vs assumed
- Enables better prioritization (can't implement stories with unresolved questions)

See `.claude/uncertainty-markers.md` for complete documentation and `.claude/uncertainty-markers-examples.md` for real-world examples.

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

## Project Structure

When using this workflow, organize documentation like this:

```
your-project/
├── .claude/
│   ├── commands/                    # These slash commands
│   │   ├── generate-feature-brief.md
│   │   ├── create-technical-spec.md
│   │   ├── decompose-feature.md
│   │   ├── refine-decomposition.md
│   │   ├── plan-user-story.md
│   │   └── implement-story.md
│   └── agents/                      # Optional: TDD agents
│       ├── story-developer.md
│       ├── story-reviewer.md
│       ├── refinement-developer.md
│       └── test-fix-specialist.md
├── docs/
│   ├── features/                   # Feature specs
│   │   ├── advanced_search.md
│   │   ├── user_auth.md
│   │   └── reporting.md
│   ├── specs/                      # Technical specs per project
│   │   ├── proj_42/
│   │   │   ├── technical_spec.md
│   │   │   ├── story_PROJ-42_tdd_tasks.md
│   │   │   └── mockups/
│   │   └── proj_43/
│   │       └── technical_spec.md
│   └── architecture/               # Your architecture docs
├── src/
│   ├── backend/
│   └── frontend/
└── tests/
```

---

## Benefits of This Approach

### 1. Reflects Real Workflow

- Features defined through meetings (not documents first)
- Story decomposition happens separately from feature planning
- Refinement is an expected, separate step
- Transcripts capture context and discussion

### 2. Conversational & Engaging

- Commands feel like collaboration, not automation
- Agent asks questions and proposes options
- Shows understanding before taking action
- Confirms before creating artifacts

### 3. Flexible & Modular

- Use core workflow (steps 1-4) for documentation
- Optionally add TDD automation (steps 5-6)
- Refine decomposition as many times as needed

### 4. Quality Through Process

- Complete acceptance criteria from the start
- Technical specs follow codebase patterns
- Smart section selection (only relevant sections)
- Maps ACs to technical implementation

### 5. Team-Friendly

- Async-friendly (paste recorded meeting transcripts)
- Supports iteration and learning
- Clear traceability (feature → technical spec → stories → tasks)
- Preserves history of changes

---

## Migration from Previous Version

If you used the old workflow:

**Old Command → New Command**

- `/create-feature-and-stories "description"` → Split into:
  - `/generate-feature-brief` (feature spec + project)
  - `/decompose-feature PROJECT-KEY` (stories)
- `/create-feature-spec PROJECT-KEY` → `/create-technical-spec PROJECT-KEY`
- New: `/refine-decomposition PROJECT-KEY` (separate refinement)

**Key Changes**:

1. **No arguments for feature brief**: Command asks for transcript
2. **Decomposition is separate**: No longer combined with feature creation
3. **Refinement is explicit**: New command for modifying decomposition
4. **Transcript-first**: All commands prefer meeting transcripts

---

## Troubleshooting

### "I don't have meeting transcripts"

No problem! All commands work conversationally:
- Select "Option B: Describe conversationally"
- Answer the agent's questions
- Same quality output, just more interactive

### "My stories need to change during development"

Perfect! That's expected:
- Use `/refine-decomposition PROJECT-KEY`
- Explain what changed and why
- Agent will update stories intelligently

### "Can I use this with other issue trackers?"

The workflow is Linear-focused but adaptable:
- Core concepts work with any tracker
- Modify commands to use your tracker's API
- Or use specs as guides and create issues manually

---

## Philosophy: Why This Workflow?

This workflow is designed for **how teams actually work**:

1. **Features, not products**: Daily work is feature-level, not product-level
2. **Meetings produce artifacts**: Planning meetings → transcripts → specs
3. **Decomposition evolves**: Story breakdown improves with team learning
4. **Conversation matters**: Nuance and context from discussions are valuable
5. **Documentation enables quality**: Good specs prevent issues before coding
6. **Automation is optional**: TDD workflow helps but isn't required

The result is a **pragmatic, conversational methodology** that fits real development workflows while maintaining high documentation quality and traceability.

---

## Support

For issues, questions, or contributions:
- Review individual command files for detailed documentation
- Each command has extensive examples and guidelines
- Commands are designed to be self-explanatory
- Agent prompts guide you through the process

---

## License

This methodology is open for use and adaptation. Modify commands to fit your team's needs.
