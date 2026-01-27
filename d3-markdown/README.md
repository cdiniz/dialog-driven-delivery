# D3 Markdown Provider

**Local-first provider for D3 - Perfect for solo developers and small teams**

Store your specifications and user stories as markdown files in your git repository. No SaaS dependencies, no accounts, no subscriptions. Everything version-controlled and portable.

---

## Why Markdown Provider?

### For Solo Developers
- ✅ **No setup:** Just create directories and start
- ✅ **Free:** No subscription costs
- ✅ **Offline-first:** Work without internet
- ✅ **Simple:** Plain markdown files
- ✅ **Portable:** Move between projects easily

### For Small Teams
- ✅ **Git-based:** Use familiar git workflows (branches, PRs)
- ✅ **Reviewable:** Specs and stories in code review
- ✅ **Searchable:** Use grep, ripgrep, or IDE search
- ✅ **Collaborative:** Pull requests for planning
- ✅ **Flexible:** Switch to Jira later if needed

### For Open Source Projects
- ✅ **Transparent:** Planning visible to contributors
- ✅ **No barriers:** No account setup for contributors
- ✅ **Fork-friendly:** Contributors can fork planning too
- ✅ **Native GitHub:** Optional GitHub Issues integration

---

## Quick Start

### 1. Install Plugin

```bash
# Install d3 core plugin
claude plugin install d3@d3-marketplace

# Install markdown provider
claude plugin install d3-markdown@d3-marketplace
```

### 2. Initialize Project

```bash
# Create directories
mkdir -p specs stories .d3

# Initialize metadata
echo '{"version": "1.0", "epics": {}, "stories": {}}' > .d3/metadata.json
```

### 3. Configure CLAUDE.md

Add this to your project's `CLAUDE.md`:

```markdown
## D3 Configuration

### Spec Provider
**Skill:** d3-markdown:markdown-spec-provider
**Configuration:**
- Specs Directory: ./specs
- Default Location: .

### Story Provider
**Skill:** d3-markdown:markdown-story-provider
**Configuration:**
- Mode: local
- Stories Directory: ./stories
- Epic Prefix: epic-
- Story Prefix: story-
```

### 4. Start Using D3!

```bash
# Create your first spec
/d3:create-spec

# Decompose into stories
/d3:decompose [spec-name]

# Work on stories
vim stories/epic-1/story-1-login.md
```

---

## Directory Structure

After creating specs and stories, your project looks like:

```
my-project/
├── specs/
│   ├── user-authentication.md
│   ├── search-feature.md
│   └── payment-integration.md
├── stories/
│   ├── epics/
│   │   ├── epic-1-authentication.md
│   │   └── epic-2-search.md
│   ├── epic-1/
│   │   ├── story-1-login.md
│   │   ├── story-2-signup.md
│   │   └── story-3-password-reset.md
│   └── epic-2/
│       ├── story-4-basic-search.md
│       └── story-5-filters.md
├── .d3/
│   └── metadata.json
└── CLAUDE.md
```

---

## File Formats

### Specification Format

```markdown
# Feature: User Authentication

**Specification:** specs/user-authentication.md

---

## 📋 Product Specification

### 1. Overview

#### What & Why
Complete user authentication system enabling users to securely access their accounts...

[Rest of product spec...]

---

## 🔧 Technical Specification

### 1. Technical Approach

Use OAuth2 for authentication with JWT tokens...

[Rest of technical spec...]
```

### Epic Format

```markdown
---
type: epic
id: epic-1
title: User Authentication
status: in_progress
created: 2026-01-27
spec: specs/user-authentication.md
---

# Epic: User Authentication

**Specification:** [User Authentication](../../specs/user-authentication.md)

Complete user authentication system including login, signup, and password reset.

## User Stories

This Epic contains 3 INVEST-compliant user stories:
- [x] story-1: User Login
- [ ] story-2: User Signup
- [ ] story-3: Password Reset
```

### Story Format

```markdown
---
type: story
id: story-1
epic: epic-1
title: User Login
status: done
size: medium
estimate: 5 days
dependencies: []
blocks: [story-2, story-3]
labels: [authentication, backend, frontend]
---

# Story: User Login

**As a** registered user
**I want** to login with my email and password
**So that** I can access my account

---

## Acceptance Criteria

**AC1: Successful login**
- **Given** a registered user with valid credentials
- **When** they enter email and password and click login
- **Then** they are redirected to dashboard
- **And** session is created with 24h expiry

[More ACs...]

---

## Technical Notes

- Use bcrypt for password hashing (cost factor: 12)
- Implement rate limiting: 5 attempts per 15 minutes

**References:**
- Specification: [User Authentication](../../specs/user-authentication.md)
- Epic: [User Authentication](../epics/epic-1-authentication.md)
```

---

## Modes

### Local Mode (Default)

Stories stored as markdown files with frontmatter. All tracking via `.d3/metadata.json`.

**Best for:**
- Solo developers
- Small teams (<5)
- Projects without GitHub
- Maximum simplicity

### GitHub Issues Mode (Optional)

Stories created as GitHub Issues with labels. Leverages GitHub's native features.

**Configuration:**
```markdown
### Story Provider
**Skill:** d3-markdown:markdown-story-provider
**Configuration:**
- Mode: github-issues
- GitHub Repo: username/my-project
```

**Best for:**
- Teams already using GitHub
- Open source projects
- Wanting GitHub's UI and notifications
- Integration with GitHub Projects

---

## Workflow Examples

### Example 1: Creating First Feature

```bash
# Day 1: Planning meeting
/d3:create-spec
> How would you like to provide info?
> Option A: [paste meeting transcript]

✅ Created: specs/user-authentication.md

# Day 2: Break into stories
/d3:decompose user-authentication
> Project: local
> Decomposition meeting? No

✅ Created Epic: epic-1-authentication
✅ Created 3 stories:
   - story-1-login.md
   - story-2-signup.md
   - story-3-password-reset.md

# Day 3-10: Implementation
vim stories/epic-1/story-1-login.md
# Update status in frontmatter: status: done

# Day 11: Review
cat .d3/metadata.json | jq '.stories'
```

### Example 2: Refining Spec

```bash
# After technical design meeting
/d3:refine-spec user-authentication
> How would you like to provide info?
> Option A: [paste technical decisions]

✅ Updated: Technical Spec 30% → 85%
```

### Example 3: Team Collaboration

```bash
# Create branch for planning
git checkout -b feature/payment-integration

# Create spec
/d3:create-spec
> [details about payment feature]

# Decompose
/d3:decompose payment-integration

# Create PR
git add specs/ stories/ .d3/
git commit -m "Add payment integration planning"
git push origin feature/payment-integration

# Team reviews planning in PR before implementation!
```

---

## Git Integration

### Recommended .gitignore

```
# Don't ignore these!
# specs/
# stories/
# .d3/

# Ignore backups
*.backup
*.md.backup
```

### Commit Messages

```bash
# After creating spec
git commit -m "Add spec: User Authentication"

# After decomposing
git commit -m "Decompose: User Authentication into 3 stories"

# After updating story status
git commit -m "Complete story-1: User Login"
```

### Branch Strategy

```bash
# Planning branch
feature/[feature-name]-planning  # Contains specs and stories

# Implementation branch
feature/[feature-name]-impl      # Contains code

# Or combined
feature/[feature-name]           # Contains both planning and code
```

---

## Searching and Querying

### Find Specs

```bash
# By keyword
rg "authentication" specs/

# By section
rg "## Technical Approach" specs/

# Open questions
rg "\[OPEN QUESTION" specs/
```

### Find Stories

```bash
# By status
rg "^status: done" stories/

# By epic
ls stories/epic-1/

# By dependency
rg "^dependencies:.*story-1" stories/

# All blocking stories
rg "^blocks:" stories/
```

### Metadata Queries

```bash
# All epics
cat .d3/metadata.json | jq '.epics'

# Stories by status
cat .d3/metadata.json | jq '.stories | map(select(.status == "done"))'

# Dependency graph
cat .d3/metadata.json | jq '.dependency_graph'

# Count stories
cat .d3/metadata.json | jq '.stories | length'
```

---

## Comparison with Atlassian Provider

| Feature | Atlassian | Markdown | Best For |
|---------|-----------|----------|----------|
| Setup Time | 30 minutes | 2 minutes | Markdown |
| Monthly Cost | $7-10/user | Free | Markdown |
| Offline Work | No | Yes | Markdown |
| Version Control | Basic | Full (git) | Markdown |
| Collaboration | Excellent | Good (PRs) | Depends |
| Rich UI | Excellent | Basic | Atlassian |
| Search | Excellent | Good (grep) | Atlassian |
| Reporting | Excellent | DIY | Atlassian |
| Enterprise Scale | Excellent | Limited | Atlassian |
| Portability | Locked-in | Fully portable | Markdown |
| Learning Curve | Moderate | Minimal | Markdown |

**Recommendation:**
- **Solo/2-3 person teams:** Markdown provider
- **4-10 person teams:** Markdown, consider Atlassian when scaling
- **10+ person teams:** Atlassian provider
- **Open source projects:** Markdown (GitHub Issues mode)

---

## Migration

### From Markdown to Atlassian

```bash
# Export stories to CSV
./scripts/export-to-csv.sh

# Import to Jira via CSV importer
# (Jira has native CSV import)

# Update CLAUDE.md to use Atlassian provider
```

### From Atlassian to Markdown

```bash
# Export from Jira to CSV
# Convert CSV to markdown files
./scripts/import-from-csv.sh

# Update CLAUDE.md to use Markdown provider
```

---

## Advanced Features

### Custom Templates

Create custom templates for specs and stories:

```bash
mkdir -p .d3/templates/
cp d3/templates/feature-spec.md .d3/templates/my-spec-template.md
# Edit template as needed
```

### Status Tracking

Update story status manually or via helper scripts:

```bash
# Manual (edit frontmatter)
vim stories/epic-1/story-1-login.md
# Change: status: todo → status: in_progress

# Future: CLI helper
d3 story update story-1 --status done
```

### Dependency Visualization

```bash
# Future: Generate dependency graph
d3 dependencies --output deps.svg
```

---

## Troubleshooting

### Problem: Metadata out of sync

```bash
# Regenerate metadata from markdown files
d3 metadata rebuild
```

### Problem: Can't find spec

```bash
# List all specs
find specs -name "*.md"

# Use search instead
/d3:refine-spec
> [paste spec content to find by search]
```

### Problem: Story IDs conflict

Edit `.d3/metadata.json` manually to fix IDs, or regenerate:

```bash
d3 metadata rebuild --fix-ids
```

---

## Future Enhancements

### Planned Features
- [ ] CLI helper tool (`d3` command)
- [ ] Dashboard generator (HTML view of all stories)
- [ ] Burndown chart generation
- [ ] GitHub Issues sync (two-way)
- [ ] Export to Jira/Linear formats
- [ ] Story templates
- [ ] Automated metadata updates via git hooks

### Contribute

Want to add features? PRs welcome!

```bash
git clone https://github.com/cdiniz/dialog-driven-delivery
cd dialog-driven-delivery/d3-markdown
# Make changes
# Submit PR
```

---

## Support

- **Issues:** [GitHub Issues](https://github.com/cdiniz/dialog-driven-delivery/issues)
- **Documentation:** See main D3 README
- **Examples:** See [examples/](examples/) directory

---

## License

MIT

---

**Make D3 accessible to everyone - no enterprise tools required!** 🚀
