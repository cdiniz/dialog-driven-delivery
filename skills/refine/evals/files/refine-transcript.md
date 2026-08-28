# Meeting: Recommendations Refinement
**Date:** Mar 28

## Transcript

PM: Two things to lock down today — how we pick the items inside a category, and what we do when a category has fewer than 3 products. Mobile layout we'll handle separately with design later.

Eng: For selection inside a category, the simplest thing that gives a useful signal is bestsellers. Sort the category by 30-day sales and take the top 3 excluding the current product. We don't have good co-purchase data yet, so let's start there and revisit once we do.

PM: OK, bestsellers it is. Note that we may want to revisit once we have more behavioural signal.

Eng: For the small-category case — if there are fewer than 3 other products in the category, we just show whatever's there. So 2 or even 1 is fine. If the category has only the current product (zero others), hide the slot entirely.

PM: Yep, that works. So the rule is: show what we have, hide the slot if there's nothing to show.

Eng: Good. That's it for me.

PM: Mobile and success metrics we'll cover next week with design and analytics.
