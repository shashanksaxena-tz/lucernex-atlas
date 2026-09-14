# Project

*111 fields · module: Platform & Tenancy · Postgres: `project`*

A lightweight project identity record (ID, RecID, UUID) distinct from the richer ProjectEntity, likely used for cross-system reference linking.

Source: `data-fields/small-miscellaneous-entities.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 111 |
| Catalogued fields | 6 (6 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 14 other records |
| Tenancy position | subtype_root |
| Rules that name it | 6 |

## What to know before rebuilding this

### 6 tenant custom columns

**Observed.** This record carries 6 physical Firm_-prefixed columns — tenant custom fields are real columns, not rows in a value store, so adding one is a DDL change. That is direct evidence for database-per-tenant and against a shared schema.

### A ProjectEntity subtype root

**Derived.** One of the nine records that are themselves a kind of ProjectEntity rather than hanging off one. The discriminator is ProjectEntityTypeName, which is how a single table serves several apparent record types.

### Census and catalogue disagree

**Observed.** The object census declares 111 fields; the Data Fields catalogue lists 6. The 105-field gap is columns the platform holds but does not expose as configurable Data Fields — a rebuild that reads only the catalogue will miss them.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [ACC-R-061](../rules/ACC-R-061.md) | the form type declares attachability as a Boolean per entity kind. For this form type, only `Portfolio` = Yes and `RE Contract` = Yes; `Capital Program`, `Prototype`, `Location`, `Parcel`, `Site`, `Project`, `Facility`, `Capital Project` an | Observed |
| [FAC-R-018](../rules/FAC-R-018.md) | Input: `Ownership`, `SiteSurvey`, `LandPurchaseSummary`, `LinkLandPurchaseInspection`, `DemographicResults` carry `ProjectEntityID` and no hard-typed FK to `Facility`/`Location`/`Parcel`. Effect: In principle any of these can attach to any  | Derived |
| [PLT-R-010](../rules/PLT-R-010.md) | Every address block in the product repeats the same `StreetAddress1..4`/`City`/ `PostalCode`/`CountryID`/`JurisdictionID` shape and resolves tax rate through `Jurisdiction`, not through the country/state master directly | Derived |
| [PLT-R-016](../rules/PLT-R-016.md) | Do not silently pick one; `../../data-model/project-entity.md` is built on `ProjectEntity` and is the authority for the spine, but `Project`'s role remains genuinely open | Derived |
| [POR-R-010](../rules/POR-R-010.md) | A physical site's lifecycle needs to distinguish "building it" from "leasing it" · `Project.ProjectType` = "Opening Project or Capital Project" (`Project`, `platform-tenancy`) vs. `Contract` (`contracts-leases`) · Two independent subtype ro | Derived |
| [POR-R-012](../rules/POR-R-012.md) | A Site is promoted toward becoming an operating asset · `Program.SiteToProjectSetupLayoutID`, then `Program.ProjectToFacilitySetupLayoutID` · Names a two-step conversion pipeline (Site → Project → Facility). The second step is corroborated  | Derived |

## Fields

### Relationships (foreign keys) (12)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BudgetTemplateID` |  | Template ID | — |  | [BudgetTemplate](BudgetTemplate.md) |
| `ComplexID` |  | Complex ID | — |  | [Complex](Complex.md) |
| `DemographicDMAID` |  | DMA ID | — |  | [DMA](DMA.md) |
| `FacilityID` | Related Project Facility | Facility ID | Global |  | [Facility](Facility.md) |
| `IStateProvinceCountryID` |  | Country, State, County ID | — |  | [StateProvinceCountry](StateProvinceCountry.md) |
| `JurisdictionID` |  | County ID | — |  | [Jurisdiction](Jurisdiction.md) |
| `LocationID` |  | Location ID | — |  | [Location](Location.md) |
| `ProgramID` |  | Portfolio ID | — |  | [Program](Program.md) |
| `PrototypeID` |  | Prototype ID | — |  | [Prototype](Prototype.md) |
| `RegionID` |  | Region ID | — |  | [Region](Region.md) |
| `RootRegionID` |  | Region ID | — |  | [Region](Region.md) |
| `SubRegionID` |  | Region ID | — |  | [Region](Region.md) |

### Soft references (2)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `LinkProjectEntityContactListData` |  | Contact | — |  |  |
| `ManagerIDList` |  | Dropdown | — |  |  |

### Coded values (drop-downs) (11)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeBuildingAreaUnitID` |  | Dropdown (Building Area Unit Code) | — |  | Building Area Unit Code |
| `CodeConstructionTypeID` |  | Dropdown (Construction Type Code) | — |  | Construction Type Code |
| `CodeCurrencyTypeID` |  | Dropdown (Currency Type Code) | — |  | Currency Type Code |
| `CodeDealTypeID` |  | Dropdown (Deal Type Code) | — |  | Deal Type Code |
| `CodeDesc_CodeMarketAreaID` |  | Dropdown (Market Area Code) | — |  | Market Area Code |
| `CodeDesc_CodeProjectTypeID` |  | Dropdown (Project Type Code) | — |  | Project Type Code |
| `CodeDistributionCenterID` |  | Dropdown (Distribution Center Code) | — |  | Distribution Center Code |
| `CodeMarketAreaID` |  | Dropdown (Market Area Code) | — |  | Market Area Code |
| `CodeMarketTypeID` |  | Dropdown (Market Type Code) | — |  | Market Type Code |
| `CodeProjectTypeID` |  | Dropdown (Project Type Code) | — |  | Project Type Code |
| `CurrentCodeProjectPhaseID` |  | Dropdown (Project Phase Code) | — |  | Project Phase Code |

### Money (1)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Firm_PriorMonthAccrualTotal` |  | Currency | — |  |  |

### Quantities (15)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ActualRevenueWeeks` |  | Number | — |  |  |
| `DBFolderSizeMB` |  | 2-Digit Number | — |  |  |
| `Depth` |  | Number | — |  |  |
| `EntityId` |  | Number | — |  |  |
| `Frontage` |  | Number | — |  |  |
| `GrossArea` |  | Number | — |  |  |
| `LatitudeDegrees` |  | 5-Digit Number | — |  |  |
| `LongitudeDegrees` |  | 5-Digit Number | — |  |  |
| `NumberOfDocuments` |  | Number | — |  |  |
| `ProjectEntityID` |  | Number | — |  |  |
| `ProjectID` | Project RecID | Number | Global |  |  |
| `RentableArea` |  | Number | — |  |  |
| `SequenceNumber` |  | Number | — |  |  |
| `SiteSequenceNumber` | Site Sequence Number | Number | Global |  |  |
| `UsableArea` |  | Number | — |  |  |

### Dates & timestamps (8)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ActualEndDate` |  | Date | — |  |  |
| `ActualStartDate` |  | Date | — |  |  |
| `BaselineEndDate` |  | Date | — |  |  |
| `ClientScheduleLastReviewedDate` |  | Date | — |  |  |
| `ExpectedEndDate` |  | Date | — |  |  |
| `OriginalEndDate` |  | Date | — |  |  |
| `OriginalStartDate` |  | Date | — |  |  |
| `SlotEndDate` |  | Date | — |  |  |

### Flags (2)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Inactive` |  | Boolean | — |  |  |
| `IsDead` |  | Boolean | — |  |  |

### Text & notes (54)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BaseProvider` |  | Text | — |  |  |
| `City` |  | Text | — |  |  |
| `CityStateProvinceCountry` |  | Text | — |  |  |
| `ClientEntityID` | Project ID | Text | Global |  |  |
| `ComparisonList` |  | Text | — |  |  |
| `CompletedPhaseStatus` |  | Text | — |  |  |
| `ConstructionPhaseStatus` |  | Text | — |  |  |
| `CountryID` |  | Text | — |  |  |
| `CrossStreet1` |  | Text | — |  |  |
| `CrossStreet2` |  | Text | — |  |  |
| `CurrentMilestone` |  | Text | — |  |  |
| `CurrentPhaseStatus` |  | Text | — |  |  |
| `DesignPhaseStatus` |  | Text | — |  |  |
| `EntityEmail` |  | Text | — |  |  |
| `EntityPhoto` |  | Text | — |  |  |
| `FacilityName` |  | Text | — |  |  |
| `FinancialModel` |  | Text | — |  |  |
| `FirmID` |  | Text | — |  |  |
| `Firm_SalesReportLogo` |  | Text | — |  |  |
| `Firm_SalesReportLogoMadewell` |  | Text | — |  |  |
| `Firm_SalesReportSignature` |  | Text | — |  |  |
| `Firm_SalesReportSignatureName` |  | Text | — |  |  |
| `Firm_SalesReportSignatureTitle` |  | Text | — |  |  |
| `HTMLAddress` |  | Text | — |  |  |
| `IssuesAndAlerts` |  | Text | — |  |  |
| `MapClientRecordID` |  | Text | — |  |  |
| `MilestoneTimeline` |  | Text | — |  |  |
| `NextMilestone` |  | Text | — |  |  |
| `Notes` |  | Text | — |  |  |
| `OperationsPhaseStatus` |  | Text | — |  |  |
| `Phone` |  | Text | — |  |  |
| `PossessionPhaseStatus` |  | Text | — |  |  |
| `PostalCode` |  | Text | — |  |  |
| `PotentialProjectName` |  | Text | — |  |  |
| `PreviousMilestone` |  | Text | — |  |  |
| `ProgramName` |  | Text | — |  |  |
| `ProjectDescription` |  | Text | — |  |  |
| `ProjectEntityName` |  | Text | — |  |  |
| `ProjectEntityTypeName` |  | Text | — |  |  |
| `ProjectName` |  | Text | — |  |  |
| `ProjectType` | Opening Project or Capital Project | Text | Global | yes |  |
| `PrototypeName` |  | Text | — |  |  |
| `RealEstatePhaseStatus` |  | Text | — |  |  |
| `RelatedEntities` |  | Text | — |  |  |
| `RelocatedFrom` |  | Text | — |  |  |
| `RunReportAction` |  | Text | — |  |  |
| `StreetAddress` |  | Text | — |  |  |
| `StreetAddress1` |  | Text | — |  |  |
| `StreetAddress2` |  | Text | — |  |  |
| `StreetAddress3` |  | Text | — |  |  |
| `StreetAddress4` |  | Text | — |  |  |
| `ThirdPartyWarehouse` |  | Text | — |  |  |
| `TimeZone` |  | Text | — |  |  |
| `TradeArea` |  | Text | — |  |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CreatedByID` |  | Member ID | — |  | [Member](Member.md) |
| `CreatedDate` |  | Time | — |  |  |
| `ModifiedByID` |  | Member ID | — |  | [Member](Member.md) |
| `ModifiedDate` |  | Time | — |  |  |
| `RevNumber` |  | Number | — |  |  |
| `UUID` | Project UUID | Text | Global |  |  |
