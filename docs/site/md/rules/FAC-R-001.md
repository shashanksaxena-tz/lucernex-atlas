# FAC-R-001 — A Facility must belong to exactly one Location

*Facilities, Locations & Sites · Observed*

**Trigger: Facility create/save. Input: `Facility.LocationID`.**

Trigger: Facility create/save. Input: `Facility.LocationID`. Effect: Required FK; save is blocked without a Location. Confidence: Observed (`Required = Yes`, `../../data-fields/facility.md`).

## What it constrains

[Facility](../entities/Facility.md)

Columns named: `Facility.LocationID`

## Confidence

Observed (`Required = Yes`, `../../data-fields/facility.md`)

---

Source: `docs/modules/facilities-locations/rules.md`
