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
8. **Unified Approach**: Single commands handle both product and technical aspects naturally

---

## Simplified Workflow (v2.0)

### Core Development Flow

For teams working on **any product** development:

```
Any Initial Meeting/Discussion
        ↓
/create-spec (paste transcript/document/description)
        ↓
Linear Project with BOTH Product & Technical Specs
(fills what's known, leaves rest empty)
        ↓
[Progressive Refinement as information becomes available]
        ↓
/refine-spec PROJECT-42 (paste any new information)
        ↓
Updated Specs (product, technical, or both)
        ↓
[Continue refining until ready]
        ↓
/decompose-feature PROJECT-42 (paste transcript or discuss)
        ↓
User Stories in Linear (linked to project)
        ↓
[Story Refinement as needed]
        ↓
/refine-decomposition PROJECT-42 (paste refinement notes)
        ↓
Updated Stories
        ↓
[Optional DEV Workflow]
/plan-user-story ISSUE-42
/implement-story docs/specs/.../tasks.md
```

---

## Prerequisites

- **Claude Code** installed and configured
- **Linear** for managing projects and user stories
- **Git** for version control

---

## Installation

Copy the commands directory to your project:

```bash
# From this repository
cp -r .claude/commands /path/to/your/project/.claude/

# Optional: Copy agents if using this dev workflow
cp -r .claude/agents /path/to/your/project/.claude/
```

---

## Conversational Slash Commands

### Core Workflow Commands (v2.0 - Simplified)

#### 1. `/create-spec`

**Purpose**: Create a comprehensive project specification from any input

**Workflow**:
1. Command asks: "How would you like to provide the project information?"
2. You provide: transcript, document, or conversational description
3. Agent proposes a project name
4. Agent creates Linear Project with **BOTH Product & Technical Spec sections**
5. Agent fills what's available from input, leaves rest empty (no hallucination)
6. Shows clear summary of what was filled vs what remains empty

**When to use**: Starting any new feature or project

**No arguments required** - the command asks for input

**Example**:
```
You: /create-spec

Agent: How would you like to provide the project information?
       Option A: Meeting Transcript
       Option B: Document
       Option C: Describe Conversationally

You: Option A
     [Paste any meeting transcript - product, technical, or both]

Agent: Based on your input, I found information about [summary].

       I propose creating a Linear project named: "Advanced Search with Filters"
       Should I create this Linear project?

You: Yes

Agent: ✅ Project specification created successfully!

       📋 Product Spec: 70% complete (requirements clear, metrics missing)
       🔧 Technical Spec: 10% complete (only basic approach mentioned)

       Missing information can be added later using /refine-spec PROJ-42
```

**Output**:
- Linear Project with both Product AND Technical spec sections
- Fills only what's available from input
- Empty sections clearly marked
- Shows coverage percentage
- Clear next steps

---

#### 2. `/refine-spec PROJECT-KEY`

**Purpose**: Refine any part of existing specifications based on new information

**Workflow**:
1. Fetches Linear Project and shows current specification coverage
2. Asks: "How would you like to provide the new information?"
3. You provide: transcript, document, feedback, or description
4. Agent detects which sections need updating (product, technical, or both)
5. Agent shows before/after for each proposed change
6. You confirm changes
7. Agent updates relevant sections in Linear project description
8. Shows comprehensive summary of what changed

**Requires**: Linear Project ID

**When to use**:
- Any new information becomes available
- Product requirements change or get clarified
- Technical decisions are made or revised
- Stakeholder feedback needs incorporation
- Open questions get answered
- Gaps in specs need filling

**Example**:
```
You: /refine-spec PROJ-42

Agent: I found Linear Project PROJ-42: Advanced Search

       **Current Coverage:**
       📋 Product Spec: ~70% complete
       🔧 Technical Spec: ~30% complete

       How would you like to provide the new information?

You: Option A
     [Paste any transcript - automatically detects what to update]

Agent: I've analyzed your input and found information affecting:

       📋 Product Specification Updates:
       - Requirements: Adding 2 new requirements
       - Open Questions: Resolving 1 question

       🔧 Technical Specification Updates:
       - Architecture: Adding 2 diagrams
       - API Contracts: Adding 3 endpoints

       [Shows before/after for each change]

       Should I proceed?

You: Yes

Agent: ✅ Specifications refined successfully!
       Product Spec: 70% → 85% complete
       Technical Spec: 30% → 75% complete
```

**Output**:
- Updates to Product Spec, Technical Spec, or both
- Clear before/after comparison
- Shows coverage improvement
- Resolution tracking for open questions

---

#### 3. `/decompose-feature PROJECT-KEY`

**Purpose**: Break feature into user stories through conversational planning

**Workflow**:
1. Fetches Linear Project and both specs
2. Asks: "Did you have a decomposition meeting?"
3. You paste transcript (preferred) OR discuss conversationally
4. Agent proposes decomposition strategies with pros/cons
5. Agent asks clarifying questions about boundaries
6. Agent shows proposed story breakdown
7. You confirm
8. Agent creates user stories in Linear with complete acceptance criteria

**Requires**: Linear Project ID

**When to use**:
- Specs are sufficiently complete
- Ready for sprint planning
- Need to break work into implementable chunks

**Example**:
```
You: /decompose-feature PROJ-42

Agent: I found Linear Project PROJ-42: Advanced Search
       Product Spec: ✅ 85% complete
       Technical Spec: ✅ 75% complete
       Current stories: 0

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

### Optional Dev Workflow (Steps 5-6)

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
# Output: Linear Project PROJ-42 with Product Spec in description

# Tuesday (Optional): Product Spec Refinement
# [If stakeholders provided feedback or requirements changed]
/refine-feature-brief PROJ-42
# [Paste feedback transcript, confirm changes]
# Output: Product Spec updated with refined requirements, impacted areas identified

# Wednesday: Technical Design Session
/create-technical-spec PROJ-42
# [Paste technical discussion, answer questions]
# Output: Linear Project PROJ-42 updated with Technical Spec (both specs in Linear)

# Thursday (Optional): Technical Refinement
# [If technical decisions change or new learnings emerge]
/refine-technical-spec PROJ-42
# [Paste refinement transcript, confirm changes]
# Output: Technical Spec updated with new decisions, impacted stories identified

# Friday: Story Decomposition Meeting
/decompose-feature PROJ-42
# [Paste decomposition discussion, confirm breakdown]
# Output: 5 user stories created (PROJ-42 through PROJ-46)

# Later: Sprint starts - Developer realizes story is too big
/refine-decomposition PROJ-42
# [Explain issue, confirm split]
# Output: PROJ-42 split into PROJ-42 (backend) + PROJ-50 (frontend)

# Later: Developer starts implementation
# Option A: Manual development using specs as guide
# Option B: Optional TDD automation
/plan-user-story PROJ-42
/implement-story docs/specs/proj_42/story_PROJ-42_tdd_tasks.md
```

---

## Command Summary (v2.0)

| Command | Purpose | Input | Output | Use Case |
|---------|---------|-------|--------|----------|
| `/create-spec` | Create both Product & Technical specs | Any context (transcript/doc/description) | Linear Project with both specs (fills what's known) | Starting any feature |
| `/refine-spec PROJECT-KEY` | Update any part of specs | Project + new information | Updated specs (auto-detects what to update) | Any new information available |
| `/decompose-feature PROJECT-KEY` | Break into stories | Project + optional transcript | User stories in Linear | Ready for sprint planning |
| `/refine-decomposition PROJECT-KEY` | Modify stories | Project + refinement notes | Updated stories | Story refinement/learning |
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

### Linear-First Documentation

**Both Product and Technical specifications** are stored **directly in Linear project descriptions**:

**Project Description Structure:**
```markdown
## 📋 Product Specification
[Complete product/feature spec]

## 🔧 Technical Specification
[Complete technical implementation spec]
```

**Benefits:**
- **Single Source of Truth**: The Linear project description contains BOTH specs
- **Built-in Collaboration**: Product and engineering teams collaborate in one place
- **No Context Switching**: View specs, stories, and progress all in Linear
- **Always Accessible**: No need to find files or navigate folders
- **Version Control**: Linear tracks changes to project descriptions
- **Unified Discussions**: Comments on both specs stay together
- **Optional Backups**: Can save local copies for reference, but Linear is authoritative

**Why This Works:**
- ✅ Product and engineering see the same information
- ✅ Specs always linked to project and stories
- ✅ No sync issues between docs and project management
- ✅ Easier onboarding (one tool, one location)
- ✅ Technical decisions visible to product team
- ✅ Product context visible to engineers

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
│   ├── commands/                    # Slash commands (v2.0)
│   │   ├── create-spec.md          # NEW: Unified spec creation
│   │   ├── refine-spec.md          # NEW: Unified spec refinement
│   │   ├── decompose-feature.md
│   │   ├── refine-decomposition.md
│   │   ├── plan-user-story.md      # Optional: Dev Workflow planning
│   │   └── implement-story.md      # Optional: Dev Workflow automation
│   └── agents/                      # Optional: Dev Workflow agents
│       ├── story-developer.md
│       ├── story-reviewer.md
│       ├── refinement-developer.md
│       └── test-fix-specialist.md
├── docs/
│   ├── specs/                      # Optional: Local backups
│   │   ├── proj_42/                # (All specs live in Linear project descriptions)
│   │   │   ├── combined_spec.md    # Optional backup of Linear content
│   │   │   ├── story_PROJ-42_tdd_tasks.md  # TDD task breakdowns
│   │   │   └── mockups/            # Design assets
│   │   └── proj_43/
│   │       └── combined_spec.md    # Optional backup
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
- Optionally DEV automation (steps 5-6)
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

## Migration from v1.0 to v2.0

**Simplified Command Structure:**

**Old Commands (v1.0) → New Commands (v2.0)**

| Old Command | New Command | Change |
|------------|-------------|---------|
| `/generate-feature-brief` | `/create-spec` | Unified - creates both specs |
| `/create-technical-spec PROJECT` | `/create-spec` or `/refine-spec PROJECT` | Merged into unified commands |
| `/refine-feature-brief PROJECT` | `/refine-spec PROJECT` | Unified refinement |
| `/refine-technical-spec PROJECT` | `/refine-spec PROJECT` | Unified refinement |
| `/decompose-feature PROJECT` | `/decompose-feature PROJECT` | No change |
| `/refine-decomposition PROJECT` | `/refine-decomposition PROJECT` | No change |

**Key Improvements:**

1. **Single creation command**: `/create-spec` creates both Product and Technical specs
2. **Single refinement command**: `/refine-spec` updates whatever needs updating
3. **Progressive filling**: Start with what you have, fill gaps over time
4. **No forced separation**: Product and technical info can be mixed naturally
5. **Smart detection**: System determines what to update based on content

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
6. **Automation is adaptable**: Dev workflow in place but isn't required

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
