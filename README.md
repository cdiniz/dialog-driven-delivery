# Dialog Driven Delivery (D3) — Tooling

[D3](https://dialogdrivendelivery.com/) is a methodology for AI-enabled software delivery, built from real engagements by practitioners at Equal Experts. It helps teams — not just individuals — work effectively with AI by focusing on collaboration and context, not tooling.

**This repository provides tooling that implements D3's workflow across multiple AI coding platforms.** It turns the methodology's principles into a concrete, repeatable process: capture conversations, create structured specifications, and decompose features into implementable stories.

Works with your existing tools. Built-in providers for Atlassian (Confluence + Jira) and Markdown (local files + git). Expandable to any specification storage or work tracking system through pluggable provider skills.

### Supported Platforms

| Platform | Status | Installation |
|----------|--------|-------------|
| **Claude Code** | Full support | Plugin marketplace |
| **OpenAI Codex** | Full support | Install script |
| **GitHub Copilot** | Full support | Install script |
| **Cursor** | Full support | Install script |

---

## Quick Start

### 1. Install D3

**Claude Code** (plugin marketplace):

```bash
claude plugin marketplace add cdiniz/dialog-driven-delivery
claude plugin install d3@d3-marketplace
claude plugin install d3-markdown@d3-marketplace   # or d3-atlassian
```

**Codex, Copilot, or Cursor** (install script):

```bash
curl -sSL https://raw.githubusercontent.com/cdiniz/dialog-driven-delivery/main/install.sh | bash -s -- <platform>
```

Where `<platform>` is `codex`, `copilot`, or `cursor`.

Or copy files manually from `dist/<platform>/` into your project.

### 2. Configure Your Provider

Edit `d3.config.md` in your project root to configure providers. This file is the same across all platforms.

See the [Configuration](#configuration) section for provider setup.

### 3. Use D3 Commands

Command invocation varies by platform:

| Command | Claude Code | Codex | Copilot | Cursor |
|---------|------------|-------|---------|--------|
| Create spec | `/d3:create-spec` | `$d3-create-spec` | `@d3-create-spec` | `@d3-create-spec` |
| Refine spec | `/d3:refine-spec` | `$d3-refine-spec` | `@d3-refine-spec` | `@d3-refine-spec` |
| Decompose | `/d3:decompose` | `$d3-decompose` | `@d3-decompose` | `@d3-decompose` |
| Capture transcript | `/d3:capture-transcript` | `$d3-capture-transcript` | `@d3-capture-transcript` | `@d3-capture-transcript` |
| Create ADR | `/d3:create-adr` | `$d3-create-adr` | `@d3-create-adr` | `@d3-create-adr` |

### Complete Feature Development Flow

```
Capture Phase (optional)  →  create-spec  →  refine-spec (iterative)  →  decompose
     ↓                           ↓                  ↓                       ↓
Meeting transcript      Feature specification   Updated spec       Epic + User Stories
                        (Product + Technical)   with new info      with acceptance criteria
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

## Installation

### Claude Code (Plugin Marketplace)

```bash
# Add the D3 marketplace
claude plugin marketplace add cdiniz/dialog-driven-delivery

# Install core + provider
claude plugin install d3@d3-marketplace
claude plugin install d3-markdown@d3-marketplace    # Local files + git
claude plugin install d3-atlassian@d3-marketplace   # Confluence + Jira
```

### Codex

```bash
curl -sSL https://raw.githubusercontent.com/cdiniz/dialog-driven-delivery/main/install.sh | bash -s -- codex
```

This places files in `.agents/skills/` and creates `AGENTS.md` with default configuration.

### GitHub Copilot

```bash
curl -sSL https://raw.githubusercontent.com/cdiniz/dialog-driven-delivery/main/install.sh | bash -s -- copilot
```

This places agent files in `.github/agents/` and creates `.github/copilot-instructions.md` with default configuration.

### Cursor

```bash
curl -sSL https://raw.githubusercontent.com/cdiniz/dialog-driven-delivery/main/install.sh | bash -s -- cursor
```

This places rule files in `.cursor/rules/` with default configuration.

### Manual Installation

Alternatively, copy files directly from the `dist/` directory:

```bash
# Codex
cp -r dist/codex/.agents your-project/
cp dist/codex/AGENTS.md your-project/

# Copilot
cp -r dist/copilot/.github your-project/

# Cursor
cp -r dist/cursor/.cursor your-project/
```

### Prerequisites

**Required:**
- **Git** for version control
- One of the supported AI coding platforms installed and configured

**Provider-specific (choose one or more):**

| Provider | Requirements | Best for |
|----------|-------------|----------|
| **Markdown** | No external services | Lightweight, git-native teams |
| **Atlassian** | Confluence + Jira + Atlassian MCP Server | Enterprise teams |

---

## Configuration

D3 configuration tells the agent which providers to use and how to connect to your tools. Edit `d3.config.md` in your project root.

### Markdown Provider (Lightweight)

```markdown
## D3 Configuration

### Spec Provider
**Skill:** markdown-spec-provider
**Configuration:**
- Specs Directory: ./specs

### Story Provider
**Skill:** markdown-story-provider
**Configuration:**
- Stories Directory: ./stories

### Transcript Provider
**Skill:** markdown-transcript-provider
**Configuration:**
- Transcripts Directory: ./transcripts
```

### Atlassian Provider (Enterprise)

```markdown
## D3 Configuration

### Spec Provider
**Skill:** atlassian-spec-provider
**Configuration:**
- Cloud ID: your-cloud-id
- Default Location: PROJ
- spaceId: 1234567
- Default parent page: https://yoursite.atlassian.net/wiki/spaces/PROJ/pages/123456

### Story Provider
**Skill:** atlassian-story-provider
**Configuration:**
- Cloud ID: your-cloud-id
- Default Project: PROJ

### Transcript Provider
**Skill:** atlassian-transcript-provider
**Configuration:**
- Cloud ID: your-cloud-id
- Default Location: PROJ
- spaceId: 1234567
- Default parent page: https://yoursite.atlassian.net/wiki/spaces/PROJ/pages/123456/Transcripts
```

### Spec Modes

D3 supports two modes for creating and storing specifications, controlled entirely by your config file.

**Combined mode** (default) — a single spec document contains both the Product and Technical specifications. Use this when your team works in one place and doesn't need to separate the two audiences.

```markdown
### Spec Provider
**Skill:** markdown-spec-provider
**Configuration:**
- Specs Directory: ./specs
```

`create-spec` produces one document. `refine-spec` updates it. `decompose` reads it.

---

**Separated mode** — Product and Technical specifications are created as two independent documents, each using its own provider. Use this when product and engineering teams work in different tools, or when you want to control access separately.

```markdown
### Product Spec Provider
**Skill:** atlassian-spec-provider
**Configuration:**
- Cloud ID: your-cloud-id
- Default Location: PROJ
- spaceId: 1234567
- Default parent page: https://yoursite.atlassian.net/wiki/spaces/PROJ/pages/123456

### Tech Spec Provider
**Skill:** markdown-spec-provider
**Configuration:**
- Specs Directory: ./specs
```

`create-spec` produces two documents — one per provider. `refine-spec` detects whether new information affects the product spec, the tech spec, or both, and updates only what's needed. `decompose` always fetches both for full context.

Providers can be mixed freely — product specs in Confluence, tech specs in local markdown, or any other combination.

---

### Quiet Mode (Optional)

By default, D3 commands are conversational — they ask clarifying questions, confirm titles, and present proposed changes before applying them. This is the recommended mode for teams.

For automated pipelines or scripted workflows, enable quiet mode to suppress all prompts:

```markdown
### Settings
- Quiet Mode: true
```

In quiet mode:
- Input must be passed directly in the command (transcript text, spec name, etc.)
- Location selection is skipped — the provider's `Default Location` is used
- Titles are inferred automatically without confirmation
- Changes are applied immediately without a review step
- Uncertainties are marked inline rather than surfaced interactively

---

### ADR Provider (Optional)

By default, ADRs use the Spec Provider. To store ADRs separately:

```markdown
### ADR Provider
**Skill:** markdown-spec-provider
**Configuration:**
- Specs Directory: ./docs/adrs
```

### Template Customisation (Optional)

D3 includes default templates via the `d3-templates` skill that work out of the box. Only customise if you need domain-specific sections, compliance requirements, or team conventions.

**Default templates included:**
- Feature Product Spec (5 sections)
- Feature Technical Spec (8 sections)
- User Story (Given-When-Then acceptance criteria)
- Meeting Transcript (summary, decisions, action items, open questions)
- ADR (MADR v4 format)

**To customise:**

1. Copy default templates to your repo:
   ```bash
   mkdir -p .d3/templates
   # Copy from the d3-templates skill references directory
   ```

2. Configure custom paths in your config file:
   ```markdown
   ### Templates
     - Feature Product Spec: ./.d3/templates/feature-product-spec.md
     - Feature Technical Spec: ./.d3/templates/feature-tech-spec.md
     - User Story: ./.d3/templates/user-story.md
     - Meeting Transcript: ./.d3/templates/meeting-transcript.md
     - ADR: ./.d3/templates/adr.md
   ```

---

## Commands

| Command | Phase | Purpose |
|---------|-------|---------|
| `create-spec` | Planning | Create feature specification from conversation, transcript, or document |
| `create-adr` | Planning | Record architectural decisions as immutable ADRs (MADR v4) |
| `refine-spec` | Planning | Update specifications with new information |
| `decompose` | Planning | Break feature into INVEST-compliant user stories |
| `capture-transcript` | Capture | Capture and structure a meeting transcript |

### When to Use Each Command

- **Had a meeting?** → `capture-transcript`
- **Starting a feature?** → `create-spec`
- **Made an architectural decision?** → `create-adr`
- **Got new information?** → `refine-spec`
- **Ready to implement?** → `decompose`

After decomposition, implement using your team's existing workflow.

### Workflow

```
Cross-functional Meeting/Discussion
        ↓
capture-transcript (optional — capture and structure the meeting)
        ↓
create-spec (paste transcript/document/description)
        ↓
Specification with BOTH Product & Technical Specs
(fills what's known, leaves rest empty)
        ↓
[Progressive Refinement as information becomes available]
        ↓
refine-spec (paste any new information)
        ↓
Updated Specification (product, technical, or both)
        ↓
[Continue refining until ready]
        ↓
decompose (specify project, paste transcript or discuss)
        ↓
Epic + User Stories (linked to specification with dependencies)
        ↓
[Implementation using your team's workflow]
```

### Architectural Decision Workflow

```
Architectural discussion (meeting/transcript)
        ↓
create-adr (paste transcript or describe decision)
        ↓
ADR created (Context, Decision, Alternatives, Consequences)
        ↓
refine-spec (incorporate ADR into spec)
        ↓
Spec's "Architectural Context > Relevant ADRs" section updated
```

ADRs are immutable records. If a decision changes, create a new ADR that supersedes the old one.

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

### Provider Architecture

```
D3 Core Commands (Tool-Agnostic)
    ├── capture-transcript → Uses Transcript Provider
    ├── create-spec        → Uses Spec Provider
    ├── create-adr         → Uses ADR Provider (falls back to Spec Provider)
    ├── refine-spec        → Uses Spec Provider
    └── decompose          → Uses Spec Provider + Story Provider

Providers (Pluggable)
    ├── Atlassian (Confluence + Jira)   — built-in
    ├── Markdown (local files + git)    — built-in
    └── Custom (Notion, Linear, etc.)   — expandable
```

### Creating Custom Providers

1. Review an existing provider (e.g. `d3-markdown/skills/markdown-spec-provider/SKILL.md`)
2. Implement the provider operations for your tool
3. Configure your config file to reference the new provider
4. D3 commands work automatically with any provider

**Provider operations:**
- **Spec**: `list_locations`, `create_spec`, `get_spec`, `update_spec`, `search_specs`
- **Story**: `list_projects`, `get_issue_types`, `create_epic`, `create_story`, `link_issues`
- **Transcript**: `list_locations`, `store_transcript`, `get_transcript`, `list_transcripts`, `search_transcripts`

---

## Repository Structure

The Claude Code plugin files (`d3/`, `d3-markdown/`, `d3-atlassian/`) are the source of truth. They use platform-agnostic natural language (e.g. "the read tool") and reference `d3.config.md` directly. The generator copies these to other platforms, transforming frontmatter and directory structure. Each platform gets a `d3-platform` reference that maps generic tool terms to platform-specific values.

```
dialog-driven-delivery/
├── d3/                              # Core plugin — commands, skills, templates
├── d3-markdown/                     # Markdown provider plugin (local files + git)
├── d3-atlassian/                    # Atlassian provider plugin (Confluence + Jira)
├── d3.platform.yaml                 # Platform tool/config mappings
├── metadata/                        # Plugin metadata (d3.yaml, d3-markdown.yaml, d3-atlassian.yaml)
├── config/
│   └── example-config.md            # Default provider configuration
├── generate.py                      # Generator — copies source to other platforms
├── install.sh                       # Install script for non-Claude platforms
└── dist/                            # Generated — other platforms
    ├── codex/                       # .agents/skills/ + d3.config.md
    ├── copilot/                     # .github/prompts/ + .github/agents/ + d3.config.md
    └── cursor/                      # .cursor/rules/ + d3.config.md
```

### How It Works

Source files use natural language for tool references and configuration. The generator copies files to each platform's directory structure, transforms frontmatter as needed, and generates a `d3-platform` reference from `d3.platform.yaml` that maps generic terms to platform-specific values.

**Platform reference mappings (from `d3.platform.yaml`):**

| Reference | Claude Code | Codex | Copilot | Cursor |
|----------|------------|-------|---------|--------|
| "the read tool" | `Read` | `read` | `read` | `read` |
| "the write tool" | `Write` | `write` | `edit` | `edit` |
| "the search tool" | `Grep` | `search` | `search` | `search` |
| "the glob tool" | `Glob` | `glob` | `search` | `search` |
| "the shell tool" | `Bash` | `execute` | `execute` | `execute` |
| skill invocation | `Skill(skill=...)` | `$name args` | `@name args` | `@name args` |

---

## Development

### Generator

The `generate.py` script copies source files to each platform's directory structure.

```bash
# Generate for a specific platform
python generate.py --platform claude    # Output: d3/ (metadata + platform ref only)
python generate.py --platform codex     # Output: dist/codex/
python generate.py --platform copilot   # Output: dist/copilot/
python generate.py --platform cursor    # Output: dist/cursor/

# Generate all platforms
python generate.py --all
```

For Claude, the generator only produces metadata files (`plugin.json`, `marketplace.json`) and the `d3-platform` reference. Other platforms get the full copy to `dist/<platform>/`.

**Requirements:** Python 3 with PyYAML (`pip install pyyaml`).

### Pre-commit Hook

A pre-commit hook automatically regenerates platform files when source files change.

```bash
# Setup (once after cloning)
pip install pre-commit
pre-commit install
```

The hook runs `python generate.py --all` when you commit changes to `d3/`, `d3-markdown/`, `d3-atlassian/`, `d3.platform.yaml`, `metadata/`, or `config/`.

### Install Script

The `install.sh` script downloads pre-generated files from this repository and places them in the correct directories for each platform.

```bash
# Usage
curl -sSL https://raw.githubusercontent.com/cdiniz/dialog-driven-delivery/main/install.sh | bash -s -- <platform>

# What it does per platform:
# codex    → .agents/skills/*  + AGENTS.md
# copilot  → .github/agents/*.agent.md + .github/copilot-instructions.md
# cursor   → .cursor/rules/*
```

The script creates config files with sensible defaults if they don't already exist.

### Local Testing

**Claude Code** (using plugin directories):

```bash
# Test in another project using local plugins
cd /path/to/test-project
claude --plugin-dir /path/to/dialog-driven-delivery/d3 \
       --plugin-dir /path/to/dialog-driven-delivery/d3-markdown
```

**Other platforms** (copy to test project):

```bash
# Generate platform output
python generate.py --platform codex

# Copy to another project
cp -r dist/codex/.agents /path/to/your-project/
cp dist/codex/AGENTS.md /path/to/your-project/
```

### Making Changes

1. Edit source files in `d3/`, `d3-markdown/`, or `d3-atlassian/`
2. Commit — the pre-commit hook regenerates `dist/` automatically
3. Test with your target platform

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

### "Can I use this with other tools?"

Yes. D3 is tool-agnostic through its provider architecture. Use Confluence + Jira, Markdown + Git, or create custom providers for Notion, Linear, GitHub Issues, etc.

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
