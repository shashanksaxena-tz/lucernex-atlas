# FAC-R-019 — `Prototype`'s Location/Complex/DMA relationships exist in the schema but are not administrator-configurable

*Facilities, Locations & Sites · Observed*

**Input: `Prototype.LocationID`, `.ComplexID`, `.DemographicDMAID` are declared columns in `_lucernex_objects_summary.txt` but do not appear anywhere in `../../data-fields/prototype.md`'s 15-row catalog. Effect: Unlike the identical columns on `Facility`/`Location`/`Parcel`, these cannot be placed on….**

Input: `Prototype.LocationID`, `.ComplexID`, `.DemographicDMAID` are declared columns in `_lucernex_objects_summary.txt` but do not appear anywhere in `../../data-fields/prototype.md`'s 15-row catalog. Effect: Unlike the identical columns on `Facility`/`Location`/`Parcel`, these cannot be placed on a Prototype layout by a tenant administrator through the observed mechanism. Confidence: Derived (cross-referencing the two sources; see `data-model.md`). Whether this reflects a deliberate platform restriction or simply that ASG's tenant never placed those fields is unresolved — see Open Questions there.

## What it constrains

[Prototype](../entities/Prototype.md), [Facility](../entities/Facility.md), [Location](../entities/Location.md), [Parcel](../entities/Parcel.md)

Columns named: `Prototype.LocationID`

## Confidence

Derived (cross-referencing the two sources; see `data-model.md`). Whether this reflects a deliberate platform restriction or simply that ASG's tenant never placed those fields is unresolved — see Open Questions there

---

Source: `docs/modules/facilities-locations/rules.md`
