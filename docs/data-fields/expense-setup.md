# ExpenseSetup — Data Fields

The recurring-expense billing configuration for a contract (insurance, taxes, CAM billed directly rather than through recovery) — coverage period begin markers for every possible billing frequency (Annual, Q1-Q4, both Semi-Annual halves) so the same setup record can support annual, quarterly, or semi-annual billing without changing schema. 105 fields split 103 Global / 2 Firm, and it appears under both the Contract group and the Wizard group — meaning this configuration also drives a guided lease-setup wizard flow, not just the standing contract record.

**Table Association:** `ExpenseSetup` &nbsp;·&nbsp; **Total fields:** 105 (Global: 103, Firm: 2)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Coverage Begin Annual | `CoverageBeginAnnual` | `sTYPE_MONTH_AND_DAY` | Global | No | No |  | Contract / Custom Coverage Payments |
| Coverage Begin Q1 | `CoverageBeginQ1` | `sTYPE_MONTH_AND_DAY` | Global | No | No |  | Contract / Custom Coverage Payments |
| Coverage Begin Q2 | `CoverageBeginQ2` | `sTYPE_MONTH_AND_DAY` | Global | No | No |  | Contract / Custom Coverage Payments |
| Coverage Begin Q3 | `CoverageBeginQ3` | `sTYPE_MONTH_AND_DAY` | Global | No | No |  | Contract / Custom Coverage Payments |
| Coverage Begin Q4 | `CoverageBeginQ4` | `sTYPE_MONTH_AND_DAY` | Global | No | No |  | Contract / Custom Coverage Payments |
| Coverage Begin Semi Annual 1 | `CoverageBeginSemiAnnual1` | `sTYPE_MONTH_AND_DAY` | Global | No | No |  | Contract / Custom Coverage Payments |
| Coverage Begin Semi Annual 2 | `CoverageBeginSemiAnnual2` | `sTYPE_MONTH_AND_DAY` | Global | No | No |  | Contract / Custom Coverage Payments |
| First Payment Due Date | `FirstPaymentDueDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Custom Coverage Payments |
| Last Payment Due Date | `LastPaymentDueDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Custom Coverage Payments |
| Payment Due Annual | `PaymentDueAnnual` | `sTYPE_MONTH_AND_DAY` | Global | No | No |  | Contract / Custom Coverage Payments |
| Payment Due Q1 | `PaymentDueQ1` | `sTYPE_MONTH_AND_DAY` | Global | No | No |  | Contract / Custom Coverage Payments |
| Payment Due Q2 | `PaymentDueQ2` | `sTYPE_MONTH_AND_DAY` | Global | No | No |  | Contract / Custom Coverage Payments |
| Payment Due Q3 | `PaymentDueQ3` | `sTYPE_MONTH_AND_DAY` | Global | No | No |  | Contract / Custom Coverage Payments |
| Payment Due Q4 | `PaymentDueQ4` | `sTYPE_MONTH_AND_DAY` | Global | No | No |  | Contract / Custom Coverage Payments |
| Payment Due Semi Annual 1 | `PaymentDueSemiAnnual1` | `sTYPE_MONTH_AND_DAY` | Global | No | No |  | Contract / Custom Coverage Payments |
| Payment Due Semi Annual 2 | `PaymentDueSemiAnnual2` | `sTYPE_MONTH_AND_DAY` | Global | No | No |  | Contract / Custom Coverage Payments |
| Amendment | `AmendmentID` | `sTYPE_CONTRACT_AMENDMENT` | Global | No | No |  | Contract / Expense Setup |
| Amount Decrease Cap | `AmountDecreaseCap` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Setup |
| Amount Increase Cap | `AmountIncreaseCap` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Setup |
| Apply Tax #1? | `ApplyTax1Flag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Expense Setup |
| Apply Tax #2? | `ApplyTax2Flag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Expense Setup |
| Apply Tax #3? | `ApplyTax3Flag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Expense Setup |
| Apply Tax #4? | `ApplyTax4Flag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Expense Setup |
| Bank Account Number | `BankAccountNumber` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Setup |
| Bank Routing Number | `BankRoutingNumber` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Setup |
| Begin Date | `BeginDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Expense Setup |
| Building Area Unit | `CodeBuildingAreaUnitID` | `sCODE_BUILDING_AREA_UNIT` | Global | No | No |  | Contract / Expense Setup |
| CPI Increase | `Firm_CPIIncrease` | `sTYPE_CHECKBOX` | Firm | No | No |  | Contract / Expense Setup |
| CPI Index | `CodeCPIIndexID` | `sCODE_CPI_INDEX` | Global | No | No |  | Contract / Expense Setup |
| CPI Multiplier | `CPIMultiplier` | `sTYPE_NUMBER` | Global | No | No |  | Contract / Expense Setup |
| CPI Notes | `CPINotes` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Expense Setup |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | Yes | No |  | Contract / Expense Setup |
| Covenant | `CovenantID` | `sTYPE_COVENANT` | Global | No | No |  | Contract / Expense Setup |
| Currency Type | `CodeCurrencyTypeID` | `sCODE_CURRENCY_TYPE` | Global | No | No |  | Contract / Expense Setup |
| Current Annual Rent | `CurrentAnnualRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Setup |
| Current Monthly Rent | `CurrentMonthlyRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Setup |
| Current Monthly Tax Amount #1 | `CurrentTaxAmount1` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Setup |
| Current Monthly Tax Amount #2 | `CurrentTaxAmount2` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Setup |
| Current Monthly Tax Amount #3 | `CurrentTaxAmount3` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Setup |
| Current Monthly Tax Amount #4 | `CurrentTaxAmount4` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Setup |
| Current Period Rent | `CurrentPeriodRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Setup |
| Current Period Tax Amount #1 | `CurrentPeriodTaxAmount1` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Setup |
| Current Period Tax Amount #2 | `CurrentPeriodTaxAmount2` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Setup |
| Current Period Tax Amount #3 | `CurrentPeriodTaxAmount3` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Setup |
| Current Period Tax Amount #4 | `CurrentPeriodTaxAmount4` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Setup |
| Custom Payment Coverage | `IsCustomPaymentCoverage` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Expense Setup |
| Daily Rent | `IsDailyRent` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Expense Setup |
| Date Range | `DateRange` | `sTYPE_DATE_RANGE` | Global | No | No |  | Contract / Expense Setup |
| Description | `Description` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Setup |
| End Date | `EndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Expense Setup |
| Expense Acct | `CodeExpenseAcctID` | `sCODE_EXPENSE_ACCT` | Global | No | No |  | Contract / Expense Setup |
| Expense Category | `CodeExpenseCategoryID` | `sCODE_EXPENSE_CATEGORY` | Global | No | No |  | Contract / Expense Setup |
| Expense Group | `CodeExpenseGroupID` | `sCODE_EXPENSE_GROUP` | Global | No | No |  | Contract / Expense Setup |
| Expense Setup ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Expense Setup |
| Expense Setup RecID | `ExpenseSetupID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Expense Setup |
| Expense Type | `CodeExpenseTypeID` | `sCODE_EXPENSE_TYPE` | Global | No | No |  | Contract / Expense Setup |
| Forecast Adjustment | `ForecastAdjustment` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Setup |
| Forecast Cap Percent | `ForecastCapPercent` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Expense Setup |
| Forecast Growth Percent | `ForecastGrowthPercent` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Expense Setup |
| Frequency | `CodeFrequencyID` | `sCODE_MONTH_FREQUENCY` | Global | Yes | No |  | Contract / Expense Setup |
| Hold? | `HoldFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Expense Setup |
| Include in Planning and Forecasting | `IncludeInPlanForecast` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Expense Setup |
| Internal Reference Number | `InternalReferenceNumber` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Setup |
| Is CPI Compounding? | `IsCPICompounding` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Expense Setup |
| Is Receivable? | `IsReceivable` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Expense Setup |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Expense Setup |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Expense Setup |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Expense Setup |
| Number Of Payments | `NumberOfPayments` | `sTYPE_NUMBER` | Global | No | No |  | Contract / Expense Setup |
| Pay in Arrears? | `IsPayArrears` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Expense Setup |
| Payment Due Day | `PaymentDueDay` | `sTYPE_NUMBER` | Global | No | No |  | Contract / Expense Setup |
| Payment Method | `CodePaymentMethodID` | `sCODE_PAYMENT_METHOD` | Global | No | No |  | Contract / Expense Setup |
| Payment Rate | `PaymentRate` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Expense Setup |
| Percent Decrease Cap | `PercentDecreaseCap` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Expense Setup |
| Percent Increase Cap | `PercentIncreaseCap` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Expense Setup |
| Plan Adjustment | `PlanAdjustment` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Setup |
| Plan Cap Percent | `PlanCapPercent` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Expense Setup |
| Plan Growth Percent | `PlanGrowthPercent` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Expense Setup |
| Plan/Forecast Based On | `CodePlanForecastBasedOnID` | `sCODE_PLAN_FORECAST_BASED_ON` | Global | No | No |  | Contract / Expense Setup |
| Plan/Forecast Group | `CodePlanForecastGroupID` | `sCODE_PLAN_FORECAST_GROUP` | Global | No | No |  | Contract / Expense Setup |
| Planning and Forecasting Notes | `PlanForecastNotes` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Expense Setup |
| Pro Rata Share Rate | `ProRataShareRate` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Expense Setup |
| Proration Method | `CodeProrationMethodID` | `sCODE_PRORATION_METHOD` | Global | No | No |  | Contract / Expense Setup |
| Ready For Payment? | `ReadyForPaymentFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Expense Setup |
| Reconcilable Expense? | `ReconcilableExpense` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Expense Setup |
| Remit Message | `RemitMessage` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Setup |
| Rentable Area | `RentableArea` | `sTYPE_AREA` | Global | No | No |  | Contract / Expense Setup |
| Secondary Rent Schedule Allocation Amount | `SecondaryRentSchedAllocAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Setup |
| Secondary Rent Schedule Allocation Percent | `SecondaryRentSchedAllocPercent` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Expense Setup |
| Section | `Section` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Setup |
| Taxes Included In Amount? | `TaxesIncludedFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Expense Setup |
| Total Current Monthly Rent | `Firm_TotalCurrentMonthlyRent` | `sTYPE_MONEY_MATH_OPERATION` | Firm | No | No |  | Contract / Expense Setup |
| Vendor | `VendorID` | `sTYPE_VENDOR` | Global | No | No |  | Contract / Expense Setup |
| Vendor Account Number | `VendorAccountNumber` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Setup |
| Vendor Allocation List | `VendorAllocationList` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Setup |
| Amount Type | `ExpenseSetupWizard_AmountType` | `sTYPE_TEXT` | Global | No | No |  | Wizard / Expense Setup Wizard |
| Effective Date | `ExpenseSetupWizard_EffectiveDates` | `sTYPE_TEXT` | Global | Yes | No |  | Wizard / Expense Setup Wizard |
| End Date | `ExpenseSetupWizard_EndDate` | `sTYPE_DATE` | Global | No | No |  | Wizard / Expense Setup Wizard |
| Escalate Every (years) | `ExpenseSetupWizard_EscalateEvery` | `sTYPE_NUMBER` | Global | No | No |  | Wizard / Expense Setup Wizard |
| Escalate by Amount/Rate | `ExpenseSetupWizard_EscalateAmountRate` | `sTYPE_MONEY` | Global | No | No |  | Wizard / Expense Setup Wizard |
| Find Starting Amount | `ExpenseSetupWizard_FindStartingAmout` | `sTYPE_CHECKBOX` | Global | No | No |  | Wizard / Expense Setup Wizard |
| Generate Expense Setup | `GenerateExpenseSetup` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Wizard / Expense Setup Wizard |
| Start Date | `ExpenseSetupWizard_StartDate` | `sTYPE_DATE` | Global | No | No |  | Wizard / Expense Setup Wizard |
| Starting Amount | `ExpenseSetupWizard_StartingAmout` | `sTYPE_MONEY` | Global | No | No |  | Wizard / Expense Setup Wizard |
| Type Of Escalation | `ExpenseSetupWizard_TypeOfEscalation` | `sTYPE_EXPENSE_ESCALTION_TYPE` | Global | No | No |  | Wizard / Expense Setup Wizard |
