# Location

*141 fields · module: Facilities, Locations & Sites · Postgres: `location`*

A general site/location record — address and geocoding fields (Latitude, Longitude) plus percentage-based site metrics — used as a lighter-weight alternative to Facility for sites that are tracked before or without a full facility record. 66 fields (61 Global, 5 Firm) under its own Location group.

Source: `data-fields/location.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 141 |
| Fields with a vendor definition | 130 of 143 inventoried |
| Physical tables | `location` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 66 (61 global, 5 firm) |
| Physical tables | 1 |
| Referenced by | 9 keys from 9 record types |
| Points at | 13 other records |
| Tenancy position | subtype_root |
| Rules that name it | 10 |

## What to know before rebuilding this

### 10 tenant custom columns

**Observed.** This record carries 10 physical Firm_-prefixed columns — tenant custom fields are real columns, not rows in a value store, so adding one is a DDL change. That is direct evidence for database-per-tenant and against a shared schema.

### A ProjectEntity subtype root

**Derived.** One of the nine records that are themselves a kind of ProjectEntity rather than hanging off one. The discriminator is ProjectEntityTypeName, which is how a single table serves several apparent record types.

### Census and catalogue disagree

**Observed.** The object census declares 141 fields; the Data Fields catalogue lists 66. The 75-field gap is columns the platform holds but does not expose as configurable Data Fields — a rebuild that reads only the catalogue will miss them.

### 5 catalogued Firm-scope fields

**Observed.** Of 66 catalogued fields on this record, 5 are Firm scope — defined by this tenant rather than shipped by the platform. Firm-scope definitions are RGAF rows carrying IsGlobal, FirmID and IsClientExtensionField.

### Lands in location

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 130 fields carry a vendor definition

**Observed.** 130 of this record's 143 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 6 of this record's fields required; the Data Fields catalogue marks 5; 4 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

### 1 field excluded from extraction

**Observed.** Observed of the loader. The inventory marks 1 of this record's fields as not extracted to PostgreSQL, so the replication target creates no column for them. They still exist in Lx; anything reading the replica rather than the product will not see them.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [ACC-R-061](../rules/ACC-R-061.md) | the form type declares attachability as a Boolean per entity kind. For this form type, only `Portfolio` = Yes and `RE Contract` = Yes; `Capital Program`, `Prototype`, `Location`, `Parcel`, `Site`, `Project`, `Facility`, `Capital Project` an | Observed |
| [FAC-R-004](../rules/FAC-R-004.md) | Input: `Location.ProgramID`. Confidence: Observed (`Required = Yes`, `../../data-fields/location.md`). | Observed |
| [FAC-R-008](../rules/FAC-R-008.md) | Input: `ComplexID` on `Facility`, `Location`, `Parcel`, `Prototype` (all `Required = No` where exposed) and `Competitor`. Effect: Any of the four subtype roots — and a tracked competitor — may be grouped under one shared shopping-center/cam | Observed |
| [FAC-R-009](../rules/FAC-R-009.md) | Effect: `Complex`'s 45-field schema contains no FK back into `Location`/`Facility`/`Parcel`/ `Prototype`/`Program`, and no `ProjectEntityID`. It is `firm_global`, not entity-scoped. | Derived |
| [FAC-R-010](../rules/FAC-R-010.md) | Input: `Facility.UseLocationAddress` (Boolean, Required = Yes — the flag itself must always be set one way or the other). Effect: When true, the Facility is presumed to use `Location`'s address fields rather than its own `StreetAddress1..4` | Inferred |
| [FAC-R-018](../rules/FAC-R-018.md) | Input: `Ownership`, `SiteSurvey`, `LandPurchaseSummary`, `LinkLandPurchaseInspection`, `DemographicResults` carry `ProjectEntityID` and no hard-typed FK to `Facility`/`Location`/`Parcel`. Effect: In principle any of these can attach to any  | Derived |
| [FAC-R-019](../rules/FAC-R-019.md) | Input: `Prototype.LocationID`, `.ComplexID`, `.DemographicDMAID` are declared columns in `_lucernex_objects_summary.txt` but do not appear anywhere in `../../data-fields/prototype.md`'s 15-row catalog. Effect: Unlike the identical columns o | Observed |
| [PLT-R-010](../rules/PLT-R-010.md) | Every address block in the product repeats the same `StreetAddress1..4`/`City`/ `PostalCode`/`CountryID`/`JurisdictionID` shape and resolves tax rate through `Jurisdiction`, not through the country/state master directly | Derived |
| [POR-R-003](../rules/POR-R-003.md) | A user opens a `Facility`/`Location`/`Parcel`/`Prototype`/`Contract`/`CapProject`/`OpenProject`/`EquipmentContract` detail screen under a given Portfolio · `Program.<Subtype>SetupPageLayoutID` · Overrides the tenant-wide default from `Firm. | Observed |
| [POR-R-011](../rules/POR-R-011.md) | Any process needs to trace a `Facility`/`Location` back to the `PotentialProject` it originated from · (none — no such column exists) · Not possible via FK. `PotentialProject` has zero inbound edges in the 972-edge graph and zero Manage Dat | Observed |

## Fields

### Relationships (foreign keys) (11)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BudgetTemplateID` | Budget Template | If there is a budget template associated with this entity, The foreign key of the budget template. | Template ID | Global |  | `location.BudgetTemplateID · TEXT` | [BudgetTemplate](BudgetTemplate.md) |
| `ComplexID` | Complex Name | Select the complex name from this field. A complex or center is used to track information about multi-tenant structures such as shopping malls. | Complex ID | Global |  | `location.ComplexID · TEXT` | [Complex](Complex.md) |
| `DemographicDMAID` | Demographic DMA | Select your demographic market area from this field. | DMA ID | — |  | `location.DemographicDMAID · TEXT` | [DMA](DMA.md) |
| `IStateProvinceCountryID` | State | Select the state or province from this field. | Country, State, County ID | Global |  | `location.IStateProvinceCountryID · TEXT` | [StateProvinceCountry](StateProvinceCountry.md) |
| `JurisdictionID` | Jurisdiction | The county / province associated with the associated entity's address. | County ID | Global |  | `location.JurisdictionID · TEXT` | [Jurisdiction](Jurisdiction.md) |
| `OrganizationID` | Organization | Select the organization where payments should be debited from this field. | Organization ID | Global |  | `location.OrganizationID · TEXT` | [Organization](Organization.md) |
| `ProgramID` | Portfolio | Select the Portfolio that the entity belongs to from this field. | Portfolio ID | Global | yes | `location.ProgramID · TEXT` | [Program](Program.md) |
| `PrototypeID` | Prototype | Select the prototype associated with this entity from this field. | Prototype ID | — |  | `location.PrototypeID · TEXT` | [Prototype](Prototype.md) |
| `RegionID` | Region | Select the region and sub-region the location should belong to from this field. The values that appear in this field depend on the org chart of the portfolio you selected. | Region ID | Global |  | `location.RegionID · TEXT` | [Region](Region.md) |
| `RootRegionID` | Parent Region | This field sets some default membership at the creation of the entity. Its values are pulled from the organization chart. | Region ID | — |  | `location.RootRegionID · TEXT` | [Region](Region.md) |
| `SubRegionID` | Sub Region | The sub-region. | Region ID | — |  | `location.SubRegionID · TEXT` | [Region](Region.md) |

### Soft references (2)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `LinkProjectEntityContactListData` | Contact List | This field returns a list of Active and Inactive entities filtered by member security. | Contact | — |  | `location.LinkProjectEntityContactListData · TEXT` |  |
| `ManagerIDList` | Project Managers | This is a generic field that you can add to a page layout. In View mode, this field returns a list of managers assigned to the entity by the org chart and managers assigned to the entity on an ad hoc basis. In Edit mode, this field allows you to add managers to your entity. | Dropdown | — |  | `location.ManagerIDList · TEXT` |  |

### Coded values (drop-downs) (23)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeBuildingAreaUnitID` | Building Area Unit | Select the units you are using to measure your area from this field. | Dropdown (Building Area Unit Code) | Global |  | `location.CodeBuildingAreaUnitID · TEXT` | Building Area Unit Code |
| `CodeConstructionTypeID` | Construction Type | Select the construction type from this field. | Dropdown (Construction Type Code) | — |  | `location.CodeConstructionTypeID · TEXT` | Construction Type Code |
| `CodeCurrencyTypeID` | Currency Type | The Currency Type field allows you to select a currency type to be used on a record. | Dropdown (Currency Type Code) | Global |  | `location.CodeCurrencyTypeID · TEXT` | Currency Type Code |
| `CodeDealTypeID` | Deal Type | This is a generic field. It is not implemented for locations by default. | Dropdown (Deal Type Code) | — |  | `location.CodeDealTypeID · TEXT` | Deal Type Code |
| `CodeDesc_CodeMarketAreaID` | Market Potential | The description of the market of the location associated with the facility. | Dropdown (Market Area Code) | — |  | `location.CodeDesc_CodeMarketAreaID · TEXT` | Market Area Code |
| `CodeDesc_CodeProjectTypeID` | Real Estate Type | This is a generic field. It is not implemented for locations by default. | Dropdown (Project Type Code) | — |  | `location.CodeDesc_CodeProjectTypeID · TEXT` | Project Type Code |
| `CodeDistributionCenterID` | Distribution Center | Select the distribution center from which the store is receiving product from this field. | Dropdown (Distribution Center Code) | — |  | `location.CodeDistributionCenterID · TEXT` | Distribution Center Code |
| `CodeLandAreaUnitID` | Land Area Unit | Select the unit you will use for measuring your area. | Dropdown (Land Area Unit Code) | Global |  | `location.CodeLandAreaUnitID · TEXT` | Land Area Unit Code |
| `CodeLocationCategoryID` | Location Category | Select the location category from this field. Types are the third level of organization in Lx. Categories are the children of types, and the grandchildren of groups. Groups, types, and categories are used to simplify reporting. | Dropdown (Location Category Code) | Global |  | `location.CodeLocationCategoryID · TEXT` | Location Category Code |
| `CodeLocationGroupID` | Location Group | Select the location group from this field. Groups are the first level of organization in Lx. Groups are the parents of types, and the grandparents of categories. Groups, types, and categories are used to simplify reporting. | Dropdown (Location Group Code) | Global |  | `location.CodeLocationGroupID · TEXT` | Location Group Code |
| `CodeLocationStatusID` | Location Status | Select the location status from this field. | Dropdown (Location Status Code) | Global |  | `location.CodeLocationStatusID · TEXT` | Location Status Code |
| `CodeLocationTypeID` | Location Type | Select the location type from this field. Types are the second level of organization in Lx. Types are the children of groups, and the parents of categories. Groups, types, and categories are used to simplify reporting. | Dropdown (Location Type Code) | Global |  | `location.CodeLocationTypeID · TEXT` | Location Type Code |
| `CodeLocationUseID` | Location Use | Select the primary use of the location from the field. | Dropdown (Location Use Code) | Global |  | `location.CodeLocationUseID · TEXT` | Location Use Code |
| `CodeMarketAreaID` | Market Area | Select the market the location should belong to from this field. The values that appear in this field might depend on the org chart of the portfolio you selected. | Dropdown (Market Area Code) | Global |  | `location.CodeMarketAreaID · TEXT` | Market Area Code |
| `CodeMarketTypeID` | Market Type | Select the market type from this field. | Dropdown (Market Type Code) | — |  | `location.CodeMarketTypeID · TEXT` | Market Type Code |
| `CodeProjectTypeID` | Project Type | This is a generic field. It is not implemented for locations by default. | Dropdown (Project Type Code) | — |  | `location.CodeProjectTypeID · TEXT` | Project Type Code |
| `CodeSubArea1ID` | Sub Area #1 | Select the sub-area the location should belong to from this field. | Dropdown (Area Code) | Global |  | `location.CodeSubArea1ID · TEXT` | Area Code |
| `CodeSubArea2ID` | Sub Area #2 | Select the sub-area the location should belong to from this field. | Dropdown (Area Code) | Global |  | `location.CodeSubArea2ID · TEXT` | Area Code |
| `CodeSubArea3ID` | Sub Area #3 | Select the sub-area the location should belong to from this field. | Dropdown (Area Code) | Global |  | `location.CodeSubArea3ID · TEXT` | Area Code |
| `CodeSubRegion1ID` | Sub Region #1 | Select the sub-region the location should belong to from this field. | Dropdown (Region Code) | Global |  | `location.CodeSubRegion1ID · TEXT` | Region Code |
| `CodeSubRegion2ID` | Sub Region #2 | Select the sub-region the location should belong to from this field. | Dropdown (Region Code) | Global |  | `location.CodeSubRegion2ID · TEXT` | Region Code |
| `CodeSubRegion3ID` | Sub Region #3 | Select the sub-region the location should belong to from this field. | Dropdown (Region Code) | Global |  | `location.CodeSubRegion3ID · TEXT` | Region Code |
| `CurrentCodeProjectPhaseID` | Project Phase | The project phase set by the milestone timeline. This value is driven by your entity schedule. | Dropdown (Project Phase Code) | — |  | `location.CurrentCodeProjectPhaseID · TEXT` | Project Phase Code |

### Money (1)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Firm_PriorMonthAccrualTotal` |  |  | Currency | — |  |  |  |

### Rates & percentages (8)

Percentage inputs and computed rates.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `EquipContractTaxRate1` | EC Tax Rate #1 | Enter the primary tax rate you will use for this location. The value in this field will cascade down to any equipment contracts that do not have a primary tax rate. | Percentage | Global |  | `location.EquipContractTaxRate1 · TEXT` |  |
| `EquipContractTaxRate2` | EC Tax Rate #2 | Enter the secondary tax rate you will use for this location. The value in this field will cascade down to any equipment contracts that do not have a secondary tax rate. | Percentage | Global |  | `location.EquipContractTaxRate2 · TEXT` |  |
| `EquipContractTaxRate3` | EC Tax Rate #3 | Enter the third tax rate you will use for this location. The value in this field will cascade down to any equipment contracts that do not have a third tax rate. | Percentage | Global |  | `location.EquipContractTaxRate3 · TEXT` |  |
| `EquipContractTaxRate4` | EC Tax Rate #4 | Enter the fourth tax rate you will use for this location. The value in this field will cascade down to any equipment contracts that do not have a fourth tax rate. | Percentage | Global |  | `location.EquipContractTaxRate4 · TEXT` |  |
| `TaxRate1` | RE Tax Rate #1 | Enter the primary tax rate you will use for this location. The value in this field will cascade down to any real estate contracts that do not have a primary tax rate. | Percentage | Global |  | `location.TaxRate1 · TEXT` |  |
| `TaxRate2` | RE Tax Rate #2 | Enter the secondary tax rate you will use for this location. The value in this field will cascade down to any real estate contracts that do not have a secondary tax rate. | Percentage | Global |  | `location.TaxRate2 · TEXT` |  |
| `TaxRate3` | RE Tax Rate #3 | Enter the third tax rate you will use for this location. The value in this field will cascade down to any real estate contracts that do not have a third tax rate. | Percentage | Global |  | `location.TaxRate3 · TEXT` |  |
| `TaxRate4` | RE Tax Rate #4 | Enter the fourth tax rate you will use for this location. The value in this field will cascade down to any real estate contracts that do not have a fourth tax rate. | Percentage | Global |  | `location.TaxRate4 · TEXT` |  |

### Quantities (19)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActualRevenueWeeks` | Revenue Weeks | Calculates how many actual revenue weeks this entity will exist during the fiscal year. | Number | — |  | `location.ActualRevenueWeeks · TEXT` |  |
| `DBFolderSizeMB` | Storage Size (MB) | The folder size in megabytes for a given entity. | 2-Digit Number | — |  | `location.DBFolderSizeMB · TEXT` |  |
| `Depth` |  | The depth of the associated entity. | Number | — |  | `location.Depth · TEXT` |  |
| `EDGE_ASGCenterID` | ASG Center ID |  | Number | Firm |  | `location.EDGE_ASGCenterID · TEXT` |  |
| `EntityId` | Entity LxID | The Project Entity ID. | Number | — |  | `location.EntityId · TEXT` |  |
| `Frontage` |  | Enter the physical measurements of the face of the building. | Number | — |  | `location.Frontage · TEXT` |  |
| `GrossLeaseArea` | Gross Lease Area | This field is included in Test 4 of the Capital Lease Test. Enter the total area of the building. | Number | Global |  | `location.GrossLeaseArea · TEXT` |  |
| `LatitudeDegrees` | Latitude | Enter the latitude of the location in this field. This field has an impact on integrations. To learn how to automatically calculate an entity's latitude and longitude, see the Online Help. | 5-Digit Number | Global |  | `location.LatitudeDegrees · TEXT` |  |
| `LocationID` | Location RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `location.LocationID · VARCHAR(64) NOT NULL` |  |
| `LocationParcelArea` | Location Parcel Area | Enter the parcel area in acreage. | Number | Global |  | `location.LocationParcelArea · TEXT` |  |
| `LongitudeDegrees` | Longitude | Enter the longitude of the location in this field. This field has an impact on integrations. To learn how to automatically calculate an entity's latitude and longitude, see the Online Help. | 5-Digit Number | Global |  | `location.LongitudeDegrees · TEXT` |  |
| `NumberOfDocuments` | Number of Documents | The total number of documents in all folders on the entity. | Number | — |  | `location.NumberOfDocuments · TEXT` |  |
| `OpenYear` | Open Year | The year the facility opened. | Number | Global |  | `location.OpenYear · TEXT` |  |
| `OutOfDateDays` | Out Of Date Days | This field returns how many days the schedule is out of date. If the schedule hasn't been updated yet, the value of this field is 0. If the schedule has been updated, the value of the field is calculated based on the last reviewed date. | Number | Global |  | `location.OutOfDateDays · TEXT` |  |
| `ProjectEntityID` | Entity RecID | The ProjectEntityID is the Base Entity System Identifier for associated tasks, folders, documents, forms, and other records. It is assigned automatically by the system, and is not editable. | Number | — |  | `location.ProjectEntityID · TEXT` |  |
| `RentableArea` | Rentable Area | Enter the rentable area in this field. | Number | — |  | `location.RentableArea · TEXT` |  |
| `SequenceNumber` | Sequence Number | This field generates a sequence number for the record. The next record created receives the next number in the sequence. | Number | — |  | `location.SequenceNumber · TEXT` |  |
| `ThirdPartyWarehouseArea` | Third Party Warehouse Area | Enter the size of your third-party warehouse in this field. This field is typically used when a client has purchased materials and is storing them in a warehouse. | Number | Global |  | `location.ThirdPartyWarehouseArea · TEXT` |  |
| `UsableArea` | Usable Area | The usable area. | Number | — |  | `location.UsableArea · TEXT` |  |

### Dates & timestamps (9)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActualEndDate` | Actual/Forecast Delivery Date | If there is a milestone timeline, The max end date from all non-operating tasks. Otherwise, The end date for the entity utilizing the schedule. If there are no tasks defined yet, the system will return the Original End Date / Completion Year set for the entity. | Date | — |  | `location.ActualEndDate · TEXT` |  |
| `ActualStartDate` | Forecast/Actual Start Date | The start date for the schedule associated with your entity. If there are no tasks defined in your schedule, The Original End Date / Completion Year set for the entity. | Date | — |  | `location.ActualStartDate · TEXT` |  |
| `BaselineEndDate` | Baseline Delivery Date | The baseline end date for the entity utilizing the schedules. If there is a milestone timeline the system uses the max end date from all non-operating tasks, otherwise it uses the max end date from the schedule. | Date | — |  | `location.BaselineEndDate · TEXT` |  |
| `ClientScheduleLastReviewedDate` | Last Updated Date | This field displays the last updated date. | Date | — |  | `location.ClientScheduleLastReviewedDate · TEXT` |  |
| `ExpectedEndDate` | Original Delivery Date | The original end date is calculated using the projected / actual end date of the task associated with the latest completed milestone whose phase is not Operations. | Date | — |  | `location.ExpectedEndDate · TEXT` |  |
| `Firm_GrandOpeningDate` | Grand Opening Date |  | Date | Firm |  | `location.Firm_GrandOpeningDate · TEXT` |  |
| `OriginalEndDate` | Baseline End Date | The baseline end date of a schedule task on the entity. | Date | — |  | `location.OriginalEndDate · TEXT` |  |
| `OriginalStartDate` | Baseline Start Date | The baseline start date of a schedule task on the entity. | Date | — |  | `location.OriginalStartDate · TEXT` |  |
| `SlotEndDate` | RE Planner Open Date | The planned open date of the entity as set in the RE Planner. | Date | — |  | `location.SlotEndDate · TEXT` |  |

### Flags (2)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Inactive` | Is Inactive? | If selected, this check box indicates the entity is inactive. | Boolean | Global | yes | `location.Inactive · TEXT` |  |
| `IsDead` | Is Dead? | If selected, this check box indicates the entity is dead. | Boolean | — |  | `location.IsDead · TEXT` |  |

### Text & notes (58)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AccountingNumber` | Accounting Number | Enter your accounting reference number in this field. | Text | Global |  | `location.AccountingNumber · TEXT` |  |
| `BaseProvider` | System of Record | This field is used to fetch a record value from another Accruent software. | Text | — |  | `location.BaseProvider · TEXT` |  |
| `City` |  | The city associated with this record. | Text | Global |  | `location.City · TEXT` |  |
| `CityStateProvinceCountry` | City, State | The city and state / province. If there is no state / province, the field returns only the city. If there is no city, this field returns only the state / province. | Text | — |  | `location.CityStateProvinceCountry · TEXT` |  |
| `ClientEntityID` | Location ID | Enter a unique ID for the entity in this field. Remember: when uploading information to a contract using Lx's import spreadsheet functionality, the entity ID and entity name must be replicated exactly in the spreadsheet. | Text | Global |  | `location.ClientEntityID · TEXT` |  |
| `ComparisonList` | Comparison List | When added to a page layout, this field allows for a comparison of entities from a page or subpage. | Text | — |  | `location.ComparisonList · TEXT` |  |
| `CompletedPhaseStatus` | Completed Phase Status | The milestone timeline status of the entity. This status is updated when a milestone is completed. | Text | — |  | `location.CompletedPhaseStatus · TEXT` |  |
| `ConstructionPhaseStatus` | Construction Phase Status | This field corresponds to the Construction phase in your Milestone Timeline. It captures the most recent status of the milestone phase. | Text | — |  | `location.ConstructionPhaseStatus · TEXT` |  |
| `CountryID` | Country | Select the country from this field. | Text | Global |  | `location.CountryID · TEXT` |  |
| `CrossStreet1` | Cross Street #1 | Enter the first cross street in this field. | Text | Global |  | `location.CrossStreet1 · TEXT` |  |
| `CrossStreet2` | Cross Street #2 | Enter the second cross street in this field. | Text | Global |  | `location.CrossStreet2 · TEXT` |  |
| `CurrentMilestone` | Current Milestone | The current milestone task of your entity schedule. | Text | — |  | `location.CurrentMilestone · TEXT` |  |
| `CurrentPhaseStatus` | Project Status | The project status set by the milestone timeline. This value is driven by your entity schedule. | Text | — |  | `location.CurrentPhaseStatus · TEXT` |  |
| `DesignPhaseStatus` | Design Phase Status | This field corresponds to the Design phase in your Milestone Timeline. It captures the most recent status of the milestone phase. | Text | — |  | `location.DesignPhaseStatus · TEXT` |  |
| `EntityEmail` | Entity Email | The entity's email address that is created when the Email into Lx functionality is enabled. | Text | — |  | `location.EntityEmail · TEXT` |  |
| `EntityPhoto` | Entity Photo | This is a generic field. When you add this field to a page layout, you can use it to add a photo to the layout. | Text | — |  | `location.EntityPhoto · TEXT` |  |
| `FacilityName` | Facility Name | The name of the facility associated with this entity. | Text | — |  | `location.FacilityName · TEXT` |  |
| `FinancialModel` | Financial Model | When added to a page layout, this field appears as a button that generates an Excel Financial Model spreadsheet. If you have questions about this functionality, contact your Accruent representative. | Text | — |  | `location.FinancialModel · TEXT` |  |
| `FirmID` | Firm ID | The record's Firm ID. | Text | — | yes | `location.FirmID · TEXT` |  |
| `Firm_CenterName` | Center Name |  | Text | Firm |  | `location.Firm_CenterName · TEXT` |  |
| `Firm_County` | County |  | Text | Firm |  | `location.Firm_County · TEXT` |  |
| `Firm_Developer` | Developer |  | Text | Firm |  | `location.Firm_Developer · TEXT` |  |
| `Firm_SalesReportLogo` | Sales Report Logo |  | Text | — |  | `location.Firm_SalesReportLogo · TEXT` |  |
| `Firm_SalesReportLogoMadewell` |  |  | Text | — |  |  |  |
| `Firm_SalesReportSignature` | Sales Report Signature |  | Text | — |  | `location.Firm_SalesReportSignature · TEXT` |  |
| `Firm_SalesReportSignatureName` | Sales Report Signature Name |  | Text | — |  | `location.Firm_SalesReportSignatureName · TEXT` |  |
| `Firm_SalesReportSignatureTitle` | Sales Report Signature Title |  | Text | — |  | `location.Firm_SalesReportSignatureTitle · TEXT` |  |
| `HTMLAddress` | Full Address | The associated entity's address in HTML format. | Text | Global |  | `location.HTMLAddress · TEXT` |  |
| `IssuesAndAlerts` | Issues And Alerts | This field can be added to page layouts. In View mode, this field will display a table with form and workflow data, such as the work flow / form type, critical issue count, non-critical issue count, escalated count, and past due notification count. | Text | — |  | `location.IssuesAndAlerts · TEXT` |  |
| `LocationName` | Location Name | Enter the name of the location in this field. | Text | Global | yes | `location.LocationName · TEXT` |  |
| `MapClientRecordID` | Client Unique ID | The entity Map Client Record ID. | Text | — |  | `location.MapClientRecordID · TEXT` |  |
| `MilestoneTimeline` | Milestone Timeline | This field generates a list of all milestones, but hides those with no values. | Text | — |  | `location.MilestoneTimeline · TEXT` |  |
| `NextMilestone` | Next Milestone | The upcoming milestone in the milestone timeline. | Text | — |  | `location.NextMilestone · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `location.Notes · TEXT` |  |
| `OperationsPhaseStatus` | Operations Phase Status | This field corresponds to the Operations phase in your Milestone Timeline. It captures the most recent status of the milestone phase. | Text | — |  | `location.OperationsPhaseStatus · TEXT` |  |
| `Phone` |  | This field can be used to store a phone number. | Text | — |  | `location.Phone · TEXT` |  |
| `PossessionPhaseStatus` | Possession Phase Status | This field corresponds to the Possession phase in your Milestone Timeline. It captures the most recent status of the milestone phase. | Text | — |  | `location.PossessionPhaseStatus · TEXT` |  |
| `PostalCode` | Postal Code | Enter the postal code of the entity in this field. | Text | Global |  | `location.PostalCode · TEXT` |  |
| `PotentialProjectName` | Site Name | The name of the site associated with this entity. | Text | — |  | `location.PotentialProjectName · TEXT` |  |
| `PreviousMilestone` | Previous Milestone | The previous milestone task. | Text | — |  | `location.PreviousMilestone · TEXT` |  |
| `ProgramName` | Portfolio/Program Name | The name of the portfolio associated with this entity. | Text | — |  | `location.ProgramName · TEXT` |  |
| `ProjectDescription` | Description | Write a description of the record. | Text | Global |  | `location.ProjectDescription · TEXT` |  |
| `ProjectEntityName` | Name | The entity name. | Text | — | yes | `location.ProjectEntityName · TEXT` |  |
| `ProjectEntityTypeName` | Entity Type | The entity type. | Text | — |  | `location.ProjectEntityTypeName · TEXT` |  |
| `ProjectName` | Project Name | The name of the project associated with the record. | Text | — |  | `location.ProjectName · TEXT` |  |
| `PrototypeName` | Prototype Name | The name of the prototype associated with this entity. | Text | — |  | `location.PrototypeName · TEXT` |  |
| `RealEstatePhaseStatus` | Real Estate Phase Status | This field corresponds to the Real Estate phase in your Milestone Timeline. It captures the most recent status of the milestone phase. | Text | — |  | `location.RealEstatePhaseStatus · TEXT` |  |
| `RelatedEntities` | Related Entities | The name of entities associated with this entity. | Text | — |  | `location.RelatedEntities · TEXT` |  |
| `RelocatedFrom` |  | Enter where you relocated from in this field. | Text | — |  | `location.RelocatedFrom · TEXT` |  |
| `RunReportAction` | Run Report Action | This is a generic field. When you add this field to a page layout, it will run a report. See the Run Report Action Buttons article in the Online Help to learn more. | Text | — |  | `location.RunReportAction · TEXT` |  |
| `StreetAddress` | Street Address | The street address. | Text | — |  | `location.StreetAddress · TEXT` |  |
| `StreetAddress1` | Street Address #1 | The first line of the street address. | Text | Global |  | `location.StreetAddress1 · TEXT` |  |
| `StreetAddress2` | Street Address #2 | The second line of the street address. | Text | Global |  | `location.StreetAddress2 · TEXT` |  |
| `StreetAddress3` | Street Address #3 | The third line of the street address. | Text | Global |  | `location.StreetAddress3 · TEXT` |  |
| `StreetAddress4` | Street Address #4 | The fourth line of the street address. | Text | Global |  | `location.StreetAddress4 · TEXT` |  |
| `ThirdPartyWarehouse` | Third Party Warehouse | Enter the name of your third-party warehouse in this field. This field is typically used when a client has purchased materials and is storing them in a warehouse. | Text | Global |  | `location.ThirdPartyWarehouse · TEXT` |  |
| `TimeZone` | Time Zone | Select the appropriate time zone from this field. | Text | Global |  | `location.TimeZone · TEXT` |  |
| `TradeArea` | Trade Area | The trade area. | Text | — |  | `location.TradeArea · TEXT` |  |

### Audit & record keeping (7)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Location ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `location.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | — |  | `location.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | — |  | `location.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `location.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `location.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | — |  | `location.RevNumber · TEXT` |  |
| `UUID` | Location UUID | This field captures a unique identifier associated with your record. This identifier is used if you are using an integration with other Accruent products. | Text | Global |  | `location.UUID · TEXT` |  |

### Other (1)

Everything that did not fall into a named group.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `GrossArea` | Gross Acreage | Enter the gross area in this field. | Acreage | — |  | `location.GrossArea · TEXT` |  |

## What points here (9 keys)

| Record type | Via column |
|---|---|
| [BudgetOptionTemplate](BudgetOptionTemplate.md) | `LocationID` |
| [Contract](Contract.md) | `LocationID` |
| [Facility](Facility.md) | `LocationID` |
| [Parcel](Parcel.md) | `LocationID` |
| [PotentialProject](PotentialProject.md) | `LocationID` |
| [Program](Program.md) | `LocationID` |
| [Project](Project.md) | `LocationID` |
| [ProjectEntity](ProjectEntity.md) | `LocationID` |
| [Prototype](Prototype.md) | `LocationID` |
