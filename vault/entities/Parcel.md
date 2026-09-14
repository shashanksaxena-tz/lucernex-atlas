---
title: Parcel
tags: [entity, facilities, subtype-root, property-tax]
evidence: Observed
---

**`parcel` · 154 fields · [[module-facilities-locations]]**

The land record, and a [[subtype-root]]. Unusually promiscuous in its parentage: on top of a required
[[Location]] and [[Program]], it can carry **five simultaneous optional parents** — [[Facility]],
[[Contract]], [[Complex]], [[Prototype]] and [[Organization]] ([[rule-FAC-R-005]]).

`MasterParcelID` is a self-reference, mirroring `Contract.MasterContractID` exactly
([[rule-FAC-R-011]]).

**Property tax attaches only here.** All six `PropertyTax*` objects carry a required `ParcelID` and
**none carries a `FacilityID` or `ContractID`** ([[rule-TAX-R-007]], [[rule-FAC-R-014]]). So the tax
bill for a building is reached through the land it sits on, never through the building or the lease —
which is a real modelling decision and not an obvious one.

Out-degree is joint highest in the schema with [[Contract]]: 13 distinct targets across 18 FK columns.

See [[PropertyTaxSummary]] · [[module-property-tax]]
