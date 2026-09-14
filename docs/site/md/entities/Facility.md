# Facility

*133 fields · module: Facilities, Locations & Sites · Postgres: `facility`*

The physical property/building record — address fields (Street Address #1-3, City, State, Postal Code, Jurisdiction) plus facility-level dates and area figures. 89 fields (88 Global, 1 Firm) under its own top-level Facility group; this is the most 'plain real estate' entity in the catalog, closer to a CRM property record than a financial one, which is reflected in the dominance of TEXT and DATE field types over MONEY.

Source: `data-fields/facility.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 133 |
| Catalogued fields | 89 (88 global, 1 firm) |
| Physical tables | 1 |
| Referenced by | 7 keys from 7 record types |
| Points at | 13 other records |
| Tenancy position | subtype_root |
| Rules that name it | 13 |

## What to know before rebuilding this

### 8 tenant custom columns

**Observed.** This record carries 8 physical Firm_-prefixed columns — tenant custom fields are real columns, not rows in a value store, so adding one is a DDL change. That is direct evidence for database-per-tenant and against a shared schema.

### A ProjectEntity subtype root

**Derived.** One of the nine records that are themselves a kind of ProjectEntity rather than hanging off one. The discriminator is ProjectEntityTypeName, which is how a single table serves several apparent record types.

### Census and catalogue disagree

**Observed.** The object census declares 133 fields; the Data Fields catalogue lists 89. The 44-field gap is columns the platform holds but does not expose as configurable Data Fields — a rebuild that reads only the catalogue will miss them.

### 1 catalogued Firm-scope fields

**Observed.** Of 89 catalogued fields on this record, 1 are Firm scope — defined by this tenant rather than shipped by the platform. Firm-scope definitions are RGAF rows carrying IsGlobal, FirmID and IsClientExtensionField.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [ACC-R-061](../rules/ACC-R-061.md) | the form type declares attachability as a Boolean per entity kind. For this form type, only `Portfolio` = Yes and `RE Contract` = Yes; `Capital Program`, `Prototype`, `Location`, `Parcel`, `Site`, `Project`, `Facility`, `Capital Project` an | Observed |
| [FAC-R-001](../rules/FAC-R-001.md) | Trigger: Facility create/save. Input: `Facility.LocationID`. | Observed |
| [FAC-R-003](../rules/FAC-R-003.md) | Trigger: Facility create/save. Input: `Facility.ProgramID`, typed `Portfolio ID`. | Observed |
| [FAC-R-008](../rules/FAC-R-008.md) | Input: `ComplexID` on `Facility`, `Location`, `Parcel`, `Prototype` (all `Required = No` where exposed) and `Competitor`. Effect: Any of the four subtype roots — and a tracked competitor — may be grouped under one shared shopping-center/cam | Observed |
| [FAC-R-009](../rules/FAC-R-009.md) | Effect: `Complex`'s 45-field schema contains no FK back into `Location`/`Facility`/`Parcel`/ `Prototype`/`Program`, and no `ProjectEntityID`. It is `firm_global`, not entity-scoped. | Derived |
| [FAC-R-010](../rules/FAC-R-010.md) | Input: `Facility.UseLocationAddress` (Boolean, Required = Yes — the flag itself must always be set one way or the other). Effect: When true, the Facility is presumed to use `Location`'s address fields rather than its own `StreetAddress1..4` | Inferred |
| [FAC-R-013](../rules/FAC-R-013.md) | Effect: From `Facility`'s own Related Fields sidebar, `Contract` does not appear as a related lookup at all; instead the Facility Summary layout embeds an **"ASG Contract List (One to Many List)"** child grid. | Observed |
| [FAC-R-018](../rules/FAC-R-018.md) | Input: `Ownership`, `SiteSurvey`, `LandPurchaseSummary`, `LinkLandPurchaseInspection`, `DemographicResults` carry `ProjectEntityID` and no hard-typed FK to `Facility`/`Location`/`Parcel`. Effect: In principle any of these can attach to any  | Derived |
| [FAC-R-019](../rules/FAC-R-019.md) | Input: `Prototype.LocationID`, `.ComplexID`, `.DemographicDMAID` are declared columns in `_lucernex_objects_summary.txt` but do not appear anywhere in `../../data-fields/prototype.md`'s 15-row catalog. Effect: Unlike the identical columns o | Observed |
| [PLT-R-010](../rules/PLT-R-010.md) | Every address block in the product repeats the same `StreetAddress1..4`/`City`/ `PostalCode`/`CountryID`/`JurisdictionID` shape and resolves tax rate through `Jurisdiction`, not through the country/state master directly | Derived |
| [POR-R-003](../rules/POR-R-003.md) | A user opens a `Facility`/`Location`/`Parcel`/`Prototype`/`Contract`/`CapProject`/`OpenProject`/`EquipmentContract` detail screen under a given Portfolio · `Program.<Subtype>SetupPageLayoutID` · Overrides the tenant-wide default from `Firm. | Observed |
| [POR-R-006](../rules/POR-R-006.md) | A `RETransaction` is opened against a site the tenant may already occupy · `RETransaction.FacilityID` · Optional direct FK to an existing `Facility` — a renewal/expansion transaction can name its Facility before any Scenario or Contract exi | Observed |
| [POR-R-011](../rules/POR-R-011.md) | Any process needs to trace a `Facility`/`Location` back to the `PotentialProject` it originated from · (none — no such column exists) · Not possible via FK. `PotentialProject` has zero inbound edges in the 972-edge graph and zero Manage Dat | Observed |

## Fields

### Relationships (foreign keys) (11)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BudgetTemplateID` |  | Template ID | — |  | [BudgetTemplate](BudgetTemplate.md) |
| `ComplexID` |  | Complex ID | — |  | [Complex](Complex.md) |
| `DemographicDMAID` |  | DMA ID | — |  | [DMA](DMA.md) |
| `IStateProvinceCountryID` | State | Country, State, County ID | Global |  | [StateProvinceCountry](StateProvinceCountry.md) |
| `JurisdictionID` | Jurisdiction | County ID | Global |  | [Jurisdiction](Jurisdiction.md) |
| `LocationID` | Location | Location ID | Global | yes | [Location](Location.md) |
| `ProgramID` | Portfolio | Portfolio ID | Global | yes | [Program](Program.md) |
| `PrototypeID` | Prototype | Prototype ID | Global |  | [Prototype](Prototype.md) |
| `RegionID` | Region | Region ID | Global | yes | [Region](Region.md) |
| `RootRegionID` | Parent Region | Region ID | Global |  | [Region](Region.md) |
| `SubRegionID` | Sub Region | Region ID | Global |  | [Region](Region.md) |

### Soft references (3)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `LinkProjectEntityContactListData` |  | Contact | — |  |  |
| `ManagerIDList` | Project Managers | Dropdown | Global |  |  |
| `OpeningProjectPEID` | Opening Project | Entity | Global |  |  |

### Coded values (drop-downs) (16)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeBuildingAreaUnitID` | Building Area Unit | Dropdown (Building Area Unit Code) | Global |  | Building Area Unit Code |
| `CodeConstructionTypeID` | Construction Type | Dropdown (Construction Type Code) | Global |  | Construction Type Code |
| `CodeCurrencyTypeID` |  | Dropdown (Currency Type Code) | — |  | Currency Type Code |
| `CodeDealTypeID` | Deal Type | Dropdown (Deal Type Code) | Global |  | Deal Type Code |
| `CodeDesc_CodeMarketAreaID` | Market Potential | Dropdown (Market Area Code) | Global |  | Market Area Code |
| `CodeDesc_CodeProjectTypeID` | Real Estate Type | Dropdown (Project Type Code) | Global |  | Project Type Code |
| `CodeDistributionCenterID` | Distribution Center | Dropdown (Distribution Center Code) | Global |  | Distribution Center Code |
| `CodeFacilityCategoryID` | Facility Category | Dropdown (Facility Category Code) | Global |  | Facility Category Code |
| `CodeFacilityGroupID` | Facility Group | Dropdown (Facility Group Code) | Global |  | Facility Group Code |
| `CodeFacilityStatusID` | Facility Status | Dropdown (Facility Status Code) | Global |  | Facility Status Code |
| `CodeFacilityTypeID` | Facility Type | Dropdown (Facility Type Code) | Global |  | Facility Type Code |
| `CodeFacilityUseID` | Facility Use | Dropdown (Facility Use Code) | Global |  | Facility Use Code |
| `CodeMarketAreaID` | Market Area | Dropdown (Market Area Code) | Global | yes | Market Area Code |
| `CodeMarketTypeID` | Market Type | Dropdown (Market Type Code) | Global |  | Market Type Code |
| `CodeProjectTypeID` | Project Type | Dropdown (Project Type Code) | Global |  | Project Type Code |
| `CurrentCodeProjectPhaseID` |  | Dropdown (Project Phase Code) | — |  | Project Phase Code |

### Money (2)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Firm_PriorMonthAccrualTotal` |  | Currency | — |  |  |
| `LastYearsAnnualSales` | Last Years Annual Sales | Currency | Global |  |  |

### Quantities (20)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ActualRevenueWeeks` |  | Number | — |  |  |
| `BehindScheduleDays` | Behind Schedule Days | Number | Global |  |  |
| `DBFolderSizeMB` |  | 2-Digit Number | — |  |  |
| `DaysUntilOpen` | Days Until Open | Number | Global |  |  |
| `Depth` |  | Number | Global |  |  |
| `DistributionCenterArea` | Distribution Center Area | Number | Global |  |  |
| `EntityId` |  | Number | — |  |  |
| `FacilityID` | Facility RecID | Number | Global |  |  |
| `Firm_SellingSQFT` |  | Number | — |  |  |
| `Frontage` |  | Number | Global |  |  |
| `GrossArea` | Gross Area | Number | Global |  |  |
| `LatitudeDegrees` |  | 5-Digit Number | — |  |  |
| `LongitudeDegrees` |  | 5-Digit Number | — |  |  |
| `NumberOfDocuments` |  | Number | — |  |  |
| `OpenYear` | Open year | Number | Global |  |  |
| `OutOfDateDays` | Out Of Date Days | Number | Global |  |  |
| `ProjectEntityID` | Entity RecID | Number | Global | yes |  |
| `RentableArea` | Rentable Area | Number | Global |  |  |
| `SequenceNumber` | Sequence Number | Number | Global |  |  |
| `UsableArea` | Usable Area | Number | Global |  |  |

### Dates & timestamps (13)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ActualEndDate` | Actual/Forecast Delivery Date | Date | Global |  |  |
| `ActualStartDate` |  | Date | — |  |  |
| `BaselineEndDate` | Baseline End date | Date | Global |  |  |
| `BaselineStartDate` | Baseline Start Date | Date | Global |  |  |
| `ClientScheduleLastReviewedDate` |  | Date | — |  |  |
| `CloseDate` | Close Date | Date | Global |  |  |
| `ConstructionDate` | Construction Date | Date | Global |  |  |
| `ExpectedEndDate` | Original Delivery Qtr/Yr | Date | Global |  |  |
| `OpenDate` | Open Date | Date | Global |  |  |
| `OriginalEndDate` |  | Date | — |  |  |
| `OriginalStartDate` |  | Date | — |  |  |
| `RemodelDate` | Remodel Date | Date | Global |  |  |
| `SlotEndDate` | RE Planner Open Date | Date | Global |  |  |

### Flags (3)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Inactive` | Is Inactive? | Boolean | Global | yes |  |
| `IsDead` | Is Dead? | Boolean | Global | yes |  |
| `UseLocationAddress` | Use Location Address | Boolean | Global | yes |  |

### Text & notes (58)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BaseProvider` |  | Text | — |  |  |
| `City` |  | Text | Global |  |  |
| `CityStateProvinceCountry` |  | Text | — |  |  |
| `ClientEntityID` | Facility ID | Text | Global |  |  |
| `ComparisonList` |  | Text | — |  |  |
| `CompletedPhaseStatus` |  | Text | — |  |  |
| `ConstructionPhaseStatus` | Construction Phase Status | Text | Global |  |  |
| `CountryID` | Country | Text | Global |  |  |
| `CrossStreet1` |  | Text | — |  |  |
| `CrossStreet2` |  | Text | — |  |  |
| `CurrentMilestone` |  | Text | — |  |  |
| `CurrentPhaseStatus` | Project Status | Text | Global |  |  |
| `DefinedField1` | Defined Field #1 | Text | Global |  |  |
| `DefinedField2` | Defined Field #2 | Text | Global |  |  |
| `DesignPhaseStatus` | Design Phase Status | Text | Global |  |  |
| `EntityEmail` |  | Text | — |  |  |
| `EntityPhoto` | Entity Photo | Text | Global |  |  |
| `FacilityName` | Facility Name | Text | Global | yes |  |
| `FinancialModel` |  | Text | — |  |  |
| `FirmID` |  | Text | — |  |  |
| `Firm_SalesReportLogo` |  | Text | — |  |  |
| `Firm_SalesReportLogoMadewell` |  | Text | — |  |  |
| `Firm_SalesReportSignature` |  | Text | — |  |  |
| `Firm_SalesReportSignatureName` |  | Text | — |  |  |
| `Firm_SalesReportSignatureTitle` |  | Text | — |  |  |
| `Firm_SpaceNumber` | Space Number | Text | Firm |  |  |
| `HTMLAddress` | Full Address | Text | Global |  |  |
| `HoursOfOperation` | Hours Of Operation | Text | Global |  |  |
| `IssuesAndAlerts` | Issues And Alerts | Text | Global |  |  |
| `MapClientRecordID` |  | Text | — |  |  |
| `MilestoneTimeline` |  | Text | — |  |  |
| `NextMilestone` |  | Text | — |  |  |
| `Notes` |  | Text | Global |  |  |
| `OperatingStatus` | Operating Status | Text | Global | yes |  |
| `OperationsPhaseStatus` | Operations Phase Status | Text | Global |  |  |
| `Phone` |  | Text | Global |  |  |
| `PossessionPhaseStatus` | Possession Phase Status | Text | Global |  |  |
| `PostalCode` | Postal Code | Text | Global |  |  |
| `PotentialProjectName` |  | Text | — |  |  |
| `PreviousMilestone` |  | Text | — |  |  |
| `ProgramName` |  | Text | — |  |  |
| `ProjectDescription` | Description | Text | Global |  |  |
| `ProjectEntityName` |  | Text | — |  |  |
| `ProjectEntityTypeName` |  | Text | — |  |  |
| `ProjectName` |  | Text | — |  |  |
| `PrototypeName` |  | Text | — |  |  |
| `RealEstatePhaseStatus` | Real Estate Phase Status | Text | Global |  |  |
| `RelatedEntities` | Related Facility Entities | Text | Global |  |  |
| `RelocatedFrom` |  | Text | — |  |  |
| `RunReportAction` |  | Text | — |  |  |
| `StreetAddress` | Street Address | Text | Global |  |  |
| `StreetAddress1` | Street Address #1 | Text | Global |  |  |
| `StreetAddress2` | Street Address #2 | Text | Global |  |  |
| `StreetAddress3` | Street Address #3 | Text | Global |  |  |
| `StreetAddress4` | Street Address #4 | Text | Global |  |  |
| `ThirdPartyWarehouse` | Third Party Warehouse | Text | Global |  |  |
| `TimeZone` | Time Zone | Text | Global |  |  |
| `TradeArea` | Trade Area | Text | Global |  |  |

### Audit & record keeping (7)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Facility ClientID | Text | Global | yes |  |
| `CreatedByID` |  | Member ID | — |  | [Member](Member.md) |
| `CreatedDate` |  | Time | — |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` |  | Number | — |  |  |
| `UUID` | Facility UUID | Text | Global |  |  |

## What points here (7 keys)

| Record type | Via column |
|---|---|
| [Contract](Contract.md) | `FacilityID` |
| [FacilityExpense](FacilityExpense.md) | `FacilityID` |
| [Parcel](Parcel.md) | `FacilityID` |
| [Parking](Parking.md) | `FacilityID` |
| [Project](Project.md) | `FacilityID` |
| [RETransaction](RETransaction.md) | `FacilityID` |
| [Space](Space.md) | `FacilityID` |
