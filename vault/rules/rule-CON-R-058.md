---
title: "CON-R-058 — Percentage-rent tiering assumes marginal bands"
tags: [rule, contracts]
evidence: Inferred
---

**`CON-R-058`** · [[module-contracts]] · **Inferred**

> **The highest-risk rule in the contracts module.**

Tiering is assumed to use **marginal bands**; the alternative is **simple-excess**, and the two produce
different money on the same sales figure.

**Inferred**, and flagged as the module's biggest single exposure. Settle it before
[[PercentageRent]] is specified.

See [[rules-contracts]] for the full register.
