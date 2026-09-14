# SiteSurvey

*79 fields · module: Facilities, Locations & Sites · Postgres: `site_survey`*

Site-selection/demographic evaluation data for a candidate location — household income and count at 1/3/5-mile radii, median age, and condition-code ratings, used during real estate site selection before a lease is signed. 78 Global fields under its own Site Survey group; the repeated '-1 Mile/-3 Miles/-5 Miles' field triples show Lx bakes fixed trade-area radii into the schema rather than storing a single configurable radius.

Source: `data-fields/site-survey.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 79 |
| Catalogued fields | 78 (78 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 2 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 2 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [FAC-R-018](../rules/FAC-R-018.md) | Input: `Ownership`, `SiteSurvey`, `LandPurchaseSummary`, `LinkLandPurchaseInspection`, `DemographicResults` carry `ProjectEntityID` and no hard-typed FK to `Facility`/`Location`/`Parcel`. Effect: In principle any of these can attach to any  | Derived |
| [FAC-R-020](../rules/FAC-R-020.md) | Input: `SiteSurvey` carries `Population1Mile/3Miles/5Miles` (and six more metrics repeated the same way) as fixed columns; `DemographicStudyArea` carries `AreaRadius`/`AreaDriveTimeInMinutes` as a reusable, parameterised definition. | Derived |

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (13)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeBuildingAreaUnitID` | Building Area Unit | Dropdown (Building Area Unit Code) | Global |  | Building Area Unit Code |
| `CodeCeilingConditionID` | Ceiling Condition | Dropdown (Condition Code) | Global |  | Condition Code |
| `CodeCurrentZoningID` | Current Zoning | Dropdown (Zoning Code) | Global |  | Zoning Code |
| `CodeFacilityConditionID` | Facility Condition | Dropdown (Condition Code) | Global |  | Condition Code |
| `CodeFloorConditionID` | Existing Floor Condition | Dropdown (Condition Code) | Global |  | Condition Code |
| `CodeLandAreaUnitID` | Land Area Unit | Dropdown (Land Area Unit Code) | Global |  | Land Area Unit Code |
| `CodeLocationAccessID` | Accessibility | Dropdown (Location Access Code) | Global |  | Location Access Code |
| `CodeParkingLotConditionID` | Parking Lot Conditions | Dropdown (Condition Code) | Global |  | Condition Code |
| `CodeRequiredZoningID` | Required Zoning | Dropdown (Zoning Code) | Global |  | Zoning Code |
| `CodeSiteRatingID` | Site Rating | Dropdown (Site Rating Code) | Global |  | Site Rating Code |
| `CodeTradeAreaQualityID` | Trade Area Quality | Dropdown (Condition Code) | Global |  | Condition Code |
| `CodeVehicleAccessConditionID` | Vehicle Access Condition | Dropdown (Condition Code) | Global |  | Condition Code |
| `CodeVisibilityConditionID` | Visibility | Dropdown (Condition Code) | Global |  | Condition Code |

### Money (3)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `HouseholdAvgIncome1Mile` | Household Avg Income-1 Mile | Currency | Global |  |  |
| `HouseholdAvgIncome3Miles` | Household Avg Income-3 Miles | Currency | Global |  |  |
| `HouseholdAvgIncome5Miles` | Household Avg Income-5 Miles | Currency | Global |  |  |

### Quantities (31)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AgeOfHVACUnits` | Age Of HVAC Units | Number | Global |  |  |
| `ApproxBuildingLength` | Approx Building Length | Number | Global |  |  |
| `ApproxBuildingWidth` | Approx Building Width | Number | Global |  |  |
| `Households1Mile` | Households-1 Mile | Number | Global |  |  |
| `Households3Miles` | Households-3 Miles | Number | Global |  |  |
| `Households5Miles` | Households-5 Miles | Number | Global |  |  |
| `MedianAge1Mile` | Median Age-1 Mile | Number | Global |  |  |
| `MedianAge3Miles` | Median Age-3 Miles | Number | Global |  |  |
| `MedianAge5Miles` | Median Age-5 Miles | Number | Global |  |  |
| `NumberOfAmps` | Number Of Amps | Number | Global |  |  |
| `NumberOfBuildingSides` | Number Of Building Sides | Number | Global |  |  |
| `NumberOfElectricalPanels` | Number Of Electrical Panels | Number | Global |  |  |
| `NumberOfFixtures` | Number Of Fixtures | Number | Global |  |  |
| `NumberOfFloors` | Number Of Floors | Number | Global |  |  |
| `NumberOfHVACUnits` | Number Of HVAC Units | Number | Global |  |  |
| `NumberOfRestrooms` | Number Of Restrooms | Number | Global |  |  |
| `PercentFemale1Mile` | Percent Female-1 Mile | Number | Global |  |  |
| `PercentFemale3Miles` | Percent Female-3 Miles | Number | Global |  |  |
| `PercentFemale5Miles` | Percent Female-5 Miles | Number | Global |  |  |
| `PercentMale1Mile` | Percent Male-1 Mile | Number | Global |  |  |
| `PercentMale3Miles` | Percent Male-3 Miles | Number | Global |  |  |
| `PercentMale5Miles` | Percent Male-5 Miles | Number | Global |  |  |
| `Population1Mile` | Population-1 Mile | Number | Global |  |  |
| `Population3Miles` | Population-3 Miles | Number | Global |  |  |
| `Population5Miles` | Population-5 Miles | Number | Global |  |  |
| `SeatingCapacity` | Seating Capacity | Number | Global |  |  |
| `SiteSurveyID` | Site Suvery RecID | Number | Global |  |  |
| `TrafficCount` | Traffic Count | Number | Global |  |  |
| `UsableLandArea` | Usable Land Area | Number | Global |  |  |
| `UsableParcelArea` | Usable Parcel Area | Number | Global |  |  |
| `WeightOfHVACUnits` | Weight Of HVAC Units | Number | Global |  |  |

### Dates & timestamps (1)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `SentToConstructionDate` | Sent To Construction Date | Date | Global |  |  |

### Flags (17)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BuildingSignage` | Building Signage? | Boolean | Global |  |  |
| `CanopyLighting` | Canopy Lighting? | Boolean | Global |  |  |
| `FireSprinkler` | Fire Sprinkler? | Boolean | Global |  |  |
| `HandicapAccessible` | Handicap Accessible? | Boolean | Global |  |  |
| `IsBuildingPlanAvail` | Is Building Plan Available? | Boolean | Global |  |  |
| `IsCLECAvail` | Is CLEC Available? | Boolean | Global |  |  |
| `IsConstructionCriteriaAvail` | Is Construction Criteria Available? | Boolean | Global |  |  |
| `IsCurrentlyOccupied` | Is Currently Occupied? | Boolean | Global |  |  |
| `IsLODAvail` | Is LOD Available? | Boolean | Global |  |  |
| `IsLandlordWorkDescriptionAvail` | Is Landlord Work Description Available? | Boolean | Global |  |  |
| `IsRoofAccessAvail` | Roof Access | Boolean | Global |  |  |
| `IsSignCriteriaAvail` | Is Sign Criteria Available? | Boolean | Global |  |  |
| `MonumentSignage` | Monument Signage? | Boolean | Global |  |  |
| `ParkingLotLighting` | Parking Lot Lighting | Boolean | Global |  |  |
| `PylonSignage` | Pylon Signage | Boolean | Global |  |  |
| `RecommendToREC` | Recommend to REC? | Boolean | Global |  |  |
| `TrafficSignalAccess` | Signalized Access | Boolean | Global |  |  |

### Text & notes (10)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AnchorTenants` | Anchor Tenants | Text | Global |  |  |
| `CurrentOrFormerTenants` | Current Or Former Tenants | Text | Global |  |  |
| `FacilityDescription` | Facility Description | Text | Global |  |  |
| `FacilityLocation` | Facility Location | Text | Global |  |  |
| `FacilityPriorUse` | Facility Prior Use | Text | Global |  |  |
| `NeighborhoodDescription` | Neighborhood Description | Text | Global |  |  |
| `SiteRatingExplanation` | Site Rating Explanation | Text | Global |  |  |
| `SpaceNumber` | Space Number | Text | Global |  |  |
| `TypeOfFixtures` | Type Of Fixtures | Text | Global |  |  |
| `WhichSides` | Which Building Sides | Text | Global |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Site Survey ClientID | Text | Global | yes |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
