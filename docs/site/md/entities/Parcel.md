# Parcel

*154 fields · module: Facilities, Locations & Sites · Postgres: `parcel`*

The land-parcel record, distinct from Facility (building) and Location (site) — address fields plus parcel-specific attributes like Demographic DMA linkage, used primarily for ground-lease and land-purchase scenarios and as the anchor for the large PropertyTax* family (Assessment, Bill, Summary, Appeal, ParcelAccess). 74 Global fields under its own Parcel group.

Source: `data-fields/parcel.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 154 |
| Catalogued fields | 74 (74 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 8 keys from 8 record types |
| Points at | 18 other records |
| Tenancy position | subtype_root |
| Rules that name it | 10 |

## What to know before rebuilding this

### 6 tenant custom columns

**Observed.** This record carries 6 physical Firm_-prefixed columns — tenant custom fields are real columns, not rows in a value store, so adding one is a DDL change. That is direct evidence for database-per-tenant and against a shared schema.

### A ProjectEntity subtype root

**Derived.** One of the nine records that are themselves a kind of ProjectEntity rather than hanging off one. The discriminator is ProjectEntityTypeName, which is how a single table serves several apparent record types.

### Census and catalogue disagree

**Observed.** The object census declares 154 fields; the Data Fields catalogue lists 74. The 80-field gap is columns the platform holds but does not expose as configurable Data Fields — a rebuild that reads only the catalogue will miss them.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [ACC-R-061](../rules/ACC-R-061.md) | the form type declares attachability as a Boolean per entity kind. For this form type, only `Portfolio` = Yes and `RE Contract` = Yes; `Capital Program`, `Prototype`, `Location`, `Parcel`, `Site`, `Project`, `Facility`, `Capital Project` an | Observed |
| [FAC-R-005](../rules/FAC-R-005.md) | Input: `Parcel.LocationID` (Required = Yes) vs. `Parcel.FacilityID` (Required = No). | Observed |
| [FAC-R-006](../rules/FAC-R-006.md) | Input: `Parcel.ProgramID`. Confidence: Observed (`../../data-fields/parcel.md`). | Observed |
| [FAC-R-008](../rules/FAC-R-008.md) | Input: `ComplexID` on `Facility`, `Location`, `Parcel`, `Prototype` (all `Required = No` where exposed) and `Competitor`. Effect: Any of the four subtype roots — and a tracked competitor — may be grouped under one shared shopping-center/cam | Observed |
| [FAC-R-009](../rules/FAC-R-009.md) | Effect: `Complex`'s 45-field schema contains no FK back into `Location`/`Facility`/`Parcel`/ `Prototype`/`Program`, and no `ProjectEntityID`. It is `firm_global`, not entity-scoped. | Derived |
| [FAC-R-011](../rules/FAC-R-011.md) | Input: `Parcel.MasterParcelID` (self-reference, typed `Parcel ID`). Effect: Mirrors `Contract.MasterContractID`'s master/sub pattern exactly — a parcel of land can be split, with each resulting parcel pointing back at the original. | Observed |
| [FAC-R-018](../rules/FAC-R-018.md) | Input: `Ownership`, `SiteSurvey`, `LandPurchaseSummary`, `LinkLandPurchaseInspection`, `DemographicResults` carry `ProjectEntityID` and no hard-typed FK to `Facility`/`Location`/`Parcel`. Effect: In principle any of these can attach to any  | Derived |
| [FAC-R-019](../rules/FAC-R-019.md) | Input: `Prototype.LocationID`, `.ComplexID`, `.DemographicDMAID` are declared columns in `_lucernex_objects_summary.txt` but do not appear anywhere in `../../data-fields/prototype.md`'s 15-row catalog. Effect: Unlike the identical columns o | Observed |
| [PLT-R-010](../rules/PLT-R-010.md) | Every address block in the product repeats the same `StreetAddress1..4`/`City`/ `PostalCode`/`CountryID`/`JurisdictionID` shape and resolves tax rate through `Jurisdiction`, not through the country/state master directly | Derived |
| [POR-R-003](../rules/POR-R-003.md) | A user opens a `Facility`/`Location`/`Parcel`/`Prototype`/`Contract`/`CapProject`/`OpenProject`/`EquipmentContract` detail screen under a given Portfolio · `Program.<Subtype>SetupPageLayoutID` · Overrides the tenant-wide default from `Firm. | Observed |

## Fields

### Relationships (foreign keys) (16)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BudgetTemplateID` |  | Template ID | — |  | [BudgetTemplate](BudgetTemplate.md) |
| `ComplexID` | Complex Name | Complex ID | Global |  | [Complex](Complex.md) |
| `ContractID` | Contract | Contract ID | Global |  | [Contract](Contract.md) |
| `DemographicDMAID` | Demographic DMA | DMA ID | Global |  | [DMA](DMA.md) |
| `FacilityID` | Facility | Facility ID | Global |  | [Facility](Facility.md) |
| `IStateProvinceCountryID` | State | Country, State, County ID | Global |  | [StateProvinceCountry](StateProvinceCountry.md) |
| `JurisdictionID` | Jurisdiction | County ID | Global |  | [Jurisdiction](Jurisdiction.md) |
| `LocationID` | Location | Location ID | Global | yes | [Location](Location.md) |
| `MasterParcelID` | Master Parcel | Parcel ID | Global |  | [Parcel](Parcel.md) |
| `OrganizationID` | Organization | Organization ID | Global |  | [Organization](Organization.md) |
| `ProgramID` | Portfolio | Portfolio ID | Global | yes | [Program](Program.md) |
| `PrototypeID` |  | Prototype ID | — |  | [Prototype](Prototype.md) |
| `RegionID` |  | Region ID | — |  | [Region](Region.md) |
| `RootRegionID` |  | Region ID | — |  | [Region](Region.md) |
| `SubRegionID` |  | Region ID | — |  | [Region](Region.md) |
| `TaxJurisdictionID` | Tax Jurisdiction | County ID | Global |  | [Jurisdiction](Jurisdiction.md) |

### Soft references (2)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `LinkProjectEntityContactListData` |  | Contact | — |  |  |
| `ManagerIDList` |  | Dropdown | — |  |  |

### Coded values (drop-downs) (18)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeBuildingAreaUnitID` |  | Dropdown (Building Area Unit Code) | — |  | Building Area Unit Code |
| `CodeConstructionTypeID` |  | Dropdown (Construction Type Code) | — |  | Construction Type Code |
| `CodeCurrencyTypeID` | Currency Type | Dropdown (Currency Type Code) | Global |  | Currency Type Code |
| `CodeDealTypeID` |  | Dropdown (Deal Type Code) | — |  | Deal Type Code |
| `CodeDesc_CodeMarketAreaID` |  | Dropdown (Market Area Code) | — |  | Market Area Code |
| `CodeDesc_CodeProjectTypeID` |  | Dropdown (Project Type Code) | — |  | Project Type Code |
| `CodeDistributionCenterID` |  | Dropdown (Distribution Center Code) | — |  | Distribution Center Code |
| `CodeLandAreaUnitID` | Land Area Unit | Dropdown (Land Area Unit Code) | Global |  | Land Area Unit Code |
| `CodeMarketAreaID` |  | Dropdown (Market Area Code) | — |  | Market Area Code |
| `CodeMarketTypeID` |  | Dropdown (Market Type Code) | — |  | Market Type Code |
| `CodeParcelCategoryID` | Parcel Category | Dropdown (Parcel Category Code) | Global |  | Parcel Category Code |
| `CodeParcelGroupID` | Parcel Group | Dropdown (Parcel Group Code) | Global |  | Parcel Group Code |
| `CodeParcelStatusID` | Parcel Status | Dropdown (Parcel Status Code) | Global |  | Parcel Status Code |
| `CodeParcelTypeID` | Parcel Type | Dropdown (Parcel Type Code) | Global |  | Parcel Type Code |
| `CodeParcelUseID` | Parcel Use | Dropdown (Parcel Use Code) | Global |  | Parcel Use Code |
| `CodeProjectTypeID` |  | Dropdown (Project Type Code) | — |  | Project Type Code |
| `CodeTaxResponsibilityID` | Tax Responsibility | Dropdown (Responsible Party) | Global |  | Responsible Party |
| `CurrentCodeProjectPhaseID` |  | Dropdown (Project Phase Code) | — |  | Project Phase Code |

### Money (11)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Firm_PriorMonthAccrualTotal` |  | Currency | — |  |  |
| `ImprovementsAsessedAmount` | Improvements Assessed Amount | Currency | Global |  |  |
| `ImprovementsValueAmount` | Improvements Value Amount | Currency | Global |  |  |
| `LandAssessedAmount` | Land Assessed Amount | Currency | Global |  |  |
| `LandValueAmount` | Land Value Amount | Currency | Global |  |  |
| `OtherAssessedAmount` | Other Assessed Amount | Currency | Global |  |  |
| `OtherValueAmount` | Other Value Amount | Currency | Global |  |  |
| `PrimaryAssessedAmount` | Primary Assessed Amount | Currency | Global |  |  |
| `PrimaryValueAmount` | Primary Value Amount | Currency | Global |  |  |
| `SecondaryAssessedAmount` | Secondary Assessed Amount | Currency | Global |  |  |
| `SecondaryValueAmount` | Secondary Value Amount | Currency | Global |  |  |

### Quantities (16)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ActualRevenueWeeks` |  | Number | — |  |  |
| `DBFolderSizeMB` |  | 2-Digit Number | — |  |  |
| `Depth` |  | Number | — |  |  |
| `EntityId` |  | Number | — |  |  |
| `Frontage` |  | Number | — |  |  |
| `LatitudeDegrees` |  | 5-Digit Number | — |  |  |
| `LongitudeDegrees` |  | 5-Digit Number | — |  |  |
| `NumberOfDocuments` |  | Number | — |  |  |
| `OpenYear` | Open Year | Number | Global |  |  |
| `OutOfDateDays` | Out Of Date Days | Number | Global |  |  |
| `ParcelArea` | Parcel Area | Number | Global |  |  |
| `ParcelID` | Parcel RecID | Number | Global |  |  |
| `ProjectEntityID` |  | Number | — |  |  |
| `RentableArea` |  | Number | — |  |  |
| `SequenceNumber` |  | Number | — |  |  |
| `UsableArea` |  | Number | — |  |  |

### Dates & timestamps (14)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AcquiredDate` | Acquired Date | Date | Global |  |  |
| `ActualEndDate` |  | Date | — |  |  |
| `ActualStartDate` |  | Date | — |  |  |
| `BaselineEndDate` |  | Date | — |  |  |
| `ClientScheduleLastReviewedDate` |  | Date | — |  |  |
| `ExpectedEndDate` | Expected End Date | Date | Global |  |  |
| `OriginalEndDate` |  | Date | — |  |  |
| `OriginalStartDate` |  | Date | — |  |  |
| `PurchaseDate` | Purchase Date | Date | Global |  |  |
| `SlotEndDate` |  | Date | — |  |  |
| `SourceReferenceDate` | Source Reference Date | Date | Global |  |  |
| `SurveyDate` | Survey Date | Date | Global |  |  |
| `TaxBeginPeriod` | Tax Begin Period | Date | Global |  |  |
| `TaxEndPeriod` | Tax End Period | Date | Global |  |  |

### Flags (5)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `HasImprovements` | Has Improvements? | Boolean | Global |  |  |
| `Inactive` |  | Boolean | — |  |  |
| `IsDead` |  | Boolean | — |  |  |
| `IsTaxExempt` | Is Tax Exempt? | Boolean | Global |  |  |
| `UseLocationAddress` | Use Location Address? | Boolean | Global | yes |  |

### Text & notes (64)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BaseProvider` |  | Text | — |  |  |
| `Block` |  | Text | Global |  |  |
| `City` |  | Text | Global |  |  |
| `CityStateProvinceCountry` |  | Text | — |  |  |
| `ClientEntityID` | Parcel ID | Text | Global |  |  |
| `ComparisonList` |  | Text | — |  |  |
| `CompletedPhaseStatus` |  | Text | — |  |  |
| `ConstructionPhaseStatus` |  | Text | — |  |  |
| `CountryID` | Country | Text | Global |  |  |
| `CrossStreet1` | Cross Street #1 | Text | Global |  |  |
| `CrossStreet2` | Cross Street #2 | Text | Global |  |  |
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
| `Grid` |  | Text | Global |  |  |
| `HTMLAddress` | Full Address | Text | Global |  |  |
| `IndexNumber` | Index Number | Text | Global |  |  |
| `IssuesAndAlerts` |  | Text | — |  |  |
| `Lot` |  | Text | Global |  |  |
| `MapClientRecordID` |  | Text | — |  |  |
| `MilestoneTimeline` |  | Text | — |  |  |
| `NextMilestone` |  | Text | — |  |  |
| `Notes` |  | Text | Global |  |  |
| `OperationsPhaseStatus` |  | Text | — |  |  |
| `OwnerName` | Owner Name | Text | Global |  |  |
| `ParcelName` | Parcel Name | Text | Global | yes |  |
| `ParcelNumber` | Parcel Number | Text | Global |  |  |
| `ParcelPublicName` | Parcel Public Name | Text | Global |  |  |
| `Phone` |  | Text | — |  |  |
| `PossessionPhaseStatus` |  | Text | — |  |  |
| `PostalCode` | Postal Code | Text | Global |  |  |
| `PotentialProjectName` |  | Text | — |  |  |
| `PreviousMilestone` |  | Text | — |  |  |
| `ProgramName` |  | Text | — |  |  |
| `ProjectDescription` | Description | Text | Global |  |  |
| `ProjectEntityName` |  | Text | — |  |  |
| `ProjectEntityTypeName` |  | Text | — |  |  |
| `ProjectName` |  | Text | — |  |  |
| `PrototypeName` |  | Text | — |  |  |
| `RealEstatePhaseStatus` |  | Text | — |  |  |
| `RelatedEntities` |  | Text | — |  |  |
| `RelocatedFrom` |  | Text | — |  |  |
| `RunReportAction` |  | Text | — |  |  |
| `SourceReference` | Source Reference | Text | Global |  |  |
| `StreetAddress` |  | Text | — |  |  |
| `StreetAddress1` | Street Address #1 | Text | Global |  |  |
| `StreetAddress2` | Street Address #2 | Text | Global |  |  |
| `StreetAddress3` | Street Address #3 | Text | Global |  |  |
| `StreetAddress4` | Street Address #4 | Text | Global |  |  |
| `TaxAuthority` | Tax Authority | Text | Global |  |  |
| `TaxIDNumber` | Tax ID Number | Text | Global |  |  |
| `ThirdPartyWarehouse` | Third Party Warehouse | Text | Global |  |  |
| `TimeZone` | Time Zone | Text | Global |  |  |
| `TradeArea` |  | Text | — |  |  |

### Audit & record keeping (7)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Parcel ClientID | Text | Global | yes |  |
| `CreatedByID` |  | Member ID | — |  | [Member](Member.md) |
| `CreatedDate` |  | Time | — |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` |  | Number | — |  |  |
| `UUID` | Parcel UUID | Text | Global |  |  |

### Other (1)

Everything that did not fall into a named group.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `GrossArea` |  | Acreage | — |  |  |

## What points here (8 keys)

| Record type | Via column |
|---|---|
| [Parcel](Parcel.md) | `MasterParcelID` |
| [ParcelAccess](ParcelAccess.md) | `ParcelID` |
| [PropertyTaxAppeal](PropertyTaxAppeal.md) | `ParcelID` |
| [PropertyTaxAppealAward](PropertyTaxAppealAward.md) | `ParcelID` |
| [PropertyTaxAssessment](PropertyTaxAssessment.md) | `ParcelID` |
| [PropertyTaxBill](PropertyTaxBill.md) | `ParcelID` |
| [PropertyTaxDetail](PropertyTaxDetail.md) | `ParcelID` |
| [PropertyTaxSummary](PropertyTaxSummary.md) | `ParcelID` |
