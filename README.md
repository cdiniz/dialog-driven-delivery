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

Ask Claude to initialize D3 — the **d3:init** skill will walk you through it:

```
"set up D3 in this repo"
```

This walks you through choosing a storage backend (local markdown, Atlassian, Linear, or custom) and generates `d3.config.md` in your project root. You can also create `d3.config.md` manually — see [`config-samples/`](config-samples/) for ready-made examples.

### 3. Use D3 Skills

D3 is delivered as a set of Claude Code **skills** — they trigger from natural intent rather than slash commands. Just describe what you want to do.

| Skill | Purpose | Trigger examples |
|---|---|---|
| `d3:init` | Generate `d3.config.md` and copy default templates | "set up D3", "configure D3 storage" |
| `d3:create` | Create any D3 artifact — specs, ADRs, stories, transcripts | "turn this transcript into a spec", "document this ADR" |
| `d3:refine` | Update any existing artifact with new information | "update the spec with these notes", "resolve the open questions" |
| `d3:decompose` | Break a feature spec into INVEST-compliant user stories | "decompose this spec", "break this feature into stories" |
| `d3:align-spec` | Compare specification against codebase to detect drift | "does the spec still match the code", "audit drift" |
| `d3:distill` | Clean a raw transcript and split it by topic | "clean this transcript", "split this meeting by topic" |

Skills can be used independently or combined in whatever order fits your team's process. Here's one possible flow:

```
Cross-functional Meeting/Discussion
        |
d3:distill (optional, for multi-topic meetings) → per-topic cleaned transcripts
        |
d3:create (transcript) → Structured Transcript artifact
        |
d3:create (spec) → Specification with Product & Technical Specs
(fills what's known, leaves rest empty)
        |
[Progressive Refinement as information becomes available]
        |
d3:refine (paste any new information)
        |
Updated Artifact (spec)
        |
[Continue refining until ready]
        |
d3:decompose (discuss or paste transcript)
        |
User Stories (with acceptance criteria)
        |
[Implementation using your team's workflow]
        |
d3:align-spec (after development) → drift report spec vs code
```

---

## Methodology

D3 is grounded in [three principles](https://dialogdrivendelivery.com/) observed across real engagements:

1. **Cross-functional dialogue is the source** — Product, engineering, and design conversations create context that documentation alone cannot. Capture the dialogue, not just the outcome.
2. **Context engineering is the core skill** — AI follows context. The richer and more structured that context, the better the output. Structuring specifications and curating decisions determines AI effectiveness.
3. **Human accountability is non-negotiable** — AI drafts. Humans review. Every specification, every story, every decision passes through human judgment.

This tooling applies those principles through a concrete workflow:

- **Feature-centric**: Specifications at feature level, not task level
- **Transcript-first**: Skills accept meeting transcripts as primary input
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

Skills read the matching row and follow the instructions. This makes D3 work with any storage backend without code changes — just update the table.

### Quiet Mode

By default, D3 skills are conversational — they ask clarifying questions, confirm titles, and present proposed changes before applying them. This is the recommended mode for teams.

For automated pipelines or scripted workflows, enable quiet mode to suppress all prompts:

```markdown
### Settings
- Quiet Mode: true
```

In quiet mode:
- Input must be passed directly in the prompt (transcript text, spec name, etc.)
- Titles are inferred automatically without confirmation
- Changes are applied immediately without a review step
- Uncertainties are marked inline rather than surfaced interactively

### Brain Source (optional)

If your team maintains a separate knowledge repository ("team brain" / [llm-wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)) where meeting transcripts, slack threads, and other raw context get ingested into a navigable wiki, D3 can pull context directly from it:

```markdown
### Settings
- Brain Source: ../team-brain
```

When Brain Source is set, the **`d3:brain-pull`** skill reads the brain's entry-point index (`index.md` at the root or under `wiki/`), matches entries to the topic using LLM judgment (synonyms, rephrasings, hub pages followed), confirms the selection with you, then reads the matched files. The content is then available to any skill you invoke next — typically `d3:create` or `d3:refine`.

Example prompts:

- *"Create a product spec for catalog-browse, pull from the team brain."* — triggers `d3:brain-pull` then `d3:create`.
- *"Refine this spec using the brain."* — triggers `d3:brain-pull` (topic defaults to the spec's subject) then `d3:refine`.
- *"Look up checkout mechanics in the brain."* — standalone brain read.

D3 only reads from the brain — it never writes to it. The brain is decoupled from D3's layout: D3 needs only an index file whose entries are topic-bearing titles with links to markdown files. Everything else (folder structure, section names, ingest tooling) is the brain repo's concern.

### Template Customisation

D3 ships default templates inside the `init` skill's `references/` directory. They're copied into your project at `.d3/templates/` when you run `d3:init`. Only customise if you need domain-specific sections, compliance requirements, or team conventions.

**Default templates included:**
- Feature Product Spec (5 sections)
- Feature Technical Spec (8 sections)
- User Story (Given-When-Then acceptance criteria)
- Meeting Transcript (summary, decisions, action items, open questions)
- ADR (MADR v4 format)

**To customise:**

1. Copy default templates to your repo from `d3/skills/init/references/`
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

Skills ask for meeting transcripts (preferred input), work conversationally if none available, propose options with pros/cons, and confirm before creating artefacts.

---

## Repository Structure

```
dialog-driven-delivery/
├── d3/                              # Core plugin
│   └── skills/
│       ├── init/                    # Bootstrap d3.config.md; bundles default templates
│       ├── create/                  # Draft new artifacts
│       ├── refine/                  # Update existing artifacts
│       ├── decompose/               # Break specs into INVEST stories
│       ├── align-spec/              # Detect spec/code drift
│       ├── distill/                 # Clean and split transcripts
│       └── uncertainty-markers/     # Uncertainty marking standards
├── config-samples/                  # Example configurations
│   ├── d3.config.markdown.md        # Local markdown storage (default)
│   └── d3.config.atlassian.md       # Confluence + Jira storage
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

All skills work conversationally — select "Describe conversationally" and answer the skill's questions.

### "Can I use this with Confluence/Jira/Notion/Linear?"

Yes. Update the Storage table in `d3.config.md` with the location and instructions for your tools. If an MCP server is available for the tool (e.g. `mcp__atlassian`), reference it in the Instructions column — the D3 skills read that column literally and use whatever tool you name.

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
