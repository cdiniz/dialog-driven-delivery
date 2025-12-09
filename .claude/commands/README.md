# AI-Enabled Development Workflow Commands

This directory contains slash commands for AI-assisted software development, from feature planning through implementation and deployment.

---

## 📚 Documentation

### [SPEC_README.md](SPEC_README.md) - Feature Planning & Decomposition
Complete workflow for creating feature specifications and breaking them into user stories:
- `/create-spec` - Create feature specifications in Confluence
- `/refine-spec` - Refine specifications based on new information
- `/create-user-stories-from-spec` - Decompose features into Jira stories

**Use when:** Planning features, refining requirements, creating user stories

---

### [CODING_README.md](CODING_README.md) - Implementation & Code Review
Comprehensive guide for implementing user stories with AI assistance:
- `/implement-story` - Implement Jira story with tests
- `/commit-and-open-pr` - Create pull request
- `/address-pr-feedback` - Handle code review feedback

**Use when:** Implementing features, creating PRs, addressing feedback

---

## 🚀 Quick Start

### Complete Feature Development Flow

```bash
# 1. Planning Phase
/create-spec                           # Create feature spec in Confluence
/refine-spec PAGE-ID                   # Refine based on discussions

# 2. Decomposition Phase
/create-user-stories-from-spec PAGE-ID # Break into Jira stories

# 3. Implementation Phase (per story)
/implement-story                       # Implement story with tests
/manual-test-story                     # Verify ACs in browser
/commit-and-open-pr                    # Create PR
/address-pr-feedback                   # Address review comments

# 4. Merge and repeat for next story
```

---

## 📖 Available Commands

| Command | Phase | Purpose | Documentation |
|---------|-------|---------|---------------|
| `/create-spec` | Planning | Create feature specification | [SPEC_README.md](SPEC_README.md#1-create-spec) |
| `/refine-spec` | Planning | Update specifications | [SPEC_README.md](SPEC_README.md#2-refine-spec-page-id) |
| `/create-user-stories-from-spec` | Planning | Break into stories | [SPEC_README.md](SPEC_README.md#3-decompose-feature-page-id) |
| `/implement-story` | Coding | Implement story | [CODING_README.md](CODING_README.md#step-1-start-implementation) |
| `/manual-test-story` | Coding | Manual testing in browser | [CODING_README.md](CODING_README.md#step-4-manual-testing) |
| `/commit-and-open-pr` | Coding | Create PR | [CODING_README.md](CODING_README.md#step-5-commit-and-create-pr) |
| `/address-pr-feedback` | Coding | Handle feedback | [CODING_README.md](CODING_README.md#step-6-address-pr-feedback) |

---

## 🎯 When to Use Each Command

### Planning & Requirements
- **Just starting a feature?** → `/create-spec`
- **Got new information?** → `/refine-spec`
- **Ready for implementation?** → `/create-user-stories-from-spec`

### Development & Delivery
- **Starting to code?** → `/implement-story`
- **Tests passing, ready to verify?** → `/manual-test-story`
- **Manual testing done?** → `/commit-and-open-pr`
- **Got review feedback?** → `/address-pr-feedback`

---

## 🔄 Typical Weekly Workflow

```
Monday: Feature Planning
├─ /create-spec (paste meeting transcript)
└─ Confluence page created

Tuesday-Wednesday: Refinement
├─ /refine-spec (add technical details)
└─ Specifications complete

Thursday: Story Decomposition
├─ /create-user-stories-from-spec
└─ Jira stories created

Next Sprint: Implementation
├─ /implement-story (for each story)
├─ /manual-test-story (verify in browser)
├─ /commit-and-open-pr
├─ /address-pr-feedback
└─ Merge and repeat
```

---

## ✅ Prerequisites

- **Atlassian Tools**: Confluence + Jira access
- **Atlassian MCP Server**: Configured in Claude Code
- **Git**: Repository with main branch
- **Development Environment**: Tests can run locally

---

## 🎓 Learning Path

**New to the workflow?** Follow this sequence:

1. **Read [SPEC_README.md](SPEC_README.md)**
   - Understand feature planning workflow
   - Learn spec creation and refinement
   - Master story decomposition

2. **Read [CODING_README.md](CODING_README.md)**
   - Learn implementation best practices
   - Understand testing standards
   - Master PR workflow

3. **Try it out**
   - Start with a small feature
   - Follow the commands step by step
   - Iterate and improve

---

## 💡 Key Principles

### Documentation-First
- Specs live in Confluence (single source of truth)
- Stories live in Jira (actionable work items)
- Code lives in Git (implementation)

### Conversational & Engaging
- Commands ask questions and guide you
- Paste meeting transcripts for best results
- Agent proposes, you confirm

### Quality Through Process
- Comprehensive acceptance criteria
- Tests before merge
- Systematic feedback handling
- Architecture compliance

### Iterative & Adaptive
- Refine specs as you learn
- Address feedback in rounds
- Improve continuously

---

## 🔧 Project Configuration

Required in your project's `CLAUDE.md` or similar:

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

## 📊 Success Metrics

### Planning Phase
- ✅ Specs completed before coding
- ✅ All open questions resolved
- ✅ Stories have clear acceptance criteria
- ✅ Dependencies mapped in Jira

### Implementation Phase
- ✅ All tests passing before PR
- ✅ No skipped or disabled tests
- ✅ All ACs covered by tests
- ✅ Code follows architecture guidelines
- ✅ PR feedback addressed systematically

---

## 🆘 Troubleshooting

### "I don't have meeting transcripts"
All commands work conversationally - just select the option to describe conversationally and answer the agent's questions.

### "My implementation is different from the spec"
Use `/refine-spec` to update the specification with learnings from implementation.

### "Tests are failing"
Never skip tests - fix the underlying issue. See [CODING_README.md](CODING_README.md#troubleshooting) for common scenarios.

### "PR feedback seems overwhelming"
Use `/address-pr-feedback` - it categorizes by priority and works systematically through each item.

---

## 🤝 Integration

These commands integrate with:
- **Atlassian Confluence** - Feature specifications
- **Atlassian Jira** - User stories and tracking
- **GitHub** - Pull requests and code review
- **Git** - Version control and branching
- **Testing Frameworks** - Vitest, Pytest, etc.

---

## 📝 Real-World Example

See [CODING_README.md - Real Example: BOOT-8](CODING_README.md#real-example-boot-8) for a complete walkthrough of implementing a feature from story to merge.

---

## 🚢 What's Next?

After mastering these commands:
1. Customize commands for your team's workflow
2. Add project-specific templates
3. Create custom commands for repeated tasks
4. Share learnings with your team

---

## 📖 Further Reading

- [SPEC_README.md](SPEC_README.md) - Detailed spec workflow
- [CODING_README.md](CODING_README.md) - Detailed coding workflow
- Project's `CLAUDE.md` - Architecture and guidelines
- Individual command files - Specific command details

---

## 📄 License

These workflows are open for use and adaptation. Modify to fit your team's needs.

---

## 🙋 Support

- **Questions about planning?** See [SPEC_README.md](SPEC_README.md)
- **Questions about coding?** See [CODING_README.md](CODING_README.md)
- **Questions about commands?** Review individual command files
- **Issues or improvements?** Ask Claude Code for help

---

*Built for real teams, refined through real projects.* 🚀
