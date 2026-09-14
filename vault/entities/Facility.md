---
title: Facility
tags: [entity, facilities, subtype-root]
evidence: Observed
---

**`facility` · 133 fields · [[module-facilities-locations]]**

The building. A [[subtype-root]] with 17 navigation screens, sitting under a required [[Location]]
(the site) and optionally inside a [[Complex]].

- Below it, [[Space]] is the sub-facility occupancy layer: a Space must belong to exactly one Facility
  ([[rule-FAC-R-015]]).
- `Facility Status Code` **does** carry `Open`, `Closed` and `Possession` — so the BRD-24 lifecycle
  vocabulary exists in the product, just on the facility rather than the [[contract-lifecycle|lease]].
- Its own single-step creation wizard is `ASG Facility Wizard` (99141, 26 fields).

**The [[screen-contract-wizard|contract wizard writes to it]].** Step 1 carries `Facility_OpenDate` and
`Facility_CloseDate` alongside the `Contract_*` fields — contract creation updates the Facility record
in the same step, so creation is not a single-aggregate transaction. See
[[finding-wizard-writes-two-entities]].

Carries 8 [[firm-custom-field|`Firm_` columns]].

Screens: [[screen-manage-facilities]]
