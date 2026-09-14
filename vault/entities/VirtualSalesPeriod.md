---
title: VirtualSalesPeriod
tags: [entity, projection, variable-rent]
evidence: Observed
---

**66 fields, and it names no physical table at all** — the only one of the 13
[[virtual-projection|projections]] that does not even declare a view name.

Joint largest of the projections, and the forward period expansion of [[Sales]].

It backs `ASG Contract Percent Rent - Schedule` (98920), a LIST layout — so like
[[VirtualPercentageRentPeriod]] it is **user-facing**, which the corpus did not expect
([[finding-layouts-over-projections]]).

Labelled `Sales Period` in the layout registry, which is why a UI-label census diff reported it
missing. See [[caveat-labels-are-tenant-local]].
