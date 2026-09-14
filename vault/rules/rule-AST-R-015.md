---
title: "AST-R-015 — The parts catalog has no per-location stock"
tags: [rule, assets-equipment]
evidence: Derived
---

**`AST-R-015`** · [[module-assets-equipment]] · **Derived**

`QuantityOnHand` and `QuantityOnOrder` are **single firm-wide counters**. One count per part, for the
whole tenant — no warehouse, no site, no bin.

See [[rules-assets-equipment]] for the full register.
