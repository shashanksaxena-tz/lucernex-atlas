# Location

*141 fields · module: Facilities, Locations & Sites · Postgres: `location`*

A general site/location record — address and geocoding fields (Latitude, Longitude) plus percentage-based site metrics — used as a lighter-weight alternative to Facility for sites that are tracked before or without a full facility record. 66 fields (61 Global, 5 Firm) under its own Location group.

Source: `data-fields/location.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 141 |
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

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BudgetTemplateID` | Budget Template | Template ID | Global |  | [BudgetTemplate](BudgetTemplate.md) |
| `ComplexID` | Complex Name | Complex ID | Global |  | [Complex](Complex.md) |
| `DemographicDMAID` |  | DMA ID | — |  | [DMA](DMA.md) |
| `IStateProvinceCountryID` | State | Country, State, County ID | Global |  | [StateProvinceCountry](StateProvinceCountry.md) |
| `JurisdictionID` | Jurisdiction | County ID | Global |  | [Jurisdiction](Jurisdiction.md) |
| `OrganizationID` | Organization | Organization ID | Global |  | [Organization](Organization.md) |
| `ProgramID` | Portfolio | Portfolio ID | Global | yes | [Program](Program.md) |
| `PrototypeID` |  | Prototype ID | — |  | [Prototype](Prototype.md) |
| `RegionID` | Region | Region ID | Global |  | [Region](Region.md) |
| `RootRegionID` |  | Region ID | — |  | [Region](Region.md) |
| `SubRegionID` |  | Region ID | — |  | [Region](Region.md) |

### Soft references (2)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `LinkProjectEntityContactListData` |  | Contact | — |  |  |
| `ManagerIDList` |  | Dropdown | — |  |  |

### Coded values (drop-downs) (23)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeBuildingAreaUnitID` | Building Area Unit | Dropdown (Building Area Unit Code) | Global |  | Building Area Unit Code |
| `CodeConstructionTypeID` |  | Dropdown (Construction Type Code) | — |  | Construction Type Code |
| `CodeCurrencyTypeID` | Currency Type | Dropdown (Currency Type Code) | Global |  | Currency Type Code |
| `CodeDealTypeID` |  | Dropdown (Deal Type Code) | — |  | Deal Type Code |
| `CodeDesc_CodeMarketAreaID` |  | Dropdown (Market Area Code) | — |  | Market Area Code |
| `CodeDesc_CodeProjectTypeID` |  | Dropdown (Project Type Code) | — |  | Project Type Code |
| `CodeDistributionCenterID` |  | Dropdown (Distribution Center Code) | — |  | Distribution Center Code |
| `CodeLandAreaUnitID` | Land Area Unit | Dropdown (Land Area Unit Code) | Global |  | Land Area Unit Code |
| `CodeLocationCategoryID` | Location Category | Dropdown (Location Category Code) | Global |  | Location Category Code |
| `CodeLocationGroupID` | Location Group | Dropdown (Location Group Code) | Global |  | Location Group Code |
| `CodeLocationStatusID` | Location Status | Dropdown (Location Status Code) | Global |  | Location Status Code |
| `CodeLocationTypeID` | Location Type | Dropdown (Location Type Code) | Global |  | Location Type Code |
| `CodeLocationUseID` | Location Use | Dropdown (Location Use Code) | Global |  | Location Use Code |
| `CodeMarketAreaID` | Market Area | Dropdown (Market Area Code) | Global |  | Market Area Code |
| `CodeMarketTypeID` |  | Dropdown (Market Type Code) | — |  | Market Type Code |
| `CodeProjectTypeID` |  | Dropdown (Project Type Code) | — |  | Project Type Code |
| `CodeSubArea1ID` | Sub Area #1 | Dropdown (Area Code) | Global |  | Area Code |
| `CodeSubArea2ID` | Sub Area #2 | Dropdown (Area Code) | Global |  | Area Code |
| `CodeSubArea3ID` | Sub Area #3 | Dropdown (Area Code) | Global |  | Area Code |
| `CodeSubRegion1ID` | Sub Region #1 | Dropdown (Region Code) | Global |  | Region Code |
| `CodeSubRegion2ID` | Sub Region #2 | Dropdown (Region Code) | Global |  | Region Code |
| `CodeSubRegion3ID` | Sub Region #3 | Dropdown (Region Code) | Global |  | Region Code |
| `CurrentCodeProjectPhaseID` |  | Dropdown (Project Phase Code) | — |  | Project Phase Code |

### Money (1)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Firm_PriorMonthAccrualTotal` |  | Currency | — |  |  |

### Rates & percentages (8)

Percentage inputs and computed rates.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `EquipContractTaxRate1` | EC Tax Rate #1 | Percentage | Global |  |  |
| `EquipContractTaxRate2` | EC Tax Rate #2 | Percentage | Global |  |  |
| `EquipContractTaxRate3` | EC Tax Rate #3 | Percentage | Global |  |  |
| `EquipContractTaxRate4` | EC Tax Rate #4 | Percentage | Global |  |  |
| `TaxRate1` | RE Tax Rate #1 | Percentage | Global |  |  |
| `TaxRate2` | RE Tax Rate #2 | Percentage | Global |  |  |
| `TaxRate3` | RE Tax Rate #3 | Percentage | Global |  |  |
| `TaxRate4` | RE Tax Rate #4 | Percentage | Global |  |  |

### Quantities (19)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ActualRevenueWeeks` |  | Number | — |  |  |
| `DBFolderSizeMB` |  | 2-Digit Number | — |  |  |
| `Depth` |  | Number | — |  |  |
| `EDGE_ASGCenterID` | ASG Center ID | Number | Firm |  |  |
| `EntityId` |  | Number | — |  |  |
| `Frontage` |  | Number | — |  |  |
| `GrossLeaseArea` | Gross Lease Area | Number | Global |  |  |
| `LatitudeDegrees` | Latitude | 5-Digit Number | Global |  |  |
| `LocationID` | Location RecID | Number | Global |  |  |
| `LocationParcelArea` | Location Parcel Area | Number | Global |  |  |
| `LongitudeDegrees` | Longitude | 5-Digit Number | Global |  |  |
| `NumberOfDocuments` |  | Number | — |  |  |
| `OpenYear` | Open Year | Number | Global |  |  |
| `OutOfDateDays` | Out Of Date Days | Number | Global |  |  |
| `ProjectEntityID` |  | Number | — |  |  |
| `RentableArea` |  | Number | — |  |  |
| `SequenceNumber` |  | Number | — |  |  |
| `ThirdPartyWarehouseArea` | Third Party Warehouse Area | Number | Global |  |  |
| `UsableArea` |  | Number | — |  |  |

### Dates & timestamps (9)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ActualEndDate` |  | Date | — |  |  |
| `ActualStartDate` |  | Date | — |  |  |
| `BaselineEndDate` |  | Date | — |  |  |
| `ClientScheduleLastReviewedDate` |  | Date | — |  |  |
| `ExpectedEndDate` |  | Date | — |  |  |
| `Firm_GrandOpeningDate` | Grand Opening Date | Date | Firm |  |  |
| `OriginalEndDate` |  | Date | — |  |  |
| `OriginalStartDate` |  | Date | — |  |  |
| `SlotEndDate` |  | Date | — |  |  |

### Flags (2)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Inactive` | Is Inactive? | Boolean | Global | yes |  |
| `IsDead` |  | Boolean | — |  |  |

### Text & notes (58)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AccountingNumber` | Accounting Number | Text | Global |  |  |
| `BaseProvider` |  | Text | — |  |  |
| `City` |  | Text | Global |  |  |
| `CityStateProvinceCountry` |  | Text | — |  |  |
| `ClientEntityID` | Location ID | Text | Global |  |  |
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
| `Firm_CenterName` | Center Name | Text | Firm |  |  |
| `Firm_County` | County | Text | Firm |  |  |
| `Firm_Developer` | Developer | Text | Firm |  |  |
| `Firm_SalesReportLogo` |  | Text | — |  |  |
| `Firm_SalesReportLogoMadewell` |  | Text | — |  |  |
| `Firm_SalesReportSignature` |  | Text | — |  |  |
| `Firm_SalesReportSignatureName` |  | Text | — |  |  |
| `Firm_SalesReportSignatureTitle` |  | Text | — |  |  |
| `HTMLAddress` | Full Address | Text | Global |  |  |
| `IssuesAndAlerts` |  | Text | — |  |  |
| `LocationName` | Location Name | Text | Global | yes |  |
| `MapClientRecordID` |  | Text | — |  |  |
| `MilestoneTimeline` |  | Text | — |  |  |
| `NextMilestone` |  | Text | — |  |  |
| `Notes` |  | Text | Global |  |  |
| `OperationsPhaseStatus` |  | Text | — |  |  |
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
| `StreetAddress` |  | Text | — |  |  |
| `StreetAddress1` | Street Address #1 | Text | Global |  |  |
| `StreetAddress2` | Street Address #2 | Text | Global |  |  |
| `StreetAddress3` | Street Address #3 | Text | Global |  |  |
| `StreetAddress4` | Street Address #4 | Text | Global |  |  |
| `ThirdPartyWarehouse` | Third Party Warehouse | Text | Global |  |  |
| `TimeZone` | Time Zone | Text | Global |  |  |
| `TradeArea` |  | Text | — |  |  |

### Audit & record keeping (7)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Location ClientID | Text | Global | yes |  |
| `CreatedByID` |  | Member ID | — |  | [Member](Member.md) |
| `CreatedDate` |  | Time | — |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` |  | Number | — |  |  |
| `UUID` | Location UUID | Text | Global |  |  |

### Other (1)

Everything that did not fall into a named group.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `GrossArea` |  | Acreage | — |  |  |

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
