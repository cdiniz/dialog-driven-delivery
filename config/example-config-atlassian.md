## D3 Configuration

<!-- Cloud ID: visit https://yoursite.atlassian.net/_edge/tenant_info -->
<!-- Space key: the short code in Confluence URLs, e.g. PROJ from /wiki/spaces/PROJ/... -->
<!-- Project key: the prefix in Jira issue keys, e.g. PROJ from PROJ-123 -->
<!-- Space ID: numerical ID returned by the Atlassian MCP getConfluenceSpaces call -->

### Artifacts

#### Product Spec
- Provider: d3-atlassian:atlassian-spec-provider
- Provider Config:
  - Cloud ID: your-cloud-id
  - Default Location: PROJ
  - spaceId: 1234567
  - Default parent page: https://yoursite.atlassian.net/wiki/spaces/PROJ/pages/123456789/Specs

#### Tech Spec
- Provider: d3-atlassian:atlassian-spec-provider
- Provider Config:
  - Cloud ID: your-cloud-id
  - Default Location: PROJ
  - spaceId: 1234567
  - Default parent page: https://yoursite.atlassian.net/wiki/spaces/PROJ/pages/123456789/Specs

#### ADR
- Provider: d3-atlassian:atlassian-spec-provider
- Provider Config:
  - Cloud ID: your-cloud-id
  - Default Location: PROJ
  - spaceId: 1234567
  - Default parent page: https://yoursite.atlassian.net/wiki/spaces/PROJ/pages/123456789/ADRs

#### User Story
- Provider: d3-atlassian:atlassian-story-provider
- Provider Config:
  - Cloud ID: your-cloud-id
  - Default Project: PROJ

#### Meeting Transcript
- Provider: d3-atlassian:atlassian-transcript-provider
- Provider Config:
  - Cloud ID: your-cloud-id
  - Default Location: PROJ
  - spaceId: 1234567
  - Default parent page: https://yoursite.atlassian.net/wiki/spaces/PROJ/pages/123456789/Transcripts

### Settings
- Quiet Mode: false
