# Dialog Driven Delivery (D3) — Tooling

[D3](https://dialogdrivendelivery.com/) is a methodology for AI-enabled software delivery, built from real engagements by practitioners at Equal Experts. It helps teams — not just individuals — work effectively with AI by focusing on collaboration and context, not tooling.

**This repository provides tooling that implements D3's workflow across multiple AI coding platforms.** It turns the methodology's principles into a flexible toolkit: capture conversations, create structured artifacts from templates, refine them with new information, and decompose features into implementable stories.

Works with your existing tools. Built-in adapters for Confluence and Markdown (local files + git). Expandable to any specification storage or work tracking system through pluggable adapters.

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

### 2. Configure Your Artifact Catalog

Edit `d3.config.yaml` in your project root to configure artifact types and adapters. See the [Configuration](#configuration) section for details.

### 3. Use D3 Commands

Command invocation varies by platform:

| Command | Claude Code | Codex | Copilot | Cursor |
|---------|------------|-------|---------|--------|
| Create artifact | `/d3:create` | `$d3-create` | `@d3-create` | `@d3-create` |
| Refine artifact | `/d3:refine` | `$d3-refine` | `@d3-refine` | `@d3-refine` |
| Create template | `/d3:create-template` | `$d3-create-template` | `@d3-create-template` | `@d3-create-template` |
| Decompose | `/d3:decompose` | `$d3-decompose` | `@d3-decompose` | `@d3-decompose` |

### Core Workflow

```
Input (transcript / document / conversation)
        +
Template (defines artifact structure)
        ↓
   /d3:create [artifact type]
        ↓
Artifact with uncertainty markers
(fills what's known, marks what's unknown)
        ↓
   /d3:refine (iterative, with new information)
        ↓
Mature artifact ready for use
        ↓
   /d3:decompose (for specs → user stories)
```

---

## Methodology

D3 is grounded in [three principles](https://dialogdrivendelivery.com/) observed across real engagements:

1. **Cross-functional dialogue is the source** — Product, engineering, and design conversations create context that documentation alone cannot. Capture the dialogue, not just the outcome.
2. **Context engineering is the core skill** — AI follows context. The richer and more structured that context, the better the output. Structuring specifications and curating decisions determines AI effectiveness.
3. **Human accountability is non-negotiable** — AI drafts. Humans review. Every specification, every story, every decision passes through human judgment.

This tooling applies those principles through a flexible toolkit:

- **Template-driven**: Artifacts are structured by templates — customise or create your own
- **Transcript-first**: Commands accept meeting transcripts as primary input
- **Incremental delivery**: Artifacts grow through refinement, features decompose into stories
- **Explicit over implicit**: Uncertainties are marked, not assumed — prevents AI hallucination
- **Tool-agnostic**: Adapter architecture works with whatever tools your team already uses

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

**Adapter-specific (choose one or more):**

| Adapter | Requirements | Best for |
|---------|-------------|----------|
| **Markdown** | No external services | Lightweight, git-native teams |
| **Confluence** | Confluence API token | Enterprise teams |

---

## Configuration

D3 configuration tells the agent which artifact types are available, which adapters to use, and where to store artifacts. Edit `d3.config.yaml` in your project root.

### Markdown (Local Files)

```yaml
artifacts:
  product_spec:
    adapter: markdown
    directory: ./specs
  tech_spec:
    adapter: markdown
    directory: ./specs
  adr:
    adapter: markdown
    directory: ./adrs
  meeting_transcript:
    adapter: markdown
    directory: ./transcripts

settings:
  quiet_mode: false
```

### Confluence

Shared connection config goes in the `adapters:` section. Each artifact references the adapter by name and adds its own fields (like `location_id` for the parent page):

```yaml
adapters:
  confluence:
    base_url: https://yoursite.atlassian.net
    email: you@example.com
    space_key: PROJ

artifacts:
  product_spec:
    adapter: confluence
    location_id: "123456789"
  tech_spec:
    adapter: confluence
    location_id: "123456789"
  adr:
    adapter: confluence
    location_id: "123456790"

settings:
  quiet_mode: false
```

The `CONFLUENCE_API_TOKEN` environment variable must be set (or added to a `.env` file in the project root).

### Mixed Adapters

Adapters can be mixed freely — product specs in Confluence, tech specs in local markdown, or any other combination:

```yaml
adapters:
  confluence:
    base_url: https://yoursite.atlassian.net
    email: you@example.com
    space_key: PROJ

artifacts:
  product_spec:
    adapter: confluence
    location_id: "123456789"
  tech_spec:
    adapter: markdown
    directory: ./specs
```

---

### Quiet Mode (Optional)

By default, D3 commands are conversational — they ask clarifying questions, confirm titles, and present proposed changes before applying them. This is the recommended mode for teams.

For automated pipelines or scripted workflows, enable quiet mode to suppress all prompts:

```yaml
settings:
  quiet_mode: true
```

In quiet mode:
- Input must be passed directly in the command (transcript text, spec name, etc.)
- Location selection is skipped — the artifact's `location_id` is used
- Titles are inferred automatically without confirmation
- Changes are applied immediately without a review step
- Uncertainties are marked inline rather than surfaced interactively

---

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

2. Add a `template` field to each artifact in `d3.config.yaml`:
   ```yaml
   artifacts:
     product_spec:
       adapter: markdown
       directory: ./specs
       template: ./.d3/templates/feature-product-spec.md
     tech_spec:
       adapter: markdown
       directory: ./specs
       template: ./.d3/templates/feature-tech-spec.md
   ```

**To create a new template type:**

Use `/d3:create-template` to interactively design a new template, then add the artifact type to your config's `artifacts` section.

---

## Commands

| Command | Purpose |
|---------|---------|
| `create` | Create any artifact from input + template (specs, ADRs, transcripts, custom types) |
| `refine` | Update any existing artifact with new information |
| `create-template` | Design and generate a new artifact template |
| `decompose` | Break feature specs into INVEST-compliant user stories |

### When to Use Each Command

- **Starting a feature?** → `create` a Product Spec
- **Made an architectural decision?** → `create` an ADR
- **Had a meeting?** → `create` a Meeting Transcript
- **Got new information?** → `refine` an existing artifact
- **Ready to implement?** → `decompose` a spec into stories
- **Need a new artifact type?** → `create-template`

### Workflow

```
Cross-functional Meeting/Discussion
        ↓
create Meeting Transcript (optional — capture and structure the meeting)
        ↓
create Product Spec (paste transcript/document/description)
        ↓
Artifact with uncertainty markers
(fills what's known, leaves rest empty)
        ↓
[Progressive Refinement as information becomes available]
        ↓
refine (paste any new information)
        ↓
Updated artifact (only changed sections update)
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
create ADR (paste transcript or describe decision)
        ↓
ADR created (Context, Decision, Alternatives, Consequences)
        ↓
refine (incorporate ADR into relevant spec)
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

### Template-Driven Artifacts

The core technique is **inputs + template → artifact**. Templates define the structure, commands provide the scaffolding (config, input gathering, uncertainty markers, validation, provider dispatch). No domain-specific logic in the commands — that lives in templates.

### Conversational Workflow

Commands ask for meeting transcripts (preferred input), work conversationally if none available, propose options with pros/cons, and confirm before creating artefacts.

### Adapter Architecture

An MCP server exposes a uniform set of tools (`create_artifact`, `read_artifact`, `update_artifact`, `search_artifacts`) that dispatch to the configured adapter for each artifact type.

```
D3 Core Commands (Tool-Agnostic)
    ├── create             → Uses any artifact adapter
    ├── refine             → Uses any artifact adapter
    ├── create-template    → Generates template files
    ├── decompose          → Uses artifact adapter
    └── align-spec         → Uses artifact adapter + Codebase

Adapters (Pluggable)
    ├── Confluence         — built-in
    ├── Markdown           — built-in (local files + git)
    └── Custom             — expandable
```

---

## Repository Structure

The Claude Code plugin files (`d3/`) are the source of truth. They use platform-agnostic natural language (e.g. "the read tool") and reference `d3.config.yaml` directly. The generator copies these to other platforms, transforming frontmatter and directory structure. Each platform gets a `d3-platform` reference that maps generic tool terms to platform-specific values.

```
dialog-driven-delivery/
├── d3/                              # Core plugin — commands, skills, templates, MCP server
├── d3.platform.yaml                 # Platform tool/config mappings
├── metadata/                        # Plugin metadata
├── config/
│   ├── example-config-markdown.yaml # Markdown adapter example
│   ├── example-config-atlassian.yaml# Confluence adapter example
│   └── example-config-mixed.yaml    # Mixed adapter example
├── generate.py                      # Generator — copies source to other platforms
├── install.sh                       # Install script for non-Claude platforms
└── dist/                            # Generated — other platforms
    ├── codex/                       # .agents/skills/ + d3.config.yaml
    ├── copilot/                     # .github/prompts/ + .github/agents/ + d3.config.yaml
    └── cursor/                      # .cursor/rules/ + d3.config.yaml
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

The hook runs `python generate.py --all` when you commit changes to `d3/`, `d3.platform.yaml`, `metadata/`, or `config/`.

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
claude --plugin-dir /path/to/dialog-driven-delivery/d3
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

1. Edit source files in `d3/`
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

Yes. D3 is tool-agnostic through its adapter architecture. Use Confluence, Markdown + Git, or create custom adapters for Notion, Linear, GitHub Issues, etc.

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
