# Prototype

*113 fields · module: Facilities, Locations & Sites · Postgres: `prototype`*

A standardized store/facility design template used for rollout programs — approved flag, average project cost/duration, and default construction type/distribution center. 15 Global fields under its own Prototype group.

Source: `data-fields/prototype.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 113 |
| Fields with a vendor definition | 107 of 114 inventoried |
| Physical tables | `prototype` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 15 (15 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 11 keys from 11 record types |
| Points at | 12 other records |
| Tenancy position | subtype_root |
| Rules that name it | 6 |

## What to know before rebuilding this

### 6 tenant custom columns

**Observed.** This record carries 6 physical Firm_-prefixed columns — tenant custom fields are real columns, not rows in a value store, so adding one is a DDL change. That is direct evidence for database-per-tenant and against a shared schema.

### A ProjectEntity subtype root

**Derived.** One of the nine records that are themselves a kind of ProjectEntity rather than hanging off one. The discriminator is ProjectEntityTypeName, which is how a single table serves several apparent record types.

### Census and catalogue disagree

**Observed.** The object census declares 113 fields; the Data Fields catalogue lists 15. The 98-field gap is columns the platform holds but does not expose as configurable Data Fields — a rebuild that reads only the catalogue will miss them.

### Lands in prototype

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 107 fields carry a vendor definition

**Observed.** 107 of this record's 114 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: the captures agree

**Observed.** Over the 15 fields both the Data Fields catalogue and the field inventory contain, the two agree on every one. 9 are marked required.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. Field is excluded from the loader field set for this object, so no column is created That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

### 1 field excluded from extraction

**Observed.** Observed of the loader. The inventory marks 1 of this record's fields as not extracted to PostgreSQL, so the replication target creates no column for them. They still exist in Lx; anything reading the replica rather than the product will not see them.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [ACC-R-061](../rules/ACC-R-061.md) | the form type declares attachability as a Boolean per entity kind. For this form type, only `Portfolio` = Yes and `RE Contract` = Yes; `Capital Program`, `Prototype`, `Location`, `Parcel`, `Site`, `Project`, `Facility`, `Capital Project` an | Observed |
| [FAC-R-007](../rules/FAC-R-007.md) | Input: `Prototype.ProgramID`. Confidence: Observed (`../../data-fields/prototype.md`). | Observed |
| [FAC-R-008](../rules/FAC-R-008.md) | Input: `ComplexID` on `Facility`, `Location`, `Parcel`, `Prototype` (all `Required = No` where exposed) and `Competitor`. Effect: Any of the four subtype roots — and a tracked competitor — may be grouped under one shared shopping-center/cam | Observed |
| [FAC-R-009](../rules/FAC-R-009.md) | Effect: `Complex`'s 45-field schema contains no FK back into `Location`/`Facility`/`Parcel`/ `Prototype`/`Program`, and no `ProjectEntityID`. It is `firm_global`, not entity-scoped. | Derived |
| [FAC-R-019](../rules/FAC-R-019.md) | Input: `Prototype.LocationID`, `.ComplexID`, `.DemographicDMAID` are declared columns in `_lucernex_objects_summary.txt` but do not appear anywhere in `../../data-fields/prototype.md`'s 15-row catalog. Effect: Unlike the identical columns o | Observed |
| [POR-R-003](../rules/POR-R-003.md) | A user opens a `Facility`/`Location`/`Parcel`/`Prototype`/`Contract`/`CapProject`/`OpenProject`/`EquipmentContract` detail screen under a given Portfolio · `Program.<Subtype>SetupPageLayoutID` · Overrides the tenant-wide default from `Firm. | Observed |

## Fields

### Relationships (foreign keys) (10)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BudgetTemplateID` | Budget Template ID | If there is a budget template associated with this entity, The foreign key of the budget template. | Template ID | — |  | `prototype.BudgetTemplateID · TEXT` | [BudgetTemplate](BudgetTemplate.md) |
| `ComplexID` | Complex Name | This is a default field that is not used for prototypes. | Complex ID | — |  | `prototype.ComplexID · TEXT` | [Complex](Complex.md) |
| `DemographicDMAID` | Demographic DMA | This is a default field that is not used for prototypes. | DMA ID | — |  | `prototype.DemographicDMAID · TEXT` | [DMA](DMA.md) |
| `IStateProvinceCountryID` | State | This is a default field that is not used for prototypes. | Country, State, County ID | — |  | `prototype.IStateProvinceCountryID · TEXT` | [StateProvinceCountry](StateProvinceCountry.md) |
| `JurisdictionID` | Jurisdiction | This is a default field that is not used for prototypes. | County ID | — |  | `prototype.JurisdictionID · TEXT` | [Jurisdiction](Jurisdiction.md) |
| `LocationID` | Location | This is a default field that is not used for prototypes. | Location ID | — |  | `prototype.LocationID · TEXT` | [Location](Location.md) |
| `ProgramID` | Portfolio | This is a default field that is not used for prototypes. | Portfolio ID | Global | yes | `prototype.ProgramID · TEXT` | [Program](Program.md) |
| `RegionID` | Region | This is a default field that is not used for prototypes. | Region ID | — |  | `prototype.RegionID · TEXT` | [Region](Region.md) |
| `RootRegionID` | Parent Region | This field sets some default membership at the creation of the entity. Its values are pulled from the organization chart. | Region ID | — |  | `prototype.RootRegionID · TEXT` | [Region](Region.md) |
| `SubRegionID` | Sub Region | This is a default field that is not used for prototypes. | Region ID | — |  | `prototype.SubRegionID · TEXT` | [Region](Region.md) |

### Soft references (2)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `LinkProjectEntityContactListData` | Contact List | This field returns a list of Active and Inactive entities filtered by member security. | Contact | — |  | `prototype.LinkProjectEntityContactListData · TEXT` |  |
| `ManagerIDList` | Project Managers | This is a default field that is not used for prototypes. | Dropdown | — |  | `prototype.ManagerIDList · TEXT` |  |

### Coded values (drop-downs) (11)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeBuildingAreaUnitID` | Building Area Unit | Select the units you are using to measure your area from this field. | Dropdown (Building Area Unit Code) | Global | yes | `prototype.CodeBuildingAreaUnitID · TEXT` | Building Area Unit Code |
| `CodeConstructionTypeID` | Default Construction Type | This is a default field that is not used for prototypes. | Dropdown (Construction Type Code) | Global |  | `prototype.CodeConstructionTypeID · TEXT` | Construction Type Code |
| `CodeCurrencyTypeID` | Currency Type | The Currency Type field allows you to select a currency type to be used on a record. | Dropdown (Currency Type Code) | — |  | `prototype.CodeCurrencyTypeID · TEXT` | Currency Type Code |
| `CodeDealTypeID` | Deal Type | This is a generic field. It is not implemented for prototypes by default. | Dropdown (Deal Type Code) | — |  | `prototype.CodeDealTypeID · TEXT` | Deal Type Code |
| `CodeDesc_CodeMarketAreaID` | Market Potential | This is a default field that is not used for prototypes. | Dropdown (Market Area Code) | — |  | `prototype.CodeDesc_CodeMarketAreaID · TEXT` | Market Area Code |
| `CodeDesc_CodeProjectTypeID` | Real Estate Type | This is a generic field. It is not implemented for prototypes by default. | Dropdown (Project Type Code) | — |  | `prototype.CodeDesc_CodeProjectTypeID · TEXT` | Project Type Code |
| `CodeDistributionCenterID` | Default Distribution Center | This is a default field that is not being used for prototypes. | Dropdown (Distribution Center Code) | Global |  | `prototype.CodeDistributionCenterID · TEXT` | Distribution Center Code |
| `CodeMarketAreaID` | Market Area | This is a default field that is not used for prototypes. | Dropdown (Market Area Code) | — |  | `prototype.CodeMarketAreaID · TEXT` | Market Area Code |
| `CodeMarketTypeID` | Market Type | This is a generic field. It is not implemented for prototypes by default. | Dropdown (Market Type Code) | — |  | `prototype.CodeMarketTypeID · TEXT` | Market Type Code |
| `CodeProjectTypeID` | Default Project Type | This is a generic field. It is not implemented for prototypes by default. | Dropdown (Project Type Code) | Global |  | `prototype.CodeProjectTypeID · TEXT` | Project Type Code |
| `CurrentCodeProjectPhaseID` | Project Phase | This is a default field that is not used for prototypes. | Dropdown (Project Phase Code) | — |  | `prototype.CurrentCodeProjectPhaseID · TEXT` | Project Phase Code |

### Money (2)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AverageCostOfProject` | Average Cost Of Project | Enter the average cost of a project that uses this prototype. | Currency | Global | yes | `prototype.AverageCostOfProject · TEXT` |  |
| `Firm_PriorMonthAccrualTotal` |  |  | Currency | — |  |  |  |

### Quantities (16)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActualRevenueWeeks` | Revenue Weeks | This is a default field that is not used for prototypes. | Number | — |  | `prototype.ActualRevenueWeeks · TEXT` |  |
| `AverageDurationOfProject` | Average Duration Of Project (months) | Enter the average project duration in months for this prototype in this field. | Number | Global | yes | `prototype.AverageDurationOfProject · TEXT` |  |
| `DBFolderSizeMB` | Storage Size (MB) | The folder size in megabytes for a given entity. | 2-Digit Number | — |  | `prototype.DBFolderSizeMB · TEXT` |  |
| `DefaultRentableArea` | Default Rentable Area | Enter the default rentable area in this field. | Number | Global | yes | `prototype.DefaultRentableArea · TEXT` |  |
| `DefaultUsableArea` | Default Usable Area | Enter the default usable area in this field. | Number | Global | yes | `prototype.DefaultUsableArea · TEXT` |  |
| `Depth` |  | This is a default field that is not used for prototypes. | Number | — |  | `prototype.Depth · TEXT` |  |
| `EntityId` | Entity LxID | The Project Entity ID. | Number | — |  | `prototype.EntityId · TEXT` |  |
| `Frontage` |  | This is a default field that is not used for prototypes. | Number | — |  | `prototype.Frontage · TEXT` |  |
| `LatitudeDegrees` | Latitude | This is a default field that is not used for prototypes. | 5-Digit Number | — |  | `prototype.LatitudeDegrees · TEXT` |  |
| `LongitudeDegrees` | Longitude | This is a default field that is not used for prototypes. | 5-Digit Number | — |  | `prototype.LongitudeDegrees · TEXT` |  |
| `NumberOfDocuments` | Number of Documents | The total number of documents in all folders on the entity. | Number | — |  | `prototype.NumberOfDocuments · TEXT` |  |
| `ProjectEntityID` | Entity RecID | The ProjectEntityID is the Base Entity System Identifier for associated tasks, folders, documents, forms, and other records. It is assigned automatically by the system, and is not editable. | Number | — |  | `prototype.ProjectEntityID · TEXT` |  |
| `PrototypeID` | Prototype RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `prototype.PrototypeID · VARCHAR(64) NOT NULL` |  |
| `RentableArea` | Rentable Area | This is a default field that is not used for prototypes. | Number | — |  | `prototype.RentableArea · TEXT` |  |
| `SequenceNumber` | Sequence Number | This field generates a sequence number for the record. The next record created receives the next number in the sequence. | Number | — |  | `prototype.SequenceNumber · TEXT` |  |
| `UsableArea` | Usable Area | This is a default field that is not used for prototypes. | Number | — |  | `prototype.UsableArea · TEXT` |  |

### Dates & timestamps (8)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActualEndDate` | Actual/Forecast Delivery Date | If there is a milestone timeline, The max end date from all non-operating tasks. Otherwise, The end date for the entity utilizing the schedule. If there are no tasks defined yet, the system will return the Original End Date / Completion Year set for the entity. | Date | — |  | `prototype.ActualEndDate · TEXT` |  |
| `ActualStartDate` | Forecast/Actual Start Date | The start date for the schedule associated with your entity. If there are no tasks defined in your schedule, The Original End Date / Completion Year set for the entity. | Date | — |  | `prototype.ActualStartDate · TEXT` |  |
| `BaselineEndDate` | Baseline Delivery Date | The baseline end date for the entity utilizing the schedules. If there is a milestone timeline the system uses the max end date from all non-operating tasks, otherwise it uses the max end date from the schedule. | Date | — |  | `prototype.BaselineEndDate · TEXT` |  |
| `ClientScheduleLastReviewedDate` | Last Updated Date | This field displays the last updated date. | Date | — |  | `prototype.ClientScheduleLastReviewedDate · TEXT` |  |
| `ExpectedEndDate` | Original Delivery Date | This is a default field that is not used for prototypes. | Date | — |  | `prototype.ExpectedEndDate · TEXT` |  |
| `OriginalEndDate` | Baseline End Date | The baseline end date of a schedule task on the entity. | Date | — |  | `prototype.OriginalEndDate · TEXT` |  |
| `OriginalStartDate` | Baseline Start Date | The baseline start date of a schedule task on the entity. | Date | — |  | `prototype.OriginalStartDate · TEXT` |  |
| `SlotEndDate` | RE Planner Open Date | This is a default field that is not used for prototypes. | Date | — |  | `prototype.SlotEndDate · TEXT` |  |

### Flags (3)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Inactive` | Is Inactive? | If selected, this check box indicates the entity is inactive. | Boolean | — | yes | `prototype.Inactive · TEXT` |  |
| `IsApproved` | Approved? | Select this check box if the prototype has been approved. | Boolean | Global | yes | `prototype.IsApproved · TEXT` |  |
| `IsDead` | Is Dead? | If selected, this check box indicates the entity is dead. | Boolean | — |  | `prototype.IsDead · TEXT` |  |

### Text & notes (53)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BaseProvider` | System of Record | This field is used to fetch a record value from another Accruent software. | Text | — |  | `prototype.BaseProvider · TEXT` |  |
| `City` |  | This is a default field that is not used for prototypes. | Text | — |  | `prototype.City · TEXT` |  |
| `CityStateProvinceCountry` | City, State | This is a default field that is not used for prototypes. | Text | — |  | `prototype.CityStateProvinceCountry · TEXT` |  |
| `ClientEntityID` | Store Number | Enter a unique ID for the entity in this field. Remember: when uploading information to a contract using Lx's import spreadsheet functionality, the entity ID and entity name must be replicated exactly in the spreadsheet. | Text | — |  | `prototype.ClientEntityID · TEXT` |  |
| `ComparisonList` | Comparison List | When added to a page layout, this field allows for a comparison of entities from a page or subpage. | Text | — |  | `prototype.ComparisonList · TEXT` |  |
| `CompletedPhaseStatus` | Completed Phase Status | The milestone timeline status of the entity. This status is updated when a milestone is completed. | Text | — |  | `prototype.CompletedPhaseStatus · TEXT` |  |
| `ConstructionPhaseStatus` | Construction Phase Status | This is a default field that is not used for prototypes. | Text | — |  | `prototype.ConstructionPhaseStatus · TEXT` |  |
| `CountryID` | Country | This is a default field that is not used for prototypes. | Text | — |  | `prototype.CountryID · TEXT` |  |
| `CrossStreet1` | Cross Street #1 | This is a default field that is not used for prototypes. | Text | — |  | `prototype.CrossStreet1 · TEXT` |  |
| `CrossStreet2` | Cross Street #2 | This is a default field that is not used for prototypes. | Text | — |  | `prototype.CrossStreet2 · TEXT` |  |
| `CurrentMilestone` | Current Milestone | This is a default field that is not used for prototypes. | Text | — |  | `prototype.CurrentMilestone · TEXT` |  |
| `CurrentPhaseStatus` | Project Status | This is a default field that is not used for prototypes. | Text | — |  | `prototype.CurrentPhaseStatus · TEXT` |  |
| `DesignPhaseStatus` | Design Phase Status | This is a default field that is not used for prototypes. | Text | — |  | `prototype.DesignPhaseStatus · TEXT` |  |
| `EntityEmail` | Entity Email | The entity's email address that is created when the Email into Lx functionality is enabled. | Text | — |  | `prototype.EntityEmail · TEXT` |  |
| `EntityPhoto` | Entity Photo | This is a generic field. When you add this field to a page layout, you can use it to add a photo to the layout. | Text | — |  | `prototype.EntityPhoto · TEXT` |  |
| `FacilityName` | Facility Name | This is a default field that is not used for prototypes. | Text | — |  | `prototype.FacilityName · TEXT` |  |
| `FinancialModel` | Financial Model | This is a default field that is not used for prototypes. | Text | — |  | `prototype.FinancialModel · TEXT` |  |
| `FirmID` | Firm ID | The record's Firm ID. | Text | — | yes | `prototype.FirmID · TEXT` |  |
| `Firm_SalesReportLogo` | Sales Report Logo |  | Text | — |  | `prototype.Firm_SalesReportLogo · TEXT` |  |
| `Firm_SalesReportLogoMadewell` |  |  | Text | — |  |  |  |
| `Firm_SalesReportSignature` | Sales Report Signature |  | Text | — |  | `prototype.Firm_SalesReportSignature · TEXT` |  |
| `Firm_SalesReportSignatureName` | Sales Report Signature Name |  | Text | — |  | `prototype.Firm_SalesReportSignatureName · TEXT` |  |
| `Firm_SalesReportSignatureTitle` | Sales Report Signature Title |  | Text | — |  | `prototype.Firm_SalesReportSignatureTitle · TEXT` |  |
| `HTMLAddress` | Full Address | The associated entity's address in HTML format. | Text | — |  | `prototype.HTMLAddress · TEXT` |  |
| `IssuesAndAlerts` | Issues And Alerts | This field can be added to page layouts. In View mode, this field will display a table with form and workflow data, such as the work flow / form type, critical issue count, non-critical issue count, escalated count, and past due notification count. | Text | — |  | `prototype.IssuesAndAlerts · TEXT` |  |
| `MapClientRecordID` | Client Unique ID | The entity Map Client Record ID. | Text | — |  | `prototype.MapClientRecordID · TEXT` |  |
| `MilestoneTimeline` | Milestone Timeline | This field generates a list of all milestones, but hides those with no values. | Text | — |  | `prototype.MilestoneTimeline · TEXT` |  |
| `NextMilestone` | Next Milestone | This is a default field that is not used for prototypes. | Text | — |  | `prototype.NextMilestone · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `prototype.Notes · TEXT` |  |
| `OperationsPhaseStatus` | Operations Phase Status | This is a default field that is not used for prototypes. | Text | — |  | `prototype.OperationsPhaseStatus · TEXT` |  |
| `Phone` |  | This is a default field that is not used for prototypes. | Text | — |  | `prototype.Phone · TEXT` |  |
| `PossessionPhaseStatus` | Possession Phase Status | This is a default field that is not used for prototypes. | Text | — |  | `prototype.PossessionPhaseStatus · TEXT` |  |
| `PostalCode` | Postal Code | This is a default field that is not used for prototypes. | Text | — |  | `prototype.PostalCode · TEXT` |  |
| `PotentialProjectName` | Site Name | This is a default field that is not used for prototypes. | Text | — |  | `prototype.PotentialProjectName · TEXT` |  |
| `PreviousMilestone` | Previous Milestone | This is a default field that is not used for prototypes. | Text | — |  | `prototype.PreviousMilestone · TEXT` |  |
| `ProgramName` | Portfolio/Program Name | This is a default field that is not used for prototypes. | Text | — |  | `prototype.ProgramName · TEXT` |  |
| `ProjectDescription` | Description | Write a description of the record. | Text | Global |  | `prototype.ProjectDescription · TEXT` |  |
| `ProjectEntityName` | Name | The entity name. | Text | — | yes | `prototype.ProjectEntityName · TEXT` |  |
| `ProjectEntityTypeName` | Entity Type | The entity type. | Text | — |  | `prototype.ProjectEntityTypeName · TEXT` |  |
| `ProjectName` | Project Name | This is a default field that is not used for prototypes. | Text | — |  | `prototype.ProjectName · TEXT` |  |
| `PrototypeName` | Prototype Name | Enter the name of the prototype in this field. | Text | Global | yes | `prototype.PrototypeName · TEXT` |  |
| `RealEstatePhaseStatus` | Real Estate Phase Status | This is a default field that is not used for prototypes. | Text | — |  | `prototype.RealEstatePhaseStatus · TEXT` |  |
| `RelatedEntities` | Related Entities | The name of entities associated with this entity. | Text | — |  | `prototype.RelatedEntities · TEXT` |  |
| `RelocatedFrom` |  | This is a default field that is not used for prototypes. | Text | — |  | `prototype.RelocatedFrom · TEXT` |  |
| `RunReportAction` | Run Report Action | This is a generic field. When you add this field to a page layout, it will run a report. See the Run Report Action Buttons article in the Online Help to learn more. | Text | — |  | `prototype.RunReportAction · TEXT` |  |
| `StreetAddress` | Street Address | This is a default field that is not used for prototypes. | Text | — |  | `prototype.StreetAddress · TEXT` |  |
| `StreetAddress1` | Street Address #1 | This is a default field that is not used for prototypes. | Text | — |  | `prototype.StreetAddress1 · TEXT` |  |
| `StreetAddress2` | Street Address #2 | This is a default field that is not used for prototypes. | Text | — |  | `prototype.StreetAddress2 · TEXT` |  |
| `StreetAddress3` | Street Address #3 | This is a default field that is not used for prototypes. | Text | — |  | `prototype.StreetAddress3 · TEXT` |  |
| `StreetAddress4` | Street Address #4 | This is a default field that is not used for prototypes. | Text | — |  | `prototype.StreetAddress4 · TEXT` |  |
| `ThirdPartyWarehouse` | Third Party Warehouse | This is a default field that is not used for prototypes. | Text | — |  | `prototype.ThirdPartyWarehouse · TEXT` |  |
| `TimeZone` | Time Zone | This is a default field that is not used for prototypes. | Text | — |  | `prototype.TimeZone · TEXT` |  |
| `TradeArea` | Trade Area | This is a default field that is not used for prototypes. | Text | — |  | `prototype.TradeArea · TEXT` |  |

### Audit & record keeping (7)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Prototype ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `prototype.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | — |  | `prototype.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | — |  | `prototype.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | — |  | `prototype.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | — |  | `prototype.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | — |  | `prototype.RevNumber · TEXT` |  |
| `UUID` | Entity UUID | This field captures a unique identifier associated with your record. This identifier is used if you are using an integration with other Accruent products. | Text | — |  | `prototype.UUID · TEXT` |  |

### Other (1)

Everything that did not fall into a named group.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `GrossArea` | Gross Acreage | This is a default field that is not used for prototypes. | Acreage | — |  | `prototype.GrossArea · TEXT` |  |

## What points here (11 keys)

| Record type | Via column |
|---|---|
| [BudgetOptionTemplate](BudgetOptionTemplate.md) | `PrototypeID` |
| [Contract](Contract.md) | `PrototypeID` |
| [DemographicReport](DemographicReport.md) | `PrototypeID` |
| [DevelopmentSlot](DevelopmentSlot.md) | `PrototypeID` |
| [Facility](Facility.md) | `PrototypeID` |
| [Location](Location.md) | `PrototypeID` |
| [Parcel](Parcel.md) | `PrototypeID` |
| [PotentialProject](PotentialProject.md) | `PrototypeID` |
| [Program](Program.md) | `PrototypeID` |
| [Project](Project.md) | `PrototypeID` |
| [ProjectEntity](ProjectEntity.md) | `PrototypeID` |
