---
description: Generate technical specification for Linear Project (feature)
---

Generate a comprehensive technical specification for a Linear Project using a conversational, engaging approach.

## Conversational Workflow

This command uses an **engaging, conversational approach**:
1. Accept Linear Project ID as argument
2. Fetch project details and analyze current state
3. Ask if there's a technical discussion transcript
4. Analyze transcript or work conversationally
5. Review codebase architecture
6. Ask clarifying technical questions
7. Generate technical spec with smart section selection
8. Provide clear summary

## Steps

### Step 1: Get Project ID from Arguments

The command accepts the Linear Project as `$ARGUMENTS`:
- Project Key (e.g., `PROJ-42`)
- Project Name (e.g., `Advanced Search`)
- Project ID (UUID)

### Step 2: Fetch and Analyze Project

Query Linear for the project and display current state:

```markdown
I found Linear Project $ARGUMENTS:

**Project:** [PROJECT-KEY] - [Project Name]
**URL:** [Linear Project URL]
**Status:** [Current status]
**Team:** [Team name]

**Current Documentation:**
- Feature Spec: [✅ path or ❌ Not found]
- Technical Spec: [✅ path or ❌ Not found]

**User Stories:** [N] stories in this project
- [ISSUE-1]: [Title]
- [ISSUE-2]: [Title]
- [Continue listing all stories]

[If no feature spec found, warn: "⚠️ I recommend creating a feature spec first with `/generate-feature-brief`, but I can proceed with creating a technical spec based on the Linear project description and user stories."]
```

### Step 3: Read Feature Spec (If Available)

If feature spec exists:
- Read the complete feature spec
- Extract key information:
  - User workflows
  - Functional requirements
  - Non-functional requirements
  - Business rules and validation
  - Dependencies and constraints
  - Compliance requirements

### Step 4: Analyze User Stories

Read all user stories from the Linear project:
- Extract acceptance criteria
- Identify technical requirements
- Note data models needed
- Identify API endpoints
- Spot UI components
- Find integration points
- Identify security considerations

### Step 5: Request Technical Discussion Input

Ask user if they have a technical design discussion:

```markdown
Before I create the technical spec, did you have a meeting to discuss the technical approach for this feature?

**Option A: Yes, I have a transcript** - Paste your technical design meeting transcript
**Option B: No, let's discuss it now** - I'll ask you technical questions

Which would you prefer?
```

### Step 6: Analyze Technical Input

**If transcript provided (Option A):**

Analyze the transcript and extract:
- **Architecture Decisions:** Component structure, layers, patterns
- **Technology Choices:** Frameworks, libraries, tools
- **Data Model Decisions:** Database schema, entities, relationships
- **API Design:** Endpoints, request/response formats, error handling
- **Frontend Approach:** Components, state management, routing
- **Integration Strategy:** Third-party services, webhooks, events
- **Security Approach:** Authentication, authorization, data protection
- **Performance Considerations:** Caching, optimization, scalability
- **Testing Strategy:** Unit, integration, e2e approaches
- **Deployment Approach:** Infrastructure, CI/CD, monitoring

Summarize findings:

```markdown
I've analyzed your technical discussion transcript. Here's what I found:

**Architecture:**
- [Key architectural decision 1]
- [Key architectural decision 2]

**Technology Stack:**
- [Technology 1 and its purpose]
- [Technology 2 and its purpose]

**Key Design Decisions:**
- [Decision 1]
- [Decision 2]
- [Decision 3]

[Continue with all extracted information]
```

**If conversational (Option B):**

Ask structured technical questions based on the feature type.

### Step 7: Review Codebase Architecture

Before asking questions, analyze the existing codebase:

```markdown
Let me review your codebase to understand existing patterns...

I've reviewed your codebase and found:

**Project Structure:**
- [Architecture pattern: MVC, Hexagonal, Layered, etc.]
- [Frontend framework and version]
- [Backend framework and version]
- [Database type and version]

**Existing Patterns:**
- API endpoints follow: [pattern found]
- Database models use: [ORM/pattern found]
- Frontend components use: [pattern found]
- State management: [approach found]
- Testing approach: [strategy found]

**Relevant Existing Code:**
- Similar feature: [path to similar feature]
- Reusable components: [paths to components]
- Shared utilities: [paths to utilities]

I'll create the technical spec following these established patterns.
```

### Step 8: Ask Clarifying Technical Questions

Based on the feature type, transcript analysis, and codebase review, ask targeted questions:

**For Backend/API Features:**
```markdown
Let me clarify some technical details:

1. **Data Model:**
   - [Question about database schema based on requirements]
   - [Question about relationships based on workflows]

2. **API Design:**
   - [Question about endpoint structure]
   - [Question about authentication/authorization]

3. **Performance:**
   - [Question about expected load/volume]
   - [Question about caching strategy]

4. **Error Handling:**
   - [Question about error scenarios]
   - [Question about retry/fallback logic]

[Continue with relevant questions]
```

**For Frontend Features:**
```markdown
Let me clarify the frontend approach:

1. **Component Structure:**
   - [Question about component hierarchy]
   - [Question about component reusability]

2. **State Management:**
   - [Question about state structure]
   - [Question about state persistence]

3. **User Experience:**
   - [Question about loading states]
   - [Question about error feedback]

4. **Data Fetching:**
   - [Question about when to fetch data]
   - [Question about caching/invalidation]

[Continue with relevant questions]
```

**For Integration Features:**
```markdown
Let me understand the integration requirements:

1. **External Service:**
   - [Question about service selection]
   - [Question about API credentials/auth]

2. **Integration Pattern:**
   - [Question about sync vs async]
   - [Question about webhooks vs polling]

3. **Error Handling:**
   - [Question about service unavailability]
   - [Question about retry strategy]

4. **Data Sync:**
   - [Question about data mapping]
   - [Question about conflict resolution]

[Continue with relevant questions]
```

### Step 9: Determine Relevant Sections

Based on the feature type and requirements, decide which optional sections to include:

**Always Include (Core):**
- Overview & Context
- Architecture Overview
- Testing Strategy
- Open Questions & Decisions
- References

**Conditionally Include (Optional):**

**Include "Data Models" if:**
- Feature creates/modifies database entities
- User stories mention data persistence
- Transcript discusses schema changes

**Include "API Contracts" if:**
- Feature creates/modifies API endpoints
- User stories describe API interactions
- Transcript discusses REST/GraphQL APIs

**Include "UI Components" if:**
- Feature has frontend elements
- User stories describe UI
- Transcript discusses components

**Include "State Management" if:**
- Feature has complex frontend state
- User stories mention state synchronization
- Transcript discusses Redux/Vuex/Context

**Include "Integration Points" if:**
- Feature integrates with third-party services
- User stories mention external systems
- Transcript discusses webhooks/events

**Include "Security Considerations" if:**
- Feature handles authentication/authorization
- Feature handles sensitive data
- User stories mention security requirements
- Transcript discusses security concerns

**Include "Monitoring & Observability" if:**
- Feature is performance-critical
- User stories mention SLAs
- Transcript discusses monitoring/alerts

**Include "Infrastructure/Deployment" if:**
- Feature requires infrastructure changes
- Transcript discusses deployment strategy
- Feature requires new services/containers

Explain your section selection:

```markdown
Based on this feature, I'll include these sections in the technical spec:

**Core Sections:**
- Overview & Context (always included)
- Architecture Overview (always included)
- Testing Strategy (always included)
- Open Questions & Decisions (always included)
- References (always included)

**Optional Sections:**
✅ **Data Models** - This feature creates new database tables for [entities]
✅ **API Contracts** - This feature adds [N] new API endpoints
✅ **UI Components** - This feature requires [N] new frontend components
❌ **State Management** - Not needed, state is simple and component-local
✅ **Security Considerations** - This feature handles [sensitive data/auth]
❌ **Monitoring & Observability** - Not performance-critical, standard monitoring is sufficient
❌ **Infrastructure/Deployment** - No infrastructure changes needed

[Explain reasoning for each decision]
```

### Step 10: Generate Technical Specification

Create a comprehensive technical spec with only relevant sections:

```markdown
# Technical Specification: [Feature Name]

**Linear Project:** [PROJECT-KEY] - [Project URL]
**Feature Spec:** [Path to feature spec]
**Date:** [Current Date]
**Author:** Generated by Claude Code
**Status:** Draft

---

## 1. Overview & Context

### 1.1 Feature Summary
[Brief description from Linear project and feature spec]

[If feature spec exists, reference key sections]

### 1.2 Related User Stories
- **[ISSUE-XX]:** [Story Title] - [URL]
  - Focus: [What this story covers]
- **[ISSUE-YY]:** [Story Title] - [URL]
  - Focus: [What this story covers]

[List all user stories with their focus areas]

### 1.3 Technical Goals
* [Goal 1: What we're achieving technically]
* [Goal 2: What we're achieving technically]
* [Goal 3: What we're achieving technically]

### 1.4 Success Criteria (Technical)
* [Criterion 1: Measurable technical outcome]
* [Criterion 2: Measurable technical outcome]
* [Criterion 3: Measurable technical outcome]

---

## 2. Architecture Overview

### 2.1 System Context

[Mermaid C4 context diagram showing how this feature fits in the system]

\`\`\`mermaid
C4Context
  title System Context - [Feature Name]

  Person(user, "User", "User persona from feature spec")
  System(system, "Your System", "The application")
  System_Ext(external, "External System", "If applicable")

  Rel(user, system, "Uses", "Protocol")
  Rel(system, external, "Integrates with", "Protocol")
\`\`\`

### 2.2 Component Architecture

[Mermaid component diagram showing internal structure]

\`\`\`mermaid
graph TB
  subgraph Frontend
    UI[UI Components]
    State[State Management]
    API_Client[API Client]
  end

  subgraph Backend
    API[API Layer]
    Service[Service Layer]
    Data[Data Layer]
  end

  subgraph External
    DB[(Database)]
    Cache[(Cache)]
  end

  UI --> State
  State --> API_Client
  API_Client -->|HTTP| API
  API --> Service
  Service --> Data
  Data --> DB
  Service --> Cache
\`\`\`

### 2.3 Key Components

#### Frontend Components
- **[Component 1]:** [Responsibility and interactions]
- **[Component 2]:** [Responsibility and interactions]

#### Backend Components
- **[Component 1]:** [Responsibility and interactions]
- **[Component 2]:** [Responsibility and interactions]

### 2.4 Data Flow

[Mermaid sequence diagram for main workflow]

\`\`\`mermaid
sequenceDiagram
  actor User
  participant UI
  participant API
  participant Service
  participant DB

  User->>UI: [Action from workflow]
  UI->>API: [API call]
  API->>Service: [Service call]
  Service->>DB: [Database operation]
  DB-->>Service: [Data]
  Service-->>API: [Response]
  API-->>UI: [JSON response]
  UI-->>User: [Display result]
\`\`\`

### 2.5 Technology Stack

| Layer | Technology | Version | Purpose |
|-------|-----------|---------|---------|
| Frontend | [Framework] | [Version] | [Purpose] |
| Backend | [Framework] | [Version] | [Purpose] |
| Database | [Database] | [Version] | [Purpose] |
| [Other] | [Technology] | [Version] | [Purpose] |

---

## 3. Data Models (Include if database changes)

### 3.1 Entity Relationship Diagram

\`\`\`mermaid
erDiagram
  ENTITY1 ||--o{ ENTITY2 : "relationship"
  ENTITY1 {
    uuid id PK
    string field1
    timestamp created_at
  }
  ENTITY2 {
    uuid id PK
    uuid entity1_id FK
    string field2
  }
\`\`\`

### 3.2 Database Schema

#### Table: [table_name]

**Purpose:** [What this table stores]

**Columns:**
| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | UUID | PRIMARY KEY, DEFAULT uuid_generate_v4() | Unique identifier |
| [field] | [type] | [constraints] | [description] |
| created_at | TIMESTAMP | NOT NULL, DEFAULT NOW() | Record creation time |
| updated_at | TIMESTAMP | NOT NULL, DEFAULT NOW() | Last update time |

**Indexes:**
- `idx_[table]_[field]` on ([field]) - [Purpose of index]

**Relationships:**
- [Relationship description]

[Repeat for each table]

### 3.3 Data Validation

**[Entity Name] Validation:**
- **[field]:** [Validation rules extracted from acceptance criteria]
  - Error message: "[Exact error message from acceptance criteria]"
- **[field]:** [Validation rules]
  - Error message: "[Exact error message]"

### 3.4 Migration Strategy

**Migration Steps:**
1. [Step 1: What to create/modify]
2. [Step 2: What to create/modify]
3. [If existing data: How to migrate it]

**Rollback Plan:**
1. [Step 1: How to revert]
2. [Step 2: How to revert]

---

## 4. API Contracts (Include if API changes)

### 4.1 API Overview

**Base URL:** `/api/v1`

**Authentication:** [Method from codebase patterns]

**Common Headers:**
```
Authorization: Bearer <token>
Content-Type: application/json
```

### 4.2 Endpoints

#### POST /[resource]

**Purpose:** [What this endpoint does - reference user story]

**Request:**
```json
{
  "field1": "string (required, [validation rules])",
  "field2": "number (optional, [validation rules])",
  "nested": {
    "field3": "string (required, [validation rules])"
  }
}
```

**Response (201 Created):**
```json
{
  "id": "uuid",
  "field1": "string",
  "field2": "number",
  "nested": {
    "field3": "string"
  },
  "created_at": "ISO-8601 timestamp",
  "updated_at": "ISO-8601 timestamp"
}
```

**Error Responses:**

**400 Bad Request** - Validation error
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "[Exact error message from acceptance criteria]",
    "details": [
      {
        "field": "field1",
        "message": "[Exact validation error]"
      }
    ]
  }
}
```

**401 Unauthorized** - Invalid/missing authentication
```json
{
  "error": {
    "code": "UNAUTHORIZED",
    "message": "Authentication required"
  }
}
```

**403 Forbidden** - Insufficient permissions
```json
{
  "error": {
    "code": "FORBIDDEN",
    "message": "[Exact error message from acceptance criteria]"
  }
}
```

**Business Logic Errors:**
- **[Scenario from acceptance criteria]:** 400, `{"error": {"code": "[CODE]", "message": "[Exact message]"}}`
- **[Scenario from acceptance criteria]:** 409, `{"error": {"code": "[CODE]", "message": "[Exact message]"}}`

[Repeat for each endpoint: GET, PUT, PATCH, DELETE]

### 4.3 Request/Response Examples

**Example: [Scenario from acceptance criteria]**

Request:
```bash
curl -X POST /api/v1/[resource] \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "field1": "example value"
  }'
```

Response:
```json
{
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "field1": "example value",
  "created_at": "2025-01-15T10:30:00Z"
}
```

---

## 5. UI Components (Include if frontend changes)

### 5.1 Component Hierarchy

```
[ParentComponent]
├── [ChildComponent1]
│   ├── [GrandchildComponent1]
│   └── [GrandchildComponent2]
├── [ChildComponent2]
└── [ChildComponent3]
```

### 5.2 Component Specifications

#### Component: [ComponentName]

**Purpose:** [What this component does - reference user story]

**Location:** `[path following project structure]`

**Props:**
```typescript
interface [ComponentName]Props {
  prop1: string; // [Description]
  prop2?: number; // [Description, optional]
  onAction: (data: ActionData) => void; // [Event handler description]
}
```

**State:**
```typescript
interface [ComponentName]State {
  field1: string; // [Description]
  field2: boolean; // [Description]
}
```

**Behavior:**
- [Behavior 1 from acceptance criteria]
- [Behavior 2 from acceptance criteria]
- [Error handling from acceptance criteria]

**Acceptance Criteria Coverage:**
- **[AC1]:** [How this component satisfies AC1]
- **[AC2]:** [How this component satisfies AC2]

[Repeat for each component]

### 5.3 Styling Approach

**Theme/Design System:** [Reference to design system if available]

**Component Styles:**
- [Styling approach from codebase: CSS Modules, styled-components, Tailwind, etc.]
- [Responsive breakpoints]
- [Accessibility considerations]

---

## 6. State Management (Include if complex state)

### 6.1 State Structure

[Based on project's state management: Redux, Vuex, Context API, Zustand, etc.]

**Global State:**
```typescript
interface [Feature]State {
  entities: Record<string, Entity>; // [Description]
  ui: {
    loading: boolean;
    error: string | null;
    selectedId: string | null;
  };
  filters: {
    // [Filter state from requirements]
  };
}
```

### 6.2 Actions/Events

```typescript
// [Action 1]: [When triggered]
interface [Action1] {
  type: '[FEATURE]/[ACTION_NAME]';
  payload: {
    // [Payload structure]
  };
}

// [Action 2]: [When triggered]
interface [Action2] {
  type: '[FEATURE]/[ACTION_NAME]';
  payload: {
    // [Payload structure]
  };
}
```

### 6.3 State Flow

\`\`\`mermaid
stateDiagram-v2
  [*] --> Idle
  Idle --> Loading: User action
  Loading --> Success: API success
  Loading --> Error: API failure
  Success --> Idle: Reset
  Error --> Idle: Retry
\`\`\`

### 6.4 Side Effects

**Async Operations:**
- **[Operation 1]:** [API call, data source]
- **[Operation 2]:** [API call, data source]

**State Persistence:**
- [What state persists, where (localStorage, sessionStorage, etc.)]

---

## 7. Integration Points (Include if third-party integrations)

### 7.1 External Services

#### [Service Name]

**Purpose:** [Why we integrate with this service]

**Integration Method:** [REST API, SDK, Webhook, etc.]

**Authentication:** [How we authenticate]

**Endpoints Used:**
- **[Endpoint 1]:** [Purpose]
- **[Endpoint 2]:** [Purpose]

**Data Flow:**
\`\`\`mermaid
sequenceDiagram
  participant System
  participant ExternalService

  System->>ExternalService: [Request]
  ExternalService-->>System: [Response]
\`\`\`

**Error Handling:**
- **Service Unavailable:** [Fallback strategy]
- **Rate Limiting:** [Retry strategy]
- **Timeout:** [Timeout handling]

**Configuration:**
```typescript
{
  apiKey: string; // From environment variable
  baseUrl: string; // From environment variable
  timeout: number; // 30000ms
  retries: number; // 3
}
```

### 7.2 Webhooks

**Webhook: [Webhook Name]**

**Trigger:** [What triggers this webhook]

**Endpoint:** `POST /webhooks/[name]`

**Payload:**
```json
{
  "event": "string",
  "data": {
    // [Event data structure]
  },
  "timestamp": "ISO-8601"
}
```

**Processing:**
1. [Step 1: Validate signature]
2. [Step 2: Process event]
3. [Step 3: Update state]

### 7.3 Message Queues/Events

**Queue: [Queue Name]**

**Purpose:** [Why this queue is needed]

**Message Format:**
```json
{
  "type": "string",
  "payload": {
    // [Message payload]
  }
}
```

---

## 8. Security Considerations (Include if security-relevant)

### 8.1 Authentication & Authorization

**Authentication:**
- [Method: JWT, Session, OAuth, etc.]
- [Token location: Header, Cookie, etc.]
- [Token expiration and refresh strategy]

**Authorization:**
- **[Endpoint/Resource]:** Requires role: [Role name]
- **[Endpoint/Resource]:** Requires permission: [Permission name]

**Permission Matrix:**
| Resource | Action | Required Role/Permission |
|----------|--------|-------------------------|
| [Resource] | [Action] | [Role/Permission] |

### 8.2 Data Protection

**Sensitive Data:**
- **[Field]:** [Encryption method, storage approach]
- **[Field]:** [Encryption method, storage approach]

**Data in Transit:**
- HTTPS/TLS 1.2+
- Certificate pinning (if applicable)

**Data at Rest:**
- [Encryption approach for database]
- [Encryption approach for files]

### 8.3 Input Validation

**Validation Rules:**
- **[Field]:** [Server-side validation from acceptance criteria]
- **[Field]:** [Server-side validation from acceptance criteria]

**Sanitization:**
- [XSS prevention strategy]
- [SQL injection prevention (parameterized queries)]
- [CSRF protection]

### 8.4 Security Headers

```
Strict-Transport-Security: max-age=31536000; includeSubDomains
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Content-Security-Policy: [Policy]
```

### 8.5 Compliance

**[GDPR/HIPAA/SOC2/etc.]:**
- [Requirement 1 and how it's addressed]
- [Requirement 2 and how it's addressed]

**Audit Logging:**
- [What actions are logged]
- [Log retention period]
- [Log access controls]

---

## 9. Testing Strategy

### 9.1 Unit Tests

**Backend:**
- **Service Layer:**
  - Test: [Test description covering AC]
  - Test: [Test description covering AC]
- **Data Layer:**
  - Test: [Test description]
  - Test: [Test description]

**Frontend:**
- **Components:**
  - Test: [Test description covering AC]
  - Test: [Test description covering AC]
- **State Management:**
  - Test: [Test description]
  - Test: [Test description]

### 9.2 Integration Tests

**API Tests:**
- **[Endpoint]:**
  - Test: [Happy path from AC]
  - Test: [Error case from AC]
  - Test: [Edge case from AC]

**Database Tests:**
- Test: [Data persistence]
- Test: [Constraints and validations]
- Test: [Relationships]

### 9.3 End-to-End Tests

**User Flows:**
- **[Workflow from feature spec]:**
  - Given [context]
  - When [action]
  - Then [outcome from AC]

### 9.4 Test Data

**Test Fixtures:**
- [Fixture 1: Description]
- [Fixture 2: Description]

**Setup/Teardown:**
- Setup: [What to create before tests]
- Teardown: [What to clean up after tests]

### 9.5 Coverage Goals

- Unit Test Coverage: [Target %]
- Integration Test Coverage: [Target %]
- Critical Paths: 100% coverage

---

## 10. Monitoring & Observability (Include if performance-critical)

### 10.1 Key Metrics

| Metric | Description | Alert Threshold | Dashboard |
|--------|-------------|-----------------|-----------|
| [metric_name] | [What it measures] | [When to alert] | [Dashboard link] |
| api_response_time | 95th percentile response time | > 1000ms | [Link] |
| error_rate | Percentage of failed requests | > 5% | [Link] |

### 10.2 Logging

**Log Levels:**

**INFO:**
- [Event 1 to log]
- [Event 2 to log]

**WARNING:**
- [Condition 1 to log]
- [Condition 2 to log]

**ERROR:**
- [Error 1 to log with context]
- [Error 2 to log with context]

**Log Format:**
```json
{
  "timestamp": "ISO-8601",
  "level": "INFO|WARNING|ERROR",
  "service": "service-name",
  "trace_id": "uuid",
  "message": "log message",
  "context": {
    "user_id": "uuid",
    "action": "action-name"
  }
}
```

### 10.3 Alerts

**Alert: [Alert Name]**
- **Condition:** [When to fire]
- **Severity:** [Critical/Warning/Info]
- **Action:** [What to do when fired]

### 10.4 Tracing

**Distributed Tracing:**
- [Tracing tool: Jaeger, Zipkin, etc.]
- [What operations to trace]
- [Sampling rate]

---

## 11. Infrastructure/Deployment (Include if infrastructure changes)

### 11.1 Infrastructure Changes

**New Services:**
- **[Service Name]:**
  - Type: [Container, Lambda, etc.]
  - Resources: [CPU, Memory, Disk]
  - Scaling: [How it scales]

**Database Changes:**
- [Migration requirements]
- [Backup strategy]
- [Downtime requirements]

### 11.2 Deployment Strategy

**Deployment Method:** [Blue/Green, Rolling, Canary]

**Deployment Steps:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Rollback Plan:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Deployment Checklist:**
- [ ] Database migrations tested
- [ ] Environment variables configured
- [ ] Feature flags set
- [ ] Monitoring dashboards updated
- [ ] Documentation updated

### 11.3 Scaling Considerations

**Horizontal Scaling:**
- [What components scale horizontally]
- [Scaling triggers]

**Vertical Scaling:**
- [What components scale vertically]
- [Resource limits]

**Bottlenecks:**
- [Potential bottleneck 1 and mitigation]
- [Potential bottleneck 2 and mitigation]

---

## 12. Open Questions & Decisions

Track unresolved technical questions:

- [ ] **Q1:** [Technical question that needs resolution]
  - **Context:** [Why this matters]
  - **Options:** [Option A vs Option B]
  - **Owner:** [Who decides]
  - **Deadline:** [When needed]

- [ ] **Q2:** [Technical question that needs resolution]
  - **Context:** [Why this matters]
  - **Options:** [Option A vs Option B]
  - **Owner:** [Who decides]
  - **Deadline:** [When needed]

[Continue with all open questions]

**Decisions Made:**
- **[Decision 1]:** [What was decided and why]
- **[Decision 2]:** [What was decided and why]

---

## 13. References

- **Linear Project:** [PROJECT-KEY] - [URL]
- **Feature Spec:** [Path to feature spec]
- **User Stories:**
  - [ISSUE-1]: [Title] - [URL]
  - [ISSUE-2]: [Title] - [URL]
- **PRD:** [Path to PRD if available]
- **Architecture Docs:** [Link to project architecture documentation]
- **Design Mockups:** [Link to mockups if available]
- **API Documentation:** [Link to API docs]
- **Meeting Transcript:** [Date of technical discussion if transcript was provided]

---

## Appendix A: Codebase Patterns

[Document existing patterns found in codebase review]

**File Structure:**
```
[Project structure relevant to this feature]
```

**Naming Conventions:**
- [Convention 1]
- [Convention 2]

**Code Examples:**
[Reference similar existing code that can be used as examples]

---

## Appendix B: Acceptance Criteria Mapping

[Map each acceptance criterion from user stories to technical implementation]

**[ISSUE-XX]: [Story Title]**

- **AC1:** [Acceptance criterion text]
  - **Implementation:** Section [X.Y] - [Component/API/Model]
  - **Testing:** Section 9.[X] - [Test description]

- **AC2:** [Acceptance criterion text]
  - **Implementation:** Section [X.Y] - [Component/API/Model]
  - **Testing:** Section 9.[X] - [Test description]

[Repeat for all stories and acceptance criteria]
```

### Step 11: Ask for Save Location

Ask user where to save the technical spec:

```markdown
Where would you like to save the technical spec?

**Option A:** `docs/specs/[project_key]/technical_spec.md` (recommended)
**Option B:** Custom path

Which would you prefer?
```

- Create directory structure if needed
- Save the spec

### Step 12: Provide Comprehensive Summary

After completing all steps, provide a detailed summary:

```markdown
✅ Technical specification created successfully!

**Feature:** [Feature Name]
**Linear Project:** [PROJECT-KEY] - [Project URL]
**Technical Spec:** `[path to technical spec]`

**Sections Included:**

**Core Sections:**
- ✅ Overview & Context
- ✅ Architecture Overview with diagrams
- ✅ Testing Strategy
- ✅ Open Questions & Decisions
- ✅ References

**Optional Sections:**
[List which optional sections were included with brief reasoning]
- ✅ Data Models: [N] tables defined for [entities]
- ✅ API Contracts: [N] endpoints specified
- ✅ UI Components: [N] components specified
- ✅ Security Considerations: Covers [auth/data protection/etc.]
- ❌ State Management: Not needed (simple state)
- ❌ Monitoring: Standard monitoring sufficient

**Contents Summary:**
- [N] user stories covered with AC mapping
- [N] Mermaid diagrams (architecture, data flow, state, etc.)
- [N] API endpoints with complete request/response specs
- [N] database tables with schema and migrations
- [N] UI components with props and behavior
- [N] open technical questions to resolve

**Codebase Alignment:**
- Follows existing [architecture pattern] pattern
- Uses established [technology] stack
- Matches [coding conventions] conventions
- Integrates with [existing components]

**Next Steps:**
1. Review technical spec and resolve open questions (Section 12)
2. Share with development team for technical review
3. When ready to break into stories: `/decompose-feature [PROJECT-KEY]`
4. After stories created, start implementation: `/plan-user-story [ISSUE-ID]`

**Open Technical Questions:**
[List questions from Section 12 that need resolution]

This technical spec is ready for team review and provides complete implementation guidance following your project's established patterns.
```

## Guidelines

### Conversational Best Practices

1. **Check State First**: Always show current project state before asking questions
2. **Acknowledge Input**: Summarize what you found in transcripts before asking questions
3. **Explain Decisions**: When selecting sections, explain why you included/excluded them
4. **Review Codebase**: Always check existing patterns before asking questions
5. **Be Specific**: Ask concrete technical questions, not vague ones
6. **Reference ACs**: Connect technical decisions to acceptance criteria
7. **Provide Context**: Explain why you need certain information

### Transcript Analysis Tips

1. **Extract Decisions**: Look for architecture decisions, technology choices, patterns
2. **Note Trade-offs**: If transcript discusses pros/cons, capture both perspectives
3. **Identify Constraints**: Extract technical constraints and limitations
4. **Find Patterns**: Look for mentions of existing code to reuse
5. **Spot Gaps**: Identify technical details not discussed but needed

### Technical Spec Quality

1. **Use Actual Names**: No placeholders - use real field names, endpoint paths, component names
2. **Extract Error Messages**: Get exact error messages from acceptance criteria
3. **Follow Patterns**: Match existing codebase patterns and conventions
4. **Be Complete**: Include all sections needed, exclude irrelevant ones
5. **Map to ACs**: Every AC should map to implementation and tests
6. **Include Diagrams**: Use Mermaid for architecture, data flow, state, ERD
7. **Specify Exactly**: API contracts should have complete request/response with validation

### Smart Section Selection

1. **Analyze Before Deciding**: Review feature type, user stories, and transcript
2. **Include Only What's Needed**: Don't add sections just to be thorough
3. **Explain Reasoning**: Document why sections were included/excluded
4. **Cover Requirements**: Ensure all acceptance criteria are addressed somewhere
5. **Match Feature Type**: Backend features need different sections than frontend

### Codebase Review

1. **Find Patterns**: Look for similar existing features
2. **Extract Conventions**: Naming, structure, testing approaches
3. **Identify Reusable Code**: Components, utilities, services to reuse
4. **Understand Stack**: Framework versions, libraries, tools in use
5. **Match Style**: Follow existing code style and architecture

### Question Strategy

**Backend/API Features - Ask About:**
- Data model design
- API endpoint structure
- Authentication/authorization approach
- Error handling strategy
- Performance requirements
- Caching strategy

**Frontend Features - Ask About:**
- Component hierarchy
- State management approach
- User experience details
- Data fetching strategy
- Loading and error states

**Integration Features - Ask About:**
- External service selection
- Integration pattern (sync/async)
- Error/failure handling
- Data mapping
- Retry/fallback strategy

## Error Handling

If something goes wrong:

1. **No Feature Spec**: Warn but continue using Linear project description
2. **No User Stories**: Warn that decomposition should happen first, but continue
3. **Can't Determine Sections**: Ask user which sections they want
4. **Incomplete Transcript**: Identify gaps and ask targeted questions
5. **No Codebase Access**: Proceed without pattern matching, ask more questions

## Important Notes

- **Requires $ARGUMENTS**: Must provide Linear Project ID
- **Transcript is Optional**: Preferred but can work conversationally
- **Smart Section Selection**: Only include relevant sections, explain reasoning
- **Codebase Integration**: Always review existing code to match patterns
- **AC Mapping**: Every acceptance criterion should map to implementation
- **Multiple Interaction Points**: Check state, analyze transcript, ask questions, confirm sections
- **Diagrams Required**: Always include Mermaid diagrams for architecture and data flow

This conversational approach ensures the technical spec is comprehensive, follows project conventions, and provides clear implementation guidance while being engaging and collaborative.
