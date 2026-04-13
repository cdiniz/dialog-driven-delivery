# Filter products by price range

## Description
Customers can filter the product catalog by setting a minimum and maximum price, narrowing the visible products to those whose price falls within the range.

## Acceptance Criteria

### AC1: Filter by valid price range
- **Given** a customer is on the catalog page
- **When** they enter a min price of 10 and a max price of 50 and click Apply
- **Then** the catalog shows only products priced between 10 and 50 (inclusive)
- **And** the entered min and max values remain visible in the filter inputs

### AC2: Both min and max are required
- **Given** a customer is on the catalog page
- **When** they leave the min or max field empty and click Apply
- **Then** the system displays the error "Min and max are required"
- **And** the filter is not applied

### AC3: No products match the range
- _To be defined_

## Relevant docs
Feature spec: TBD
