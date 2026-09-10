# Facility — Data Fields

The physical property/building record — address fields (Street Address #1-3, City, State, Postal Code, Jurisdiction) plus facility-level dates and area figures. 89 fields (88 Global, 1 Firm) under its own top-level Facility group; this is the most 'plain real estate' entity in the catalog, closer to a CRM property record than a financial one, which is reflected in the dominance of `TEXT` and `DATE` field types over `MONEY`.

**Table Association:** `Facility` &nbsp;·&nbsp; **Total fields:** 89 (Global: 88, Firm: 1)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| City | `City` | `sTYPE_TEXT` | Global | No | No |  | Facility / Address Info |
| Country | `CountryID` | `sTYPE_COUNTRY` | Global | No | No |  | Facility / Address Info |
| Full Address | `HTMLAddress` | `sTYPE_TEXT` | Global | No | No |  | Facility / Address Info |
| Jurisdiction | `JurisdictionID` | `sTYPE_JURISDICTION` | Global | No | No |  | Facility / Address Info |
| Postal Code | `PostalCode` | `sTYPE_POSTALCODE` | Global | No | No |  | Facility / Address Info |
| State | `IStateProvinceCountryID` | `sTYPE_STATE_PROVINCE` | Global | No | No |  | Facility / Address Info |
| Street Address | `StreetAddress` | `sTYPE_TEXT` | Global | No | No |  | Facility / Address Info |
| Street Address #1 | `StreetAddress1` | `sTYPE_TEXT` | Global | No | No |  | Facility / Address Info |
| Street Address #2 | `StreetAddress2` | `sTYPE_TEXT` | Global | No | No |  | Facility / Address Info |
| Street Address #3 | `StreetAddress3` | `sTYPE_TEXT` | Global | No | No |  | Facility / Address Info |
| Street Address #4 | `StreetAddress4` | `sTYPE_TEXT` | Global | No | No |  | Facility / Address Info |
| Use Location Address | `UseLocationAddress` | `sTYPE_CHECKBOX` | Global | Yes | No |  | Facility / Address Info |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Facility / Audit Info |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Facility / Audit Info |
| Actual/Forecast Delivery Date | `ActualEndDate` | `sTYPE_DATE` | Global | No | No |  | Facility / Facility Info |
| Baseline End date | `BaselineEndDate` | `sTYPE_DATE` | Global | No | No |  | Facility / Facility Info |
| Baseline Start Date | `BaselineStartDate` | `sTYPE_DATE` | Global | No | No |  | Facility / Facility Info |
| Behind Schedule Days | `BehindScheduleDays` | `sTYPE_NUMBER` | Global | No | No |  | Facility / Facility Info |
| Building Area Unit | `CodeBuildingAreaUnitID` | `sCODE_BUILDING_AREA_UNIT` | Global | No | No |  | Facility / Facility Info |
| Close Date | `CloseDate` | `sTYPE_DATE` | Global | No | No |  | Facility / Facility Info |
| Construction Date | `ConstructionDate` | `sTYPE_DATE` | Global | No | No |  | Facility / Facility Info |
| Construction Phase Status | `ConstructionPhaseStatus` | `sTYPE_TEXT` | Global | No | No |  | Facility / Facility Info |
| Construction Type | `CodeConstructionTypeID` | `sCODE_CONSTRUCTION_TYPE` | Global | No | No |  | Facility / Facility Info |
| Days Until Open | `DaysUntilOpen` | `sTYPE_NUMBER` | Global | No | No |  | Facility / Facility Info |
| Deal Type | `CodeDealTypeID` | `sCODE_DEAL_TYPE` | Global | No | No |  | Facility / Facility Info |
| Defined Field #1 | `DefinedField1` | `sTYPE_TEXT` | Global | No | No |  | Facility / Facility Info |
| Defined Field #2 | `DefinedField2` | `sTYPE_TEXT` | Global | No | No |  | Facility / Facility Info |
| Depth | `Depth` | `sTYPE_AREA` | Global | No | No |  | Facility / Facility Info |
| Description | `ProjectDescription` | `sTYPE_TEXTAREA` | Global | No | No |  | Facility / Facility Info |
| Design Phase Status | `DesignPhaseStatus` | `sTYPE_TEXT` | Global | No | No |  | Facility / Facility Info |
| Distribution Center | `CodeDistributionCenterID` | `sCODE_DISTRIBUTION_CENTER` | Global | No | No |  | Facility / Facility Info |
| Distribution Center Area | `DistributionCenterArea` | `sTYPE_AREA` | Global | No | No |  | Facility / Facility Info |
| Entity Photo | `EntityPhoto` | `sTYPE_TEXT` | Global | No | No |  | Facility / Facility Info |
| Entity RecID | `ProjectEntityID` | `sTYPE_UNFORMATTED_NUMBER` | Global | Yes | No |  | Facility / Facility Info |
| Facility Category | `CodeFacilityCategoryID` | `sCODE_FACILITY_CATEGORY` | Global | No | No |  | Facility / Facility Info |
| Facility ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Facility / Facility Info |
| Facility Group | `CodeFacilityGroupID` | `sCODE_FACILITY_GROUP` | Global | No | No |  | Facility / Facility Info |
| Facility ID | `ClientEntityID` | `sTYPE_TEXT` | Global | No | No |  | Facility / Facility Info |
| Facility Name | `FacilityName` | `sTYPE_ENTITY_NAME` | Global | Yes | No |  | Facility / Facility Info |
| Facility RecID | `FacilityID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Facility / Facility Info |
| Facility Status | `CodeFacilityStatusID` | `sCODE_FACILITY_STATUS` | Global | No | No |  | Facility / Facility Info |
| Facility Type | `CodeFacilityTypeID` | `sCODE_FACILITY_TYPE` | Global | No | No |  | Facility / Facility Info |
| Facility UUID | `UUID` | `sTYPE_TEXT` | Global | No | No |  | Facility / Facility Info |
| Facility Use | `CodeFacilityUseID` | `sCODE_FACILITY_USE` | Global | No | No |  | Facility / Facility Info |
| Frontage | `Frontage` | `sTYPE_AREA` | Global | No | No |  | Facility / Facility Info |
| Gross Area | `GrossArea` | `sTYPE_AREA` | Global | No | No |  | Facility / Facility Info |
| Hours Of Operation | `HoursOfOperation` | `sTYPE_TEXTAREA` | Global | No | No |  | Facility / Facility Info |
| Is Dead? | `IsDead` | `sTYPE_CHECKBOX` | Global | Yes | No |  | Facility / Facility Info |
| Is Inactive? | `Inactive` | `sTYPE_CHECKBOX` | Global | Yes | No |  | Facility / Facility Info |
| Issues And Alerts | `IssuesAndAlerts` | `sTYPE_TEXT` | Global | No | No |  | Facility / Facility Info |
| Last Years Annual Sales | `LastYearsAnnualSales` | `sTYPE_MONEY` | Global | No | No |  | Facility / Facility Info |
| Location | `LocationID` | `sTYPE_LOCATION` | Global | Yes | No |  | Facility / Facility Info |
| Market Area | `CodeMarketAreaID` | `sCODE_MARKET_AREA` | Global | Yes | No |  | Facility / Facility Info |
| Market Potential | `CodeDesc_CodeMarketAreaID` | `sCODE_MARKET_AREA` | Global | No | No |  | Facility / Facility Info |
| Market Type | `CodeMarketTypeID` | `sCODE_MARKET_TYPE` | Global | No | No |  | Facility / Facility Info |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Facility / Facility Info |
| Open Date | `OpenDate` | `sTYPE_DATE` | Global | No | No |  | Facility / Facility Info |
| Open year | `OpenYear` | `sTYPE_DROPDOWN_YEAR` | Global | No | No |  | Facility / Facility Info |
| Opening Project | `OpeningProjectPEID` | `sTYPE_ACTIVEINACTIVE_PROJECT` | Global | No | No |  | Facility / Facility Info |
| Operating Status | `OperatingStatus` | `sTYPE_TEXT` | Global | Yes | No |  | Facility / Facility Info |
| Operations Phase Status | `OperationsPhaseStatus` | `sTYPE_TEXT` | Global | No | No |  | Facility / Facility Info |
| Original Delivery Date | `ExpectedEndDate` | `sTYPE_DATE` | Global | No | No |  | Facility / Facility Info |
| Original Delivery Month/Year | `ExpectedEndDate` | `sTYPE_MONTHS_YEAR` | Global | No | No |  | Facility / Facility Info |
| Original Delivery Period/Year | `ExpectedEndDate` | `sTYPE_PERIOD_YEAR` | Global | No | No |  | Facility / Facility Info |
| Original Delivery Qtr/Yr | `ExpectedEndDate` | `sTYPE_QUARTERS_YEAR` | Global | No | No |  | Facility / Facility Info |
| Out Of Date Days | `OutOfDateDays` | `sTYPE_NUMBER` | Global | No | No |  | Facility / Facility Info |
| Parent Region | `RootRegionID` | `sTYPE_ROOT_REGION` | Global | No | No |  | Facility / Facility Info |
| Phone | `Phone` | `sTYPE_PHONE` | Global | No | No |  | Facility / Facility Info |
| Portfolio | `ProgramID` | `sTYPE_PROGRAM` | Global | Yes | No |  | Facility / Facility Info |
| Possession Phase Status | `PossessionPhaseStatus` | `sTYPE_TEXT` | Global | No | No |  | Facility / Facility Info |
| Project Managers | `ManagerIDList` | `sTYPE_PROJECT_MANAGER` | Global | No | No |  | Facility / Facility Info |
| Project Status | `CurrentPhaseStatus` | `sTYPE_TEXT` | Global | No | No |  | Facility / Facility Info |
| Project Type | `CodeProjectTypeID` | `sCODE_PROJECT_TYPE` | Global | No | No |  | Facility / Facility Info |
| Prototype | `PrototypeID` | `sTYPE_PROTOTYPE` | Global | No | No |  | Facility / Facility Info |
| RE Planner Open Date | `SlotEndDate` | `sTYPE_DATE` | Global | No | No |  | Facility / Facility Info |
| Real Estate Phase Status | `RealEstatePhaseStatus` | `sTYPE_TEXT` | Global | No | No |  | Facility / Facility Info |
| Real Estate Type | `CodeDesc_CodeProjectTypeID` | `sCODE_PROJECT_TYPE` | Global | No | No |  | Facility / Facility Info |
| Region | `RegionID` | `sTYPE_REGION` | Global | Yes | No |  | Facility / Facility Info |
| Related Facility Entities | `RelatedEntities` | `sTYPE_TEXT` | Global | No | No |  | Facility / Facility Info |
| Remodel Date | `RemodelDate` | `sTYPE_DATE` | Global | No | No |  | Facility / Facility Info |
| Rentable Area | `RentableArea` | `sTYPE_AREA` | Global | No | No |  | Facility / Facility Info |
| Schedule Creation Method | `TaskCreationMethod` | `sTYPE_TASK_CREATION_METHOD` | Global | Yes | No |  | Facility / Facility Info |
| Sequence Number | `SequenceNumber` | `sTYPE_NUMBER` | Global | No | No |  | Facility / Facility Info |
| Space Number | `Firm_SpaceNumber` | `sTYPE_TEXT` | Firm | No | No |  | Facility / Facility Info |
| Sub Region | `SubRegionID` | `sTYPE_SUBREGION` | Global | No | No |  | Facility / Facility Info |
| Third Party Warehouse | `ThirdPartyWarehouse` | `sTYPE_TEXT` | Global | No | No |  | Facility / Facility Info |
| Time Zone | `TimeZone` | `sTYPE_TIMEZONE` | Global | No | No |  | Facility / Facility Info |
| Trade Area | `TradeArea` | `sTYPE_TEXT` | Global | No | No |  | Facility / Facility Info |
| Usable Area | `UsableArea` | `sTYPE_AREA` | Global | No | No |  | Facility / Facility Info |
