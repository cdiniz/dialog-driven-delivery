# D3 Markdown Provider - Quickstart Guide

**Get started with D3 in 5 minutes - perfect for solo developers!**

---

## Prerequisites

- **Claude Code** installed
- **Git** for version control
- A project directory

---

## Step 1: Install D3 Plugins (2 minutes)

```bash
# Add the D3 marketplace (if not already added)
claude plugin marketplace add cdiniz/dialog-driven-delivery

# Install core D3 plugin
claude plugin install d3@d3-marketplace

# Install markdown provider
claude plugin install d3-markdown@d3-marketplace
```

---

## Step 2: Initialize Your Project (1 minute)

```bash
# Navigate to your project
cd my-awesome-project

# Create D3 directories
mkdir -p specs stories .d3

# Initialize metadata file
echo '{"version": "1.0", "epics": {}, "stories": {}, "next_id": {"epic": 1, "story": 1}}' > .d3/metadata.json

# Create CLAUDE.md (or add to existing)
cat >> CLAUDE.md << 'EOF'

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
EOF
```

---

## Step 3: Create Your First Spec (2 minutes)

Start Claude Code and run:

```bash
claude code

# In Claude Code:
/d3:create-spec
```

Claude will ask you:
```
How would you like to provide the feature information?

**Option A: Meeting Transcript**
**Option B: Document**
**Option C: Describe Conversationally**
```

**Choose Option C** and describe your feature. For example:

```
I want to build a user authentication feature with login and signup.
Users should be able to register with email and password, then log in
to access their account.
```

Claude will:
1. Ask where to create the spec (answer: `.` for root)
2. Propose a title (e.g., "User Authentication")
3. Create the spec file

Result: `specs/user-authentication.md` created! ✅

---

## Step 4: Review and Refine (Optional)

Open your spec file:

```bash
cat specs/user-authentication.md
# or
vim specs/user-authentication.md
```

If you want to add more details:

```bash
# In Claude Code:
/d3:refine-spec user-authentication
```

Add new information (technical decisions, requirements, etc.)

---

## Step 5: Break Into Stories (2 minutes)

```bash
# In Claude Code:
/d3:decompose user-authentication
```

Claude will ask:
```
Which project should I create user stories in?
```

Answer: `local`

```
Did you have a decomposition meeting?

**Option A: Yes, I have a transcript**
**Option B: No, let's decompose it together**
```

Choose **Option B** - Claude will propose story breakdown based on INVEST principles.

Review and confirm. Claude creates:
- Epic file: `stories/epics/epic-1-authentication.md`
- Story files: `stories/epic-1/story-1-*.md`, `story-2-*.md`, etc.

---

## Step 6: Start Implementing

Check your stories:

```bash
# List all stories
find stories -name "story-*.md"

# View first story
cat stories/epic-1/story-1-*.md
```

Pick a story and start coding!

---

## Step 7: Track Progress

As you work on stories, update the frontmatter:

```bash
# Edit story file
vim stories/epic-1/story-1-login.md

# Change status in frontmatter:
# status: todo → status: in_progress → status: done
```

Or check overall progress:

```bash
# View metadata
cat .d3/metadata.json | jq '.stories'

# Count done stories
cat .d3/metadata.json | jq '.stories | map(select(.status == "done")) | length'
```

---

## Step 8: Commit to Git

```bash
# Add files
git add specs/ stories/ .d3/ CLAUDE.md

# Commit
git commit -m "Add User Authentication feature planning"

# Push
git push
```

---

## Complete Example Workflow

Here's a complete session:

```bash
# Day 1: Planning
claude code
> /d3:create-spec
> [Describe user authentication feature]
> Location: .
✅ Created: specs/user-authentication.md

> /d3:decompose user-authentication
> Project: local
> Option B: Let's decompose together
✅ Created Epic: epic-1
✅ Created 3 stories

# Check what was created
cat .d3/metadata.json | jq .

# Commit planning
git add specs/ stories/ .d3/
git commit -m "Add auth feature planning"

# Day 2-5: Implementation
# Work on story-1
vim stories/epic-1/story-1-login.md  # Check acceptance criteria
# ... implement ...
# Update status to 'done'

# Day 6: Deploy and track
# All stories done!
git add .
git commit -m "Complete User Authentication feature"
```

---

## Directory Structure After Quickstart

```
my-awesome-project/
├── specs/
│   └── user-authentication.md          # ✅ Your spec
├── stories/
│   ├── epics/
│   │   └── epic-1-authentication.md    # ✅ Your epic
│   └── epic-1/
│       ├── story-1-login.md            # ✅ Your stories
│       ├── story-2-signup.md
│       └── story-3-password-reset.md
├── .d3/
│   └── metadata.json                   # ✅ Tracking metadata
├── CLAUDE.md                           # ✅ D3 configuration
└── .git/                               # ✅ Git repo
```

---

## Next Steps

### Daily Workflow

1. **Work on a story:**
   ```bash
   # Pick story
   cat stories/epic-1/story-1-login.md

   # Implement
   # ... code ...

   # Update status
   vim stories/epic-1/story-1-login.md
   # Change: status: in_progress → status: done

   # Commit
   git commit -m "Complete story-1: User Login"
   ```

2. **Add new information to spec:**
   ```bash
   /d3:refine-spec user-authentication
   > [Add technical decisions from architecture meeting]
   ```

3. **Check progress:**
   ```bash
   cat .d3/metadata.json | jq '.stories[] | {id, title, status}'
   ```

### Advanced Usage

**Use GitHub Issues instead of local files:**

Update CLAUDE.md:
```markdown
### Story Provider
**Skill:** d3-markdown:markdown-story-provider
**Configuration:**
- Mode: github-issues
- GitHub Repo: yourusername/your-repo
```

**Search specs:**
```bash
# Find specs with specific content
rg "OAuth" specs/

# Find all open questions
rg "\[OPEN QUESTION" specs/
```

**View dependency graph:**
```bash
cat .d3/metadata.json | jq '.stories[] | {id, blocks, dependencies}'
```

---

## Troubleshooting

### Problem: Metadata file is empty or corrupt

```bash
# Reinitialize
echo '{"version": "1.0", "epics": {}, "stories": {}, "next_id": {"epic": 1, "story": 1}}' > .d3/metadata.json
```

### Problem: Can't find spec

```bash
# List all specs
find specs -name "*.md"

# Use search in refine command
/d3:refine-spec
> [Paste some content from spec to search]
```

### Problem: Story files not created

Check that directories exist:
```bash
ls -la stories/epics/
ls -la stories/epic-1/
```

If missing, create manually:
```bash
mkdir -p stories/epics
```

---

## Getting Help

- **Examples:** See `d3-markdown/examples/` directory
- **Issues:** https://github.com/cdiniz/dialog-driven-delivery/issues
- **Documentation:** See `d3-markdown/README.md`

---

## What's Next?

Once comfortable with markdown provider:

1. **Scale up:** Add more team members using git workflows
2. **Migrate:** Switch to Atlassian provider when team grows (10+ people)
3. **Customize:** Create custom templates in `.d3/templates/`
4. **Automate:** Add git hooks for metadata updates

---

**Congratulations! You're now using D3 with markdown files!** 🎉

Start building features with better planning and tracking! 🚀
