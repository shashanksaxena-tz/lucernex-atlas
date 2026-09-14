# POR-R-003

*Portfolio & Real-Estate Transactions · Observed*

**A user opens a `Facility`/`Location`/`Parcel`/`Prototype`/`Contract`/`CapProject`/`OpenProject`/`EquipmentContract` detail screen under a given Portfolio · `Program.<Subtype>SetupPageLayoutID` · Overrides the tenant-wide default from `Firm.<Subtype>SetupPageLayoutID` for that Portfolio. Two….**

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | A user opens a `Facility`/`Location`/`Parcel`/`Prototype`/`Contract`/`CapProject`/`OpenProject`/`EquipmentContract` detail screen under a given Portfolio |
| Stated as | `Program.<Subtype>SetupPageLayoutID` |
| Stated as | Overrides the tenant-wide default from `Firm.<Subtype>SetupPageLayoutID` for that Portfolio. Two additional fields, `SiteToProjectSetupLayoutID` and `ProjectToFacilitySetupLayoutID`, exist only on `Program` and name a conversion between subtypes rather than one subtype's own layout — see `POR-R-012`. |
| Stated as | Observed field existence; Inferred override semantics |

## What it constrains

[Facility](../entities/Facility.md), [Location](../entities/Location.md), [Parcel](../entities/Parcel.md), [Prototype](../entities/Prototype.md), [Contract](../entities/Contract.md), [Program](../entities/Program.md)

## Rules it cites

[POR-R-012](POR-R-012.md)

---

Source: `docs/modules/portfolio-transactions/rules.md`
