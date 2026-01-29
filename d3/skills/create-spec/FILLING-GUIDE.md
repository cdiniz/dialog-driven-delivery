# Anti-Hallucination Filling Guide

This guide provides detailed rules for filling specifications without inventing content.

## Core Principle

**Fill ONLY what was explicitly discussed. Use placeholders for everything else.**

## Template Placeholders Are NOT Content

Templates contain examples like:
- `[New API endpoint being created]`
- `POST /api/path`
- `[Architecture diagram showing components]`
- `{field: "type - description"}`

**These are STRUCTURE GUIDES showing what COULD go there, NOT content to fill in.**

### Example

**Template shows:**
```markdown
### API Contracts
| Operation | Endpoint | Input | Output |
| [What it does] | `POST /api/path` | `{fields}` | `{response}` |
```

**If API contracts weren't discussed:**
```markdown
### API Contracts
_To be defined - not yet discussed_
```

**NOT:**
```markdown
### API Contracts
| Create item | `POST /api/items` | `{name, description}` | `{id, created_at}` |
```

## What NOT to Invent

### Technical Details (Never Invent These)

- **API endpoint names** - No `/api/resource/{id}/action` unless explicitly mentioned
- **Architecture diagrams or component names** - No invented service boundaries
- **Database schemas or table structures** - No field definitions beyond what was stated
- **Technology choices** - No "we'll use PostgreSQL" unless discussed
- **Error codes or status codes** - No `404`, `500`, `INVALID_INPUT` unless specified
- **Authentication/authorization patterns** - No JWT, OAuth, API keys unless mentioned
- **Deployment strategies** - No Kubernetes, Docker, CI/CD unless discussed
- **Performance metrics or SLAs** - No "< 100ms response time" unless defined
- **Logging or monitoring approaches** - No specific tools or formats
- **Testing strategies** - No unit/integration/e2e breakdown unless discussed

### Product Details (Don't Elaborate)

- **If transcript says "display items"** - Don't specify carousel, grid, list, or card layout
- **If transcript says "track actions"** - Don't invent analytics event schemas or properties
- **If transcript says "filter by type"** - Don't define the taxonomy or filtering UI
- **If transcript says "notify users"** - Don't specify email/SMS/push or template formats
- **If transcript says "handle errors"** - Don't invent specific error messages or recovery flows
- **If transcript says "fast performance"** - Don't invent specific time thresholds

## What TO Fill

Only fill sections with information explicitly provided:

✅ **Business goals mentioned** - "Increase AOV", "Reduce churn", "Improve conversion"
✅ **User workflows described** - "User clicks button, sees list, selects item"
✅ **Requirements stated** - "Must support 1000 concurrent users", "Need offline mode"
✅ **Metrics defined** - "Track click-through rate", "Measure time to completion"
✅ **Constraints discussed** - "Must work on mobile", "Can't change existing API"
✅ **Edge cases mentioned** - "What if user has no items?", "Handle empty state"
✅ **Decisions made** - "Use approach A, not B", "Start with simple, add complex later"

## Section-by-Section Process

For EACH section in the template:

1. **Ask yourself**: "Was this specific topic explicitly discussed in the transcript?"

2. **If YES - discussed**:
   - Write the actual information from the transcript
   - Use quotes or paraphrases from the discussion
   - Include specific details that were mentioned
   - Add uncertainty markers for ambiguous parts

3. **If NO - not discussed**:
   - Keep the section heading (with numbering)
   - Replace content with: `_To be defined - not yet discussed_`
   - Don't try to "help" by filling it with reasonable guesses

## Examples

### Example 1: Product-Focused Discussion

**Transcript mentions:**
- "Show 2-3 related products"
- "Track which ones users click"
- "Goal is to increase average order value"
- "Order by price descending"

**Correct filling:**

```markdown
## 1. Overview
Increase average order value (AOV) by showing related product recommendations.

## 2. Requirements
- Display 2-3 related products
- Track which recommendations users click
- Order recommendations by price descending

## 3. Success Metrics
- Average order value (AOV)
- Click-through rate on recommendations

## 4. Technical Approach
_To be defined - not yet discussed_

## 5. API Contracts
_To be defined - not yet discussed_

## 6. Data Models
_To be defined - not yet discussed_

## 7. Architecture
_To be defined - not yet discussed_
```

**Incorrect filling (hallucination):**

```markdown
## 5. API Contracts

GET /api/products/{id}/recommendations
Response: {
  recommendations: [
    { id: string, name: string, price: number, image_url: string }
  ]
}

## 7. Architecture

sequenceDiagram
  Frontend->>RecommendationService: GET /recommendations
  RecommendationService->>Database: Query products
  Database-->>RecommendationService: Product list
  RecommendationService-->>Frontend: Recommendations
```

### Example 2: Mixed Product + Some Technical

**Transcript mentions:**
- "Users can export data to CSV"
- "Need to validate email format"
- "Use the existing user service for authentication"

**Correct filling:**

```markdown
## Requirements
- Users can export data to CSV format
- Email validation required

## Technical Approach
Use existing user service for authentication.

## Data Validation
Email format validation required.

## Export Format
CSV export capability.

## API Contracts
_To be defined - not yet discussed_

## Performance Requirements
_To be defined - not yet discussed_
```

**Incorrect filling:**

```markdown
## API Contracts

POST /api/export
Request: { format: "csv", filters: {...} }
Response: { download_url: string, expires_at: timestamp }

Email validation regex: ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$

## Performance Requirements
CSV generation must complete within 30 seconds for files up to 10,000 rows.
```

## Typical Coverage Patterns

### After Initial Product Discussion

Most common pattern:

**Product Spec**: 40-70% filled
- Overview: Usually filled
- User Journey: Partially filled
- Requirements: Partially filled
- Open Questions: Many items

**Technical Spec**: 10-30% filled
- Technical Approach: Maybe high-level mention
- Architecture: Usually empty
- API Contracts: Usually empty
- Data Models: Usually empty
- Integrations: Usually empty

**This is EXPECTED and CORRECT.**

### After Technical Discussion

**Product Spec**: 60-80% filled
- Refined from earlier discussions

**Technical Spec**: 50-70% filled
- Technical Approach: Filled
- Architecture: Some diagrams
- API Contracts: Maybe 1-2 endpoints
- Data Models: Core entities defined
- Still many `_To be defined_` sections

## Red Flags (Signs You're Hallucinating)

If you find yourself doing any of these, STOP:

1. **"This is a reasonable default"** → No, use placeholder
2. **"Most systems do it this way"** → Doesn't matter, use placeholder
3. **"The template shows an example"** → Template ≠ content to fill
4. **"I can infer this from context"** → If not stated, use placeholder
5. **"This is obviously needed"** → Obvious ≠ discussed
6. **"Let me help by filling this in"** → Don't help, be honest
7. **"This is standard practice"** → Standard ≠ stated
8. **"The user probably wants"** → Probably ≠ explicitly requested

## When in Doubt

**Default to placeholder: `_To be defined - not yet discussed_`**

Better to have an honest gap than an invented detail.

The spec will be refined through `/d3:refine-spec` as more information becomes available.
