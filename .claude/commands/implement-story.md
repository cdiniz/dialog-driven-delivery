---
description: Orchestrate TDD implementation, review, and refinement workflow
---

Orchestrate the complete development workflow to implement a story $ARGUMENTS.

# Orchestration Plan

1. Use the subagent story developer to work on  $ARGUMENTS
2. Use the subagent story-reviewer to review the code changes for the story $ARGUMENTS
3. Use the subagent refinement-developer to work on the review for the story $ARGUMENTS

**Completion Criteria**

1. All agents finished their job successfully, all tasks from the plan are implemented
2. All tests are passing [# of tests] passing = [# of tests] in the project

IMPORTANT: You should NEVER try to justify that some tests are not passing.

If there are failing tests, you MUST ask the test-fix-specialist to fix them, until you confirm ALL TESTS are passing.
