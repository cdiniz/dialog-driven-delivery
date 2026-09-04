# Filter catalog products by price range

## Description
Shoppers can narrow the catalog to a price range they specify, so they only see products they can afford.

## Acceptance Criteria

### AC1: Filter returns products within the range, inclusive
- **Given** the shopper is on the catalog page
- **When** they enter a minimum of 10 and a maximum of 50 and apply the filter
- **Then** only products priced between 10 and 50 are shown
- **And** a product priced at exactly 50 is included

### AC2: Both bounds are required
- **Given** the shopper is on the catalog page
- **When** they fill in only one of the two price fields
- **Then** the filter is not applied

### AC3: Minimum higher than maximum is rejected
- **Given** the shopper is on the catalog page
- **When** they enter a minimum higher than the maximum
- **Then** an inline error "Minimum must be less than maximum" is shown beneath the field
- **And** the search is not run

### AC4: No products in range
- **Given** the shopper has applied a valid price range
- **When** no products fall within that range
- **Then** the message "No products match that price range" is shown in place of the product grid

## Open Questions
- [OPEN QUESTION: Does the price filter persist when the shopper moves to the next page of results?]

## Relevant docs
Feature spec: TBD
