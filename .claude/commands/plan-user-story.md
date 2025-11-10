---
description: Generate TDD task list for user story implementation
---

Generate a TDD-focused implementation task list for user story $ARGUMENTS and save it to the project's documentation structure.

## Steps

1. **Query Story**: Get story details from Linear (use story ID like "PROJ-42" or just "42")
2. **Get Project Context**: Get the Linear project (feature) that this story belongs to
3. **Find Feature Spec**: Look for the feature specification document for this project
4. **Find Technical Spec**: Locate and read the technical spec for this feature
5. **Find Mockups**: Look for relevant UI mockups or design files
6. **Analyze Codebase**: Identify existing patterns, architecture, and integration points
7. **Determine Save Location**: Ask user for preferred location or use: `docs/specs/[project_key]/story_[issue_id]_tdd_tasks.md`
8. **Generate Plan**: Create TDD task list following the template below
9. **Save Plan**: Create necessary directories and save the plan

## TDD Task List Template

<plan_template>
# TDD Implementation Tasks: [Story Title]

**Story:** [ISSUE-ID] - [Story Title]
**Linear Project:** [PROJECT-KEY] - [Project URL]
**Feature:** [Feature Name]
**Date:** [Current Date]

---

## Story Overview

**Description:**
[Story description from Linear]

**Acceptance Criteria:**
- [ ] [AC 1 from Linear]
- [ ] [AC 2 from Linear]
- [ ] [AC 3 from Linear]

**Integration Points:**
- Backend: [Existing services/modules this story will touch]
- Frontend: [Existing components/pages this story will modify]
- External: [Third-party APIs or services if applicable]

**Related Mockups:** `[relevant mockup files or design links]`
**Feature Spec:** `[path to feature spec]`
**Technical Spec:** `[path to technical spec]` - Section [X]

---

## Prerequisites

- [ ] Database migration created and tested
- [ ] Domain models defined (if new entities needed)
- [ ] API contracts defined in technical spec
- [ ] Mock data prepared for testing
- [ ] ...

---

## TDD Task List

### Backend Tasks

> **Note:** Adjust file paths and testing approaches based on your project's structure and architecture (e.g., MVC, hexagonal, layered, etc.)

#### Task 1: [Data Model / Business Logic]
**File:** `[path to model/entity file]`

**Tests to Write (RED):**
- [ ] Test: Create test file following project conventions
- [ ] Test: `test_[model]_creation_with_valid_data`
- [ ] Test: `test_[model]_validation_fails_with_[invalid_case]`
- [ ] Test: `test_[business_rule_method]_returns_expected_result`

**Implementation (GREEN):**
- [ ] Create model/entity file
- [ ] Implement validation methods
- [ ] Implement business logic methods
- [ ] Run tests - all should pass, iterate the implementation till everything passes

**Refactor:**
- [ ] Extract common validation logic if applicable
- [ ] Add type hints/annotations if applicable
- [ ] Ensure no code duplication

---

#### Task 2: [External Integration / Data Access]
**File:** `[path to integration/repository file]`

**Tests to Write (RED):**
- [ ] Test: Create test file following project conventions
- [ ] Test: `test_[method_name]_success_case`
- [ ] Test: `test_[method_name]_handles_external_error`
- [ ] Test: `test_[method_name]_with_[edge_case]`
- [ ] Setup: Use appropriate test doubles (containers, mocks, stubs)

**Implementation (GREEN):**
- [ ] Create integration/repository file
- [ ] Implement method `[method_name]()`
- [ ] Add error handling for external failures
- [ ] Run tests - all should pass, iterate the implementation till everything passes

**Refactor:**
- [ ] Extract connection logic if reusable
- [ ] Simplify error handling
- [ ] Add proper logging

---

#### Task 3: [Business Logic / Use Case / Controller]
**File:** `[path to service/controller file]`

**Tests to Write (RED):**
- [ ] Test: Create test file following project conventions
- [ ] Test: `test_[use_case]_success`
- [ ] Test: `test_[use_case]_handles_[error_condition]`
- [ ] Test: `test_[use_case]_validates_[business_rule]`
- [ ] Setup: Mock dependencies appropriately

**Implementation (GREEN):**
- [ ] Create service/controller file
- [ ] Add dependency injection if applicable
- [ ] Implement use case/business method
- [ ] Run tests - all should pass

**Refactor:**
- [ ] Extract common orchestration logic
- [ ] Simplify conditional logic
- [ ] Ensure single responsibility

---

#### Task 4: [API Endpoint / Route Handler]
**File:** `[path to endpoint/route file]`

**Tests to Write (RED):**
- [ ] Test: Create integration test file
- [ ] Test: `test_[endpoint]_returns_success_with_valid_request`
- [ ] Test: `test_[endpoint]_returns_error_with_invalid_request`
- [ ] Test: `test_[endpoint]_handles_authentication_properly`
- [ ] Test: `test_[endpoint]_returns_expected_response_structure`
- [ ] Setup: Use HTTP client with appropriate test database/fixtures

**Implementation (GREEN):**
- [ ] Create endpoint/route handler
- [ ] Define request/response schemas
- [ ] Implement endpoint logic
- [ ] Add authentication/authorization
- [ ] Register route in application
- [ ] Run tests - all should pass

**Refactor:**
- [ ] Extract common request validation
- [ ] Simplify response formatting
- [ ] Add API documentation

---

### Frontend Tasks

> **Note:** Adjust file paths and testing approaches based on your project's frontend framework (React, Vue, Angular, etc.) and state management approach

#### Task 5: [API/Service Layer]
**File:** `[path to service file]`

**Tests to Write (RED):**
- [ ] Test: Create test file following project conventions
- [ ] Test: `test_[serviceFunction]_calls_correct_endpoint`
- [ ] Test: `test_[serviceFunction]_handles_success_response`
- [ ] Test: `test_[serviceFunction]_handles_error_response`
- [ ] Setup: Mock HTTP client (fetch/axios/etc.)

**Implementation (GREEN):**
- [ ] Create service file
- [ ] Implement function `[serviceFunction]()`
- [ ] Add types/interfaces for request/response
- [ ] Run tests - all should pass

**Refactor:**
- [ ] Extract common API call logic
- [ ] Simplify error handling
- [ ] Add documentation comments

---

#### Task 6: [Data Fetching / State Management]
**File:** `[path to hook/store/composable file]`

**Tests to Write (RED):**
- [ ] Test: Create test file following project conventions
- [ ] Test: `test_[function]_loads_data_successfully`
- [ ] Test: `test_[function]_handles_loading_state`
- [ ] Test: `test_[function]_handles_error_state`
- [ ] Test: `test_[function]_refetches_on_[trigger]`
- [ ] Setup: Use appropriate testing utilities, mock service

**Implementation (GREEN):**
- [ ] Create data fetching/state management file
- [ ] Implement data fetching logic
- [ ] Handle loading, error, and success states
- [ ] Configure caching/retry logic if applicable
- [ ] Run tests - all should pass

**Refactor:**
- [ ] Extract common configuration
- [ ] Simplify state management logic
- [ ] Add documentation comments

---

#### Task 7: [UI Component]
**File:** `[path to component file]`
**Story:** [ISSUE-ID]
**Mockup:** `[mockup reference]`

**Tests to Write (RED):**
- [ ] Test: Create component test file
- [ ] Test: `test_renders_[component]_with_required_props`
- [ ] Test: `test_displays_loading_state_while_fetching`
- [ ] Test: `test_displays_error_message_on_failure`
- [ ] Test: `test_user_can_[interaction]`
- [ ] Test: `test_calls_[callback]_on_[event]`
- [ ] Setup: Mock data fetching/state management

**Implementation (GREEN):**
- [ ] Create component file
- [ ] Implement UI based on mockup/design
- [ ] Integrate data fetching/state management
- [ ] Add loading and error states
- [ ] Add form validation (if applicable)
- [ ] Run tests - all should pass

**Refactor:**
- [ ] Extract reusable sub-components
- [ ] Simplify conditional rendering
- [ ] Ensure accessibility (ARIA labels, keyboard navigation)
- [ ] Add internationalization for all user-facing strings

---

#### Task 8: [Integration & Routing]
**File:** `[path to router/app config]`

**Tests to Write (RED):**
- [ ] Test: Create integration test file
- [ ] Test: `test_user_can_navigate_to_[feature]`
- [ ] Test: `test_[feature]_integrates_with_[existing_component]`
- [ ] Test: `test_full_user_flow_[scenario]`
- [ ] Setup: Full application context, mock backend

**Implementation (GREEN):**
- [ ] Add route in router configuration
- [ ] Add navigation links in appropriate components
- [ ] Verify route guards/auth checks
- [ ] Run tests - all should pass

**Refactor:**
- [ ] Extract common route configuration
- [ ] Simplify navigation structure
- [ ] Ensure consistent navigation patterns

---

### Documentation

#### Task 9: [Documentation]
- [ ] Update API documentation with new endpoints/changes
- [ ] Add inline comments for complex logic
- [ ] Update architecture documentation if new patterns introduced
- [ ] Create/update user documentation (if needed)
- [ ] Document any deviations from the original plan

---

## TDD Principles Reminder

For each task, follow the **Red-Green-Refactor** cycle:

1. **RED:** Write a failing test first
   - Think about the interface/API before implementation
   - Test describes the desired behavior
   - Run test - it should fail

2. **GREEN:** Write minimal code to make the test pass
   - Don't worry about perfection
   - Focus on making the test pass
   - Run test - it should pass

3. **REFACTOR:** Improve the code without changing behavior
   - Clean up duplication
   - Improve naming
   - Simplify logic
   - Run test - it should still pass

**Key Rules:**
- Never write production code without a failing test
- Write the simplest test that could possibly fail
- Write the simplest code that could possibly pass
- Refactor only when needed and only when tests are green

---

## Task Tracking

### Completed Tasks
- [ ] Task 1: [Data Model / Business Logic]
- [ ] Task 2: [External Integration / Data Access]
- [ ] Task 3: [Business Logic / Use Case / Controller]
- [ ] Task 4: [API Endpoint / Route Handler]
- [ ] Task 5: [API/Service Layer]
- [ ] Task 6: [Data Fetching / State Management]
- [ ] Task 7: [UI Component]
- [ ] Task 8: [Integration & Routing]
- [ ] Task 9: [Documentation]

### Notes & Blockers
[Space for notes, decisions, and blockers during implementation]

---

## Success Criteria

- [ ] All acceptance criteria from story are met
- [ ] All tests pass (unit, integration, e2e as applicable)
- [ ] No linter/formatter errors
- [ ] UI matches design/mockups (if applicable)
- [ ] Internationalization implemented for all user-facing text (if applicable)
- [ ] Performance meets project requirements
- [ ] Accessibility standards met (if applicable)
- [ ] Security requirements satisfied

---

## References

- **Story:** [ISSUE-ID] - [Linear story URL]
- **Linear Project:** [PROJECT-KEY] - [Linear project URL]
- **Feature Spec:** `[path to feature spec]`
- **Technical Spec:** `[path to technical spec]`
- **UI Mockups/Designs:** `[path to mockups or design links]`
- **Architecture Docs:** `[path to architecture documentation]`

</plan_template>

## Guidelines

- **Test First:** Every task starts with writing tests (RED phase)
- **Minimal Implementation:** Write just enough code to pass tests (GREEN phase)
- **Refactor Continuously:** Clean up code after tests pass (REFACTOR phase)
- **Be Specific:** Reference exact file paths and test names
- **Follow Patterns:** Point to existing tests as examples
- **Keep Tasks Small:** Each task should be completable in 1-2 hours
- **Map to Acceptance Criteria:** Each task should directly support an acceptance criterion from the story

## Output

After generating and saving the TDD task list:

```markdown
Generated TDD task list for Story [ISSUE-ID]:

**Story:** [ISSUE-ID] - [Story Title]
**Linear Project:** [PROJECT-KEY] - [Feature Name]
**Location:** `[path where plan was saved]`

**Summary:**
- [N] TDD tasks identified
- [N] test files to create
- [N] implementation files to create
- Estimated effort: [X] hours/days

**Acceptance Criteria:**
- [ ] [AC 1]
- [ ] [AC 2]
- [ ] [AC 3]

**TDD Workflow:**
Each task follows Red → Green → Refactor cycle:
1. Write failing tests (RED)
2. Implement minimal code (GREEN)
3. Refactor and improve (REFACTOR)

Next steps:
1. Review the task list with team/stakeholders
2. Run `/implement-story [path to plan]` to start implementation
3. Or manually start with Task 1 and work through tasks sequentially
4. Follow TDD discipline strictly
5. Update story status in Linear as work progresses
```
