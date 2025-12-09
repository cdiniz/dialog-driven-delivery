# Coding & Implementation Workflow

A comprehensive guide for implementing user stories from Jira through to merged code, based on pragmatic development practices with AI assistance.

**Context:** This workflow complements the [Spec-Driven Product Development Workflow](SPEC_README.md) and focuses specifically on the coding/implementation phase (Steps 4-5 in the overall process).

---

## Philosophy

This coding workflow is built on **pragmatic engineering principles**:

1. **Quality First**: Tests before merge, all tests passing, no skipped tests
2. **Iterative Development**: Implement, test, review, refine
3. **Clean Commits**: Meaningful commit messages with context
4. **Collaborative Review**: Address feedback systematically
5. **Continuous Integration**: Keep main branch stable and up-to-date
6. **Architecture Compliance**: Follow established patterns and guidelines
7. **Test-Driven Mindset**: Comprehensive test coverage with proper assertions
8. **Security Conscious**: No vulnerabilities, proper error handling

---

## Prerequisites

Before starting implementation:

- **Jira Story**: Well-defined user story with acceptance criteria
- **Feature Spec**: Confluence page with product and technical specifications
- **Development Environment**: Local environment set up and running
- **Git**: Clean working directory on main branch
- **Tests Passing**: All existing tests passing before starting

---

## Development Flow

### High-Level Process

```
Jira Story (with ACs)
        ↓
/implement-story (fetch story + spec, create plan)
        ↓
Create Feature Branch
        ↓
Implement Code + Tests
        ↓
Run Tests Locally (all must pass)
        ↓
/manual-test-story (verify ACs in browser)
        ↓
/commit-and-open-pr
        ↓
Code Review & Feedback
        ↓
/address-pr-feedback (iteratively)
        ↓
Merge to Main
        ↓
Delete Feature Branch
```

---

## Step-by-Step Implementation Guide

### Step 1: Start Implementation

**Command:** `/implement-story`

**What it does:**
1. Asks for Jira story link and Confluence spec link
2. Fetches story details and acceptance criteria from Jira
3. Fetches technical context from Confluence spec
4. Creates an implementation plan based on:
   - Acceptance criteria from Jira
   - Technical specifications from Confluence
   - Existing codebase patterns and architecture
5. Creates feature branch following naming convention
6. Begins implementation following the plan

**Example:**
```
You: /implement-story

Agent: Please provide:
       1. Jira story link (e.g., https://yoursite.atlassian.net/browse/BOOT-8)
       2. Confluence feature spec link

You: https://yoursite.atlassian.net/browse/BOOT-8
     https://yoursite.atlassian.net/wiki/spaces/BOOT/pages/7864324/

Agent: ✅ Fetched BOOT-8: Individual Product Detail Page
       ✅ Fetched feature spec: Product Navigation and Browsing

       Creating implementation plan...

       **Implementation Plan:**
       1. Backend verification (endpoint already exists)
       2. Create useProduct hook for data fetching
       3. Implement ProductDetailPage component
       4. Add navigation from ProductCard
       5. Add route to App.tsx
       6. Write comprehensive tests

       Creating branch: BOOT-8-product-detail-page

       Starting implementation...
```

**Best Practices:**
- Review the implementation plan before proceeding
- Ensure the plan covers all acceptance criteria
- Check that the plan follows project architecture guidelines
- Ask questions if anything is unclear

---

### Step 2: Implementation Process

**During implementation, Claude Code will:**

1. **Follow Architecture Patterns**
   - Review existing code structure
   - Match established patterns
   - Use existing utilities and components
   - Follow dependency injection principles

2. **Write Tests First (or Alongside)**
   - Create test files colocated with components
   - Cover all acceptance criteria
   - Test user behavior, not implementation
   - Use proper assertions (specific, not ranges)

3. **Implement Features Incrementally**
   - Start with core functionality
   - Add error handling
   - Implement loading states
   - Add accessibility features
   - Refine based on tests

4. **Run Tests Continuously**
   - Run tests after each significant change
   - Fix failures immediately
   - Never skip tests
   - Ensure all tests pass before moving forward

**Key Principles:**

✅ **DO:**
- Read files before modifying them
- Use established patterns from the codebase
- Write integration tests over unit tests
- Test real behavior with proper assertions
- Follow YAGNI (You Aren't Gonna Need It)
- Keep solutions simple and focused
- Fix bugs immediately when found

❌ **DON'T:**
- Make changes to code you haven't read
- Over-engineer solutions
- Add features beyond what's requested
- Mock the method you're testing
- Use generic exceptions
- Skip or disable tests
- Add unnecessary abstractions
- Guess at implementation details

---

### Step 3: Testing Standards

**Testing Philosophy:**
- **Integration tests preferred**: Test real behavior with real dependencies where possible
- **Testcontainers for databases**: Use real database instances in tests
- **MockTransport for HTTP**: Mock external HTTP calls
- **Specific assertions**: Test exact values, not ranges or negations
- **Test real behavior**: If a test only has `pass` or tests mocks, rewrite it

**Frontend Testing:**

```typescript
// ✅ GOOD - Tests user behavior
it('navigates to product detail when card is clicked', async () => {
  const user = userEvent.setup();
  renderWithProviders(<ProductCard product={mockProduct} />);

  const card = screen.getByTestId('product-card');
  await user.click(card);

  expect(mockNavigate).toHaveBeenCalledWith('/product/1');
});

// ❌ BAD - Tests implementation details
it('card has cursor pointer styling', () => {
  const card = screen.getByTestId('product-card');
  expect(card).toHaveClass('cursor-pointer');
});
```

**Async Testing Best Practices:**

```typescript
// ✅ GOOD - Wait for async state
it('displays product details after loading', async () => {
  renderWithProviders(<ProductDetailPage />);

  // Wait for the element to appear
  const productName = await screen.findByText('Test Product');
  expect(productName).toBeInTheDocument();
});

// ✅ GOOD - Use waitFor for complex async assertions
it('handles error state correctly', async () => {
  mockFetchProduct.mockRejectedValue(new Error('API Error'));

  renderWithProviders(<ProductDetailPage />);

  await waitFor(() => {
    expect(screen.getByText(/something went wrong/i)).toBeInTheDocument();
  });
});
```

**Backend Testing:**

```python
# ✅ GOOD - Tests real behavior with testcontainers
def test_create_product_success(client, db_session):
    response = client.post(
        "/api/products",
        json={"name": "Test Product", "price": 29.99}
    )
    assert response.status_code == 201
    assert response.json()["name"] == "Test Product"

    # Verify in database
    product = db_session.query(Product).filter_by(name="Test Product").first()
    assert product is not None
    assert product.price == 29.99

# ❌ BAD - Over-mocked, doesn't test real behavior
def test_create_product_mocked(mock_db):
    mock_db.add.return_value = None
    mock_db.commit.return_value = None
    # This doesn't test anything meaningful
```

**Test Coverage Requirements:**
- ✅ All acceptance criteria covered by tests
- ✅ Happy path scenarios
- ✅ Error cases (404, API errors, validation errors)
- ✅ Edge cases (empty data, null values, boundaries)
- ✅ Loading states
- ✅ Accessibility features (keyboard navigation, ARIA labels)

---

### Step 4: Manual Testing

**Command:** `/manual-test-story`

**What it does:**
1. Asks for Jira story link
2. Fetches story and acceptance criteria from Jira
3. Checks if dev servers are running (asks to start if needed)
4. Uses Chrome DevTools MCP to:
   - Open application in browser (http://localhost:5173)
   - Navigate to relevant page for the feature
   - Walk through each acceptance criterion systematically
   - Take screenshots of key states (loading, success, errors)
   - Verify functionality works as expected
5. Guides you through testing each AC interactively
6. Documents any issues found
7. Provides summary of passed/failed ACs and next steps

**Example Session:**

```
You: /manual-test-story

Agent: Please provide the Jira story link to test.

You: https://yoursite.atlassian.net/browse/BOOT-8

Agent: ✅ Fetched BOOT-8: Individual Product Detail Page

       Acceptance Criteria:
       1. Product detail page displays all information
       2. Navigation from catalog works
       3. 404 errors show proper message
       ... (8 total ACs)

       Are your dev servers running?
       - API: http://localhost:8000
       - Web: http://localhost:5173

You: Yes

Agent: Opening application in Chrome...
       ✅ Application loaded successfully

       Let's test AC1: Product detail page displays all information

       Navigating to /product/1...
       ✅ Page loaded

       Verifying elements:
       - Product name: ✅ "Equal Experts T-Shirt" found
       - Price: ✅ "29,99 €" found
       - Description: ✅ Found
       - Category: ✅ "Clothing" found
       - Image: ✅ Displayed

       📸 Screenshot saved of product detail page

       Does AC1 look correct to you? (yes/no)

You: yes

Agent: ✅ AC1: Passed

       Testing AC2: Navigation from catalog works...

       Going back to /catalog...
       ✅ Catalog page loaded

       Clicking on first product card...
       ✅ Navigated to /product/1

       📸 Screenshot saved

       Does AC2 look correct? (yes/no)

You: yes

Agent: ✅ AC2: Passed

       ... [continues through all ACs]

       📊 Test Summary:
       ✅ 8/8 Acceptance criteria passed

       No issues found. Ready to create PR!

       Next step: /commit-and-open-pr
```

**Best Practices:**
- Run this after all automated tests pass
- Test on a clean database if possible
- Test all edge cases mentioned in ACs
- Document any visual issues or UX concerns
- If issues found, fix them before creating PR

---

### Step 5: Commit and Create PR

**Command:** `/commit-and-open-pr`

**What it does:**
1. Runs `git status` to check modified files
2. Runs `git diff` to see changes
3. Runs `git log` to understand commit message style
4. Analyzes all changes to draft comprehensive commit message
5. Stages relevant files (excludes secrets, credentials)
6. Creates commit with structured message
7. Pushes to remote branch
8. Creates Pull Request with:
   - Summary of changes
   - Test plan/checklist
   - Links to Jira story and Confluence spec

**Commit Message Format:**

```
feat(BOOT-8): Implement individual product detail page

- Add ProductDetailPage component with full product information
- Create useProduct hook for data fetching with React Query
- Make ProductCard clickable with keyboard navigation
- Add comprehensive error handling (404 + API errors)
- Implement loading states with skeleton animations
- Add route to App.tsx for /product/:id

All acceptance criteria met. Tests: 68 frontend + 55 backend passing.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

**PR Description Format:**

```markdown
## Summary
- Implements BOOT-8: Individual Product Detail Page
- Users can now click products to see full details
- Comprehensive error handling and loading states

## Changes
- New: ProductDetailPage component
- New: useProduct hook
- Updated: ProductCard for navigation
- Updated: App routes

## Test Plan
- [x] Product detail page loads correctly
- [x] Navigation from catalog works
- [x] 404 errors display properly
- [x] API errors show user-friendly messages
- [x] All 68 frontend tests pass
- [x] All 55 backend tests pass

## Links
- Jira: BOOT-8
- Confluence: [Feature Spec](https://...)
```

**Example Session:**

```
You: /commit-and-open-pr

Agent: Let me review the changes...

       Modified Files:
       - web/src/pages/ProductDetailPage.tsx (new)
       - web/src/hooks/useProduct.ts (new)
       - web/src/components/catalog/ProductCard.tsx
       - web/src/App.tsx

       I'll create a commit summarizing these changes...

       ✅ Committed: feat(BOOT-8): Implement individual product detail page
       ✅ Pushed to origin/BOOT-8-product-detail-page
       ✅ Created PR #8: https://github.com/.../pull/8

       PR is ready for review!
```

---

### Step 6: Address PR Feedback

**Command:** `/address-pr-feedback`

**What it does:**
1. Asks for PR link (or detects current PR)
2. Fetches all review comments and feedback
3. Categorizes issues by priority (Critical, Medium, Minor)
4. Creates todo list for tracking progress
5. Addresses each issue systematically:
   - Critical issues first
   - Medium issues second
   - Minor issues last
6. Runs tests after each fix
7. Commits changes with clear message
8. Pushes to PR branch
9. Asks if you want to merge or request re-review

**Example Session:**

```
You: /address-pr-feedback

Agent: Found PR #8: Individual Product Detail Page

       Fetching review feedback...

       **Feedback Summary:**
       🔴 1 Critical issue
       🟡 3 Medium issues
       🟢 2 Minor issues

       Creating todo list to track progress...

       **Critical Issue: Type Safety in Error Handling**
       Location: ProductDetailPage.tsx:27
       Problem: Unsafe type casting for error status

       Fixing by implementing NetworkError type guard...
       ✅ Fixed

       **Medium Issue: Image State Reset**
       Location: ProductDetailPage.tsx:15
       Problem: Image state not reset on product change

       Adding useEffect to reset state...
       ✅ Fixed

       ...continuing with remaining issues...

       All issues addressed! Running tests...
       ✅ 67 frontend tests passing
       ✅ 55 backend tests passing

       Committing changes...
       ✅ Committed: refactor(BOOT-8): Address PR feedback
       ✅ Pushed to origin/BOOT-8-product-detail-page

       What would you like to do next?
       1. Merge PR and return to main
       2. Request another review
       3. Continue with more improvements
```

**Feedback Addressing Principles:**

1. **Prioritize by Severity**
   - Critical: Type safety, security, breaking changes
   - Medium: Code quality, potential bugs, performance
   - Minor: Style, documentation, minor improvements

2. **Be Systematic**
   - Create todo list to track progress
   - Address one issue at a time
   - Run tests after each fix
   - Commit incrementally if changes are extensive

3. **Communicate Changes**
   - Clear commit messages explaining what was fixed
   - Reference specific feedback items
   - Update PR description if scope changed

4. **Iterate if Needed**
   - Be prepared for multiple review rounds
   - Each round makes the code better
   - Don't rush to merge

---

### Step 7: Merge and Clean Up

**After all feedback is addressed:**

```
Agent: All feedback addressed. Ready to merge?

You: Yes

Agent: Merging PR #8 with squash...
       ✅ PR merged to main
       ✅ Feature branch deleted
       ✅ Switched to main branch
       ✅ Pulled latest changes

       Running tests to verify main branch...
       ✅ 67 frontend tests passing
       ✅ 55 backend tests passing

       BOOT-8 implementation complete! 🎉
```

---

## Common Scenarios

### Scenario 1: Tests Failing During Implementation

```
Agent: Tests are failing:
       ❌ ProductDetailPage.test.tsx - 404 error test failing

       Analyzing failure...
       Issue: Test expects plain Error but code uses NetworkError

       Fixing test to use NetworkError instances...
       ✅ Tests now passing
```

**Key Principle:** Never skip or disable tests. Fix the issue.

---

### Scenario 2: Manual Testing Reveals Bug

```
You: When I click products, I see "Page Not Found"

Agent: Let me debug this...

       Using Chrome DevTools to inspect...
       Found: ProductGrid uses /products/:id but route is /product/:id

       Fixing routing mismatch...
       ✅ Updated ProductGrid to use /product/:id
       ✅ Manual testing confirmed working
       ✅ Tests updated and passing
```

---

### Scenario 3: Multiple Review Rounds

```
Round 1 Feedback:
- Critical type safety issue
- Medium code duplication
- Minor missing accessibility

Agent: Addressing all issues...
       ✅ All fixed and pushed

Round 2 Feedback:
- Add stopPropagation to button
- Simplify image loading logic
- Remove CSS test

Agent: Addressing additional feedback...
       ✅ All improvements made
       ✅ Code quality improved

       Ready to merge!
```

---

## Best Practices

### Code Quality

1. **Read Before Writing**
   - Always read existing files before modifying
   - Understand patterns before implementing
   - Follow established conventions

2. **Keep It Simple**
   - Avoid over-engineering
   - Only add what's requested
   - Don't add "future" features
   - Three similar lines > premature abstraction

3. **Proper Error Handling**
   - Use specific exception types
   - Log details internally
   - Return generic messages to users
   - Handle edge cases gracefully

4. **Type Safety**
   - Use proper TypeScript types
   - Create type guards for runtime checks
   - Avoid `any` type
   - No unsafe type casting

### Testing Quality

1. **Test Behavior, Not Implementation**
   - Test what users see and do
   - Don't test CSS classes
   - Don't test internal state
   - Use Testing Library best practices

2. **Comprehensive Coverage**
   - All acceptance criteria covered
   - Happy path + error cases + edge cases
   - Loading states tested
   - Accessibility features verified

3. **Proper Async Handling**
   - Use `waitFor` for async assertions
   - Use `findBy*` for elements that appear asynchronously
   - Don't forget `await` on async operations
   - Wrap state changes in `act()` when needed

4. **Real Tests, Not Mocks**
   - Prefer integration tests
   - Use testcontainers for databases
   - Mock only external services
   - Never mock what you're testing

### Git Workflow

1. **Branch Naming**
   - Format: `STORY-KEY-brief-description`
   - Example: `BOOT-8-product-detail-page`
   - Lowercase with hyphens
   - Keep it brief but descriptive

2. **Commit Messages**
   - Format: `type(scope): brief description`
   - Types: `feat`, `fix`, `refactor`, `test`, `docs`, `chore`
   - Include "why" context in body
   - Reference Jira story key
   - List key changes as bullets

3. **PR Hygiene**
   - One PR per story
   - Keep PRs focused
   - Update PR description if scope changes
   - Respond to feedback promptly
   - Squash merge to keep main clean

### Architecture Compliance

1. **Backend (Hexagonal Architecture)**
   - Domain: Pure business logic, no external dependencies
   - Services: Orchestrate domain + adapters via DI
   - Adapters: Handle external systems
   - Routers: HTTP concerns only

2. **Frontend (React Best Practices)**
   - React Query for all data fetching
   - Colocate tests with components
   - Use established patterns
   - Proper provider hierarchy

3. **Security**
   - No generic exceptions exposing details
   - Validate at system boundaries
   - Audit log security events
   - Never commit secrets

---

## Troubleshooting

### "Tests are failing on CI but passing locally"

**Common causes:**
- Race conditions in async tests
- Missing `await` statements
- Test pollution (missing cleanup)
- Environment differences

**Solution:**
```typescript
// Add proper cleanup
afterEach(() => {
  vi.clearAllMocks();
});

// Ensure proper awaits
await waitFor(() => {
  expect(element).toBeInTheDocument();
});
```

---

### "PR feedback seems contradictory"

**Solution:**
- Ask clarifying questions
- Request specific examples
- Propose solution and ask for confirmation
- Remember: iteration makes code better

---

### "Implementation is taking longer than expected"

**Solution:**
- Break story into smaller tasks
- Implement core functionality first
- Add enhancements incrementally
- Communicate with team
- Consider splitting story in Jira

---

## Integration with Spec Workflow

This coding workflow integrates with the broader spec-driven process:

```
Feature Planning Meeting
        ↓
/create-spec → Confluence Page
        ↓
Technical Design Session
        ↓
/refine-spec → Updated Confluence Page
        ↓
Story Decomposition
        ↓
/create-user-stories-from-spec → Jira Stories
        ↓
        ↓
[YOU ARE HERE - IMPLEMENTATION]
        ↓
/implement-story → Code + Tests
        ↓
/commit-and-open-pr → PR
        ↓
/address-pr-feedback → Refined Code
        ↓
Merge to Main
```

---

## Command Reference

### `/implement-story`

**Purpose:** Start implementing a Jira story

**Input:** Jira story link + Confluence spec link

**Output:**
- Feature branch created
- Implementation plan
- Code + tests implemented
- All tests passing

---

### `/commit-and-open-pr`

**Purpose:** Commit changes and create pull request

**Input:** None (works on current branch)

**Output:**
- Changes committed with structured message
- Pushed to remote
- PR created with summary and test plan

---

### `/address-pr-feedback`

**Purpose:** Systematically address PR review feedback

**Input:** PR link (or auto-detects current PR)

**Output:**
- All feedback categorized and addressed
- Tests passing
- Changes committed and pushed
- Ready for merge or re-review

---

## Metrics & Quality Gates

### Before Opening PR

- ✅ All acceptance criteria implemented
- ✅ All tests passing (frontend + backend)
- ✅ No skipped or disabled tests
- ✅ No console errors or warnings
- ✅ Manual testing completed
- ✅ Code follows architecture guidelines
- ✅ No security vulnerabilities introduced

### Before Merging PR

- ✅ All review feedback addressed
- ✅ All tests still passing
- ✅ No merge conflicts
- ✅ PR approved by reviewer(s)
- ✅ CI/CD pipeline green
- ✅ Documentation updated if needed

---

## Real Example: BOOT-8

**Story:** Implement Individual Product Detail Page

**Implementation Timeline:**
1. `/implement-story` - Created plan and branch
2. Backend verification - Endpoint already existed
3. Frontend implementation:
   - Created `useProduct` hook
   - Implemented `ProductDetailPage` component
   - Updated `ProductCard` for navigation
   - Added route to `App.tsx`
   - Wrote 18 comprehensive tests
4. Manual testing - Found routing bug, fixed immediately
5. `/commit-and-open-pr` - Created PR #8
6. First review - 1 critical, 3 medium, 2 minor issues
7. `/address-pr-feedback` - Fixed all issues
8. Second review - 4 additional improvements
9. `/address-pr-feedback` - Made improvements
10. Merged to main

**Final Stats:**
- 9 files changed
- 682 additions, 20 deletions
- 67 frontend tests passing
- 55 backend tests passing
- 2 review rounds
- Zero bugs in production

---

## Support

For issues or questions about the coding workflow:
- Review project's `CLAUDE.md` for architecture guidelines
- Check `SPEC_README.md` for upstream workflow
- Refer to individual command files for detailed documentation
- Ask Claude Code for clarification during implementation

---

## License

This workflow is open for use and adaptation. Modify to fit your team's needs.
