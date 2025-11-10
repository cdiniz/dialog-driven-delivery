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
Linear Project with Product Spec
        ↓
[Product Refinement as needed]
        ↓
/refine-feature-brief PROJECT-42 (paste feedback/changes)
        ↓
Updated Product Spec
        ↓
Technical Design Meeting
        ↓
/create-technical-spec PROJECT-42 (paste transcript)
        ↓
Updates Linear Project (adds Technical Spec)
        ↓
[Technical Refinement as needed]
        ↓
/refine-technical-spec PROJECT-42 (paste technical refinement)
        ↓
Updated Technical Spec
        ↓
Story Decomposition Meeting
        ↓
/decompose-feature PROJECT-42 (paste transcript)
        ↓
User Stories in Linear (linked to project)
        ↓
[Story Refinement as needed]
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
4. Agent generates Product Specification
5. Agent creates Linear Project with **Product Spec in the project description**
6. Agent adds placeholder for Technical Spec (to be filled by `/create-technical-spec`)
7. Agent optionally saves local backup to `docs/features/[name].md`

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

Agent: [Generates Product Spec and creates Linear Project]
       ✅ Linear Project: PROJ-42 created
       ✅ Product Spec: In Linear project description
       ✅ Technical Spec: Placeholder added (ready for /create-technical-spec)
```

**Output**:
- Linear Project created with structured description
- Product Specification stored in project description
- Technical Spec placeholder added
- Optional local backup file
- Clear next steps

---

#### 1.5. `/refine-feature-brief PROJECT-KEY` (Optional)

**Purpose**: Refine existing product specification based on feedback or changing requirements

**Workflow**:
1. Fetches Linear Project and shows current Product Spec state
2. Asks: "What prompted this refinement? Do you have a transcript?"
3. You paste refinement transcript OR discuss conversationally
4. Agent analyzes what needs to change and shows current state
5. Agent asks clarifying questions about the changes
6. Agent shows before/after for each proposed change
7. You confirm changes
8. Agent **updates Product Spec section** in Linear project description
9. Agent identifies which user stories or technical specs might be impacted

**Requires**: Linear Project ID with existing Product Spec

**When to use**:
- User feedback revealed new requirements
- Stakeholder review requested changes
- Scope needs adjustment (add/remove features)
- Requirements were too vague and need clarification
- Success metrics need updating
- Business constraints changed
- Open questions now have answers

**Example**:
```
You: /refine-feature-brief PROJ-42

Agent: I found Linear Project PROJ-42: Advanced Search

       Product Spec: ✅ In Linear project description
       User Stories: 5 stories

       **Current Product Spec Summary:**
       - Must Have: 8 core features
       - Success Metrics: 2 metrics defined
       - Open Questions: 2 unresolved

       What prompted this product spec refinement?

       **Option A: Refinement Meeting Transcript**
       **Option B: Describe Changes Conversationally**

You: Option A
     [Paste transcript: "After user testing, we found users need to
      share saved filters with their team. Also, real-time search is
      too aggressive - 1-2 second delay is fine..."]

Agent: I've analyzed your refinement transcript:

       **Changes Requested:**
       1. Filter Sharing: Add team sharing capability
          - Reason: User testing revealed collaboration need
          - Impact: Requires new user story

       2. Performance Requirements: Relax real-time → 1-2s delay OK
          - Reason: User testing validated acceptable delay
          - Impact: Technical spec can be simplified

       Let me show you the proposed changes:

       ### Change 1: Add Filter Sharing (Section 3)

       **BEFORE:**
       ```
       * **FR5:** Users can save filter presets
         - Presets stored per-user
       ```

       **AFTER:**
       ```
       * **FR5:** Users can save and share filter presets
         - Presets can be personal or team-shared
         - Any team member can create shared presets
         - Shared presets visible to all team members
       ```

       **Rationale:** User testing revealed strong collaboration need
       **Type:** Addition + Modification
       **Impact:** Requires new user story for sharing functionality

       ### Change 2: Performance Requirements (Section 3)

       **BEFORE:**
       ```
       * **NFR2:** Real-time search results as user types (<100ms)
       ```

       **AFTER:**
       ```
       * **NFR2:** Search results within 1-2 seconds
         - Show loading indicator during search
       ```

       **Rationale:** User testing showed 1-2s delay acceptable
       **Type:** Modification + Clarification
       **Impact:** Technical spec can use simpler architecture

       Does this look correct?

You: Yes, update it

Agent: ✅ Product specification refined successfully!
       ✅ 2 sections updated
       ✅ 1 requirement added, 1 modified
       ✅ 2 open questions resolved

       **Impact on User Stories:**
       ⚠️ These stories may need review:
       - PROJ-44: Filter Presets (needs sharing capability)
       - NEW STORY NEEDED: For search refinement feature

       Consider running `/refine-decomposition PROJ-42` to update stories.

       **Impact on Technical Specification:**
       ⚠️ Technical spec may need review for:
       - Sharing permissions/authorization
       - Relaxed performance requirements

       Consider running `/refine-technical-spec PROJ-42` to update.
```

**Output**:
- Updated Product Spec section in Linear project description
- Clear before/after comparison of changes
- Rationale for each change documented
- Scope changes tracked (additions/deletions/clarifications)
- List of potentially impacted user stories and technical specs
- Resolution of open questions if answered

---

#### 2. `/create-technical-spec PROJECT-KEY`

**Purpose**: Generate technical specification and add it to Linear project

**Workflow**:
1. Fetches Linear Project and reads Product Spec from description
2. Asks: "Did you have a technical design meeting?"
3. You paste transcript (optional) OR discuss conversationally
4. Agent reviews your codebase patterns
5. Agent asks clarifying technical questions
6. Agent generates technical spec with smart section selection
7. Agent **updates Linear project description** to add Technical Spec section
8. Agent optionally saves local backup to `docs/specs/[project_key]/technical_spec.md`

**Requires**: Linear Project ID (e.g., `PROJ-42`)

**Example**:
```
You: /create-technical-spec PROJ-42

Agent: I found Linear Project PROJ-42: Advanced Search

       Product Spec: ✅ In Linear project description
       Technical Spec: ⏳ Placeholder (ready to populate)
       User Stories: 5 stories in project

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

Agent: [Generates technical spec and updates Linear]
       ✅ Linear project updated with Technical Spec
       ✅ Both Product and Technical specs now in Linear: [URL]
       Sections included: Data Models, API Contracts, UI Components
```

**Output**:
- Technical specification added to Linear project description
- Complete technical spec with relevant sections only
- Architecture diagrams (Mermaid)
- API contracts, data models, UI components
- Optional local backup file
- Clear implementation guidance

---

#### 2.5. `/refine-technical-spec PROJECT-KEY` (Optional)

**Purpose**: Refine existing technical specification based on new discussions or learnings

**Workflow**:
1. Fetches Linear Project and shows current Technical Spec state
2. Asks: "What prompted this refinement? Do you have a transcript?"
3. You paste refinement transcript OR discuss conversationally
4. Agent analyzes what needs to change and shows current state
5. Agent asks clarifying questions about the changes
6. Agent shows before/after for each proposed change
7. You confirm changes
8. Agent **updates Technical Spec section** in Linear project description
9. Agent identifies which user stories might be impacted

**Requires**: Linear Project ID with existing Technical Spec

**When to use**:
- Technical decisions change during development
- Architecture needs adjustment based on learnings
- New integrations or dependencies discovered
- Performance or security concerns identified
- Implementation reveals gaps in technical spec

**Example**:
```
You: /refine-technical-spec PROJ-42

Agent: I found Linear Project PROJ-42: Advanced Search

       Technical Spec: ✅ In Linear project description
       User Stories: 5 stories

       **Current Technical Decisions:**
       - Using Elasticsearch for full-text search
       - REST API with JWT authentication
       - React with Redux state management

       What prompted this technical spec refinement?

       **Option A: Refinement Meeting Transcript**
       **Option B: Describe Changes Conversationally**

You: Option A
     [Paste transcript: "We need to switch from Elasticsearch to PostgreSQL
      full-text search due to infrastructure constraints..."]

Agent: I've analyzed your refinement transcript:

       **Changes Requested:**
       1. Search Technology: Elasticsearch → PostgreSQL full-text search
          - Reason: Infrastructure team doesn't want to maintain ES cluster
          - Impact: Slightly slower search, but simpler architecture

       2. Performance Requirements: <100ms → <500ms acceptable
          - Reason: PostgreSQL FTS is sufficient for our needs

       Let me show you the proposed changes:

       ### Change 1: Technical Approach (Section 1)

       **BEFORE:**
       ```
       We will use Elasticsearch for fast, full-text search...
       ```

       **AFTER:**
       ```
       We will use PostgreSQL native full-text search with tsvector
       columns. This provides sufficient performance (<500ms) without
       requiring additional infrastructure...
       ```

       Does this look correct?

You: Yes, update it

Agent: ✅ Technical specification refined successfully!
       ✅ 3 sections updated
       ✅ 1 architecture diagram updated
       ✅ 1 open question resolved

       **Impact on User Stories:**
       ⚠️ These stories may need review:
       - PROJ-42: Backend API (data model changes needed)
       - PROJ-43: Search UI (updated performance expectations)
```

**Output**:
- Updated Technical Spec section in Linear project description
- Clear before/after comparison of changes
- Rationale for each change documented
- List of potentially impacted user stories
- Updated architecture diagrams if needed
- Resolution of open questions if answered

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

## Command Summary

| Command | Purpose | Input | Output | Use Case |
|---------|---------|-------|--------|----------|
| `/generate-feature-brief` | Create Product Spec | Transcript or conversation | Linear Project with Product Spec in description | Feature planning meeting |
| `/refine-feature-brief PROJECT-KEY` | Update Product Spec | Project + refinement transcript | Updated Product Spec with change rationale | Product refinement/feedback |
| `/create-technical-spec PROJECT-KEY` | Add Technical Spec | Project + optional transcript | Updates Linear project with Technical Spec | Technical design session |
| `/refine-technical-spec PROJECT-KEY` | Update Technical Spec | Project + refinement transcript | Updated Technical Spec with change rationale | Technical refinement/changes |
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
│   ├── features/                   # Optional: Local backups of Product specs
│   │   ├── advanced_search.md      # (Product specs live in Linear project descriptions)
│   │   ├── user_auth.md
│   │   └── reporting.md
│   ├── specs/                      # Optional: Local backups of Technical specs
│   │   ├── proj_42/                # (Technical specs live in Linear project descriptions)
│   │   │   ├── technical_spec.md   # Optional backup
│   │   │   ├── story_PROJ-42_tdd_tasks.md  # TDD task breakdowns
│   │   │   └── mockups/            # Design assets
│   │   └── proj_43/
│   │       └── technical_spec.md   # Optional backup
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
