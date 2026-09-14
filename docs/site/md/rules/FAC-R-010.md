# FAC-R-010 — A Facility may defer its address to its parent Location

*Facilities, Locations & Sites · Inferred*

**Input: `Facility.UseLocationAddress` (Boolean, Required = Yes — the flag itself must always be set one way or the other). Effect: When true, the Facility is presumed to use `Location`'s address fields rather than its own `StreetAddress1..4`/`City`/`PostalCode`.**

Input: `Facility.UseLocationAddress` (Boolean, Required = Yes — the flag itself must always be set one way or the other). Effect: When true, the Facility is presumed to use `Location`'s address fields rather than its own `StreetAddress1..4`/`City`/`PostalCode`. Confidence: Inferred — plausible from the field name and the required-boolean pattern, not confirmed by any screen capture of the resulting render behaviour.

## What it constrains

[Facility](../entities/Facility.md), [Location](../entities/Location.md)

Columns named: `Facility.UseLocationAddress`

## Confidence

Inferred — plausible from the field name and the required-boolean pattern, not confirmed by any screen capture of the resulting render behaviour

---

Source: `docs/modules/facilities-locations/rules.md`
