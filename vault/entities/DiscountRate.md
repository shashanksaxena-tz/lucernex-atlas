---
title: DiscountRate
tags: [entity, accounting, reference-data, core]
evidence: Observed
---

**`discount_rate` · 16 fields · [[module-accounting]]**

The table that supplies the rate ASC 842 and IFRS 16 need to compute a lease liability — and it is
**empty in both tenants**. See [[finding-discount-rate-table-empty]], which is the most consequential
blocker in this corpus for the accounting rebuild.

Even empty, its column set gives the lookup key, and it is **richer than assumed — seven dimensions**:

| Dimension | Note |
|---|---|
| Effective date range | |
| **Lease-length band** (`Length Month min`–`max`) | an incremental-borrowing-rate **curve**, not a scalar |
| Country | |
| State / Province | |
| Portfolio | resolves via [[Program]] before [[Firm]] ([[rule-ACC-R-001]]) |
| **Accounting Method** | so **the same lease can discount differently under ASC 842 and IFRS 16** |
| Use Type | |

A rate is entered as `5`, not `0.05` ([[rule-ACC-R-001]]).

Resolution is Portfolio-level first, then Firm-level, and **never contract-level** — which makes
`Asset.DiscountRateOverride` and the [[SLSummary]] equivalent the other candidate path entirely.

Screens: [[screen-manage-discount-rates]]
