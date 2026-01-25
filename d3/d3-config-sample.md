# ADD THIS TO YOUR claude.md, REPLACE with your config

# D3 Provider Configuration

This file configures which provider skills D3 (Dialog Driven Delivery) uses for specification storage and story tracking.

**If this file doesn't exist:** D3 defaults to Atlassian providers using configuration from `CLAUDE.md`.

## How It Works

### 1. User runs a D3 command
```
/create-spec
/refine-spec [PAGE-ID]
/decompose [PAGE-ID]
```

### 2. D3 skill detects which provider to use
Each D3 skill has a "Step 0: Detect Provider":
1. Uses Read tool to check if `.claude/d3-config.md` exists
2. If exists: Reads this file and extracts Skill name (e.g., "atlassian-spec-provider")
3. If not exists: Defaults to "atlassian-spec-provider" and reads config from `CLAUDE.md`

### 3. D3 skill invokes the provider
```
Skill(skill="atlassian-spec-provider", args="create_spec location_id=\"BOOT\" title=\"...\" body=\"...\"")
```

### 4. Provider skill executes
1. Provider skill is loaded into context
2. Parses the operation and arguments
3. Reads configuration (Cloud ID, Default Location) from this file or `CLAUDE.md`
4. Calls the appropriate Atlassian MCP tool
5. Returns result to D3 skill

### 5. D3 skill continues
Uses the provider's response to continue the workflow.

## Context Flow

**What gets into context and when:**

| Step | What's in Context | How |
|------|-------------------|-----|
| User runs `/create-spec` | create-spec skill loaded | Skill tool invocation |
| Step 0: Detect Provider | d3-config.md content | Read tool |
| Step X: Use Provider | Provider skill loaded (atlassian-spec-provider) | Skill tool invocation |
| Provider executes | Provider skill + d3-config.md (or CLAUDE.md) | Read tool inside provider |
| Provider calls MCP | MCP tool parameters | Direct MCP call |

**Key Point:** Configuration files are NOT automatically in context. Skills explicitly read them using the Read tool when needed.

---

## Current Configuration

### Spec Provider
**Skill:** atlassian-spec-provider
**Configuration:**
- Cloud ID: XXXXXXX
- Default Location: BOOT
- spaceId: XXXXXXX
- Default parent page: some_url

### Story Provider
**Skill:** atlassian-story-provider
**Configuration:**
- Cloud ID: XXXXXXX
- Default Project: BOOT

