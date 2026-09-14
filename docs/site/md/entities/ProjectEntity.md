# ProjectEntity

*107 fields · module: Platform & Tenancy · Postgres: `project_entity`*

The generic 'project' record used for capital projects, store rollouts, and portfolio initiatives — distinct from Contract, it tracks phase-gate status (Design, Construction, Possession, Operations) via parallel status/date pairs and milestone pointers, plus SUBMITBUTTON action fields for phase transitions. It spans four top-level groups (Milestones, Schedule, Statics, Summary Information), which is unusual and reflects that a 'project' is a cross-cutting concept touched by scheduling, milestone tracking, and portfolio reporting rather than owned by a single functional group. 170 fields.

Source: `data-fields/project-entity.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 107 |
| Fields with a vendor definition | 101 of 108 inventoried |
| Physical tables | `project_entity` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 170 (165 global, 5 firm) |
| Physical tables | 1 |
| Referenced by | 163 keys from 161 record types |
| Points at | 12 other records |
| Tenancy position | supertype |
| Rules that name it | 11 |

## What to know before rebuilding this

### 6 tenant custom columns

**Observed.** This record carries 6 physical Firm_-prefixed columns — tenant custom fields are real columns, not rows in a value store, so adding one is a DDL change. That is direct evidence for database-per-tenant and against a shared schema.

### The polymorphic spine

**Derived.** The supertype every business record hangs off. Its ProjectEntityTypeName column is the discriminator that makes one physical table present as several record types.

### 5 catalogued Firm-scope fields

**Observed.** Of 170 catalogued fields on this record, 5 are Firm scope — defined by this tenant rather than shipped by the platform. Firm-scope definitions are RGAF rows carrying IsGlobal, FirmID and IsClientExtensionField.

### A hub: 163 keys point here

**Observed.** 161 record types hold a foreign key into this one, so it sits at the centre of the relationship graph. Changing its key or its identity is a change to AccrualTransaction, AcctingAssumptionAdjust, Allowance, AllowanceTransaction and 157 others.

### Lands in project_entity

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 101 fields carry a vendor definition

**Observed.** 101 of this record's 108 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 3 of this record's fields required; the Data Fields catalogue marks 3; 3 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. Field is excluded from the loader field set for this object, so no column is created That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

### 1 field excluded from extraction

**Observed.** Observed of the loader. The inventory marks 1 of this record's fields as not extracted to PostgreSQL, so the replication target creates no column for them. They still exist in Lx; anything reading the replica rather than the product will not see them.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [WF-R-045](../rules/WF-R-045.md) | When an assignee completes the form and presses Submit, SubmitForApprovalByMemberID/Name/Date are set once for the whole step. This is the direct consequence of the approver/assignee asymmetry: assignees do the work, one stamp records that  | Derived |
| [LAY-R-015](../rules/LAY-R-015.md) | Candidate driver fields are: the layout's primary table, plus every table reachable by a many-to-one FK from it, plus `ProjectEntity`. | Derived |
| [FAC-R-018](../rules/FAC-R-018.md) | Input: `Ownership`, `SiteSurvey`, `LandPurchaseSummary`, `LinkLandPurchaseInspection`, `DemographicResults` carry `ProjectEntityID` and no hard-typed FK to `Facility`/`Location`/`Parcel`. Effect: In principle any of these can attach to any  | Derived |
| [PLT-R-001](../rules/PLT-R-001.md) | The record is one of the 161 `entity_scoped` objects (not `ProjectEntity` itself or one of its 9 subtype roots) | Derived |
| [PLT-R-008](../rules/PLT-R-008.md) | The routing rule names a region-scoped principal category (see `../workflow/routing-and-approvals.md` §2, Dimension 2) | Derived |
| [PLT-R-010](../rules/PLT-R-010.md) | Every address block in the product repeats the same `StreetAddress1..4`/`City`/ `PostalCode`/`CountryID`/`JurisdictionID` shape and resolves tax rate through `Jurisdiction`, not through the country/state master directly | Derived |
| [PLT-R-015](../rules/PLT-R-015.md) | A single audit table serves templating across modules; `EntityTemplate` (this module) is the only one of the four whose home object is filed here | Observed |
| [PLT-R-016](../rules/PLT-R-016.md) | Do not silently pick one; `../../data-model/project-entity.md` is built on `ProjectEntity` and is the authority for the spine, but `Project`'s role remains genuinely open | Derived |
| [PPL-R-011](../rules/PPL-R-011.md) | This is a two-hop resolution (entity → region/market → manager), not a direct `Member` attribute lookup | Derived |
| [AST-R-001](../rules/AST-R-001.md) | Trigger: N/A (structural). Input: `Asset.ProjectEntityID`, the only entity-scoping column on `Asset`. | Observed |
| [PRJ-R-002](../rules/PRJ-R-002.md) | An entity needs milestone/phase tracking (`CurrentMilestone`/`NextMilestone`/`PreviousMilestone` on the `ProjectEntity` union block) · `ProcessTimeline` → `ProcessTimelineTemplate` · Produces a flat, non-networked milestone list — no hierar | Observed |

## Fields

### Relationships (foreign keys) (10)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BudgetTemplateID` | Budget Template ID | If there is a budget template associated with this entity, The foreign key of the budget template. | Template ID | Global |  | `project_entity.BudgetTemplateID · TEXT` | [BudgetTemplate](BudgetTemplate.md) |
| `ComplexID` | Complex Name | The ID of the complex associated with the location where the competitor is located. | Complex ID | Global |  | `project_entity.ComplexID · TEXT` | [Complex](Complex.md) |
| `DemographicDMAID` | Demographic DMA | Select your demographic market area from this field. | DMA ID | Global |  | `project_entity.DemographicDMAID · TEXT` | [DMA](DMA.md) |
| `IStateProvinceCountryID` | State | The state or province of the associated entity. | Country, State, County ID | Global |  | `project_entity.IStateProvinceCountryID · TEXT` | [StateProvinceCountry](StateProvinceCountry.md) |
| `JurisdictionID` | Jurisdiction | The county / province associated with the associated entity's address. | County ID | Global |  | `project_entity.JurisdictionID · TEXT` | [Jurisdiction](Jurisdiction.md) |
| `LocationID` | Location | Select the location that your entity will be associated with from this field. | Location ID | Global |  | `project_entity.LocationID · TEXT` | [Location](Location.md) |
| `PrototypeID` | Prototype | Select the prototype associated with this entity from this field. | Prototype ID | Global |  | `project_entity.PrototypeID · TEXT` | [Prototype](Prototype.md) |
| `RegionID` | Region | Select the region and sub-region the entity should belong to from this field. The values that appear in this field depend on the org chart of the portfolio you selected. | Region ID | Global |  | `project_entity.RegionID · TEXT` | [Region](Region.md) |
| `RootRegionID` | Parent Region | This field sets some default membership at the creation of the entity. Its values are pulled from the organization chart. | Region ID | Global |  | `project_entity.RootRegionID · TEXT` | [Region](Region.md) |
| `SubRegionID` | Sub Region | The sub-region. | Region ID | Global |  | `project_entity.SubRegionID · TEXT` | [Region](Region.md) |

### Soft references (2)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `LinkProjectEntityContactListData` | Contact List | This field returns a list of Active and Inactive entities filtered by member security. | Contact | Global |  | `project_entity.LinkProjectEntityContactListData · TEXT` |  |
| `ManagerIDList` | Project Managers | This is a generic field that you can add to a page layout. In View mode, this field returns a list of managers assigned to the entity by the org chart and managers assigned to the entity on an ad hoc basis. In Edit mode, this field allows you to add managers to your entity. | Dropdown | Global |  | `project_entity.ManagerIDList · TEXT` |  |

### Coded values (drop-downs) (11)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeBuildingAreaUnitID` | Building Area Unit | Select the units you are using to measure your area from this field. | Dropdown (Building Area Unit Code) | Global |  | `project_entity.CodeBuildingAreaUnitID · TEXT` | Building Area Unit Code |
| `CodeConstructionTypeID` | Construction Type | Select the construction type from this field. | Dropdown (Construction Type Code) | Global |  | `project_entity.CodeConstructionTypeID · TEXT` | Construction Type Code |
| `CodeCurrencyTypeID` | Currency Type | The Currency Type field allows you to select a currency type to be used on a record. | Dropdown (Currency Type Code) | Global |  | `project_entity.CodeCurrencyTypeID · TEXT` | Currency Type Code |
| `CodeDealTypeID` | Deal Type | This is a generic field. It is not implemented for this record type. | Dropdown (Deal Type Code) | Global |  | `project_entity.CodeDealTypeID · TEXT` | Deal Type Code |
| `CodeDesc_CodeMarketAreaID` | Market Potential | The description of the market. | Dropdown (Market Area Code) | Global |  | `project_entity.CodeDesc_CodeMarketAreaID · TEXT` | Market Area Code |
| `CodeDesc_CodeProjectTypeID` | Real Estate Type | The description of the project type. | Dropdown (Project Type Code) | Global |  | `project_entity.CodeDesc_CodeProjectTypeID · TEXT` | Project Type Code |
| `CodeDistributionCenterID` | Distribution Center | Select the distribution center from which the store is receiving product from this field. | Dropdown (Distribution Center Code) | Global |  | `project_entity.CodeDistributionCenterID · TEXT` | Distribution Center Code |
| `CodeMarketAreaID` | Market Area | Select the market the entity should belong to from this field. The values that appear in this field might depend on the org chart of the portfolio you selected. | Dropdown (Market Area Code) | Global |  | `project_entity.CodeMarketAreaID · TEXT` | Market Area Code |
| `CodeMarketTypeID` | Market Type | Select the market type from this field. | Dropdown (Market Type Code) | Global |  | `project_entity.CodeMarketTypeID · TEXT` | Market Type Code |
| `CodeProjectTypeID` | Project Type | Select the project type from this field. | Dropdown (Project Type Code) | Global |  | `project_entity.CodeProjectTypeID · TEXT` | Project Type Code |
| `CurrentCodeProjectPhaseID` | Project Phase | The project phase set by the milestone timeline. This value is driven by your entity schedule. | Dropdown (Project Phase Code) | Global |  | `project_entity.CurrentCodeProjectPhaseID · TEXT` | Project Phase Code |

### Money (1)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Firm_PriorMonthAccrualTotal` |  |  | Currency | — |  |  |  |

### Quantities (12)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActualRevenueWeeks` | Revenue Weeks | Calculates how many actual revenue weeks this entity will exist during the fiscal year. | Number | Global |  | `project_entity.ActualRevenueWeeks · TEXT` |  |
| `DBFolderSizeMB` | Storage Size (MB) | The folder size in megabytes for a given entity. | 2-Digit Number | Global |  | `project_entity.DBFolderSizeMB · TEXT` |  |
| `Depth` |  | The depth of the associated entity. | Number | Global |  | `project_entity.Depth · TEXT` |  |
| `EntityId` | Entity LxID | The Project Entity ID. | Number | Global |  | `project_entity.EntityId · TEXT` |  |
| `Frontage` |  | Enter the physical measurements of the face of the building. | Number | Global |  | `project_entity.Frontage · TEXT` |  |
| `LatitudeDegrees` | Latitude | Enter the latitude of the entity in this field. To learn how to automatically calculate an entity's latitude and longitude, see the Online Help. | 5-Digit Number | Global |  | `project_entity.LatitudeDegrees · TEXT` |  |
| `LongitudeDegrees` | Longitude | Enter the longitude of the entity in this field. To learn how to automatically calculate an entity's latitude and longitude, see the Online Help. | 5-Digit Number | Global |  | `project_entity.LongitudeDegrees · TEXT` |  |
| `NumberOfDocuments` | Number of Documents | The total number of documents in all folders on the entity. | Number | Global |  | `project_entity.NumberOfDocuments · TEXT` |  |
| `ProjectEntityID` | Entity RecID | The ProjectEntityID is the Base Entity System Identifier for associated tasks, folders, documents, forms, and other records. It is assigned automatically by the system, and is not editable. | Number | Global |  | `project_entity.ProjectEntityID · VARCHAR(64) NOT NULL` |  |
| `RentableArea` | Rentable Area | Enter the rentable area in this field. | Number | Global |  | `project_entity.RentableArea · TEXT` |  |
| `SequenceNumber` | Sequence Number | This field generates a sequence number for the record. The next record created receives the next number in the sequence. | Number | Global |  | `project_entity.SequenceNumber · TEXT` |  |
| `UsableArea` | Usable Area | The usable area. | Number | Global |  | `project_entity.UsableArea · TEXT` |  |

### Dates & timestamps (8)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActualEndDate` | Actual/Forecast Delivery Year | If there is a milestone timeline, The max end date from all non-operating tasks. Otherwise, The end date for the entity utilizing the schedule. If there are no tasks defined yet, the system will return the Original End Date / Completion Year set for the entity. | Date | Global |  | `project_entity.ActualEndDate · TEXT` |  |
| `ActualStartDate` | Forecast/Actual Start Date | The start date for the schedule associated with your entity. If there are no tasks defined in your schedule, The Original End Date / Completion Year set for the entity. | Date | Global |  | `project_entity.ActualStartDate · TEXT` |  |
| `BaselineEndDate` | Baseline Delivery Year | The baseline end date for the entity utilizing the schedules. If there is a milestone timeline the system uses the max end date from all non-operating tasks, otherwise it uses the max end date from the schedule. | Date | Global |  | `project_entity.BaselineEndDate · TEXT` |  |
| `ClientScheduleLastReviewedDate` | Last Updated Date | This field displays the last updated date. | Date | Global |  | `project_entity.ClientScheduleLastReviewedDate · TEXT` |  |
| `ExpectedEndDate` | Original Delivery Year | The original end date is calculated using the projected / actual end date of the task associated with the latest completed milestone whose phase is not Operations. | Date | Global |  | `project_entity.ExpectedEndDate · TEXT` |  |
| `OriginalEndDate` | Baseline End Date | The baseline end date of a schedule task on the entity. | Date | Global |  | `project_entity.OriginalEndDate · TEXT` |  |
| `OriginalStartDate` | Baseline Start Date | The baseline start date of a schedule task on the entity. | Date | Global |  | `project_entity.OriginalStartDate · TEXT` |  |
| `SlotEndDate` | RE Planner Open Year | The planned open date of the entity as set in the RE Planner. | Date | Global |  | `project_entity.SlotEndDate · TEXT` |  |

### Flags (2)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Inactive` | Is Inactive? | If selected, this check box indicates the entity is inactive. | Boolean | Global | yes | `project_entity.Inactive · TEXT` |  |
| `IsDead` | Is Dead? | If selected, this check box indicates the entity is dead. | Boolean | Global |  | `project_entity.IsDead · TEXT` |  |

### Text & notes (54)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BaseProvider` | System of Record | This field is used to fetch a record value from another Accruent software. | Text | Global |  | `project_entity.BaseProvider · TEXT` |  |
| `City` |  | The city associated with this record. | Text | Global |  | `project_entity.City · TEXT` |  |
| `CityStateProvinceCountry` | City, State | The city and state / province. If there is no state / province, the field returns only the city. If there is no city, this field returns only the state / province. | Text | Global |  | `project_entity.CityStateProvinceCountry · TEXT` |  |
| `ClientEntityID` | Store Number | Enter a unique ID for the entity in this field. Remember: when uploading information to a contract using Lx's import spreadsheet functionality, the entity ID and entity name must be replicated exactly in the spreadsheet. | Text | Global |  | `project_entity.ClientEntityID · TEXT` |  |
| `ComparisonList` | Comparison List | When added to a page layout, this field allows for a comparison of entities from a page or subpage. | Text | Global |  | `project_entity.ComparisonList · TEXT` |  |
| `CompletedPhaseStatus` | Completed Phase Status | The milestone timeline status of the entity. This status is updated when a milestone is completed. | Text | Global |  | `project_entity.CompletedPhaseStatus · TEXT` |  |
| `ConstructionPhaseStatus` | Construction Phase Status | This field corresponds to the Construction phase in your Milestone Timeline. It captures the most recent status of the milestone phase. | Text | Global |  | `project_entity.ConstructionPhaseStatus · TEXT` |  |
| `CountryID` | Country | Select the country from this field. | Text | Global |  | `project_entity.CountryID · TEXT` |  |
| `CrossStreet1` | Cross Street #1 | Enter the first cross street in this field. | Text | Global |  | `project_entity.CrossStreet1 · TEXT` |  |
| `CrossStreet2` | Cross Street #2 | Enter the second cross street in this field. | Text | Global |  | `project_entity.CrossStreet2 · TEXT` |  |
| `CurrentMilestone` | Current Milestone | The current milestone task of your entity schedule. | Text | Global |  | `project_entity.CurrentMilestone · TEXT` |  |
| `CurrentPhaseStatus` | Project Status | The project status set by the milestone timeline. This value is driven by your entity schedule. | Text | Global |  | `project_entity.CurrentPhaseStatus · TEXT` |  |
| `DesignPhaseStatus` | Design Phase Status | This field corresponds to the Design phase in your Milestone Timeline. It captures the most recent status of the milestone phase. | Text | Global |  | `project_entity.DesignPhaseStatus · TEXT` |  |
| `EntityEmail` | Entity Email | The entity's email address that is created when the Email into Lx functionality is enabled. | Text | Global |  | `project_entity.EntityEmail · TEXT` |  |
| `EntityPhoto` | Entity Photo | This is a generic field. When you add this field to a page layout, you can use it to add a photo to the layout. | Text | Global |  | `project_entity.EntityPhoto · TEXT` |  |
| `FacilityName` | Facility Name | The name of the facility associated with this entity. | Text | Global |  | `project_entity.FacilityName · TEXT` |  |
| `FinancialModel` | Financial Model | When added to a page layout, this field appears as a button that generates an Excel Financial Model spreadsheet. If you have questions about this functionality, contact your Accruent representative. | Text | Global |  | `project_entity.FinancialModel · TEXT` |  |
| `FirmID` | Firm ID | The record's Firm ID. | Text | Global | yes | `project_entity.FirmID · TEXT` |  |
| `Firm_SalesReportLogo` | Sales Report Logo |  | Text | Firm |  | `project_entity.Firm_SalesReportLogo · TEXT` |  |
| `Firm_SalesReportLogoMadewell` |  |  | Text | — |  |  |  |
| `Firm_SalesReportSignature` | Sales Report Signature |  | Text | Firm |  | `project_entity.Firm_SalesReportSignature · TEXT` |  |
| `Firm_SalesReportSignatureName` | Sales Report Signature Name |  | Text | Firm |  | `project_entity.Firm_SalesReportSignatureName · TEXT` |  |
| `Firm_SalesReportSignatureTitle` | Sales Report Signature Title |  | Text | Firm |  | `project_entity.Firm_SalesReportSignatureTitle · TEXT` |  |
| `HTMLAddress` | Full Address | The associated entity's address in HTML format. | Text | Global |  | `project_entity.HTMLAddress · TEXT` |  |
| `IssuesAndAlerts` | Issues And Alerts | This field can be added to page layouts. In View mode, this field will display a table with form and workflow data, such as the work flow / form type, critical issue count, non-critical issue count, escalated count, and past due notification count. | Text | Global |  | `project_entity.IssuesAndAlerts · TEXT` |  |
| `MapClientRecordID` | Client Unique ID | The entity Map Client Record ID. | Text | Global |  | `project_entity.MapClientRecordID · TEXT` |  |
| `MilestoneTimeline` | Milestone Timeline | This field generates a list of all milestones, but hides those with no values. | Text | Global |  | `project_entity.MilestoneTimeline · TEXT` |  |
| `NextMilestone` | Next Milestone | The upcoming milestone in the milestone timeline. | Text | Global |  | `project_entity.NextMilestone · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `project_entity.Notes · TEXT` |  |
| `OperationsPhaseStatus` | Operations Phase Status | This field corresponds to the Operations phase in your Milestone Timeline. It captures the most recent status of the milestone phase. | Text | Global |  | `project_entity.OperationsPhaseStatus · TEXT` |  |
| `Phone` |  | This field can be used to store a phone number. | Text | Global |  | `project_entity.Phone · TEXT` |  |
| `PossessionPhaseStatus` | Possession Phase Status | This field corresponds to the Possession phase in your Milestone Timeline. It captures the most recent status of the milestone phase. | Text | Global |  | `project_entity.PossessionPhaseStatus · TEXT` |  |
| `PostalCode` | Postal Code | Enter the postal code of the entity in this field. | Text | Global |  | `project_entity.PostalCode · TEXT` |  |
| `PotentialProjectName` | Site Name | The name of the site associated with this entity. | Text | Global |  | `project_entity.PotentialProjectName · TEXT` |  |
| `PreviousMilestone` | Previous Milestone | The previous milestone task. | Text | Global |  | `project_entity.PreviousMilestone · TEXT` |  |
| `ProgramID` | Portfolio/Program RecID | Select the Portfolio that the entity belongs to from this field. | Text | Global |  | `project_entity.ProgramID · TEXT` |  |
| `ProgramName` | Portfolio/Program Name | The name of the portfolio associated with this entity. | Text | Global |  | `project_entity.ProgramName · TEXT` |  |
| `ProjectDescription` | Description | Write a description of the record. | Text | Global |  | `project_entity.ProjectDescription · TEXT` |  |
| `ProjectEntityName` | Name | The entity name. | Text | Global | yes | `project_entity.ProjectEntityName · TEXT` |  |
| `ProjectEntityTypeName` | Entity Type | The entity type. | Text | Global |  | `project_entity.ProjectEntityTypeName · TEXT` |  |
| `ProjectName` | Project Name | The name of the project associated with the record. | Text | Global |  | `project_entity.ProjectName · TEXT` |  |
| `PrototypeName` | Prototype Name | The name of the prototype associated with this entity. | Text | Global |  | `project_entity.PrototypeName · TEXT` |  |
| `RealEstatePhaseStatus` | Real Estate Phase Status | This field corresponds to the Real Estate phase in your Milestone Timeline. It captures the most recent status of the milestone phase. | Text | Global |  | `project_entity.RealEstatePhaseStatus · TEXT` |  |
| `RelatedEntities` | Related Entities | The name of entities associated with this entity. | Text | Global |  | `project_entity.RelatedEntities · TEXT` |  |
| `RelocatedFrom` |  | Enter where you relocated from in this field. | Text | Global |  | `project_entity.RelocatedFrom · TEXT` |  |
| `RunReportAction` | Run Report Action | This is a generic field. When you add this field to a page layout, it will run a report. See the Run Report Action Buttons article in the Online Help to learn more. | Text | Global |  | `project_entity.RunReportAction · TEXT` |  |
| `StreetAddress` | Street Address | The street address. | Text | Global |  | `project_entity.StreetAddress · TEXT` |  |
| `StreetAddress1` | Street Address #1 | The first line of the street address. | Text | Global |  | `project_entity.StreetAddress1 · TEXT` |  |
| `StreetAddress2` | Street Address #2 | The second line of the street address. | Text | Global |  | `project_entity.StreetAddress2 · TEXT` |  |
| `StreetAddress3` | Street Address #3 | The third line of the street address. | Text | Global |  | `project_entity.StreetAddress3 · TEXT` |  |
| `StreetAddress4` | Street Address #4 | The fourth line of the street address. | Text | Global |  | `project_entity.StreetAddress4 · TEXT` |  |
| `ThirdPartyWarehouse` | Third Party Warehouse | Enter the name of your third-party warehouse in this field. This field is typically used when a client has purchased materials and is storing them in a warehouse. | Text | Global |  | `project_entity.ThirdPartyWarehouse · TEXT` |  |
| `TimeZone` | Time Zone | Select the appropriate time zone from this field. | Text | Global |  | `project_entity.TimeZone · TEXT` |  |
| `TradeArea` | Trade Area | The trade area. | Text | Global |  | `project_entity.TradeArea · TEXT` |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `project_entity.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `project_entity.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `project_entity.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `project_entity.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | Global |  | `project_entity.RevNumber · TEXT` |  |
| `UUID` | Entity UUID | This field captures a unique identifier associated with your record. This identifier is used if you are using an integration with other Accruent products. | Text | Global |  | `project_entity.UUID · TEXT` |  |

### Other (1)

Everything that did not fall into a named group.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `GrossArea` | Gross Area | Enter the gross area in this field. | Acreage | Global |  | `project_entity.GrossArea · TEXT` |  |

## What points here (163 keys)

| Record type | Via column |
|---|---|
| [BudgetOption](BudgetOption.md) | `BudgetOptionTemplateID`, `ProjectEntityID` |
| [DevelopmentSlot](DevelopmentSlot.md) | `ProjectEntityID`, `ProjectPEID` |
| [AccrualTransaction](AccrualTransaction.md) | `ProjectEntityID` |
| [AcctingAssumptionAdjust](AcctingAssumptionAdjust.md) | `ProjectEntityID` |
| [Allowance](Allowance.md) | `ProjectEntityID` |
| [AllowanceTransaction](AllowanceTransaction.md) | `ProjectEntityID` |
| [AlternateRentSchedule](AlternateRentSchedule.md) | `ProjectEntityID` |
| [Asset](Asset.md) | `ProjectEntityID` |
| [AuditColumn](AuditColumn.md) | `ProjectEntityID` |
| [AuditTable](AuditTable.md) | `ProjectEntityID` |
| [BidPackage](BidPackage.md) | `ProjectEntityID` |
| [BidPackageAlternate](BidPackageAlternate.md) | `ProjectEntityID` |
| [BidPackageAlternateValue](BidPackageAlternateValue.md) | `ProjectEntityID` |
| [BidPackageBreakout](BidPackageBreakout.md) | `ProjectEntityID` |
| [BidPackageBreakoutValue](BidPackageBreakoutValue.md) | `ProjectEntityID` |
| [BidPackageTemplate](BidPackageTemplate.md) | `ProjectEntityID` |
| [BidderIssue](BidderIssue.md) | `ProjectEntityID` |
| [BudgetColumn](BudgetColumn.md) | `ProjectEntityID` |
| [BudgetColumnItemValue](BudgetColumnItemValue.md) | `ProjectEntityID` |
| [BudgetIndexValue](BudgetIndexValue.md) | `ProjectEntityID` |
| [BudgetLineGroup](BudgetLineGroup.md) | `ProjectEntityID` |
| [BudgetLineItem](BudgetLineItem.md) | `ProjectEntityID` |
| [BudgetLineLeaf](BudgetLineLeaf.md) | `ProjectEntityID` |
| [BudgetTemplate](BudgetTemplate.md) | `ProjectEntityID` |
| [BudgetTemplateAudit](BudgetTemplateAudit.md) | `ProjectEntityID` |
| [BudgetView](BudgetView.md) | `ProjectEntityID` |
| [CLRExtensionPart](CLRExtensionPart.md) | `ProjectEntityID` |
| [CPI](CPI.md) | `ProjectEntityID` |
| [ChangeOrder](ChangeOrder.md) | `ProjectEntityID` |
| [ClientListRow](ClientListRow.md) | `ProjectEntityID` |
| [CoTenancy](CoTenancy.md) | `ProjectEntityID` |
| [CommitteePackage](CommitteePackage.md) | `ProjectEntityID` |
| [ComparisonItem](ComparisonItem.md) | `ProjectEntityID` |
| [ComparisonReport](ComparisonReport.md) | `ProjectEntityID` |
| [Competitor](Competitor.md) | `ProjectEntityID` |
| [ContractAmendment](ContractAmendment.md) | `ProjectEntityID` |
| [ContractFinancialTest](ContractFinancialTest.md) | `ProjectEntityID` |
| [ContractTerm](ContractTerm.md) | `ProjectEntityID` |
| [CostTrackingTemplate](CostTrackingTemplate.md) | `ProjectEntityID` |
| [Covenant](Covenant.md) | `ProjectEntityID` |
| [DemographicResults](DemographicResults.md) | `ProjectEntityID` |
| [DevelopmentPlan](DevelopmentPlan.md) | `ProjectEntityID` |
| [Document](Document.md) | `ProjectEntityID` |
| [DocumentMarkup](DocumentMarkup.md) | `ProjectEntityID` |
| [EMailReceivedLog](EMailReceivedLog.md) | `ProjectEntityID` |
| [EMailSentLog](EMailSentLog.md) | `ProjectEntityID` |
| [EntityTemplate](EntityTemplate.md) | `ProjectEntityID` |
| [ExpenseAccrualSchedule](ExpenseAccrualSchedule.md) | `ProjectEntityID` |
| [ExpenseAccrualSetup](ExpenseAccrualSetup.md) | `ProjectEntityID` |
| [ExpenseAllocation](ExpenseAllocation.md) | `ProjectEntityID` |
| [ExpenseEscalation](ExpenseEscalation.md) | `ProjectEntityID` |
| [ExpenseRecovery](ExpenseRecovery.md) | `ProjectEntityID` |
| [ExpenseRecoveryItem](ExpenseRecoveryItem.md) | `ProjectEntityID` |
| [ExpenseRecoveryItemMapping](ExpenseRecoveryItemMapping.md) | `ProjectEntityID` |
| [ExpenseSchedule](ExpenseSchedule.md) | `ProjectEntityID` |
| [ExpenseSetup](ExpenseSetup.md) | `ProjectEntityID` |
| [ExpenseVendorAllocation](ExpenseVendorAllocation.md) | `ProjectEntityID` |
| [FacilityExpense](FacilityExpense.md) | `ProjectEntityID` |
| [FinancialAdjustment](FinancialAdjustment.md) | `ProjectEntityID` |
| [FiscalPeriod](FiscalPeriod.md) | `ProjectEntityID` |
| [Folder](Folder.md) | `ProjectEntityID` |
| [FolderTemplate](FolderTemplate.md) | `ProjectEntityID` |
| [FolderTemplateAudit](FolderTemplateAudit.md) | `ProjectEntityID` |
| [Insurance](Insurance.md) | `ProjectEntityID` |
| [InvoiceIssue](InvoiceIssue.md) | `ProjectEntityID` |
| [InvoiceItem](InvoiceItem.md) | `ProjectEntityID` |
| [Issue](Issue.md) | `ProjectEntityID` |
| [IssueResponse](IssueResponse.md) | `ProjectEntityID` |
| [IssueSubmittal](IssueSubmittal.md) | `ProjectEntityID` |
| [KeyDate](KeyDate.md) | `ProjectEntityID` |
| [LandPurchaseSummary](LandPurchaseSummary.md) | `ProjectEntityID` |
| [LandlordInvoice](LandlordInvoice.md) | `ProjectEntityID` |
| [LandlordInvoiceItem](LandlordInvoiceItem.md) | `ProjectEntityID` |
| [LeaseAudit](LeaseAudit.md) | `ProjectEntityID` |
| [LeaseInfo](LeaseInfo.md) | `ProjectEntityID` |
| [LinkBudgetIndexBLI](LinkBudgetIndexBLI.md) | `ProjectEntityID` |
| [LinkBudgetViewBLI](LinkBudgetViewBLI.md) | `ProjectEntityID` |
| [LinkEMailReceivedLogDocument](LinkEMailReceivedLogDocument.md) | `ProjectEntityID` |
| [LinkIssuePart](LinkIssuePart.md) | `ProjectEntityID` |
| [LinkIssuePartOrder](LinkIssuePartOrder.md) | `ProjectEntityID` |
| [LinkLandPurchaseInspection](LinkLandPurchaseInspection.md) | `ProjectEntityID` |
| [LinkLandlordInvPaymentTxn](LinkLandlordInvPaymentTxn.md) | `ProjectEntityID` |
| [LinkMemberProjectEntity](LinkMemberProjectEntity.md) | `ProjectEntityID` |
| [LinkPEMemberCodeJobTitle](LinkPEMemberCodeJobTitle.md) | `ProjectEntityID` |
| [LinkProjectEntityContact](LinkProjectEntityContact.md) | `ProjectEntityID` |
| [LinkProjectEntityVendor](LinkProjectEntityVendor.md) | `ProjectEntityID` |
| [LinkReTransScenContact](LinkReTransScenContact.md) | `ProjectEntityID` |
| [LinkReceiptTransaction](LinkReceiptTransaction.md) | `ProjectEntityID` |
| [LinkRegionManager](LinkRegionManager.md) | `ProjectEntityID` |
| [LinkSchedOffsetExpGrpType](LinkSchedOffsetExpGrpType.md) | `ProjectEntityID` |
| [LinkTaskByCodeMember](LinkTaskByCodeMember.md) | `ProjectEntityID` |
| [LinkTaskDocument](LinkTaskDocument.md) | `ProjectEntityID` |
| [LinkTaskMember](LinkTaskMember.md) | `ProjectEntityID` |
| [MapClientSchedule](MapClientSchedule.md) | `ProjectEntityID` |
| [MemberAudit](MemberAudit.md) | `ProjectEntityID` |
| [Notify](Notify.md) | `ProjectEntityID` |
| [Ownership](Ownership.md) | `ProjectEntityID` |
| [ParcelAccess](ParcelAccess.md) | `ProjectEntityID` |
| [Parking](Parking.md) | `ProjectEntityID` |
| [Party](Party.md) | `ProjectEntityID` |
| [PayApp](PayApp.md) | `ProjectEntityID` |
| [PaymentReceipt](PaymentReceipt.md) | `ProjectEntityID` |
| [PaymentTransaction](PaymentTransaction.md) | `ProjectEntityID` |
| [PaymentTransactionFullImport](PaymentTransactionFullImport.md) | `ProjectEntityID` |
| [PercentageRent](PercentageRent.md) | `ProjectEntityID` |
| [PercentageRentBreakpoint](PercentageRentBreakpoint.md) | `ProjectEntityID` |
| [ProFormaBudget](ProFormaBudget.md) | `ProjectEntityID` |
| [ProcessTimeline](ProcessTimeline.md) | `ProjectEntityID` |
| [ProgramRevenueWeeks](ProgramRevenueWeeks.md) | `ProjectEntityID` |
| [PropertyTaxAppeal](PropertyTaxAppeal.md) | `ProjectEntityID` |
| [PropertyTaxAppealAward](PropertyTaxAppealAward.md) | `ProjectEntityID` |
| [PropertyTaxAssessment](PropertyTaxAssessment.md) | `ProjectEntityID` |
| [PropertyTaxBill](PropertyTaxBill.md) | `ProjectEntityID` |
| [PropertyTaxDetail](PropertyTaxDetail.md) | `ProjectEntityID` |
| [PropertyTaxSummary](PropertyTaxSummary.md) | `ProjectEntityID` |
| [PurchaseOrder](PurchaseOrder.md) | `ProjectEntityID` |
| [Question](Question.md) | `ProjectEntityID` |
| [RETransaction](RETransaction.md) | `ProjectEntityID` |
| [RecalcOverrideNotes](RecalcOverrideNotes.md) | `ProjectEntityID` |
| [Region](Region.md) | `ProjectEntityID` |
| [Responsibility](Responsibility.md) | `ProjectEntityID` |
| [SLPeriod](SLPeriod.md) | `ProjectEntityID` |
| [SLSummary](SLSummary.md) | `ProjectEntityID` |
| [Sales](Sales.md) | `ProjectEntityID` |
| [SalesExclusion](SalesExclusion.md) | `ProjectEntityID` |
| [SalesExclusionCap](SalesExclusionCap.md) | `ProjectEntityID` |
| [Scenario](Scenario.md) | `ProjectEntityID` |
| [ScheduledOffset](ScheduledOffset.md) | `ProjectEntityID` |
| [ScratchPad](ScratchPad.md) | `ProjectEntityID` |
| [SecurityDeposit](SecurityDeposit.md) | `ProjectEntityID` |
| [ServiceRequest](ServiceRequest.md) | `ProjectEntityID` |
| [SiteSurvey](SiteSurvey.md) | `ProjectEntityID` |
| [Space](Space.md) | `ProjectEntityID` |
| [Task](Task.md) | `ProjectEntityID` |
| [TaskGroup](TaskGroup.md) | `ProjectEntityID` |
| [TaskItem](TaskItem.md) | `ProjectEntityID` |
| [TaskPredecessor](TaskPredecessor.md) | `ProjectEntityID` |
| [TaskTemplate](TaskTemplate.md) | `ProjectEntityID` |
| [TaskTemplateAudit](TaskTemplateAudit.md) | `ProjectEntityID` |
| [TemplateAudit](TemplateAudit.md) | `ProjectEntityID` |
| [Tenant](Tenant.md) | `ProjectEntityID` |
| [Usage](Usage.md) | `ProjectEntityID` |
| [UseBasedRent](UseBasedRent.md) | `ProjectEntityID` |
| [UseBasedRentBreakpoint](UseBasedRentBreakpoint.md) | `ProjectEntityID` |
| [VariableRentOffset](VariableRentOffset.md) | `ProjectEntityID` |
| [VirtualPRAccrualPeriod](VirtualPRAccrualPeriod.md) | `ProjectEntityID` |
| [VirtualPRPAggregate](VirtualPRPAggregate.md) | `ProjectEntityID` |
| [VirtualPercentageRentPeriod](VirtualPercentageRentPeriod.md) | `ProjectEntityID` |
| [VirtualTemplateBudget](VirtualTemplateBudget.md) | `ProjectEntityID` |
| [VirtualTemplateBudgetOption](VirtualTemplateBudgetOption.md) | `ProjectEntityID` |
| [VirtualTemplateFolder](VirtualTemplateFolder.md) | `ProjectEntityID` |
| [VirtualTemplateSchedule](VirtualTemplateSchedule.md) | `ProjectEntityID` |
| [VirtualUBRPAggregate](VirtualUBRPAggregate.md) | `ProjectEntityID` |
| [VirtualUseBasedRentPeriod](VirtualUseBasedRentPeriod.md) | `ProjectEntityID` |
| [WFStepFullImport](WFStepFullImport.md) | `ProjectEntityID` |
| [WorkFlow](WorkFlow.md) | `ProjectEntityID` |
| [WorkFlowStep](WorkFlowStep.md) | `ProjectEntityID` |
| [WorkFlowStepApprover](WorkFlowStepApprover.md) | `ProjectEntityID` |
| [WorkFlowStepAssignee](WorkFlowStepAssignee.md) | `ProjectEntityID` |
| [WorkFlowTemplateStepAction](WorkFlowTemplateStepAction.md) | `ProjectEntityID` |
| [WorkOrder](WorkOrder.md) | `ProjectEntityID` |
