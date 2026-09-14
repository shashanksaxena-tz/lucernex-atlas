# BudgetOptionTemplate

*107 fields · module: Budgeting, Cost Tracking & Bidding — OUT OF SCOPE · Postgres: `none exported`*

Not covered by the Data Fields catalogue: this record type appears in the 223-object census but has no row in the catalogue of 6,158 configurable fields, so no document describes the record as a whole. What is known is structural — 107 declared fields, filed under Budgeting, Cost Tracking & Bidding — OUT OF SCOPE, 0 foreign keys pointing at it. Its fields are documented even though the record is not: 100 of its 108 inventoried fields carry a definition written by the vendor. Open the field groups below and read them — that is the best account of this record available.

Source: `data-model/pg/bbw-field-inventory.csv`, `_lucernex_objects_summary.txt`

## At a glance

|  | Value |
|---|---|
| Fields declared | 107 |
| Fields with a vendor definition | 100 of 108 inventoried |
| Physical tables | — |
| Replication database | — |
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

### 100 fields carry a vendor definition

**Observed.** 100 of this record's 108 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one source in the corpus that explains fields rather than listing them.

### 3 fields marked required

**Observed.** The inventory marks 3 of this record's fields Required. Across the whole inventory that is 606 fields, which independently corroborates the 603 the corpus had derived from the Data Fields catalogue — two sources, arrived at separately, agreeing to within three.

### 108 fields excluded from extraction

**Observed.** Observed of the loader. The inventory marks 108 of this record's fields as not extracted to PostgreSQL, so the replication target creates no column for them. They still exist in Lx; anything reading the replica rather than the product will not see them.

### Out of scope by decision

**Observed.** Its module is excluded from the rebuild. It stays in the census so impact analysis through the relationship graph is never silently wrong at the boundary, but nothing here is being built.

## Fields

### Relationships (foreign keys) (10)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BudgetTemplateID` | Budget Template ID | If there is a budget template associated with this entity, The foreign key of the budget template. | Template ID | — |  | not extracted | [BudgetTemplate](BudgetTemplate.md) |
| `ComplexID` | Complex Name | This is a default field that is not used for budget option templates. | Complex ID | — |  | not extracted | [Complex](Complex.md) |
| `DemographicDMAID` | Demographic DMA | This is a default field that is not used for budget option templates. | DMA ID | — |  | not extracted | [DMA](DMA.md) |
| `IStateProvinceCountryID` | State | This is a default field that is not used for budget option templates. | Country, State, County ID | — |  | not extracted | [StateProvinceCountry](StateProvinceCountry.md) |
| `JurisdictionID` | Jurisdiction | This is a default field that is not used for budget option templates. | County ID | — |  | not extracted | [Jurisdiction](Jurisdiction.md) |
| `LocationID` | Location | This is a default field that is not used for budget option templates. | Location ID | — |  | not extracted | [Location](Location.md) |
| `PrototypeID` | Prototype | This is a default field that is not used for budget option templates. | Prototype ID | — |  | not extracted | [Prototype](Prototype.md) |
| `RegionID` | Region | This is a default field that is not used for budget option templates. | Region ID | — |  | not extracted | [Region](Region.md) |
| `RootRegionID` | Parent Region | This is a default field that is not used for budget option templates. | Region ID | — |  | not extracted | [Region](Region.md) |
| `SubRegionID` | Sub Region | This is a default field that is not used for budget option templates. | Region ID | — |  | not extracted | [Region](Region.md) |

### Soft references (2)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `LinkProjectEntityContactListData` | Contact List | This is a default field that is not used for budget option templates. | Contact | — |  | not extracted |  |
| `ManagerIDList` | Project Managers | This is a default field that is not used for budget option templates. | Dropdown | — |  | not extracted |  |

### Coded values (drop-downs) (11)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeBuildingAreaUnitID` | Building Area Unit | This is a default field that is not used for budget option templates. | Dropdown (Building Area Unit Code) | — |  | not extracted | Building Area Unit Code |
| `CodeConstructionTypeID` | Construction Type | This is a default field that is not used for budget option templates. | Dropdown (Construction Type Code) | — |  | not extracted | Construction Type Code |
| `CodeCurrencyTypeID` | Currency Type | This is a default field that is not used for budget option templates. | Dropdown (Currency Type Code) | — |  | not extracted | Currency Type Code |
| `CodeDealTypeID` | Deal Type | This is a default field that is not used for budget option templates. | Dropdown (Deal Type Code) | — |  | not extracted | Deal Type Code |
| `CodeDesc_CodeMarketAreaID` | Market Potential | This is a default field that is not used for budget option templates. | Dropdown (Market Area Code) | — |  | not extracted | Market Area Code |
| `CodeDesc_CodeProjectTypeID` | Real Estate Type | This is a default field that is not used for budget option templates. | Dropdown (Project Type Code) | — |  | not extracted | Project Type Code |
| `CodeDistributionCenterID` | Distribution Center | This is a default field that is not used for budget option templates. | Dropdown (Distribution Center Code) | — |  | not extracted | Distribution Center Code |
| `CodeMarketAreaID` | Market Area | This is a default field that is not used for budget option templates. | Dropdown (Market Area Code) | — |  | not extracted | Market Area Code |
| `CodeMarketTypeID` | Market Type | This is a default field that is not used for budget option templates. | Dropdown (Market Type Code) | — |  | not extracted | Market Type Code |
| `CodeProjectTypeID` | Project Type | This is a default field that is not used for budget option templates. | Dropdown (Project Type Code) | — |  | not extracted | Project Type Code |
| `CurrentCodeProjectPhaseID` | Project Phase | This is a default field that is not used for budget option templates. | Dropdown (Project Phase Code) | — |  | not extracted | Project Phase Code |

### Money (1)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Firm_PriorMonthAccrualTotal` |  |  | Currency | — |  |  |  |

### Quantities (12)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActualRevenueWeeks` | Revenue Weeks | This is a default field that is not used for budget option templates. | Number | — |  | not extracted |  |
| `DBFolderSizeMB` | Storage Size (MB) | This is a default field that is not used for budget option templates. | 2-Digit Number | — |  | not extracted |  |
| `Depth` |  | This is a default field that is not used for budget option templates. | Number | — |  | not extracted |  |
| `EntityId` | Entity LxID | The Project Entity ID. | Number | — |  | not extracted |  |
| `Frontage` |  | This is a default field that is not used for budget option templates. | Number | — |  | not extracted |  |
| `LatitudeDegrees` | Latitude | This is a default field that is not used for budget option templates. | 5-Digit Number | — |  | not extracted |  |
| `LongitudeDegrees` | Longitude | This is a default field that is not used for budget option templates. | 5-Digit Number | — |  | not extracted |  |
| `NumberOfDocuments` | Number of Documents | This is a default field that is not used for budget option templates. | Number | — |  | not extracted |  |
| `ProjectEntityID` | Entity RecID | The ProjectEntityID is the Base Entity System Identifier for associated tasks, folders, documents, forms, and other records. It is assigned automatically by the system, and is not editable. | Number | — |  | not extracted |  |
| `RentableArea` | Rentable Area | This is a default field that is not used for budget option templates. | Number | — |  | not extracted |  |
| `SequenceNumber` | Sequence Number | This field generates a sequence number for the record. The next record created receives the next number in the sequence. | Number | — |  | not extracted |  |
| `UsableArea` | Usable Area | This is a default field that is not used for budget option templates. | Number | — |  | not extracted |  |

### Dates & timestamps (8)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActualEndDate` | Actual/Forecast Delivery Date | This is a default field that is not used for budget option templates. | Date | — |  | not extracted |  |
| `ActualStartDate` | Forecast/Actual Start Date | This is a default field that is not used for budget option templates. | Date | — |  | not extracted |  |
| `BaselineEndDate` | Baseline Delivery Date | This is a default field that is not used for budget option templates. | Date | — |  | not extracted |  |
| `ClientScheduleLastReviewedDate` | Last Updated Date | This is a default field that is not used for budget option templates. | Date | — |  | not extracted |  |
| `ExpectedEndDate` | Original Delivery Date | This is a default field that is not used for budget option templates. | Date | — |  | not extracted |  |
| `OriginalEndDate` | Baseline End Date | The baseline end date of a schedule task on the entity. | Date | — |  | not extracted |  |
| `OriginalStartDate` | Baseline Start Date | The baseline start date of a schedule task on the entity. | Date | — |  | not extracted |  |
| `SlotEndDate` | RE Planner Open Date | This is a default field that is not used for budget option templates. | Date | — |  | not extracted |  |

### Flags (2)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Inactive` | Is Inactive? | This is a default field that is not used for budget option templates. | Boolean | — | yes | not extracted |  |
| `IsDead` | Is Dead? | This is a default field that is not used for budget option templates. | Boolean | — |  | not extracted |  |

### Text & notes (54)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BaseProvider` | System of Record | This is a default field that is not used for budget option templates. | Text | — |  | not extracted |  |
| `City` |  | This is a default field that is not used for budget option templates. | Text | — |  | not extracted |  |
| `CityStateProvinceCountry` | City, State | This is a default field that is not used for budget option templates. | Text | — |  | not extracted |  |
| `ClientEntityID` | Store Number | Enter a unique ID for the entity in this field. Remember: when uploading information to a contract using Lx's import spreadsheet functionality, the entity ID and entity name must be replicated exactly in the spreadsheet. | Text | — |  | not extracted |  |
| `ComparisonList` | Comparison List | This is a default field that is not used for budget option templates. | Text | — |  | not extracted |  |
| `CompletedPhaseStatus` | Completed Phase Status |  | Text | — |  | not extracted |  |
| `ConstructionPhaseStatus` | Construction Phase Status | This is a default field that is not used for budget option templates. | Text | — |  | not extracted |  |
| `CountryID` | Country | This is a default field that is not used for budget option templates. | Text | — |  | not extracted |  |
| `CrossStreet1` | Cross Street #1 | This is a default field that is not used for budget option templates. | Text | — |  | not extracted |  |
| `CrossStreet2` | Cross Street #2 | This is a default field that is not used for budget option templates. | Text | — |  | not extracted |  |
| `CurrentMilestone` | Current Milestone | This is a default field that is not used for budget option templates. | Text | — |  | not extracted |  |
| `CurrentPhaseStatus` | Project Status | This is a default field that is not used for budget option templates. | Text | — |  | not extracted |  |
| `DesignPhaseStatus` | Design Phase Status | This is a default field that is not used for budget option templates. | Text | — |  | not extracted |  |
| `EntityEmail` | Entity Email | This is a default field that is not used for budget option templates. | Text | — |  | not extracted |  |
| `EntityPhoto` | Entity Photo | This is a generic field. When you add this field to a page layout, you can use it to add a photo to the layout. | Text | — |  | not extracted |  |
| `FacilityName` | Facility Name | This is a default field that is not used for budget option templates. | Text | — |  | not extracted |  |
| `FinancialModel` | Financial Model | This is a default field that is not used for budget option templates. | Text | — |  | not extracted |  |
| `FirmID` | Firm ID | The record's Firm ID. | Text | — | yes | not extracted |  |
| `Firm_SalesReportLogo` | Sales Report Logo |  | Text | — |  | not extracted |  |
| `Firm_SalesReportLogoMadewell` |  |  | Text | — |  |  |  |
| `Firm_SalesReportSignature` | Sales Report Signature |  | Text | — |  | not extracted |  |
| `Firm_SalesReportSignatureName` | Sales Report Signature Name |  | Text | — |  | not extracted |  |
| `Firm_SalesReportSignatureTitle` | Sales Report Signature Title |  | Text | — |  | not extracted |  |
| `HTMLAddress` | Full Address | This is a default field that is not used for budget option templates. | Text | — |  | not extracted |  |
| `IssuesAndAlerts` | Issues And Alerts | This is a default field that is not used for budget option templates. | Text | — |  | not extracted |  |
| `MapClientRecordID` | Client Unique ID | This is a default field that is not used for budget option templates. | Text | — |  | not extracted |  |
| `MilestoneTimeline` | Milestone Timeline | This is a default field that is not used for budget option templates. | Text | — |  | not extracted |  |
| `NextMilestone` | Next Milestone | This is a default field that is not used for budget option templates. | Text | — |  | not extracted |  |
| `Notes` |  | Add any notes about the record. | Text | — |  | not extracted |  |
| `OperationsPhaseStatus` | Operations Phase Status | This is a default field that is not used for budget option templates. | Text | — |  | not extracted |  |
| `Phone` |  | This is a default field that is not used for budget option templates. | Text | — |  | not extracted |  |
| `PossessionPhaseStatus` | Possession Phase Status | This is a default field that is not used for budget option templates. | Text | — |  | not extracted |  |
| `PostalCode` | Postal Code | This is a default field that is not used for budget option templates. | Text | — |  | not extracted |  |
| `PotentialProjectName` | Site Name | This is a default field that is not used for budget option templates. | Text | — |  | not extracted |  |
| `PreviousMilestone` | Previous Milestone | This is a default field that is not used for budget option templates. | Text | — |  | not extracted |  |
| `ProgramID` | Capital Program | This is a default field that is not used for budget option templates. | Text | — |  | not extracted |  |
| `ProgramName` | Portfolio/Program Name | This is a default field that is not used for budget option templates. | Text | — |  | not extracted |  |
| `ProjectDescription` | Description | Write a description of the record. | Text | — |  | not extracted |  |
| `ProjectEntityName` | Name | The record name. | Text | — | yes | not extracted |  |
| `ProjectEntityTypeName` | Entity Type | This is a default field that is not used for budget option templates. | Text | — |  | not extracted |  |
| `ProjectName` | Project Name | This is a default field that is not used for budget option templates. | Text | — |  | not extracted |  |
| `PrototypeName` | Prototype Name | This is a default field that is not used for budget option templates. | Text | — |  | not extracted |  |
| `RealEstatePhaseStatus` | Real Estate Phase Status | This is a default field that is not used for budget option templates. | Text | — |  | not extracted |  |
| `RelatedEntities` | Related Entities | This is a default field that is not used for budget option templates. | Text | — |  | not extracted |  |
| `RelocatedFrom` |  | This is a default field that is not used for budget option templates. | Text | — |  | not extracted |  |
| `RunReportAction` | Run Report Action | This is a generic field. When you add this field to a page layout, it will run a report. See the Run Report Action Buttons article in the Online Help to learn more. | Text | — |  | not extracted |  |
| `StreetAddress` | Street Address | This is a default field that is not used for budget option templates. | Text | — |  | not extracted |  |
| `StreetAddress1` | Street Address #1 | This is a default field that is not used for budget option templates. | Text | — |  | not extracted |  |
| `StreetAddress2` | Street Address #2 | This is a default field that is not used for budget option templates. | Text | — |  | not extracted |  |
| `StreetAddress3` | Street Address #3 | This is a default field that is not used for budget option templates. | Text | — |  | not extracted |  |
| `StreetAddress4` | Street Address #4 | This is a default field that is not used for budget option templates. | Text | — |  | not extracted |  |
| `ThirdPartyWarehouse` | Third Party Warehouse | This is a default field that is not used for budget option templates. | Text | — |  | not extracted |  |
| `TimeZone` | Time Zone | This is a default field that is not used for budget option templates. | Text | — |  | not extracted |  |
| `TradeArea` | Trade Area | This is a default field that is not used for budget option templates. | Text | — |  | not extracted |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | — |  | not extracted | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | — |  | not extracted |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | — |  | not extracted | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | — |  | not extracted |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | — |  | not extracted |  |
| `UUID` | Entity UUID | This field captures a unique identifier associated with your record. This identifier is used if you are using an integration with other Accruent products. | Text | — |  | not extracted |  |

### Other (1)

Everything that did not fall into a named group.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `GrossArea` | Gross Acreage | This is a default field that is not used for budget option templates. | Acreage | — |  | not extracted |  |
