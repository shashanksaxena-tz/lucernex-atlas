# SiteSurvey — Data Fields

Site-selection/demographic evaluation data for a candidate location — household income and count at 1/3/5-mile radii, median age, and condition-code ratings, used during real estate site selection before a lease is signed. 78 Global fields under its own Site Survey group; the repeated '-1 Mile/-3 Miles/-5 Miles' field triples show Lucernex bakes fixed trade-area radii into the schema rather than storing a single configurable radius.

**Table Association:** `SiteSurvey` &nbsp;·&nbsp; **Total fields:** 78 (Global: 78, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Site Survey / Audit Info |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Site Survey / Audit Info |
| Household Avg Income-1 Mile | `HouseholdAvgIncome1Mile` | `sTYPE_MONEY` | Global | No | No |  | Site Survey / Demographics |
| Household Avg Income-3 Miles | `HouseholdAvgIncome3Miles` | `sTYPE_MONEY` | Global | No | No |  | Site Survey / Demographics |
| Household Avg Income-5 Miles | `HouseholdAvgIncome5Miles` | `sTYPE_MONEY` | Global | No | No |  | Site Survey / Demographics |
| Households-1 Mile | `Households1Mile` | `sTYPE_NUMBER` | Global | No | No |  | Site Survey / Demographics |
| Households-3 Miles | `Households3Miles` | `sTYPE_NUMBER` | Global | No | No |  | Site Survey / Demographics |
| Households-5 Miles | `Households5Miles` | `sTYPE_NUMBER` | Global | No | No |  | Site Survey / Demographics |
| Median Age-1 Mile | `MedianAge1Mile` | `sTYPE_NUMBER` | Global | No | No |  | Site Survey / Demographics |
| Median Age-3 Miles | `MedianAge3Miles` | `sTYPE_NUMBER` | Global | No | No |  | Site Survey / Demographics |
| Median Age-5 Miles | `MedianAge5Miles` | `sTYPE_NUMBER` | Global | No | No |  | Site Survey / Demographics |
| Percent Female-1 Mile | `PercentFemale1Mile` | `sTYPE_NUMBER` | Global | No | No |  | Site Survey / Demographics |
| Percent Female-3 Miles | `PercentFemale3Miles` | `sTYPE_NUMBER` | Global | No | No |  | Site Survey / Demographics |
| Percent Female-5 Miles | `PercentFemale5Miles` | `sTYPE_NUMBER` | Global | No | No |  | Site Survey / Demographics |
| Percent Male-1 Mile | `PercentMale1Mile` | `sTYPE_NUMBER` | Global | No | No |  | Site Survey / Demographics |
| Percent Male-3 Miles | `PercentMale3Miles` | `sTYPE_NUMBER` | Global | No | No |  | Site Survey / Demographics |
| Percent Male-5 Miles | `PercentMale5Miles` | `sTYPE_NUMBER` | Global | No | No |  | Site Survey / Demographics |
| Population-1 Mile | `Population1Mile` | `sTYPE_NUMBER` | Global | No | No |  | Site Survey / Demographics |
| Population-3 Miles | `Population3Miles` | `sTYPE_NUMBER` | Global | No | No |  | Site Survey / Demographics |
| Population-5 Miles | `Population5Miles` | `sTYPE_NUMBER` | Global | No | No |  | Site Survey / Demographics |
| Accessibility | `CodeLocationAccessID` | `sCODE_LOCATION_ACCESS` | Global | No | No |  | Site Survey / Site Survey Info |
| Age Of HVAC Units | `AgeOfHVACUnits` | `sTYPE_NUMBER` | Global | No | No |  | Site Survey / Site Survey Info |
| Anchor Tenants | `AnchorTenants` | `sTYPE_TEXT` | Global | No | No |  | Site Survey / Site Survey Info |
| Approx Building Length | `ApproxBuildingLength` | `sTYPE_NUMBER` | Global | No | No |  | Site Survey / Site Survey Info |
| Approx Building Width | `ApproxBuildingWidth` | `sTYPE_NUMBER` | Global | No | No |  | Site Survey / Site Survey Info |
| Building Area Unit | `CodeBuildingAreaUnitID` | `sCODE_BUILDING_AREA_UNIT` | Global | No | No |  | Site Survey / Site Survey Info |
| Building Signage? | `BuildingSignage` | `sTYPE_BOOLEAN` | Global | No | No |  | Site Survey / Site Survey Info |
| Canopy Lighting? | `CanopyLighting` | `sTYPE_BOOLEAN` | Global | No | No |  | Site Survey / Site Survey Info |
| Ceiling Condition | `CodeCeilingConditionID` | `sCODE_CONDITION` | Global | No | No |  | Site Survey / Site Survey Info |
| Current Or Former Tenants | `CurrentOrFormerTenants` | `sTYPE_TEXT` | Global | No | No |  | Site Survey / Site Survey Info |
| Current Zoning | `CodeCurrentZoningID` | `sCODE_ZONING` | Global | No | No |  | Site Survey / Site Survey Info |
| Existing Floor Condition | `CodeFloorConditionID` | `sCODE_CONDITION` | Global | No | No |  | Site Survey / Site Survey Info |
| Facility Condition | `CodeFacilityConditionID` | `sCODE_CONDITION` | Global | No | No |  | Site Survey / Site Survey Info |
| Facility Description | `FacilityDescription` | `sTYPE_TEXTAREA` | Global | No | No |  | Site Survey / Site Survey Info |
| Facility Location | `FacilityLocation` | `sTYPE_TEXT` | Global | No | No |  | Site Survey / Site Survey Info |
| Facility Prior Use | `FacilityPriorUse` | `sTYPE_TEXT` | Global | No | No |  | Site Survey / Site Survey Info |
| Fire Sprinkler? | `FireSprinkler` | `sTYPE_BOOLEAN` | Global | No | No |  | Site Survey / Site Survey Info |
| Handicap Accessible? | `HandicapAccessible` | `sTYPE_BOOLEAN` | Global | No | No |  | Site Survey / Site Survey Info |
| Is Building Plan Available? | `IsBuildingPlanAvail` | `sTYPE_BOOLEAN` | Global | No | No |  | Site Survey / Site Survey Info |
| Is CLEC Available? | `IsCLECAvail` | `sTYPE_BOOLEAN` | Global | No | No |  | Site Survey / Site Survey Info |
| Is Construction Criteria Available? | `IsConstructionCriteriaAvail` | `sTYPE_BOOLEAN` | Global | No | No |  | Site Survey / Site Survey Info |
| Is Currently Occupied? | `IsCurrentlyOccupied` | `sTYPE_CHECKBOX` | Global | No | No |  | Site Survey / Site Survey Info |
| Is LOD Available? | `IsLODAvail` | `sTYPE_BOOLEAN` | Global | No | No |  | Site Survey / Site Survey Info |
| Is Landlord Work Description Available? | `IsLandlordWorkDescriptionAvail` | `sTYPE_BOOLEAN` | Global | No | No |  | Site Survey / Site Survey Info |
| Is Sign Criteria Available? | `IsSignCriteriaAvail` | `sTYPE_BOOLEAN` | Global | No | No |  | Site Survey / Site Survey Info |
| Land Area Unit | `CodeLandAreaUnitID` | `sCODE_LAND_AREA_UNIT` | Global | No | No |  | Site Survey / Site Survey Info |
| Monument Signage? | `MonumentSignage` | `sTYPE_BOOLEAN` | Global | No | No |  | Site Survey / Site Survey Info |
| Neighborhood Description | `NeighborhoodDescription` | `sTYPE_TEXT` | Global | No | No |  | Site Survey / Site Survey Info |
| Number Of Amps | `NumberOfAmps` | `sTYPE_NUMBER` | Global | No | No |  | Site Survey / Site Survey Info |
| Number Of Building Sides | `NumberOfBuildingSides` | `sTYPE_NUMBER` | Global | No | No |  | Site Survey / Site Survey Info |
| Number Of Electrical Panels | `NumberOfElectricalPanels` | `sTYPE_NUMBER` | Global | No | No |  | Site Survey / Site Survey Info |
| Number Of Fixtures | `NumberOfFixtures` | `sTYPE_NUMBER` | Global | No | No |  | Site Survey / Site Survey Info |
| Number Of Floors | `NumberOfFloors` | `sTYPE_NUMBER` | Global | No | No |  | Site Survey / Site Survey Info |
| Number Of HVAC Units | `NumberOfHVACUnits` | `sTYPE_NUMBER` | Global | No | No |  | Site Survey / Site Survey Info |
| Number Of Restrooms | `NumberOfRestrooms` | `sTYPE_NUMBER` | Global | No | No |  | Site Survey / Site Survey Info |
| Parking Lot Conditions | `CodeParkingLotConditionID` | `sCODE_CONDITION` | Global | No | No |  | Site Survey / Site Survey Info |
| Parking Lot Lighting | `ParkingLotLighting` | `sTYPE_BOOLEAN` | Global | No | No |  | Site Survey / Site Survey Info |
| Pylon Signage | `PylonSignage` | `sTYPE_BOOLEAN` | Global | No | No |  | Site Survey / Site Survey Info |
| Recommend to REC? | `RecommendToREC` | `sTYPE_CHECKBOX` | Global | No | No |  | Site Survey / Site Survey Info |
| Required Zoning | `CodeRequiredZoningID` | `sCODE_ZONING` | Global | No | No |  | Site Survey / Site Survey Info |
| Roof Access | `IsRoofAccessAvail` | `sTYPE_BOOLEAN` | Global | No | No |  | Site Survey / Site Survey Info |
| Seating Capacity | `SeatingCapacity` | `sTYPE_NUMBER` | Global | No | No |  | Site Survey / Site Survey Info |
| Sent To Construction Date | `SentToConstructionDate` | `sTYPE_DATE` | Global | No | No |  | Site Survey / Site Survey Info |
| Signalized Access | `TrafficSignalAccess` | `sTYPE_BOOLEAN` | Global | No | No |  | Site Survey / Site Survey Info |
| Site Rating | `CodeSiteRatingID` | `sCODE_SITE_RATING` | Global | No | No |  | Site Survey / Site Survey Info |
| Site Rating Explanation | `SiteRatingExplanation` | `sTYPE_TEXTAREA` | Global | No | No |  | Site Survey / Site Survey Info |
| Site Survey ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Site Survey / Site Survey Info |
| Site Suvery RecID | `SiteSurveyID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Site Survey / Site Survey Info |
| Space Number | `SpaceNumber` | `sTYPE_TEXT` | Global | No | No |  | Site Survey / Site Survey Info |
| Trade Area Quality | `CodeTradeAreaQualityID` | `sCODE_CONDITION` | Global | No | No |  | Site Survey / Site Survey Info |
| Traffic Count | `TrafficCount` | `sTYPE_NUMBER` | Global | No | No |  | Site Survey / Site Survey Info |
| Type Of Fixtures | `TypeOfFixtures` | `sTYPE_TEXT` | Global | No | No |  | Site Survey / Site Survey Info |
| Usable Land Area | `UsableLandArea` | `sTYPE_NUMBER` | Global | No | No |  | Site Survey / Site Survey Info |
| Usable Parcel Area | `UsableParcelArea` | `sTYPE_NUMBER` | Global | No | No |  | Site Survey / Site Survey Info |
| Vehicle Access Condition | `CodeVehicleAccessConditionID` | `sCODE_CONDITION` | Global | No | No |  | Site Survey / Site Survey Info |
| Visibility | `CodeVisibilityConditionID` | `sCODE_CONDITION` | Global | No | No |  | Site Survey / Site Survey Info |
| Weight Of HVAC Units | `WeightOfHVACUnits` | `sTYPE_NUMBER` | Global | No | No |  | Site Survey / Site Survey Info |
| Which Building Sides | `WhichSides` | `sTYPE_TEXT` | Global | No | No |  | Site Survey / Site Survey Info |
