# PLT-R-010 — Geography is two-level: country/state master, then jurisdiction

*Platform & Tenancy · Derived*

**Every address block in the product repeats the same `StreetAddress1..4`/`City`/ `PostalCode`/`CountryID`/`JurisdictionID` shape and resolves tax rate through `Jurisdiction`, not through the country/state master directly.**

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | Any address capture on `Facility`, `Location`, `Parcel`, `Project`, `ProjectEntity`, or a person/company record in `people-parties` |
| What it reads | `StateProvinceCountryID` → `StateProvinceCountry` (ISO Alpha-2/3 codes); `JurisdictionID` → `Jurisdiction` (adds `TaxRate1`/`TaxRate2`) |
| What it writes | Every address block in the product repeats the same `StreetAddress1..4`/`City`/ `PostalCode`/`CountryID`/`JurisdictionID` shape and resolves tax rate through `Jurisdiction`, not through the country/state master directly |

## What it constrains

[Facility](../entities/Facility.md), [Location](../entities/Location.md), [Parcel](../entities/Parcel.md), [Project](../entities/Project.md), [ProjectEntity](../entities/ProjectEntity.md), [StateProvinceCountry](../entities/StateProvinceCountry.md), [Jurisdiction](../entities/Jurisdiction.md)

## Confidence

Derived — repeated field-block signature across every address-carrying object in `data-model.md` and `../../data-model/object-catalog.md`

---

Source: `docs/modules/platform-tenancy/rules.md`
