## D3 Configuration

### Settings
- Quiet Mode: false

<!-- Separated spec mode: product specs in Confluence, tech specs in local markdown -->

### Product Spec Provider
**Skill:** d3-atlassian:atlassian-spec-provider
**Configuration:**
- Cloud ID: your-cloud-id
- Default Location: PROJ
- spaceId: 1234567
- Default parent page: https://yoursite.atlassian.net/wiki/spaces/PROJ/pages/123456789/Specs

### Tech Spec Provider
**Skill:** d3-markdown:markdown-spec-provider
**Configuration:**
- Specs Directory: ./specs

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
