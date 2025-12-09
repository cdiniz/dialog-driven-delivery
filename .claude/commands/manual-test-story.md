---
description: Launch app and manually test user story with Chrome DevTools
---

**Purpose:** Systematically verify all acceptance criteria in the browser using Chrome DevTools MCP.

**Workflow:**

1. **Get Story Information**
   - Ask the user for the Jira story link
   - Fetch the story, title, and acceptance criteria from Jira using Atlassian MCP
   - Display the story summary and list all acceptance criteria

2. **Verify Development Environment**
   - Check if dev servers are running:
     - API: http://localhost:8000
     - Web: http://localhost:5173
   - If not running, ask user to start them:
     - In one terminal: `pnpm run dev:api`
     - In another terminal: `pnpm run dev:web`
   - Wait for confirmation before proceeding

3. **Interactive Testing Per AC**
   For each acceptance criterion:

   a. **Announce AC**: Display the AC being tested (e.g., "Testing AC1: Product detail page displays all information")

   b. **Navigate**: Use Chrome DevTools MCP to navigate to the relevant page/URL based on the AC

   c. **Take Snapshot**: Use `take_snapshot` to get page content and verify elements are present

   d. **Verify Elements**: Check that required elements/text/functionality are visible

   e. **Interactive Actions**: If the AC requires interaction (clicks, form inputs, etc.):
      - Use `click`, `fill`, or other Chrome DevTools actions
      - Take snapshots after each action
      - Verify expected outcomes

   f. **Screenshot Key States**: Use `take_screenshot` for:
      - Initial page load
      - After user interactions
      - Success states
      - Error states (if AC covers error handling)
      - Loading states (if AC covers loading)

   g. **Ask for Confirmation**:
      - Show the user what was verified
      - Ask: "Does AC[N] look correct? (yes/no/issue)"
      - If "issue", ask user to describe the problem

   h. **Document Result**: Mark AC as passed/failed/issue and note any problems

4. **Test Edge Cases**
   - If ACs mention error handling, test error scenarios
   - If ACs mention empty states, test with no data
   - If ACs mention loading states, verify they appear
   - If ACs mention responsive design, test different viewport sizes

5. **Provide Comprehensive Summary**
   ```
   📊 Manual Testing Summary for [STORY-KEY]

   ✅ Passed: [list of passed ACs]
   ❌ Failed: [list of failed ACs]
   ⚠️  Issues: [list of ACs with issues]

   🐛 Bugs Found:
   - [Description of each bug/issue]

   📸 Screenshots saved: [count]

   Next Steps:
   - [If all passed]: Ready to create PR with /commit-and-open-pr
   - [If issues found]: Fix the following issues before creating PR:
     1. [Issue 1]
     2. [Issue 2]
   ```

**Best Practices:**
- Be systematic: Test one AC at a time
- Be thorough: Don't skip edge cases mentioned in ACs
- Be visual: Take screenshots of important states
- Be interactive: Confirm with user that each AC looks correct
- Be helpful: If issues found, provide clear description for fixing

**Error Handling:**
- If Chrome DevTools fails to connect, guide user to restart browser
- If page doesn't load, check if servers are actually running
- If element not found, take snapshot and ask user if page is correct
- If user reports issue, document it clearly for fixing
