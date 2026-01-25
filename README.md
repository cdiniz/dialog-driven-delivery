# Dialog Driven Delivery (D3)

A pragmatic, streamlined methodology for building software products through **conversational, transcript-first** documentation and development. Designed for real-world teams where features are defined through meetings, refined through discussion, and implemented incrementally.

**Tool-Agnostic Architecture:** Works with any specification storage (Confluence, Notion, Markdown) and work tracking system (Jira, Linear, GitHub). Uses pluggable providers for maximum flexibility.

---

## Quick Start

### Complete Feature Development Flow

```bash
# 1. Planning Phase
/d3:create-spec                        # Create feature spec
/d3:refine-spec PAGE-ID                # Refine based on discussions

# 2. Decomposition Phase
/d3:decompose PAGE-ID                  # Break into user stories

# 3. Implementation Phase (your choice of development method)
# Options:
# - Use your team's existing workflow
# - Use superpowers skills (optional, for structured AI-assisted development):
#   - brainstorming, writing-plans, test-driven-development, etc.
# - Mix and match approaches as needed

# 4. Merge and repeat for next story
```

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
9. **Tool-Agnostic**: Provider-based architecture works with any tools
10. **Skills-Based Architecture**: Commands invoke detailed skills for automatic activation and progressive disclosure

---

## Prerequisites

### Required
- **Claude Code** installed and configured
- **Git** for version control

### Provider-Specific (choose one or more)

**Default Setup (Atlassian):**
- **Confluence** for feature specifications
- **Jira** for user stories and tracking
- **Atlassian MCP Server** configured for Claude Code

**Alternative Setups:**
- **Notion + Linear:** Notion MCP Server + Linear MCP Server
- **Markdown + GitHub:** GitHub MCP Server (specs in files, stories in issues)
- **Mix & Match:** Any combination of spec and story providers

See `d3-config-sample.md` for configuration examples.

---

## Installation

### As Claude Code Plugins (Recommended)

```bash
# Install the core D3 plugin
claude plugin install d3 --plugin-dir ./d3

# Install the Atlassian provider (if using Confluence + Jira)
claude plugin install d3-atlassian --plugin-dir ./d3-atlassian
```

For production use, install from a marketplace (see [Plugin Marketplaces](#plugin-marketplaces) below).

### Local Development

Test the plugins locally:

```bash
# Test both plugins together
claude --plugin-dir ./d3 --plugin-dir ./d3-atlassian
```

---

## Core Workflow

### Simplified Development Flow

```
Any Initial Meeting/Discussion
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
[Implementation - Use Your Preferred Development Method]
Options:
• Your team's existing workflow and practices
• Superpowers skills (optional AI-assisted development):
  - brainstorming, writing-plans, test-driven-development,
    systematic-debugging, code-reviewer, verification-before-completion
• Any combination that works for your team
        ↓
Commit, Create PR, and Merge
```

**Tool Selection:** Configure providers in `.claude/d3-config.md` to use your preferred tools:
- **Specifications:** Confluence, Notion, Markdown files, etc.
- **Stories:** Jira, Linear, GitHub Issues, etc.
- **Mix & Match:** Use different tools for specs and stories!

---

## Skills-Based Architecture

D3 uses a **skills-based architecture** for automatic activation and progressive disclosure:

- **Commands** (`/create-spec`, `/refine-spec`, `/decompose`): Thin triggers that invoke skills
- **Skills** (`.claude/skills/*/SKILL.md`): Detailed workflows with full implementation guidance
- **Benefits**:
  - Skills activate automatically based on context (not just explicit commands)
  - Progressive disclosure reduces context usage
  - Shared resources (templates, uncertainty markers) referenced, not duplicated

---

## Commands

### Available Commands

| Command | Phase | Purpose |
|---------|-------|---------|
| `/d3:create-spec` | Planning | Create feature specification |
| `/d3:refine-spec` | Planning | Update specifications |
| `/d3:decompose` | Planning | Break into user stories |

**For Implementation:** Use superpowers skills for development workflow

### When to Use Each Command

**Planning & Requirements**
- **Just starting a feature?** → `/d3:create-spec`
- **Got new information?** → `/d3:refine-spec`
- **Ready for implementation?** → `/d3:decompose`

**Development & Delivery**

After decomposition, implement using your preferred method:
- **Your existing workflow** → Continue with your team's practices
- **Want AI assistance?** → Optionally use superpowers skills:
  - `brainstorming` (design approach)
  - `writing-plans` (create implementation plan)
  - `test-driven-development` (TDD workflow)
  - `systematic-debugging` (debug issues)
  - `code-reviewer` (review work)
  - `verification-before-completion` (verify before commit)

---

## Detailed Command Reference

### 1. `/d3:create-spec`

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

Agent: ✅ Feature specification created successfully!

       📋 Product Spec: 70% complete (requirements clear, metrics missing)
       🔧 Technical Spec: 10% complete (only basic approach mentioned)

       Missing information can be added later using /d3:refine-spec [PAGE-ID]
```

**Output**:
- Specification with both Product AND Technical spec sections
- Fills only what's available from input
- Empty sections clearly marked
- Shows coverage percentage
- Clear next steps

---

### 2. `/d3:refine-spec PAGE-ID`

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

### 3. `/d3:decompose PAGE-ID`

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
       Product Spec: ✅ 85% complete
       Technical Spec: ✅ 75% complete

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

       ✅ Created Epic PROJ-41: Advanced Search with Filters
          https://yourproject.example.com/browse/PROJ-41

       Now creating user stories under this Epic...

       ✅ Created PROJ-42: Basic text search (under Epic PROJ-41)
       ✅ Created PROJ-43: Add status filter (under Epic PROJ-41)
       ...

       Creating dependency links between stories...

       ✅ Linked PROJ-42 blocks PROJ-43
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

After creating your user stories with `/d3:decompose`, implement them using your preferred development method.

**Implementation Options:**

**Option 1: Your Team's Existing Workflow**
- Use your established development practices
- D3 provides the specs and stories, you handle implementation however works best

**Option 2: Superpowers Skills (Optional AI-Assisted Development)**

If you want structured AI assistance during implementation, superpowers provides specialized skills:

- **`brainstorming`**: Design implementation approach before coding
- **`writing-plans`**: Create detailed implementation plans
- **`test-driven-development`**: TDD workflow for feature implementation
- **`systematic-debugging`**: Debug issues systematically
- **`code-reviewer`**: Review completed work against plan and standards
- **`verification-before-completion`**: Verify tests and quality before committing

**Example Workflow with Superpowers (Optional):**
```
1. Pick a story from your project tracker
2. Use brainstorming skill to design approach (optional)
3. Use writing-plans skill to create implementation plan (optional)
4. Implement using your preferred method
5. Use code-reviewer skill to review work (optional)
6. Use verification-before-completion skill before committing (optional)
7. Create PR and merge
```

**Option 3: Mix and Match**
- Use superpowers for complex features
- Use your existing workflow for straightforward tasks
- Adapt based on team needs and preferences

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

### Specification Storage

**Both Product and Technical specifications** are stored in your configured specification provider:

**Page Structure:**
```markdown
# Feature: [Feature Name]

## 📋 Product Specification
[Complete product/feature spec]

## 🔧 Technical Specification
[Complete technical implementation spec]
```

**Benefits:**
- **Single Source of Truth**: One page contains BOTH specs
- **Built-in Collaboration**: Product and engineering teams collaborate in one place
- **No Context Switching**: View specs, track work, all integrated
- **Always Accessible**: Web-based access
- **Version Control**: Platform tracks changes
- **Unified Discussions**: Comments on both specs stay together
- **Native Integration**: Specs link to stories, stories link back
- **Rich Content**: Support for images, diagrams, tables

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

Use the `uncertainty-markers` skill for complete documentation and examples.

---

## Provider Architecture

D3 uses a **provider-based architecture** to work with any tools:

### How It Works

```
D3 Core Skills (Tool-Agnostic)
    ├── create-spec  → Uses Spec Provider
    ├── refine-spec  → Uses Spec Provider
    └── decompose    → Uses Spec Provider + Story Provider

Spec Providers (Pluggable)
    ├── atlassian-spec (Confluence)
    ├── notion-spec (Notion databases) [Future]
    └── markdown-spec (Local files) [Future]

Story Providers (Pluggable)
    ├── atlassian-story (Jira)
    ├── linear-story (Linear) [Future]
    └── github-story (GitHub Issues) [Future]
```

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

### Configuration

Edit `.claude/d3-config.md`:

```markdown
### Spec Provider
**Skill:** atlassian-spec-provider
**Configuration:**
- Cloud ID: your-cloud-id
- Default Location: BOOT
- spaceId: 1234567
- Default parent page: https://yoursite.atlassian.net/wiki/spaces/PROJ/pages/...

### Story Provider
**Skill:** atlassian-story-provider
**Configuration:**
- Cloud ID: your-cloud-id
- Default Project: BOOT
```

**Default Behavior:** If config file doesn't exist, D3 uses Atlassian providers with settings from `CLAUDE.md`.

### Creating Custom Providers

To create a provider for a different tool (Notion, Linear, GitHub, etc.):

1. **Review existing provider**: See `.claude/skills/atlassian-spec-provider/SKILL.md` or `.claude/skills/atlassian-story-provider/SKILL.md`
2. **Create provider skill**: Implement operations in `.claude/skills/your-provider-name/SKILL.md`
3. **Map operations to your tool's MCP/API**: Each operation should call the appropriate tool
4. **Configure**: Update `.claude/d3-config.md` to use your provider skill
5. **Use D3 commands**: They work automatically with any provider!

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
├─ /d3:create-spec (paste meeting transcript)
└─ Specification created

Tuesday-Wednesday: Refinement
├─ /d3:refine-spec (add technical details)
└─ Specifications complete

Thursday: Story Decomposition
├─ /d3:decompose
└─ User stories created

Next Sprint: Implementation (your development method)
├─ Implement using your team's workflow
├─ OR optionally use superpowers skills for AI assistance
├─ (brainstorming, writing-plans, test-driven-development, etc.)
└─ Commit, PR, and merge
```

---

## Success Metrics

### Planning Phase
- ✅ Specs completed before coding
- ✅ All open questions resolved
- ✅ Stories have clear acceptance criteria
- ✅ Dependencies mapped in work tracker

### Implementation Phase
- ✅ All tests passing before PR
- ✅ No skipped or disabled tests
- ✅ All ACs covered by tests
- ✅ Code follows architecture guidelines
- ✅ PR feedback addressed systematically

---

## Troubleshooting

### "I don't have meeting transcripts"

No problem! All commands work conversationally:
- Select "Option B: Describe conversationally" or "Option C"
- Answer the agent's questions
- Same quality output, just more interactive

### "My implementation is different from the spec"

Use `/d3:refine-spec` to update the specification with learnings from implementation.

### "My stories need to change during development"

That's expected and normal! You can:
- Update stories directly in your story provider using native editing
- Split stories using your tool's split/clone features
- Create new stories and link them to the Epic
- Update dependencies using your tool's link functionality
- Use `/d3:refine-spec` to update the specification if requirements changed

### "Can I use this with other tools?"

Yes! D3 is tool-agnostic through its provider architecture:
- Configure providers in `.claude/d3-config.md`
- Use Confluence + Jira (default), Notion + Linear, Markdown + GitHub, or any combination
- Create custom providers for your specific tools
- See "Creating Custom Providers" section above

### "How do I implement the stories?"

After decomposition, implement using your preferred development method:
- Use your team's existing workflow and practices
- Optionally use superpowers skills for AI-assisted development
- Mix and match approaches based on your needs

D3 focuses on planning and decomposition - implementation is flexible.

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

### 5. Conversational & Engaging

- Commands feel like collaboration, not automation
- Agent asks questions and proposes options
- Shows understanding before taking action
- Confirms before creating artifacts

### 6. Flexible & Modular

- Use core workflow for documentation and decomposition
- Optionally add dev automation
- Refine specifications and stories as needed

### 7. Quality Through Process

- Complete acceptance criteria from the start
- Technical specs follow codebase patterns
- Smart section selection (only relevant sections)
- Maps ACs to technical implementation

### 8. Team-Friendly

- Async-friendly (paste recorded meeting transcripts)
- Supports iteration and learning
- Clear traceability (spec → stories → tasks)
- Preserves history of changes

---

## Plugin Architecture

D3 is distributed as **Claude Code plugins** for easy installation and updates.

### Plugin Structure

- **`d3`** - Core plugin containing main skills and commands
- **`d3-atlassian`** - Atlassian provider (Confluence + Jira)
- **Future:** `d3-notion`, `d3-linear`, `d3-github`, etc.

### Repository Structure

```
dialog-driven-delivery/
├── README.md                  # This file - main documentation
├── d3/                        # Core D3 plugin
│   ├── .claude-plugin/
│   │   └── plugin.json       # Plugin manifest
│   ├── commands/             # Thin command triggers
│   ├── skills/               # Main workflow skills
│   ├── templates/            # Spec templates
│   ├── d3-config-sample.md   # Configuration example
│   └── README.md             # Plugin-specific docs
├── d3-atlassian/             # Atlassian provider plugin
│   ├── .claude-plugin/
│   │   └── plugin.json       # Plugin manifest
│   ├── skills/               # Provider skills
│   └── README.md             # Provider docs
└── .claude/                  # Original structure (deprecated)
```

### Local Testing

Test plugins locally before publishing:

```bash
# Test both plugins together
claude --plugin-dir ./d3 --plugin-dir ./d3-atlassian

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

## Project Configuration

Add to your project's `CLAUDE.md`:

```markdown
### Atlassian Configuration

- **Cloud ID**: your-cloud-id
- **Jira Project Code**: PROJ
- **Confluence Space Code**: PROJ

### Development Commands

- `pnpm test:all` - Run all tests
- `pnpm test:web` - Run frontend tests
- `pnpm test:api` - Run backend tests
```

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

This methodology is open for use and adaptation. Modify to fit your team's needs.

---

## Support

For issues, questions, or contributions:
- Review individual skill files for detailed documentation
- Each skill has extensive examples and guidelines
- Skills are designed to be self-explanatory
- Agent prompts guide you through the process

---

*Built for real teams, refined through real projects.* 🚀
