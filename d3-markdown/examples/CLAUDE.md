# Project Configuration

## D3 Configuration

### Spec Provider
**Skill:** d3-markdown:markdown-spec-provider
**Configuration:**
- Specs Directory: ./specs
- Default Location: .

### ADR Provider
**Skill:** d3-markdown:markdown-spec-provider
**Configuration:**
- Specs Directory: ./adrs
- Default Location: .

### Story Provider
**Skill:** d3-markdown:markdown-story-provider
**Configuration:**
- Stories Directory: ./stories
- Epic Prefix: epic-
- Story Prefix: story-

### Transcript Provider
**Skill:** d3-markdown:markdown-transcript-provider
**Configuration:**
- Transcripts Directory: ./transcripts
- Default Location: .

---

## Project Information

**Project Name:** My Awesome App
**Tech Stack:** Node.js, React, PostgreSQL
**Team Size:** 1 (solo developer)

---

## Development Commands

```bash
# Install dependencies
npm install

# Run tests
npm test

# Run locally
npm run dev

# Build for production
npm run build
```

---

## D3 Usage Tips

### Getting Started
1. Create your first spec: `/d3:create-spec`
2. Refine it as needed: `/d3:refine-spec [spec-name]`
3. Decompose into stories: `/d3:decompose [spec-name]`
4. Implement stories one by one

### Best Practices
- Commit specs and stories to git regularly
- Update story status in frontmatter as you progress
- Keep specs and code in sync via `/d3:refine-spec`
- Review the `.d3/metadata.json` to see progress

### File Locations
- **Specs:** `./specs/*.md`
- **Stories:** `./stories/*/story-*.md`
- **Transcripts:** `./transcripts/YYYY-MM/*.md`

---

## Git Workflow

```bash
# When starting new feature
git checkout -b feature/awesome-feature
/d3:create-spec  # Create spec
/d3:decompose    # Create stories
git add specs/ stories/ .d3/
git commit -m "Add planning for awesome feature"
git push

# Implement each story
git checkout -b feature/awesome-feature-story-1
# ... implement ...
git commit -m "Implement story-1: User login"
# Update story status to 'done' in frontmatter
git commit -m "Complete story-1"
git push

# Merge story
# Repeat for other stories

# After all stories done, merge feature branch
```

---

## Notes

This is a simple solo developer setup. As your team grows, you can:
- Switch to an enterprise provider if needed
- Add more sophisticated tracking tools
- Integrate with other platforms via custom providers

The beauty of D3 with markdown is that everything is in git, so you can always migrate later without losing history!
