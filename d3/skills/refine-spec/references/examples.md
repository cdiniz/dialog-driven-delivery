# Refine Spec Examples

Detailed examples showing various refinement scenarios for updating existing specifications.

---

## Example 1: Product Refinement

**Scenario:** Adding product details from a review meeting.

```
User: /d3:refine-spec 123456789

Agent: I found Specification: Advanced Search

       **Current Coverage:**
       📋 Product Spec: ~70% complete (missing success metrics)
       🔧 Technical Spec: ~30% complete (basic approach only)

       How would you like to provide new information?

User: Option A
      [Pastes product review meeting discussing success metrics and new requirements]

Agent: I found information affecting:

       **📋 Product Specification Updates:**
       - Overview: Adding success metrics
       - Requirements: Adding 3 new requirements
       - Open Questions: Resolving 2 questions

       **🔧 Technical Specification Updates:**
       - No changes detected

       [Shows before/after for each change]

       Should I proceed?

User: Yes

Agent: ✅ Specifications refined successfully!

       Product Spec: 70% → 85% complete
       Technical Spec: 30% (unchanged)
```

---

## Example 2: Technical Refinement

**Scenario:** Updating technical approach based on architecture decision.

```
User: /d3:refine-spec https://yoursite.atlassian.net/wiki/spaces/PROJ/pages/123456789

Agent: [Shows current state]

       How would you like to provide new information?

User: Option C
      We decided to use PostgreSQL full-text search instead of Elasticsearch

Agent: I found information affecting:

       **🔧 Technical Specification Updates:**
       - Technical Approach: Updating search implementation
       - Architecture: Updating diagrams
       - Integrations: Removing Elasticsearch, updating PostgreSQL

       **BEFORE (Technical Approach):**
       ```
       Use Elasticsearch for full-text search with <100ms response time
       ```

       **AFTER (Technical Approach):**
       ```
       Use PostgreSQL full-text search with tsvector and GIN indexes
       for <100ms response time
       ```

       **Rationale:** Cost savings and simpler infrastructure
       **Type:** Modification

User: Yes, update it

Agent: ✅ Technical Spec updated: 30% → 75% complete
```

---

## Example 3: Combined Refinement

**Scenario:** Updating both product and technical specs from comprehensive review.

```
User: /d3:refine-spec Advanced Search

Agent: [Searches and finds page]
       [Shows current state]

User: Option A
      [Pastes comprehensive review meeting covering both aspects]

Agent: I found information affecting both specifications:

       **📋 Product Updates:**
       - User Journey: Adding error recovery workflow
       - Requirements: Modifying 2 requirements

       **🔧 Technical Updates:**
       - API Contracts: Adding 3 new endpoints
       - Data Models: Adding audit log model

       **Product Change 1: User Journey**

       **BEFORE:**
       ```
       3. System displays search results
       ```

       **AFTER:**
       ```
       3. System displays search results
       4. If no results found, system suggests alternative search terms
       5. User can refine search with suggested terms
       ```

       **Rationale:** Improves user experience for failed searches
       **Type:** Enhancement

       **Technical Change 1: API Contracts**

       **BEFORE:**
       ```
       POST /api/search - Basic search endpoint
       ```

       **AFTER:**
       ```
       POST /api/search - Basic search endpoint
       POST /api/search/suggestions - Get search term suggestions
       GET /api/search/history - Get user's search history
       ```

       **Rationale:** Support new error recovery workflow
       **Type:** Addition

       [Shows all changes]

User: Perfect, apply all changes

Agent: ✅ Both specifications updated successfully!
       Product: 85% → 92% complete
       Technical: 75% → 88% complete

       **Key Changes:**
       1. Added error recovery workflow
       2. Added 3 new API endpoints
       3. Resolved 2 open questions
```

---

## Example 4: Resolving Uncertainties

**Scenario:** Refining spec to resolve marked uncertainties.

```
User: /d3:refine-spec 123456789

Agent: Current spec has 5 [OPEN QUESTION] markers.

       How would you like to provide information?

User: Option C
      Let's resolve the open questions

Agent: **Open Question 1:** Authentication method - OAuth2, password, or social?

User: OAuth2 with Google and GitHub providers

Agent: **Open Question 2:** Target response time - <500ms, <1s, or <3s?

User: <500ms for search, <1s for filters

Agent: **Open Question 3:** Mobile support - yes or desktop only?

User: Desktop first, mobile in phase 2

Agent: I'll update:

       **Product Spec:**
       - Replace [OPEN QUESTION: auth method] → "OAuth2 with Google and GitHub"
       - Add Phase 2 scope: Mobile support
       - Remove Question 1 and 3 from Open Questions section

       **Technical Spec:**
       - Replace [OPEN QUESTION: response time] → "<500ms search, <1s filters"
       - Add performance requirements section
       - Remove Question 2 from Open Questions section

User: Apply changes

Agent: ✅ Resolved 3 open questions
       Remaining: 2 technical questions
```

---

## Example 5: Conflict Resolution

**Scenario:** Handling conflicting information during refinement.

```
User: /d3:refine-spec 123456789
      [Pastes meeting notes saying feature should be "simple" but also "support 50+ filters"]

Agent: I found conflicting information:

       **Product requirement:** "Keep interface simple and clean"
       **Product requirement:** "Support 50+ filter options"

       These requirements may conflict. I can:

       **Option A:** Add as [DECISION PENDING] in Open Questions
       **Option B:** Create two separate requirements with note about tension
       **Option C:** Add progressive disclosure approach (simple by default, advanced on demand)

User: Option C

Agent: I'll update Requirements:

       **BEFORE:**
       ```
       - Must have: Simple, clean interface
       ```

       **AFTER:**
       ```
       - Must have: Simple, clean interface with progressive disclosure
         - Default view: 5 most common filters
         - Advanced mode: All 50+ filters available
         - Auto-suggest filters based on context
       ```

       This resolves the apparent conflict.

User: Perfect

Agent: ✅ Updated with progressive disclosure approach
```

---

## Example 6: Feedback-Driven Update

**Scenario:** Incorporating stakeholder feedback.

```
User: /d3:refine-spec 123456789

       Option D
       [Pastes stakeholder feedback: "Need to clarify data retention policy"
       and "Missing information about error handling"]

Agent: Analyzing feedback:

       **Feedback 1:** Data retention policy (Product Spec - Constraints)
       **Feedback 2:** Error handling (Technical Spec - Error Handling)

       **Product Change:**
       Adding to Constraints section:

       **Data Retention:**
       - Search history: 90 days
       - User preferences: Until account deletion
       - Audit logs: 7 years (compliance requirement)

       **Technical Change:**
       Adding Error Handling section:

       **Error Categories:**
       - Search failures: Return empty results + log error
       - Invalid filters: Return 400 with specific message
       - Timeout: Return 503, retry with exponential backoff

User: Looks good

Agent: ✅ Added data retention policy and error handling
       Both sections were previously empty - now complete
```

---

## Example 7: Minor Update

**Scenario:** Quick update to a single section.

```
User: /d3:refine-spec 123456789
      Update the success metric - we changed target from 80% to 90% user satisfaction

Agent: I'll update the Product Spec Overview:

       **BEFORE:**
       ```
       Success Metrics:
       - User satisfaction: 80% rating or higher
       ```

       **AFTER:**
       ```
       Success Metrics:
       - User satisfaction: 90% rating or higher
       ```

User: Yes

Agent: ✅ Updated success metric
       1 section modified, minimal change
```

---

## Tips for Effective Refinement

1. **Use specific inputs:** Point to what needs updating
2. **Review before/after:** Verify changes match intent
3. **Resolve uncertainties incrementally:** Don't need to resolve all at once
4. **Document rationale:** Changes include why, not just what
5. **Update dependencies:** If requirements change, update related stories
6. **Iterate frequently:** Small, frequent updates better than large batches
7. **Link to discussions:** Reference meetings or decisions in version messages
