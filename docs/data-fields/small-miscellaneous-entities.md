# Small / Miscellaneous Entities

These 38 tables (332 fields, all Global) are the remainder after the other seven thematic buckets were pulled out — each is a real, distinct business entity (a holiday calendar, a CPI reading, a development plan, a bid-package Q&A thread) but with too few fields (1-14) and too little in common with its neighbors to justify either a standalone file or a more specific bucket. They are ordered below by field count, largest first, so the more substantial ones surface first.

**Entities in this file:** 38 &nbsp;·&nbsp; **Total fields:** 332 (Global: 332, Firm: 0)

| Entity | Fields (G/F) | One-line role |
|---|---|---|
| `ExpenseAllocation` | 14 (14/0) | Splits one recoverable expense across multiple contracts/entities by percentage — the allocation record for shared-building expenses. |
| `PropertyTaxDetail` | 14 (14/0) | Free-form notes detail attached to a Parcel's property tax record. |
| `ProgramRevenueWeeks` | 14 (14/0) | Weekly revenue-target tracking (filled/unfilled targets and weeks) for a development Program, feeding DevelopmentSlot planning. |
| `TaskPredecessor` | 14 (14/0) | Defines a dependency between two Task records, with actual lead/lag days — the scheduling-network edge beneath Task. |
| `PayApp` | 14 (14/0) | An AIA-style payment application against a construction contract — invoice retainage and cost-tracking variance. |
| `EMailReceivedLog` | 14 (14/0) | A logged inbound email tied to a record — arrival date and body, the source EMailReceivedLog rows LinkEMailReceivedLogDocument attaches Documents to. |
| `AllowanceTransaction` | 13 (13/0) | An individual draw/payment transaction against an Allowance — due date and linkage back to the Allowance and Contract. |
| `VirtualExpAccrualForecastPeriod` | 13 (13/0) | A computed forward forecast of an expense accrual by period, referencing the ExpenseAccrualSchedule/Setup it projects from. |
| `VirtualUBRPAggregate` | 13 (13/0) | An aggregated projection of use-based-rent obligation across a contract term, the use-based-rent counterpart to VirtualPRPAggregate. |
| `Usage` | 13 (13/0) | A recorded consumption/usage reading against a contract on a given posting date, feeding usage-based rent calculations. |
| `Question` | 13 (13/0) | A question posted during a bid Q&A process, with published/private visibility flags — the counterpart IssueResponse replies to. |
| `HolidayDate` | 12 (12/0) | One calendar date within a HolidaySchedule. |
| `EscalationIndex` | 12 (12/0) | A named index value series (e.g., a specific published CPI series) used to drive ExpenseEscalation calculations. |
| `StateProvinceCountry` | 11 (11/0) | Master geography reference with ISO Alpha-2/3 country codes, backing every address field across Facility, Location, and Parcel. |
| `Party` | 11 (11/0) | A generic company/contact reference tied to a Contract, used where the role doesn't fit Employer or Person specifically. |
| `MapClientSchedule` | 11 (11/0) | Links a RETransaction/schedule to auto-push forecast behavior and percent-complete tracking. |
| `ProcessTimelineTemplate` | 10 (10/0) | A reusable milestone/phase template that ProcessTimeline instances are created from, with default phase-status labels. |
| `Jurisdiction` | 10 (10/0) | A tax/legal jurisdiction reference record, referenced by Facility, Parcel, and Location address blocks. |
| `CPI` | 9 (9/0) | A recorded Consumer Price Index value at a point in time, tied to a Contract, feeding CPI-indexed rent escalation. |
| `Ownership` | 9 (9/0) | Records a funding/ownership percentage and type for an entity in a land purchase, supporting multi-party purchases. |
| `ExchangeRate` | 8 (8/0) | A currency exchange rate captured at a point in time for a Contract, supporting multi-currency financial calculations. |
| `HolidaySchedule` | 8 (8/0) | A named calendar of holidays (the header record for HolidayDate), used in schedule/task date calculations. |
| `ComparisonItem` | 8 (8/0) | One line in a competitive/market comparison analysis, with a computed value and expense-group total. |
| `PartPackageItem` | 7 (7/0) | One part within a PartPackage kit. |
| `RecalcOverrideNotes` | 6 (6/0) | A free-text note explaining why a financial recalculation was manually overridden — an audit-style justification field. |
| `DevelopmentPlan` | 6 (6/0) | A named development pipeline plan under RE Planner, the header record above DevelopmentSlot. |
| `Project` | 6 (6/0) | A lightweight project identity record (ID, RecID, UUID) distinct from the richer ProjectEntity, likely used for cross-system reference linking. |
| `PartPackage` | 6 (6/0) | A named kit/bundle of parts, the header record above PartPackageItem. |
| `ReportGroupData` | 5 (5/0) | Platform metadata for a top-level or subgroup node in this very Data Fields hierarchy — parent group name and firm scoping. |
| `ExpenseRecoveryItemMapping` | 5 (5/0) | Maps an ExpenseRecoveryItem to an external invoice line item name and a JSON configuration blob, likely supporting invoice-import matching. |
| `Issue` | 4 (4/0) | A bid-package issue/question thread header — date range and type, the object Question and IssueResponse attach to. |
| `InformationOverlay` | 4 (4/0) | Configuration for an in-app guided-tour/tooltip overlay — tour name, field name list, and expiration date. |
| `GlobalProperty` | 4 (4/0) | A generic firm-scoped key/value configuration setting, organized by property section — a low-level settings-store table. |
| `MapClientBudget` | 3 (3/0) | Links a ProjectEntity to its budget with a last-reviewed-date stamp. |
| `ComparisonReport` | 3 (3/0) | A saved competitive-comparison report with its own assigned page layout. |
| `Site` | 3 (3/0) | A minimal site-identity stub (ID, RecID, UUID only) used for cross-system reference rather than data capture. |
| `CommitteePackage` | 1 (1/0) | A single-field stub representing a committee-review package record (see LinkCommPkgTemplDocContent). |
| `EntityTemplate` | 1 (1/0) | A single-field stub representing a reusable entity-setup template, referenced by TemplateAudit. |

Field type codes are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Entity | Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|---|
| ExpenseAllocation | Allocation ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Expense Allocation |
| ExpenseAllocation | Allocation Percentage | `AllocationPercentage` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Expense Allocation |
| ExpenseAllocation | Allocation RecID | `ExpenseAllocationID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Expense Allocation |
| ExpenseAllocation | Begin Date | `BeginDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Expense Allocation |
| ExpenseAllocation | Contract | `ContractID` | `sTYPE_CONTRACT` | Global | Yes | No |  | Contract / Expense Allocation |
| ExpenseAllocation | Effective Date | `EffectiveDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Expense Allocation |
| ExpenseAllocation | End Date | `EndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Expense Allocation |
| ExpenseAllocation | Equipment | `AssetID` | `sTYPE_EQUIPMENT` | Global | No | No |  | Contract / Expense Allocation |
| ExpenseAllocation | Equipment Associated Entity | `AssetAssociatedProjectEntityID` | `sTYPE_MIXEDENTITY` | Global | No | No |  | Contract / Expense Allocation |
| ExpenseAllocation | Expense Setup | `ExpenseSetupID` | `sTYPE_EXPENSE_SETUP` | Global | No | No |  | Contract / Expense Allocation |
| ExpenseAllocation | Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Expense Allocation |
| ExpenseAllocation | Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Expense Allocation |
| ExpenseAllocation | Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Expense Allocation |
| ExpenseAllocation | Organization | `OrganizationID` | `sTYPE_ORGANIZATION` | Global | No | No |  | Contract / Expense Allocation |
| PropertyTaxDetail | Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Parcel / Property Tax Detail |
| PropertyTaxDetail | Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Parcel / Property Tax Detail |
| PropertyTaxDetail | Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Parcel / Property Tax Detail |
| PropertyTaxDetail | Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Parcel / Property Tax Detail |
| PropertyTaxDetail | Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Parcel / Property Tax Detail |
| PropertyTaxDetail | Parcel | `ParcelID` | `sTYPE_PARCEL` | Global | Yes | No |  | Parcel / Property Tax Detail |
| PropertyTaxDetail | Property Tax Bill | `PropertyTaxBillID` | `sTYPE_PROPERTY_TAX_BILL` | Global | Yes | No |  | Parcel / Property Tax Detail |
| PropertyTaxDetail | Property Tax Detail ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Parcel / Property Tax Detail |
| PropertyTaxDetail | Property Tax Detail RecID | `PropertyTaxDetailID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Parcel / Property Tax Detail |
| PropertyTaxDetail | Rate? | `RateFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Parcel / Property Tax Detail |
| PropertyTaxDetail | Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Parcel / Property Tax Detail |
| PropertyTaxDetail | Tax Amount | `TaxAmount` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Property Tax Detail |
| PropertyTaxDetail | Tax Rate | `TaxRate` | `sTYPE_PERCENTAGE` | Global | No | No |  | Parcel / Property Tax Detail |
| PropertyTaxDetail | Tax Type | `CodeTaxTypeID` | `sCODE_TAX_TYPE` | Global | No | No |  | Parcel / Property Tax Detail |
| ProgramRevenueWeeks | Current Filled Targets | `NumberCurrentFilledSlots` | `sTYPE_NUMBER` | Global | No | No |  | RE Planner / RE Planner info |
| ProgramRevenueWeeks | Current Filled Weeks | `NumberCurrentFilledWeeks` | `sTYPE_NUMBER` | Global | No | No |  | RE Planner / RE Planner info |
| ProgramRevenueWeeks | Current Targets | `NumberCurrentTotalSlots` | `sTYPE_NUMBER` | Global | No | No |  | RE Planner / RE Planner info |
| ProgramRevenueWeeks | Current Unfilled Targets | `NumberCurrentUnfilledSlots` | `sTYPE_NUMBER` | Global | No | No |  | RE Planner / RE Planner info |
| ProgramRevenueWeeks | Current Unfilled Weeks | `NumberCurrentUnfilledWeeks` | `sTYPE_NUMBER` | Global | No | No |  | RE Planner / RE Planner info |
| ProgramRevenueWeeks | Current Weeks | `NumberCurrentTotalWeeks` | `sTYPE_NUMBER` | Global | No | No |  | RE Planner / RE Planner info |
| ProgramRevenueWeeks | Goal Targets | `NumberOfSlots` | `sTYPE_NUMBER` | Global | Yes | No |  | RE Planner / RE Planner info |
| ProgramRevenueWeeks | Goal Weeks | `RevenueWeeks` | `sTYPE_NUMBER` | Global | Yes | No |  | RE Planner / RE Planner info |
| ProgramRevenueWeeks | Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | RE Planner / RE Planner info |
| ProgramRevenueWeeks | Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | RE Planner / RE Planner info |
| ProgramRevenueWeeks | Program Revenue Weeks ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | RE Planner / RE Planner info |
| ProgramRevenueWeeks | Program Revenue Weeks RecID | `ProgramRevenueWeeksID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | RE Planner / RE Planner info |
| ProgramRevenueWeeks | Fiscal Year | `FiscalYear` | `sTYPE_UNFORMATTED_NUMBER` | Global | Yes | No |  | Statics / Hidden |
| ProgramRevenueWeeks | Program Revenue Weeks Parent Program | `ProgramID` | `sTYPE_PROGRAM` | Global | Yes | No |  | Statics / Hidden |
| TaskPredecessor | Actual Lead Lag Days | `ActualLeadLagDays` | `sTYPE_NUMBER` | Global | Yes | No |  | Schedule / Task Predecessor |
| TaskPredecessor | Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Schedule / Task Predecessor |
| TaskPredecessor | Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Schedule / Task Predecessor |
| TaskPredecessor | Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Schedule / Task Predecessor |
| TaskPredecessor | Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Schedule / Task Predecessor |
| TaskPredecessor | Original Lead Lag Days | `OriginalLeadLagDays` | `sTYPE_NUMBER` | Global | Yes | No |  | Schedule / Task Predecessor |
| TaskPredecessor | Predecessor Task | `PredecessorTaskID` | `sTYPE_TASK` | Global | No | No |  | Schedule / Task Predecessor |
| TaskPredecessor | Predecessor Task Name | `PredecessorTemplateTaskName` | `sTYPE_TEXT` | Global | No | No |  | Schedule / Task Predecessor |
| TaskPredecessor | Projected Lead/Lag Days | `ProjectedLeadLagDays` | `sTYPE_NUMBER` | Global | Yes | No |  | Schedule / Task Predecessor |
| TaskPredecessor | Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Schedule / Task Predecessor |
| TaskPredecessor | Successor Task | `SuccessorTaskID` | `sTYPE_TASK` | Global | Yes | No |  | Schedule / Task Predecessor |
| TaskPredecessor | Task Lead Lag Type | `CodeTaskLeadLagTypeID` | `sCODE_TASK_LEAD_LAG_TYPE` | Global | Yes | No |  | Schedule / Task Predecessor |
| TaskPredecessor | Task Predecessor ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Schedule / Task Predecessor |
| TaskPredecessor | Task Predecessor RecID | `TaskPredecessorID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Schedule / Task Predecessor |
| PayApp | Cost Tracking Variance | `CostTrackingVariance` | `sTYPE_MONEY` | Global | No | No |  | Specialized Forms / Pay App |
| PayApp | Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Specialized Forms / Pay App |
| PayApp | Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Specialized Forms / Pay App |
| PayApp | Invoice Retainage | `RetainagePercent` | `sTYPE_PERCENTAGE` | Global | No | No |  | Specialized Forms / Pay App |
| PayApp | Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Specialized Forms / Pay App |
| PayApp | Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Specialized Forms / Pay App |
| PayApp | Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Specialized Forms / Pay App |
| PayApp | Pay App Amount | `PayAppAmount` | `sTYPE_MONEY` | Global | No | No |  | Specialized Forms / Pay App |
| PayApp | Pay App Sequence Number | `PayAppSequenceNumber` | `sTYPE_TEXT` | Global | No | No |  | Specialized Forms / Pay App |
| PayApp | Pay app ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Specialized Forms / Pay App |
| PayApp | Pay app Issue | `IssueID` | `sTYPE_ISSUE` | Global | Yes | No |  | Specialized Forms / Pay App |
| PayApp | Pay app RecID | `PayAppID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Specialized Forms / Pay App |
| PayApp | Related Purchase Order | `PurchaseOrderID` | `sTYPE_PURCHASE_ORDER` | Global | No | No |  | Specialized Forms / Pay App |
| PayApp | Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Specialized Forms / Pay App |
| EMailReceivedLog | Arrival Date | `ArrivalDate` | `sTYPE_DATE` | Global | No | No |  | Summary Information / In-bound Email |
| EMailReceivedLog | Body | `Body` | `sTYPE_TEXTAREA` | Global | No | No |  | Summary Information / In-bound Email |
| EMailReceivedLog | Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Summary Information / In-bound Email |
| EMailReceivedLog | Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Summary Information / In-bound Email |
| EMailReceivedLog | E-Mail Rcvd ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Summary Information / In-bound Email |
| EMailReceivedLog | E-Mail Rcvd RecID | `EMailReceivedLogID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Summary Information / In-bound Email |
| EMailReceivedLog | Is Critical? | `IsCritical` | `sTYPE_CHECKBOX` | Global | No | No |  | Summary Information / In-bound Email |
| EMailReceivedLog | Mail Service Event ID | `MailServiceEventID` | `sTYPE_TEXT` | Global | Yes | No |  | Summary Information / In-bound Email |
| EMailReceivedLog | Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Summary Information / In-bound Email |
| EMailReceivedLog | Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Summary Information / In-bound Email |
| EMailReceivedLog | Number Of Attachments | `NumberOfAttachments` | `sTYPE_NUMBER` | Global | Yes | No |  | Summary Information / In-bound Email |
| EMailReceivedLog | Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Summary Information / In-bound Email |
| EMailReceivedLog | Sender | `Sender` | `sTYPE_TEXTAREA` | Global | No | No |  | Summary Information / In-bound Email |
| EMailReceivedLog | Subject | `Subject` | `sTYPE_TEXTAREA` | Global | No | No |  | Summary Information / In-bound Email |
| AllowanceTransaction | Allowance | `AllowanceID` | `sTYPE_ALLOWANCE` | Global | Yes | No |  | Contract / Allowance Transaction |
| AllowanceTransaction | Allowance Transaction ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Allowance Transaction |
| AllowanceTransaction | Allowance Transaction RecID | `AllowanceTransactionID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Allowance Transaction |
| AllowanceTransaction | Contract | `ContractID` | `sTYPE_CONTRACT` | Global | Yes | No |  | Contract / Allowance Transaction |
| AllowanceTransaction | Due Date | `DueDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Allowance Transaction |
| AllowanceTransaction | Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Allowance Transaction |
| AllowanceTransaction | Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Allowance Transaction |
| AllowanceTransaction | Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Allowance Transaction |
| AllowanceTransaction | Penalty Amount | `PenaltyAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Allowance Transaction |
| AllowanceTransaction | Receive Amount | `ReceiveAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Allowance Transaction |
| AllowanceTransaction | Receive Date | `ReceiveDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Allowance Transaction |
| AllowanceTransaction | Request Amount | `RequestAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Allowance Transaction |
| AllowanceTransaction | Request Date | `RequestDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Allowance Transaction |
| VirtualExpAccrualForecastPeriod | Accrual Schedule | `ExpenseAccrualScheduleID` | `sTYPE_EXPENSE_ACCRUAL_SCHEDULE` | Global | No | No |  | Contract / Expense Accrual Forecast |
| VirtualExpAccrualForecastPeriod | Accrual Setup | `ExpenseAccrualSetupID` | `sTYPE_EXPENSE_ACCRUAL_SETUP` | Global | No | No |  | Contract / Expense Accrual Forecast |
| VirtualExpAccrualForecastPeriod | Accrual Type | `CodeAccrualTypeID` | `sCODE_ACCRUAL_TYPE` | Global | No | No |  | Contract / Expense Accrual Forecast |
| VirtualExpAccrualForecastPeriod | Begin Date | `BeginDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Expense Accrual Forecast |
| VirtualExpAccrualForecastPeriod | Contract | `ContractID` | `sTYPE_CONTRACT` | Global | No | No |  | Contract / Expense Accrual Forecast |
| VirtualExpAccrualForecastPeriod | Date Range | `DateRange` | `sTYPE_DATE_RANGE` | Global | No | No |  | Contract / Expense Accrual Forecast |
| VirtualExpAccrualForecastPeriod | End Date | `EndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Expense Accrual Forecast |
| VirtualExpAccrualForecastPeriod | Expense Category | `CodeExpenseCategoryID` | `sCODE_EXPENSE_CATEGORY` | Global | No | No |  | Contract / Expense Accrual Forecast |
| VirtualExpAccrualForecastPeriod | Expense Group | `CodeExpenseGroupID` | `sCODE_EXPENSE_GROUP` | Global | No | No |  | Contract / Expense Accrual Forecast |
| VirtualExpAccrualForecastPeriod | Expense Type | `CodeExpenseTypeID` | `sCODE_EXPENSE_TYPE` | Global | No | No |  | Contract / Expense Accrual Forecast |
| VirtualExpAccrualForecastPeriod | Fiscal Period | `Period` | `sTYPE_NUMBER` | Global | No | No |  | Contract / Expense Accrual Forecast |
| VirtualExpAccrualForecastPeriod | Fiscal Year | `Year` | `sTYPE_DROPDOWN_YEAR` | Global | No | No |  | Contract / Expense Accrual Forecast |
| VirtualExpAccrualForecastPeriod | Period Amount | `PeriodExpense` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Accrual Forecast |
| VirtualUBRPAggregate | Billing Frequency | `CodeBillingFrequencyID` | `sCODE_FREQUENCY` | Global | No | No |  | Contract / Use Based Rent Summary Schedule |
| VirtualUBRPAggregate | Contract | `ContractID` | `sTYPE_CONTRACT` | Global | No | No |  | Contract / Use Based Rent Summary Schedule |
| VirtualUBRPAggregate | Current Use Based Rent | `CurrentRentDue` | `sTYPE_MONEY` | Global | No | No |  | Contract / Use Based Rent Summary Schedule |
| VirtualUBRPAggregate | Current Use Based Rent Paid | `CurrentRentPaid` | `sTYPE_MONEY` | Global | No | No |  | Contract / Use Based Rent Summary Schedule |
| VirtualUBRPAggregate | Expense Group | `CodeExpenseGroupID` | `sCODE_EXPENSE_GROUP` | Global | No | No |  | Contract / Use Based Rent Summary Schedule |
| VirtualUBRPAggregate | Expense Type | `CodeExpenseTypeID` | `sCODE_EXPENSE_TYPE` | Global | No | No |  | Contract / Use Based Rent Summary Schedule |
| VirtualUBRPAggregate | Model Type | `CodeUseRentModelTypeID` | `sCODE_USE_RENT_MODEL_TYPE` | Global | No | No |  | Contract / Use Based Rent Summary Schedule |
| VirtualUBRPAggregate | Net Use Based Rent Due | `NetUseBasedRentDue` | `sTYPE_MONEY` | Global | No | No |  | Contract / Use Based Rent Summary Schedule |
| VirtualUBRPAggregate | Period Begin Date | `PeriodBeginDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Use Based Rent Summary Schedule |
| VirtualUBRPAggregate | Period End Date | `PeriodEndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Use Based Rent Summary Schedule |
| VirtualUBRPAggregate | Rent Year Begin Date | `RentYearBeginDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Use Based Rent Summary Schedule |
| VirtualUBRPAggregate | Rent Year End Date | `RentYearEndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Use Based Rent Summary Schedule |
| VirtualUBRPAggregate | Total Use Based Rent | `CurrentRentObligation` | `sTYPE_MONEY` | Global | No | No |  | Contract / Use Based Rent Summary Schedule |
| Usage | Contract | `ContractID` | `sTYPE_CONTRACT` | Global | Yes | No |  | Contract / Usage |
| Usage | Effective Date | `EffectiveDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Usage |
| Usage | Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Usage |
| Usage | Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Usage |
| Usage | Posting Date | `PostingDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Usage |
| Usage | Usage Category | `CodeUsageCategoryID` | `sCODE_USAGE_CATEGORY` | Global | No | No |  | Contract / Usage |
| Usage | Usage ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Usage |
| Usage | Usage Count | `UsageCount` | `sTYPE_NUMBER` | Global | No | No |  | Contract / Usage |
| Usage | Usage Group | `CodeUsageGroupID` | `sCODE_USAGE_GROUP` | Global | No | No |  | Contract / Usage |
| Usage | Usage RecID | `UsageID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Usage |
| Usage | Usage Share | `UsageShare` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Usage |
| Usage | Usage Type | `CodeUsageTypeID` | `sCODE_USAGE_TYPE` | Global | No | No |  | Contract / Usage |
| Usage | Usage Unit Type | `CodeUsageUnitTypeID` | `sCODE_USAGE_UNIT_TYPE` | Global | No | No |  | Contract / Usage |
| Question | Accepted Response | `AcceptedResponseID` | `sTYPE_ISSUE_RESPONSE` | Global | No | No |  | Specialized Forms / Question |
| Question | Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Specialized Forms / Question |
| Question | Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Specialized Forms / Question |
| Question | Is PrivateQandA | `IsPrivateQandA` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Specialized Forms / Question |
| Question | Is Published | `IsPublished` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Specialized Forms / Question |
| Question | Is Shared | `IsShared` | `sTYPE_BOOLEAN` | Global | No | No |  | Specialized Forms / Question |
| Question | Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Specialized Forms / Question |
| Question | Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Specialized Forms / Question |
| Question | Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Specialized Forms / Question |
| Question | Question ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Specialized Forms / Question |
| Question | Question Issue | `IssueID` | `sTYPE_ISSUE` | Global | Yes | No |  | Specialized Forms / Question |
| Question | Question RecID | `QuestionID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Specialized Forms / Question |
| Question | Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Specialized Forms / Question |
| HolidayDate | Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Holiday Date |
| HolidayDate | Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Company Items / Holiday Date |
| HolidayDate | Day | `Day` | `sTYPE_UNFORMATTED_NUMBER` | Global | Yes | No |  | Company Items / Holiday Date |
| HolidayDate | Holiday Date ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / Holiday Date |
| HolidayDate | Holiday Date Name | `HolidayDateName` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / Holiday Date |
| HolidayDate | Holiday Date RecID | `HolidayDateID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Holiday Date |
| HolidayDate | Holiday Schedule | `HolidayScheduleID` | `sTYPE_HOLIDAY_SCHEDULE` | Global | Yes | No |  | Company Items / Holiday Date |
| HolidayDate | Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Holiday Date |
| HolidayDate | Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Company Items / Holiday Date |
| HolidayDate | Month | `Month` | `sTYPE_MONTH` | Global | Yes | No |  | Company Items / Holiday Date |
| HolidayDate | Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Holiday Date |
| HolidayDate | Year | `Year` | `sTYPE_DROPDOWN_YEAR` | Global | No | No |  | Company Items / Holiday Date |
| EscalationIndex | Effective Date | `EffectiveDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Escalation Index |
| EscalationIndex | Escalation Index ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Escalation Index |
| EscalationIndex | Escalation Index Name | `EscalationIndexName` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Escalation Index |
| EscalationIndex | Escalation Index RecID | `EscalationIndexID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Escalation Index |
| EscalationIndex | Index Amount | `IndexAmount` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Escalation Index |
| EscalationIndex | Index Group | `CodeIndexGroupID` | `sCODE_INDEX_GROUP` | Global | No | No |  | Contract / Escalation Index |
| EscalationIndex | Index Source | `CodeIndexSourceID` | `sCODE_INDEX_SOURCE` | Global | No | No |  | Contract / Escalation Index |
| EscalationIndex | Index Type | `CodeIndexTypeID` | `sCODE_INDEX_TYPE` | Global | No | No |  | Contract / Escalation Index |
| EscalationIndex | Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Escalation Index |
| EscalationIndex | Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Escalation Index |
| EscalationIndex | Period Month | `PeriodMonth` | `sTYPE_NUMBER` | Global | No | No |  | Contract / Escalation Index |
| EscalationIndex | Period Year | `PeriodYear` | `sTYPE_DROPDOWN_YEAR` | Global | No | No |  | Contract / Escalation Index |
| StateProvinceCountry | Country | `Country` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / State Province Country |
| StateProvinceCountry | ISO Alpha #2 Code | `ISOAlpha2Code` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / State Province Country |
| StateProvinceCountry | ISO Alpha #3 Code | `ISOAlpha3Code` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / State Province Country |
| StateProvinceCountry | Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / State Province Country |
| StateProvinceCountry | Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Company Items / State Province Country |
| StateProvinceCountry | State Province | `StateProvince` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / State Province Country |
| StateProvinceCountry | State Province Country | `StateProvinceCountryName` | `sTYPE_TEXT` | Global | No | No |  | Company Items / State Province Country |
| StateProvinceCountry | State Province Country ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / State Province Country |
| StateProvinceCountry | State Province Country RecID | `StateProvinceCountryID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / State Province Country |
| StateProvinceCountry | Tax Rate 1 | `TaxRate1` | `sTYPE_PERCENTAGE` | Global | No | No |  | Company Items / State Province Country |
| StateProvinceCountry | Tax Rate 2 | `TaxRate2` | `sTYPE_PERCENTAGE` | Global | No | No |  | Company Items / State Province Country |
| Party | Company | `CompanyID` | `sTYPE_EMPLOYER` | Global | No | No |  | Contract / Party |
| Party | Contact | `ContactID` | `sTYPE_PERSON` | Global | No | No |  | Contract / Party |
| Party | Contract | `ContractID` | `sTYPE_CONTRACT` | Global | Yes | No |  | Contract / Party |
| Party | Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Party |
| Party | Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Party |
| Party | Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Party |
| Party | Party ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Party |
| Party | Party Group | `CodePartyGroupID` | `sCODE_PARTY_GROUP` | Global | No | No |  | Contract / Party |
| Party | Party RecID | `PartyID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Party |
| Party | Party Type | `CodePartyTypeID` | `sCODE_PARTY_TYPE` | Global | No | No |  | Contract / Party |
| Party | Primary? | `PrimaryFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Party |
| MapClientSchedule | Auto Push Forecast End Date? | `AutoPushForecastEndDate` | `sTYPE_CHECKBOX` | Global | Yes | No |  | Schedule / Summary Information |
| MapClientSchedule | Holiday Schedule | `HolidayScheduleID` | `sTYPE_HOLIDAY_SCHEDULE` | Global | No | No |  | Schedule / Summary Information |
| MapClientSchedule | Is Completed? | `IsCompleted` | `sTYPE_CHECKBOX` | Global | No | No |  | Schedule / Summary Information |
| MapClientSchedule | Percent Complete | `ComputedPercentComplete` | `sTYPE_NUMBER` | Global | No | No |  | Schedule / Summary Information |
| MapClientSchedule | RETransaction | `RETransactionID` | `sTYPE_RE_TRANSACTION` | Global | No | No |  | Schedule / Summary Information |
| MapClientSchedule | Scenario | `ScenarioID` | `sTYPE_SCENARIO` | Global | No | No |  | Schedule / Summary Information |
| MapClientSchedule | Task Status | `CodeTaskStatusID` | `sCODE_TASK_STATUS` | Global | No | No |  | Schedule / Summary Information |
| MapClientSchedule | Work Holidays? | `WorkHolidays` | `sTYPE_CHECKBOX` | Global | Yes | No |  | Schedule / Summary Information |
| MapClientSchedule | Work Weekends? | `WorkWeekends` | `sTYPE_CHECKBOX` | Global | Yes | No |  | Schedule / Summary Information |
| MapClientSchedule | Map Client Schedule Recid | `MapClientScheduleID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Statics / Hidden |
| MapClientSchedule | Schedule Last Reviewed Date | `LastReviewedDate` | `sTYPE_TIME` | Global | Yes | No |  | Statics / Hidden |
| ProcessTimelineTemplate | Always Show in Summary? | `AlwaysShowInSummary` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Company Items / Milestone Timeline |
| ProcessTimelineTemplate | Completed Phase Status | `CompletedPhaseStatus` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / Milestone Timeline |
| ProcessTimelineTemplate | Default Task Name | `DefaultTaskName` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Milestone Timeline |
| ProcessTimelineTemplate | In Process Phase Status | `InProcessPhaseStatus` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / Milestone Timeline |
| ProcessTimelineTemplate | Milestone Template Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Milestone Timeline |
| ProcessTimelineTemplate | Milestone Template Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Company Items / Milestone Timeline |
| ProcessTimelineTemplate | Milestone Template Name | `ProcessTimelineTemplateName` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / Milestone Timeline |
| ProcessTimelineTemplate | Milestone Template RecID | `ProcessTimelineTemplateID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Milestone Timeline |
| ProcessTimelineTemplate | Previous Milestone Template | `PreviousProcessTimelineID` | `sTYPE_PROCESS_TIMELINE_TEMPLATE` | Global | No | No |  | Company Items / Milestone Timeline |
| ProcessTimelineTemplate | Project Phase | `CodeProjectPhaseID` | `sCODE_PROJECT_PHASE` | Global | Yes | No |  | Company Items / Milestone Timeline |
| Jurisdiction | Country | `Country` | `sTYPE_TEXT` | Global | No | No |  | Summary Information / Jurisdiction |
| Jurisdiction | Jurisdiction ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Summary Information / Jurisdiction |
| Jurisdiction | Jurisdiction Name | `JurisdictionName` | `sTYPE_TEXT` | Global | Yes | No |  | Summary Information / Jurisdiction |
| Jurisdiction | Jurisdiction RecID | `JurisdictionID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Summary Information / Jurisdiction |
| Jurisdiction | Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Summary Information / Jurisdiction |
| Jurisdiction | Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Summary Information / Jurisdiction |
| Jurisdiction | State | `StateProvinceCountryID` | `sTYPE_STATE_PROVINCE` | Global | Yes | No |  | Summary Information / Jurisdiction |
| Jurisdiction | State Province | `StateProvince` | `sTYPE_TEXT` | Global | No | No |  | Summary Information / Jurisdiction |
| Jurisdiction | Tax Rate #1 | `TaxRate1` | `sTYPE_PERCENTAGE` | Global | No | No |  | Summary Information / Jurisdiction |
| Jurisdiction | Tax Rate #2 | `TaxRate2` | `sTYPE_PERCENTAGE` | Global | No | No |  | Summary Information / Jurisdiction |
| CPI | CPI Index | `CodeCPIIndexID` | `sCODE_CPI_INDEX` | Global | No | No |  | Contract / CPI |
| CPI | CPI RecID | `CPIID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / CPI |
| CPI | CPI Value | `CPI` | `sTYPE_NUMBER_FRACTION5DIGITS` | Global | Yes | No |  | Contract / CPI |
| CPI | Contract | `ContractID` | `sTYPE_CONTRACT` | Global | No | No |  | Contract / CPI |
| CPI | Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / CPI |
| CPI | Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / CPI |
| CPI | Month | `Month` | `sTYPE_NUMBER` | Global | Yes | No |  | Contract / CPI |
| CPI | Published Date | `PublishedDate` | `sTYPE_DATE` | Global | No | No |  | Contract / CPI |
| CPI | Year | `Year` | `sTYPE_DROPDOWN_YEAR` | Global | Yes | No |  | Contract / CPI |
| Ownership | Entity | `ProjectEntityID` | `sTYPE_PROJECT_ENTITY` | Global | Yes | No |  | Purchase Management / Ownership |
| Ownership | Funding Amount | `FundingAmount` | `sTYPE_MONEY` | Global | Yes | No |  | Purchase Management / Ownership |
| Ownership | Funding Percent | `FundingPercent` | `sTYPE_PERCENTAGE` | Global | Yes | No |  | Purchase Management / Ownership |
| Ownership | Funding Type | `CodeFundingTypeID` | `sCODE_FUNDING_TYPE` | Global | Yes | No |  | Purchase Management / Ownership |
| Ownership | Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Purchase Management / Ownership |
| Ownership | Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Purchase Management / Ownership |
| Ownership | Owner | `OwnerID` | `sTYPE_PERSON` | Global | Yes | No |  | Purchase Management / Ownership |
| Ownership | Ownership ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Purchase Management / Ownership |
| Ownership | Ownership RecID | `OwnershipID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Purchase Management / Ownership |
| ExchangeRate | Contract | `ContractID` | `sTYPE_CONTRACT` | Global | No | No |  | Company Items / Exchange Rates |
| ExchangeRate | Effective Date | `EffectiveDate` | `sTYPE_DATE` | Global | Yes | No |  | Company Items / Exchange Rates |
| ExchangeRate | Exchange Rate | `ConversionRate` | `sTYPE_NUMBER_FRACTION6DIGITS` | Global | Yes | No |  | Company Items / Exchange Rates |
| ExchangeRate | Exchange Rate ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / Exchange Rates |
| ExchangeRate | Exchange Rate RecID | `ExchangeRateID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Exchange Rates |
| ExchangeRate | Exchange Rate Type | `CodeExchangeRateTypeID` | `sCODE_EXCHANGE_RATE_TYPE` | Global | Yes | No |  | Company Items / Exchange Rates |
| ExchangeRate | From Currency | `CodeFromCurrencyTypeID` | `sCODE_CURRENCY_TYPE` | Global | Yes | No |  | Company Items / Exchange Rates |
| ExchangeRate | To Currency | `CodeToCurrencyTypeID` | `sCODE_CURRENCY_TYPE` | Global | Yes | No |  | Company Items / Exchange Rates |
| HolidaySchedule | Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Holiday Schedule |
| HolidaySchedule | Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Company Items / Holiday Schedule |
| HolidaySchedule | Holiday Schedule ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / Holiday Schedule |
| HolidaySchedule | Holiday Schedule Name | `HolidayScheduleName` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / Holiday Schedule |
| HolidaySchedule | Holiday Schedule RecID | `HolidayScheduleID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Holiday Schedule |
| HolidaySchedule | Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Holiday Schedule |
| HolidaySchedule | Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Company Items / Holiday Schedule |
| HolidaySchedule | Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Holiday Schedule |
| ComparisonItem | Assumptions | `Assumptions` | `sTYPE_COMP_ASSUMPTIONS` | Global | No | No |  | Summary Information / Comparison Report |
| ComparisonItem | Comparison Item ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Summary Information / Comparison Report |
| ComparisonItem | Comparison Item RecID | `ComparisonItemID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Summary Information / Comparison Report |
| ComparisonItem | Computed Value | `ComputedValue` | `sTYPE_JAVASCRIPT` | Global | No | No |  | Summary Information / Comparison Report |
| ComparisonItem | Expense Group Total | `ExpenseGroup` | `sTYPE_COMP_EXPENSE_GROUP` | Global | No | No |  | Summary Information / Comparison Report |
| ComparisonItem | Scenario Date | `ScenarioDate` | `sTYPE_DATE` | Global | No | No |  | Summary Information / Comparison Report |
| ComparisonItem | Scenario Name | `ScenarioName` | `sTYPE_TEXT` | Global | No | No |  | Summary Information / Comparison Report |
| ComparisonItem | Scenario XmlData | `XmlData` | `sTYPE_TEXTAREA` | Global | Yes | No |  | Summary Information / Comparison Report |
| PartPackageItem | Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / PartPackageItem |
| PartPackageItem | Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Company Items / PartPackageItem |
| PartPackageItem | Part | `PartID` | `sTYPE_PART` | Global | Yes | No |  | Company Items / PartPackageItem |
| PartPackageItem | Part Package | `PartPackageID` | `sTYPE_PART_PACKAGE` | Global | Yes | No |  | Company Items / PartPackageItem |
| PartPackageItem | Part Package Item ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / PartPackageItem |
| PartPackageItem | Part Package Item RecID | `PartPackageItemID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / PartPackageItem |
| PartPackageItem | Quantity | `Quantity` | `sTYPE_NUMBER` | Global | Yes | No |  | Company Items / PartPackageItem |
| RecalcOverrideNotes | Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / ReCalc Override Notes |
| RecalcOverrideNotes | Date of entry | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / ReCalc Override Notes |
| RecalcOverrideNotes | Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / ReCalc Override Notes |
| RecalcOverrideNotes | Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / ReCalc Override Notes |
| RecalcOverrideNotes | Override Note | `Notes` | `sTYPE_TEXTAREA` | Global | Yes | No |  | Contract / ReCalc Override Notes |
| RecalcOverrideNotes | Straight Line Summary | `SLSummaryID` | `sTYPE_SL_SUMMARY` | Global | Yes | No |  | Contract / ReCalc Override Notes |
| DevelopmentPlan | Development Plan ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | RE Planner / RE Planner info |
| DevelopmentPlan | Development Plan Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | RE Planner / RE Planner info |
| DevelopmentPlan | Development Plan Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | RE Planner / RE Planner info |
| DevelopmentPlan | Development Plan Name | `DevelopmentPlanName` | `sTYPE_TEXT` | Global | Yes | No |  | RE Planner / RE Planner info |
| DevelopmentPlan | Development Plan Portfolio | `ProgramID` | `sTYPE_PORTFOLIO` | Global | Yes | No |  | RE Planner / RE Planner info |
| DevelopmentPlan | Development Plan RecID | `DevelopmentPlanID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | RE Planner / RE Planner info |
| Project | Opening Project or Capital Project | `ProjectType` | `sTYPE_TEXT` | Global | Yes | No |  | Summary Information / General Summary Information |
| Project | Project ID | `ClientEntityID` | `sTYPE_TEXT` | Global | No | No |  | Summary Information / General Summary Information |
| Project | Project RecID | `ProjectID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Summary Information / General Summary Information |
| Project | Project UUID | `UUID` | `sTYPE_TEXT` | Global | No | No |  | Summary Information / General Summary Information |
| Project | Related Project Facility | `FacilityID` | `sTYPE_FACILITY` | Global | No | No |  | Summary Information / General Summary Information |
| Project | Site Sequence Number | `SiteSequenceNumber` | `sTYPE_NUMBER` | Global | No | No |  | Summary Information / General Summary Information |
| PartPackage | Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / PartPackages |
| PartPackage | Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Company Items / PartPackages |
| PartPackage | Part Package ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / PartPackages |
| PartPackage | Part Package Name | `PartPackageName` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / PartPackages |
| PartPackage | Part Package RecID | `PartPackageID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / PartPackages |
| PartPackage | Vendor | `VendorID` | `sTYPE_EMPLOYER` | Global | No | No |  | Company Items / PartPackages |
| ReportGroupData | Parent Group Name | `ParentReportGroupDataID` | `sTYPE_REPORT_GROUP_DATA` | Global | No | No |  | Company Items / Data Field Groups |
| ReportGroupData | RGD Created Date | `CreatedDate` | `sTYPE_DATE` | Global | No | No |  | Company Items / Data Field Groups |
| ReportGroupData | RGD Modified Date | `ModifiedDate` | `sTYPE_DATE` | Global | No | No |  | Company Items / Data Field Groups |
| ReportGroupData | Report Group Name | `ReportGroupDataName` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / Data Field Groups |
| ReportGroupData | RGD FirmID | `FirmID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Statics / Hidden |
| ExpenseRecoveryItemMapping | Contract | `ContractID` | `sTYPE_CONTRACT` | Global | Yes | No |  | Contract / Expense Recovery Item Mapping |
| ExpenseRecoveryItemMapping | Document | `DocumentID` | `sTYPE_DOCUMENT` | Global | Yes | No |  | Contract / Expense Recovery Item Mapping |
| ExpenseRecoveryItemMapping | Expense Recovery Item | `ExpenseRecoveryItemID` | `sTYPE_EXPENSE_RECOVERY_ITEM` | Global | Yes | No |  | Contract / Expense Recovery Item Mapping |
| ExpenseRecoveryItemMapping | Invoice Line Item Name | `InvoiceLineItemName` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Recovery Item Mapping |
| ExpenseRecoveryItemMapping | JSON Config | `JSONConfigText` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Expense Recovery Item Mapping |
| Issue | Submit Bid | `BidderBudget` | `sTYPE_BIDDER_BUDGET` | Global | No | No |  | Specialized Forms / Bidder |
| Issue | ImportedCreatedDate | `ImportedCreatedDate` | `sTYPE_TIME` | Global | No | No |  | Statics / Hidden |
| Issue | Issue Date Range | `IssueDateRange` | `sTYPE_ISSUE_DATE_RANGE` | Global | No | No |  | Statics / Issue |
| Issue | Issue Date Type | `IssueDateType` | `sTYPE_ISSUE_DATE_FILTER` | Global | No | No |  | Statics / Issue |
| InformationOverlay | Expiration Date | `ExpirationDate` | `sTYPE_DATE` | Global | No | No |  | Statics / Hidden |
| InformationOverlay | Field Name List | `FieldNameList` | `sTYPE_TEXT` | Global | No | No |  | Statics / Hidden |
| InformationOverlay | JSON Config | `JSONConfigText` | `sTYPE_TEXT` | Global | No | No |  | Statics / Hidden |
| InformationOverlay | Tour Name | `TourName` | `sTYPE_TEXT` | Global | Yes | No |  | Statics / Hidden |
| GlobalProperty | FirmID | `FirmID` | `sTYPE_FIRM` | Global | No | No |  | Statics / Properties |
| GlobalProperty | Property Key | `PropertyKey` | `sTYPE_TEXT` | Global | Yes | No |  | Statics / Properties |
| GlobalProperty | Property Section | `GlobalPropertySectionID` | `sTYPE_GLOBAL_PROPERTY_SECTION` | Global | No | No |  | Statics / Properties |
| GlobalProperty | Property Value | `PropertyValue` | `sTYPE_TEXT` | Global | No | No |  | Statics / Properties |
| MapClientBudget | Last Reviewed Date | `LastReviewedDate` | `sTYPE_TIME` | Global | Yes | No |  | Statics / Hidden |
| MapClientBudget | Map Client Budget RecID | `MapClientBudgetID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Statics / Hidden |
| MapClientBudget | Project Entity | `ProjectEntityID` | `sTYPE_PROJECT_ENTITY` | Global | Yes | No |  | Statics / Hidden |
| ComparisonReport | Comparison Report ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Summary Information / Comparison Report |
| ComparisonReport | Comparison Report Layout | `PageLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | Yes | No |  | Summary Information / Comparison Report |
| ComparisonReport | Comparison Report RecID | `ComparisonReportID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Summary Information / Comparison Report |
| Site | Site ID | `ClientEntityID` | `sTYPE_TEXT` | Global | No | No |  | Summary Information / General Summary Information |
| Site | Site RecID | `PotentialProjectID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Summary Information / General Summary Information |
| Site | Site UUID | `UUID` | `sTYPE_TEXT` | Global | No | No |  | Summary Information / General Summary Information |
| CommitteePackage | Committee Package RecID | `CommitteePackageID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Statics / Hidden |
| EntityTemplate | Entity Template RecID | `EntityTemplateID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Statics / Hidden |
