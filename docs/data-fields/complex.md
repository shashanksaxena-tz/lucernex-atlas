# Complex — Data Fields

A multi-building property complex/campus record sitting above Facility in the property hierarchy — complex-level classification and status fields plus a linked Person (likely site or leasing contact). 45 Global fields under its own Complex group.

**Table Association:** `Complex` &nbsp;·&nbsp; **Total fields:** 45 (Global: 45, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Complex / Audit Info |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Complex / Audit Info |
| Building Area Unit | `CodeBuildingAreaUnitID` | `sCODE_BUILDING_AREA_UNIT` | Global | No | No |  | Complex / Complex Info |
| City | `City` | `sTYPE_TEXT` | Global | No | No |  | Complex / Complex Info |
| Client Number | `ClientNumber` | `sTYPE_TEXT` | Global | No | No |  | Complex / Complex Info |
| Complex Class | `CodeComplexClassID` | `sCODE_BUILDING_CLASS` | Global | No | No |  | Complex / Complex Info |
| Complex ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Complex / Complex Info |
| Complex Name | `ComplexName` | `sTYPE_TEXT` | Global | Yes | No |  | Complex / Complex Info |
| Complex RecID | `ComplexID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Complex / Complex Info |
| Complex Status | `CodeComplexStatusID` | `sCODE_COMPLEX_STATUS` | Global | No | No |  | Complex / Complex Info |
| Complex Type | `CodeComplexTypeID` | `sCODE_COMPLEX_TYPE` | Global | No | No |  | Complex / Complex Info |
| Country | `CountryID` | `sTYPE_COUNTRY` | Global | No | No |  | Complex / Complex Info |
| Developer | `DeveloperID` | `sTYPE_PERSON` | Global | No | No |  | Complex / Complex Info |
| Expansion Plan Date | `ExpansionPlanDate` | `sTYPE_DATE` | Global | No | No |  | Complex / Complex Info |
| GLA Excluding Anchors | `GLAExcludingAnchors` | `sTYPE_AREA` | Global | No | No |  | Complex / Complex Info |
| Gross Lease Area | `GrossLeaseArea` | `sTYPE_AREA` | Global | No | No |  | Complex / Complex Info |
| Has Food Court? | `HasFoodCourt` | `sTYPE_CHECKBOX` | Global | No | No |  | Complex / Complex Info |
| Hours Of Operation | `HoursOfOperation` | `sTYPE_TEXTAREA` | Global | No | No |  | Complex / Complex Info |
| Is Enclosed? | `IsEnclosed` | `sTYPE_CHECKBOX` | Global | No | No |  | Complex / Complex Info |
| Is Expansion Planned? | `IsExpansionPlanned` | `sTYPE_CHECKBOX` | Global | No | No |  | Complex / Complex Info |
| Is Renovation Planned? | `IsRenovationPlanned` | `sTYPE_CHECKBOX` | Global | No | No |  | Complex / Complex Info |
| Is Space Available? | `IsSpaceAvailable` | `sTYPE_CHECKBOX` | Global | No | No |  | Complex / Complex Info |
| Jurisdiction | `JurisdictionID` | `sTYPE_JURISDICTION` | Global | No | No |  | Complex / Complex Info |
| Landlord | `LandlordID` | `sTYPE_PERSON` | Global | No | No |  | Complex / Complex Info |
| Last Renovated | `LastRenovated` | `sTYPE_TEXT` | Global | No | No |  | Complex / Complex Info |
| Nearest Competition | `NearestCompetition` | `sTYPE_TEXT` | Global | No | No |  | Complex / Complex Info |
| Notable Tenants | `NotableTenants` | `sTYPE_TEXTAREA` | Global | No | No |  | Complex / Complex Info |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Complex / Complex Info |
| Number Levels | `NumberLevels` | `sTYPE_NUMBER` | Global | No | No |  | Complex / Complex Info |
| Number Outparcels | `NumberOutparcels` | `sTYPE_NUMBER` | Global | No | No |  | Complex / Complex Info |
| Number Parking Spaces | `NumberParkingSpaces` | `sTYPE_NUMBER` | Global | No | No |  | Complex / Complex Info |
| Number Stores | `NumberStores` | `sTYPE_NUMBER` | Global | No | No |  | Complex / Complex Info |
| Occupancy Percentage | `OccupancyPercentage` | `sTYPE_PERCENTAGE` | Global | No | No |  | Complex / Complex Info |
| Phone | `Phone` | `sTYPE_TEXT` | Global | No | No |  | Complex / Complex Info |
| Postal Code | `PostalCode` | `sTYPE_POSTALCODE` | Global | No | No |  | Complex / Complex Info |
| Property Manager | `PropertyManagerID` | `sTYPE_PERSON` | Global | No | No |  | Complex / Complex Info |
| Renovation Plan Date | `RenovationPlanDate` | `sTYPE_DATE` | Global | No | No |  | Complex / Complex Info |
| Sales Per Area | `SalesPerArea` | `sTYPE_MONEY` | Global | No | No |  | Complex / Complex Info |
| State | `IStateProvinceCountryID` | `sTYPE_STATE_PROVINCE` | Global | No | No |  | Complex / Complex Info |
| Street Address #1 | `StreetAddress1` | `sTYPE_TEXT` | Global | No | No |  | Complex / Complex Info |
| Street Address #2 | `StreetAddress2` | `sTYPE_TEXT` | Global | No | No |  | Complex / Complex Info |
| Street Address #3 | `StreetAddress3` | `sTYPE_TEXT` | Global | No | No |  | Complex / Complex Info |
| Street Address #4 | `StreetAddress4` | `sTYPE_TEXT` | Global | No | No |  | Complex / Complex Info |
| Vacancy Rate | `VacancyRate` | `sTYPE_PERCENTAGE` | Global | No | No |  | Complex / Complex Info |
| Year Built | `YearBuilt` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Complex / Complex Info |
