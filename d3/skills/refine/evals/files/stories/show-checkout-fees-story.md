# Show fee breakdown on the checkout page

## Description
At checkout, the customer sees a breakdown of subtotal, shipping, tax, and the final total before they pay, so the price they confirm matches the price they're charged.

## Acceptance Criteria

### AC1: Subtotal and shipping are shown
- **Given** a customer has items in their cart and proceeds to checkout
- **When** the checkout page loads
- **Then** the page shows the cart subtotal as one line
- **And** the page shows the shipping cost as a separate line below the subtotal

### AC2: Tax is shown itemized by jurisdiction
- **Given** a customer has items in their cart that incur tax from more than one jurisdiction (e.g. state + city) and proceeds to checkout
- **When** the checkout page loads
- **Then** the page shows each applicable tax jurisdiction on its own line with the jurisdiction name and amount
- **And** the jurisdictions are grouped under a "Taxes" sub-heading below shipping

### AC3: Final total reflects all fees
- **Given** the customer is on the checkout page with subtotal, shipping, and tax visible
- **When** the customer reviews the order
- **Then** the final total displayed equals subtotal + shipping + tax
- **And** the final total is the amount the customer is charged on payment

## Relevant docs
Feature spec: ./specs/product/checkout-fees-spec.md
