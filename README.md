# Dialog Driven Delivery (D3) — Tooling

[D3](https://dialogdrivendelivery.com/) is a methodology for AI-enabled software delivery, built from real engagements by practitioners at Equal Experts. It helps teams — not just individuals — work effectively with AI by focusing on collaboration and context, not tooling.

**This repository provides tooling that implements D3's workflow.** It turns the methodology's principles into a concrete, repeatable process: capture conversations, create structured specifications, and decompose features into implementable stories.

Works with your existing tools. A simple configuration table tells D3 where and how to store each artifact type — local markdown files, Confluence pages, Jira issues, or any combination.

---

## Quick Start

### 1. Install D3

**Claude Code** (plugin marketplace):

```bash
claude plugin marketplace add cdiniz/dialog-driven-delivery
claude plugin install d3@d3-marketplace
```

### 2. Configure Storage

Edit `d3.config.md` in your project root. The Storage table tells D3 where to put each artifact type and how to write it:

```markdown
## D3 Configuration

### Settings
- Quiet Mode: false

### Templates
Uses default D3 templates. Override by adding paths:
- Product Spec Template: (default)
- Tech Spec Template: (default)
- User Story Template: (default)
- ADR Template: (default)
- Meeting Transcript Template: (default)

### Storage

| Artifact      | Location          | Instructions                    |
|---------------|-------------------|---------------------------------|
| Specs         | ./specs/          | Write as markdown files         |
| Stories       | ./stories/        | Write as markdown files         |
| ADRs          | ./adrs/           | Write as markdown files         |
| Transcripts   | ./transcripts/    | Write as markdown files         |
```

For Atlassian teams, the table changes to point at Confluence and Jira:

```markdown
### Storage

| Artifact      | Location                      | Instructions                                              |
|---------------|-------------------------------|-----------------------------------------------------------|
| Specs         | Confluence space PROJ         | Use mcp__atlassian tool to create pages under parent 12345 |
| Stories       | Jira project PROJ             | Use mcp__atlassian tool to create issues                   |
| ADRs          | Confluence space PROJ         | Use mcp__atlassian tool to create pages under parent 67890 |
| Transcripts   | ./transcripts/                | Write as markdown files                                    |
```

### 3. Use D3 Commands

| Command | Purpose |
|---------|---------|
| `/d3:create-spec` | Create feature specification from conversation, transcript, or document |
| `/d3:refine-spec` | Update specifications with new information |
| `/d3:decompose` | Break feature into INVEST-compliant user stories |
| `/d3:capture-transcript` | Capture and structure a meeting transcript |
| `/d3:create-adr` | Record architectural decisions as immutable ADRs (MADR v4) |
| `/d3:align-spec` | Compare specification against codebase to detect drift |

### Complete Feature Development Flow

```
Cross-functional Meeting/Discussion
        |
capture-transcript (optional -- capture and structure the meeting)
        |
create-spec (paste transcript/document/description)
        |
Specification with BOTH Product & Technical Specs
(fills what's known, leaves rest empty)
        |
[Progressive Refinement as information becomes available]
        |
refine-spec (paste any new information)
        |
Updated Specification (product, technical, or both)
        |
[Continue refining until ready]
        |
decompose (discuss or paste transcript)
        |
User Stories (with acceptance criteria)
        |
[Implementation using your team's workflow]
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

---

## Configuration

### Storage Table

The Storage table in `d3.config.md` has three columns:

| Column | Purpose |
|--------|---------|
| **Artifact** | The type of artifact (Specs, Stories, ADRs, Transcripts) |
| **Location** | Where to store it (a directory path, Confluence space, Jira project, etc.) |
| **Instructions** | How to write it (write as markdown, use an MCP tool, etc.) |

Commands read the matching row and follow the instructions. This makes D3 work with any storage backend without code changes — just update the table.

### Quiet Mode

By default, D3 commands are conversational — they ask clarifying questions, confirm titles, and present proposed changes before applying them. This is the recommended mode for teams.

For automated pipelines or scripted workflows, enable quiet mode to suppress all prompts:

```markdown
### Settings
- Quiet Mode: true
```

In quiet mode:
- Input must be passed directly in the command (transcript text, spec name, etc.)
- Titles are inferred automatically without confirmation
- Changes are applied immediately without a review step
- Uncertainties are marked inline rather than surfaced interactively

### Template Customisation

D3 includes default templates via the `d3-templates` skill that work out of the box. Only customise if you need domain-specific sections, compliance requirements, or team conventions.

**Default templates included:**
- Feature Product Spec (5 sections)
- Feature Technical Spec (8 sections)
- User Story (Given-When-Then acceptance criteria)
- Meeting Transcript (summary, decisions, action items, open questions)
- ADR (MADR v4 format)

**To customise:**

1. Copy default templates to your repo from `d3/skills/d3-templates/references/`
2. Configure custom paths in the Templates section of `d3.config.md`:
   ```markdown
   ### Templates
   - Product Spec Template: ./.d3/templates/feature-product-spec.md
   - Tech Spec Template: ./.d3/templates/feature-tech-spec.md
   - User Story Template: ./.d3/templates/user-story.md
   - ADR Template: ./.d3/templates/adr.md
   - Meeting Transcript Template: ./.d3/templates/meeting-transcript.md
   ```

---

## Key Features

### Uncertainty Markers

When AI generates specifications, it can hallucinate plausible-sounding details that were never discussed. D3 prevents this with explicit uncertainty markers:

- `[OPEN QUESTION: text]` — User decision needed
- `[DECISION PENDING: options]` — Valid choices exist, decision deferred
- `[ASSUMPTION: statement]` — Inference made from context, needs validation
- `[CLARIFICATION NEEDED: aspect]` — Requirement is vague

```markdown
BAD (silent hallucination):
Users authenticate via OAuth2 using Google provider

GOOD (explicit uncertainty):
Users authenticate via [OPEN QUESTION: OAuth2, password, or social login?]
```

### Pragmatic Templates

Feature specs use a **streamlined 5-section product template** and **8-section technical template**. This produces 2-3 pages instead of 5-10. Faster to write, faster to review, still captures everything that matters.

### Conversational Workflow

Commands ask for meeting transcripts (preferred input), work conversationally if none available, propose options with pros/cons, and confirm before creating artefacts.

---

## Repository Structure

```
dialog-driven-delivery/
├── d3/                              # Core plugin
│   ├── commands/                    # 6 commands (create-spec, refine-spec, decompose, etc.)
│   └── skills/
│       ├── d3-templates/            # 5 reference templates
│       └── uncertainty-markers/     # Uncertainty marking standards
├── samples/                         # Example configurations
│   ├── d3.config.markdown.md        # Local markdown storage (default)
│   └── d3.config.atlassian.md       # Confluence + Jira storage
├── metadata/
│   └── d3.yaml                      # Plugin metadata
└── tests/                           # E2E tests
```

---

## Best Practices

### For Feature Planning
1. **Record your meetings** — transcripts are the best input
2. **Be specific** — discuss concrete examples and scenarios
3. **Define boundaries** — what's in scope and out of scope

### For Story Decomposition
1. **Natural boundaries** — break at logical workflow points
2. **Independent stories** — minimise dependencies
3. **Complete ACs** — cover happy path, errors, edge cases

### For Refinement
1. **Learn and adapt** — refine based on development learnings
2. **Split when needed** — don't force large stories
3. **Update dependencies** — keep the dependency graph current

---

## Troubleshooting

### "I don't have meeting transcripts"

All commands work conversationally — select "Describe conversationally" and answer the agent's questions.

### "Can I use this with Confluence/Jira/Notion/Linear?"

Yes. Update the Storage table in `d3.config.md` with the location and instructions for your tools. If an MCP server is available for the tool (e.g. mcp__atlassian), reference it in the Instructions column.

### "How do I implement the stories?"

Use your team's existing development workflow. D3 focuses on the planning phase — turning conversations into structured context and implementable stories.

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
