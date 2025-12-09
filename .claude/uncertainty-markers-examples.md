# Uncertainty Marker Examples

Real-world examples showing how to use uncertainty markers in spec-driven development.

---

## Example 1: Feature Spec with Mixed Uncertainties

### Scenario
User provides a meeting transcript about a "Task Assignment" feature but doesn't answer all clarifying questions about notification strategy and assignment limits.

### Generated Feature Spec Excerpt

```markdown
## 3. Functional Requirements

### 3.1 Core Functionality

* **FR1:** Users can assign tasks to [OPEN QUESTION: single user or multiple users?]
  - Assignment UI shows [CLARIFICATION NEEDED: dropdown, autocomplete, or multi-select component?]
  - Notification sent to assignee(s) via [DECISION PENDING: email, in-app, or both - see Q2]
  - Assignment history tracked with [ASSUMPTION: timestamps and user IDs based on audit pattern in codebase]

* **FR2:** Task assignee can reassign to another user
  - Reassignment creates [ASSUMPTION: audit log entry following existing audit trail pattern]
  - Previous assignee receives [OPEN QUESTION: notification of reassignment?]
  - Task status [ASSUMPTION: remains unchanged during reassignment based on current workflow]

### 3.2 Validation Rules

* **VR1:** Assignee - Must be [ASSUMPTION: active project member based on current permission model]
  - Error message: "Selected user is not a member of this project"
  - [CLARIFICATION NEEDED: Should we allow assigning to deactivated users? What error message?]

* **VR2:** Assignment Limit - [OPEN QUESTION: Maximum number of assignees per task?]
  - If limit exists: Error message: [CLARIFICATION NEEDED: exact wording]
```

### Section 7: Open Questions

```markdown
## 7. Open Questions

- [ ] **Q1:** Can tasks be assigned to a single user or multiple users?
  - **Owner:** Product Manager
  - **Deadline:** Before technical design
  - **Context:** Referenced in FR1, affects UI component choice and data model
  - **Options:**
    - Single assignee (simpler, matches most competitors)
    - Multiple assignees (more flexible, increases complexity)

- [ ] **Q2:** How should we notify assignees?
  - **Owner:** Product Manager
  - **Deadline:** Before implementation
  - **Context:** Referenced in FR1, affects notification service integration
  - **Options:**
    - Email only (simple, reliable)
    - In-app only (no external dependency)
    - Both email and in-app (best UX, more complexity)

- [ ] **Q3:** Should previous assignee be notified when task is reassigned?
  - **Owner:** Product/UX
  - **Deadline:** Before UI design
  - **Context:** Referenced in FR2, affects notification logic

- [ ] **Q4:** What is the maximum number of assignees allowed per task?
  - **Owner:** Product Manager
  - **Deadline:** Before technical design (depends on Q1 answer)
  - **Context:** Referenced in VR2, affects validation and UI

- [ ] **Q5:** Can tasks be assigned to deactivated users? What error should we show?
  - **Owner:** Product/Engineering
  - **Deadline:** Before implementation
  - **Context:** Referenced in VR1, affects validation logic
```

### Section 10: Appendix > Assumptions

```markdown
### Assumptions

1. **Audit Trail Pattern:** We assume task assignments create audit log entries following the existing pattern in `src/services/audit.ts` which logs user ID, timestamp, action, and entity. This maintains consistency with other audited actions. Needs validation that assignment events follow same structure.

2. **Project Membership Scope:** We assume only active project members can be assigned tasks, following the permission model in `src/auth/permissions.ts`. This prevents assigning to external users or deactivated accounts. Needs validation with security requirements.

3. **Status Preservation:** We assume task status remains unchanged during reassignment, based on the current workflow where status and ownership are independent. This means reassigning an "In Progress" task keeps it "In Progress." Needs validation with product requirements for workflow rules.
```

---

## Example 2: Technical Spec with Architecture Decisions

### Scenario
Creating technical spec for the Task Assignment feature. Database choice has been made but notification implementation approach is still undecided.

### Generated Technical Spec Excerpt

```markdown
## 4. Data Models

### 4.1 Task Assignments

Data will be stored in [ASSUMPTION: PostgreSQL based on existing stack] with the following schema:

```typescript
// Based on answer to Open Question Q1: Multiple assignees chosen
interface TaskAssignment {
  id: string;
  taskId: string; // FK to tasks table
  userId: string; // FK to users table
  assignedAt: Date;
  assignedBy: string; // FK to users table
  isActive: boolean; // For reassignment tracking
  // [ASSUMPTION: Using soft delete pattern per codebase standard]
}
```

**Table: task_assignments**
```sql
CREATE TABLE task_assignments (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  task_id UUID NOT NULL REFERENCES tasks(id) ON DELETE CASCADE,
  user_id UUID NOT NULL REFERENCES users(id),
  assigned_at TIMESTAMP NOT NULL DEFAULT NOW(),
  assigned_by UUID NOT NULL REFERENCES users(id),
  is_active BOOLEAN NOT NULL DEFAULT true,
  created_at TIMESTAMP NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_task_assignments_task_id ON task_assignments(task_id);
CREATE INDEX idx_task_assignments_user_id ON task_assignments(user_id);
-- [ASSUMPTION: Following existing index naming pattern from migrations/]
```

**Rationale:** Separate assignment table allows:
- Multiple assignees per task
- Historical tracking of all assignments
- Efficient queries for "tasks assigned to user"

## 5. API Contracts

### 5.1 POST /api/tasks/:taskId/assignments

Assign user(s) to a task.

**Request:**
```json
{
  "userIds": ["uuid1", "uuid2"], // Array supports multiple assignees
  "notifyAssignees": true // [DECISION PENDING: notification method - see Q3]
}
```

**Response:**
- Success: 201 Created
  ```json
  {
    "assignments": [
      {
        "id": "uuid",
        "taskId": "uuid",
        "userId": "uuid1",
        "assignedAt": "2025-01-09T10:00:00Z",
        "assignedBy": "current-user-uuid"
      }
    ],
    "notificationsSent": [DECISION PENDING: depends on notification approach - see Q3]
  }
  ```
- Validation Error: 400 Bad Request
- Authorization Error: 403 Forbidden

**Business Logic:**
1. Validate user has permission to assign tasks in this project
2. Validate all userIds are active project members
3. Validate assignment limit [ASSUMPTION: no limit for MVP based on product decision]
4. Create task_assignments records
5. [DECISION PENDING: Send notifications - implementation depends on Q3]
6. Create audit log entries [ASSUMPTION: using AuditService from src/services/audit.ts]

## 8. Integrations

### 8.1 Notification Service

**Service:** [DECISION PENDING: Email service choice - see Q4]

**Integration Approach:**

[DECISION PENDING: The entire notification implementation approach depends on unresolved questions. Options:]

**Option A: Email Only (Simple)**
- Use [DECISION PENDING: SendGrid vs AWS SES vs existing email service - see Q4]
- Template: "You've been assigned to task '{taskTitle}' by {assignerName}"
- Error handling: Log failure, don't block assignment
- [ASSUMPTION: Async sending via message queue based on existing pattern]

**Option B: In-App Only (No External Dependency)**
- Create notification records in database
- Real-time delivery via [ASSUMPTION: WebSocket connection per existing notification pattern]
- No external service dependency
- [ASSUMPTION: Using existing NotificationService from src/services/notifications.ts]

**Option C: Both Email and In-App (Best UX)**
- Combine both approaches above
- User preferences control delivery method [CLARIFICATION NEEDED: notification preferences UI?]
- Fallback: If email fails, in-app notification still works

## 12. Open Questions & Decisions

- [ ] **Q3:** How should we implement notifications for task assignment?
  - **Context:** Affects API response, external service integration, error handling
  - **Options:**
    - Option A (Email Only): Simple, requires email service integration
      - Pros: Reliable, users get notification even offline
      - Cons: Requires email service, can fail, slower
    - Option B (In-App Only): No external dependency, real-time
      - Pros: Fast, no external service cost, uses existing WebSocket
      - Cons: User must be online, no notification if user doesn't log in
    - Option C (Both): Best UX, more complexity
      - Pros: Covers all use cases, reliable + fast
      - Cons: More code, more potential failure points
  - **Owner:** Tech Lead / Product Manager
  - **Deadline:** Before sprint planning
  - **Referenced in:** Section 5.1 (API Contracts), Section 8.1 (Integrations)

- [ ] **Q4:** If we choose email notifications, which email service?
  - **Context:** Depends on Q3 answer; affects cost, setup, reliability
  - **Options:**
    - SendGrid (dedicated email service, good deliverability)
    - AWS SES (cheaper, may need warm-up period)
    - Existing email service (if we already have one integrated)
  - **Owner:** Tech Lead / DevOps
  - **Deadline:** Before sprint planning (only if Q3 = email)
  - **Referenced in:** Section 8.1 (Integrations)

**Decisions Made:**

- **Multiple Assignees:** Task can have multiple assignees (resolved from Feature Spec Q1)
  - **Rationale:** Flexibility requested by product team for collaborative tasks
  - **Tradeoffs:** More complex UI and data model, but matches user needs
  - **Alternatives Considered:** Single assignee only - simpler but too restrictive

- **PostgreSQL for Storage:** Use existing PostgreSQL database
  - **Rationale:** Matches existing stack, relational data fits well, team expertise
  - **Tradeoffs:** N/A - this is the established pattern
  - **Alternatives Considered:** None - following established architecture

## Appendix A: Technical Assumptions

1. **Database Choice - PostgreSQL:** We assume PostgreSQL based on the existing stack found in `database/config.ts` and all existing migrations. This is not an assumption but a confirmed architectural decision. Affects schema design and query patterns.

2. **Soft Delete Pattern:** We assume using `is_active` flag for "deleting" assignments (reassignment marks old assignment inactive, creates new active one) based on the soft delete pattern used throughout the codebase in `users`, `projects`, and `tasks` tables. This maintains history and enables audit trails. Validate pattern is desired for assignments.

3. **Audit Service Integration:** We assume using the existing `AuditService` from `src/services/audit.ts` for logging assignment events, following the pattern used for task creation, updates, and deletions. This maintains consistent audit trail. Validate that assignment events should be audited the same way.

4. **Index Naming Convention:** We assume following the existing index naming pattern `idx_{table}_{column}` found in existing migrations. This maintains consistency in database schema. No validation needed - just following convention.

5. **Async Message Queue:** We assume using existing message queue (RabbitMQ found in `src/queue/`) for async notification sending to avoid blocking API responses, following pattern used for email notifications in other features. Validate that notification sending should be async.

6. **WebSocket for Real-Time:** If choosing in-app notifications, we assume using the existing WebSocket infrastructure in `src/websocket/` that's already used for real-time updates. This avoids adding new infrastructure. Validate existing WebSocket can handle notification delivery.
```

---

## Example 3: User Story with Referenced Uncertainties

### Scenario
Creating a story for task assignment where the notification method is still undecided in the technical spec.

### Generated User Story

```markdown
## User Story
As a project manager,
I want to assign tasks to team members,
So that I can delegate work and track ownership.

## User Value Statement
This enables project managers to distribute work efficiently and provides team members with clear ownership and accountability for tasks. Supports the core workflow of collaborative project management.

## Context
This story implements the core task assignment functionality from the "Task Assignment" feature (PROJ-123). It covers the end-to-end workflow of selecting and assigning one or more users to a task.

## Acceptance Criteria

### AC1: Assign single user to an unassigned task
- **Given** I am a project manager viewing task "Review designs"
- **And** the task currently has no assignees
- **When** I click "Assign"
- **And** I select "John Doe" from the user list
- **And** I click "Save"
- **Then** I see the success message "Task assigned to John Doe"
- **And** "John Doe" appears as the assignee on the task
- **And** [PENDING DECISION: notification sent per Technical Spec Q3]

### AC2: Assign multiple users to a task
- **Given** I am viewing an unassigned task
- **When** I click "Assign"
- **And** I select "John Doe" and "Jane Smith"
- **And** I click "Save"
- **Then** I see "Task assigned to 2 users"
- **And** both users appear as assignees
- **And** [PENDING DECISION: notifications sent per Technical Spec Q3]

### AC3: Validation error when assigning non-project member
- **Given** I am assigning a task in "Project Alpha"
- **When** I try to select "Bob Wilson" who is not a member of "Project Alpha"
- **Then** I see the error "Selected user is not a member of this project"
- **And** the assignment is not saved
- **And** no notification is sent

### AC4: Only active project members can be assigned
- **Given** I am viewing the assignee selection UI
- **When** the user list loads
- **Then** I only see active project members
- **And** deactivated users are not shown in the list

## Technical Notes

**Architecture:**
- See Technical Spec Section 4.1: Task Assignments data model
- See Technical Spec Section 5.1: POST /api/tasks/:taskId/assignments

**API Endpoints:**
- POST /api/tasks/:taskId/assignments (create assignment)
- GET /api/projects/:projectId/members (list assignable users)

**Data Models:**
- task_assignments table
- Updates tasks table (assigned_at timestamp)

**UI Components:**
- AssignmentModal component (new)
- UserMultiSelect component (reuse from existing codebase)

**Dependencies:**
- Requires: User authentication and project membership system
- Blocks: PROJ-125 (Task reassignment), PROJ-126 (Assignment notifications)
- Pending Decisions: Technical Spec Q3 (notification method) - may affect AC1 and AC2

**Uncertainties:**
- **Pending Decision from Technical Spec:** See Technical Spec Section 12, Q3 - Notification implementation approach (email, in-app, or both)
- **Impact:** Acceptance criteria AC1 and AC2 reference notifications but exact behavior depends on Q3 resolution. May need to add specific ACs for notification delivery and error handling once decision is made. Story can be implemented for happy path, notification details can be refined in PROJ-126 (dedicated notification story).

## Definition of Done

- [ ] All acceptance criteria pass
- [ ] Unit tests written and passing
- [ ] Integration tests written and passing (API + database)
- [ ] Code reviewed and approved
- [ ] No linting errors
- [ ] Accessibility requirements met (keyboard navigation, screen reader support)
- [ ] Notification implementation follows decision from Tech Spec Q3 (or deferred to PROJ-126)
- [ ] Documentation updated (API docs for new endpoint)
- [ ] Deployed to staging and verified

## References

- **Confluence Feature:** Task Assignment Feature
- **Jira Epic:** Task Assignment Feature
- **Related Stories:**
  - PROJ-125: Task Reassignment (depends on this story)
  - PROJ-126: Assignment Notifications (notification details if complex)
```

---

## Example 4: Before vs After - Preventing Hallucination

### ❌ BEFORE (Silent Assumptions - Bad)

```markdown
## 3. Functional Requirements

### 3.1 Core Functionality

* **FR1:** Users can create tasks with title, description, and due date
  - Title: Required, max 255 characters
  - Description: Optional, supports Markdown formatting
  - Due date: Optional, must be future date
  - Priority: Required, values: Low, Medium, High, Urgent
  - Tags: Optional, max 10 tags per task
```

**Problem:** User never mentioned:
- Max length for title (255 chars is assumed)
- Markdown support (assumed)
- Future date validation (assumed)
- Priority field or values (completely hallucinated)
- Tag limit (assumed)

### ✅ AFTER (Explicit Uncertainties - Good)

```markdown
## 3. Functional Requirements

### 3.1 Core Functionality

* **FR1:** Users can create tasks with title, description, and due date
  - Title: Required, [CLARIFICATION NEEDED: max length? 100 chars, 255 chars, or unlimited?]
  - Description: Optional, [OPEN QUESTION: plain text only or rich text/Markdown support?]
  - Due date: Optional, [ASSUMPTION: must be today or future date, not past dates]
  - Priority: [OPEN QUESTION: Is priority field needed? If yes, what values?]
  - Tags: [OPEN QUESTION: Can tasks be tagged? If yes, max number of tags?]
```

**Result:** User is prompted to answer these questions, preventing incorrect assumptions from becoming implementation requirements.

---

## Key Takeaways

1. **Inline markers make uncertainties visible** - Readers immediately see what's not decided
2. **Tracking in dedicated sections** - Open Questions and Assumptions sections provide complete context
3. **Linked markers** - Every inline marker has a corresponding tracked entry
4. **Stories reference uncertainties** - Implementation knows what might change
5. **Quality gates** - Specs can't proceed with too many unresolved questions
6. **Better than hallucination** - Explicit uncertainty is far better than plausible-sounding fiction

When in doubt: **Mark it, track it, resolve it.**
