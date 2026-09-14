# Facilities, Locations & Sites

*In scope for the rebuild*

The physical estate and the site-selection data around it: Facility, Location, Complex, Parcel, Space, Parking, plus prototypes, demographics and site surveys.

Stated up front. This module is the physical real-estate register: 20 objects, 918 fields, built around four independently-ownable ProjectEntity subtype roots — Facility, Location, Parcel, Prototype — plus a shared optional container (Complex), a sub-Facility occupancy layer (Space/Tenant), and a site-selection/demographics family with no ASG Edge+ counterpart today. The central finding: Location is the retail site/"Center"; Facility is the building on it. A Location can hold more than one Facility; a Facility belongs to exactly one Location (Facility.LocationID is required; Location has no reverse pointer at all). Complex is an optional physical grouping above both — a shopping-mall/campus record that a Location, Facility, Parcel or Prototype may join, itself parentless. Parcel's mandatory containment parent is the Location, not the Facility, and it is the sole attachment point for the entire property-tax subsystem. Prototype is not a place at all — a reusable design template a Facility can be built from. "Site" is not one of this module's objects — it is PotentialProject, which lives in portfolio-transactions, the pre-development pipeline before any of the above exists. Full argument in location-vs-facility-vs-site.md.

|  | Count |
|---|---|
| Record types | 20 |
| Fields | 918 |
| Keys in | 34 |
| Keys out | 82 |
| Rules | 20 |

## Record types

| Record type | Postgres table | Fields | Referenced by |
|---|---|---|---|
| [Parcel](../entities/Parcel.md) | `parcel` | 154 | 8 |
| [Location](../entities/Location.md) | `location` | 141 | 9 |
| [Facility](../entities/Facility.md) | `facility` | 133 | 7 |
| [Prototype](../entities/Prototype.md) | `prototype` | 113 | 11 |
| [SiteSurvey](../entities/SiteSurvey.md) | `site_survey` | 79 | 0 |
| [Complex](../entities/Complex.md) | `complex` | 45 | 11 |
| [Tenant](../entities/Tenant.md) | `tenant` | 42 | 0 |
| [LandPurchaseSummary](../entities/LandPurchaseSummary.md) | `land_purchase_summary` | 35 | 0 |
| [Space](../entities/Space.md) | `space` | 27 | 1 |
| [Competitor](../entities/Competitor.md) | `competitor` | 26 | 0 |
| [FacilityExpense](../entities/FacilityExpense.md) | `facility_expense` | 22 | 0 |
| [ParcelAccess](../entities/ParcelAccess.md) | `parcel_access` | 20 | 0 |
| [Parking](../entities/Parking.md) | `parking` | 19 | 0 |
| [DemographicResults](../entities/DemographicResults.md) | `demographic_results` | 12 | 0 |
| [DemographicFact](../entities/DemographicFact.md) | `demographic_fact` | 10 | 0 |
| [DemographicReport](../entities/DemographicReport.md) | `demographic_report` | 10 | 0 |
| [Ownership](../entities/Ownership.md) | `ownership` | 9 | 0 |
| [LinkLandPurchaseInspection](../entities/LinkLandPurchaseInspection.md) | `link_land_purchase_inspection` | 8 | 0 |
| [DMA](../entities/DMA.md) | `d_m_a` | 7 | 10 |
| [DemographicStudyArea](../entities/DemographicStudyArea.md) | `demographic_study_area` | 6 | 0 |

## Rules

| Rule | Subject | What it requires | Confidence |
|---|---|---|---|
| [FAC-R-001](../rules/FAC-R-001.md) | A Facility must belong to exactly one Location | Trigger: Facility create/save. Input: `Facility.LocationID`. | Observed |
| [FAC-R-002](../rules/FAC-R-002.md) | A Location has no reverse pointer to any Facility | Trigger: N/A (structural). Effect: A Location's field set contains no `FacilityID`-typed column; | Observed |
| [FAC-R-003](../rules/FAC-R-003.md) | A Facility must belong to exactly one Portfolio (Program) | Trigger: Facility create/save. Input: `Facility.ProgramID`, typed `Portfolio ID`. | Observed |
| [FAC-R-004](../rules/FAC-R-004.md) | A Location must belong to exactly one Portfolio (Program) | Input: `Location.ProgramID`. Confidence: Observed (`Required = Yes`, `../../data-fields/location.md`). | Observed |
| [FAC-R-005](../rules/FAC-R-005.md) | A Parcel's mandatory containment parent is its Location, not its Facility | Input: `Parcel.LocationID` (Required = Yes) vs. `Parcel.FacilityID` (Required = No). | Observed |
| [FAC-R-006](../rules/FAC-R-006.md) | A Parcel must belong to exactly one Portfolio (Program) | Input: `Parcel.ProgramID`. Confidence: Observed (`../../data-fields/parcel.md`). | Observed |
| [FAC-R-007](../rules/FAC-R-007.md) | A Prototype must belong to exactly one Portfolio (Program) | Input: `Prototype.ProgramID`. Confidence: Observed (`../../data-fields/prototype.md`). | Observed |
| [FAC-R-008](../rules/FAC-R-008.md) | Complex membership is optional and available to four different entity types | Input: `ComplexID` on `Facility`, `Location`, `Parcel`, `Prototype` (all `Required = No` where exposed) and `Competitor`. Effect: Any of the four subtype roots — and a tracked competitor — may be grou | Observed |
| [FAC-R-009](../rules/FAC-R-009.md) | Complex sits above the hierarchy and has no parent of its own | Effect: `Complex`'s 45-field schema contains no FK back into `Location`/`Facility`/`Parcel`/ `Prototype`/`Program`, and no `ProjectEntityID`. It is `firm_global`, not entity-scoped. | Derived |
| [FAC-R-010](../rules/FAC-R-010.md) | A Facility may defer its address to its parent Location | Input: `Facility.UseLocationAddress` (Boolean, Required = Yes — the flag itself must always be set one way or the other). Effect: When true, the Facility is presumed to use `Location`'s address fields | Inferred |
| [FAC-R-011](../rules/FAC-R-011.md) | A Parcel may subdivide from another Parcel | Input: `Parcel.MasterParcelID` (self-reference, typed `Parcel ID`). Effect: Mirrors `Contract.MasterContractID`'s master/sub pattern exactly — a parcel of land can be split, with each resulting parcel | Observed |
| [FAC-R-012](../rules/FAC-R-012.md) | Contract attaches to Facility and Location directly, not only through one another | Input: `Contract.FacilityID`, `Contract.LocationID` (both present, both optional per 009). Effect: A lease can be tied to a Location without a Facility, a Facility without going through a Location loo | Observed |
| [FAC-R-013](../rules/FAC-R-013.md) | The reverse of Contract → Facility is composed as a child grid, not a lookup | Effect: From `Facility`'s own Related Fields sidebar, `Contract` does not appear as a related lookup at all; instead the Facility Summary layout embeds an **"ASG Contract List (One to Many List)"** ch | Observed |
| [FAC-R-014](../rules/FAC-R-014.md) | Property tax attaches only to the Parcel, never the Facility or the lease | Input: All six `PropertyTax*` objects (`PropertyTaxAppeal`, `PropertyTaxAppealAward`, `PropertyTaxAssessment`, `PropertyTaxBill`, `PropertyTaxDetail`, `PropertyTaxSummary`) carry a `ParcelID` FK and n | Observed |
| [FAC-R-015](../rules/FAC-R-015.md) | A Space must belong to exactly one Facility | Input: `Space.FacilityID`, Required = Yes. Confidence: Observed (`../../data-fields/space.md`). | Observed |
| [FAC-R-016](../rules/FAC-R-016.md) | A Space's lease link is optional | Input: `Space.ContractID`, Required = No. Effect: A Space can be defined on a Facility before any lease references it — e.g., during Space Management setup ahead of leasing. | Observed |
| [FAC-R-017](../rules/FAC-R-017.md) | A Tenant must belong to exactly one Space | Input: `Tenant.SpaceID`, typed `Space ID`. Confidence: Derived — the FK type is declared and every `Tenant` field (headcount, capacity, move-in/out dates) is scoped around occupying one space; | Derived |
| [FAC-R-018](../rules/FAC-R-018.md) | A generic-attachment child (soft `ProjectEntityID` only) is not restricted to this module's entity types | Input: `Ownership`, `SiteSurvey`, `LandPurchaseSummary`, `LinkLandPurchaseInspection`, `DemographicResults` carry `ProjectEntityID` and no hard-typed FK to `Facility`/`Location`/`Parcel`. Effect: In p | Derived |
| [FAC-R-019](../rules/FAC-R-019.md) | `Prototype`'s Location/Complex/DMA relationships exist in the schema but are not administrator-configurable | Input: `Prototype.LocationID`, `.ComplexID`, `.DemographicDMAID` are declared columns in `_lucernex_objects_summary.txt` but do not appear anywhere in `../../data-fields/prototype.md`'s 15-row catalog | Observed |
| [FAC-R-020](../rules/FAC-R-020.md) | `DemographicStudyArea` and `SiteSurvey`'s fixed mile-bands are two independent, non-integrated mechanisms for the same concept | Input: `SiteSurvey` carries `Population1Mile/3Miles/5Miles` (and six more metrics repeated the same way) as fixed columns; `DemographicStudyArea` carries `AreaRadius`/`AreaDriveTimeInMinutes` as a reu | Derived |
