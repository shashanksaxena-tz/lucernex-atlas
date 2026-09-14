---
title: "AST-R-012 — ServiceRequest and WorkOrder are Issues"
tags: [rule, assets-equipment]
evidence: Observed
---

**`AST-R-012`** · [[module-assets-equipment]] · **Observed**

Each is **1:1 with an underlying [[Issue]]** (`IssueID`, Required) — **and the schema export types the
link as untyped `Text`**, so the [[foreign-key-graph|FK graph]] misses the maintenance loop entirely.
See [[soft-reference]].

See [[rules-assets-equipment]] for the full register.
