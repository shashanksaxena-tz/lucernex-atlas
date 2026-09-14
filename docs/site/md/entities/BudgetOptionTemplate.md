# BudgetOptionTemplate

*107 fields · module: Budgeting, Cost Tracking & Bidding — OUT OF SCOPE · Postgres: `none exported`*

Not covered by the Data Fields catalogue: this record type appears in the 223-object census but has no row in the catalogue of 6,158 configurable fields, so nothing in the corpus explains it in the vendor's own words. What is known is structural — 107 declared fields, filed under Budgeting, Cost Tracking & Bidding — OUT OF SCOPE, 0 foreign keys pointing at it.

Source: `_lucernex_objects_summary.txt`

## At a glance

|  | Value |
|---|---|
| Fields declared | 107 |
| Catalogued fields | not in the catalogue |
| Physical tables | 0 |
| Referenced by | 0 keys from 0 record types |
| Points at | 12 other records |
| Tenancy position | subtype_root |
| Rules that name it | 0 |

## What to know before rebuilding this

### 6 tenant custom columns

**Observed.** This record carries 6 physical Firm_-prefixed columns — tenant custom fields are real columns, not rows in a value store, so adding one is a DDL change. That is direct evidence for database-per-tenant and against a shared schema.

### A ProjectEntity subtype root

**Derived.** One of the nine records that are themselves a kind of ProjectEntity rather than hanging off one. The discriminator is ProjectEntityTypeName, which is how a single table serves several apparent record types.

### Out of scope by decision

**Observed.** Its module is excluded from the rebuild. It stays in the census so impact analysis through the relationship graph is never silently wrong at the boundary, but nothing here is being built.

## Fields

### Relationships (foreign keys) (10)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BudgetTemplateID` |  | Template ID | — |  | [BudgetTemplate](BudgetTemplate.md) |
| `ComplexID` |  | Complex ID | — |  | [Complex](Complex.md) |
| `DemographicDMAID` |  | DMA ID | — |  | [DMA](DMA.md) |
| `IStateProvinceCountryID` |  | Country, State, County ID | — |  | [StateProvinceCountry](StateProvinceCountry.md) |
| `JurisdictionID` |  | County ID | — |  | [Jurisdiction](Jurisdiction.md) |
| `LocationID` |  | Location ID | — |  | [Location](Location.md) |
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

### Quantities (12)

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
| `ProjectEntityID` |  | Number | — |  |  |
| `RentableArea` |  | Number | — |  |  |
| `SequenceNumber` |  | Number | — |  |  |
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
| `ClientEntityID` |  | Text | — |  |  |
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
| `ProgramID` |  | Text | — |  |  |
| `ProgramName` |  | Text | — |  |  |
| `ProjectDescription` |  | Text | — |  |  |
| `ProjectEntityName` |  | Text | — |  |  |
| `ProjectEntityTypeName` |  | Text | — |  |  |
| `ProjectName` |  | Text | — |  |  |
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
| `UUID` |  | Text | — |  |  |

### Other (1)

Everything that did not fall into a named group.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `GrossArea` |  | Acreage | — |  |  |
