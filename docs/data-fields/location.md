# Location — Data Fields

A general site/location record — address and geocoding fields (Latitude, Longitude) plus percentage-based site metrics — used as a lighter-weight alternative to Facility for sites that are tracked before or without a full facility record. 66 fields (61 Global, 5 Firm) under its own Location group.

**Table Association:** `Location` &nbsp;·&nbsp; **Total fields:** 66 (Global: 61, Firm: 5)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| City | `City` | `sTYPE_TEXT` | Global | No | No |  | Location / Address Info |
| Country | `CountryID` | `sTYPE_COUNTRY` | Global | No | No |  | Location / Address Info |
| County | `Firm_County` | `sTYPE_TEXT` | Firm | No | No |  | Location / Address Info |
| Cross Street #1 | `CrossStreet1` | `sTYPE_TEXT` | Global | No | No |  | Location / Address Info |
| Cross Street #2 | `CrossStreet2` | `sTYPE_TEXT` | Global | No | No |  | Location / Address Info |
| Full Address | `HTMLAddress` | `sTYPE_TEXT` | Global | No | No |  | Location / Address Info |
| Jurisdiction | `JurisdictionID` | `sTYPE_JURISDICTION` | Global | No | No |  | Location / Address Info |
| Latitude | `LatitudeDegrees` | `sTYPE_NUMBER_FRACTION6DIGITS` | Global | No | No |  | Location / Address Info |
| Longitude | `LongitudeDegrees` | `sTYPE_NUMBER_FRACTION6DIGITS` | Global | No | No |  | Location / Address Info |
| Postal Code | `PostalCode` | `sTYPE_POSTALCODE` | Global | No | No |  | Location / Address Info |
| State | `IStateProvinceCountryID` | `sTYPE_STATE_PROVINCE` | Global | No | No |  | Location / Address Info |
| Street Address #1 | `StreetAddress1` | `sTYPE_TEXT` | Global | No | No |  | Location / Address Info |
| Street Address #2 | `StreetAddress2` | `sTYPE_TEXT` | Global | No | No |  | Location / Address Info |
| Street Address #3 | `StreetAddress3` | `sTYPE_TEXT` | Global | No | No |  | Location / Address Info |
| Street Address #4 | `StreetAddress4` | `sTYPE_TEXT` | Global | No | No |  | Location / Address Info |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Location / Audit Info |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Location / Audit Info |
| ASG Center ID | `EDGE_ASGCenterID` | `sTYPE_NUMBER` | Firm | No | No |  | Location / Location Info |
| Accounting Number | `AccountingNumber` | `sTYPE_TEXT` | Global | No | No |  | Location / Location Info |
| Budget Template | `BudgetTemplateID` | `sTYPE_BUDGET_TEMPLATE` | Global | No | No |  | Location / Location Info |
| Building Area Unit | `CodeBuildingAreaUnitID` | `sCODE_BUILDING_AREA_UNIT` | Global | No | No |  | Location / Location Info |
| Center Name | `Firm_CenterName` | `sTYPE_TEXT` | Firm | No | No |  | Location / Location Info |
| Complex Name | `ComplexID` | `sTYPE_COMPLEX` | Global | No | No |  | Location / Location Info |
| Currency Type | `CodeCurrencyTypeID` | `sCODE_CURRENCY_TYPE` | Global | No | No |  | Location / Location Info |
| Description | `ProjectDescription` | `sTYPE_TEXT` | Global | No | No |  | Location / Location Info |
| Developer | `Firm_Developer` | `sTYPE_TEXT` | Firm | No | No |  | Location / Location Info |
| EC Tax Rate #1 | `EquipContractTaxRate1` | `sTYPE_PERCENTAGE` | Global | No | No |  | Location / Location Info |
| EC Tax Rate #2 | `EquipContractTaxRate2` | `sTYPE_PERCENTAGE` | Global | No | No |  | Location / Location Info |
| EC Tax Rate #3 | `EquipContractTaxRate3` | `sTYPE_PERCENTAGE` | Global | No | No |  | Location / Location Info |
| EC Tax Rate #4 | `EquipContractTaxRate4` | `sTYPE_PERCENTAGE` | Global | No | No |  | Location / Location Info |
| Grand Opening Date | `Firm_GrandOpeningDate` | `sTYPE_DATE` | Firm | No | No |  | Location / Location Info |
| Gross Lease Area | `GrossLeaseArea` | `sTYPE_AREA` | Global | No | No |  | Location / Location Info |
| Is Inactive? | `Inactive` | `sTYPE_CHECKBOX` | Global | Yes | No |  | Location / Location Info |
| Land Area Unit | `CodeLandAreaUnitID` | `sCODE_LAND_AREA_UNIT` | Global | No | No |  | Location / Location Info |
| Location Category | `CodeLocationCategoryID` | `sCODE_LOCATION_CATEGORY` | Global | No | No |  | Location / Location Info |
| Location ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Location / Location Info |
| Location Group | `CodeLocationGroupID` | `sCODE_LOCATION_GROUP` | Global | No | No |  | Location / Location Info |
| Location ID | `ClientEntityID` | `sTYPE_TEXT` | Global | No | No |  | Location / Location Info |
| Location Name | `LocationName` | `sTYPE_ENTITY_NAME` | Global | Yes | No |  | Location / Location Info |
| Location Parcel Area | `LocationParcelArea` | `sTYPE_AREA` | Global | No | No |  | Location / Location Info |
| Location RecID | `LocationID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Location / Location Info |
| Location Status | `CodeLocationStatusID` | `sCODE_LOCATION_STATUS` | Global | No | No |  | Location / Location Info |
| Location Type | `CodeLocationTypeID` | `sCODE_LOCATION_TYPE` | Global | No | No |  | Location / Location Info |
| Location UUID | `UUID` | `sTYPE_TEXT` | Global | No | No |  | Location / Location Info |
| Location Use | `CodeLocationUseID` | `sCODE_LOCATION_USE` | Global | No | No |  | Location / Location Info |
| Market Area | `CodeMarketAreaID` | `sCODE_MARKET_AREA` | Global | No | No |  | Location / Location Info |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Location / Location Info |
| Open Year | `OpenYear` | `sTYPE_DROPDOWN_YEAR` | Global | No | No |  | Location / Location Info |
| Organization | `OrganizationID` | `sTYPE_ORGANIZATION` | Global | No | No |  | Location / Location Info |
| Out Of Date Days | `OutOfDateDays` | `sTYPE_NUMBER` | Global | No | No |  | Location / Location Info |
| Portfolio | `ProgramID` | `sTYPE_PROGRAM` | Global | Yes | No |  | Location / Location Info |
| RE Tax Rate #1 | `TaxRate1` | `sTYPE_PERCENTAGE` | Global | No | No |  | Location / Location Info |
| RE Tax Rate #2 | `TaxRate2` | `sTYPE_PERCENTAGE` | Global | No | No |  | Location / Location Info |
| RE Tax Rate #3 | `TaxRate3` | `sTYPE_PERCENTAGE` | Global | No | No |  | Location / Location Info |
| RE Tax Rate #4 | `TaxRate4` | `sTYPE_PERCENTAGE` | Global | No | No |  | Location / Location Info |
| Region | `RegionID` | `sTYPE_REGION` | Global | No | No |  | Location / Location Info |
| Schedule Creation Method | `TaskCreationMethod` | `sTYPE_TASK_CREATION_METHOD` | Global | Yes | No |  | Location / Location Info |
| Sub Area #1 | `CodeSubArea1ID` | `sCODE_AREA` | Global | No | No |  | Location / Location Info |
| Sub Area #2 | `CodeSubArea2ID` | `sCODE_AREA` | Global | No | No |  | Location / Location Info |
| Sub Area #3 | `CodeSubArea3ID` | `sCODE_AREA` | Global | No | No |  | Location / Location Info |
| Sub Region #1 | `CodeSubRegion1ID` | `sCODE_REGION` | Global | No | No |  | Location / Location Info |
| Sub Region #2 | `CodeSubRegion2ID` | `sCODE_REGION` | Global | No | No |  | Location / Location Info |
| Sub Region #3 | `CodeSubRegion3ID` | `sCODE_REGION` | Global | No | No |  | Location / Location Info |
| Third Party Warehouse | `ThirdPartyWarehouse` | `sTYPE_TEXT` | Global | No | No |  | Location / Location Info |
| Third Party Warehouse Area | `ThirdPartyWarehouseArea` | `sTYPE_AREA` | Global | No | No |  | Location / Location Info |
| Time Zone | `TimeZone` | `sTYPE_TIMEZONE` | Global | No | No |  | Location / Location Info |
