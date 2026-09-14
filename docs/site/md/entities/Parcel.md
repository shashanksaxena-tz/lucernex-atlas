# Parcel

*154 fields · module: Facilities, Locations & Sites · Postgres: `parcel`*

The land-parcel record, distinct from Facility (building) and Location (site) — address fields plus parcel-specific attributes like Demographic DMA linkage, used primarily for ground-lease and land-purchase scenarios and as the anchor for the large PropertyTax* family (Assessment, Bill, Summary, Appeal, ParcelAccess). 74 Global fields under its own Parcel group.

Source: `data-fields/parcel.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 154 |
| Fields with a vendor definition | 148 of 155 inventoried |
| Physical tables | `parcel` |
| Replication database | `lxr_drp_bbw` |
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

### Lands in parcel

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 148 fields carry a vendor definition

**Observed.** 148 of this record's 155 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 8 of this record's fields required; the Data Fields catalogue marks 6; 5 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. Field is excluded from the loader field set for this object, so no column is created That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

### 1 field excluded from extraction

**Observed.** Observed of the loader. The inventory marks 1 of this record's fields as not extracted to PostgreSQL, so the replication target creates no column for them. They still exist in Lx; anything reading the replica rather than the product will not see them.

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

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BudgetTemplateID` | Budget Template ID | If there is a budget template associated with this entity, The foreign key of the budget template. | Template ID | — |  | `parcel.BudgetTemplateID · TEXT` | [BudgetTemplate](BudgetTemplate.md) |
| `ComplexID` | Complex Name | The ID of the complex associated with the location where the competitor is located. | Complex ID | Global |  | `parcel.ComplexID · TEXT` | [Complex](Complex.md) |
| `ContractID` | Contract | Select the contract this parcel is associated with from this field. This field must be populated if you want to generate tax payments from the Parcel module. | Contract ID | Global |  | `parcel.ContractID · TEXT` | [Contract](Contract.md) |
| `DemographicDMAID` | Demographic DMA | Select your demographic market area from this field. | DMA ID | Global |  | `parcel.DemographicDMAID · TEXT` | [DMA](DMA.md) |
| `FacilityID` | Facility | Select the facility this parcel is associated with from this field. | Facility ID | Global |  | `parcel.FacilityID · TEXT` | [Facility](Facility.md) |
| `IStateProvinceCountryID` | State | Select the state or province from this field. | Country, State, County ID | Global |  | `parcel.IStateProvinceCountryID · TEXT` | [StateProvinceCountry](StateProvinceCountry.md) |
| `JurisdictionID` | Jurisdiction | The county / province associated with the associated entity's address. | County ID | Global |  | `parcel.JurisdictionID · TEXT` | [Jurisdiction](Jurisdiction.md) |
| `LocationID` | Location | Select the location that your entity will be associated with from this field. | Location ID | Global | yes | `parcel.LocationID · TEXT` | [Location](Location.md) |
| `MasterParcelID` | Master Parcel | If this parcel is listed on a consolidated tax bill that contains multiple parcels, select the master parcel from this field. The master parcel is the parent record where you will track your single tax bill. You should still have other parcel records for each individual parcel, but you will not add tax bill records to those parcels. If you receive separate tax bills for each parcel, ignore this field. | Parcel ID | Global |  | `parcel.MasterParcelID · TEXT` | [Parcel](Parcel.md) |
| `OrganizationID` | Organization | Select the organization where payments should be debited from this field. | Organization ID | Global |  | `parcel.OrganizationID · TEXT` | [Organization](Organization.md) |
| `ProgramID` | Portfolio | Select the Portfolio that the entity belongs to from this field. | Portfolio ID | Global | yes | `parcel.ProgramID · TEXT` | [Program](Program.md) |
| `PrototypeID` | Prototype | Select the prototype associated with this entity from this field. | Prototype ID | — |  | `parcel.PrototypeID · TEXT` | [Prototype](Prototype.md) |
| `RegionID` | Region | The region and sub-region of the associated location record. | Region ID | — |  | `parcel.RegionID · TEXT` | [Region](Region.md) |
| `RootRegionID` | Parent Region | This field sets some default membership at the creation of the entity. Its values are pulled from the organization chart. | Region ID | — |  | `parcel.RootRegionID · TEXT` | [Region](Region.md) |
| `SubRegionID` | Sub Region | The sub-region. | Region ID | — |  | `parcel.SubRegionID · TEXT` | [Region](Region.md) |
| `TaxJurisdictionID` | Tax Jurisdiction | Select the tax jurisdiction from this field. The value in this field is determined by the location of the parcel. | County ID | Global |  | `parcel.TaxJurisdictionID · TEXT` | [Jurisdiction](Jurisdiction.md) |

### Soft references (2)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `LinkProjectEntityContactListData` | Contact List | This field returns a list of Active and Inactive entities filtered by member security. | Contact | — |  | `parcel.LinkProjectEntityContactListData · TEXT` |  |
| `ManagerIDList` | Project Managers | This is a generic field that you can add to a page layout. In View mode, this field returns a list of managers assigned to the entity by the org chart and managers assigned to the entity on an ad hoc basis. In Edit mode, this field allows you to add managers to your entity. | Dropdown | — |  | `parcel.ManagerIDList · TEXT` |  |

### Coded values (drop-downs) (18)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeBuildingAreaUnitID` | Building Area Unit | Select the units you are using to measure your area from this field. | Dropdown (Building Area Unit Code) | — |  | `parcel.CodeBuildingAreaUnitID · TEXT` | Building Area Unit Code |
| `CodeConstructionTypeID` | Construction Type | The construction type of the site associated with this parcel. | Dropdown (Construction Type Code) | — |  | `parcel.CodeConstructionTypeID · TEXT` | Construction Type Code |
| `CodeCurrencyTypeID` | Currency Type | The Currency Type field allows you to select a currency type to be used on a record. | Dropdown (Currency Type Code) | Global |  | `parcel.CodeCurrencyTypeID · TEXT` | Currency Type Code |
| `CodeDealTypeID` | Deal Type | The deal type of the site associated with this parcel. | Dropdown (Deal Type Code) | — |  | `parcel.CodeDealTypeID · TEXT` | Deal Type Code |
| `CodeDesc_CodeMarketAreaID` | Market Potential | The description of the market that the location associated with this parcel record belongs to. | Dropdown (Market Area Code) | — |  | `parcel.CodeDesc_CodeMarketAreaID · TEXT` | Market Area Code |
| `CodeDesc_CodeProjectTypeID` | Real Estate Type | This is a generic field. It is not implemented for parcels by default. | Dropdown (Project Type Code) | — |  | `parcel.CodeDesc_CodeProjectTypeID · TEXT` | Project Type Code |
| `CodeDistributionCenterID` | Distribution Center | Select the distribution center from which the store is receiving product from this field. | Dropdown (Distribution Center Code) | — |  | `parcel.CodeDistributionCenterID · TEXT` | Distribution Center Code |
| `CodeLandAreaUnitID` | Land Area Unit | Select the unit you will use for measuring your area. | Dropdown (Land Area Unit Code) | Global |  | `parcel.CodeLandAreaUnitID · TEXT` | Land Area Unit Code |
| `CodeMarketAreaID` | Market Area | The market that the location associated with this parcel record belongs to. | Dropdown (Market Area Code) | — |  | `parcel.CodeMarketAreaID · TEXT` | Market Area Code |
| `CodeMarketTypeID` | Market Type | The market of the location associated with the parcel. | Dropdown (Market Type Code) | — |  | `parcel.CodeMarketTypeID · TEXT` | Market Type Code |
| `CodeParcelCategoryID` | Parcel Category | Select the parcel category from this field. | Dropdown (Parcel Category Code) | Global |  | `parcel.CodeParcelCategoryID · TEXT` | Parcel Category Code |
| `CodeParcelGroupID` | Parcel Group | Select the parcel group from this field. | Dropdown (Parcel Group Code) | Global |  | `parcel.CodeParcelGroupID · TEXT` | Parcel Group Code |
| `CodeParcelStatusID` | Parcel Status | Select the status of the parcel from this field. | Dropdown (Parcel Status Code) | Global |  | `parcel.CodeParcelStatusID · TEXT` | Parcel Status Code |
| `CodeParcelTypeID` | Parcel Type | Select the parcel type from this field. | Dropdown (Parcel Type Code) | Global |  | `parcel.CodeParcelTypeID · TEXT` | Parcel Type Code |
| `CodeParcelUseID` | Parcel Use | Select the purpose of the parcel from this field. | Dropdown (Parcel Use Code) | Global |  | `parcel.CodeParcelUseID · TEXT` | Parcel Use Code |
| `CodeProjectTypeID` | Project Type | This is a generic field. It is not implemented for parcels by default. | Dropdown (Project Type Code) | — |  | `parcel.CodeProjectTypeID · TEXT` | Project Type Code |
| `CodeTaxResponsibilityID` | Tax Responsibility | Select the party responsible for the taxes on this parcel from this field. Common values in this field are "landlord" and "tenant". | Dropdown (Responsible Party) | Global |  | `parcel.CodeTaxResponsibilityID · TEXT` | Responsible Party |
| `CurrentCodeProjectPhaseID` | Project Phase | This is a default field. This field is not implemented for parcels. | Dropdown (Project Phase Code) | — |  | `parcel.CurrentCodeProjectPhaseID · TEXT` | Project Phase Code |

### Money (11)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Firm_PriorMonthAccrualTotal` |  |  | Currency | — |  |  |  |
| `ImprovementsAsessedAmount` | Improvements Assessed Amount | The Parcel Tax Assessment section was created before the Property Taxes sub-module was created. You may use this section to log assessment data, but understand that this section does not create or store individual tax assessment records. To create and store individual tax assessment records, see the Property Taxes sub-module. | Currency | Global |  | `parcel.ImprovementsAsessedAmount · TEXT` |  |
| `ImprovementsValueAmount` | Improvements Value Amount | The Parcel Tax Assessment section was created before the Property Taxes sub-module was created. You may use this section to log assessment data, but understand that this section does not create or store individual tax assessment records. To create and store individual tax assessment records, see the Property Taxes sub-module. | Currency | Global |  | `parcel.ImprovementsValueAmount · TEXT` |  |
| `LandAssessedAmount` | Land Assessed Amount | The Parcel Tax Assessment section was created before the Property Taxes sub-module was created. You may use this section to log assessment data, but understand that this section does not create or store individual tax assessment records. To create and store individual tax assessment records, see the Property Taxes sub-module. | Currency | Global |  | `parcel.LandAssessedAmount · TEXT` |  |
| `LandValueAmount` | Land Value Amount | The Parcel Tax Assessment section was created before the Property Taxes sub-module was created. You may use this section to log assessment data, but understand that this section does not create or store individual tax assessment records. To create and store individual tax assessment records, see the Property Taxes sub-module. | Currency | Global |  | `parcel.LandValueAmount · TEXT` |  |
| `OtherAssessedAmount` | Other Assessed Amount | The Parcel Tax Assessment section was created before the Property Taxes sub-module was created. You may use this section to log assessment data, but understand that this section does not create or store individual tax assessment records. To create and store individual tax assessment records, see the Property Taxes sub-module. | Currency | Global |  | `parcel.OtherAssessedAmount · TEXT` |  |
| `OtherValueAmount` | Other Value Amount | The Parcel Tax Assessment section was created before the Property Taxes sub-module was created. You may use this section to log assessment data, but understand that this section does not create or store individual tax assessment records. To create and store individual tax assessment records, see the Property Taxes sub-module. | Currency | Global |  | `parcel.OtherValueAmount · TEXT` |  |
| `PrimaryAssessedAmount` | Primary Assessed Amount | The Parcel Tax Assessment section was created before the Property Taxes sub-module was created. You may use this section to log assessment data, but understand that this section does not create or store individual tax assessment records. To create and store individual tax assessment records, see the Property Taxes sub-module. | Currency | Global |  | `parcel.PrimaryAssessedAmount · TEXT` |  |
| `PrimaryValueAmount` | Primary Value Amount | The Parcel Tax Assessment section was created before the Property Taxes sub-module was created. You may use this section to log assessment data, but understand that this section does not create or store individual tax assessment records. To create and store individual tax assessment records, see the Property Taxes sub-module. | Currency | Global |  | `parcel.PrimaryValueAmount · TEXT` |  |
| `SecondaryAssessedAmount` | Secondary Assessed Amount | The Parcel Tax Assessment section was created before the Property Taxes sub-module was created. You may use this section to log assessment data, but understand that this section does not create or store individual tax assessment records. To create and store individual tax assessment records, see the Property Taxes sub-module. | Currency | Global |  | `parcel.SecondaryAssessedAmount · TEXT` |  |
| `SecondaryValueAmount` | Secondary Value Amount | The Parcel Tax Assessment section was created before the Property Taxes sub-module was created. You may use this section to log assessment data, but understand that this section does not create or store individual tax assessment records. To create and store individual tax assessment records, see the Property Taxes sub-module. | Currency | Global |  | `parcel.SecondaryValueAmount · TEXT` |  |

### Quantities (16)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActualRevenueWeeks` | Revenue Weeks | This is a default field that is not used for parcels. | Number | — |  | `parcel.ActualRevenueWeeks · TEXT` |  |
| `DBFolderSizeMB` | Storage Size (MB) | The folder size in megabytes for a given entity. | 2-Digit Number | — |  | `parcel.DBFolderSizeMB · TEXT` |  |
| `Depth` |  | The depth of the associated entity. | Number | — |  | `parcel.Depth · TEXT` |  |
| `EntityId` | Entity LxID | The Project Entity ID. | Number | — |  | `parcel.EntityId · TEXT` |  |
| `Frontage` |  | Enter the physical measurements of the face of the building. | Number | — |  | `parcel.Frontage · TEXT` |  |
| `LatitudeDegrees` | Latitude | Enter the latitude of the parcel in this field. To learn how to automatically calculate an entity's latitude and longitude, see the Online Help. | 5-Digit Number | — |  | `parcel.LatitudeDegrees · TEXT` |  |
| `LongitudeDegrees` | Longitude | Enter the longitude of the parcel in this field. To learn how to automatically calculate an entity's latitude and longitude, see the Online Help. | 5-Digit Number | — |  | `parcel.LongitudeDegrees · TEXT` |  |
| `NumberOfDocuments` | Number of Documents | The total number of documents in all folders on the entity. | Number | — |  | `parcel.NumberOfDocuments · TEXT` |  |
| `OpenYear` | Open Year | The year the facility opened. | Number | Global |  | `parcel.OpenYear · TEXT` |  |
| `OutOfDateDays` | Out Of Date Days | This field returns how many days the schedule is out of date. If the schedule hasn't been updated yet, the value of this field is 0. If the schedule has been updated, the value of the field is calculated based on the last reviewed date. | Number | Global |  | `parcel.OutOfDateDays · TEXT` |  |
| `ParcelArea` | Parcel Area | Enter the total area of the parcel in this field. | Number | Global |  | `parcel.ParcelArea · TEXT` |  |
| `ParcelID` | Parcel RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `parcel.ParcelID · VARCHAR(64) NOT NULL` |  |
| `ProjectEntityID` | Entity RecID | The ProjectEntityID is the Base Entity System Identifier for associated tasks, folders, documents, forms, and other records. It is assigned automatically by the system, and is not editable. | Number | — |  | `parcel.ProjectEntityID · TEXT` |  |
| `RentableArea` | Rentable Area | Enter the rentable area in this field. | Number | — |  | `parcel.RentableArea · TEXT` |  |
| `SequenceNumber` | Sequence Number | This field generates a sequence number for the record. The next record created receives the next number in the sequence. | Number | — |  | `parcel.SequenceNumber · TEXT` |  |
| `UsableArea` | Usable Area | The usable area. | Number | — |  | `parcel.UsableArea · TEXT` |  |

### Dates & timestamps (14)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AcquiredDate` | Acquired Date | Enter the date you acquired the parcel in this field. The acquired date is similar to a possession date. | Date | Global |  | `parcel.AcquiredDate · TEXT` |  |
| `ActualEndDate` | Actual/Forecast Delivery Date | If there is a milestone timeline, The max end date from all non-operating tasks. Otherwise, The end date for the entity utilizing the schedule. If there are no tasks defined yet, the system will return the Original End Date / Completion Year set for the entity. | Date | — |  | `parcel.ActualEndDate · TEXT` |  |
| `ActualStartDate` | Forecast/Actual Start Date | The start date for the schedule associated with your entity. If there are no tasks defined in your schedule, The Original End Date / Completion Year set for the entity. | Date | — |  | `parcel.ActualStartDate · TEXT` |  |
| `BaselineEndDate` | Baseline Delivery Date | The baseline end date for the entity utilizing the schedules. If there is a milestone timeline the system uses the max end date from all non-operating tasks, otherwise it uses the max end date from the schedule. | Date | — |  | `parcel.BaselineEndDate · TEXT` |  |
| `ClientScheduleLastReviewedDate` | Last Updated Date | This field displays the last updated date. | Date | — |  | `parcel.ClientScheduleLastReviewedDate · TEXT` |  |
| `ExpectedEndDate` | Expected End Date | This is a default field that is not used for parcels. | Date | Global |  | `parcel.ExpectedEndDate · TEXT` |  |
| `OriginalEndDate` | Baseline End Date | The baseline end date of a schedule task on the entity. | Date | — |  | `parcel.OriginalEndDate · TEXT` |  |
| `OriginalStartDate` | Baseline Start Date | The baseline start date of a schedule task on the entity. | Date | — |  | `parcel.OriginalStartDate · TEXT` |  |
| `PurchaseDate` | Purchase Date | Enter the purchase date of the parcel in this field. | Date | Global |  | `parcel.PurchaseDate · TEXT` |  |
| `SlotEndDate` | RE Planner Open Date | This is a default field that is not used for parcels. | Date | — |  | `parcel.SlotEndDate · TEXT` |  |
| `SourceReferenceDate` | Source Reference Date | The Parcel Tax Assessment section was created before the Property Taxes sub-module was created. You may use this section to log assessment data, but understand that this section does not create or store individual tax assessment records. To create and store individual tax assessment records, see the Property Taxes sub-module. | Date | Global |  | `parcel.SourceReferenceDate · TEXT` |  |
| `SurveyDate` | Survey Date | Enter the survey date in this field. Note: The Parcel Tax Assessment section was created before the Property Taxes sub-module was created. You may use this section to log assessment data, but understand that this section does not create or store individual tax assessment records. To create and store individual tax assessment records, see the Property Taxes sub-module. | Date | Global |  | `parcel.SurveyDate · TEXT` |  |
| `TaxBeginPeriod` | Tax Begin Period | Enter the begin date of the tax period in this field. | Date | Global |  | `parcel.TaxBeginPeriod · TEXT` |  |
| `TaxEndPeriod` | Tax End Period | Enter the end date of the tax period in this field. | Date | Global |  | `parcel.TaxEndPeriod · TEXT` |  |

### Flags (5)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `HasImprovements` | Has Improvements? | If this parcel has improvements such as a building select this check box. | Boolean | Global |  | `parcel.HasImprovements · TEXT` |  |
| `Inactive` | Is Inactive? | If selected, this check box indicates the entity is inactive. | Boolean | — | yes | `parcel.Inactive · TEXT` |  |
| `IsDead` | Is Dead? | If selected, this check box indicates the entity is dead. | Boolean | — |  | `parcel.IsDead · TEXT` |  |
| `IsTaxExempt` | Is Tax Exempt? | If this parcel is tax exempt, select this check box. | Boolean | Global |  | `parcel.IsTaxExempt · TEXT` |  |
| `UseLocationAddress` | Use Location Address? | If this check box is selected, the parcel record will use the address of the associated location record. | Boolean | Global | yes | `parcel.UseLocationAddress · TEXT` |  |

### Text & notes (64)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BaseProvider` | System of Record | This field is used to fetch a record value from another Accruent software. | Text | — |  | `parcel.BaseProvider · TEXT` |  |
| `Block` |  | If your parcel has a block identifier this is commonly for parcels in urban areas enter the block identifier in this field. | Text | Global |  | `parcel.Block · TEXT` |  |
| `City` |  | The city associated with this record. | Text | Global |  | `parcel.City · TEXT` |  |
| `CityStateProvinceCountry` | City, State | The city and state / province. If there is no state / province, the field returns only the city. If there is no city, this field returns only the state / province. | Text | — |  | `parcel.CityStateProvinceCountry · TEXT` |  |
| `ClientEntityID` | Parcel ID | Enter a unique ID for the entity in this field. Remember: when uploading information to a contract using Lx's import spreadsheet functionality, the entity ID and entity name must be replicated exactly in the spreadsheet. | Text | Global |  | `parcel.ClientEntityID · TEXT` |  |
| `ComparisonList` | Comparison List | When added to a page layout, this field allows for a comparison of entities from a page or subpage. | Text | — |  | `parcel.ComparisonList · TEXT` |  |
| `CompletedPhaseStatus` | Completed Phase Status | The milestone timeline status of the entity. This status is updated when a milestone is completed. | Text | — |  | `parcel.CompletedPhaseStatus · TEXT` |  |
| `ConstructionPhaseStatus` | Construction Phase Status | This is a default field that is not used for parcels. | Text | — |  | `parcel.ConstructionPhaseStatus · TEXT` |  |
| `CountryID` | Country | The country of the location this parcel is associated with. | Text | Global |  | `parcel.CountryID · TEXT` |  |
| `CrossStreet1` | Cross Street #1 | Enter the first cross street in this field. | Text | Global |  | `parcel.CrossStreet1 · TEXT` |  |
| `CrossStreet2` | Cross Street #2 | Enter the second cross street in this field. | Text | Global |  | `parcel.CrossStreet2 · TEXT` |  |
| `CurrentMilestone` | Current Milestone | The current milestone task of your entity schedule. | Text | — |  | `parcel.CurrentMilestone · TEXT` |  |
| `CurrentPhaseStatus` | Project Status | This is a default field. This field is not implemented for parcels. | Text | — |  | `parcel.CurrentPhaseStatus · TEXT` |  |
| `DesignPhaseStatus` | Design Phase Status | This is a default field that is not used for parcels. | Text | — |  | `parcel.DesignPhaseStatus · TEXT` |  |
| `EntityEmail` | Entity Email | The entity's email address that is created when the Email into Lx functionality is enabled. | Text | — |  | `parcel.EntityEmail · TEXT` |  |
| `EntityPhoto` | Entity Photo | This is a generic field. When you add this field to a page layout, you can use it to add a photo to the layout. | Text | — |  | `parcel.EntityPhoto · TEXT` |  |
| `FacilityName` | Facility Name | The name of the facility associated with this entity. | Text | — |  | `parcel.FacilityName · TEXT` |  |
| `FinancialModel` | Financial Model | When added to a page layout, this field appears as a button that generates an Excel Financial Model spreadsheet. If you have questions about this functionality, contact your Accruent representative. | Text | — |  | `parcel.FinancialModel · TEXT` |  |
| `FirmID` | Firm ID | The record's Firm ID. | Text | — | yes | `parcel.FirmID · TEXT` |  |
| `Firm_SalesReportLogo` | Sales Report Logo |  | Text | — |  | `parcel.Firm_SalesReportLogo · TEXT` |  |
| `Firm_SalesReportLogoMadewell` |  |  | Text | — |  |  |  |
| `Firm_SalesReportSignature` | Sales Report Signature |  | Text | — |  | `parcel.Firm_SalesReportSignature · TEXT` |  |
| `Firm_SalesReportSignatureName` | Sales Report Signature Name |  | Text | — |  | `parcel.Firm_SalesReportSignatureName · TEXT` |  |
| `Firm_SalesReportSignatureTitle` | Sales Report Signature Title |  | Text | — |  | `parcel.Firm_SalesReportSignatureTitle · TEXT` |  |
| `Grid` |  | Enter the parcel's grid number in this field. | Text | Global |  | `parcel.Grid · TEXT` |  |
| `HTMLAddress` | Full Address | The associated entity's address in HTML format. | Text | Global |  | `parcel.HTMLAddress · TEXT` |  |
| `IndexNumber` | Index Number | Enter the parcel's index number in this field. | Text | Global |  | `parcel.IndexNumber · TEXT` |  |
| `IssuesAndAlerts` | Issues And Alerts | This field can be added to page layouts. In View mode, this field will display a table with form and workflow data, such as the work flow / form type, critical issue count, non-critical issue count, escalated count, and past due notification count. | Text | — |  | `parcel.IssuesAndAlerts · TEXT` |  |
| `Lot` |  | If your parcel has a lot identifier this is commonly for parcels in urban areas enter the lot identifier in this field. | Text | Global |  | `parcel.Lot · TEXT` |  |
| `MapClientRecordID` | Client Unique ID | The entity Map Client Record ID. | Text | — |  | `parcel.MapClientRecordID · TEXT` |  |
| `MilestoneTimeline` | Milestone Timeline | This field generates a list of all milestones, but hides those with no values. | Text | — |  | `parcel.MilestoneTimeline · TEXT` |  |
| `NextMilestone` | Next Milestone | The upcoming milestone in the milestone timeline. | Text | — |  | `parcel.NextMilestone · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `parcel.Notes · TEXT` |  |
| `OperationsPhaseStatus` | Operations Phase Status | This is a default field that is not used for parcels. | Text | — |  | `parcel.OperationsPhaseStatus · TEXT` |  |
| `OwnerName` | Owner Name | Enter the owner of the parcel in this field. | Text | Global |  | `parcel.OwnerName · TEXT` |  |
| `ParcelName` | Parcel Name | Enter the parcel name in this field. | Text | Global | yes | `parcel.ParcelName · TEXT` |  |
| `ParcelNumber` | Parcel Number | Enter the parcel number in this field. | Text | Global |  | `parcel.ParcelNumber · TEXT` |  |
| `ParcelPublicName` | Parcel Public Name | If your parcel has an official or public name on the assessor's documentation that differs from the name you use in Lx, enter the name here. | Text | Global |  | `parcel.ParcelPublicName · TEXT` |  |
| `Phone` |  | This field can be used to store a phone number. | Text | — |  | `parcel.Phone · TEXT` |  |
| `PossessionPhaseStatus` | Possession Phase Status | This is a default field that is not used for parcels. | Text | — |  | `parcel.PossessionPhaseStatus · TEXT` |  |
| `PostalCode` | Postal Code | Enter the postal code of the entity in this field. | Text | Global |  | `parcel.PostalCode · TEXT` |  |
| `PotentialProjectName` | Site Name | The name of the site associated with this entity. | Text | — |  | `parcel.PotentialProjectName · TEXT` |  |
| `PreviousMilestone` | Previous Milestone | The previous milestone task. | Text | — |  | `parcel.PreviousMilestone · TEXT` |  |
| `ProgramName` | Portfolio/Program Name | The name of the portfolio associated with this entity. | Text | — |  | `parcel.ProgramName · TEXT` |  |
| `ProjectDescription` | Description | Write a description of the record. | Text | Global |  | `parcel.ProjectDescription · TEXT` |  |
| `ProjectEntityName` | Name | The entity name. | Text | — | yes | `parcel.ProjectEntityName · TEXT` |  |
| `ProjectEntityTypeName` | Entity Type | The entity type. | Text | — |  | `parcel.ProjectEntityTypeName · TEXT` |  |
| `ProjectName` | Project Name | The name of the project associated with the record. | Text | — |  | `parcel.ProjectName · TEXT` |  |
| `PrototypeName` | Prototype Name | The name of the prototype associated with this entity. | Text | — |  | `parcel.PrototypeName · TEXT` |  |
| `RealEstatePhaseStatus` | Real Estate Phase Status | This is a default field that is not used for parcels. | Text | — |  | `parcel.RealEstatePhaseStatus · TEXT` |  |
| `RelatedEntities` | Related Entities | The name of entities associated with this entity. | Text | — |  | `parcel.RelatedEntities · TEXT` |  |
| `RelocatedFrom` |  | This field is not implemented for parcels. | Text | — |  | `parcel.RelocatedFrom · TEXT` |  |
| `RunReportAction` | Run Report Action | This is a generic field. When you add this field to a page layout, it will run a report. See the Run Report Action Buttons article in the Online Help to learn more. | Text | — |  | `parcel.RunReportAction · TEXT` |  |
| `SourceReference` | Source Reference | The Parcel Tax Assessment section was created before the Property Taxes sub-module was created. You may use this section to log assessment data, but understand that this section does not create or store individual tax assessment records. To create and store individual tax assessment records, see the Property Taxes sub-module. | Text | Global |  | `parcel.SourceReference · TEXT` |  |
| `StreetAddress` | Street Address | The street address. | Text | — |  | `parcel.StreetAddress · TEXT` |  |
| `StreetAddress1` | Street Address #1 | The first line of the street address. | Text | Global |  | `parcel.StreetAddress1 · TEXT` |  |
| `StreetAddress2` | Street Address #2 | The second line of the street address. | Text | Global |  | `parcel.StreetAddress2 · TEXT` |  |
| `StreetAddress3` | Street Address #3 | The third line of the street address. | Text | Global |  | `parcel.StreetAddress3 · TEXT` |  |
| `StreetAddress4` | Street Address #4 | The fourth line of the street address. | Text | Global |  | `parcel.StreetAddress4 · TEXT` |  |
| `TaxAuthority` | Tax Authority | Enter the main tax authority for the parcel in this field. You can enter tax assessment records for other tax authorities such as county, city, or state, on the Property Taxes page. | Text | Global |  | `parcel.TaxAuthority · TEXT` |  |
| `TaxIDNumber` | Tax ID Number | Enter the tax ID number for the parcel. Each parcel has a unique parcel number and often more than one parcel will be part of a location. An assessor may group multiple parcels together with a single tax ID and provide a consolidated tax bill, or a company might have multiple tax IDs if they are receiving separate tax bills for a location. | Text | Global |  | `parcel.TaxIDNumber · TEXT` |  |
| `ThirdPartyWarehouse` | Third Party Warehouse | This is a default field that is not used for parcels. | Text | Global |  | `parcel.ThirdPartyWarehouse · TEXT` |  |
| `TimeZone` | Time Zone | Select the appropriate time zone from this field. | Text | Global |  | `parcel.TimeZone · TEXT` |  |
| `TradeArea` | Trade Area | The trade area from the parcel's location. | Text | — |  | `parcel.TradeArea · TEXT` |  |

### Audit & record keeping (7)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Parcel ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `parcel.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | — |  | `parcel.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | — |  | `parcel.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `parcel.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `parcel.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | — |  | `parcel.RevNumber · TEXT` |  |
| `UUID` | Parcel UUID | This field captures a unique identifier associated with your record. This identifier is used if you are using an integration with other Accruent products. | Text | Global |  | `parcel.UUID · TEXT` |  |

### Other (1)

Everything that did not fall into a named group.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `GrossArea` | Gross Acreage | Enter the gross area in this field. | Acreage | — |  | `parcel.GrossArea · TEXT` |  |

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
