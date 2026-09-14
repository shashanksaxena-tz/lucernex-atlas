# SiteSurvey

*79 fields · module: Facilities, Locations & Sites · Postgres: `site_survey`*

Site-selection/demographic evaluation data for a candidate location — household income and count at 1/3/5-mile radii, median age, and condition-code ratings, used during real estate site selection before a lease is signed. 78 Global fields under its own Site Survey group; the repeated '-1 Mile/-3 Miles/-5 Miles' field triples show Lx bakes fixed trade-area radii into the schema rather than storing a single configurable radius.

Source: `data-fields/site-survey.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 79 |
| Fields with a vendor definition | 8 of 79 inventoried |
| Physical tables | `site_survey` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 78 (78 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 2 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 2 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in site_survey

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 8 fields carry a vendor definition

**Observed.** 8 of this record's 79 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one source in the corpus that explains fields rather than listing them.

### 1 field marked required

**Observed.** The inventory marks 1 of this record's fields Required. Across the whole inventory that is 606 fields, which independently corroborates the 603 the corpus had derived from the Data Fields catalogue — two sources, arrived at separately, agreeing to within three.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [FAC-R-018](../rules/FAC-R-018.md) | Input: `Ownership`, `SiteSurvey`, `LandPurchaseSummary`, `LinkLandPurchaseInspection`, `DemographicResults` carry `ProjectEntityID` and no hard-typed FK to `Facility`/`Location`/`Parcel`. Effect: In principle any of these can attach to any  | Derived |
| [FAC-R-020](../rules/FAC-R-020.md) | Input: `SiteSurvey` carries `Population1Mile/3Miles/5Miles` (and six more metrics repeated the same way) as fixed columns; `DemographicStudyArea` carries `AreaRadius`/`AreaDriveTimeInMinutes` as a reusable, parameterised definition. | Derived |

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ProjectEntityID` |  |  | Entity ID | — |  | `site_survey.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (13)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeBuildingAreaUnitID` | Building Area Unit | Select the units you are using to measure your area from this field. | Dropdown (Building Area Unit Code) | Global |  | `site_survey.CodeBuildingAreaUnitID · TEXT` | Building Area Unit Code |
| `CodeCeilingConditionID` | Ceiling Condition |  | Dropdown (Condition Code) | Global |  | `site_survey.CodeCeilingConditionID · TEXT` | Condition Code |
| `CodeCurrentZoningID` | Current Zoning |  | Dropdown (Zoning Code) | Global |  | `site_survey.CodeCurrentZoningID · TEXT` | Zoning Code |
| `CodeFacilityConditionID` | Facility Condition |  | Dropdown (Condition Code) | Global |  | `site_survey.CodeFacilityConditionID · TEXT` | Condition Code |
| `CodeFloorConditionID` | Existing Floor Condition |  | Dropdown (Condition Code) | Global |  | `site_survey.CodeFloorConditionID · TEXT` | Condition Code |
| `CodeLandAreaUnitID` | Land Area Unit | Select the unit you will use for measuring your area. | Dropdown (Land Area Unit Code) | Global |  | `site_survey.CodeLandAreaUnitID · TEXT` | Land Area Unit Code |
| `CodeLocationAccessID` | Accessibility |  | Dropdown (Location Access Code) | Global |  | `site_survey.CodeLocationAccessID · TEXT` | Location Access Code |
| `CodeParkingLotConditionID` | Parking Lot Conditions |  | Dropdown (Condition Code) | Global |  | `site_survey.CodeParkingLotConditionID · TEXT` | Condition Code |
| `CodeRequiredZoningID` | Required Zoning |  | Dropdown (Zoning Code) | Global |  | `site_survey.CodeRequiredZoningID · TEXT` | Zoning Code |
| `CodeSiteRatingID` | Site Rating |  | Dropdown (Site Rating Code) | Global |  | `site_survey.CodeSiteRatingID · TEXT` | Site Rating Code |
| `CodeTradeAreaQualityID` | Trade Area Quality |  | Dropdown (Condition Code) | Global |  | `site_survey.CodeTradeAreaQualityID · TEXT` | Condition Code |
| `CodeVehicleAccessConditionID` | Vehicle Access Condition |  | Dropdown (Condition Code) | Global |  | `site_survey.CodeVehicleAccessConditionID · TEXT` | Condition Code |
| `CodeVisibilityConditionID` | Visibility |  | Dropdown (Condition Code) | Global |  | `site_survey.CodeVisibilityConditionID · TEXT` | Condition Code |

### Money (3)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `HouseholdAvgIncome1Mile` | Household Avg Income-1 Mile |  | Currency | Global |  | `site_survey.HouseholdAvgIncome1Mile · TEXT` |  |
| `HouseholdAvgIncome3Miles` | Household Avg Income-3 Miles |  | Currency | Global |  | `site_survey.HouseholdAvgIncome3Miles · TEXT` |  |
| `HouseholdAvgIncome5Miles` | Household Avg Income-5 Miles |  | Currency | Global |  | `site_survey.HouseholdAvgIncome5Miles · TEXT` |  |

### Quantities (31)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AgeOfHVACUnits` | Age Of HVAC Units |  | Number | Global |  | `site_survey.AgeOfHVACUnits · TEXT` |  |
| `ApproxBuildingLength` | Approx Building Length |  | Number | Global |  | `site_survey.ApproxBuildingLength · TEXT` |  |
| `ApproxBuildingWidth` | Approx Building Width |  | Number | Global |  | `site_survey.ApproxBuildingWidth · TEXT` |  |
| `Households1Mile` | Households-1 Mile |  | Number | Global |  | `site_survey.Households1Mile · TEXT` |  |
| `Households3Miles` | Households-3 Miles |  | Number | Global |  | `site_survey.Households3Miles · TEXT` |  |
| `Households5Miles` | Households-5 Miles |  | Number | Global |  | `site_survey.Households5Miles · TEXT` |  |
| `MedianAge1Mile` | Median Age-1 Mile |  | Number | Global |  | `site_survey.MedianAge1Mile · TEXT` |  |
| `MedianAge3Miles` | Median Age-3 Miles |  | Number | Global |  | `site_survey.MedianAge3Miles · TEXT` |  |
| `MedianAge5Miles` | Median Age-5 Miles |  | Number | Global |  | `site_survey.MedianAge5Miles · TEXT` |  |
| `NumberOfAmps` | Number Of Amps |  | Number | Global |  | `site_survey.NumberOfAmps · TEXT` |  |
| `NumberOfBuildingSides` | Number Of Building Sides |  | Number | Global |  | `site_survey.NumberOfBuildingSides · TEXT` |  |
| `NumberOfElectricalPanels` | Number Of Electrical Panels |  | Number | Global |  | `site_survey.NumberOfElectricalPanels · TEXT` |  |
| `NumberOfFixtures` | Number Of Fixtures |  | Number | Global |  | `site_survey.NumberOfFixtures · TEXT` |  |
| `NumberOfFloors` | Number Of Floors |  | Number | Global |  | `site_survey.NumberOfFloors · TEXT` |  |
| `NumberOfHVACUnits` | Number Of HVAC Units |  | Number | Global |  | `site_survey.NumberOfHVACUnits · TEXT` |  |
| `NumberOfRestrooms` | Number Of Restrooms |  | Number | Global |  | `site_survey.NumberOfRestrooms · TEXT` |  |
| `PercentFemale1Mile` | Percent Female-1 Mile |  | Number | Global |  | `site_survey.PercentFemale1Mile · TEXT` |  |
| `PercentFemale3Miles` | Percent Female-3 Miles |  | Number | Global |  | `site_survey.PercentFemale3Miles · TEXT` |  |
| `PercentFemale5Miles` | Percent Female-5 Miles |  | Number | Global |  | `site_survey.PercentFemale5Miles · TEXT` |  |
| `PercentMale1Mile` | Percent Male-1 Mile |  | Number | Global |  | `site_survey.PercentMale1Mile · TEXT` |  |
| `PercentMale3Miles` | Percent Male-3 Miles |  | Number | Global |  | `site_survey.PercentMale3Miles · TEXT` |  |
| `PercentMale5Miles` | Percent Male-5 Miles |  | Number | Global |  | `site_survey.PercentMale5Miles · TEXT` |  |
| `Population1Mile` | Population-1 Mile |  | Number | Global |  | `site_survey.Population1Mile · TEXT` |  |
| `Population3Miles` | Population-3 Miles |  | Number | Global |  | `site_survey.Population3Miles · TEXT` |  |
| `Population5Miles` | Population-5 Miles |  | Number | Global |  | `site_survey.Population5Miles · TEXT` |  |
| `SeatingCapacity` | Seating Capacity |  | Number | Global |  | `site_survey.SeatingCapacity · TEXT` |  |
| `SiteSurveyID` | Site Suvery RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `site_survey.SiteSurveyID · VARCHAR(64) NOT NULL` |  |
| `TrafficCount` | Traffic Count |  | Number | Global |  | `site_survey.TrafficCount · TEXT` |  |
| `UsableLandArea` | Usable Land Area |  | Number | Global |  | `site_survey.UsableLandArea · TEXT` |  |
| `UsableParcelArea` | Usable Parcel Area |  | Number | Global |  | `site_survey.UsableParcelArea · TEXT` |  |
| `WeightOfHVACUnits` | Weight Of HVAC Units |  | Number | Global |  | `site_survey.WeightOfHVACUnits · TEXT` |  |

### Dates & timestamps (1)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `SentToConstructionDate` | Sent To Construction Date |  | Date | Global |  | `site_survey.SentToConstructionDate · TEXT` |  |

### Flags (17)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BuildingSignage` | Building Signage? |  | Boolean | Global |  | `site_survey.BuildingSignage · TEXT` |  |
| `CanopyLighting` | Canopy Lighting? |  | Boolean | Global |  | `site_survey.CanopyLighting · TEXT` |  |
| `FireSprinkler` | Fire Sprinkler? |  | Boolean | Global |  | `site_survey.FireSprinkler · TEXT` |  |
| `HandicapAccessible` | Handicap Accessible? |  | Boolean | Global |  | `site_survey.HandicapAccessible · TEXT` |  |
| `IsBuildingPlanAvail` | Is Building Plan Available? |  | Boolean | Global |  | `site_survey.IsBuildingPlanAvail · TEXT` |  |
| `IsCLECAvail` | Is CLEC Available? |  | Boolean | Global |  | `site_survey.IsCLECAvail · TEXT` |  |
| `IsConstructionCriteriaAvail` | Is Construction Criteria Available? |  | Boolean | Global |  | `site_survey.IsConstructionCriteriaAvail · TEXT` |  |
| `IsCurrentlyOccupied` | Is Currently Occupied? |  | Boolean | Global |  | `site_survey.IsCurrentlyOccupied · TEXT` |  |
| `IsLODAvail` | Is LOD Available? |  | Boolean | Global |  | `site_survey.IsLODAvail · TEXT` |  |
| `IsLandlordWorkDescriptionAvail` | Is Landlord Work Description Available? |  | Boolean | Global |  | `site_survey.IsLandlordWorkDescriptionAvail · TEXT` |  |
| `IsRoofAccessAvail` | Roof Access |  | Boolean | Global |  | `site_survey.IsRoofAccessAvail · TEXT` |  |
| `IsSignCriteriaAvail` | Is Sign Criteria Available? |  | Boolean | Global |  | `site_survey.IsSignCriteriaAvail · TEXT` |  |
| `MonumentSignage` | Monument Signage? |  | Boolean | Global |  | `site_survey.MonumentSignage · TEXT` |  |
| `ParkingLotLighting` | Parking Lot Lighting |  | Boolean | Global |  | `site_survey.ParkingLotLighting · TEXT` |  |
| `PylonSignage` | Pylon Signage |  | Boolean | Global |  | `site_survey.PylonSignage · TEXT` |  |
| `RecommendToREC` | Recommend to REC? |  | Boolean | Global |  | `site_survey.RecommendToREC · TEXT` |  |
| `TrafficSignalAccess` | Signalized Access |  | Boolean | Global |  | `site_survey.TrafficSignalAccess · TEXT` |  |

### Text & notes (10)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AnchorTenants` | Anchor Tenants |  | Text | Global |  | `site_survey.AnchorTenants · TEXT` |  |
| `CurrentOrFormerTenants` | Current Or Former Tenants |  | Text | Global |  | `site_survey.CurrentOrFormerTenants · TEXT` |  |
| `FacilityDescription` | Facility Description | Write a description of the record. | Text | Global |  | `site_survey.FacilityDescription · TEXT` |  |
| `FacilityLocation` | Facility Location |  | Text | Global |  | `site_survey.FacilityLocation · TEXT` |  |
| `FacilityPriorUse` | Facility Prior Use |  | Text | Global |  | `site_survey.FacilityPriorUse · TEXT` |  |
| `NeighborhoodDescription` | Neighborhood Description | Write a description of the record. | Text | Global |  | `site_survey.NeighborhoodDescription · TEXT` |  |
| `SiteRatingExplanation` | Site Rating Explanation |  | Text | Global |  | `site_survey.SiteRatingExplanation · TEXT` |  |
| `SpaceNumber` | Space Number |  | Text | Global |  | `site_survey.SpaceNumber · TEXT` |  |
| `TypeOfFixtures` | Type Of Fixtures |  | Text | Global |  | `site_survey.TypeOfFixtures · TEXT` |  |
| `WhichSides` | Which Building Sides |  | Text | Global |  | `site_survey.WhichSides · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Site Survey ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `site_survey.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `site_survey.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `site_survey.ModifiedDate · TEXT` |  |
