---
title: "Related Fields and the data model"
tags: [screen, administration,layouts,data-model]
evidence: Observed
---

`LayoutEditorAJAX.jsp · /en/admin/ShowObjectDetails.jsp · /en/test/walkHierarchy.jsp`

![Related Fields for Contract. Exactly eight related tables — and the self node exposes only 4 fields and 2 subgroups.](../assets/screenshots/page-layouts/related-fields-top-level-list.jpg)
`docs/assets/screenshots/page-layouts/related-fields-top-level-list.jpg`

![`PaymentTransaction.VendorID` declared as type `Employer ID`. The column name and the type name disagree, and the type is right.](../assets/screenshots/data-model/object-model-paymenttransaction-vendorid.jpg)
`docs/assets/screenshots/data-model/object-model-paymenttransaction-vendorid.jpg`

**This screen is the evidence that Related Fields is a genuine FK-driven relational model**, not a
shared-label taxonomy — and that Lx's [[type-system]] has **first-class FK types named after their
target table**.

- [[Contract]] has **307** fields as the viewer reports it, against 570 in the census — see
  [[finding-firm-fields-are-physical-columns]].
- `sqlTableID` values: Contract 2792, [[Facility]] 2530, [[Location]] 2804, [[Employer]] 2529,
  [[PaymentTransaction]] 2810, [[Complex]] 2791.
- **`PaymentTransaction.VendorID` is typed `Employer ID`** — "Vendor" is a relabelled [[Employer]]
  ([[rule-PPL-R-004]]).
- `walkHierarchy.jsp` nests **~70 owned child tables under [[Contract]]**; [[Facility]], [[Location]]
  and [[Organization]] appear only as separate roots.

![`walkHierarchy.jsp` — ~70 child tables under one contract. This is what "a contract is a small header plus twenty-five collections" looks like in the schema.](../assets/screenshots/data-model/walk-hierarchy-re-contract-schema.jpg)
`docs/assets/screenshots/data-model/walk-hierarchy-re-contract-schema.jpg`

See [[foreign-key-graph]] · [[screen-view-object-model]]

All screens: [[map-of-screens]] · caveat: [[caveat-viewport]]
