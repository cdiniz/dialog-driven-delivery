## D3 Configuration

<!-- Mixed mode: product specs in Confluence, tech specs in local markdown -->

### Artifacts

#### Product Spec
- Provider: d3-atlassian:atlassian-spec-provider
- Provider Config:
  - Cloud ID: your-cloud-id
  - Default Location: PROJ
  - spaceId: 1234567
  - Default parent page: https://yoursite.atlassian.net/wiki/spaces/PROJ/pages/123456789/Specs

#### Tech Spec
- Provider: d3-markdown:markdown-spec-provider
- Provider Config:
  - Directory: ./specs

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
