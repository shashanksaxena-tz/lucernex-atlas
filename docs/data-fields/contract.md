# Contract — Data Fields

The lease/contract header record itself — the central entity the rest of the schema hangs off of. It mixes core lease terms (dates, base rent, discount rate, renewal options) with dozens of Boolean 'in lease?' flags (Automatic Renewal In Lease?, Bargain Renewal In Lease?) that record whether a clause exists versus whether it has been exercised, plus `SUBMITBUTTON` fields that are workflow triggers rather than data. At 402 fields (255 Global + 147 Firm) it is also the entity this tenant has customized the most — 147 of the 205 total Firm-scope fields attach here, confirming Contract is where ASG has extended Lucernex's base model with tenant-specific CAM, co-tenancy, and delivery-requirement fields.

**Table Association:** `Contract` &nbsp;·&nbsp; **Total fields:** 402 (Global: 255, Firm: 147)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Contract Discount Rate | `DiscountRate` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Accounting Assumptions |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Audit Info |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Audit Info |
| Aggregate NNN Base Rent NPV | `AggregateNNNBaseRentNPV` | `sTYPE_MONEY` | Global | No | No |  | Contract / Cap Lease Test |
| Automatic Renewal In Lease? | `AutomaticRenewalInLease` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Cap Lease Test |
| Automatic Renewal Option? | `AutomaticRenewalOption` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Cap Lease Test |
| Bargain Renewal In Lease? | `BargainRenewalInLease` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Cap Lease Test |
| Bargain Renewal Option? | `BargainRenewalOption` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Cap Lease Test |
| Base Year Operating Expenses | `BaseYearOperatingExpenses` | `sTYPE_MONEY` | Global | No | No |  | Contract / Cap Lease Test |
| Base Year Other Expenses | `BaseYearOtherExpenses` | `sTYPE_MONEY` | Global | No | No |  | Contract / Cap Lease Test |
| Base Year RE Tax | `BaseYearRETax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Cap Lease Test |
| Contains Bargain Purchase Option? | `ContainsBargainPurchaseOption` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Cap Lease Test |
| Does Title Revert To Tenant? | `DoesTitleRevertToTenant` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Cap Lease Test |
| FMV Of Building | `FMVOfBuilding` | `sTYPE_MONEY` | Global | No | No |  | Contract / Cap Lease Test |
| FMV Of Land | `FMVOfLand` | `sTYPE_MONEY` | Global | No | No |  | Contract / Cap Lease Test |
| FMV Source | `FMVSource` | `sTYPE_TEXT` | Global | No | No |  | Contract / Cap Lease Test |
| Final Result | `FinalResult` | `sTYPE_TEXT` | Global | No | No |  | Contract / Cap Lease Test |
| Leased Land Area | `LeasedLandArea` | `sTYPE_AREA` | Global | No | No |  | Contract / Cap Lease Test |
| Project Land Area | `ProjectLandArea` | `sTYPE_AREA` | Global | No | No |  | Contract / Cap Lease Test |
| Ratio Lease w/ Auto Renewal To FMV | `RatioLeaseAutoRenewToFMV` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Cap Lease Test |
| Ratio Lease w/ Bargain Renewal To FMV | `RatioLeaseBargainRenewToFMV` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Cap Lease Test |
| Ratio Term w/ Auto Renewal To Life | `RatioTermAutoRenewToLife` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Cap Lease Test |
| Ratio Term w/ Bargain Renewal To Life | `RatioTermBargainRenewToLife` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Cap Lease Test |
| Remaining Life | `RemainingLife` | `sTYPE_NUMBER` | Global | No | No |  | Contract / Cap Lease Test |
| Test #1 Result | `Test1Result` | `sTYPE_TEXT` | Global | No | No |  | Contract / Cap Lease Test |
| Test #2 Result | `Test2Result` | `sTYPE_TEXT` | Global | No | No |  | Contract / Cap Lease Test |
| Test #3 Result | `Test3Result` | `sTYPE_TEXT` | Global | No | No |  | Contract / Cap Lease Test |
| Test #4 Result | `Test4Result` | `sTYPE_TEXT` | Global | No | No |  | Contract / Cap Lease Test |
| Test #5a Result | `Test5aResult` | `sTYPE_TEXT` | Global | No | No |  | Contract / Cap Lease Test |
| Test #5b Result | `Test5bResult` | `sTYPE_TEXT` | Global | No | No |  | Contract / Cap Lease Test |
| Year Built | `YearBuilt` | `sTYPE_DROPDOWN_YEAR` | Global | No | No |  | Contract / Cap Lease Test |
| Administrative Fee | `Firm_CAMAdministrativeYN` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Common Area Maintenance |
| Administrative Fee Definition | `Firm_CAMAdministrativeFeeDefinition` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Common Area Maintenance |
| Administrative Fee Exclusions | `Firm_CAMAdministrativeFeeExclusionsYN` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Common Area Maintenance |
| Administrative Fee Percent | `Firm_CAMAdministrativeFeePercent` | `sTYPE_PERCENTAGE` | Firm | No | No |  | Contract / Common Area Maintenance |
| Audit Rights | `Firm_CAMAuditRightsYN` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Common Area Maintenance |
| Audit Rights Reference | `Firm_CAMAuditRightsReference` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Common Area Maintenance |
| Comment | `Firm_CAMComment` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Common Area Maintenance |
| Contributions | `Firm_CAMContributionsYN` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Common Area Maintenance |
| Contributions Reference | `Firm_CAMContributionsReference` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Common Area Maintenance |
| Date of First Increase | `Firm_CAMDateofFirstIncrease` | `sTYPE_DATE` | Firm | No | No |  | Contract / Common Area Maintenance |
| Document | `Firm_CAMDocument` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Common Area Maintenance |
| Exclusions | `Firm_CAMExclusionsYN` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Common Area Maintenance |
| Exclusions Reference | `Firm_CAMExclusionsReference` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Common Area Maintenance |
| Fixed CAM Increase Comment | `Firm_CAMFixedComment` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Common Area Maintenance |
| Fixed CAM Increase Percent | `Firm_CAMFixedIncreasePercent` | `sTYPE_PERCENTAGE` | Firm | No | No |  | Contract / Common Area Maintenance |
| Fixed CAM Status | `Firm_CAMFixedStatus` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Common Area Maintenance |
| Fixed CAM Text | `Firm_CAMFixedText` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Common Area Maintenance |
| Floor Percent | `Firm_CAMFloorPercent` | `sTYPE_PERCENTAGE` | Firm | No | No |  | Contract / Common Area Maintenance |
| Initial Fixed CAM Monthly | `Firm_CAMInitialFixedMO` | `sTYPE_NUMBER` | Firm | No | No |  | Contract / Common Area Maintenance |
| Initial Fixed CAM PSF | `Firm_CAMInitialFixedPSF` | `sTYPE_NUMBER` | Firm | No | No |  | Contract / Common Area Maintenance |
| Is CAM Fixed? | `Firm_CAMFixedYN` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Common Area Maintenance |
| Lease Term Cap | `Firm_CAMLeaseTermCapYN` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Common Area Maintenance |
| Lease Term Cap Comment | `Firm_CAMLeaseTermCapComment` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Common Area Maintenance |
| Lease Term Cap Exclusions | `Firm_CAMLeaseTermCapExclusions` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Common Area Maintenance |
| Lease Term Cap Percent | `Firm_CAMLeaseTermCapPercent` | `sTYPE_PERCENTAGE` | Firm | No | No |  | Contract / Common Area Maintenance |
| Lease Term Cap Text Reference | `Firm_CAMLeaseTermCapTextReference` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Common Area Maintenance |
| Lease Term Cap Type | `Firm_CAMLeaseTermCapType` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Common Area Maintenance |
| Month of Increase | `Firm_CAMMonthofIncrease` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Common Area Maintenance |
| No Duplication of Costs Language | `Firm_CAMNoDuplicationofCostsLanguageYN` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Common Area Maintenance |
| No Duplication of Costs Reference | `Firm_CAMNoDuplicationofCostsReference` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Common Area Maintenance |
| Notes | `Firm_CAMNotes` | `sTYPE_TEXTAREA` | Firm | No | No |  | Contract / Common Area Maintenance |
| Number of Years Auditable | `Firm_CAMNumberofYearsAuditable` | `sTYPE_NUMBER` | Firm | No | No |  | Contract / Common Area Maintenance |
| PR Share | `Firm_CAMPRShare` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Common Area Maintenance |
| Page | `Firm_CAMPage` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Common Area Maintenance |
| Prorata Share Status | `Firm_CAMPRShareStatus` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Common Area Maintenance |
| Section | `Firm_CAMSection` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Common Area Maintenance |
| Starting Cap | `Firm_CAMStartingCapYN` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Common Area Maintenance |
| Starting Cap Amount Monthly | `Firm_CAMStartingCapMonthly` | `sTYPE_NUMBER` | Firm | No | No |  | Contract / Common Area Maintenance |
| Starting Cap Amount PSF | `Firm_CAMStartingCapAmountPSF` | `sTYPE_NUMBER` | Firm | No | No |  | Contract / Common Area Maintenance |
| Starting Cap Comment | `Firm_CAMStartingCapComment` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Common Area Maintenance |
| Starting Cap Exclusions | `Firm_CAMStartingCapExclusionsYN` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Common Area Maintenance |
| Starting Cap Status | `Firm_CAMStartingCapStatus` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Common Area Maintenance |
| Starting Cap Text Reference | `Firm_CAMStartingCapTextReference` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Common Area Maintenance |
| Statements Binding Language | `Firm_CAMStatementsBindingLanguageYN` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Common Area Maintenance |
| Statements Binding Language Reference | `Firm_CAMStatementsBindingLanguageReference` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Common Area Maintenance |
| Statements Due | `Firm_CAMStatementsDue` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Common Area Maintenance |
| Statements Due Reference | `Firm_CAMStatementsDueReference` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Common Area Maintenance |
| Actual End Date | `ActualEndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Contract Dates |
| Actual Start Date | `ActualStartDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Contract Dates |
| Baseline End Date | `BaselineEndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Contract Dates |
| Baseline Start Date | `BaselineStartDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Contract Dates |
| Commence Date | `CommenceDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Contract Dates |
| Current Month/Year | `CurrentMonthYear` | `sTYPE_TEXT` | Global | No | No |  | Contract / Contract Dates |
| Current Year | `CurrentYear` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Contract Dates |
| Days to Expiration | `DaysToExpiration` | `sTYPE_NUMBER_FRACTION0DIGITS` | Global | No | No |  | Contract / Contract Dates |
| Execute Date | `ExecuteDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Contract Dates |
| Expected End Date | `ExpectedEndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Contract Dates |
| Expire Date | `ExpireDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Contract Dates |
| Fixturing Period | `Firm_FixturingPeriod` | `sTYPE_NUMBER` | Firm | No | No |  | Contract / Contract Dates |
| Obligation Date | `ObligationDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Contract Dates |
| Original Possession Date | `Firm_OriginalPossessionDate` | `sTYPE_DATE` | Firm | No | No |  | Contract / Contract Dates |
| Payments Begin Date | `PaymentsBeginDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Contract Dates |
| Payments End Date | `PaymentsEndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Contract Dates |
| Possession Begin Date | `PossessionBeginDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Contract Dates |
| Possession End Date | `PossessionEndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Contract Dates |
| Status Effective Date | `StatusEffectiveDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Contract Dates |
| Term Length | `TermLength` | `sTYPE_DATE_MATH_OPERATION` | Global | No | No |  | Contract / Contract Dates |
| Agreement Type | `CodeAgreementTypeID` | `sCODE_AGREEMENT_TYPE` | Global | No | No |  | Contract / Contract Info |
| Asset Class | `CodeAssetClassID` | `sCODE_ASSET_CLASS` | Global | No | No |  | Contract / Contract Info |
| Brand | `Firm_Brand` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Contract Info |
| Building Area Unit | `CodeBuildingAreaUnitID` | `sCODE_BUILDING_AREA_UNIT` | Global | No | No |  | Contract / Contract Info |
| Computed Discount Rate | `ComputedSLDiscountRate` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Contract Info |
| Contract Category | `CodeContractCategoryID` | `sCODE_CONTRACT_CATEGORY` | Global | No | No |  | Contract / Contract Info |
| Contract Class | `ContractClass` | `sTYPE_TEXT` | Global | No | No |  | Contract / Contract Info |
| Contract ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Contract Info |
| Contract Group | `CodeContractGroupID` | `sCODE_CONTRACT_GROUP` | Global | No | No |  | Contract / Contract Info |
| Contract ID | `ClientEntityID` | `sTYPE_TEXT` | Global | No | No |  | Contract / Contract Info |
| Contract Name | `ContractName` | `sTYPE_ENTITY_NAME` | Global | Yes | No |  | Contract / Contract Info |
| Contract RecID | `ContractID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Contract Info |
| Contract Status | `CodeContractStatusID` | `sCODE_CONTRACT_STATUS` | Global | No | No |  | Contract / Contract Info |
| Contract Tax Rate #1 | `ContractTaxRate1` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Contract Info |
| Contract Tax Rate #2 | `ContractTaxRate2` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Contract Info |
| Contract Tax Rate #3 | `ContractTaxRate3` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Contract Info |
| Contract Tax Rate #4 | `ContractTaxRate4` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Contract Info |
| Contract Type | `CodeContractTypeID` | `sCODE_CONTRACT_TYPE` | Global | No | No |  | Contract / Contract Info |
| Contract UUID | `UUID` | `sTYPE_TEXT` | Global | No | No |  | Contract / Contract Info |
| Contract Use | `CodeContractUseID` | `sCODE_CONTRACT_USE` | Global | No | No |  | Contract / Contract Info |
| Corp | `Firm_CorporateCode` | `sTYPE_NUMBER` | Firm | No | No |  | Contract / Contract Info |
| Cost Center | `Firm_CostCenter` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Contract Info |
| Currency Type | `CodeCurrencyTypeID` | `sCODE_CURRENCY_TYPE` | Global | No | No |  | Contract / Contract Info |
| Description | `ProjectDescription` | `sTYPE_TEXT` | Global | No | No |  | Contract / Contract Info |
| Developer Lease ID | `Firm_DeveloperLeaseID` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Contract Info |
| Expense Accrual Forecast Table | `ExpAccrualForecastTable` | `sTYPE_EXPACCRUAL_FORECAST_TABLE` | Global | No | No |  | Contract / Contract Info |
| Expense Forecast Table | `ExpenseForecastTable` | `sTYPE_EXPENSE_FORECAST_TABLE` | Global | No | No |  | Contract / Contract Info |
| Facility | `FacilityID` | `sTYPE_FACILITY` | Global | No | No |  | Contract / Contract Info |
| Fair Value Threshold | `FairValueThreshold` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Contract Info |
| Franchise Location | `Firm_FranchiseLocation` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Contract Info |
| Guarantor | `Firm_Guarantor` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Contract Info |
| Holding Interest | `CodeHoldingInterestID` | `sCODE_HOLDING_INTEREST` | Global | No | No |  | Contract / Contract Info |
| In Alternate Rent? | `InAlternateRent` | `sTYPE_BOOLEAN` | Global | No | No |  | Contract / Contract Info |
| Is Low Asset Value | `IsLowAssetValue` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Contract Info |
| Is Short Term | `IsShortTerm` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Contract Info |
| Is Translation | `IsTranslation` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Contract Info |
| Landlord Legal Name | `Firm_LandlordLegalName` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Contract Info |
| Last Deferred SL Entry | `Firm_LastDeferredSLEntry` | `sTYPE_MONEY` | Firm | No | No |  | Contract / Contract Info |
| Last Deferred SL Entry Date | `Firm_LastDeferredSLEntryDate` | `sTYPE_DATE` | Firm | No | No |  | Contract / Contract Info |
| Last Deferred SL Total | `Firm_LastDeferredSLTotal` | `sTYPE_MONEY` | Firm | No | No |  | Contract / Contract Info |
| Latest Financial Test Result | `LatestFinancialTestFinalResult` | `sTYPE_TEXT` | Global | No | No |  | Contract / Contract Info |
| Lease Analyst | `Firm_LeaseAnalyst` | `sTYPE_MEMBER` | Firm | No | No |  | Contract / Contract Info |
| Lease Expiration Reference | `Firm_LeaseExpirationReference` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Contract Info |
| Lease Status | `Firm_LeaseStatus` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Contract Info |
| Lease Status Notes | `Firm_LeaseStatusNotes` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Contract Info |
| Lease Year | `Firm_LeaseYear` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Contract Info |
| Lease Year Reference | `Firm_LeaseYearReference` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Contract Info |
| Likely Term End Date | `LastLikelyOptionDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Contract Info |
| Location | `LocationID` | `sTYPE_LOCATION` | Global | No | No |  | Contract / Contract Info |
| Master Contract | `MasterContractID` | `sTYPE_CONTRACT` | Global | No | No |  | Contract / Contract Info |
| Month To Month? | `MonthToMonth` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Contract Info |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Contract Info |
| Open Year | `OpenYear` | `sTYPE_DROPDOWN_YEAR` | Global | No | No |  | Contract / Contract Info |
| Option Description | `OptionDescription` | `sTYPE_TEXT` | Global | No | No |  | Contract / Contract Info |
| Organization | `OrganizationID` | `sTYPE_ORGANIZATION` | Global | No | No |  | Contract / Contract Info |
| Out Of Date Days | `OutOfDateDays` | `sTYPE_NUMBER` | Global | No | No |  | Contract / Contract Info |
| Payment Rate | `PaymentRate` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Contract Info |
| Portfolio | `ProgramID` | `sTYPE_PROGRAM` | Global | No | No |  | Contract / Contract Info |
| Pro Rata Share Rate | `ProRataShareRate` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Contract Info |
| Proration Method | `CodeProrationMethodID` | `sCODE_PRORATION_METHOD` | Global | No | No |  | Contract / Contract Info |
| Remaining Economic Life Threshold | `RemainingEconomicLifeThreshold` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Contract Info |
| Rent Commencement Notes | `Firm_RentCommencementNotes` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Contract Info |
| Rentable Area | `RentableArea` | `sTYPE_AREA` | Global | No | No |  | Contract / Contract Info |
| Schedule Behind Days | `BehindScheduleDays` | `sTYPE_NUMBER` | Global | No | No |  | Contract / Contract Info |
| Schedule Creation Method | `TaskCreationMethod` | `sTYPE_TASK_CREATION_METHOD` | Global | Yes | No |  | Contract / Contract Info |
| Service Channel Location ID | `ScLocationID` | `sTYPE_TEXT` | Global | No | No |  | Contract / Contract Info |
| Tenant Legal Name | `Firm_TenantLegalName` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Contract Info |
| Time Zone | `TimeZone` | `sTYPE_TIMEZONE` | Global | No | No |  | Contract / Contract Info |
| currPaymentRate | `math_currPaymentRate_9` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Contract Info |
| zLeaseSquareFootage | `zFirm_LeaseSquareFootage` | `sTYPE_NUMBER_FRACTION2DIGITS` | Firm | No | No |  | Contract / Contract Info |
| Next Available Term | `NextAvailableTermID` | `sTYPE_CONTRACT_TERM` | Global | No | No |  | Contract / Contract Term |
| Next Available Term Key Date Info | `NextAvailableTermKeyDateID` | `sTYPE_KEY_DATE` | Global | No | No |  | Contract / Contract Term |
| Remaining Number of Terms | `RemainingNumberOfTerms` | `sTYPE_NUMBER` | Global | No | No |  | Contract / Contract Term |
| Default Log | `Firm_DefaultLog` | `sTYPE_CLIENT_LISTS` | Firm | No | No |  | Contract / Custom Lists |
| Funds | `Firm_Funds` | `sTYPE_CLIENT_LISTS` | Firm | No | No |  | Contract / Custom Lists |
| Operating Expenses | `Firm_OperatingExpenses` | `sTYPE_CLIENT_LISTS` | Firm | No | No |  | Contract / Custom Lists |
| Reconciliation Log | `Firm_ReconciliationLog` | `sTYPE_CLIENT_LISTS` | Firm | No | No |  | Contract / Custom Lists |
| Savings Log | `Firm_SavingsLog` | `sTYPE_CLIENT_LISTS` | Firm | No | No |  | Contract / Custom Lists |
| Anticipated Delivery Date | `Firm_DRAnticipatedDeliveryDate` | `sTYPE_DATE` | Firm | No | No |  | Contract / Delivery Requirements |
| Document | `Firm_DRDocument` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Delivery Requirements |
| Landlord's Punchlist Complete | `Firm_DRLandlordPunchlistComplete` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Delivery Requirements |
| Notes | `Firm_DRNotes` | `sTYPE_TEXTAREA` | Firm | No | No |  | Contract / Delivery Requirements |
| Page | `Firm_DRPage` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Delivery Requirements |
| Rent Abatement | `Firm_DRRentAbatement` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Delivery Requirements |
| Section | `Firm_DRSection` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Delivery Requirements |
| Termination Right Date | `Firm_DRTerminationRightDate` | `sTYPE_DATE` | Firm | No | No |  | Contract / Delivery Requirements |
| Aggregate Base Rent | `AggregateBaseRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar |
| Aggregate Total Rent | `AggregateTotalRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar |
| Beyond Fifth Calendar Year Base Rent | `BeyondFifthYearBaseRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar |
| Beyond Fifth Calendar Year Total Rent | `BeyondFifthYearTotalRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar |
| Beyond Sixth Calendar Year Base Rent | `BeyondSixthYearBaseRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar |
| Beyond Sixth Calendar Year Total Rent | `BeyondSixthYearTotalRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar |
| Current Annual Calendar Base Rent | `CurrentAnnualBaseRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar |
| Current Annual Calendar Total Rent | `CurrentAnnualTotalRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar |
| Current Calendar Q1 Base Rent | `CurrentCalendarYearQ1BaseRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar |
| Current Calendar Q1 Total Rent | `CurrentCalendarYearQ1TotalRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar |
| Current Calendar Q2 Base Rent | `CurrentCalendarYearQ2BaseRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar |
| Current Calendar Q2 Total Rent | `CurrentCalendarYearQ2TotalRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar |
| Current Calendar Q3 Base Rent | `CurrentCalendarYearQ3BaseRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar |
| Current Calendar Q3 Total Rent | `CurrentCalendarYearQ3TotalRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar |
| Current Calendar Q4 Base Rent | `CurrentCalendarYearQ4BaseRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar |
| Current Calendar Q4 Total Rent | `CurrentCalendarYearQ4TotalRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar |
| Current Calendar Year Gross Sales | `CurrentCalendarYearGrossSales` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar |
| Current Monthly Base Rent | `CurrentMonthlyBaseRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar |
| Current Monthly Total Rent | `CurrentMonthlyTotalRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar |
| Current Straight Line Asset Balance | `CurrentStraightLineAssetBalance` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar |
| Current Straight Line Liability Balance | `CurrentStraightLineLiabilityBalance` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar |
| Fifth Calendar Year Base Rent | `FifthYearBaseRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar |
| Fifth Calendar Year Total Rent | `FifthYearTotalRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar |
| Fourth Calendar Year Base Rent | `FourthYearBaseRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar |
| Fourth Calendar Year Total Rent | `FourthYearTotalRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar |
| Next Calendar Year Base Rent | `NextYearBaseRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar |
| Next Calendar Year Total Rent | `NextYearTotalRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar |
| Prior Calendar Year Gross Sales | `PriorCalendarYearGrossSales` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar |
| Remaining Base Rent Obligation | `RemainingObligationBaseRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar |
| Remaining Total Rent Obligation | `RemainingObligationTotalRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar |
| Sixth Calendar Year Base Rent | `SixthYearBaseRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar |
| Sixth Calendar Year Total Rent | `SixthYearTotalRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar |
| Third Calendar Year Base Rent | `ThirdYearBaseRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar |
| Third Calendar Year Total Rent | `ThirdYearTotalRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar |
| Aggregate Base Rent w/ Tax | `AggregateBaseRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar w/ Tax |
| Aggregate Total Rent w/ Tax | `AggregateTotalRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar w/ Tax |
| Beyond Fifth Calendar Year Base Rent w/ Tax | `BeyondFifthYearBaseRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar w/ Tax |
| Beyond Fifth Calendar Year Total Rent w/ Tax | `BeyondFifthYearTotalRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar w/ Tax |
| Beyond Sixth Calendar Year Base Rent w/ Tax | `BeyondSixthYearBaseRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar w/ Tax |
| Beyond Sixth Calendar Year Total Rent w/ Tax | `BeyondSixthYearTotalRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar w/ Tax |
| Current Annual Calendar Base Rent w/ Tax | `CurrentAnnualBaseRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar w/ Tax |
| Current Annual Calendar Total Rent w/ Tax | `CurrentAnnualTotalRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar w/ Tax |
| Current Calendar Q1 Base Rent w/ Tax | `CurrentCalendarYearQ1BaseRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar w/ Tax |
| Current Calendar Q1 Total Rent w/ Tax | `CurrentCalendarYearQ1TotalRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar w/ Tax |
| Current Calendar Q2 Base Rent w/ Tax | `CurrentCalendarYearQ2BaseRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar w/ Tax |
| Current Calendar Q2 Total Rent w/ Tax | `CurrentCalendarYearQ2TotalRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar w/ Tax |
| Current Calendar Q3 Base Rent w/ Tax | `CurrentCalendarYearQ3BaseRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar w/ Tax |
| Current Calendar Q3 Total Rent w/ Tax | `CurrentCalendarYearQ3TotalRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar w/ Tax |
| Current Calendar Q4 Base Rent w/ Tax | `CurrentCalendarYearQ4BaseRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar w/ Tax |
| Current Calendar Q4 Total Rent w/ Tax | `CurrentCalendarYearQ4TotalRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar w/ Tax |
| Current Monthly Base Rent w/ Tax | `CurrentMonthlyBaseRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar w/ Tax |
| Current Monthly Total Rent w/ Tax | `CurrentMonthlyTotalRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar w/ Tax |
| Fifth Calendar Year Base Rent w/ Tax | `FifthYearBaseRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar w/ Tax |
| Fifth Calendar Year Total Rent w/ Tax | `FifthYearTotalRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar w/ Tax |
| Fourth Calendar Year Base Rent w/ Tax | `FourthYearBaseRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar w/ Tax |
| Fourth Calendar Year Total Rent w/ Tax | `FourthYearTotalRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar w/ Tax |
| Next Calendar Year Base Rent w/ Tax | `NextYearBaseRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar w/ Tax |
| Next Calendar Year Total Rent w/ Tax | `NextYearTotalRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar w/ Tax |
| Remaining Base Rent Obligation w/ Tax | `RemainingObligationBaseRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar w/ Tax |
| Remaining Total Rent Obligation w/ Tax | `RemainingObligationTotalRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar w/ Tax |
| Sixth Calendar Year Base Rent w/ Tax | `SixthYearBaseRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar w/ Tax |
| Sixth Calendar Year Total Rent w/ Tax | `SixthYearTotalRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar w/ Tax |
| Third Calendar Year Base Rent w/ Tax | `ThirdYearBaseRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar w/ Tax |
| Third Calendar Year Total Rent w/ Tax | `ThirdYearTotalRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Calendar w/ Tax |
| Beyond Fifth Fiscal Year Base Rent | `BeyondFifthFiscalYearBaseRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal |
| Beyond Fifth Fiscal Year Total Rent | `BeyondFifthFiscalYearTotalRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal |
| Beyond Sixth Fiscal Year Base Rent | `BeyondSixthFiscalYearBaseRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal |
| Beyond Sixth Fiscal Year Total Rent | `BeyondSixthFiscalYearTotalRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal |
| Current Annual Fiscal Base Rent | `CurrentAnnualFiscalBaseRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal |
| Current Annual Fiscal Total Rent | `CurrentAnnualFiscalTotalRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal |
| Current Fiscal Q1 Base Rent | `CurrentFiscalYearQ1BaseRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal |
| Current Fiscal Q1 Total Rent | `CurrentFiscalYearQ1TotalRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal |
| Current Fiscal Q2 Base Rent | `CurrentFiscalYearQ2BaseRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal |
| Current Fiscal Q2 Total Rent | `CurrentFiscalYearQ2TotalRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal |
| Current Fiscal Q3 Base Rent | `CurrentFiscalYearQ3BaseRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal |
| Current Fiscal Q3 Total Rent | `CurrentFiscalYearQ3TotalRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal |
| Current Fiscal Q4 Base Rent | `CurrentFiscalYearQ4BaseRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal |
| Current Fiscal Q4 Total Rent | `CurrentFiscalYearQ4TotalRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal |
| Current Period Base Rent | `CurrentPeriodBaseRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal |
| Current Period Total Rent | `CurrentPeriodTotalRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal |
| Fifth Fiscal Year Base Rent | `FifthFiscalYearBaseRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal |
| Fifth Fiscal Year Total Rent | `FifthFiscalYearTotalRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal |
| Fourth Fiscal Year Base Rent | `FourthFiscalYearBaseRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal |
| Fourth Fiscal Year Total Rent | `FourthFiscalYearTotalRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal |
| Next Fiscal Year Base Rent | `NextFiscalYearBaseRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal |
| Next Fiscal Year Total Rent | `NextFiscalYearTotalRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal |
| Remaining Base Rent Obligation(Fiscal Year) | `RemainingFiscalObligationBaseRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal |
| Remaining Total Rent Obligation(Fiscal Year) | `RemainingFiscalObligationTotalRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal |
| Sixth Fiscal Year Base Rent | `SixthFiscalYearBaseRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal |
| Sixth Fiscal Year Total Rent | `SixthFiscalYearTotalRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal |
| Third Fiscal Year Base Rent | `ThirdFiscalYearBaseRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal |
| Third Fiscal Year Total Rent | `ThirdFiscalYearTotalRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal |
| Beyond Fifth Fiscal Year Base Rent w/ Tax | `BeyondFifthFiscalYearBaseRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal w/ Tax |
| Beyond Fifth Fiscal Year Total Rent w/ Tax | `BeyondFifthFiscalYearTotalRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal w/ Tax |
| Beyond Sixth Fiscal Year Base Rent w/ Tax | `BeyondSixthFiscalYearBaseRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal w/ Tax |
| Beyond Sixth Fiscal Year Total Rent w/ Tax | `BeyondSixthFiscalYearTotalRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal w/ Tax |
| Current Annual Fiscal Base Rent w/ Tax | `CurrentAnnualFiscalBaseRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal w/ Tax |
| Current Annual Fiscal Total Rent w/ Tax | `CurrentAnnualFiscalTotalRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal w/ Tax |
| Current Fiscal Q1 Base Rent w/ Tax | `CurrentFiscalYearQ1BaseRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal w/ Tax |
| Current Fiscal Q1 Total Rent w/ Tax | `CurrentFiscalYearQ1TotalRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal w/ Tax |
| Current Fiscal Q2 Base Rent w/ Tax | `CurrentFiscalYearQ2BaseRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal w/ Tax |
| Current Fiscal Q2 Total Rent w/ Tax | `CurrentFiscalYearQ2TotalRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal w/ Tax |
| Current Fiscal Q3 Base Rent w/ Tax | `CurrentFiscalYearQ3BaseRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal w/ Tax |
| Current Fiscal Q3 Total Rent w/ Tax | `CurrentFiscalYearQ3TotalRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal w/ Tax |
| Current Fiscal Q4 Base Rent w/ Tax | `CurrentFiscalYearQ4BaseRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal w/ Tax |
| Current Fiscal Q4 Total Rent w/ Tax | `CurrentFiscalYearQ4TotalRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal w/ Tax |
| Current Period Base Rent w/ Tax | `CurrentPeriodBaseRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal w/ Tax |
| Current Period Total Rent w/ Tax | `CurrentPeriodTotalRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal w/ Tax |
| Fifth Fiscal Year Base Rent w/ Tax | `FifthFiscalYearBaseRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal w/ Tax |
| Fifth Fiscal Year Total Rent w/ Tax | `FifthFiscalYearTotalRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal w/ Tax |
| Fourth Fiscal Year Base Rent w/ Tax | `FourthFiscalYearBaseRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal w/ Tax |
| Fourth Fiscal Year Total Rent w/ Tax | `FourthFiscalYearTotalRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal w/ Tax |
| Next Fiscal Year Base Rent w/ Tax | `NextFiscalYearBaseRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal w/ Tax |
| Next Fiscal Year Total Rent w/ Tax | `NextFiscalYearTotalRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal w/ Tax |
| Remaining Base Rent Obligation(Fiscal Year) w/ Tax | `RemainingFiscalObligationBaseRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal w/ Tax |
| Remaining Total Rent Obligation(Fiscal Year) w/ Tax | `RemainingFiscalObligationTotalRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal w/ Tax |
| Sixth Fiscal Year Base Rent w/ Tax | `SixthFiscalYearBaseRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal w/ Tax |
| Sixth Fiscal Year Total Rent w/ Tax | `SixthFiscalYearTotalRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal w/ Tax |
| Third Fiscal Year Base Rent w/ Tax | `ThirdFiscalYearBaseRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal w/ Tax |
| Third Fiscal Year Total Rent w/ Tax | `ThirdFiscalYearTotalRentWithTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Fiscal w/ Tax |
| Alternative Rent Terms | `Firm_ONCOTAlternativeRentTerms` | `sTYPE_TEXTAREA` | Firm | No | No |  | Contract / Ongoing Co Tenancy |
| Document | `Firm_ONCOTDocument` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Ongoing Co Tenancy |
| Frequency | `Firm_ONCOTFrequency` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Ongoing Co Tenancy |
| Limit Per Year | `Firm_ONCOTLimitPerYear` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Ongoing Co Tenancy |
| Notes | `Firm_ONCOTNotes` | `sTYPE_TEXTAREA` | Firm | No | No |  | Contract / Ongoing Co Tenancy |
| Ongoing Cotenancy Clause | `Firm_ONCOTClause` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Ongoing Co Tenancy |
| Page | `Firm_ONCOTPage` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Ongoing Co Tenancy |
| Remedy | `Firm_ONCOTRemedy` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Ongoing Co Tenancy |
| Required Number of Anchors | `Firm_ONCOTRequiredNumberofAnchors` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Ongoing Co Tenancy |
| Required Percent of Inline Space | `Firm_ONCOTRequiredPercentofInlineSpace` | `sTYPE_PERCENTAGE` | Firm | No | No |  | Contract / Ongoing Co Tenancy |
| Right To Request Roster | `Firm_ONCOTRightToRequestRoster` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Ongoing Co Tenancy |
| Right to Terminate | `Firm_ONCOTRighttoTerminate` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Ongoing Co Tenancy |
| Section | `Firm_ONCOTSection` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Ongoing Co Tenancy |
| Alternative Rent Terms | `Firm_OPCOTAlternativeRentTerms` | `sTYPE_TEXTAREA` | Firm | No | No |  | Contract / Opening Co Tenancy |
| Document | `Firm_OPCOTDocument` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Opening Co Tenancy |
| Notes | `Firm_OPCOTNotes` | `sTYPE_TEXTAREA` | Firm | No | No |  | Contract / Opening Co Tenancy |
| Opening Cotenancy Clause | `Firm_OPCOTClause` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Opening Co Tenancy |
| Page | `Firm_OPCOTPage` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Opening Co Tenancy |
| Required Number of Anchors | `Firm_OPCOTRequiredNumberofAnchors` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Opening Co Tenancy |
| Required Percent of Inline Space | `Firm_OPCOTRequiredPercentofInlineSpace` | `sTYPE_PERCENTAGE` | Firm | No | No |  | Contract / Opening Co Tenancy |
| Right to Terminate | `Firm_OPCOTRighttoTerminate` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Opening Co Tenancy |
| Section | `Firm_OPCOTSection` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Opening Co Tenancy |
| Administrative Fee | `Firm_RETAdministrativeFee` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Real Estate Taxes |
| Administrative Fee Exclusions | `Firm_RETAdministrativeFeeExclusionsYN` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Real Estate Taxes |
| Administrative Fee Percent | `Firm_RETAdministrativeFeePercent` | `sTYPE_PERCENTAGE` | Firm | No | No |  | Contract / Real Estate Taxes |
| Administrative Fee Reference | `Firm_RETAdministrativeFeeReference` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Real Estate Taxes |
| Audit Rights | `Firm_RETAuditRightsYN` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Real Estate Taxes |
| Audit Rights Reference | `Firm_RETAuditRightsReference` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Real Estate Taxes |
| Comment | `Firm_RETComment` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Real Estate Taxes |
| Consulting Fee Allowed | `Firm_RETConsultingFeeAllowedYN` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Real Estate Taxes |
| Consulting Fee Reference | `Firm_RETConsultingFeeReference` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Real Estate Taxes |
| Contributions | `Firm_RETContributionsYN` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Real Estate Taxes |
| Contributions Reference | `Firm_RETContributionsReferences` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Real Estate Taxes |
| Document | `Firm_RETDocument` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Real Estate Taxes |
| Floor Percent | `Firm_RETFloorPercent` | `sTYPE_PERCENTAGE` | Firm | No | No |  | Contract / Real Estate Taxes |
| GIS Link | `Firm_GISLink` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Real Estate Taxes |
| GIS Website | `Firm_GISWebsite` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Real Estate Taxes |
| Initial Estimate Monthly | `Firm_RETInitialEstimateMonthly` | `sTYPE_NUMBER` | Firm | No | No |  | Contract / Real Estate Taxes |
| Initial Estimate PSF | `Firm_RETInitialEstimatePSF` | `sTYPE_NUMBER` | Firm | No | No |  | Contract / Real Estate Taxes |
| Initial Estimate Reference | `Firm_RETInitialEstimateReference` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Real Estate Taxes |
| Is RET Fixed? | `Firm_RETFixedYN` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Real Estate Taxes |
| Landlord to Provide Tax Bills | `Firm_RETLandlordtoProvideTaxBillsYN` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Real Estate Taxes |
| Lease Term Cap | `Firm_RETLeaseTermCapYN` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Real Estate Taxes |
| Lease Term Cap Comment | `Firm_RETLeaseTermCapComment` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Real Estate Taxes |
| Lease Term Cap Percent | `Firm_RETLeaseTermCapPercent` | `sTYPE_PERCENTAGE` | Firm | No | No |  | Contract / Real Estate Taxes |
| Lease Term Cap Text Reference | `Firm_RETLeaseTermCapTextReference` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Real Estate Taxes |
| Lease Term Cap Type | `Firm_RETLeaseTermCapType` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Real Estate Taxes |
| Notes | `Firm_RETNotes` | `sTYPE_TEXTAREA` | Firm | No | No |  | Contract / Real Estate Taxes |
| PR Share | `Firm_RETPRShare` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Real Estate Taxes |
| Page | `Firm_RETPage` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Real Estate Taxes |
| Prorata Share Status | `Firm_RETPRShareStatus` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Real Estate Taxes |
| Section | `Firm_RETSection` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Real Estate Taxes |
| Starting Cap | `Firm_RETStartingCapYN` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Real Estate Taxes |
| Starting Cap Amount | `Firm_RETStartingCapAmount` | `sTYPE_NUMBER` | Firm | No | No |  | Contract / Real Estate Taxes |
| Starting Cap Exclusions | `Firm_RETStartingCapExclusionsYN` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Real Estate Taxes |
| Starting Cap Status | `Firm_RETStartingCapStatus` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Real Estate Taxes |
| Starting Cap Text Reference | `Firm_RETStartingCapTextReference` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Real Estate Taxes |
| Statements Binding | `Firm_RETStatementsBindingYN` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Real Estate Taxes |
| Statements Binding Reference | `Firm_RETStatementsBindingReference` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Real Estate Taxes |
| Statements Due | `Firm_RETStatementsDue` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Real Estate Taxes |
| Statements Due Reference | `Firm_RETStatementsDueReference` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Real Estate Taxes |
| Tax Link 1 | `Firm_TaxLink1` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Real Estate Taxes |
| Tax Link 2 | `Firm_TaxLink2` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Real Estate Taxes |
| Tax Website 1 | `Firm_TaxWebsite1` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Real Estate Taxes |
| Tax Website 2 | `Firm_TaxWebsite2` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Real Estate Taxes |
| Taxes For? | `Firm_RETTaxesFor` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Real Estate Taxes |
| Abstract Lease | `ABSTRACT_LEASE` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Alternate Rent Wizard | `ALTERNATE_RENT_WIZARD` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Apply Offsets | `APPLY_OFFSETS` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Audit Log | `AUDIT_LOG` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| CPI Adjustments | `CPI_ADJUSTMENTS` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Change Vendor | `CHANGE_EXPENSE_ALLOCATION_VENDOR` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Copy Expense | `COPY_EXPENSE_SETUP` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Copy Transaction | `COPY_PAYMENT_TRANSACTION` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Delete Accrual Payments | `DELETE_ACCRUAL_PAYMENTS` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Delete Asset Payments | `DELETE_ASSET_PAYMENTS` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Delete Payments | `DELETE_PAYMENTS` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Generate 842 Rent Schedule | `GenerateFASBSchedule` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Generate Accruals | `GENERATE_ACCRUALS` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Generate Asset Rent | `GENERATE_ASSET_RENT` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Generate Estimated Accruals | `GENERATE_ESTIMATED_ACCRUALS` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Generate Expense Accruals | `GENERATE_EXPENSE_ACCRUALS` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Generate IFRS 16 Rent Schedule | `GenerateIFRS16Schedule` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Generate Pass-through Payments | `GENERATE_PASS_THROUGH_PAYMENTS` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Generate Percentage Rent Accruals | `GENERATE_PERCENTAGE_RENT_ACCRUALS` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Generate Rent | `GENERATE_RENT` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Generate Retro Payment | `GENERATE_RETRO_PAYMENT` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Generate Straight-line Rent Schedule | `GenerateStraightLineRent` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Import Invoice | `IMPORT_INVOICE` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Modify Straight-Line Status | `ModifyStraightLineStatus` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Plan/Forecast | `PLAN_FORECAST` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Process Mid Month Payment | `PROCESS_MID_MONTH_PAYMENT` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Process Payment | `PROCESS_PAYMENT` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Process Usage Payment | `PROCESS_USAGE_PAYMENT` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Reconcile | `RECONCILE` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Reconcile Receipt | `RECONCILE_RECEIPT` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Recovery Setup | `RECOVERY_SETUP` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Update Escrow | `UPDATE_ESCROW` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |

## Migration engineer's notes: fields worth a second look

Contract is the one entity ASG Edge+ has already built against, so beyond the field inventory above, here is what stands out structurally for anyone mapping this table to the Edge+ schema.

### Fields that encode business rules directly (Approval / Workflow / Trigger)

No field on Contract itself carries "Approval", "Workflow", or "Trigger" in its label or internal name — those concepts live one level down, on `ExpenseRecovery` (`Approval Status`), the `WorkFlow*` family, and similar "Approval Status" fields on `AccrualTransaction`/`PaymentTransaction`-adjacent entities. What Contract *does* carry directly is **32 `sTYPE_SUBMITBUTTON` fields** (all under the `Summary Information / Summary Page Buttons` subgroup, visible at the bottom of the table above — Generate Rent, Generate 842 Rent Schedule, Generate IFRS 16 Rent Schedule, Reconcile, Process Payment, Delete Payments, Apply Offsets, CPI Adjustments, Recovery Setup, etc.). These aren't data at all — each is an executable server-side operation exposed as if it were a form field. A migration needs to model each as a **command/action**, not a persisted attribute, and needs to confirm what permission model (if any) gates who can fire them.

### Fields with a dropdown / master-list dependency

Three distinct dropdown mechanisms are visible on Contract, cross-referenced against [006-manage-custom-lists.md](../admin/006-manage-custom-lists.md) and [007-firm-and-client-drop-downs.md](../admin/007-firm-and-client-drop-downs.md):

| Mechanism | Count on Contract | Examples | Likely target catalog (007) |
|---|---:|---|---|
| `sCODE_*` (Global) | 11 | `Contract Status`, `Contract Type`, `Contract Category`, `Contract Group`, `Contract Use`, `Currency Type`, `Agreement Type`, `Asset Class`, `Building Area Unit`, `Holding Interest`, `Proration Method` | Fixed, platform-defined **Firm Drop Downs** (207-entry catalog; edit-only for a tenant) |
| `sTYPE_CUSTOM_CODE_FIELD` (Firm) | 31 | all `Firm_CAM*`, `Firm_RET*`, `Firm_ONCOT*`, `Firm_OPCOT*` fields, plus `Firm_Brand`, `Firm_CostCenter`, `Firm_FranchiseLocation`, `Firm_Guarantor`, `Firm_LeaseStatus`, `Firm_TenantLegalName` | The **"Contract drop downs"** Drop Down Types category (one of the six values in 006's Custom List field editor) |
| `sTYPE_CLIENT_LISTS` (Firm) | 5 | `Firm_DefaultLog`, `Firm_Funds`, `Firm_OperatingExpenses`, `Firm_ReconciliationLog`, `Firm_SavingsLog` | The **"Custom Drop downs"** category — i.e. the tenant-extensible **Client/Custom Drop Downs** catalog (`CustomCodeTableEdit.jsp`), a *different* store than the row above |

The last distinction matters for migration: `sTYPE_CUSTOM_CODE_FIELD` and `sTYPE_CLIENT_LISTS` fields look similar (both are Firm-scope, both render as dropdowns) but per 007's analysis they likely resolve against two structurally different list stores — one a fixed platform category, the other a tenant-extensible one with full CRUD. Neither mapping was directly re-verified by opening the field editor for a Contract field specifically (007 flags this as unresolved); treat it as inferred, not confirmed, and verify before building an automated migration mapping.

### Fields that look deprecated or legacy

No field on Contract uses an explicit `DoNotUse`/`Old`/`Temp` naming convention, but two are structurally suspicious enough to warrant asking ASG directly before carrying them forward:

- **`zLeaseSquareFootage`** (internal name `zFirm_LeaseSquareFootage`, Firm scope, `sTYPE_NUMBER_FRACTION2DIGITS`) — the leading lowercase `z` is a common convention for sorting a field to the bottom of a picker/column list, and is frequently used to mark a field as superseded-but-kept-for-historical-data. No other field in the Firm namespace uses this convention, which makes it stand out rather than look like a house style.
- **`currPaymentRate`** (internal name `math_currPaymentRate_9`, Global scope, `sTYPE_MONEY_MATH_OPERATION`) — the `math_` prefix and trailing `_9` suffix are consistent with an internally-generated calculation-engine artifact name rather than an author-assigned field name. Every other computed field on Contract uses a normal PascalCase internal name (e.g. `AggregateNNNBaseRentNPV`), so this one is worth confirming is still live rather than an orphaned intermediate calculation slot.
- **Not believed to be deprecated, flagged only to pre-empt a false positive:** the six `Test #1 Result` … `Test #5b Result` fields plus `Latest Financial Test Result` are real lease-classification/covenant financial test outputs (consistent with ASC 842 / IFRS 16 classification testing), not test/debug artifacts — "Test" here is domain terminology, not a code smell.

