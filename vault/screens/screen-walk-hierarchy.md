---
title: "View Data Model / Data Values (experimental)"
tags: [screen, administration,data-model,diagnostics]
evidence: Observed
---

`/en/test/walkHierarchy.jsp`

![The containment hierarchy, walked. ~70 child tables under one Contract — this is the shape "a contract is a small header plus twenty-five collections" takes in the schema.](../../docs/assets/screenshots/data-model/walk-hierarchy-re-contract-schema.jpg)
`docs/assets/screenshots/data-model/walk-hierarchy-re-contract-schema.jpg`

![The admin entry point, labelled experimental.](../../docs/assets/screenshots/bbw-admin/46-view-data-model-data-values-experimental.jpg)
`docs/assets/screenshots/bbw-admin/46-view-data-model-data-values-experimental.jpg`

A second, different view of the schema from
[[screen-view-object-model|View Object Model]]: **containment** rather than columns.

It nests ~70 owned child tables under [[Contract]]. **[[Facility]], [[Location]] and [[Organization]]
appear only as separate roots** — which is the containment-side confirmation that they are
[[subtype-root|independent subtype roots]], not children of the contract.

Marked *experimental* by the product itself. See [[screen-related-fields]] · [[foreign-key-graph]]

All screens: [[map-of-screens]] · caveat: [[caveat-viewport]]
