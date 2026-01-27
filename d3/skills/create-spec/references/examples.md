# Create Spec Examples

Detailed examples showing various input types and scenarios for the create-spec skill.

---

## Example 1: Product-Focused Input

**Scenario:** Creating a spec from a product planning meeting transcript.

```
User: /d3:create-spec

Agent: How would you like to provide the feature information?

User: Option A
      [Pastes product planning meeting transcript]

Agent: Where would you like to create this specification?
       Location: ?

User: PROJ

Agent: Based on your input, I found information about an advanced search feature
       with filters for project managers.

       I propose creating a specification named: "Advanced Search with Filters"

       Should I create this specification in PROJ?

User: Yes

Agent: ✅ Feature specification created successfully!

       **Specification:** Advanced Search with Filters

       **📋 Product Specification:**
       - ✅ Overview: Filled (target users, success metrics defined)
       - ✅ User Journey: 3 workflows defined
       - ✅ Requirements: 8 must-haves, 3 out of scope
       - ⚠️ Open Questions: 5 questions need answers

       **🔧 Technical Specification:**
       - ⚪ Technical Approach: Empty - not discussed
       - ⚪ Architecture: Empty - not discussed
       - ⚪ API Contracts: Empty - not discussed
       - ⚠️ Open Questions: 8 technical decisions pending

       The technical aspects can be added later using `/d3:refine-spec [PAGE-ID]`
```

---

## Example 2: Technical-Focused Input

**Scenario:** Creating a spec from a technical design discussion with minimal product context.

```
User: /d3:create-spec

Agent: How would you like to provide the feature information?

User: Option C
      We need to implement Elasticsearch for full-text search with <100ms response

Agent: Where would you like to create this specification?

User: Engineering location, under "Technical Specs" page

Agent: Based on your input, I found information about implementing full-text
       search using Elasticsearch.

       I propose creating a specification named: "Full-Text Search Implementation"

       Should I create this page?

User: Name it "Smart Search" instead

Agent: I'll create a specification named: "Smart Search"

       Should I proceed?

User: Yes

Agent: ✅ Feature specification created successfully!

       **📋 Product Specification:**
       - ⚠️ Overview: Minimal (inferred purpose only)
       - ⚪ User Journey: Empty - user workflows not discussed
       - ⚪ Requirements: Empty - functional requirements not discussed
       - ⚠️ Open Questions: 7 product questions added

       **🔧 Technical Specification:**
       - ✅ Technical Approach: Filled (Elasticsearch implementation)
       - ✅ Architecture: 1 diagram added
       - ✅ Technical Specifications: Search API defined
       - ✅ Integrations: Elasticsearch details documented

       Product requirements can be added later using `/d3:refine-spec [PAGE-ID]`
```

---

## Example 3: Comprehensive Input

**Scenario:** Creating a spec from a transcript covering both product and technical discussions.

```
User: /d3:create-spec
      Option A
      [Pastes transcript covering both product and technical discussions]

Agent: Where would you like to create this specification?

User: ANALYTICS

Agent: Based on your input, I found comprehensive information about a reporting
       dashboard feature including user needs, workflows, and technical architecture.

       I propose creating a specification named: "Analytics Reporting Dashboard"

       Should I create this specification in ANALYTICS?

User: Yes

Agent: ✅ Feature specification created successfully!

       **📋 Product Specification:**
       - ✅ Overview: Filled
       - ✅ User Journey: 2 workflows defined
       - ✅ Requirements: 6 must-haves captured

       **🔧 Technical Specification:**
       - ✅ Technical Approach: Filled
       - ✅ Architecture: 2 diagrams added
       - ✅ API Contracts: 4 endpoints defined
       - ⚠️ Data Models: Partial (mentioned but not detailed)

       Both specifications have good coverage. Missing details can be added
       using `/d3:refine-spec [PAGE-ID]`
```

---

## Example 4: Resolving Uncertainties

**Scenario:** User chooses to resolve uncertainty markers immediately.

```
User: /d3:create-spec
      [Provides input with some ambiguities]

Agent: I've generated the feature specification with 8 uncertainty markers:

       **Open Questions:** 3 items requiring user decisions
       **Clarifications Needed:** 2 items requiring more specific definitions
       **Assumptions:** 3 items inferred from context that need validation

       These uncertainties should be resolved before implementation. Would you like to:

       **Option A:** Resolve them now - I'll ask follow-up questions
       **Option B:** Leave them marked for later resolution
       **Option C:** Review the spec first, then resolve

User: Option A

Agent: Let's resolve the open questions:

       **Q1:** Should authentication use OAuth2, password, or social login?

User: OAuth2 with Google and GitHub

Agent: **Q2:** What's the target response time - <500ms, <1s, or <3s?

User: <500ms

Agent: **Q3:** Should we support mobile or desktop only?

User: Desktop first, mobile in phase 2

Agent: ✅ Resolved 3 open questions

       Now for clarifications:

       **C1:** "Users can filter results" - by what fields?

User: By date, status, and category

Agent: ✅ All uncertainties resolved!

       Creating specification with complete information...

       ✅ Specification created with 0 open questions
```

---

## Example 5: Handling Conflicting Information

**Scenario:** Input contains contradictory requirements.

```
User: /d3:create-spec
      [Pastes transcript where PM says "real-time updates" but architect says "batch processing"]

Agent: I found conflicting information in your input:

       **Product requirement:** Real-time updates every second
       **Technical approach:** Batch processing every 5 minutes

       I've marked this as [DECISION PENDING] in both specs with reference to:

       Open Question #3: Should updates be real-time or batch processed?
       - Real-time: Better UX but higher server load
       - Batch: Scalable but delayed data

       Please resolve this before implementation.
```

---

## Tips for Best Results

1. **Use transcripts when possible:** More context leads to better specs
2. **Include both product and technical discussions:** Results in more complete specs
3. **Be specific in conversations:** Concrete examples better than abstract descriptions
4. **Resolve uncertainties early:** Makes implementation smoother
5. **Iterate with refine-spec:** Specs are meant to grow over time
