## D3 Configuration

<!-- Cloud ID: visit https://yoursite.atlassian.net/_edge/tenant_info -->
<!-- Space key: the short code in Confluence URLs, e.g. PROJ from /wiki/spaces/PROJ/... -->
<!-- Project key: the prefix in Jira issue keys, e.g. PROJ from PROJ-123 -->
<!-- Space ID: numerical ID returned by the Atlassian MCP getConfluenceSpaces call -->

### Spec Provider
**Skill:** d3-atlassian:atlassian-spec-provider
**Configuration:**
- Cloud ID: your-cloud-id
- Default Location: PROJ
- Spec Mode: combined

### ADR Provider
**Skill:** d3-atlassian:atlassian-spec-provider
**Configuration:**
- Cloud ID: your-cloud-id
- Default Location: PROJ

### Story Provider
**Skill:** d3-atlassian:atlassian-story-provider
**Configuration:**
- Cloud ID: your-cloud-id
- Default Project: PROJ

### Transcript Provider
**Skill:** d3-atlassian:atlassian-transcript-provider
**Configuration:**
- Cloud ID: your-cloud-id
- Default Location: PROJ
- spaceId: 1234567
- Default parent page: https://yoursite.atlassian.net/wiki/spaces/PROJ/pages/123456789/Transcripts
