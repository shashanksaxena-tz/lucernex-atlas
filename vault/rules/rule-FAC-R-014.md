---
title: "FAC-R-014 — Property tax attaches only to the Parcel"
tags: [rule, facilities-locations]
evidence: Observed
---

**`FAC-R-014`** · [[module-facilities-locations]] · **Observed**

All six `PropertyTax*` objects carry `ParcelID`, and **none carries a `FacilityID` or `ContractID`**.
The tax bill for a building is reached through the land it sits on. See
[[module-property-tax]] · [[rule-TAX-R-007]].

See [[rules-facilities-locations]] for the full register.
