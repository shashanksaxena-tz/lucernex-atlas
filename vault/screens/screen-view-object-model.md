---
title: "View Object Model"
tags: [screen, administration,data-model,diagnostics]
evidence: Observed
---

`/en/admin/ShowObjectDetails.jsp`

![The `sqlTableID` picker — 227 tables, against a 223-object census. And 25 of the 227 are refused when you select them.](../../docs/assets/screenshots/bbw-admin/45-view-object-model.jpg)
`docs/assets/screenshots/bbw-admin/45-view-object-model.jpg` · `af-admin/51-view-object-model.jpg`

**The schema viewer, and the source of the 227-table count** that the 223-object census is measured
against.

- **31 of 227 are undocumented** — but only **6 are real gaps**, and the composition is the finding:
  **25 are tables the viewer itself refuses to open** ([[finding-punch-list-out-of-scope]]).
- The refused 25 are **the platform's own machinery** — [[PageLayout]], [[PageLayoutField]],
  [[PageLayoutFilter]], `CustomCodeTable`, `Dashboard`, `Job Log`, `Audit Master`. All recoverable over
  [[rest-business-object|REST]].
- **Never match on UI label.** It labels [[ProjectEntity]] *"General Entity Info"*, and ten
  [[virtual-projection|`Virtual*`]] views under other names — [[caveat-labels-are-tenant-local]].
- Its field counts are a **lower bound**, because the default capture parameter is `showGlobal=true`
  and firm columns are excluded ([[method-cheap-signals]]).

Open: [[q-bbw-13-census-gap]] · see [[screen-related-fields]]

All screens: [[map-of-screens]] · caveat: [[caveat-viewport]]
