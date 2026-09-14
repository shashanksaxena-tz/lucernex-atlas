---
title: Facilities and locations
tags: [module, facilities]
evidence: Observed
---

**20 objects · 918 fields · rules `FAC-R-001`…`FAC-R-020`**

The physical real-estate register: four of the nine [[subtype-root|subtype roots]], plus an optional
container and a sub-facility occupancy layer.

The central question it settles: **[[Location]] is the site or "Center"; [[Facility]] is the building
on it.** One Location holds many Facilities; `Facility.LocationID` is required and Location has no
reverse pointer.

Entities: [[Location]] · [[Facility]] · [[Parcel]] · [[Prototype]] · [[Complex]] · [[Space]] ·
[[DMA]]

- End-user screens: Facility 17, Location 12.
- Internal FK edges 23; **inbound cross-module 34 from only 7 distinct source objects**.
- [[Complex]] has zero outbound FKs and no `ProjectEntityID` ([[rule-FAC-R-009]]).
- All six `PropertyTax*` objects FK to [[Parcel]] **alone** ([[rule-FAC-R-014]]).
- "Site" is [[PotentialProject]] and belongs to [[module-portfolio-transactions]], not here.
- Demographics is **9 objects with no ASG Edge+ counterpart**.

Screens: [[screen-manage-facilities]] · [[screen-manage-locations]] · [[screen-manage-complex]]

Rules: [[rules-facilities-locations]] ·
[`modules/facilities-locations/`](../../docs/modules/facilities-locations/README.md)
