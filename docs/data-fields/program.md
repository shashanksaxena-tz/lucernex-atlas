# Program — Data Fields

A capital/rollout program header — the container above ProjectEntity for a slate of related capital projects, carrying its own page-layout assignments (Cap Project Setup Page Layout, Cap Project Map Setup Layout) and exchange-rate-type overrides per cost category (Asset Amortization, Asset Balance, Cash Expenses) with matching '(Translation)' fields for multi-currency portfolios. 85 Global fields under Program Summary Information; the page-layout fields here are notable because they mean a Program's own metadata determines which page layout its child projects render with, tying this entity directly into the PAGE-LAYOUTS-01 configuration domain.

**Table Association:** `Program` &nbsp;·&nbsp; **Total fields:** 85 (Global: 85, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| % Projects Complete | `PercentCompleteByCount` | `sTYPE_PERCENTAGE` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Asset Amortization Exchange Rate Type | `CodeAssetAmortFXTypeID` | `sCODE_EXCHANGE_RATE_TYPE` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Asset Amortization Exchange Rate Type (Translation) | `CodeAssetAmortSubFXTypeID` | `sCODE_EXCHANGE_RATE_TYPE` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Asset Balance Exchange Rate Type | `CodeAssetBalFXTypeID` | `sCODE_EXCHANGE_RATE_TYPE` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Asset Balance Exchange Rate Type (Translation) | `CodeAssetBalSubFXTypeID` | `sCODE_EXCHANGE_RATE_TYPE` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Cap Project Map Setup Layout | `CapProjectMapSetupLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Cap Project Setup Page Layout | `CapProjectSetupPageLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Cash Expenses Exchange Rate Type | `CodeCashExpensesFXTypeID` | `sCODE_EXCHANGE_RATE_TYPE` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Cash Expenses Exchange Rate Type (Translation) | `CodeCashExpensesSubFXTypeID` | `sCODE_EXCHANGE_RATE_TYPE` | Global | No | No |  | Program Summary Information / Program Summary Information |
| City | `City` | `sTYPE_TEXT` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Currency Type | `CodeCurrencyTypeID` | `sCODE_CURRENCY_TYPE` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Default Auto Push Forecast End Date | `DefaultAutoPushForecastEndDate` | `sTYPE_YES_NO_RADIO` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Default Holiday Schedule | `DefaultHolidayScheduleID` | `sTYPE_HOLIDAY_SCHEDULE` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Default Work Weekends | `DefaultWorkWeekends` | `sTYPE_YES_NO_RADIO` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Description | `Description` | `sTYPE_TEXT` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Equipment Contract Setup Page Layout | `EquipmentContractSetupPageLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Facility Map Setup Layout | `FacilityMapSetupLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Facility Setup Page Layout | `FacilitySetupPageLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Fair Value Threshold | `FairValueThreshold` | `sTYPE_PERCENTAGE` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Fiscal year end | `FiscalYearEnd` | `sTYPE_DATE` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Interest Exchange Rate Type | `CodeInterestFXTypeID` | `sCODE_EXCHANGE_RATE_TYPE` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Interest Exchange Rate Type (Translation) | `CodeInterestSubFXTypeID` | `sCODE_EXCHANGE_RATE_TYPE` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Liability Amortization Exchange Rate Type | `CodeLiabAmortFXTypeID` | `sCODE_EXCHANGE_RATE_TYPE` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Liability Amortization Exchange Rate Type (Translation) | `CodeLiabAmortSubFXTypeID` | `sCODE_EXCHANGE_RATE_TYPE` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Liability Balances Exchange Rate Type | `CodeLiabilityBalFXTypeID` | `sCODE_EXCHANGE_RATE_TYPE` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Liability Balances Exchange Rate Type (Translation) | `CodeLiabilityBalSubFXTypeID` | `sCODE_EXCHANGE_RATE_TYPE` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Location Map Setup Layout | `LocationMapSetupLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Location Setup Page Layout | `LocationSetupPageLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Markets Summary | `MarketsInProgram` | `sTYPE_TEXT` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Name | `ProgramName` | `sTYPE_ENTITY_NAME` | Global | Yes | No |  | Program Summary Information / Program Summary Information |
| New SetUp Rate On Remeasure | `UseNewSetUpRateOnRemeasure` | `sTYPE_CHECKBOX` | Global | No | No |  | Program Summary Information / Program Summary Information |
| New SetUp Rate on Remeasurement | `UseNewSetUpRateOnRemeasure` | `sTYPE_YES_NO_RADIO` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Number Of Equipment Contract Approval Levels | `NumberOfEquipPTApprovalLevels` | `sTYPE_NUMBER` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Number of RE Contract Approval Levels | `NumberOfPTApprovalLevels` | `sTYPE_NUMBER` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Open Project Map Setup Layout | `OpenProjectMapSetupLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Open Project Setup Page Layout | `OpenProjectSetupPageLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Parcel Map Setup Layout | `ParcelMapSetupLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Parcel Setup Page Layout | `ParcelSetupPageLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Portfolio for Org Chart | `OrgChartProgramID` | `sTYPE_PROGRAM` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Postal Code | `PostalCode` | `sTYPE_POSTALCODE` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Program ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Program Summary Information / Program Summary Information |
| Program RecID | `ProgramID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Program or Portfolio | `ProgramType` | `sTYPE_TEXT` | Global | Yes | No |  | Program Summary Information / Program Summary Information |
| Project To Facility Setup Layout | `ProjectToFacilitySetupLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Projects Completed | `NumProjectsComplete` | `sTYPE_NUMBER` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Projects Completion Date | `CapProjectsEndDate` | `sTYPE_DATE` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Projects Remaining | `NumProjectsNotComplete` | `sTYPE_NUMBER` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Projects Summary | `CapProjectsInProgram` | `sTYPE_TEXT` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Prototype Setup Page Layout | `PrototypeSetupPageLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Prototypes Summary | `PrototypesInProgram` | `sTYPE_TEXT` | Global | No | No |  | Program Summary Information / Program Summary Information |
| RE Contract Setup Page Layout | `ContractSetupPageLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Regions Summary | `RegionsInProgram` | `sTYPE_TEXT` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Remaining Economic Life Threshold | `RemainingEconomicLifeThreshold` | `sTYPE_PERCENTAGE` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Revenue per week | `RevenuePerWeek` | `sTYPE_MONEY` | Global | No | No |  | Program Summary Information / Program Summary Information |
| SL Asset Amortize Method | `SLAssetAmortizeMethod` | `sTYPE_TEXT` | Global | No | No |  | Program Summary Information / Program Summary Information |
| SL Cash Amortize Method | `SLCashAmortizeMethod` | `sTYPE_TEXT` | Global | No | No |  | Program Summary Information / Program Summary Information |
| SL Discount Rate | `SLDiscountRate` | `sTYPE_PERCENTAGE` | Global | No | No |  | Program Summary Information / Program Summary Information |
| SL Expense Amortize Method | `SLExpenseAmortizeMethod` | `sTYPE_TEXT` | Global | No | No |  | Program Summary Information / Program Summary Information |
| SL Match Year Ends? | `SLMatchYearEnds` | `sTYPE_YES_NO_RADIO` | Global | No | No |  | Program Summary Information / Program Summary Information |
| SL Prorate #35 As #28? | `SLProrate35As28` | `sTYPE_YES_NO_RADIO` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Scenario Map Setup Layout | `ScenarioMapSetupLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Single Lease Exchange Rate Type | `CodeSingleLeaseFXTypeID` | `sCODE_EXCHANGE_RATE_TYPE` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Single Lease Exchange Rate Type (Translation) | `CodeSingleLeaseSubFXTypeID` | `sCODE_EXCHANGE_RATE_TYPE` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Site Map Setup Layout | `SiteMapSetupLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Site Setup Page Layout | `SiteSetupPageLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Site To Project Setup Layout | `SiteToProjectSetupLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | No | No |  | Program Summary Information / Program Summary Information |
| State | `IStateProvinceCountryID` | `sTYPE_STATE_PROVINCE` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Street address #1 | `StreetAddress1` | `sTYPE_TEXT` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Street address #2 | `StreetAddress2` | `sTYPE_TEXT` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Street address #3 | `StreetAddress3` | `sTYPE_TEXT` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Street address #4 | `StreetAddress4` | `sTYPE_TEXT` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Total Active Projects | `TotalActiveProjects` | `sTYPE_NUMBER` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Total Capital Projects | `TotalCapitalProjects` | `sTYPE_NUMBER` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Total Contracts | `TotalContracts` | `sTYPE_NUMBER` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Total Dead Projects | `TotalDeadProjects` | `sTYPE_NUMBER` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Total Equipment Contracts | `TotalEquipmentContracts` | `sTYPE_NUMBER` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Total Facilities | `TotalFacilities` | `sTYPE_NUMBER` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Total Inactive Projects | `TotalInactiveProjects` | `sTYPE_NUMBER` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Total Locations | `TotalLocations` | `sTYPE_NUMBER` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Total Opening Projects | `TotalOpeningProjects` | `sTYPE_NUMBER` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Total Parcels | `TotalParcels` | `sTYPE_NUMBER` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Total Projects | `TotalProjects` | `sTYPE_NUMBER` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Total RE Contracts | `TotalREContracts` | `sTYPE_NUMBER` | Global | No | No |  | Program Summary Information / Program Summary Information |
| Total Sites | `TotalSites` | `sTYPE_NUMBER` | Global | No | No |  | Program Summary Information / Program Summary Information |
