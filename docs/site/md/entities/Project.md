# Project

*111 fields · module: Platform & Tenancy · Postgres: `project`*

A lightweight project identity record (ID, RecID, UUID) distinct from the richer ProjectEntity, likely used for cross-system reference linking.

Source: `data-fields/small-miscellaneous-entities.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 111 |
| Fields with a vendor definition | 105 of 112 inventoried |
| Physical tables | `project` |
| Replication database | `lxr_drp_bbw` |
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

### Lands in project

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 105 fields carry a vendor definition

**Observed.** 105 of this record's 112 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one source in the corpus that explains fields rather than listing them.

### 4 fields marked required

**Observed.** The inventory marks 4 of this record's fields Required. Across the whole inventory that is 606 fields, which independently corroborates the 603 the corpus had derived from the Data Fields catalogue — two sources, arrived at separately, agreeing to within three.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. Field is excluded from the loader field set for this object, so no column is created That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

### 1 field excluded from extraction

**Observed.** Observed of the loader. The inventory marks 1 of this record's fields as not extracted to PostgreSQL, so the replication target creates no column for them. They still exist in Lx; anything reading the replica rather than the product will not see them.

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

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BudgetTemplateID` | Budget Template ID | If there is a budget template associated with this entity, The foreign key of the budget template. | Template ID | — |  | `project.BudgetTemplateID · TEXT` | [BudgetTemplate](BudgetTemplate.md) |
| `ComplexID` | Complex Name | Select the complex name from this field. A complex or center is used to track information about multi-tenant structures such as shopping malls. | Complex ID | — |  | `project.ComplexID · TEXT` | [Complex](Complex.md) |
| `DemographicDMAID` | Demographic DMA | Select your demographic market area from this field. | DMA ID | — |  | `project.DemographicDMAID · TEXT` | [DMA](DMA.md) |
| `FacilityID` | Related Project Facility | Select the facility that your entity will be associated with from this field. | Facility ID | Global |  | `project.FacilityID · TEXT` | [Facility](Facility.md) |
| `IStateProvinceCountryID` | State | Select the state or province from this field. | Country, State, County ID | — |  | `project.IStateProvinceCountryID · TEXT` | [StateProvinceCountry](StateProvinceCountry.md) |
| `JurisdictionID` | Jurisdiction | The county / province associated with the associated entity's address. | County ID | — |  | `project.JurisdictionID · TEXT` | [Jurisdiction](Jurisdiction.md) |
| `LocationID` | Location | Select the location that your entity will be associated with from this field. | Location ID | — |  | `project.LocationID · TEXT` | [Location](Location.md) |
| `ProgramID` | Portfolio/Program | Select the Portfolio that the entity belongs to from this field. | Portfolio ID | — |  | `project.ProgramID · TEXT` | [Program](Program.md) |
| `PrototypeID` | Prototype | Select the prototype associated with this entity from this field. | Prototype ID | — |  | `project.PrototypeID · TEXT` | [Prototype](Prototype.md) |
| `RegionID` | Region | Select the region and sub-region the project should belong to from this field. The values that appear in this field depend on the org chart of the portfolio you selected. | Region ID | — |  | `project.RegionID · TEXT` | [Region](Region.md) |
| `RootRegionID` | Parent Region | This field sets some default membership at the creation of the entity. Its values are pulled from the organization chart. | Region ID | — |  | `project.RootRegionID · TEXT` | [Region](Region.md) |
| `SubRegionID` | Sub Region | The sub-region. | Region ID | — |  | `project.SubRegionID · TEXT` | [Region](Region.md) |

### Soft references (2)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `LinkProjectEntityContactListData` | Contact List | This field returns a list of Active and Inactive entities filtered by member security. | Contact | — |  | `project.LinkProjectEntityContactListData · TEXT` |  |
| `ManagerIDList` | Project Managers | This is a generic field that you can add to a page layout. In View mode, this field returns a list of managers assigned to the entity by the org chart and managers assigned to the entity on an ad hoc basis. In Edit mode, this field allows you to add managers to your entity. | Dropdown | — |  | `project.ManagerIDList · TEXT` |  |

### Coded values (drop-downs) (11)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeBuildingAreaUnitID` | Building Area Unit | Select the units you are using to measure your area from this field. | Dropdown (Building Area Unit Code) | — |  | `project.CodeBuildingAreaUnitID · TEXT` | Building Area Unit Code |
| `CodeConstructionTypeID` | Construction Type | Select the construction type from this field. | Dropdown (Construction Type Code) | — |  | `project.CodeConstructionTypeID · TEXT` | Construction Type Code |
| `CodeCurrencyTypeID` | Currency Type | The Currency Type field allows you to select a currency type to be used on a record. | Dropdown (Currency Type Code) | — |  | `project.CodeCurrencyTypeID · TEXT` | Currency Type Code |
| `CodeDealTypeID` | Deal Type | Select the deal type from this field. | Dropdown (Deal Type Code) | — |  | `project.CodeDealTypeID · TEXT` | Deal Type Code |
| `CodeDesc_CodeMarketAreaID` | Market Potential | This is a default field that is not used for programs. | Dropdown (Market Area Code) | — |  | `project.CodeDesc_CodeMarketAreaID · TEXT` | Market Area Code |
| `CodeDesc_CodeProjectTypeID` | Real Estate Type | The description of the project type. | Dropdown (Project Type Code) | — |  | `project.CodeDesc_CodeProjectTypeID · TEXT` | Project Type Code |
| `CodeDistributionCenterID` | Distribution Center | Select the distribution center from which the store is receiving product from this field. | Dropdown (Distribution Center Code) | — |  | `project.CodeDistributionCenterID · TEXT` | Distribution Center Code |
| `CodeMarketAreaID` | Market Area | Select the market the project should belong to from this field. The values that appear in this field might depend on the org chart of the portfolio you selected. | Dropdown (Market Area Code) | — |  | `project.CodeMarketAreaID · TEXT` | Market Area Code |
| `CodeMarketTypeID` | Market Type | Select the market type from this field. | Dropdown (Market Type Code) | — |  | `project.CodeMarketTypeID · TEXT` | Market Type Code |
| `CodeProjectTypeID` | Project Type | Select the project type from this field. | Dropdown (Project Type Code) | — |  | `project.CodeProjectTypeID · TEXT` | Project Type Code |
| `CurrentCodeProjectPhaseID` | Project Phase | The project phase set by the milestone timeline. This value is driven by your entity schedule. | Dropdown (Project Phase Code) | — |  | `project.CurrentCodeProjectPhaseID · TEXT` | Project Phase Code |

### Money (1)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Firm_PriorMonthAccrualTotal` |  |  | Currency | — |  |  |  |

### Quantities (15)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActualRevenueWeeks` | Revenue Weeks | Calculates how many actual revenue weeks this entity will exist during the fiscal year. | Number | — |  | `project.ActualRevenueWeeks · TEXT` |  |
| `DBFolderSizeMB` | Storage Size (MB) | The folder size in megabytes for a given entity. | 2-Digit Number | — |  | `project.DBFolderSizeMB · TEXT` |  |
| `Depth` |  | Enter the depth of the project site in this field. | Number | — |  | `project.Depth · TEXT` |  |
| `EntityId` | Entity LxID | The Project Entity ID. | Number | — |  | `project.EntityId · TEXT` |  |
| `Frontage` |  | Enter the physical measurements of the face of the building. | Number | — |  | `project.Frontage · TEXT` |  |
| `GrossArea` | Gross Area | Enter the gross area in this field. | Number | — |  | `project.GrossArea · TEXT` |  |
| `LatitudeDegrees` | Latitude | Enter the latitude of the project in this field. To learn how to automatically calculate an entity's latitude and longitude, see the Online Help. | 5-Digit Number | — |  | `project.LatitudeDegrees · TEXT` |  |
| `LongitudeDegrees` | Longitude | Enter the longitude of the project in this field. To learn how to automatically calculate an entity's latitude and longitude, see the Online Help. | 5-Digit Number | — |  | `project.LongitudeDegrees · TEXT` |  |
| `NumberOfDocuments` | Number of Documents | The total number of documents in all folders on the entity. | Number | — |  | `project.NumberOfDocuments · TEXT` |  |
| `ProjectEntityID` | Entity RecID | The ProjectEntityID is the Base Entity System Identifier for associated tasks, folders, documents, forms, and other records. It is assigned automatically by the system, and is not editable. | Number | — |  | `project.ProjectEntityID · TEXT` |  |
| `ProjectID` | Project RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `project.ProjectID · VARCHAR(64) NOT NULL` |  |
| `RentableArea` | Rentable Area | Enter the rentable area in this field. | Number | — |  | `project.RentableArea · TEXT` |  |
| `SequenceNumber` | Sequence Number | This field generates a sequence number for the record. The next record created receives the next number in the sequence. | Number | — |  | `project.SequenceNumber · TEXT` |  |
| `SiteSequenceNumber` | Site Sequence Number | This field is not implemented for projects. | Number | Global |  | `project.SiteSequenceNumber · TEXT` |  |
| `UsableArea` | Usable Area | Enter the usable area. | Number | — |  | `project.UsableArea · TEXT` |  |

### Dates & timestamps (8)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActualEndDate` | Actual/Forecast Delivery Date | If there is a milestone timeline, The max end date from all non-operating tasks. Otherwise, The end date for the entity utilizing the schedule. If there are no tasks defined yet, the system will return the Original End Date / Completion Year set for the entity. | Date | — |  | `project.ActualEndDate · TEXT` |  |
| `ActualStartDate` | Forecast/Actual Start Date | The start date for the schedule associated with your entity. If there are no tasks defined in your schedule, The Original End Date / Completion Year set for the entity. | Date | — |  | `project.ActualStartDate · TEXT` |  |
| `BaselineEndDate` | Baseline Delivery Date | The baseline end date for the entity utilizing the schedules. If there is a milestone timeline the system uses the max end date from all non-operating tasks, otherwise it uses the max end date from the schedule. | Date | — |  | `project.BaselineEndDate · TEXT` |  |
| `ClientScheduleLastReviewedDate` | Last Updated Date | This field displays the last updated date. | Date | — |  | `project.ClientScheduleLastReviewedDate · TEXT` |  |
| `ExpectedEndDate` | Original Delivery Date | The original end date is calculated using the projected / actual end date of the task associated with the latest completed milestone whose phase is not Operations. | Date | — |  | `project.ExpectedEndDate · TEXT` |  |
| `OriginalEndDate` | Baseline End Date | The baseline end date of a schedule task on the entity. | Date | — |  | `project.OriginalEndDate · TEXT` |  |
| `OriginalStartDate` | Baseline Start Date | The baseline start date of a schedule task on the entity. | Date | — |  | `project.OriginalStartDate · TEXT` |  |
| `SlotEndDate` | RE Planner Open Date | The planned open date of the entity as set in the RE Planner. | Date | — |  | `project.SlotEndDate · TEXT` |  |

### Flags (2)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Inactive` | Is Inactive? | If selected, this check box indicates the entity is inactive. | Boolean | — | yes | `project.Inactive · TEXT` |  |
| `IsDead` | Is Dead? | If selected, this check box indicates the entity is dead. | Boolean | — |  | `project.IsDead · TEXT` |  |

### Text & notes (54)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BaseProvider` | System of Record | This field is used to fetch a record value from another Accruent software. | Text | — |  | `project.BaseProvider · TEXT` |  |
| `City` |  | The city associated with this record. | Text | — |  | `project.City · TEXT` |  |
| `CityStateProvinceCountry` | City, State | The city and state / province. If there is no state / province, the field returns only the city. If there is no city, this field returns only the state / province. | Text | — |  | `project.CityStateProvinceCountry · TEXT` |  |
| `ClientEntityID` | Project ID | Enter a unique ID for the entity in this field. Remember: when uploading information to a contract using Lx's import spreadsheet functionality, the entity ID and entity name must be replicated exactly in the spreadsheet. | Text | Global |  | `project.ClientEntityID · TEXT` |  |
| `ComparisonList` | Comparison List | When added to a page layout, this field allows for a comparison of entities from a page or subpage. | Text | — |  | `project.ComparisonList · TEXT` |  |
| `CompletedPhaseStatus` | Completed Phase Status | The milestone timeline status of the entity. This status is updated when a milestone is completed. | Text | — |  | `project.CompletedPhaseStatus · TEXT` |  |
| `ConstructionPhaseStatus` | Construction Phase Status | This field corresponds to the Construction phase in your Milestone Timeline. It captures the most recent status of the milestone phase. | Text | — |  | `project.ConstructionPhaseStatus · TEXT` |  |
| `CountryID` | Country | Select the country from this field. | Text | — |  | `project.CountryID · TEXT` |  |
| `CrossStreet1` | Cross Street #1 | Enter the first cross street in this field. | Text | — |  | `project.CrossStreet1 · TEXT` |  |
| `CrossStreet2` | Cross Street #2 | Enter the second cross street in this field. | Text | — |  | `project.CrossStreet2 · TEXT` |  |
| `CurrentMilestone` | Current Milestone | The current milestone task of your entity schedule. | Text | — |  | `project.CurrentMilestone · TEXT` |  |
| `CurrentPhaseStatus` | Project Status | The project status set by the milestone timeline. This value is driven by your entity schedule. | Text | — |  | `project.CurrentPhaseStatus · TEXT` |  |
| `DesignPhaseStatus` | Design Phase Status | This field corresponds to the Design phase in your Milestone Timeline. It captures the most recent status of the milestone phase. | Text | — |  | `project.DesignPhaseStatus · TEXT` |  |
| `EntityEmail` | Entity Email | The entity's email address that is created when the Email into Lx functionality is enabled. | Text | — |  | `project.EntityEmail · TEXT` |  |
| `EntityPhoto` | Entity Photo | This is a generic field. When you add this field to a page layout, you can use it to add a photo to the layout. | Text | — |  | `project.EntityPhoto · TEXT` |  |
| `FacilityName` | Facility Name | The name of the facility associated with this entity. | Text | — |  | `project.FacilityName · TEXT` |  |
| `FinancialModel` | Financial Model | When added to a page layout, this field appears as a button that generates an Excel Financial Model spreadsheet. If you have questions about this functionality, contact your Accruent representative. | Text | — |  | `project.FinancialModel · TEXT` |  |
| `FirmID` | Firm ID | The record's Firm ID. | Text | — | yes | `project.FirmID · TEXT` |  |
| `Firm_SalesReportLogo` | Sales Report Logo |  | Text | — |  | `project.Firm_SalesReportLogo · TEXT` |  |
| `Firm_SalesReportLogoMadewell` |  |  | Text | — |  |  |  |
| `Firm_SalesReportSignature` | Sales Report Signature |  | Text | — |  | `project.Firm_SalesReportSignature · TEXT` |  |
| `Firm_SalesReportSignatureName` | Sales Report Signature Name |  | Text | — |  | `project.Firm_SalesReportSignatureName · TEXT` |  |
| `Firm_SalesReportSignatureTitle` | Sales Report Signature Title |  | Text | — |  | `project.Firm_SalesReportSignatureTitle · TEXT` |  |
| `HTMLAddress` | Full Address | The associated entity's address in HTML format. | Text | — |  | `project.HTMLAddress · TEXT` |  |
| `IssuesAndAlerts` | Issues And Alerts | This field can be added to page layouts. In View mode, this field will display a table with form and workflow data, such as the work flow / form type, critical issue count, non-critical issue count, escalated count, and past due notification count. | Text | — |  | `project.IssuesAndAlerts · TEXT` |  |
| `MapClientRecordID` | Client Unique ID | The entity Map Client Record ID. | Text | — |  | `project.MapClientRecordID · TEXT` |  |
| `MilestoneTimeline` | Milestone Timeline | This field generates a list of all milestones, but hides those with no values. | Text | — |  | `project.MilestoneTimeline · TEXT` |  |
| `NextMilestone` | Next Milestone | The upcoming milestone in the milestone timeline. | Text | — |  | `project.NextMilestone · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | — |  | `project.Notes · TEXT` |  |
| `OperationsPhaseStatus` | Operations Phase Status | This field corresponds to the Operations phase in your Milestone Timeline. It captures the most recent status of the milestone phase. | Text | — |  | `project.OperationsPhaseStatus · TEXT` |  |
| `Phone` |  | This field can be used to store a phone number. | Text | — |  | `project.Phone · TEXT` |  |
| `PossessionPhaseStatus` | Possession Phase Status | This field corresponds to the Possession phase in your Milestone Timeline. It captures the most recent status of the milestone phase. | Text | — |  | `project.PossessionPhaseStatus · TEXT` |  |
| `PostalCode` | Postal Code | Enter the postal code of the entity in this field. | Text | — |  | `project.PostalCode · TEXT` |  |
| `PotentialProjectName` | Site Name | The name of the site associated with this entity. | Text | — |  | `project.PotentialProjectName · TEXT` |  |
| `PreviousMilestone` | Previous Milestone | The previous milestone task. | Text | — |  | `project.PreviousMilestone · TEXT` |  |
| `ProgramName` | Portfolio/Program Name | The name of the portfolio associated with this entity. | Text | — |  | `project.ProgramName · TEXT` |  |
| `ProjectDescription` | Description | Write a description of the record. | Text | — |  | `project.ProjectDescription · TEXT` |  |
| `ProjectEntityName` | Name | The entity name. | Text | — | yes | `project.ProjectEntityName · TEXT` |  |
| `ProjectEntityTypeName` | Entity Type | The entity type. | Text | — |  | `project.ProjectEntityTypeName · TEXT` |  |
| `ProjectName` | Project Name | The name of the project associated with the record. | Text | — |  | `project.ProjectName · TEXT` |  |
| `ProjectType` | Opening Project or Capital Project | This field has one of two values: opening project or capital project. | Text | Global | yes | `project.ProjectType · TEXT` |  |
| `PrototypeName` | Prototype Name | The name of the prototype associated with this entity. | Text | — |  | `project.PrototypeName · TEXT` |  |
| `RealEstatePhaseStatus` | Real Estate Phase Status | This field corresponds to the Real Estate phase in your Milestone Timeline. It captures the most recent status of the milestone phase. | Text | — |  | `project.RealEstatePhaseStatus · TEXT` |  |
| `RelatedEntities` | Related Entities | The name of entities associated with this entity. | Text | — |  | `project.RelatedEntities · TEXT` |  |
| `RelocatedFrom` |  | Enter where you relocated from in this field. If you created this project using the Convert Site to Project functionality, this field will get the value you entered for the site. | Text | — |  | `project.RelocatedFrom · TEXT` |  |
| `RunReportAction` | Run Report Action | This is a generic field. When you add this field to a page layout, it will run a report. See the Run Report Action Buttons article in the Online Help to learn more. | Text | — |  | `project.RunReportAction · TEXT` |  |
| `StreetAddress` | Street Address | The street address. | Text | — |  | `project.StreetAddress · TEXT` |  |
| `StreetAddress1` | Street Address #1 | The first line of the street address. | Text | — |  | `project.StreetAddress1 · TEXT` |  |
| `StreetAddress2` | Street Address #2 | The second line of the street address. | Text | — |  | `project.StreetAddress2 · TEXT` |  |
| `StreetAddress3` | Street Address #3 | The third line of the street address. | Text | — |  | `project.StreetAddress3 · TEXT` |  |
| `StreetAddress4` | Street Address #4 | The fourth line of the street address. | Text | — |  | `project.StreetAddress4 · TEXT` |  |
| `ThirdPartyWarehouse` | Third Party Warehouse | Enter the name of your third-party warehouse in this field. This field is typically used when a client has purchased materials and is storing them in a warehouse. | Text | — |  | `project.ThirdPartyWarehouse · TEXT` |  |
| `TimeZone` | Time Zone | Select the appropriate time zone from this field. | Text | — |  | `project.TimeZone · TEXT` |  |
| `TradeArea` | Trade Area | Enter the trade area in this field. | Text | — |  | `project.TradeArea · TEXT` |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | — |  | `project.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | — |  | `project.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | — |  | `project.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | — |  | `project.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | — |  | `project.RevNumber · TEXT` |  |
| `UUID` | Project UUID | This field captures a unique identifier associated with your record. This identifier is used if you are using an integration with other Accruent products. | Text | Global |  | `project.UUID · TEXT` |  |
