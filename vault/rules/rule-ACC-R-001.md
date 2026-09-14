---
title: "ACC-R-001 — Discount rate resolution order"
tags: [rule, accounting]
evidence: Observed
---

**`ACC-R-001`** · [[module-accounting]] · **Observed**

The rate resolves **[[Program|Portfolio]]-level first, then [[Firm]]-level, and never
contract-level.** It is entered as `5`, not `0.05`.

That resolution order is why [[finding-discount-rate-table-empty|an empty rate table]] is such a
problem: there is no contract-level fallback in the table itself. The only per-record path is
[[Asset]]`.DiscountRateOverride` — see [[DiscountRate]].

See [[rules-accounting]] for the full register.
