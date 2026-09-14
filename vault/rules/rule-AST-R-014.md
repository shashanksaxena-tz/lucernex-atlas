---
title: "AST-R-014 — Parts belong to the Issue, not the WorkOrder"
tags: [rule, assets-equipment]
evidence: Derived
---

**`AST-R-014`** · [[module-assets-equipment]] · **Derived**

`WorkOrder → `[[Issue]]` → LinkIssuePart`. Parts consumed on a job are recorded **against the Issue**.

A rebuild that hangs parts off the work order will not round-trip the incumbent's data.

See [[rules-assets-equipment]] for the full register.
