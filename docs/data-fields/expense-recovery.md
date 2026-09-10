# ExpenseRecovery — Data Fields

The CAM/OpEx recovery engine for a lease — one record per recoverable expense category (CAM, taxes, insurance, HVAC, etc.) per contract per year, carrying the base year, cap formula (percent or dollar, per-period or cumulative), pro rata share method, gross-up rules, and admin fee. It is by far the largest entity in the catalog (567 fields, 92% Global) because commercial CAM reconciliation is one of the most negotiated and variably-structured terms in a lease — every landlord uses a different combination of caps, exclusions, base-year stops, and gross-up methodologies, and Lucernex models each variant as its own field rather than a generic formula, which is why nearly half the fields are `MONEY_MATH_OPERATION`/`PERCENT_MATH_OPERATION` computed values.

**Table Association:** `ExpenseRecovery` &nbsp;·&nbsp; **Total fields:** 567 (Global: 558, Firm: 9)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Amendment | `AmendmentID` | `sTYPE_CONTRACT_AMENDMENT` | Global | No | No |  | Contract / Expense Recovery |
| Approval Status | `CodeApprovalStatusID` | `sCODE_APPROVAL_STATUS_EXPRECOVERY` | Global | No | No |  | Contract / Expense Recovery |
| Base Year | `BaseYear` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Recovery |
| Base Year Amount | `BaseYearAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Recovery |
| Base Year Amount Type | `CodeBaseYearAmountTypeID` | `sCODE_BASE_YEAR_AMOUNT_TYPE` | Global | No | No |  | Contract / Expense Recovery |
| Begin Date | `BeginDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Expense Recovery |
| Calculation Method | `CodeCalculationMethodID` | `sCODE_CALCULATION_METHOD` | Global | No | No |  | Contract / Expense Recovery |
| Cap Amount Per-Period Change (Percent) | `CapAmountChangePercent` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Expense Recovery |
| Cap Amount Per-Period Change (Value) | `CapAmountChangeValue` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Recovery |
| Cap Percentage | `CapPercentage` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Expense Recovery |
| Cap Type | `CodeCapTypeID` | `sCODE_CAP_TYPE` | Global | No | No |  | Contract / Expense Recovery |
| Catch Up Number of Months | `CatchUpNumberOfMonths` | `sTYPE_NUMBER_FRACTION2DIGITS` | Global | No | No |  | Contract / Expense Recovery |
| Catch Up Payment Amount | `CatchUpPaymentAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Recovery |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | Yes | No |  | Contract / Expense Recovery |
| Covenant | `CovenantID` | `sTYPE_COVENANT` | Global | No | No |  | Contract / Expense Recovery |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Expense Recovery |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Expense Recovery |
| Currency Type | `CodeCurrencyTypeID` | `sCODE_CURRENCY_TYPE` | Global | No | No |  | Contract / Expense Recovery |
| Current Escrow Payment | `CurrentEscrowPayment` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Recovery |
| Date Received | `DateReceived` | `sTYPE_DATE` | Global | No | No |  | Contract / Expense Recovery |
| Documents | `DocumentIDList` | `sTYPE_DOCUMENT_LIST` | Global | No | No |  | Contract / Expense Recovery |
| End Date | `EndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Expense Recovery |
| Escalation Amount Increase | `EscalationAmountIncrease` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Expense Recovery |
| Escalation Payment Method | `CodeEscalationPaymentMethodID` | `sCODE_ESCALATION_PAYMENT_METHOD` | Global | No | No |  | Contract / Expense Recovery |
| Escalation Percentage | `EscalationPercentage` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Expense Recovery |
| Exp Rec Based On | `CodeExpRecBasedOnID` | `sCODE_EXP_REC_BASED_ON` | Global | No | No |  | Contract / Expense Recovery |
| Expense Group | `CodeExpenseGroupID` | `sCODE_EXPENSE_GROUP` | Global | No | No |  | Contract / Expense Recovery |
| Expense Recovery ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Expense Recovery |
| Expense Recovery Due Date Processed | `Firm_ExpenseRecoveryDueDateProcessed` | `sTYPE_DATE` | Firm | No | No |  | Contract / Expense Recovery |
| Expense Recovery Pro Rata Share | `Firm_ProRataShare` | `sTYPE_MONEY` | Firm | No | No |  | Contract / Expense Recovery |
| Expense Recovery Pro Rata Share Amount Paid | `Firm_ProRataShareAmountPaid` | `sTYPE_MONEY` | Firm | No | No |  | Contract / Expense Recovery |
| Expense Recovery Pro Rata Share Subtotal | `Firm_ExpenseRecoveryProRataShareSubtotal` | `sTYPE_MONEY_MATH_OPERATION` | Firm | No | No |  | Contract / Expense Recovery |
| Expense Recovery Pro Rata Share Total Due | `Firm_ExpenseRecoveryProRataShareTotalDue` | `sTYPE_MONEY_MATH_OPERATION` | Firm | No | No |  | Contract / Expense Recovery |
| Expense Recovery RecID | `ExpenseRecoveryID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Expense Recovery |
| Expense Recovery Reviewer | `Firm_ExpenseRecoveryReviewer` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Expense Recovery |
| Expense Recovery Sales Tax | `Firm_ExpenseRecoverySalesTax` | `sTYPE_MONEY` | Firm | No | No |  | Contract / Expense Recovery |
| Expense Recovery Savings | `Firm_ExpenseRecoverySavings` | `sTYPE_MONEY` | Firm | No | No |  | Contract / Expense Recovery |
| Expense Recovery Status | `Firm_ExpenseRecoveryStatus` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Expense Recovery |
| Expense Type | `CodeExpenseTypeID` | `sCODE_EXPENSE_TYPE` | Global | No | No |  | Contract / Expense Recovery |
| Grossup Rate | `GrossupRate` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Recovery |
| Is Escalation Non-Cumulative | `IsRecoveryCapEscalationNonCum` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Expense Recovery |
| Maximum Value | `MaximumValue` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Recovery |
| Minimum Value | `MinimumValue` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Recovery |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Expense Recovery |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Expense Recovery |
| New Escalation Payment | `NewEscalationPayment` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Recovery |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Expense Recovery |
| Number of Days In Period | `NumDaysInRecoveryPeriod` | `sTYPE_DATE_MATH_OPERATION` | Global | No | No |  | Contract / Expense Recovery |
| Occupancy Factor | `OccupancyAdjustedThreshold` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Expense Recovery |
| Payment Frequency | `CodePaymentFrequencyID` | `sCODE_MONTH_FREQUENCY` | Global | No | No |  | Contract / Expense Recovery |
| Pro Rata Share Method | `CodeProRataShareMethodID` | `sCODE_PRO_RATA_SHARE_METHOD` | Global | No | No |  | Contract / Expense Recovery |
| Proposed Catch Up Payment Amount | `ProposedCatchUpPaymentAmount` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Expense Recovery |
| Proposed Escalation Payment | `ProposedEscalationPayment` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Expense Recovery |
| Reconciled Date | `ReconciledDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Expense Recovery |
| Reconciled? | `ReconciledFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Expense Recovery |
| Reconciliation Frequency | `CodeReconciliationFrequencyID` | `sCODE_MONTH_FREQUENCY` | Global | No | No |  | Contract / Expense Recovery |
| Recovery Exclusions | `RecoveryExclusions` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Expense Recovery |
| Recovery Group | `CodeRecoveryGroupID` | `sCODE_RECOVERY_GROUP` | Global | No | No |  | Contract / Expense Recovery |
| Recovery Period | `RecoveryPeriod` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Recovery |
| Recovery Period Days | `RecoveryPeriodDaysNoZeroDef` | `sTYPE_NUMBER` | Global | No | No |  | Contract / Expense Recovery |
| Recovery Type | `CodeRecoveryTypeID` | `sCODE_RECOVERY_TYPE` | Global | No | No |  | Contract / Expense Recovery |
| Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Expense Recovery |
| Section | `Section` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Recovery |
| Tenant Due Date | `TenantDueDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Expense Recovery |
| Tenant Savings Amount | `TenantSavingsAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Recovery |
| Approved Additions | `ApprovedAdditionsGross` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Approved (Gross) |
| Approved Admin Fee Percentage Amount | `ApprovedAdminFeePercentageAmountGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved (Gross) |
| Approved Administration Fees | `ApprovedAdministrationFeesGross` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Approved (Gross) |
| Approved Controllable Expenses | `ApprovedControllableExpensesGross` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Approved (Gross) |
| Approved Deductions | `ApprovedDeductionsGross` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Approved (Gross) |
| Approved Net Amount Due (NPT-PP) | `ApprovedNetAmountDueGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved (Gross) |
| Approved Net Pass-Through (ST2*PRS*Occ) | `ApprovedNetPassThroughGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved (Gross) |
| Approved Net Pass-Through (ST2*PRS*Occ) Duplicate | `ApprovedNetPassThroughCOREFirmOnlyGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved (Gross) |
| Approved Non-Controllable Expenses | `ApprovedNonControllableExpensesGross` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Approved (Gross) |
| Approved Pass-Through (ST1+AF%+AF+A) | `ApprovedPassThroughGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved (Gross) |
| Approved Recoveries | `ApprovedRecoveriesGross` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Approved (Gross) |
| Approved Revised Amount Due (Net+Adj) | `ApprovedRevisedNetAmountDueGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved (Gross) |
| Approved Sub Total #1 (C+NC-D) | `ApprovedSubTotal1Gross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved (Gross) |
| Approved Sub Total #2 (PT-R) | `ApprovedSubTotal2Gross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved (Gross) |
| Approved Adjustment Amount | `ApprovedAdjustmentAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Approved (Gross/Net) |
| Approved Admin Fee Percentage | `ApprovedAdminFeePercentage` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Statement Audit - Approved (Gross/Net) |
| Approved Cap Amount | `ApprovedCapAmountNoZeroDef` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Approved (Gross/Net) |
| Approved GLA | `ApprovedGLA` | `sTYPE_AREA` | Global | No | No |  | Contract / Statement Audit - Approved (Gross/Net) |
| Approved Pre Paid Amount | `ApprovedPrePaidAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Approved (Gross/Net) |
| Approved Pro Rata Share Rate | `ApprovedProRataShareRate` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Statement Audit - Approved (Gross/Net) |
| Approved Rentable Area | `ApprovedRentableArea` | `sTYPE_AREA` | Global | No | No |  | Contract / Statement Audit - Approved (Gross/Net) |
| Approved Additions | `ApprovedAdditionsNet` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Approved (Net) |
| Approved Admin Fee Percentage Amount | `ApprovedAdminFeePercentageAmountNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved (Net) |
| Approved Administration Fees | `ApprovedAdministrationFeesNet` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Approved (Net) |
| Approved Controllable Expenses | `ApprovedControllableExpensesNet` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Approved (Net) |
| Approved Deductions | `ApprovedDeductionsNet` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Approved (Net) |
| Approved Net Amount Due (NPT-PP) | `ApprovedNetAmountDueNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved (Net) |
| Approved Net Pass-Through (ST2*PRS*Occ) | `ApprovedNetPassThroughNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved (Net) |
| Approved Net Pass-Through (ST2*PRS*Occ) Duplicate | `ApprovedNetPassThroughCOREFirmOnlyNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved (Net) |
| Approved Non-Controllable Expenses | `ApprovedNonControllableExpensesNet` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Approved (Net) |
| Approved Pass-Through (ST1+AF%+AF+A) | `ApprovedPassThroughNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved (Net) |
| Approved Recoveries | `ApprovedRecoveriesNet` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Approved (Net) |
| Approved Revised Amount Due (Net+Adj) | `ApprovedRevisedNetAmountDueNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved (Net) |
| Approved Sub Total #1 (C+NC-D) | `ApprovedSubTotal1Net` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved (Net) |
| Approved Sub Total #2 (PT-R) | `ApprovedSubTotal2Net` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved (Net) |
| A-B Variance - Additions | `ABVarianceAdditionsGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Budgeted Variance (Gross) |
| A-B Variance - Admin Fee Percentage | `ABVarianceAdminFeePercentageGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Budgeted Variance (Gross) |
| A-B Variance - Admin Fee Percentage Amount | `ABVarianceAdminFeePercentageAmountGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Budgeted Variance (Gross) |
| A-B Variance - Administration Fees | `ABVarianceAdministrationFeesGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Budgeted Variance (Gross) |
| A-B Variance - Cap Amount | `ABVarianceCapAmountGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Budgeted Variance (Gross) |
| A-B Variance - Controllable Expenses | `ABVarianceControllableExpensesGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Budgeted Variance (Gross) |
| A-B Variance - Deductions | `ABVarianceDeductionsGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Budgeted Variance (Gross) |
| A-B Variance - GLA | `ABVarianceGLAGross` | `sTYPE_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Budgeted Variance (Gross) |
| A-B Variance - Net Amount Due (NPT-PP) | `ABVarianceNetAmountDueGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Budgeted Variance (Gross) |
| A-B Variance - Net Pass-Through (ST2*PRR) | `ABVarianceNetPassThroughGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Budgeted Variance (Gross) |
| A-B Variance - Non-Controllable Expenses | `ABVarianceNonControllableExpensesGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Budgeted Variance (Gross) |
| A-B Variance - Pass-Through (ST1+AF%+AF+A) | `ABVariancePassThroughGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Budgeted Variance (Gross) |
| A-B Variance - Pre Paid Amount | `ABVariancePrePaidAmountGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Budgeted Variance (Gross) |
| A-B Variance - Pro Rata Share Rate | `ABVarianceProRataShareRateGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Budgeted Variance (Gross) |
| A-B Variance - Recoveries | `ABVarianceRecoveriesGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Budgeted Variance (Gross) |
| A-B Variance - Rentable Area | `ABVarianceRentableAreaGross` | `sTYPE_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Budgeted Variance (Gross) |
| A-B Variance - Sub Total #1 (C+NC-D) | `ABVarianceSubTotal1Gross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Budgeted Variance (Gross) |
| A-B Variance - Sub Total #2 (PT-R) | `ABVarianceSubTotal2Gross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Budgeted Variance (Gross) |
| A-B Variance - Additions | `ABVarianceAdditionsNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Budgeted Variance (Net) |
| A-B Variance - Admin Fee Percentage | `ABVarianceAdminFeePercentageNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Budgeted Variance (Net) |
| A-B Variance - Admin Fee Percentage Amount | `ABVarianceAdminFeePercentageAmountNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Budgeted Variance (Net) |
| A-B Variance - Administration Fees | `ABVarianceAdministrationFeesNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Budgeted Variance (Net) |
| A-B Variance - Cap Amount | `ABVarianceCapAmountNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Budgeted Variance (Net) |
| A-B Variance - Controllable Expenses | `ABVarianceControllableExpensesNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Budgeted Variance (Net) |
| A-B Variance - Deductions | `ABVarianceDeductionsNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Budgeted Variance (Net) |
| A-B Variance - GLA | `ABVarianceGLANet` | `sTYPE_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Budgeted Variance (Net) |
| A-B Variance - Net Amount Due (NPT-PP) | `ABVarianceNetAmountDueNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Budgeted Variance (Net) |
| A-B Variance - Net Pass-Through (ST2*PRR) | `ABVarianceNetPassThroughNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Budgeted Variance (Net) |
| A-B Variance - Non-Controllable Expenses | `ABVarianceNonControllableExpensesNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Budgeted Variance (Net) |
| A-B Variance - Pass-Through (ST1+AF%+AF+A) | `ABVariancePassThroughNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Budgeted Variance (Net) |
| A-B Variance - Pre Paid Amount | `ABVariancePrePaidAmountNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Budgeted Variance (Net) |
| A-B Variance - Pro Rata Share Rate | `ABVarianceProRataShareRateNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Budgeted Variance (Net) |
| A-B Variance - Recoveries | `ABVarianceRecoveriesNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Budgeted Variance (Net) |
| A-B Variance - Rentable Area | `ABVarianceRentableAreaNet` | `sTYPE_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Budgeted Variance (Net) |
| A-B Variance - Sub Total #1 (C+NC-D) | `ABVarianceSubTotal1Net` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Budgeted Variance (Net) |
| A-B Variance - Sub Total #2 (PT-R) | `ABVarianceSubTotal2Net` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Budgeted Variance (Net) |
| A-P Variance % - Additions | `APVariancePctAdditionsGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance % (Gross) |
| A-P Variance % - Admin Fee Percentage | `APVariancePctAdminFeePercentageGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance % (Gross) |
| A-P Variance % - Admin Fee Percentage Amount | `APVariancePctAdminFeePercentageAmountGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance % (Gross) |
| A-P Variance % - Administration Fees | `APVariancePctAdministrationFeesGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance % (Gross) |
| A-P Variance % - Cap Amount | `APVariancePctCapAmountGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance % (Gross) |
| A-P Variance % - Controllable Expenses | `APVariancePctControllableExpensesGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance % (Gross) |
| A-P Variance % - Deductions | `APVariancePctDeductionsGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance % (Gross) |
| A-P Variance % - GLA | `APVariancePctGLAGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance % (Gross) |
| A-P Variance % - Net Amount Due (NPT-PP) | `APVariancePctNetAmountDueGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance % (Gross) |
| A-P Variance % - Net Pass-Through (ST2*PRR) | `APVariancePctNetPassThroughGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance % (Gross) |
| A-P Variance % - Non-Controllable Expenses | `APVariancePctNonControllableExpensesGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance % (Gross) |
| A-P Variance % - Pass-Through (ST1+AF%+AF+A) | `APVariancePctPassThroughGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance % (Gross) |
| A-P Variance % - Pre Paid Amount | `APVariancePctPrePaidAmountGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance % (Gross) |
| A-P Variance % - Pro Rata Share Rate | `APVariancePctProRataShareRateGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance % (Gross) |
| A-P Variance % - Recoveries | `APVariancePctRecoveriesGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance % (Gross) |
| A-P Variance % - Rentable Area | `APVariancePctRentableAreaGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance % (Gross) |
| A-P Variance % - Sub Total #1 (C+NC-D) | `APVariancePctSubTotal1Gross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance % (Gross) |
| A-P Variance % - Sub Total #2 (PT-R) | `APVariancePctSubTotal2Gross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance % (Gross) |
| A-P Variance % - Additions | `APVariancePctAdditionsNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance % (Net) |
| A-P Variance % - Admin Fee Percentage | `APVariancePctAdminFeePercentageNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance % (Net) |
| A-P Variance % - Admin Fee Percentage Amount | `APVariancePctAdminFeePercentageAmountNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance % (Net) |
| A-P Variance % - Administration Fees | `APVariancePctAdministrationFeesNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance % (Net) |
| A-P Variance % - Cap Amount | `APVariancePctCapAmountNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance % (Net) |
| A-P Variance % - Controllable Expenses | `APVariancePctControllableExpensesNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance % (Net) |
| A-P Variance % - Deductions | `APVariancePctDeductionsNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance % (Net) |
| A-P Variance % - GLA | `APVariancePctGLANet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance % (Net) |
| A-P Variance % - Net Amount Due (NPT-PP) | `APVariancePctNetAmountDueNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance % (Net) |
| A-P Variance % - Net Pass-Through (ST2*PRR) | `APVariancePctNetPassThroughNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance % (Net) |
| A-P Variance % - Non-Controllable Expenses | `APVariancePctNonControllableExpensesNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance % (Net) |
| A-P Variance % - Pass-Through (ST1+AF%+AF+A) | `APVariancePctPassThroughNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance % (Net) |
| A-P Variance % - Pre Paid Amount | `APVariancePctPrePaidAmountNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance % (Net) |
| A-P Variance % - Pro Rata Share Rate | `APVariancePctProRataShareRateNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance % (Net) |
| A-P Variance % - Recoveries | `APVariancePctRecoveriesNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance % (Net) |
| A-P Variance % - Rentable Area | `APVariancePctRentableAreaNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance % (Net) |
| A-P Variance % - Sub Total #1 (C+NC-D) | `APVariancePctSubTotal1Net` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance % (Net) |
| A-P Variance % - Sub Total #2 (PT-R) | `APVariancePctSubTotal2Net` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance % (Net) |
| A-P Variance - Additions | `APVarianceAdditionsGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance (Gross) |
| A-P Variance - Admin Fee Percentage | `APVarianceAdminFeePercentageGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance (Gross) |
| A-P Variance - Admin Fee Percentage Amount | `APVarianceAdminFeePercentageAmountGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance (Gross) |
| A-P Variance - Administration Fees | `APVarianceAdministrationFeesGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance (Gross) |
| A-P Variance - Cap Amount | `APVarianceCapAmountGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance (Gross) |
| A-P Variance - Controllable Expenses | `APVarianceControllableExpensesGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance (Gross) |
| A-P Variance - Deductions | `APVarianceDeductionsGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance (Gross) |
| A-P Variance - GLA | `APVarianceGLAGross` | `sTYPE_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance (Gross) |
| A-P Variance - Net Amount Due (NPT-PP) | `APVarianceNetAmountDueGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance (Gross) |
| A-P Variance - Net Pass-Through (ST2*PRR) | `APVarianceNetPassThroughGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance (Gross) |
| A-P Variance - Non-Controllable Expenses | `APVarianceNonControllableExpensesGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance (Gross) |
| A-P Variance - Pass-Through (ST1+AF%+AF+A) | `APVariancePassThroughGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance (Gross) |
| A-P Variance - Pre Paid Amount | `APVariancePrePaidAmountGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance (Gross) |
| A-P Variance - Pro Rata Share Rate | `APVarianceProRataShareRateGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance (Gross) |
| A-P Variance - Recoveries | `APVarianceRecoveriesGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance (Gross) |
| A-P Variance - Rentable Area | `APVarianceRentableAreaGross` | `sTYPE_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance (Gross) |
| A-P Variance - Sub Total #1 (C+NC-D) | `APVarianceSubTotal1Gross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance (Gross) |
| A-P Variance - Sub Total #2 (PT-R) | `APVarianceSubTotal2Gross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance (Gross) |
| A-P Variance - Additions | `APVarianceAdditionsNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance (Net) |
| A-P Variance - Admin Fee Percentage | `APVarianceAdminFeePercentageNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance (Net) |
| A-P Variance - Admin Fee Percentage Amount | `APVarianceAdminFeePercentageAmountNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance (Net) |
| A-P Variance - Administration Fees | `APVarianceAdministrationFeesNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance (Net) |
| A-P Variance - Cap Amount | `APVarianceCapAmountNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance (Net) |
| A-P Variance - Controllable Expenses | `APVarianceControllableExpensesNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance (Net) |
| A-P Variance - Deductions | `APVarianceDeductionsNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance (Net) |
| A-P Variance - GLA | `APVarianceGLANet` | `sTYPE_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance (Net) |
| A-P Variance - Net Amount Due (NPT-PP) | `APVarianceNetAmountDueNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance (Net) |
| A-P Variance - Net Pass-Through (ST2*PRR) | `APVarianceNetPassThroughNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance (Net) |
| A-P Variance - Non-Controllable Expenses | `APVarianceNonControllableExpensesNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance (Net) |
| A-P Variance - Pass-Through (ST1+AF%+AF+A) | `APVariancePassThroughNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance (Net) |
| A-P Variance - Pre Paid Amount | `APVariancePrePaidAmountNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance (Net) |
| A-P Variance - Pro Rata Share Rate | `APVarianceProRataShareRateNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance (Net) |
| A-P Variance - Recoveries | `APVarianceRecoveriesNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance (Net) |
| A-P Variance - Rentable Area | `APVarianceRentableAreaNet` | `sTYPE_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance (Net) |
| A-P Variance - Sub Total #1 (C+NC-D) | `APVarianceSubTotal1Net` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance (Net) |
| A-P Variance - Sub Total #2 (PT-R) | `APVarianceSubTotal2Net` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Approved-Prior Variance (Net) |
| Budgeted Additions | `BudgetedAdditionsGross` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Budgeted (Gross) |
| Budgeted Admin Fee Percentage Amount | `BudgetedAdminFeePercentageAmountGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted (Gross) |
| Budgeted Administration Fees | `BudgetedAdministrationFeesGross` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Budgeted (Gross) |
| Budgeted Controllable Expenses | `BudgetedControllableExpensesGross` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Budgeted (Gross) |
| Budgeted Deductions | `BudgetedDeductionsGross` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Budgeted (Gross) |
| Budgeted Net Amount Due (NPT-PP) | `BudgetedNetAmountDueGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted (Gross) |
| Budgeted Net Pass-Through (ST2*PRR) | `BudgetedNetPassThroughGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted (Gross) |
| Budgeted Non-Controllable Expenses | `BudgetedNonControllableExpensesGross` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Budgeted (Gross) |
| Budgeted Pass-Through (ST1+AF%+AF+A) | `BudgetedPassThroughGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted (Gross) |
| Budgeted Recoveries | `BudgetedRecoveriesGross` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Budgeted (Gross) |
| Budgeted Sub Total #1 (C+NC-D) | `BudgetedSubTotal1Gross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted (Gross) |
| Budgeted Sub Total #2 (PT-R) | `BudgetedSubTotal2Gross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted (Gross) |
| Budgeted Admin Fee Percentage | `BudgetedAdminFeePercentage` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Statement Audit - Budgeted (Gross/Net) |
| Budgeted Cap Amount | `BudgetedCapAmountNoZeroDef` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Budgeted (Gross/Net) |
| Budgeted GLA | `BudgetedGLA` | `sTYPE_AREA` | Global | No | No |  | Contract / Statement Audit - Budgeted (Gross/Net) |
| Budgeted Pre Paid Amount | `BudgetedPrePaidAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Budgeted (Gross/Net) |
| Budgeted Pro Rata Share Rate | `BudgetedProRataShareRate` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Statement Audit - Budgeted (Gross/Net) |
| Budgeted Rentable Area | `BudgetedRentableArea` | `sTYPE_AREA` | Global | No | No |  | Contract / Statement Audit - Budgeted (Gross/Net) |
| Budgeted Additions | `BudgetedAdditionsNet` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Budgeted (Net) |
| Budgeted Admin Fee Percentage Amount | `BudgetedAdminFeePercentageAmountNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted (Net) |
| Budgeted Administration Fees | `BudgetedAdministrationFeesNet` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Budgeted (Net) |
| Budgeted Controllable Expenses | `BudgetedControllableExpensesNet` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Budgeted (Net) |
| Budgeted Deductions | `BudgetedDeductionsNet` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Budgeted (Net) |
| Budgeted Net Amount Due (NPT-PP) | `BudgetedNetAmountDueNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted (Net) |
| Budgeted Net Pass-Through (ST2*PRR) | `BudgetedNetPassThroughNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted (Net) |
| Budgeted Non-Controllable Expenses | `BudgetedNonControllableExpensesNet` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Budgeted (Net) |
| Budgeted Pass-Through (ST1+AF%+AF+A) | `BudgetedPassThroughNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted (Net) |
| Budgeted Recoveries | `BudgetedRecoveriesNet` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Budgeted (Net) |
| Budgeted Sub Total #1 (C+NC-D) | `BudgetedSubTotal1Net` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted (Net) |
| Budgeted Sub Total #2 (PT-R) | `BudgetedSubTotal2Net` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted (Net) |
| B-P Variance % - Additions | `BPVariancePctAdditionsGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance % (Gross) |
| B-P Variance % - Admin Fee Percentage Amount | `BPVariancePctAdminFeePercentageAmountGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance % (Gross) |
| B-P Variance % - Administration Fees | `BPVariancePctAdministrationFeesGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance % (Gross) |
| B-P Variance % - Cap Amount | `BPVariancePctCapAmountGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance % (Gross) |
| B-P Variance % - Controllable Expenses | `BPVariancePctControllableExpensesGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance % (Gross) |
| B-P Variance % - Deductions | `BPVariancePctDeductionsGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance % (Gross) |
| B-P Variance % - GLA | `BPVariancePctGLAGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance % (Gross) |
| B-P Variance % - Net Amount Due (NPT-PP) | `BPVariancePctNetAmountDueGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance % (Gross) |
| B-P Variance % - Net Pass-Through (ST2*PRR) | `BPVariancePctNetPassThroughGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance % (Gross) |
| B-P Variance % - Non-Controllable Expenses | `BPVariancePctNonControllableExpensesGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance % (Gross) |
| B-P Variance % - Pass-Through (ST1+AF%+AF+A) | `BPVariancePctPassThroughGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance % (Gross) |
| B-P Variance % - Pre Paid Amount | `BPVariancePctPrePaidAmountGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance % (Gross) |
| B-P Variance % - Pro Rata Share Rate | `BPVariancePctProRataShareRateGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance % (Gross) |
| B-P Variance % - Recoveries | `BPVariancePctRecoveriesGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance % (Gross) |
| B-P Variance % - Rentable Area | `BPVariancePctRentableAreaGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance % (Gross) |
| B-P Variance % - Sub Total #1 (C+NC-D) | `BPVariancePctSubTotal1Gross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance % (Gross) |
| B-P Variance % - Sub Total #2 (PT-R) | `BPVariancePctSubTotal2Gross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance % (Gross) |
| B-P Variance% - Admin Fee Percentage | `BPVariancePctAdminFeePercentageGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance % (Gross) |
| B-P Variance % - Additions | `BPVariancePctAdditionsNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance % (Net) |
| B-P Variance % - Admin Fee Percentage Amount | `BPVariancePctAdminFeePercentageAmountNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance % (Net) |
| B-P Variance % - Administration Fees | `BPVariancePctAdministrationFeesNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance % (Net) |
| B-P Variance % - Cap Amount | `BPVariancePctCapAmountNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance % (Net) |
| B-P Variance % - Controllable Expenses | `BPVariancePctControllableExpensesNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance % (Net) |
| B-P Variance % - Deductions | `BPVariancePctDeductionsNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance % (Net) |
| B-P Variance % - GLA | `BPVariancePctGLANet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance % (Net) |
| B-P Variance % - Net Amount Due (NPT-PP) | `BPVariancePctNetAmountDueNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance % (Net) |
| B-P Variance % - Net Pass-Through (ST2*PRR) | `BPVariancePctNetPassThroughNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance % (Net) |
| B-P Variance % - Non-Controllable Expenses | `BPVariancePctNonControllableExpensesNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance % (Net) |
| B-P Variance % - Pass-Through (ST1+AF%+AF+A) | `BPVariancePctPassThroughNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance % (Net) |
| B-P Variance % - Pre Paid Amount | `BPVariancePctPrePaidAmountNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance % (Net) |
| B-P Variance % - Pro Rata Share Rate | `BPVariancePctProRataShareRateNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance % (Net) |
| B-P Variance % - Recoveries | `BPVariancePctRecoveriesNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance % (Net) |
| B-P Variance % - Rentable Area | `BPVariancePctRentableAreaNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance % (Net) |
| B-P Variance % - Sub Total #1 (C+NC-D) | `BPVariancePctSubTotal1Net` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance % (Net) |
| B-P Variance % - Sub Total #2 (PT-R) | `BPVariancePctSubTotal2Net` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance % (Net) |
| B-P Variance% - Admin Fee Percentage | `BPVariancePctAdminFeePercentageNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance % (Net) |
| B-P Variance - Additions | `BPVarianceAdditionsGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance (Gross) |
| B-P Variance - Admin Fee Percentage | `BPVarianceAdminFeePercentageGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance (Gross) |
| B-P Variance - Admin Fee Percentage Amount | `BPVarianceAdminFeePercentageAmountGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance (Gross) |
| B-P Variance - Administration Fees | `BPVarianceAdministrationFeesGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance (Gross) |
| B-P Variance - Cap Amount | `BPVarianceCapAmountGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance (Gross) |
| B-P Variance - Controllable Expenses | `BPVarianceControllableExpensesGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance (Gross) |
| B-P Variance - Deductions | `BPVarianceDeductionsGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance (Gross) |
| B-P Variance - GLA | `BPVarianceGLAGross` | `sTYPE_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance (Gross) |
| B-P Variance - Net Amount Due (NPT-PP) | `BPVarianceNetAmountDueGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance (Gross) |
| B-P Variance - Net Pass-Through (ST2*PRR) | `BPVarianceNetPassThroughGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance (Gross) |
| B-P Variance - Non-Controllable Expenses | `BPVarianceNonControllableExpensesGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance (Gross) |
| B-P Variance - Pass-Through (ST1+AF%+AF+A) | `BPVariancePassThroughGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance (Gross) |
| B-P Variance - Pre Paid Amount | `BPVariancePrePaidAmountGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance (Gross) |
| B-P Variance - Pro Rata Share Rate | `BPVarianceProRataShareRateGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance (Gross) |
| B-P Variance - Recoveries | `BPVarianceRecoveriesGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance (Gross) |
| B-P Variance - Rentable Area | `BPVarianceRentableAreaGross` | `sTYPE_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance (Gross) |
| B-P Variance - Sub Total #1 (C+NC-D) | `BPVarianceSubTotal1Gross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance (Gross) |
| B-P Variance - Sub Total #2 (PT-R) | `BPVarianceSubTotal2Gross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance (Gross) |
| B-P Variance - Additions | `BPVarianceAdditionsNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance (Net) |
| B-P Variance - Admin Fee Percentage | `BPVarianceAdminFeePercentageNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance (Net) |
| B-P Variance - Admin Fee Percentage Amount | `BPVarianceAdminFeePercentageAmountNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance (Net) |
| B-P Variance - Administration Fees | `BPVarianceAdministrationFeesNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance (Net) |
| B-P Variance - Cap Amount | `BPVarianceCapAmountNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance (Net) |
| B-P Variance - Controllable Expenses | `BPVarianceControllableExpensesNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance (Net) |
| B-P Variance - Deductions | `BPVarianceDeductionsNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance (Net) |
| B-P Variance - GLA | `BPVarianceGLANet` | `sTYPE_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance (Net) |
| B-P Variance - Net Amount Due (NPT-PP) | `BPVarianceNetAmountDueNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance (Net) |
| B-P Variance - Net Pass-Through (ST2*PRR) | `BPVarianceNetPassThroughNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance (Net) |
| B-P Variance - Non-Controllable Expenses | `BPVarianceNonControllableExpensesNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance (Net) |
| B-P Variance - Pass-Through (ST1+AF%+AF+A) | `BPVariancePassThroughNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance (Net) |
| B-P Variance - Pre Paid Amount | `BPVariancePrePaidAmountNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance (Net) |
| B-P Variance - Pro Rata Share Rate | `BPVarianceProRataShareRateNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance (Net) |
| B-P Variance - Recoveries | `BPVarianceRecoveriesNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance (Net) |
| B-P Variance - Rentable Area | `BPVarianceRentableAreaNet` | `sTYPE_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance (Net) |
| B-P Variance - Sub Total #1 (C+NC-D) | `BPVarianceSubTotal1Net` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance (Net) |
| B-P Variance - Sub Total #2 (PT-R) | `BPVarianceSubTotal2Net` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Budgeted-Prior Variance (Net) |
| Prior Approved Additions | `PriorApprovedAdditionsGross` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Approved (Gross) |
| Prior Approved Admin Fee Percentage | `PriorApprovedAdminFeePercentageGross` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Statement Audit - Prior Approved (Gross) |
| Prior Approved Admin Fee Percentage Amount | `PriorApprovedAdminFeePercentageAmountGrossNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Approved (Gross) |
| Prior Approved Administration Fees | `PriorApprovedAdministrationFeesGross` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Approved (Gross) |
| Prior Approved Cap Amount | `PriorApprovedCapAmountGrossNoZeroDef` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Approved (Gross) |
| Prior Approved Controllable Expenses | `PriorApprovedControllableExpensesGross` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Approved (Gross) |
| Prior Approved Deductions | `PriorApprovedDeductionsGross` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Approved (Gross) |
| Prior Approved GLA | `PriorApprovedGLAGross` | `sTYPE_AREA` | Global | No | No |  | Contract / Statement Audit - Prior Approved (Gross) |
| Prior Approved Net Amount Due (NPT-PP) | `PriorApprovedNetAmountDueGrossNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Approved (Gross) |
| Prior Approved Net Pass-Through (ST2*PRR) | `PriorApprovedNetPassThroughGrossNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Approved (Gross) |
| Prior Approved Net Pass-Through (ST2*PRR) Duplicate | `PriorApprovedNetPassThroughCOREFirmOnlyGrossNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Approved (Gross) |
| Prior Approved Non-Controllable Expenses | `PriorApprovedNonControllableExpensesGross` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Approved (Gross) |
| Prior Approved Pass-Through (ST1+AF%+AF+A) | `PriorApprovedPassThroughGrossNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Approved (Gross) |
| Prior Approved Pre Paid Amount | `PriorApprovedPrePaidAmountGross` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Approved (Gross) |
| Prior Approved Pro Rata Share Rate | `PriorApprovedProRataShareRateGross` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Statement Audit - Prior Approved (Gross) |
| Prior Approved Recoveries | `PriorApprovedRecoveriesGross` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Approved (Gross) |
| Prior Approved Rentable Area | `PriorApprovedRentableAreaGross` | `sTYPE_AREA` | Global | No | No |  | Contract / Statement Audit - Prior Approved (Gross) |
| Prior Approved Sub Total #1 (C+NC-D) | `PriorApprovedSubTotal1GrossNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Approved (Gross) |
| Prior Approved Sub Total #2 (PT-R) | `PriorApprovedSubTotal2GrossNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Approved (Gross) |
| Prior Approved Additions | `PriorApprovedAdditionsNet` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Approved (Net) |
| Prior Approved Admin Fee Percentage | `PriorApprovedAdminFeePercentageNet` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Statement Audit - Prior Approved (Net) |
| Prior Approved Admin Fee Percentage Amount | `PriorApprovedAdminFeePercentageAmountNetNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Approved (Net) |
| Prior Approved Administration Fees | `PriorApprovedAdministrationFeesNet` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Approved (Net) |
| Prior Approved Cap Amount | `PriorApprovedCapAmountNetNoZeroDef` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Approved (Net) |
| Prior Approved Controllable Expenses | `PriorApprovedControllableExpensesNet` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Approved (Net) |
| Prior Approved Deductions | `PriorApprovedDeductionsNet` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Approved (Net) |
| Prior Approved GLA | `PriorApprovedGLANet` | `sTYPE_AREA` | Global | No | No |  | Contract / Statement Audit - Prior Approved (Net) |
| Prior Approved Net Amount Due (NPT-PP) | `PriorApprovedNetAmountDueNetNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Approved (Net) |
| Prior Approved Net Pass-Through (ST2*PRR) | `PriorApprovedNetPassThroughNetNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Approved (Net) |
| Prior Approved Net Pass-Through (ST2*PRR) Duplicate | `PriorApprovedNetPassThroughCOREFirmOnlyNetNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Approved (Net) |
| Prior Approved Non-Controllable Expenses | `PriorApprovedNonControllableExpensesNet` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Approved (Net) |
| Prior Approved Pass-Through (ST1+AF%+AF+A) | `PriorApprovedPassThroughNetNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Approved (Net) |
| Prior Approved Pre Paid Amount | `PriorApprovedPrePaidAmountNet` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Approved (Net) |
| Prior Approved Pro Rata Share Rate | `PriorApprovedProRataShareRateNet` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Statement Audit - Prior Approved (Net) |
| Prior Approved Recoveries | `PriorApprovedRecoveriesNet` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Approved (Net) |
| Prior Approved Rentable Area | `PriorApprovedRentableAreaNet` | `sTYPE_AREA` | Global | No | No |  | Contract / Statement Audit - Prior Approved (Net) |
| Prior Approved Sub Total #1 (C+NC-D) | `PriorApprovedSubTotal1NetNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Approved (Net) |
| Prior Approved Sub Total #2 (PT-R) | `PriorApprovedSubTotal2NetNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Approved (Net) |
| Prior Budgeted Additions | `PriorBudgetedAdditionsGross` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Budgeted (Gross) |
| Prior Budgeted Admin Fee Percentage | `PriorBudgetedAdminFeePercentageGross` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Statement Audit - Prior Budgeted (Gross) |
| Prior Budgeted Admin Fee Percentage Amount | `PriorBudgetedAdminFeePercentageAmountGrossNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Budgeted (Gross) |
| Prior Budgeted Administration Fees | `PriorBudgetedAdministrationFeesGross` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Budgeted (Gross) |
| Prior Budgeted Cap Amount | `PriorBudgetedCapAmountGrossNoZeroDef` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Budgeted (Gross) |
| Prior Budgeted Controllable Expenses | `PriorBudgetedControllableExpensesGross` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Budgeted (Gross) |
| Prior Budgeted Deductions | `PriorBudgetedDeductionsGross` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Budgeted (Gross) |
| Prior Budgeted GLA | `PriorBudgetedGLAGross` | `sTYPE_AREA` | Global | No | No |  | Contract / Statement Audit - Prior Budgeted (Gross) |
| Prior Budgeted Net Amount Due (NPT-PP) | `PriorBudgetedNetAmountDueGrossNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Budgeted (Gross) |
| Prior Budgeted Net Pass-Through (ST2*PRR) | `PriorBudgetedNetPassThroughGrossNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Budgeted (Gross) |
| Prior Budgeted Net Pass-Through (ST2*PRR) Duplicate | `PriorBudgetedNetPassThroughCOREFirmOnlyGrossNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Budgeted (Gross) |
| Prior Budgeted Non-Controllable Expenses | `PriorBudgetedNonControllableExpensesGross` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Budgeted (Gross) |
| Prior Budgeted Pass-Through (ST1+AF%+AF+A) | `PriorBudgetedPassThroughGrossNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Budgeted (Gross) |
| Prior Budgeted Pre Paid Amount | `PriorBudgetedPrePaidAmountGross` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Budgeted (Gross) |
| Prior Budgeted Pro Rata Share Rate | `PriorBudgetedProRataShareRateGross` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Statement Audit - Prior Budgeted (Gross) |
| Prior Budgeted Recoveries | `PriorBudgetedRecoveriesGross` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Budgeted (Gross) |
| Prior Budgeted Rentable Area | `PriorBudgetedRentableAreaGross` | `sTYPE_AREA` | Global | No | No |  | Contract / Statement Audit - Prior Budgeted (Gross) |
| Prior Budgeted Sub Total #1 (C+NC-D) | `PriorBudgetedSubTotal1GrossNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Budgeted (Gross) |
| Prior Budgeted Sub Total #2 (PT-R) | `PriorBudgetedSubTotal2GrossNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Budgeted (Gross) |
| Prior Budgeted Additions | `PriorBudgetedAdditionsNet` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Budgeted (Net) |
| Prior Budgeted Admin Fee Percentage | `PriorBudgetedAdminFeePercentageNet` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Statement Audit - Prior Budgeted (Net) |
| Prior Budgeted Admin Fee Percentage Amount | `PriorBudgetedAdminFeePercentageAmountNetNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Budgeted (Net) |
| Prior Budgeted Administration Fees | `PriorBudgetedAdministrationFeesNet` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Budgeted (Net) |
| Prior Budgeted Cap Amount | `PriorBudgetedCapAmountNetNoZeroDef` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Budgeted (Net) |
| Prior Budgeted Controllable Expenses | `PriorBudgetedControllableExpensesNet` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Budgeted (Net) |
| Prior Budgeted Deductions | `PriorBudgetedDeductionsNet` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Budgeted (Net) |
| Prior Budgeted GLA | `PriorBudgetedGLANet` | `sTYPE_AREA` | Global | No | No |  | Contract / Statement Audit - Prior Budgeted (Net) |
| Prior Budgeted Net Amount Due (NPT-PP) | `PriorBudgetedNetAmountDueNetNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Budgeted (Net) |
| Prior Budgeted Net Pass-Through (ST2*PRR) | `PriorBudgetedNetPassThroughNetNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Budgeted (Net) |
| Prior Budgeted Net Pass-Through (ST2*PRR) Duplicate | `PriorBudgetedNetPassThroughCOREFirmOnlyNetNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Budgeted (Net) |
| Prior Budgeted Non-Controllable Expenses | `PriorBudgetedNonControllableExpensesNet` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Budgeted (Net) |
| Prior Budgeted Pass-Through (ST1+AF%+AF+A) | `PriorBudgetedPassThroughNetNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Budgeted (Net) |
| Prior Budgeted Pre Paid Amount | `PriorBudgetedPrePaidAmountNet` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Budgeted (Net) |
| Prior Budgeted Pro Rata Share Rate | `PriorBudgetedProRataShareRateNet` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Statement Audit - Prior Budgeted (Net) |
| Prior Budgeted Recoveries | `PriorBudgetedRecoveriesNet` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Budgeted (Net) |
| Prior Budgeted Rentable Area | `PriorBudgetedRentableAreaNet` | `sTYPE_AREA` | Global | No | No |  | Contract / Statement Audit - Prior Budgeted (Net) |
| Prior Budgeted Sub Total #1 (C+NC-D) | `PriorBudgetedSubTotal1NetNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Budgeted (Net) |
| Prior Budgeted Sub Total #2 (PT-R) | `PriorBudgetedSubTotal2NetNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Budgeted (Net) |
| Prior Reported Additions | `PriorReportedAdditionsGross` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Reported (Gross) |
| Prior Reported Admin Fee Percentage | `PriorReportedAdminFeePercentageGross` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Statement Audit - Prior Reported (Gross) |
| Prior Reported Admin Fee Percentage Amount | `PriorReportedAdminFeePercentageAmountGrossNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Reported (Gross) |
| Prior Reported Administration Fees | `PriorReportedAdministrationFeesGross` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Reported (Gross) |
| Prior Reported Cap Amount | `PriorReportedCapAmountGrossNoZeroDef` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Reported (Gross) |
| Prior Reported Controllable Expenses | `PriorReportedControllableExpensesGross` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Reported (Gross) |
| Prior Reported Deductions | `PriorReportedDeductionsGross` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Reported (Gross) |
| Prior Reported GLA | `PriorReportedGLAGross` | `sTYPE_AREA` | Global | No | No |  | Contract / Statement Audit - Prior Reported (Gross) |
| Prior Reported Net Amount Due (NPT-PP) | `PriorReportedNetAmountDueGrossNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Reported (Gross) |
| Prior Reported Net Pass-Through (ST2*PRR) | `PriorReportedNetPassThroughGrossNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Reported (Gross) |
| Prior Reported Net Pass-Through (ST2*PRR) Duplicate | `PriorReportedNetPassThroughCOREFirmOnlyGrossNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Reported (Gross) |
| Prior Reported Non-Controllable Expenses | `PriorReportedNonControllableExpensesGross` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Reported (Gross) |
| Prior Reported Pass-Through (ST1+AF%+AF+A) | `PriorReportedPassThroughGrossNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Reported (Gross) |
| Prior Reported Pre Paid Amount | `PriorReportedPrePaidAmountGross` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Reported (Gross) |
| Prior Reported Pro Rata Share Rate | `PriorReportedProRataShareRateGross` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Statement Audit - Prior Reported (Gross) |
| Prior Reported Recoveries | `PriorReportedRecoveriesGross` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Reported (Gross) |
| Prior Reported Rentable Area | `PriorReportedRentableAreaGross` | `sTYPE_AREA` | Global | No | No |  | Contract / Statement Audit - Prior Reported (Gross) |
| Prior Reported Sub Total #1 (C+NC-D) | `PriorReportedSubTotal1GrossNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Reported (Gross) |
| Prior Reported Sub Total #2 (PT-R) | `PriorReportedSubTotal2GrossNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Reported (Gross) |
| Prior Reported Additions | `PriorReportedAdditionsNet` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Reported (Net) |
| Prior Reported Admin Fee Percentage | `PriorReportedAdminFeePercentageNet` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Statement Audit - Prior Reported (Net) |
| Prior Reported Admin Fee Percentage Amount | `PriorReportedAdminFeePercentageAmountNetNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Reported (Net) |
| Prior Reported Administration Fees | `PriorReportedAdministrationFeesNet` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Reported (Net) |
| Prior Reported Cap Amount | `PriorReportedCapAmountNetNoZeroDef` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Reported (Net) |
| Prior Reported Controllable Expenses | `PriorReportedControllableExpensesNet` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Reported (Net) |
| Prior Reported Deductions | `PriorReportedDeductionsNet` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Reported (Net) |
| Prior Reported GLA | `PriorReportedGLANet` | `sTYPE_AREA` | Global | No | No |  | Contract / Statement Audit - Prior Reported (Net) |
| Prior Reported Net Amount Due (NPT-PP) | `PriorReportedNetAmountDueNetNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Reported (Net) |
| Prior Reported Net Pass-Through (ST2*PRR) | `PriorReportedNetPassThroughNetNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Reported (Net) |
| Prior Reported Net Pass-Through (ST2*PRR) Duplicate | `PriorReportedNetPassThroughCOREFirmOnlyNetNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Reported (Net) |
| Prior Reported Non-Controllable Expenses | `PriorReportedNonControllableExpensesNet` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Reported (Net) |
| Prior Reported Pass-Through (ST1+AF%+AF+A) | `PriorReportedPassThroughNetNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Reported (Net) |
| Prior Reported Pre Paid Amount | `PriorReportedPrePaidAmountNet` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Reported (Net) |
| Prior Reported Pro Rata Share Rate | `PriorReportedProRataShareRateNet` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Statement Audit - Prior Reported (Net) |
| Prior Reported Recoveries | `PriorReportedRecoveriesNet` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Prior Reported (Net) |
| Prior Reported Rentable Area | `PriorReportedRentableAreaNet` | `sTYPE_AREA` | Global | No | No |  | Contract / Statement Audit - Prior Reported (Net) |
| Prior Reported Sub Total #1 (C+NC-D) | `PriorReportedSubTotal1NetNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Reported (Net) |
| Prior Reported Sub Total #2 (PT-R) | `PriorReportedSubTotal2NetNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Prior Reported (Net) |
| Reported Additions | `ReportedAdditionsGross` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Reported (Gross) |
| Reported Admin Fee Percentage Amount | `ReportedAdminFeePercentageAmountGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported (Gross) |
| Reported Administration Fees | `ReportedAdministrationFeesGross` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Reported (Gross) |
| Reported Controllable Expenses | `ReportedControllableExpensesGross` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Reported (Gross) |
| Reported Deductions | `ReportedDeductionsGross` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Reported (Gross) |
| Reported Net Amount Due (NPT-PP) | `ReportedNetAmountDueGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported (Gross) |
| Reported Net Pass-Through (ST2*PRR) | `ReportedNetPassThroughGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported (Gross) |
| Reported Net Pass-Through (ST2*PRR) Duplicate | `ReportedNetPassThroughCOREFirmOnlyGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported (Gross) |
| Reported Non-Controllable Expenses | `ReportedNonControllableExpensesGross` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Reported (Gross) |
| Reported Pass-Through (ST1+AF%+AF+A) | `ReportedPassThroughGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported (Gross) |
| Reported Recoveries | `ReportedRecoveriesGross` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Reported (Gross) |
| Reported Revised Amount Due (Net+Adj) | `ReportedRevisedNetAmountDueGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported (Gross) |
| Reported Sub Total #1 (C+NC-D) | `ReportedSubTotal1Gross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported (Gross) |
| Reported Sub Total #2 (PT-R) | `ReportedSubTotal2Gross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported (Gross) |
| Reported Adjustment Amount | `ReportedAdjustmentAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Reported (Gross/Net) |
| Reported Admin Fee Percentage | `ReportedAdminFeePercentage` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Statement Audit - Reported (Gross/Net) |
| Reported Cap Amount | `ReportedCapAmountNoZeroDef` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Reported (Gross/Net) |
| Reported GLA | `ReportedGLA` | `sTYPE_AREA` | Global | No | No |  | Contract / Statement Audit - Reported (Gross/Net) |
| Reported Pre Paid Amount | `ReportedPrePaidAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Reported (Gross/Net) |
| Reported Pro Rata Share Rate | `ReportedProRataShareRate` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Statement Audit - Reported (Gross/Net) |
| Reported Rentable Area | `ReportedRentableArea` | `sTYPE_AREA` | Global | No | No |  | Contract / Statement Audit - Reported (Gross/Net) |
| Reported Additions | `ReportedAdditionsNet` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Reported (Net) |
| Reported Admin Fee Percentage Amount | `ReportedAdminFeePercentageAmountNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported (Net) |
| Reported Administration Fees | `ReportedAdministrationFeesNet` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Reported (Net) |
| Reported Controllable Expenses | `ReportedControllableExpensesNet` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Reported (Net) |
| Reported Deductions | `ReportedDeductionsNet` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Reported (Net) |
| Reported Net Amount Due (NPT-PP) | `ReportedNetAmountDueNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported (Net) |
| Reported Net Pass-Through (ST2*PRR) | `ReportedNetPassThroughNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported (Net) |
| Reported Net Pass-Through (ST2*PRR) Duplicate | `ReportedNetPassThroughCOREFirmOnlyNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported (Net) |
| Reported Non-Controllable Expenses | `ReportedNonControllableExpensesNet` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Reported (Net) |
| Reported Pass-Through (ST1+AF%+AF+A) | `ReportedPassThroughNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported (Net) |
| Reported Recoveries | `ReportedRecoveriesNet` | `sTYPE_MONEY` | Global | No | No |  | Contract / Statement Audit - Reported (Net) |
| Reported Revised Amount Due (Net+Adj) | `ReportedRevisedNetAmountDueNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported (Net) |
| Reported Sub Total #1 (C+NC-D) | `ReportedSubTotal1Net` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported (Net) |
| Reported Sub Total #2 (PT-R) | `ReportedSubTotal2Net` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported (Net) |
| R-A Variance - Additions | `RAVarianceAdditionsGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Approved Variance (Gross) |
| R-A Variance - Admin Fee Percentage | `RAVarianceAdminFeePercentageGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Approved Variance (Gross) |
| R-A Variance - Admin Fee Percentage Amount | `RAVarianceAdminFeePercentageAmountGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Approved Variance (Gross) |
| R-A Variance - Administration Fees | `RAVarianceAdministrationFeesGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Approved Variance (Gross) |
| R-A Variance - Cap Amount | `RAVarianceCapAmountGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Approved Variance (Gross) |
| R-A Variance - Controllable Expenses | `RAVarianceControllableExpensesGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Approved Variance (Gross) |
| R-A Variance - Deductions | `RAVarianceDeductionsGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Approved Variance (Gross) |
| R-A Variance - GLA | `RAVarianceGLAGross` | `sTYPE_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Approved Variance (Gross) |
| R-A Variance - Net Amount Due (NPT-PP) | `RAVarianceNetAmountDueGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Approved Variance (Gross) |
| R-A Variance - Net Pass-Through (ST2*PRR) | `RAVarianceNetPassThroughGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Approved Variance (Gross) |
| R-A Variance - Non-Controllable Expenses | `RAVarianceNonControllableExpensesGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Approved Variance (Gross) |
| R-A Variance - Pass-Through (ST1+AF%+AF+A) | `RAVariancePassThroughGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Approved Variance (Gross) |
| R-A Variance - Pre Paid Amount | `RAVariancePrePaidAmountGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Approved Variance (Gross) |
| R-A Variance - Pro Rata Share Rate | `RAVarianceProRataShareRateGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Approved Variance (Gross) |
| R-A Variance - Recoveries | `RAVarianceRecoveriesGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Approved Variance (Gross) |
| R-A Variance - Rentable Area | `RAVarianceRentableAreaGross` | `sTYPE_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Approved Variance (Gross) |
| R-A Variance - Sub Total #1 (C+NC-D) | `RAVarianceSubTotal1Gross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Approved Variance (Gross) |
| R-A Variance - Sub Total #2 (PT-R) | `RAVarianceSubTotal2Gross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Approved Variance (Gross) |
| R-A Variance - Additions | `RAVarianceAdditionsNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Approved Variance (Net) |
| R-A Variance - Admin Fee Percentage | `RAVarianceAdminFeePercentageNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Approved Variance (Net) |
| R-A Variance - Admin Fee Percentage Amount | `RAVarianceAdminFeePercentageAmountNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Approved Variance (Net) |
| R-A Variance - Administration Fees | `RAVarianceAdministrationFeesNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Approved Variance (Net) |
| R-A Variance - Cap Amount | `RAVarianceCapAmountNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Approved Variance (Net) |
| R-A Variance - Controllable Expenses | `RAVarianceControllableExpensesNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Approved Variance (Net) |
| R-A Variance - Deductions | `RAVarianceDeductionsNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Approved Variance (Net) |
| R-A Variance - GLA | `RAVarianceGLANet` | `sTYPE_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Approved Variance (Net) |
| R-A Variance - Net Amount Due (NPT-PP) | `RAVarianceNetAmountDueNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Approved Variance (Net) |
| R-A Variance - Net Pass-Through (ST2*PRR) | `RAVarianceNetPassThroughNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Approved Variance (Net) |
| R-A Variance - Non-Controllable Expenses | `RAVarianceNonControllableExpensesNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Approved Variance (Net) |
| R-A Variance - Pass-Through (ST1+AF%+AF+A) | `RAVariancePassThroughNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Approved Variance (Net) |
| R-A Variance - Pre Paid Amount | `RAVariancePrePaidAmountNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Approved Variance (Net) |
| R-A Variance - Pro Rata Share Rate | `RAVarianceProRataShareRateNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Approved Variance (Net) |
| R-A Variance - Recoveries | `RAVarianceRecoveriesNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Approved Variance (Net) |
| R-A Variance - Rentable Area | `RAVarianceRentableAreaNet` | `sTYPE_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Approved Variance (Net) |
| R-A Variance - Sub Total #1 (C+NC-D) | `RAVarianceSubTotal1Net` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Approved Variance (Net) |
| R-A Variance - Sub Total #2 (PT-R) | `RAVarianceSubTotal2Net` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Approved Variance (Net) |
| R-P Variance % - Additions | `RPVariancePctAdditionsGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance % (Gross) |
| R-P Variance % - Admin Fee Percentage | `RPVariancePctAdminFeePercentageGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance % (Gross) |
| R-P Variance % - Admin Fee Percentage Amount | `RPVariancePctAdminFeePercentageAmountGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance % (Gross) |
| R-P Variance % - Administration Fees | `RPVariancePctAdministrationFeesGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance % (Gross) |
| R-P Variance % - Cap Amount | `RPVariancePctCapAmountGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance % (Gross) |
| R-P Variance % - Controllable Expenses | `RPVariancePctControllableExpensesGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance % (Gross) |
| R-P Variance % - Deductions | `RPVariancePctDeductionsGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance % (Gross) |
| R-P Variance % - GLA | `RPVariancePctGLAGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance % (Gross) |
| R-P Variance % - Net Amount Due (NPT-PP) | `RPVariancePctNetAmountDueGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance % (Gross) |
| R-P Variance % - Net Pass-Through (ST2*PRR) | `RPVariancePctNetPassThroughGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance % (Gross) |
| R-P Variance % - Non-Controllable Expenses | `RPVariancePctNonControllableExpensesGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance % (Gross) |
| R-P Variance % - Pass-Through (ST1+AF%+AF+A) | `RPVariancePctPassThroughGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance % (Gross) |
| R-P Variance % - Pre Paid Amount | `RPVariancePctPrePaidAmountGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance % (Gross) |
| R-P Variance % - Pro Rata Share Rate | `RPVariancePctProRataShareRateGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance % (Gross) |
| R-P Variance % - Recoveries | `RPVariancePctRecoveriesGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance % (Gross) |
| R-P Variance % - Rentable Area | `RPVariancePctRentableAreaGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance % (Gross) |
| R-P Variance % - Sub Total #1 (C+NC-D) | `RPVariancePctSubTotal1Gross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance % (Gross) |
| R-P Variance % - Sub Total #2 (PT-R) | `RPVariancePctSubTotal2Gross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance % (Gross) |
| R-P Variance % - Additions | `RPVariancePctAdditionsNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance % (Net) |
| R-P Variance % - Admin Fee Percentage | `RPVariancePctAdminFeePercentageNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance % (Net) |
| R-P Variance % - Admin Fee Percentage Amount | `RPVariancePctAdminFeePercentageAmountNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance % (Net) |
| R-P Variance % - Administration Fees | `RPVariancePctAdministrationFeesNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance % (Net) |
| R-P Variance % - Cap Amount | `RPVariancePctCapAmountNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance % (Net) |
| R-P Variance % - Controllable Expenses | `RPVariancePctControllableExpensesNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance % (Net) |
| R-P Variance % - Deductions | `RPVariancePctDeductionsNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance % (Net) |
| R-P Variance % - GLA | `RPVariancePctGLANet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance % (Net) |
| R-P Variance % - Net Amount Due (NPT-PP) | `RPVariancePctNetAmountDueNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance % (Net) |
| R-P Variance % - Net Pass-Through (ST2*PRR) | `RPVariancePctNetPassThroughNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance % (Net) |
| R-P Variance % - Non-Controllable Expenses | `RPVariancePctNonControllableExpensesNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance % (Net) |
| R-P Variance % - Pass-Through (ST1+AF%+AF+A) | `RPVariancePctPassThroughNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance % (Net) |
| R-P Variance % - Pre Paid Amount | `RPVariancePctPrePaidAmountNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance % (Net) |
| R-P Variance % - Pro Rata Share Rate | `RPVariancePctProRataShareRateNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance % (Net) |
| R-P Variance % - Recoveries | `RPVariancePctRecoveriesNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance % (Net) |
| R-P Variance % - Rentable Area | `RPVariancePctRentableAreaNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance % (Net) |
| R-P Variance % - Sub Total #1 (C+NC-D) | `RPVariancePctSubTotal1Net` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance % (Net) |
| R-P Variance % - Sub Total #2 (PT-R) | `RPVariancePctSubTotal2Net` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance % (Net) |
| R-P Variance - Additions | `RPVarianceAdditionsGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance (Gross) |
| R-P Variance - Admin Fee Percentage | `RPVarianceAdminFeePercentageGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance (Gross) |
| R-P Variance - Admin Fee Percentage Amount | `RPVarianceAdminFeePercentageAmountGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance (Gross) |
| R-P Variance - Administration Fees | `RPVarianceAdministrationFeesGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance (Gross) |
| R-P Variance - Cap Amount | `RPVarianceCapAmountGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance (Gross) |
| R-P Variance - Controllable Expenses | `RPVarianceControllableExpensesGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance (Gross) |
| R-P Variance - Deductions | `RPVarianceDeductionsGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance (Gross) |
| R-P Variance - GLA | `RPVarianceGLAGross` | `sTYPE_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance (Gross) |
| R-P Variance - Net Amount Due (NPT-PP) | `RPVarianceNetAmountDueGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance (Gross) |
| R-P Variance - Net Pass-Through (ST2*PRR) | `RPVarianceNetPassThroughGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance (Gross) |
| R-P Variance - Non-Controllable Expenses | `RPVarianceNonControllableExpensesGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance (Gross) |
| R-P Variance - Pass-Through (ST1+AF%+AF+A) | `RPVariancePassThroughGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance (Gross) |
| R-P Variance - Pre Paid Amount | `RPVariancePrePaidAmountGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance (Gross) |
| R-P Variance - Pro Rata Share Rate | `RPVarianceProRataShareRateGross` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance (Gross) |
| R-P Variance - Recoveries | `RPVarianceRecoveriesGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance (Gross) |
| R-P Variance - Rentable Area | `RPVarianceRentableAreaGross` | `sTYPE_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance (Gross) |
| R-P Variance - Sub Total #1 (C+NC-D) | `RPVarianceSubTotal1Gross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance (Gross) |
| R-P Variance - Sub Total #2 (PT-R) | `RPVarianceSubTotal2Gross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance (Gross) |
| R-P Variance - Additions | `RPVarianceAdditionsNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance (Net) |
| R-P Variance - Admin Fee Percentage | `RPVarianceAdminFeePercentageNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance (Net) |
| R-P Variance - Admin Fee Percentage Amount | `RPVarianceAdminFeePercentageAmountNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance (Net) |
| R-P Variance - Administration Fees | `RPVarianceAdministrationFeesNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance (Net) |
| R-P Variance - Cap Amount | `RPVarianceCapAmountNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance (Net) |
| R-P Variance - Controllable Expenses | `RPVarianceControllableExpensesNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance (Net) |
| R-P Variance - Deductions | `RPVarianceDeductionsNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance (Net) |
| R-P Variance - GLA | `RPVarianceGLANet` | `sTYPE_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance (Net) |
| R-P Variance - Net Amount Due (NPT-PP) | `RPVarianceNetAmountDueNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance (Net) |
| R-P Variance - Net Pass-Through (ST2*PRR) | `RPVarianceNetPassThroughNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance (Net) |
| R-P Variance - Non-Controllable Expenses | `RPVarianceNonControllableExpensesNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance (Net) |
| R-P Variance - Pass-Through (ST1+AF%+AF+A) | `RPVariancePassThroughNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance (Net) |
| R-P Variance - Pre Paid Amount | `RPVariancePrePaidAmountNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance (Net) |
| R-P Variance - Pro Rata Share Rate | `RPVarianceProRataShareRateNet` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance (Net) |
| R-P Variance - Recoveries | `RPVarianceRecoveriesNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance (Net) |
| R-P Variance - Rentable Area | `RPVarianceRentableAreaNet` | `sTYPE_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance (Net) |
| R-P Variance - Sub Total #1 (C+NC-D) | `RPVarianceSubTotal1Net` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance (Net) |
| R-P Variance - Sub Total #2 (PT-R) | `RPVarianceSubTotal2Net` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Statement Audit - Reported-Prior Variance (Net) |
