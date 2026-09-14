---
title: Location
tags: [entity, facilities, subtype-root]
evidence: Observed
---

**`location` · 141 fields · [[module-facilities-locations]]**

**Location is the site — the "Center".** [[Facility]] is the building on it. That is the central
naming question of the facilities module, and it is settled two independent ways.

- `Facility.LocationID` is **required**: a facility must belong to exactly one location
  ([[rule-FAC-R-001]]).
- `Location` has **no reverse `FacilityID` pointer** — the one-to-many is enforced only from the child
  side ([[rule-FAC-R-002]]). One Location can hold many Facilities.
- A [[Contract]] attaches to Location and Facility **independently** ([[rule-FAC-R-012]]).

A [[subtype-root]] with 12 navigation screens, and one of the four roots that render in both tenants.
It has its own single-step creation wizard, `ASG Location Wizard` (99142, 23 fields) — see
[[screen-contract-wizard]].

Carries 10 [[firm-custom-field|`Firm_` columns]], the second largest count after [[Contract]]'s 258.

Screens: [[screen-manage-locations]] ·
[`location-vs-facility-vs-site.md`](../../docs/modules/facilities-locations/location-vs-facility-vs-site.md)
