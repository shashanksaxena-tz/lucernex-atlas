---
title: PercentageRent
tags: [entity, contracts, variable-rent, retail]
evidence: Observed
---

**`percentage_rent` · 45 fields · variable-rent**

Turnover rent: a percentage of reported [[Sales]] above a breakpoint, with a cap and an audit-right
flag.

**The highest-risk rule in the contracts module lives here.** [[rule-CON-R-058]] assumes percentage-rent
tiering uses **marginal bands**; the alternative is simple-excess, and the two produce different money.
It is **Inferred**, and it is flagged as the module's biggest single exposure.

Its forward projection is [[VirtualPercentageRentPeriod]] — one of the two
[[virtual-projection|computed projections]] that turn out to be the **primary table of user-facing
screens** ([[finding-layouts-over-projections]]).

[[SalesExclusionCap]] limits what sales may be excluded — online sales, for instance.

Retail-specific, so **dropped from [[equipment-contract]]**.
