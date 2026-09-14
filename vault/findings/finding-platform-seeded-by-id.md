---
title: The platform layer is seeded identically — proved by primary key, not by name
tags: [finding, tenancy, architecture]
evidence: Observed
---

Same names across two tenants could mean two firms configured themselves the same way. **Same primary
keys cannot.**

| Surface | Result |
|---|---|
| [[navigation-tree\|Navigation]] — 4 roots, 23 groups, 82 screens | **109 of 109 nodes share the same numeric `PageLayoutID`.** Zero differences |
| [[code-table\|Firm Drop Downs]] | **207 of 207 match on both name and `TableType` id.** Not one mismatch, neither tenant has a table the other lacks |
| The sql-table catalog | **227 of 227 identical** in both tenants |

`Contract : Details : Summary` is `PageLayoutID=3494` at [[tenant-american-freight|American Freight]]
and `3494` at [[tenant-bbw|BBW]]. `Portfolio` is `924` in both. `Contract Status Code` is `2094` in
both; `Issue Type Code` is `2035` in both.

> **These rows are seeded from one platform source, identical per tenant.**

This is what converts a [[hub-and-spoke]] assumption into evidence: navigation and the code-table
*registry* belong in the **Hub**; code-table *values* differ per tenant and belong in the **Spoke**.

**The contrast is the point.** [[page-layout-concept|Page layouts]] share **zero** ids — and 80 names
— which is a completely different distribution model ([[finding-publish-then-fork]]). Three models
run side by side in one estate, and telling them apart matters as much as the pattern.

Source: [`tenants/bbw-vs-american-freight.md` §9](../../docs/tenants/bbw-vs-american-freight.md)
