# FAC-R-018 — A generic-attachment child (soft `ProjectEntityID` only) is not restricted to this module's entity types

*Facilities, Locations & Sites · Derived*

**Input: `Ownership`, `SiteSurvey`, `LandPurchaseSummary`, `LinkLandPurchaseInspection`, `DemographicResults` carry `ProjectEntityID` and no hard-typed FK to `Facility`/`Location`/`Parcel`. Effect: In principle any of these can attach to any of the eight/nine `ProjectEntity` subtype roots across the….**

Input: `Ownership`, `SiteSurvey`, `LandPurchaseSummary`, `LinkLandPurchaseInspection`, `DemographicResults` carry `ProjectEntityID` and no hard-typed FK to `Facility`/`Location`/`Parcel`. Effect: In principle any of these can attach to any of the eight/nine `ProjectEntity` subtype roots across the whole product (including `PotentialProject`/"Site", `Program`, `Project`, `Contract`), not only to a record in this module. Confidence: Derived — no screen capture shows which subtype a live row actually points at (see `demographics.md` Open Question 1).

## What it constrains

[Ownership](../entities/Ownership.md), [SiteSurvey](../entities/SiteSurvey.md), [LandPurchaseSummary](../entities/LandPurchaseSummary.md), [LinkLandPurchaseInspection](../entities/LinkLandPurchaseInspection.md), [DemographicResults](../entities/DemographicResults.md), [Facility](../entities/Facility.md), [Location](../entities/Location.md), [Parcel](../entities/Parcel.md), [ProjectEntity](../entities/ProjectEntity.md), [PotentialProject](../entities/PotentialProject.md), [Program](../entities/Program.md), [Project](../entities/Project.md)

## Confidence

Derived — no screen capture shows which subtype a live row actually points at (see `demographics.md` Open Question 1)

---

Source: `docs/modules/facilities-locations/rules.md`
