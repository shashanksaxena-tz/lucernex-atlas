---
title: "AST-R-001 — An Asset attaches softly, or not at all"
tags: [rule, assets-equipment]
evidence: Observed
---

**`AST-R-001`** · [[module-assets-equipment]] · **Observed**

[[Asset]] carries a [[soft-reference|soft `ProjectEntityID`]] only — **no hard `FacilityID` or
`LocationID` column**. So "where is this asset" is not answerable by a join on a typed key.

See [[rules-assets-equipment]] for the full register.
