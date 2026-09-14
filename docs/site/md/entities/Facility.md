# Facility

*133 fields · module: Facilities, Locations & Sites · Postgres: `facility`*

The physical property/building record — address fields (Street Address #1-3, City, State, Postal Code, Jurisdiction) plus facility-level dates and area figures. 89 fields (88 Global, 1 Firm) under its own top-level Facility group; this is the most 'plain real estate' entity in the catalog, closer to a CRM property record than a financial one, which is reflected in the dominance of TEXT and DATE field types over MONEY.

Source: `data-fields/facility.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 133 |
| Fields with a vendor definition | 125 of 140 inventoried |
| Physical tables | `facility` |
| Replication database | `lxr_drp_bbw` |
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

### Lands in facility

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 125 fields carry a vendor definition

**Observed.** 125 of this record's 140 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: the captures agree

**Observed.** Over the 85 fields both the Data Fields catalogue and the field inventory contain, the two agree on every one. 11 are marked required.

### 1 field excluded from extraction

**Observed.** Observed of the loader. The inventory marks 1 of this record's fields as not extracted to PostgreSQL, so the replication target creates no column for them. They still exist in Lx; anything reading the replica rather than the product will not see them.

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

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BudgetTemplateID` | Budget Template ID | If there is a budget template associated with this entity, The foreign key of the budget template. | Template ID | — |  | `facility.BudgetTemplateID · TEXT` | [BudgetTemplate](BudgetTemplate.md) |
| `ComplexID` | Complex Name | The ID of the complex associated with the location where the competitor is located. | Complex ID | — |  | `facility.ComplexID · TEXT` | [Complex](Complex.md) |
| `DemographicDMAID` | Demographic DMA | Select your demographic market area from this field. | DMA ID | — |  | `facility.DemographicDMAID · TEXT` | [DMA](DMA.md) |
| `IStateProvinceCountryID` | State | Select the state or province from this field. | Country, State, County ID | Global |  | `facility.IStateProvinceCountryID · TEXT` | [StateProvinceCountry](StateProvinceCountry.md) |
| `JurisdictionID` | Jurisdiction | The county / province associated with the associated entity's address. | County ID | Global |  | `facility.JurisdictionID · TEXT` | [Jurisdiction](Jurisdiction.md) |
| `LocationID` | Location | Select the location that your entity will be associated with from this field. | Location ID | Global | yes | `facility.LocationID · TEXT` | [Location](Location.md) |
| `ProgramID` | Portfolio | Select the Portfolio that the entity belongs to from this field. | Portfolio ID | Global | yes | `facility.ProgramID · TEXT` | [Program](Program.md) |
| `PrototypeID` | Prototype | Select the prototype associated with this entity from this field. | Prototype ID | Global |  | `facility.PrototypeID · TEXT` | [Prototype](Prototype.md) |
| `RegionID` | Region | Select the region and sub-region the facility should belong to from this field. The values that appear in this field depend on the org chart of the portfolio you selected. | Region ID | Global | yes | `facility.RegionID · TEXT` | [Region](Region.md) |
| `RootRegionID` | Parent Region | This field sets some default membership at the creation of the entity. Its values are pulled from the organization chart. | Region ID | Global |  | `facility.RootRegionID · TEXT` | [Region](Region.md) |
| `SubRegionID` | Sub Region | This field pulls the sub-region from the facility's associated location record. | Region ID | Global |  | `facility.SubRegionID · TEXT` | [Region](Region.md) |

### Soft references (3)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `LinkProjectEntityContactListData` | Contact List | This field returns a list of Active and Inactive entities filtered by member security. | Contact | — |  | `facility.LinkProjectEntityContactListData · TEXT` |  |
| `ManagerIDList` | Project Managers | This is a generic field that you can add to a page layout. In View mode, this field returns a list of managers assigned to the entity by the org chart and managers assigned to the entity on an ad hoc basis. In Edit mode, this field allows you to add managers to your entity. | Dropdown | Global |  | `facility.ManagerIDList · TEXT` |  |
| `OpeningProjectPEID` | Opening Project | This field determines the associated opening project for the facility. | Entity | Global |  | `facility.OpeningProjectPEID · TEXT` |  |

### Coded values (drop-downs) (16)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeBuildingAreaUnitID` | Building Area Unit | Select the units you are using to measure your area from this field. | Dropdown (Building Area Unit Code) | Global |  | `facility.CodeBuildingAreaUnitID · TEXT` | Building Area Unit Code |
| `CodeConstructionTypeID` | Construction Type | Select the construction type from this field. | Dropdown (Construction Type Code) | Global |  | `facility.CodeConstructionTypeID · TEXT` | Construction Type Code |
| `CodeCurrencyTypeID` | Currency Type | The Currency Type field allows you to select a currency type to be used on a record. | Dropdown (Currency Type Code) | — |  | `facility.CodeCurrencyTypeID · TEXT` | Currency Type Code |
| `CodeDealTypeID` | Deal Type | Select the deal type from this field. | Dropdown (Deal Type Code) | Global |  | `facility.CodeDealTypeID · TEXT` | Deal Type Code |
| `CodeDesc_CodeMarketAreaID` | Market Potential | The description of the market of the location. | Dropdown (Market Area Code) | Global |  | `facility.CodeDesc_CodeMarketAreaID · TEXT` | Market Area Code |
| `CodeDesc_CodeProjectTypeID` | Real Estate Type | This is a generic field. It is not implemented for facilties by default. | Dropdown (Project Type Code) | Global |  | `facility.CodeDesc_CodeProjectTypeID · TEXT` | Project Type Code |
| `CodeDistributionCenterID` | Distribution Center | Select the distribution center from which the store is receiving product from this field. | Dropdown (Distribution Center Code) | Global |  | `facility.CodeDistributionCenterID · TEXT` | Distribution Center Code |
| `CodeFacilityCategoryID` | Facility Category | Select the facility category from this field. Categories are the third level of organization in Lx. Categories are the children of types, and grandchildren of groups. Groups, types, and categories are used to simplify reporting. | Dropdown (Facility Category Code) | Global |  | `facility.CodeFacilityCategoryID · TEXT` | Facility Category Code |
| `CodeFacilityGroupID` | Facility Group | Select the facility group from this field. Groups are the first level of organization in Lx. Groups are the parents of types, and grandparents of Categories. Groups, types, and categories are used to simplify reporting. | Dropdown (Facility Group Code) | Global |  | `facility.CodeFacilityGroupID · TEXT` | Facility Group Code |
| `CodeFacilityStatusID` | Facility Status | Select the facility status from this field. | Dropdown (Facility Status Code) | Global |  | `facility.CodeFacilityStatusID · TEXT` | Facility Status Code |
| `CodeFacilityTypeID` | Facility Type | Select the facility type from this field. Types are the second level of organization in Lx. Types are the children of groups, and parents of categories. Groups, types, and categories are used to simplify reporting. | Dropdown (Facility Type Code) | Global |  | `facility.CodeFacilityTypeID · TEXT` | Facility Type Code |
| `CodeFacilityUseID` | Facility Use | Select the facility use from this field. | Dropdown (Facility Use Code) | Global |  | `facility.CodeFacilityUseID · TEXT` | Facility Use Code |
| `CodeMarketAreaID` | Market Area | Select the market the facility should belong to from this field. The values that appear in this field might depend on the org chart of the portfolio you selected. | Dropdown (Market Area Code) | Global | yes | `facility.CodeMarketAreaID · TEXT` | Market Area Code |
| `CodeMarketTypeID` | Market Type | Select the market type from this field. | Dropdown (Market Type Code) | Global |  | `facility.CodeMarketTypeID · TEXT` | Market Type Code |
| `CodeProjectTypeID` | Project Type | This is a generic field. It is not implemented for facilties by default. | Dropdown (Project Type Code) | Global |  | `facility.CodeProjectTypeID · TEXT` | Project Type Code |
| `CurrentCodeProjectPhaseID` | Project Phase | The project phase set by the milestone timeline. This value is driven by your entity schedule. | Dropdown (Project Phase Code) | — |  | `facility.CurrentCodeProjectPhaseID · TEXT` | Project Phase Code |

### Money (2)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Firm_PriorMonthAccrualTotal` |  |  | Currency | — |  |  |  |
| `LastYearsAnnualSales` | Last Years Annual Sales | Enter last year's annual sales in this field. | Currency | Global |  | `facility.LastYearsAnnualSales · TEXT` |  |

### Quantities (20)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActualRevenueWeeks` | Revenue Weeks | Calculates how many actual revenue weeks this entity will exist during the fiscal year. | Number | — |  | `facility.ActualRevenueWeeks · TEXT` |  |
| `BehindScheduleDays` | Behind Schedule Days | This field displays the number of days behind schedule. | Number | Global |  | `facility.BehindScheduleDays · TEXT` |  |
| `DBFolderSizeMB` | Storage Size (MB) | The folder size in megabytes for a given entity. | 2-Digit Number | — |  | `facility.DBFolderSizeMB · TEXT` |  |
| `DaysUntilOpen` | Days Until Open | This field is not implemented for facilities. | Number | Global |  | `facility.DaysUntilOpen · TEXT` |  |
| `Depth` |  | Enter the depth of the facility in this field. | Number | Global |  | `facility.Depth · TEXT` |  |
| `DistributionCenterArea` | Distribution Center Area | Enter the size of the distribution center in this field. | Number | Global |  | `facility.DistributionCenterArea · TEXT` |  |
| `EntityId` | Entity LxID | The Project Entity ID. | Number | — |  | `facility.EntityId · TEXT` |  |
| `FacilityID` | Facility RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `facility.FacilityID · VARCHAR(64) NOT NULL` |  |
| `Firm_SellingSQFT` | Selling SQFT |  | Number | — |  | `facility.Firm_SellingSQFT · TEXT` |  |
| `Frontage` |  | Enter the physical measurements of the face of the building. | Number | Global |  | `facility.Frontage · TEXT` |  |
| `GrossArea` | Gross Area | Enter the gross area in this field. | Number | Global |  | `facility.GrossArea · TEXT` |  |
| `LatitudeDegrees` | Latitude | Enter the latitude of the facility in this field. To learn how to automatically calculate an entity's latitude and longitude, see the Online Help. | 5-Digit Number | — |  | `facility.LatitudeDegrees · TEXT` |  |
| `LongitudeDegrees` | Longitude | Enter the longitude of the facility in this field. To learn how to automatically calculate an entity's latitude and longitude, see the Online Help. | 5-Digit Number | — |  | `facility.LongitudeDegrees · TEXT` |  |
| `NumberOfDocuments` | Number of Documents | The total number of documents in all folders on the entity. | Number | — |  | `facility.NumberOfDocuments · TEXT` |  |
| `OpenYear` | Open year | The year the facility opened. | Number | Global |  | `facility.OpenYear · TEXT` |  |
| `OutOfDateDays` | Out Of Date Days | This field returns how many days the schedule is out of date. If the schedule hasn't been updated yet, the value of this field is 0. If the schedule has been updated, the value of the field is calculated based on the last reviewed date. | Number | Global |  | `facility.OutOfDateDays · TEXT` |  |
| `ProjectEntityID` | Entity RecID | The ProjectEntityID is the Base Entity System Identifier for associated tasks, folders, documents, forms, and other records. It is assigned automatically by the system, and is not editable. | Number | Global | yes | `facility.ProjectEntityID · TEXT` |  |
| `RentableArea` | Rentable Area | Enter the rentable area in this field. | Number | Global |  | `facility.RentableArea · TEXT` |  |
| `SequenceNumber` | Sequence Number | This field generates a sequence number for the record. The next record created receives the next number in the sequence. | Number | Global |  | `facility.SequenceNumber · TEXT` |  |
| `UsableArea` | Usable Area | Enter the usable area. | Number | Global |  | `facility.UsableArea · TEXT` |  |

### Dates & timestamps (13)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActualEndDate` | Actual/Forecast Delivery Date | If there is a milestone timeline, The max end date from all non-operating tasks. Otherwise, The end date for the entity utilizing the schedule. If there are no tasks defined yet, the system will return the Original End Date / Completion Year set for the entity. | Date | Global |  | `facility.ActualEndDate · TEXT` |  |
| `ActualStartDate` | Forecast/Actual Start Date | The start date for the schedule associated with your entity. If there are no tasks defined in your schedule, The Original End Date / Completion Year set for the entity. | Date | — |  | `facility.ActualStartDate · TEXT` |  |
| `BaselineEndDate` | Baseline End date | The baseline end date for the entity utilizing the schedules. If there is a milestone timeline the system uses the max end date from all non-operating tasks, otherwise it uses the max end date from the schedule. | Date | Global |  | `facility.BaselineEndDate · TEXT` |  |
| `BaselineStartDate` | Baseline Start Date | Get the baseline start date for the entity utilizing the schedule if it exists. If there are no tasks defined yet, this field will return the original start date and year set for the entity. | Date | Global |  | `facility.BaselineStartDate · TEXT` |  |
| `ClientScheduleLastReviewedDate` | Last Updated Date | This field displays the last updated date. | Date | — |  | `facility.ClientScheduleLastReviewedDate · TEXT` |  |
| `CloseDate` | Close Date | Enter the close date in this field. | Date | Global |  | `facility.CloseDate · TEXT` |  |
| `ConstructionDate` | Construction Date | Enter the construction date in this field. | Date | Global |  | `facility.ConstructionDate · TEXT` |  |
| `ExpectedEndDate` | Original Delivery Qtr/Yr | The original end date is calculated using the projected / actual end date of the task associated with the latest completed milestone whose phase is not Operations. | Date | Global |  | `facility.ExpectedEndDate · TEXT` |  |
| `OpenDate` | Open Date | Enter the open date in this field. | Date | Global |  | `facility.OpenDate · TEXT` |  |
| `OriginalEndDate` | Baseline End Date | The baseline end date of a schedule task on the entity. | Date | — |  | `facility.OriginalEndDate · TEXT` |  |
| `OriginalStartDate` | Baseline Start Date | The baseline start date of a schedule task on the entity. | Date | — |  | `facility.OriginalStartDate · TEXT` |  |
| `RemodelDate` | Remodel Date | Enter the remodel date in this field. | Date | Global |  | `facility.RemodelDate · TEXT` |  |
| `SlotEndDate` | RE Planner Open Date | The planned open date of the entity as set in the RE Planner. | Date | Global |  | `facility.SlotEndDate · TEXT` |  |

### Flags (3)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Inactive` | Is Inactive? | If selected, this check box indicates the entity is inactive. | Boolean | Global | yes | `facility.Inactive · TEXT` |  |
| `IsDead` | Is Dead? | If selected, this check box indicates the entity is dead. | Boolean | Global | yes | `facility.IsDead · TEXT` |  |
| `UseLocationAddress` | Use Location Address | Select this check box to use the address of the location associated with this facility. | Boolean | Global | yes | `facility.UseLocationAddress · TEXT` |  |

### Text & notes (58)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BaseProvider` | System of Record | This field is used to fetch a record value from another Accruent software. | Text | — |  | `facility.BaseProvider · TEXT` |  |
| `City` |  | The city associated with this record. | Text | Global |  | `facility.City · TEXT` |  |
| `CityStateProvinceCountry` | City, State | The city and state / province. If there is no state / province, the field returns only the city. If there is no city, this field returns only the state / province. | Text | — |  | `facility.CityStateProvinceCountry · TEXT` |  |
| `ClientEntityID` | Facility ID | Enter a unique ID for the entity in this field. Remember: when uploading information to a contract using Lx's import spreadsheet functionality, the entity ID and entity name must be replicated exactly in the spreadsheet. | Text | Global |  | `facility.ClientEntityID · TEXT` |  |
| `ComparisonList` | Comparison List | When added to a page layout, this field allows for a comparison of entities from a page or subpage. | Text | — |  | `facility.ComparisonList · TEXT` |  |
| `CompletedPhaseStatus` | Completed Phase Status | The milestone timeline status of the entity. This status is updated when a milestone is completed. | Text | — |  | `facility.CompletedPhaseStatus · TEXT` |  |
| `ConstructionPhaseStatus` | Construction Phase Status | This field corresponds to the Construction phase in your Milestone Timeline. It captures the most recent status of the milestone phase. | Text | Global |  | `facility.ConstructionPhaseStatus · TEXT` |  |
| `CountryID` | Country | Select the country from this field. | Text | Global |  | `facility.CountryID · TEXT` |  |
| `CrossStreet1` | Cross Street #1 | Enter the first cross street in this field. | Text | — |  | `facility.CrossStreet1 · TEXT` |  |
| `CrossStreet2` | Cross Street #2 | Enter the second cross street in this field. | Text | — |  | `facility.CrossStreet2 · TEXT` |  |
| `CurrentMilestone` | Current Milestone | The current milestone task of your entity schedule. | Text | — |  | `facility.CurrentMilestone · TEXT` |  |
| `CurrentPhaseStatus` | Project Status | The project status set by the milestone timeline. This value is driven by your entity schedule. | Text | Global |  | `facility.CurrentPhaseStatus · TEXT` |  |
| `DefinedField1` | Defined Field #1 | This field is a reserved space for client fields. | Text | Global |  | `facility.DefinedField1 · TEXT` |  |
| `DefinedField2` | Defined Field #2 | This field is a reserved space for client fields. | Text | Global |  | `facility.DefinedField2 · TEXT` |  |
| `DesignPhaseStatus` | Design Phase Status | This field corresponds to the Design phase in your Milestone Timeline. It captures the most recent status of the milestone phase. | Text | Global |  | `facility.DesignPhaseStatus · TEXT` |  |
| `EntityEmail` | Entity Email | The entity's email address that is created when the Email into Lx functionality is enabled. | Text | — |  | `facility.EntityEmail · TEXT` |  |
| `EntityPhoto` | Entity Photo | This is a generic field. When you add this field to a page layout, you can use it to add a photo to the layout. | Text | Global |  | `facility.EntityPhoto · TEXT` |  |
| `FacilityName` | Facility Name | Enter the facility name in this field. | Text | Global | yes | `facility.FacilityName · TEXT` |  |
| `FinancialModel` | Financial Model | When added to a page layout, this field appears as a button that generates an Excel Financial Model spreadsheet. If you have questions about this functionality, contact your Accruent representative. | Text | — |  | `facility.FinancialModel · TEXT` |  |
| `FirmID` | Firm ID | The record's Firm ID. | Text | — | yes | `facility.FirmID · TEXT` |  |
| `Firm_SalesReportLogo` | Sales Report Logo |  | Text | — |  | `facility.Firm_SalesReportLogo · TEXT` |  |
| `Firm_SalesReportLogoMadewell` |  |  | Text | — |  |  |  |
| `Firm_SalesReportSignature` | Sales Report Signature |  | Text | — |  | `facility.Firm_SalesReportSignature · TEXT` |  |
| `Firm_SalesReportSignatureName` | Sales Report Signature Name |  | Text | — |  | `facility.Firm_SalesReportSignatureName · TEXT` |  |
| `Firm_SalesReportSignatureTitle` | Sales Report Signature Title |  | Text | — |  | `facility.Firm_SalesReportSignatureTitle · TEXT` |  |
| `Firm_SpaceNumber` | Space Number |  | Text | Firm |  | `facility.Firm_SpaceNumber · TEXT` |  |
| `HTMLAddress` | Full Address | The associated entity's address in HTML format. | Text | Global |  | `facility.HTMLAddress · TEXT` |  |
| `HoursOfOperation` | Hours Of Operation | Enter the hours of operation of the facility in this field. | Text | Global |  | `facility.HoursOfOperation · TEXT` |  |
| `IssuesAndAlerts` | Issues And Alerts | This field can be added to page layouts. In View mode, this field will display a table with form and workflow data, such as the work flow / form type, critical issue count, non-critical issue count, escalated count, and past due notification count. | Text | Global |  | `facility.IssuesAndAlerts · TEXT` |  |
| `MapClientRecordID` | Client Unique ID | The entity Map Client Record ID. | Text | — |  | `facility.MapClientRecordID · TEXT` |  |
| `MilestoneTimeline` | Milestone Timeline | This field generates a list of all milestones, but hides those with no values. | Text | — |  | `facility.MilestoneTimeline · TEXT` |  |
| `NextMilestone` | Next Milestone | The upcoming milestone in the milestone timeline. | Text | — |  | `facility.NextMilestone · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `facility.Notes · TEXT` |  |
| `OperatingStatus` | Operating Status | This field specifies that the facility is using the operating org chart. | Text | Global | yes | `facility.OperatingStatus · TEXT` |  |
| `OperationsPhaseStatus` | Operations Phase Status | This field corresponds to the Operations phase in your Milestone Timeline. It captures the most recent status of the milestone phase. | Text | Global |  | `facility.OperationsPhaseStatus · TEXT` |  |
| `Phone` |  | Enter the facility's phone number in this field. | Text | Global |  | `facility.Phone · TEXT` |  |
| `PossessionPhaseStatus` | Possession Phase Status | This field corresponds to the Possession phase in your Milestone Timeline. It captures the most recent status of the milestone phase. | Text | Global |  | `facility.PossessionPhaseStatus · TEXT` |  |
| `PostalCode` | Postal Code | Enter the postal code of the entity in this field. | Text | Global |  | `facility.PostalCode · TEXT` |  |
| `PotentialProjectName` | Site Name | The name of the site associated with this entity. | Text | — |  | `facility.PotentialProjectName · TEXT` |  |
| `PreviousMilestone` | Previous Milestone | The previous milestone task. | Text | — |  | `facility.PreviousMilestone · TEXT` |  |
| `ProgramName` | Portfolio/Program Name | The name of the portfolio associated with this entity. | Text | — |  | `facility.ProgramName · TEXT` |  |
| `ProjectDescription` | Description | Write a description of the record. | Text | Global |  | `facility.ProjectDescription · TEXT` |  |
| `ProjectEntityName` | Name | The entity name. | Text | — | yes | `facility.ProjectEntityName · TEXT` |  |
| `ProjectEntityTypeName` | Entity Type | The entity type. | Text | — |  | `facility.ProjectEntityTypeName · TEXT` |  |
| `ProjectName` | Project Name | The name of the project associated with the record. | Text | — |  | `facility.ProjectName · TEXT` |  |
| `PrototypeName` | Prototype Name | The name of the prototype associated with this entity. | Text | — |  | `facility.PrototypeName · TEXT` |  |
| `RealEstatePhaseStatus` | Real Estate Phase Status | This field corresponds to the Real Estate phase in your Milestone Timeline. It captures the most recent status of the milestone phase. | Text | Global |  | `facility.RealEstatePhaseStatus · TEXT` |  |
| `RelatedEntities` | Related Facility Entities | The name of entities associated with this entity. | Text | Global |  | `facility.RelatedEntities · TEXT` |  |
| `RelocatedFrom` |  | This field is not implemented for facilities. | Text | — |  | `facility.RelocatedFrom · TEXT` |  |
| `RunReportAction` | Run Report Action | This is a generic field. When you add this field to a page layout, it will run a report. See the Run Report Action Buttons article in the Online Help to learn more. | Text | — |  | `facility.RunReportAction · TEXT` |  |
| `StreetAddress` | Street Address | The street address. | Text | Global |  | `facility.StreetAddress · TEXT` |  |
| `StreetAddress1` | Street Address #1 | The first line of the street address. | Text | Global |  | `facility.StreetAddress1 · TEXT` |  |
| `StreetAddress2` | Street Address #2 | The second line of the street address. | Text | Global |  | `facility.StreetAddress2 · TEXT` |  |
| `StreetAddress3` | Street Address #3 | The third line of the street address. | Text | Global |  | `facility.StreetAddress3 · TEXT` |  |
| `StreetAddress4` | Street Address #4 | The fourth line of the street address. | Text | Global |  | `facility.StreetAddress4 · TEXT` |  |
| `ThirdPartyWarehouse` | Third Party Warehouse | Enter the name of your third-party warehouse in this field. This field is typically used when a client has purchased materials and is storing them in a warehouse. | Text | Global |  | `facility.ThirdPartyWarehouse · TEXT` |  |
| `TimeZone` | Time Zone | Select the appropriate time zone from this field. | Text | Global |  | `facility.TimeZone · TEXT` |  |
| `TradeArea` | Trade Area | Enter the trade area in this field. | Text | Global |  | `facility.TradeArea · TEXT` |  |

### Audit & record keeping (7)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Facility ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `facility.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | — |  | `facility.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | — |  | `facility.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `facility.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `facility.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | — |  | `facility.RevNumber · TEXT` |  |
| `UUID` | Facility UUID | This field captures a unique identifier associated with your record. This identifier is used if you are using an integration with other Accruent products. | Text | Global |  | `facility.UUID · TEXT` |  |

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
