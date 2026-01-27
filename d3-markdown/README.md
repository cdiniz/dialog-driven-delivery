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
- ✅ **Flexible:** Migrate to enterprise tools later if needed

### For Open Source Projects
- ✅ **Transparent:** Planning visible to contributors
- ✅ **No barriers:** No account setup for contributors
- ✅ **Fork-friendly:** Contributors can fork planning too
- ✅ **Git-native:** Full version control for planning docs

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
mkdir -p specs stories
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
- Stories Directory: ./stories
- Story Prefix: story-
```

### 4. Start Using D3!

```bash
# Create your first spec
/d3:create-spec

# Decompose into stories
/d3:decompose [spec-name]

# Work on stories
vim stories/user-authentication/story-1-login.md
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
│   ├── user-authentication/
│   │   ├── story-1-login.md
│   │   ├── story-2-signup.md
│   │   └── story-3-password-reset.md
│   └── search-feature/
│       ├── story-1-basic-search.md
│       └── story-2-filters.md
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

### Story Format

```markdown
---
type: story
id: story-1
spec: specs/user-authentication.md
title: User Login
status: done
size: medium
estimate: 5 days
dependencies: []
blocks: [story-2, story-3]
labels: [authentication, backend, frontend]
created: 2026-01-27
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
- Spec: [User Authentication](../../specs/user-authentication.md)
```

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

✅ Created 3 stories in stories/user-authentication/:
   - story-1-login.md
   - story-2-signup.md
   - story-3-password-reset.md

# Day 3-10: Implementation
vim stories/user-authentication/story-1-login.md
# Update status in frontmatter: status: done

# Day 11: Review
find stories -name "*.md" -exec head -20 {} \; | grep "^status:"
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
git add specs/ stories/
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

# By feature/spec
ls stories/user-authentication/

# By dependency
rg "^dependencies:.*story-1" stories/

# All blocking stories
rg "^blocks:" stories/
```

### Story Queries

```bash
# All stories
find stories -name "story-*.md"

# Count stories
find stories -name "story-*.md" | wc -l

# View all story statuses
rg "^status:" stories/ --no-filename | sort | uniq -c

# List done stories
rg "^status: done" stories/ -l
```

---

## Comparison with Enterprise Tools

| Feature | Enterprise Tools | Markdown | Best For |
|---------|-----------------|----------|----------|
| Setup Time | 30+ minutes | 2 minutes | Markdown |
| Monthly Cost | $7-20/user | Free | Markdown |
| Offline Work | Usually No | Yes | Markdown |
| Version Control | Basic | Full (git) | Markdown |
| Collaboration | Excellent | Good (PRs) | Depends |
| Rich UI | Excellent | Basic | Enterprise |
| Search | Excellent | Good (grep) | Enterprise |
| Reporting | Excellent | DIY | Enterprise |
| Enterprise Scale | Excellent | Good (5-10) | Enterprise |
| Portability | Vendor lock-in | Fully portable | Markdown |
| Learning Curve | Moderate-High | Minimal | Markdown |

**Recommendation:**
- **Solo/2-3 person teams:** Markdown provider (perfect fit)
- **4-10 person teams:** Markdown (works well with git workflows)
- **10+ person teams:** Consider enterprise provider for scale
- **Open source projects:** Markdown (fully transparent planning)

---

## Migration

### From Markdown to Other Tools

```bash
# Export stories to CSV
./scripts/export-to-csv.sh

# Import to your work tracking tool via CSV
# Most tools support CSV import

# Update CLAUDE.md to use appropriate provider
```

### From Other Tools to Markdown

```bash
# Export from your work tracking tool to CSV
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
vim stories/user-authentication/story-1-login.md
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

### Problem: Can't find spec

```bash
# List all specs
find specs -name "*.md"

# Use search instead
/d3:refine-spec
> [paste spec content to find by search]
```

---

## Future Enhancements

### Planned Features
- [ ] CLI helper tool (`d3` command)
- [ ] Dashboard generator (HTML view of all stories)
- [ ] Burndown chart generation
- [ ] GitHub Issues sync (two-way)
- [ ] Export to CSV for work tracking tools
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
