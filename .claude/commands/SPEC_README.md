# Spec-Driven Product Development Workflow

A pragmatic, streamlined methodology for building software products through **conversational, transcript-first** documentation and development. Designed for real-world teams where features are defined through meetings, refined through discussion, and implemented incrementally.

**Now with Atlassian Integration:** Specifications in Confluence, Stories in Jira.

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
9. **Atlassian Native**: Confluence for specs, Jira for stories - industry standard tools

---

## Simplified Workflow (v2.0 - Atlassian Edition)

### Core Development Flow

For teams working on **any product** development:

```
Any Initial Meeting/Discussion
        ↓
/create-spec (paste transcript/document/description)
        ↓
Confluence Page with BOTH Product & Technical Specs
(fills what's known, leaves rest empty)
        ↓
[Progressive Refinement as information becomes available]
        ↓
/refine-spec PAGE-ID (paste any new information)
        ↓
Updated Confluence Page (product, technical, or both)
        ↓
[Continue refining until ready]
        ↓
/decompose-feature PAGE-ID (specify Jira project, paste transcript or discuss)
        ↓
Epic + Jira Stories (linked to Confluence page with dependencies)
        ↓
[Optional: AI-Assisted Implementation - see CODING_README.md]
/implement-story (Jira story link + Confluence spec)
        ↓
Code + Tests + Feature Branch
        ↓
/commit-and-open-pr
        ↓
Pull Request Created
        ↓
/address-pr-feedback (iteratively)
        ↓
Merge to Main
```

---

## Prerequisites

- **Claude Code** installed and configured
- **Confluence** for feature specifications
- **Jira** for user stories and tracking
- **Atlassian MCP Server** configured for Claude Code
- **Git** for version control

---

## Installation

Copy the commands directory to your project:

```bash
# From this repository
cp -r .claude/commands /path/to/your/project/.claude/
```

---

## Conversational Slash Commands

### Core Workflow Commands (v2.0 - Simplified for Atlassian)

#### 1. `/create-spec`

**Purpose**: Create a comprehensive feature specification in Confluence from any input

**Workflow**:
1. Command asks: "How would you like to provide the feature information?"
2. You provide: transcript, document, or conversational description
3. Command asks: "Which Confluence space should I create this in?"
4. Agent proposes a page title
5. Agent creates Confluence page with **BOTH Product & Technical Spec sections**
6. Agent fills what's available from input, leaves rest empty (no hallucination)
7. Shows clear summary of what was filled vs what remains empty

**When to use**: Starting any new feature

**No arguments required** - the command asks for input

**Example**:
```
You: /create-spec

Agent: How would you like to provide the feature information?
       Option A: Meeting Transcript
       Option B: Document
       Option C: Describe Conversationally

You: Option A
     [Paste any meeting transcript - product, technical, or both]

Agent: Where would you like to create this in Confluence?
       Confluence Space: ?

You: PROJ

Agent: Based on your input, I found information about [summary].

       I propose creating a Confluence page named: "Advanced Search with Filters"
       Should I create this page in PROJ space?

You: Yes

Agent: ✅ Feature specification created successfully!

       📋 Product Spec: 70% complete (requirements clear, metrics missing)
       🔧 Technical Spec: 10% complete (only basic approach mentioned)

       Missing information can be added later using /refine-spec [PAGE-ID]
```

**Output**:
- Confluence page with both Product AND Technical spec sections
- Fills only what's available from input
- Empty sections clearly marked
- Shows coverage percentage
- Clear next steps

---

#### 2. `/refine-spec PAGE-ID`

**Purpose**: Refine any part of existing specifications based on new information

**Workflow**:
1. Fetches Confluence page and shows current specification coverage
2. Asks: "How would you like to provide the new information?"
3. You provide: transcript, document, feedback, or description
4. Agent detects which sections need updating (product, technical, or both)
5. Agent shows before/after for each proposed change
6. You confirm changes
7. Agent updates relevant sections in Confluence page
8. Shows comprehensive summary of what changed

**Requires**: Confluence Page ID or URL

**When to use**:
- Any new information becomes available
- Product requirements change or get clarified
- Technical decisions are made or revised
- Stakeholder feedback needs incorporation
- Open questions get answered
- Gaps in specs need filling

**Example**:
```
You: /refine-spec 123456789

Agent: I found Confluence Page: Advanced Search

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

#### 3. `/decompose-feature PAGE-ID`

**Purpose**: Break feature into user stories in Jira through conversational planning

**Workflow**:
1. Fetches Confluence page and both specs
2. Asks: "Which Jira project should I create stories in?"
3. Asks: "Did you have a decomposition meeting?"
4. You paste transcript (preferred) OR discuss conversationally
5. Agent proposes decomposition strategies with pros/cons
6. Agent asks clarifying questions about boundaries
7. Agent shows proposed story breakdown
8. You confirm
9. Agent creates Epic in Jira for the feature (with Confluence reference)
10. Agent creates user stories under the Epic with complete acceptance criteria
11. Agent creates Jira issue links for dependencies (blocks/is blocked by)

**Requires**: Confluence Page ID/URL

**When to use**:
- Specs are sufficiently complete
- Ready for sprint planning
- Need to break work into implementable chunks

**Example**:
```
You: /decompose-feature 123456789

Agent: I found Confluence Page: Advanced Search
       Product Spec: ✅ 85% complete
       Technical Spec: ✅ 75% complete

       Which Jira project should I create the user stories in?

You: PROJ

Agent: Great! I'll create stories in Jira project PROJ.

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

Agent: Creating Epic for this feature in Jira Project PROJ...

       ✅ Created Epic PROJ-41: Advanced Search with Filters
          https://yoursite.atlassian.net/browse/PROJ-41

       Now creating user stories under this Epic...

       ✅ Created PROJ-42: Basic text search (under Epic PROJ-41)
       ✅ Created PROJ-43: Add status filter (under Epic PROJ-41)
       ...

       Creating dependency links between stories...

       ✅ Linked PROJ-42 blocks PROJ-43
       ...
```

**Output**:
- Epic created in Jira with reference to Confluence page
- Jira stories created under the Epic
- Complete acceptance criteria (Gherkin format)
- Dependencies mapped using Jira issue links (blocks/is blocked by)
- Implementation order suggested

---

### Optional Dev Workflow (Steps 4-5)

These steps are **completely optional** for teams that want AI-assisted implementation workflow:

#### 4. `/implement-story`

**Purpose**: Implement a Jira story from requirements to working code

**When to use**: When you're ready to start coding a story

**Skip if**: You prefer pure manual development

#### 5. `/commit-and-open-pr`

**Purpose**: Commit changes and create a pull request

**When to use**: When implementation is complete and tests are passing

#### 6. `/address-pr-feedback`

**Purpose**: Systematically address PR review feedback

**When to use**: After receiving code review feedback

**📖 For comprehensive implementation guidance, see [CODING_README.md](CODING_README.md)**

---

---

## Command Summary (v2.0 - Atlassian)

| Command | Purpose | Input | Output | Use Case |
|---------|---------|-------|--------|----------|
| `/create-spec` | Create both Product & Technical specs | Any context (transcript/doc/description) + Confluence space | Confluence page with both specs (fills what's known) | Starting any feature |
| `/refine-spec PAGE-ID` | Update any part of specs | Page ID + new information | Updated Confluence page (auto-detects what to update) | Any new information available |
| `/create-user-stories-from-spec PAGE-ID` | Break into Epic + stories | Page ID + Jira project + optional transcript | Epic + Jira stories with issue links | Ready for sprint planning |
| `/implement-story` | Implement a Jira story | Jira story + Confluence spec links | Code + tests + feature branch | Optional: Start coding |
| `/manual-test-story` | Manual browser testing | Jira story link | Test results + screenshots | Optional: Verify ACs |
| `/commit-and-open-pr` | Commit and create PR | None (current branch) | Commit + PR with description | Optional: Create PR |
| `/address-pr-feedback` | Address review feedback | PR link | Fixed code + updated PR | Optional: Handle feedback |

📖 **For detailed coding workflow, see [CODING_README.md](CODING_README.md)**

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

### Confluence-First Documentation

**Both Product and Technical specifications** are stored **directly in Confluence pages**:

**Page Structure:**
```markdown
# Feature: [Feature Name]

## 📋 Product Specification
[Complete product/feature spec]

## 🔧 Technical Specification
[Complete technical implementation spec]
```

**Benefits:**
- **Single Source of Truth**: The Confluence page contains BOTH specs
- **Built-in Collaboration**: Product and engineering teams collaborate in one place
- **No Context Switching**: View specs in Confluence, track work in Jira
- **Always Accessible**: No need to find files or navigate folders
- **Version Control**: Confluence tracks changes to pages
- **Unified Discussions**: Comments on both specs stay together
- **Native Atlassian**: Confluence pages can link to Jira issues, Jira issues link back
- **Rich Content**: Support for images, diagrams, tables, macros

**Why This Works:**
- ✅ Product and engineering see the same information
- ✅ Specs always linked to Jira project
- ✅ No sync issues between docs and project management
- ✅ Easier onboarding (industry-standard tools)
- ✅ Technical decisions visible to product team
- ✅ Product context visible to engineers

### Jira for Actionable Work

Features are decomposed into a hierarchical structure in Jira:

**Epic Level:**
- One Epic per feature
- Epic contains reference to Confluence specification
- Epic summary matches feature name
- All stories for the feature are linked as children

**Story Level:**
- User stories created under the Epic
- Complete acceptance criteria (Gherkin format)
- Links back to Confluence spec page
- Proper labels for categorization
- Dependencies tracked via Jira issue links (blocks/is blocked by)
- Full Jira workflow support

This creates a clear hierarchy: **Epic → Stories → Tasks** (if needed)

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
- Specifications can be refined as new information becomes available (`/refine-spec`)
- Stories can be refined directly in Jira using native tools
- Epic structure provides clear organization and traceability
- Preserves history and tracks changes in both Confluence and Jira

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
│   │   ├── SPEC_README.md                      # Spec workflow documentation
│   │   ├── CODING_README.md                    # Implementation workflow documentation
│   │   ├── create-spec.md                      # Unified Confluence spec creation
│   │   ├── refine-spec.md                      # Unified Confluence spec refinement
│   │   ├── create-user-stories-from-spec.md    # Confluence → Jira decomposition
│   │   ├── implement-story.md                  # AI-assisted implementation
│   │   ├── manual-test-story.md                # Browser testing with Chrome DevTools
│   │   ├── commit-and-open-pr.md               # Create PR
│   │   └── address-pr-feedback.md              # Handle PR feedback
├── docs/
│   └── architecture/               # Your architecture docs
├── src/
│   ├── backend/
│   └── frontend/
└── tests/
```

**Note:**
- Feature specs live in Confluence, not in local files
- User stories live in Jira
- Code and tests live in source control

---

## Benefits of This Approach

### 1. Industry Standard Tools

- Confluence and Jira are the most widely used tools in enterprise
- Better integration ecosystem
- Familiar to most developers and product managers
- Better compliance and security features

### 2. Clear Separation of Concerns

- Confluence for long-form documentation and specs
- Jira for actionable work items and tracking
- Natural workflow that matches team mental models

### 3. Native Integration

- Confluence pages can embed Jira queries
- Jira issues can link to Confluence pages
- Bidirectional linking built into the platform
- Comments and mentions work across tools

### 4. Reflects Real Workflow

- Features defined through meetings (not documents first)
- Story decomposition happens separately from feature planning
- Refinement is an expected, separate step
- Transcripts capture context and discussion

### 5. Conversational & Engaging

- Commands feel like collaboration, not automation
- Agent asks questions and proposes options
- Shows understanding before taking action
- Confirms before creating artifacts

### 6. Flexible & Modular

- Use core workflow (steps 1-3) for documentation and decomposition
- Optionally add dev automation (steps 4-5)
- Refine specifications and stories as needed

### 7. Quality Through Process

- Complete acceptance criteria from the start
- Technical specs follow codebase patterns
- Smart section selection (only relevant sections)
- Maps ACs to technical implementation

### 8. Team-Friendly

- Async-friendly (paste recorded meeting transcripts)
- Supports iteration and learning
- Clear traceability (Confluence page → Jira stories → tasks)
- Preserves history of changes

---

## Troubleshooting

### "I don't have meeting transcripts"

No problem! All commands work conversationally:
- Select "Option B: Describe conversationally" or "Option C"
- Answer the agent's questions
- Same quality output, just more interactive

### "My stories need to change during development"

That's expected and normal! You can:
- Update stories directly in Jira using native editing
- Split stories using Jira's "Split Issue" feature
- Create new stories and link them to the Epic
- Update dependencies using Jira's link functionality
- Use `/refine-spec` to update the Confluence specification if requirements changed

### "Can I use this with other tools?"

The workflow is Atlassian-focused but adaptable:
- Core concepts work with any tracker/wiki
- Modify commands to use your tool's API
- Or use specs as guides and create issues manually

---

## Philosophy: Why This Workflow?

This workflow is designed for **how teams actually work**:

1. **Features, not products**: Daily work is feature-level, not product-level
2. **Meetings produce artifacts**: Planning meetings → transcripts → specs
3. **Decomposition evolves**: Story breakdown improves with team learning
4. **Conversation matters**: Nuance and context from discussions are valuable
5. **Documentation enables quality**: Good specs prevent issues before coding
6. **Industry tools**: Atlassian is the standard in most organizations
7. **Automation is adaptable**: Dev workflow in place but isn't required

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
