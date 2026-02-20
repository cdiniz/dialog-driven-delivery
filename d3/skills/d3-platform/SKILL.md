---
name: d3-platform
description: D3 platform-specific tool and configuration mappings for Claude Code. Read this before executing D3 commands or skills.
---
# D3 Platform Reference

## Tool Mapping
| Reference | Tool |
|---|---|
| read tool | `Read` |
| write tool | `Write` |
| search tool | `Grep` |
| glob tool | `Glob` |
| shell tool | `Bash` |

## Skill Invocation
To invoke a skill, use this syntax:
```
Skill(skill="<skill-name>", args="<arguments>")
```

## Template References
D3 template files are located at:
```
d3/skills/d3-templates/references
```
