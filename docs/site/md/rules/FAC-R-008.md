# FAC-R-008 — Complex membership is optional and available to four different entity types

*Facilities, Locations & Sites · Observed*

**Input: `ComplexID` on `Facility`, `Location`, `Parcel`, `Prototype` (all `Required = No` where exposed) and `Competitor`. Effect: Any of the four subtype roots — and a tracked competitor — may be grouped under one shared shopping-center/campus record, or none.**

Input: `ComplexID` on `Facility`, `Location`, `Parcel`, `Prototype` (all `Required = No` where exposed) and `Competitor`. Effect: Any of the four subtype roots — and a tracked competitor — may be grouped under one shared shopping-center/campus record, or none. `Complex` itself carries no count or capacity field, so the platform does not enforce or expose how many children a Complex actually has. Confidence: Observed (FK presence/optionality); "no capacity enforcement" is Derived (absence of any such column in Complex's 45 fields).

## What it constrains

[Facility](../entities/Facility.md), [Location](../entities/Location.md), [Parcel](../entities/Parcel.md), [Prototype](../entities/Prototype.md), [Competitor](../entities/Competitor.md), [Complex](../entities/Complex.md)

## Confidence

Observed (FK presence/optionality); "no capacity enforcement" is Derived (absence of any such column in Complex's 45 fields)

---

Source: `docs/modules/facilities-locations/rules.md`
