---
title: "AST-R-006 — RemainingAssetBalance is magnitude-typed"
tags: [rule, assets-equipment]
evidence: Observed
---

**`AST-R-006`** · [[module-assets-equipment]] · **Observed**

> **0–100 reads as a percent. ≥100.01 reads as currency. And the user can override it.**

A genuine landmine: the same column means two different things depending on its value, with no type
or flag to say which. Do not reproduce this.

See [[rules-assets-equipment]] for the full register.
