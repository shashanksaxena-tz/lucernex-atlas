# FAC-R-005 — A Parcel's mandatory containment parent is its Location, not its Facility

*Facilities, Locations & Sites · Observed*

**Input: `Parcel.LocationID` (Required = Yes) vs. `Parcel.FacilityID` (Required = No).**

Input: `Parcel.LocationID` (Required = Yes) vs. `Parcel.FacilityID` (Required = No). Effect: A Parcel can exist under a Location with no building yet on it; a Facility on that Parcel is an optional refinement, added once construction identifies which building sits on which piece of land. Confidence: Observed (`../../data-fields/parcel.md`).

## What it constrains

[Parcel](../entities/Parcel.md)

Columns named: `Parcel.LocationID`, `Parcel.FacilityID`

## Confidence

Observed (`../../data-fields/parcel.md`)

---

Source: `docs/modules/facilities-locations/rules.md`
