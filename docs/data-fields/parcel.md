# Parcel — Data Fields

The land-parcel record, distinct from Facility (building) and Location (site) — address fields plus parcel-specific attributes like Demographic DMA linkage, used primarily for ground-lease and land-purchase scenarios and as the anchor for the large PropertyTax* family (Assessment, Bill, Summary, Appeal, ParcelAccess). 74 Global fields under its own Parcel group.

**Table Association:** `Parcel` &nbsp;·&nbsp; **Total fields:** 74 (Global: 74, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| City | `City` | `sTYPE_TEXT` | Global | No | No |  | Parcel / Address Info |
| Country | `CountryID` | `sTYPE_COUNTRY` | Global | No | No |  | Parcel / Address Info |
| Cross Street #1 | `CrossStreet1` | `sTYPE_TEXT` | Global | No | No |  | Parcel / Address Info |
| Cross Street #2 | `CrossStreet2` | `sTYPE_TEXT` | Global | No | No |  | Parcel / Address Info |
| Demographic DMA | `DemographicDMAID` | `sTYPE_DMA` | Global | No | No |  | Parcel / Address Info |
| Full Address | `HTMLAddress` | `sTYPE_TEXT` | Global | No | No |  | Parcel / Address Info |
| Jurisdiction | `JurisdictionID` | `sTYPE_JURISDICTION` | Global | No | No |  | Parcel / Address Info |
| Postal Code | `PostalCode` | `sTYPE_POSTALCODE` | Global | No | No |  | Parcel / Address Info |
| State | `IStateProvinceCountryID` | `sTYPE_STATE_PROVINCE` | Global | No | No |  | Parcel / Address Info |
| Street Address #1 | `StreetAddress1` | `sTYPE_TEXT` | Global | No | No |  | Parcel / Address Info |
| Street Address #2 | `StreetAddress2` | `sTYPE_TEXT` | Global | No | No |  | Parcel / Address Info |
| Street Address #3 | `StreetAddress3` | `sTYPE_TEXT` | Global | No | No |  | Parcel / Address Info |
| Street Address #4 | `StreetAddress4` | `sTYPE_TEXT` | Global | No | No |  | Parcel / Address Info |
| Use Location Address? | `UseLocationAddress` | `sTYPE_CHECKBOX` | Global | Yes | No |  | Parcel / Address Info |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Parcel / Audit Info |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Parcel / Audit Info |
| Acquired Date | `AcquiredDate` | `sTYPE_DATE` | Global | No | No |  | Parcel / Parcel Info |
| Block | `Block` | `sTYPE_TEXT` | Global | No | No |  | Parcel / Parcel Info |
| Complex Name | `ComplexID` | `sTYPE_COMPLEX` | Global | No | No |  | Parcel / Parcel Info |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | No | No |  | Parcel / Parcel Info |
| Currency Type | `CodeCurrencyTypeID` | `sCODE_CURRENCY_TYPE` | Global | No | No |  | Parcel / Parcel Info |
| Description | `ProjectDescription` | `sTYPE_TEXT` | Global | No | No |  | Parcel / Parcel Info |
| Expected End Date | `ExpectedEndDate` | `sTYPE_DATE` | Global | No | No |  | Parcel / Parcel Info |
| Facility | `FacilityID` | `sTYPE_FACILITY` | Global | No | No |  | Parcel / Parcel Info |
| Grid | `Grid` | `sTYPE_TEXT` | Global | No | No |  | Parcel / Parcel Info |
| Has Improvements? | `HasImprovements` | `sTYPE_CHECKBOX` | Global | No | No |  | Parcel / Parcel Info |
| Improvements Assessed Amount | `ImprovementsAsessedAmount` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Parcel Info |
| Improvements Value Amount | `ImprovementsValueAmount` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Parcel Info |
| Index Number | `IndexNumber` | `sTYPE_TEXT` | Global | No | No |  | Parcel / Parcel Info |
| Is Tax Exempt? | `IsTaxExempt` | `sTYPE_CHECKBOX` | Global | No | No |  | Parcel / Parcel Info |
| Land Area Unit | `CodeLandAreaUnitID` | `sCODE_LAND_AREA_UNIT` | Global | No | No |  | Parcel / Parcel Info |
| Land Assessed Amount | `LandAssessedAmount` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Parcel Info |
| Land Value Amount | `LandValueAmount` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Parcel Info |
| Location | `LocationID` | `sTYPE_LOCATION` | Global | Yes | No |  | Parcel / Parcel Info |
| Lot | `Lot` | `sTYPE_TEXT` | Global | No | No |  | Parcel / Parcel Info |
| Master Parcel | `MasterParcelID` | `sTYPE_PARCEL` | Global | No | No |  | Parcel / Parcel Info |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Parcel / Parcel Info |
| Open Year | `OpenYear` | `sTYPE_DROPDOWN_YEAR` | Global | No | No |  | Parcel / Parcel Info |
| Organization | `OrganizationID` | `sTYPE_ORGANIZATION` | Global | No | No |  | Parcel / Parcel Info |
| Other Assessed Amount | `OtherAssessedAmount` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Parcel Info |
| Other Value Amount | `OtherValueAmount` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Parcel Info |
| Out Of Date Days | `OutOfDateDays` | `sTYPE_NUMBER` | Global | No | No |  | Parcel / Parcel Info |
| Owner Name | `OwnerName` | `sTYPE_TEXT` | Global | No | No |  | Parcel / Parcel Info |
| Parcel Area | `ParcelArea` | `sTYPE_AREA` | Global | No | No |  | Parcel / Parcel Info |
| Parcel Category | `CodeParcelCategoryID` | `sCODE_PARCEL_CATEGORY` | Global | No | No |  | Parcel / Parcel Info |
| Parcel ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Parcel / Parcel Info |
| Parcel Group | `CodeParcelGroupID` | `sCODE_PARCEL_GROUP` | Global | No | No |  | Parcel / Parcel Info |
| Parcel ID | `ClientEntityID` | `sTYPE_TEXT` | Global | No | No |  | Parcel / Parcel Info |
| Parcel Name | `ParcelName` | `sTYPE_ENTITY_NAME` | Global | Yes | No |  | Parcel / Parcel Info |
| Parcel Number | `ParcelNumber` | `sTYPE_TEXT` | Global | No | No |  | Parcel / Parcel Info |
| Parcel Public Name | `ParcelPublicName` | `sTYPE_TEXT` | Global | No | No |  | Parcel / Parcel Info |
| Parcel RecID | `ParcelID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Parcel / Parcel Info |
| Parcel Status | `CodeParcelStatusID` | `sCODE_PARCEL_STATUS` | Global | No | No |  | Parcel / Parcel Info |
| Parcel Type | `CodeParcelTypeID` | `sCODE_PARCEL_TYPE` | Global | No | No |  | Parcel / Parcel Info |
| Parcel UUID | `UUID` | `sTYPE_TEXT` | Global | No | No |  | Parcel / Parcel Info |
| Parcel Use | `CodeParcelUseID` | `sCODE_PARCEL_USE` | Global | No | No |  | Parcel / Parcel Info |
| Portfolio | `ProgramID` | `sTYPE_PROGRAM` | Global | Yes | No |  | Parcel / Parcel Info |
| Primary Assessed Amount | `PrimaryAssessedAmount` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Parcel Info |
| Primary Value Amount | `PrimaryValueAmount` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Parcel Info |
| Purchase Date | `PurchaseDate` | `sTYPE_DATE` | Global | No | No |  | Parcel / Parcel Info |
| Schedule Creation Method | `TaskCreationMethod` | `sTYPE_TASK_CREATION_METHOD` | Global | Yes | No |  | Parcel / Parcel Info |
| Secondary Assessed Amount | `SecondaryAssessedAmount` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Parcel Info |
| Secondary Value Amount | `SecondaryValueAmount` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Parcel Info |
| Source Reference | `SourceReference` | `sTYPE_TEXTAREA` | Global | No | No |  | Parcel / Parcel Info |
| Source Reference Date | `SourceReferenceDate` | `sTYPE_DATE` | Global | No | No |  | Parcel / Parcel Info |
| Survey Date | `SurveyDate` | `sTYPE_DATE` | Global | No | No |  | Parcel / Parcel Info |
| Tax Authority | `TaxAuthority` | `sTYPE_TEXT` | Global | No | No |  | Parcel / Parcel Info |
| Tax Begin Period | `TaxBeginPeriod` | `sTYPE_DATE` | Global | No | No |  | Parcel / Parcel Info |
| Tax End Period | `TaxEndPeriod` | `sTYPE_DATE` | Global | No | No |  | Parcel / Parcel Info |
| Tax ID Number | `TaxIDNumber` | `sTYPE_TEXT` | Global | No | No |  | Parcel / Parcel Info |
| Tax Jurisdiction | `TaxJurisdictionID` | `sTYPE_JURISDICTION` | Global | No | No |  | Parcel / Parcel Info |
| Tax Responsibility | `CodeTaxResponsibilityID` | `sCODE_RESPONSIBLE_PARTY` | Global | No | No |  | Parcel / Parcel Info |
| Third Party Warehouse | `ThirdPartyWarehouse` | `sTYPE_TEXT` | Global | No | No |  | Parcel / Parcel Info |
| Time Zone | `TimeZone` | `sTYPE_TIMEZONE` | Global | No | No |  | Parcel / Parcel Info |
