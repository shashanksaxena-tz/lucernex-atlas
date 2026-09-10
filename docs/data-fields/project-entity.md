# ProjectEntity — Data Fields

The generic 'project' record used for capital projects, store rollouts, and portfolio initiatives — distinct from Contract, it tracks phase-gate status (Design, Construction, Possession, Operations) via parallel status/date pairs and milestone pointers, plus `SUBMITBUTTON` action fields for phase transitions. It spans four top-level groups (Milestones, Schedule, Statics, Summary Information), which is unusual and reflects that a 'project' is a cross-cutting concept touched by scheduling, milestone tracking, and portfolio reporting rather than owned by a single functional group. 170 fields.

**Table Association:** `ProjectEntity` &nbsp;·&nbsp; **Total fields:** 170 (Global: 165, Firm: 5)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Completed Phase Status | `CompletedPhaseStatus` | `sTYPE_TEXT` | Global | No | No |  | Milestones / Summary |
| Construction Phase Status | `ConstructionPhaseStatus` | `sTYPE_TEXT` | Global | No | No |  | Milestones / Summary |
| Current Milestone | `CurrentMilestone` | `sTYPE_PROCESS_TIMELINE` | Global | No | No |  | Milestones / Summary |
| Design Phase Status | `DesignPhaseStatus` | `sTYPE_TEXT` | Global | No | No |  | Milestones / Summary |
| Milestone Timeline | `MilestoneTimeline` | `sTYPE_TEXT` | Global | No | No |  | Milestones / Summary |
| Next Milestone | `NextMilestone` | `sTYPE_PROCESS_TIMELINE` | Global | No | No |  | Milestones / Summary |
| Operations Phase Status | `OperationsPhaseStatus` | `sTYPE_TEXT` | Global | No | No |  | Milestones / Summary |
| Possession Phase Status | `PossessionPhaseStatus` | `sTYPE_TEXT` | Global | No | No |  | Milestones / Summary |
| Previous Milestone | `PreviousMilestone` | `sTYPE_PROCESS_TIMELINE` | Global | No | No |  | Milestones / Summary |
| Real Estate Phase Status | `RealEstatePhaseStatus` | `sTYPE_TEXT` | Global | No | No |  | Milestones / Summary |
| Baseline End Date | `OriginalEndDate` | `sTYPE_DATE` | Global | No | No |  | Schedule / Summary Information |
| Baseline Start Date | `OriginalStartDate` | `sTYPE_DATE` | Global | No | No |  | Schedule / Summary Information |
| Forecast/Actual Start Date | `ActualStartDate` | `sTYPE_DATE` | Global | No | No |  | Schedule / Summary Information |
| Last Updated Date | `ClientScheduleLastReviewedDate` | `sTYPE_DATE` | Global | No | No |  | Schedule / Summary Information |
| DefinedField1 | `DefinedField1` | `sTYPE_TEXT` | Global | No | No |  | Statics / Hidden |
| DefinedField2 | `DefinedField2` | `sTYPE_TEXT` | Global | No | No |  | Statics / Hidden |
| JavaScript Value | `JavaScriptValue` | `sTYPE_JAVASCRIPT_FIELD` | Global | No | No |  | Statics / Hidden |
| Annual Variance | `AnnualVariance` | `sTYPE_ANNUAL_VARIANCE` | Global | No | No |  | Statics / Layout |
| Blank Row | `BlankRow` | `sTYPE_BLANK_ROW` | Global | No | No |  | Statics / Layout |
| Blank Space | `BlankSpace` | `sTYPE_BLANK_SPACE` | Global | No | No |  | Statics / Layout |
| Budget Total | `BudgetTotal` | `sTYPE_BUDGET_COLUMN_TOTAL` | Global | No | No |  | Statics / Layout |
| Date | `CurrentDate` | `sTYPE_CURRENT_DATE` | Global | No | No |  | Statics / Layout |
| Date Comparison: | `DateComparison` | `sTYPE_DATE_MATH_OPERATION` | Global | No | No |  | Statics / Layout |
| Geo Map | `Ymap` | `sTYPE_YMAP` | Global | No | No |  | Statics / Layout |
| Many to Many List | `ManyToManyList` | `sTYPE_MANYTOMANY_LIST` | Global | No | No |  | Statics / Layout |
| Math ($): | `MoneyMathOperation` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Statics / Layout |
| Math (%): | `PercentMathOperation` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Statics / Layout |
| Math: | `MathOperation` | `sTYPE_MATH_OPERATION` | Global | No | No |  | Statics / Layout |
| Month | `Month` | `sTYPE_MONTH` | Global | No | No |  | Statics / Layout |
| Months | `AllMonths` | `sTYPE_ALLMONTHS` | Global | No | No |  | Statics / Layout |
| Months with Data | `MonthsWithData` | `sTYPE_MONTHS_WITH_DATA` | Global | No | No |  | Statics / Layout |
| One to Many List | `OneToManyList` | `sTYPE_ONETOMANY_LIST` | Global | No | No |  | Statics / Layout |
| Page Break | `PageBreakForPrint` | `sTYPE_PAGEBREAK` | Global | No | No |  | Statics / Layout |
| Periods | `AllPeriods` | `sTYPE_ALLPERIODS` | Global | No | No |  | Statics / Layout |
| Qtrs | `AllQuarters` | `sTYPE_ALLQUARTERS` | Global | No | No |  | Statics / Layout |
| Quarterly Variance | `QuarterVariance` | `sTYPE_QUARTER_VARIANCE` | Global | No | No |  | Statics / Layout |
| Semi-Annual Variance | `SemiAnnualVariance` | `sTYPE_SEMIANNUAL_VARIANCE` | Global | No | No |  | Statics / Layout |
| Slide Show | `SlideShow` | `sTYPE_DOCUMENT_SLIDESHOW` | Global | No | No |  | Statics / Layout |
| Static Text | `StaticText` | `sTYPE_STATICTEXT_LABEL` | Global | No | No |  | Statics / Layout |
| Sub Edit Form | `SubEditForm` | `sTYPE_SUB_EDITFORM` | Global | No | No |  | Statics / Layout |
| Time Comparison | `TimeComparison` | `sTYPE_TIME_MATH_OPERATION` | Global | No | No |  | Statics / Layout |
| Total Math | `TotalMath` | `sTYPE_TOTAL_MATH_OPERATION` | Global | No | No |  | Statics / Layout |
| Years | `Years` | `sTYPE_YEARS` | Global | No | No |  | Statics / Layout |
| Years with Data | `YearsWithData` | `sTYPE_YEARS_WITH_DATA` | Global | No | No |  | Statics / Layout |
| Comparison List | `ComparisonList` | `sTYPE_COMPARISONLIST` | Global | No | No |  | Summary Information / Comparison Report |
| Client Request Log | `Firm_ClientRequestLog` | `sTYPE_CLIENT_LISTS` | Firm | No | No |  | Summary Information / Custom Lists |
| Budget Template ID | `BudgetTemplateID` | `sTYPE_BUDGET_TEMPLATE` | Global | No | No |  | Summary Information / General Summary Information |
| Building Area Unit | `CodeBuildingAreaUnitID` | `sCODE_BUILDING_AREA_UNIT` | Global | No | No |  | Summary Information / General Summary Information |
| Capital Program | `ProgramID` | `sTYPE_CAPITALPROGRAM` | Global | No | No |  | Summary Information / General Summary Information |
| City | `City` | `sTYPE_TEXT` | Global | No | No |  | Summary Information / General Summary Information |
| City, State | `CityStateProvinceCountry` | `sTYPE_CITY` | Global | No | No |  | Summary Information / General Summary Information |
| Client Unique ID | `MapClientRecordID` | `sTYPE_TEXT` | Global | No | No |  | Summary Information / General Summary Information |
| Complex Name | `ComplexID` | `sTYPE_COMPLEX` | Global | No | No |  | Summary Information / General Summary Information |
| Construction Type | `CodeConstructionTypeID` | `sCODE_CONSTRUCTION_TYPE` | Global | No | No |  | Summary Information / General Summary Information |
| Contact List | `LinkProjectEntityContactListData` | `sTYPE_PE_CONTACTEMPLOYER_LIST` | Global | No | No |  | Summary Information / General Summary Information |
| Country | `CountryID` | `sTYPE_COUNTRY` | Global | No | No |  | Summary Information / General Summary Information |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Summary Information / General Summary Information |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Summary Information / General Summary Information |
| Cross Street #1 | `CrossStreet1` | `sTYPE_TEXT` | Global | No | No |  | Summary Information / General Summary Information |
| Cross Street #2 | `CrossStreet2` | `sTYPE_TEXT` | Global | No | No |  | Summary Information / General Summary Information |
| Currency Type | `CodeCurrencyTypeID` | `sCODE_CURRENCY_TYPE` | Global | No | No |  | Summary Information / General Summary Information |
| Deal Type | `CodeDealTypeID` | `sCODE_DEAL_TYPE` | Global | No | No |  | Summary Information / General Summary Information |
| Demographic DMA | `DemographicDMAID` | `sTYPE_DMA` | Global | No | No |  | Summary Information / General Summary Information |
| Depth | `Depth` | `sTYPE_AREA` | Global | No | No |  | Summary Information / General Summary Information |
| Description | `ProjectDescription` | `sTYPE_TEXT` | Global | No | No |  | Summary Information / General Summary Information |
| Distribution Center | `CodeDistributionCenterID` | `sCODE_DISTRIBUTION_CENTER` | Global | No | No |  | Summary Information / General Summary Information |
| Entity Email | `EntityEmail` | `sTYPE_ENTITY_EMAIL` | Global | No | No |  | Summary Information / General Summary Information |
| Entity LxID | `EntityId` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Summary Information / General Summary Information |
| Entity Photo | `EntityPhoto` | `sTYPE_TEXT` | Global | No | No |  | Summary Information / General Summary Information |
| Entity RecID | `ProjectEntityID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Summary Information / General Summary Information |
| Entity Type | `ProjectEntityTypeName` | `sTYPE_TEXT` | Global | No | No |  | Summary Information / General Summary Information |
| Entity UUID | `UUID` | `sTYPE_TEXT` | Global | No | No |  | Summary Information / General Summary Information |
| Facility Name | `FacilityName` | `sTYPE_ENTITY_NAME` | Global | No | No |  | Summary Information / General Summary Information |
| Firm ID | `FirmID` | `sTYPE_TEXT` | Global | Yes | No |  | Summary Information / General Summary Information |
| Frontage | `Frontage` | `sTYPE_AREA` | Global | No | No |  | Summary Information / General Summary Information |
| Full Address | `HTMLAddress` | `sTYPE_TEXT` | Global | No | No |  | Summary Information / General Summary Information |
| Gross Acreage | `GrossArea` | `sTYPE_ACREAGE` | Global | No | No |  | Summary Information / General Summary Information |
| Gross Area | `GrossArea` | `sTYPE_AREA` | Global | No | No |  | Summary Information / General Summary Information |
| Is Dead? | `IsDead` | `sTYPE_CHECKBOX` | Global | No | No |  | Summary Information / General Summary Information |
| Is Inactive? | `Inactive` | `sTYPE_CHECKBOX` | Global | Yes | No |  | Summary Information / General Summary Information |
| Issues And Alerts | `IssuesAndAlerts` | `sTYPE_TEXT` | Global | No | No |  | Summary Information / General Summary Information |
| Jurisdiction | `JurisdictionID` | `sTYPE_JURISDICTION` | Global | No | No |  | Summary Information / General Summary Information |
| Latitude | `LatitudeDegrees` | `sTYPE_NUMBER_FRACTION6DIGITS` | Global | No | No |  | Summary Information / General Summary Information |
| Location | `LocationID` | `sTYPE_LOCATION` | Global | No | No |  | Summary Information / General Summary Information |
| Longitude | `LongitudeDegrees` | `sTYPE_NUMBER_FRACTION6DIGITS` | Global | No | No |  | Summary Information / General Summary Information |
| Market Area | `CodeMarketAreaID` | `sCODE_MARKET_AREA` | Global | No | No |  | Summary Information / General Summary Information |
| Market Potential | `CodeDesc_CodeMarketAreaID` | `sCODE_MARKET_AREA` | Global | No | No |  | Summary Information / General Summary Information |
| Market Type | `CodeMarketTypeID` | `sCODE_MARKET_TYPE` | Global | No | No |  | Summary Information / General Summary Information |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Summary Information / General Summary Information |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Summary Information / General Summary Information |
| Name | `ProjectEntityName` | `sTYPE_ENTITY_NAME` | Global | Yes | No |  | Summary Information / General Summary Information |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Summary Information / General Summary Information |
| Number of Documents | `NumberOfDocuments` | `sTYPE_NUMBER` | Global | No | No |  | Summary Information / General Summary Information |
| Parent Region | `RootRegionID` | `sTYPE_ROOT_REGION` | Global | No | No |  | Summary Information / General Summary Information |
| Phone | `Phone` | `sTYPE_TEXT` | Global | No | No |  | Summary Information / General Summary Information |
| Portfolio | `ProgramID` | `sTYPE_PORTFOLIO` | Global | No | No |  | Summary Information / General Summary Information |
| Portfolio/Program | `ProgramID` | `sTYPE_PROGRAM` | Global | No | No |  | Summary Information / General Summary Information |
| Portfolio/Program Name | `ProgramName` | `sTYPE_TEXT` | Global | No | No |  | Summary Information / General Summary Information |
| Portfolio/Program RecID | `ProgramID` | `sTYPE_TEXT` | Global | No | No |  | Summary Information / General Summary Information |
| Postal Code | `PostalCode` | `sTYPE_POSTALCODE` | Global | No | No |  | Summary Information / General Summary Information |
| Project Managers | `ManagerIDList` | `sTYPE_PROJECT_MANAGER` | Global | No | No |  | Summary Information / General Summary Information |
| Project Name | `ProjectName` | `sTYPE_ENTITY_NAME` | Global | No | No |  | Summary Information / General Summary Information |
| Project Phase | `CurrentCodeProjectPhaseID` | `sCODE_PROJECT_PHASE` | Global | No | No |  | Summary Information / General Summary Information |
| Project Status | `CurrentPhaseStatus` | `sTYPE_TEXT` | Global | No | No |  | Summary Information / General Summary Information |
| Project Type | `CodeProjectTypeID` | `sCODE_PROJECT_TYPE` | Global | No | No |  | Summary Information / General Summary Information |
| Prototype | `PrototypeID` | `sTYPE_PROTOTYPE` | Global | No | No |  | Summary Information / General Summary Information |
| Prototype Name | `PrototypeName` | `sTYPE_TEXT` | Global | No | No |  | Summary Information / General Summary Information |
| Real Estate Type | `CodeDesc_CodeProjectTypeID` | `sCODE_PROJECT_TYPE` | Global | No | No |  | Summary Information / General Summary Information |
| Region | `RegionID` | `sTYPE_REGION` | Global | No | No |  | Summary Information / General Summary Information |
| Related Entities | `RelatedEntities` | `sTYPE_TEXT` | Global | No | No |  | Summary Information / General Summary Information |
| RelocatedFrom | `RelocatedFrom` | `sTYPE_TEXT` | Global | No | No |  | Summary Information / General Summary Information |
| Rentable Area | `RentableArea` | `sTYPE_AREA` | Global | No | No |  | Summary Information / General Summary Information |
| Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Summary Information / General Summary Information |
| Revenue Weeks | `ActualRevenueWeeks` | `sTYPE_NUMBER` | Global | No | No |  | Summary Information / General Summary Information |
| Sales Report Logo | `Firm_SalesReportLogo` | `sTYPE_FIRM_LOGO` | Firm | No | No |  | Summary Information / General Summary Information |
| Sales Report Signature | `Firm_SalesReportSignature` | `sTYPE_FIRM_LOGO` | Firm | No | No |  | Summary Information / General Summary Information |
| Sales Report Signature Name | `Firm_SalesReportSignatureName` | `sTYPE_TEXT` | Firm | No | No | TBD | Summary Information / General Summary Information |
| Sales Report Signature Title | `Firm_SalesReportSignatureTitle` | `sTYPE_TEXT` | Firm | No | No | TBD | Summary Information / General Summary Information |
| Schedule Creation Method | `TaskCreationMethod` | `sTYPE_TASK_CREATION_METHOD` | Global | No | No |  | Summary Information / General Summary Information |
| Sequence Number | `SequenceNumber` | `sTYPE_NUMBER` | Global | No | No |  | Summary Information / General Summary Information |
| Site Name | `PotentialProjectName` | `sTYPE_ENTITY_NAME` | Global | No | No |  | Summary Information / General Summary Information |
| State | `IStateProvinceCountryID` | `sTYPE_STATE_PROVINCE` | Global | No | No |  | Summary Information / General Summary Information |
| Storage Size (MB) | `DBFolderSizeMB` | `sTYPE_NUMBER_FRACTION2DIGITS` | Global | No | No |  | Summary Information / General Summary Information |
| Store Number | `ClientEntityID` | `sTYPE_TEXT` | Global | No | No |  | Summary Information / General Summary Information |
| Street Address | `StreetAddress` | `sTYPE_TEXT` | Global | No | No |  | Summary Information / General Summary Information |
| Street Address #1 | `StreetAddress1` | `sTYPE_TEXT` | Global | No | No |  | Summary Information / General Summary Information |
| Street Address #2 | `StreetAddress2` | `sTYPE_TEXT` | Global | No | No |  | Summary Information / General Summary Information |
| Street Address #3 | `StreetAddress3` | `sTYPE_TEXT` | Global | No | No |  | Summary Information / General Summary Information |
| Street Address #4 | `StreetAddress4` | `sTYPE_TEXT` | Global | No | No |  | Summary Information / General Summary Information |
| Sub Region | `SubRegionID` | `sTYPE_SUBREGION` | Global | No | No |  | Summary Information / General Summary Information |
| System of Record | `BaseProvider` | `sTYPE_VALUES_PROVIDER` | Global | No | No |  | Summary Information / General Summary Information |
| Third Party Warehouse | `ThirdPartyWarehouse` | `sTYPE_TEXT` | Global | No | No |  | Summary Information / General Summary Information |
| Time Zone | `TimeZone` | `sTYPE_TIMEZONE` | Global | No | No |  | Summary Information / General Summary Information |
| Trade Area | `TradeArea` | `sTYPE_TEXT` | Global | No | No |  | Summary Information / General Summary Information |
| Usable Area | `UsableArea` | `sTYPE_AREA` | Global | No | No |  | Summary Information / General Summary Information |
| Actual/Forecast Delivery Date | `ActualEndDate` | `sTYPE_DATE` | Global | No | No |  | Summary Information / Summary Dates |
| Actual/Forecast Delivery Period/Year | `ActualEndDate` | `sTYPE_PERIOD_YEAR` | Global | No | No |  | Summary Information / Summary Dates |
| Actual/Forecast Delivery Qtr/Year | `ActualEndDate` | `sTYPE_QUARTERS_YEAR` | Global | No | No |  | Summary Information / Summary Dates |
| Actual/Forecast Delivery Year | `ActualEndDate` | `sTYPE_FISCAL_YEAR` | Global | No | No |  | Summary Information / Summary Dates |
| Baseline Delivery Date | `BaselineEndDate` | `sTYPE_DATE` | Global | No | No |  | Summary Information / Summary Dates |
| Baseline Delivery Period/Year | `BaselineEndDate` | `sTYPE_PERIOD_YEAR` | Global | No | No |  | Summary Information / Summary Dates |
| Baseline Delivery Qtr/Year | `BaselineEndDate` | `sTYPE_QUARTERS_YEAR` | Global | No | No |  | Summary Information / Summary Dates |
| Baseline Delivery Year | `BaselineEndDate` | `sTYPE_FISCAL_YEAR` | Global | No | No |  | Summary Information / Summary Dates |
| Original Delivery Date | `ExpectedEndDate` | `sTYPE_DATE` | Global | No | No |  | Summary Information / Summary Dates |
| Original Delivery Period/Year | `ExpectedEndDate` | `sTYPE_PERIOD_YEAR` | Global | No | No |  | Summary Information / Summary Dates |
| Original Delivery Qtr/Yr | `ExpectedEndDate` | `sTYPE_QUARTERS_YEAR` | Global | No | No |  | Summary Information / Summary Dates |
| Original Delivery Year | `ExpectedEndDate` | `sTYPE_FISCAL_YEAR` | Global | No | No |  | Summary Information / Summary Dates |
| RE Planner Open Date | `SlotEndDate` | `sTYPE_DATE` | Global | No | No |  | Summary Information / Summary Dates |
| RE Planner Open Period/Year | `SlotEndDate` | `sTYPE_PERIOD_YEAR` | Global | No | No |  | Summary Information / Summary Dates |
| RE Planner Open Qtr/Yr | `SlotEndDate` | `sTYPE_QUARTERS_YEAR` | Global | No | No |  | Summary Information / Summary Dates |
| RE Planner Open Year | `SlotEndDate` | `sTYPE_FISCAL_YEAR` | Global | No | No |  | Summary Information / Summary Dates |
| Activate/Deactivate | `ActivateAndDeactivateButton` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Approve Asset Payments | `APPROVE_ASSET_PAYMENTS` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Approve Payments | `APPROVE_PAYMENTS` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Cancel | `CancelButton` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Convert Entity | `ConvertIGenericProject` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Dead / Not Dead | `MarkDeadAndMarkNotDeadButton` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Delete | `DeleteButton` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Extend Asset Contracts | `EXTEND_ASSET_CONTRACTS` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Extend Asset Payments | `EXTEND_ASSET_PAYMENTS` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Extend Contracts | `EXTEND_CONTRACTS` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Financial Model | `FinancialModel` | `sTYPE_FINANCIALMODEL` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Help | `HELP` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Import CPI Data | `IMPORT_CPI_DATA` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Lx Contract Abstractor | `KIMVIO` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Month & Year Selector | `MonthYearSelection` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Period & Year Selector | `PeriodYearSelection` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| RE Transaction Wizard | `RETransactionWizard` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Run Report Action | `RunReportAction` | `sTYPE_ACTION_RUN_REPORT` | Global | No | No |  | Summary Information / Summary Page Buttons |
| Submit | `FormSubmitButton` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
