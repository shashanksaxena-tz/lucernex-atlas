# FAC-R-009 — Complex sits above the hierarchy and has no parent of its own

*Facilities, Locations & Sites · Derived*

**Effect: `Complex`'s 45-field schema contains no FK back into `Location`/`Facility`/`Parcel`/ `Prototype`/`Program`, and no `ProjectEntityID`. It is `firm_global`, not entity-scoped.**

Effect: `Complex`'s 45-field schema contains no FK back into `Location`/`Facility`/`Parcel`/ `Prototype`/`Program`, and no `ProjectEntityID`. It is `firm_global`, not entity-scoped. Confidence: Derived (exhaustive field-list read), corroborated by `../../data-model/project-entity.md` §2's independent classification of `Complex` as one of the 52 firm-global objects.

## What it constrains

[Complex](../entities/Complex.md), [Location](../entities/Location.md), [Facility](../entities/Facility.md), [Parcel](../entities/Parcel.md), [Prototype](../entities/Prototype.md), [Program](../entities/Program.md)

## Confidence

Derived (exhaustive field-list read), corroborated by `../../data-model/project-entity.md` §2's independent classification of `Complex` as one of the 52 firm-global objects

---

Source: `docs/modules/facilities-locations/rules.md`
