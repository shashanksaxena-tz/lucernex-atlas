# FAC-R-012 — Contract attaches to Facility and Location directly, not only through one another

*Facilities, Locations & Sites · Observed*

**Input: `Contract.FacilityID`, `Contract.LocationID` (both present, both optional per 009). Effect: A lease can be tied to a Location without a Facility, a Facility without going through a Location lookup, or both at once — the two attachment points are independent, not a forced traversal through….**

Input: `Contract.FacilityID`, `Contract.LocationID` (both present, both optional per 009). Effect: A lease can be tied to a Location without a Facility, a Facility without going through a Location lookup, or both at once — the two attachment points are independent, not a forced traversal through one to reach the other. Confidence: Observed (009's schema-browser capture of `Contract.FacilityID`/`LocationID` as separate typed columns).

## What it constrains

[Contract](../entities/Contract.md)

Columns named: `Contract.FacilityID`, `Contract.LocationID`

## Confidence

Observed (009's schema-browser capture of `Contract.FacilityID`/`LocationID` as separate typed columns)

---

Source: `docs/modules/facilities-locations/rules.md`
