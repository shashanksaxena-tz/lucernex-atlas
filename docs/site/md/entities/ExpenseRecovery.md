# ExpenseRecovery

*565 fields, split across 4 physical tables · module: Expense Recovery (CAM / Reconciliation) · Postgres: `expense_recovery_part1,expense_recovery_part2,expense_recovery_part3,expense_recovery_part4`*

The CAM/OpEx recovery engine for a lease — one record per recoverable expense category (CAM, taxes, insurance, HVAC, etc.) per contract per year, carrying the base year, cap formula (percent or dollar, per-period or cumulative), pro rata share method, gross-up rules, and admin fee. It is by far the largest entity in the catalog (567 fields, 92% Global) because commercial CAM reconciliation is one of the most negotiated and variably-structured terms in a lease — every landlord uses a different combination of caps, exclusions, base-year stops, and gross-up methodologies, and Lx models each variant as its own field rather than a generic formula, which is why nearly half the fields are MONEY_MATH_OPERATION/PERCENT_MATH_OPERATION computed values.

Source: `data-fields/expense-recovery.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 565 |
| Catalogued fields | 567 (558 global, 9 firm) |
| Physical tables | 4 |
| Referenced by | 0 keys from 0 record types |
| Points at | 6 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 1 |

## What to know before rebuilding this

### Split across 4 physical tables

**Observed.** The logical record and the physical rows are not one to one: its columns are spread over expense_recovery_part1,expense_recovery_part2,expense_recovery_part3,expense_recovery_part4. That is the platform working around a column-count ceiling, and any rebuild has to decide deliberately whether to reproduce the split or collapse it.

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### 9 catalogued Firm-scope fields

**Observed.** Of 567 catalogued fields on this record, 9 are Firm scope — defined by this tenant rather than shipped by the platform. Firm-scope definitions are RGAF rows carrying IsGlobal, FirmID and IsClientExtensionField.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-161](../rules/CON-R-161.md) | Classifying any field · View Object Model filters · Of 7,047 fields: 3,437 editable (49%), 1,804 non-math computed (26%), 422 math (6%). 90% of all formula fields live on `ExpenseRecovery` · Field classification · Observed | Observed |

## Fields

### Relationships (foreign keys) (4)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AmendmentID` | Amendment | Contract Amendment ID | Global |  | [ContractAmendment](ContractAmendment.md) |
| `ContractID` | Contract | Contract ID | Global | yes | [Contract](Contract.md) |
| `CovenantID` | Covenant | Covenant ID | Global |  | [Covenant](Covenant.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DocumentIDList` | Documents | Document List | Global |  |  |

### Coded values (drop-downs) (14)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeApprovalStatusID` | Approval Status | Dropdown (Approval Status Code) | Global |  | Approval Status Code |
| `CodeBaseYearAmountTypeID` | Base Year Amount Type | Dropdown (Base Year Amount Type Code) | Global |  | Base Year Amount Type Code |
| `CodeCalculationMethodID` | Calculation Method | Dropdown (Calculation Method Code) | Global |  | Calculation Method Code |
| `CodeCapTypeID` | Cap Type | Dropdown (Cap Type Code) | Global |  | Cap Type Code |
| `CodeCurrencyTypeID` | Currency Type | Dropdown (Currency Type Code) | Global |  | Currency Type Code |
| `CodeEscalationPaymentMethodID` | Escalation Payment Method | Dropdown (Escalation Payment Method Code) | Global |  | Escalation Payment Method Code |
| `CodeExpRecBasedOnID` | Exp Rec Based On | Dropdown (Exp Rec Based On Code) | Global |  | Exp Rec Based On Code |
| `CodeExpenseGroupID` | Expense Group | Dropdown (Expense Group Code) | Global |  | Expense Group Code |
| `CodeExpenseTypeID` | Expense Type | Dropdown (Expense Type Code) | Global |  | Expense Type Code |
| `CodePaymentFrequencyID` | Payment Frequency | Dropdown (Frequency Code) | Global |  | Frequency Code |
| `CodeProRataShareMethodID` | Pro Rata Share Method | Dropdown (Pro Rata Share Method Code) | Global |  | Pro Rata Share Method Code |
| `CodeReconciliationFrequencyID` | Reconciliation Frequency | Dropdown (Frequency Code) | Global |  | Frequency Code |
| `CodeRecoveryGroupID` | Recovery Group | Dropdown (Recovery Group Code) | Global |  | Recovery Group Code |
| `CodeRecoveryTypeID` | Recovery Type | Dropdown (Recovery Type Code) | Global |  | Recovery Type Code |

### Money (332)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ABVarianceAdditionsGross` | A-B Variance - Additions | Currency | Global |  |  |
| `ABVarianceAdditionsNet` | A-B Variance - Additions | Currency | Global |  |  |
| `ABVarianceAdminFeePercentageAmountGross` | A-B Variance - Admin Fee Percentage Amount | Currency | Global |  |  |
| `ABVarianceAdminFeePercentageAmountNet` | A-B Variance - Admin Fee Percentage Amount | Currency | Global |  |  |
| `ABVarianceAdministrationFeesGross` | A-B Variance - Administration Fees | Currency | Global |  |  |
| `ABVarianceAdministrationFeesNet` | A-B Variance - Administration Fees | Currency | Global |  |  |
| `ABVarianceCapAmountGross` | A-B Variance - Cap Amount | Currency | Global |  |  |
| `ABVarianceCapAmountNet` | A-B Variance - Cap Amount | Currency | Global |  |  |
| `ABVarianceControllableExpensesGross` | A-B Variance - Controllable Expenses | Currency | Global |  |  |
| `ABVarianceControllableExpensesNet` | A-B Variance - Controllable Expenses | Currency | Global |  |  |
| `ABVarianceDeductionsGross` | A-B Variance - Deductions | Currency | Global |  |  |
| `ABVarianceDeductionsNet` | A-B Variance - Deductions | Currency | Global |  |  |
| `ABVarianceNetAmountDueGross` | A-B Variance - Net Amount Due (NPT-PP) | Currency | Global |  |  |
| `ABVarianceNetAmountDueNet` | A-B Variance - Net Amount Due (NPT-PP) | Currency | Global |  |  |
| `ABVarianceNetPassThroughGross` | A-B Variance - Net Pass-Through (ST2*PRR) | Currency | Global |  |  |
| `ABVarianceNetPassThroughNet` | A-B Variance - Net Pass-Through (ST2*PRR) | Currency | Global |  |  |
| `ABVarianceNonControllableExpensesGross` | A-B Variance - Non-Controllable Expenses | Currency | Global |  |  |
| `ABVarianceNonControllableExpensesNet` | A-B Variance - Non-Controllable Expenses | Currency | Global |  |  |
| `ABVariancePassThroughGross` | A-B Variance - Pass-Through (ST1+AF%+AF+A) | Currency | Global |  |  |
| `ABVariancePassThroughNet` | A-B Variance - Pass-Through (ST1+AF%+AF+A) | Currency | Global |  |  |
| `ABVariancePrePaidAmountGross` | A-B Variance - Pre Paid Amount | Currency | Global |  |  |
| `ABVariancePrePaidAmountNet` | A-B Variance - Pre Paid Amount | Currency | Global |  |  |
| `ABVarianceRecoveriesGross` | A-B Variance - Recoveries | Currency | Global |  |  |
| `ABVarianceRecoveriesNet` | A-B Variance - Recoveries | Currency | Global |  |  |
| `ABVarianceSubTotal1Gross` | A-B Variance - Sub Total #1 (C+NC-D) | Currency | Global |  |  |
| `ABVarianceSubTotal1Net` | A-B Variance - Sub Total #1 (C+NC-D) | Currency | Global |  |  |
| `ABVarianceSubTotal2Gross` | A-B Variance - Sub Total #2 (PT-R) | Currency | Global |  |  |
| `ABVarianceSubTotal2Net` | A-B Variance - Sub Total #2 (PT-R) | Currency | Global |  |  |
| `APVarianceAdditionsGross` | A-P Variance - Additions | Currency | Global |  |  |
| `APVarianceAdditionsNet` | A-P Variance - Additions | Currency | Global |  |  |
| `APVarianceAdminFeePercentageAmountGross` | A-P Variance - Admin Fee Percentage Amount | Currency | Global |  |  |
| `APVarianceAdminFeePercentageAmountNet` | A-P Variance - Admin Fee Percentage Amount | Currency | Global |  |  |
| `APVarianceAdministrationFeesGross` | A-P Variance - Administration Fees | Currency | Global |  |  |
| `APVarianceAdministrationFeesNet` | A-P Variance - Administration Fees | Currency | Global |  |  |
| `APVarianceCapAmountGross` | A-P Variance - Cap Amount | Currency | Global |  |  |
| `APVarianceCapAmountNet` | A-P Variance - Cap Amount | Currency | Global |  |  |
| `APVarianceControllableExpensesGross` | A-P Variance - Controllable Expenses | Currency | Global |  |  |
| `APVarianceControllableExpensesNet` | A-P Variance - Controllable Expenses | Currency | Global |  |  |
| `APVarianceDeductionsGross` | A-P Variance - Deductions | Currency | Global |  |  |
| `APVarianceDeductionsNet` | A-P Variance - Deductions | Currency | Global |  |  |
| `APVarianceNetAmountDueGross` | A-P Variance - Net Amount Due (NPT-PP) | Currency | Global |  |  |
| `APVarianceNetAmountDueNet` | A-P Variance - Net Amount Due (NPT-PP) | Currency | Global |  |  |
| `APVarianceNetPassThroughGross` | A-P Variance - Net Pass-Through (ST2*PRR) | Currency | Global |  |  |
| `APVarianceNetPassThroughNet` | A-P Variance - Net Pass-Through (ST2*PRR) | Currency | Global |  |  |
| `APVarianceNonControllableExpensesGross` | A-P Variance - Non-Controllable Expenses | Currency | Global |  |  |
| `APVarianceNonControllableExpensesNet` | A-P Variance - Non-Controllable Expenses | Currency | Global |  |  |
| `APVariancePassThroughGross` | A-P Variance - Pass-Through (ST1+AF%+AF+A) | Currency | Global |  |  |
| `APVariancePassThroughNet` | A-P Variance - Pass-Through (ST1+AF%+AF+A) | Currency | Global |  |  |
| `APVariancePctSubTotal2Gross` | A-P Variance % - Sub Total #2 (PT-R) | Currency | Global |  |  |
| `APVariancePctSubTotal2Net` | A-P Variance % - Sub Total #2 (PT-R) | Currency | Global |  |  |
| `APVariancePrePaidAmountGross` | A-P Variance - Pre Paid Amount | Currency | Global |  |  |
| `APVariancePrePaidAmountNet` | A-P Variance - Pre Paid Amount | Currency | Global |  |  |
| `APVarianceRecoveriesGross` | A-P Variance - Recoveries | Currency | Global |  |  |
| `APVarianceRecoveriesNet` | A-P Variance - Recoveries | Currency | Global |  |  |
| `APVarianceSubTotal1Gross` | A-P Variance - Sub Total #1 (C+NC-D) | Currency | Global |  |  |
| `APVarianceSubTotal1Net` | A-P Variance - Sub Total #1 (C+NC-D) | Currency | Global |  |  |
| `APVarianceSubTotal2Gross` | A-P Variance - Sub Total #2 (PT-R) | Currency | Global |  |  |
| `APVarianceSubTotal2Net` | A-P Variance - Sub Total #2 (PT-R) | Currency | Global |  |  |
| `ApprovedAdditionsGross` | Approved Additions | Currency | Global |  |  |
| `ApprovedAdditionsNet` | Approved Additions | Currency | Global |  |  |
| `ApprovedAdjustmentAmount` | Approved Adjustment Amount | Currency | Global |  |  |
| `ApprovedAdminFeePercentageAmountGross` | Approved Admin Fee Percentage Amount | Currency | Global |  |  |
| `ApprovedAdminFeePercentageAmountNet` | Approved Admin Fee Percentage Amount | Currency | Global |  |  |
| `ApprovedAdministrationFeesGross` | Approved Administration Fees | Currency | Global |  |  |
| `ApprovedAdministrationFeesNet` | Approved Administration Fees | Currency | Global |  |  |
| `ApprovedCapAmountNoZeroDef` | Approved Cap Amount | Currency | Global |  |  |
| `ApprovedControllableExpensesGross` | Approved Controllable Expenses | Currency | Global |  |  |
| `ApprovedControllableExpensesNet` | Approved Controllable Expenses | Currency | Global |  |  |
| `ApprovedDeductionsGross` | Approved Deductions | Currency | Global |  |  |
| `ApprovedDeductionsNet` | Approved Deductions | Currency | Global |  |  |
| `ApprovedNetAmountDueGross` | Approved Net Amount Due (NPT-PP) | Currency | Global |  |  |
| `ApprovedNetAmountDueNet` | Approved Net Amount Due (NPT-PP) | Currency | Global |  |  |
| `ApprovedNetPassThroughCOREFirmOnlyGross` | Approved Net Pass-Through (ST2*PRS*Occ) Duplicate | Currency | Global |  |  |
| `ApprovedNetPassThroughCOREFirmOnlyNet` | Approved Net Pass-Through (ST2*PRS*Occ) Duplicate | Currency | Global |  |  |
| `ApprovedNetPassThroughGross` | Approved Net Pass-Through (ST2*PRS*Occ) | Currency | Global |  |  |
| `ApprovedNetPassThroughNet` | Approved Net Pass-Through (ST2*PRS*Occ) | Currency | Global |  |  |
| `ApprovedNonControllableExpensesGross` | Approved Non-Controllable Expenses | Currency | Global |  |  |
| `ApprovedNonControllableExpensesNet` | Approved Non-Controllable Expenses | Currency | Global |  |  |
| `ApprovedPassThroughGross` | Approved Pass-Through (ST1+AF%+AF+A) | Currency | Global |  |  |
| `ApprovedPassThroughNet` | Approved Pass-Through (ST1+AF%+AF+A) | Currency | Global |  |  |
| `ApprovedPrePaidAmount` | Approved Pre Paid Amount | Currency | Global |  |  |
| `ApprovedRecoveriesGross` | Approved Recoveries | Currency | Global |  |  |
| `ApprovedRecoveriesNet` | Approved Recoveries | Currency | Global |  |  |
| `ApprovedRevisedNetAmountDueGross` | Approved Revised Amount Due (Net+Adj) | Currency | Global |  |  |
| `ApprovedRevisedNetAmountDueNet` | Approved Revised Amount Due (Net+Adj) | Currency | Global |  |  |
| `ApprovedSubTotal1Gross` | Approved Sub Total #1 (C+NC-D) | Currency | Global |  |  |
| `ApprovedSubTotal1Net` | Approved Sub Total #1 (C+NC-D) | Currency | Global |  |  |
| `ApprovedSubTotal2Gross` | Approved Sub Total #2 (PT-R) | Currency | Global |  |  |
| `ApprovedSubTotal2Net` | Approved Sub Total #2 (PT-R) | Currency | Global |  |  |
| `BPVarianceAdditionsGross` | B-P Variance - Additions | Currency | Global |  |  |
| `BPVarianceAdditionsNet` | B-P Variance - Additions | Currency | Global |  |  |
| `BPVarianceAdminFeePercentageAmountGross` | B-P Variance - Admin Fee Percentage Amount | Currency | Global |  |  |
| `BPVarianceAdminFeePercentageAmountNet` | B-P Variance - Admin Fee Percentage Amount | Currency | Global |  |  |
| `BPVarianceAdministrationFeesGross` | B-P Variance - Administration Fees | Currency | Global |  |  |
| `BPVarianceAdministrationFeesNet` | B-P Variance - Administration Fees | Currency | Global |  |  |
| `BPVarianceCapAmountGross` | B-P Variance - Cap Amount | Currency | Global |  |  |
| `BPVarianceCapAmountNet` | B-P Variance - Cap Amount | Currency | Global |  |  |
| `BPVarianceControllableExpensesGross` | B-P Variance - Controllable Expenses | Currency | Global |  |  |
| `BPVarianceControllableExpensesNet` | B-P Variance - Controllable Expenses | Currency | Global |  |  |
| `BPVarianceDeductionsGross` | B-P Variance - Deductions | Currency | Global |  |  |
| `BPVarianceDeductionsNet` | B-P Variance - Deductions | Currency | Global |  |  |
| `BPVarianceNetAmountDueGross` | B-P Variance - Net Amount Due (NPT-PP) | Currency | Global |  |  |
| `BPVarianceNetAmountDueNet` | B-P Variance - Net Amount Due (NPT-PP) | Currency | Global |  |  |
| `BPVarianceNetPassThroughGross` | B-P Variance - Net Pass-Through (ST2*PRR) | Currency | Global |  |  |
| `BPVarianceNetPassThroughNet` | B-P Variance - Net Pass-Through (ST2*PRR) | Currency | Global |  |  |
| `BPVarianceNonControllableExpensesGross` | B-P Variance - Non-Controllable Expenses | Currency | Global |  |  |
| `BPVarianceNonControllableExpensesNet` | B-P Variance - Non-Controllable Expenses | Currency | Global |  |  |
| `BPVariancePassThroughGross` | B-P Variance - Pass-Through (ST1+AF%+AF+A) | Currency | Global |  |  |
| `BPVariancePassThroughNet` | B-P Variance - Pass-Through (ST1+AF%+AF+A) | Currency | Global |  |  |
| `BPVariancePrePaidAmountGross` | B-P Variance - Pre Paid Amount | Currency | Global |  |  |
| `BPVariancePrePaidAmountNet` | B-P Variance - Pre Paid Amount | Currency | Global |  |  |
| `BPVarianceRecoveriesGross` | B-P Variance - Recoveries | Currency | Global |  |  |
| `BPVarianceRecoveriesNet` | B-P Variance - Recoveries | Currency | Global |  |  |
| `BPVarianceSubTotal1Gross` | B-P Variance - Sub Total #1 (C+NC-D) | Currency | Global |  |  |
| `BPVarianceSubTotal1Net` | B-P Variance - Sub Total #1 (C+NC-D) | Currency | Global |  |  |
| `BPVarianceSubTotal2Gross` | B-P Variance - Sub Total #2 (PT-R) | Currency | Global |  |  |
| `BPVarianceSubTotal2Net` | B-P Variance - Sub Total #2 (PT-R) | Currency | Global |  |  |
| `BaseYearAmount` | Base Year Amount | Currency | Global |  |  |
| `BudgetedAdditionsGross` | Budgeted Additions | Currency | Global |  |  |
| `BudgetedAdditionsNet` | Budgeted Additions | Currency | Global |  |  |
| `BudgetedAdminFeePercentageAmountGross` | Budgeted Admin Fee Percentage Amount | Currency | Global |  |  |
| `BudgetedAdminFeePercentageAmountNet` | Budgeted Admin Fee Percentage Amount | Currency | Global |  |  |
| `BudgetedAdministrationFeesGross` | Budgeted Administration Fees | Currency | Global |  |  |
| `BudgetedAdministrationFeesNet` | Budgeted Administration Fees | Currency | Global |  |  |
| `BudgetedCapAmountNoZeroDef` | Budgeted Cap Amount | Currency | Global |  |  |
| `BudgetedControllableExpensesGross` | Budgeted Controllable Expenses | Currency | Global |  |  |
| `BudgetedControllableExpensesNet` | Budgeted Controllable Expenses | Currency | Global |  |  |
| `BudgetedDeductionsGross` | Budgeted Deductions | Currency | Global |  |  |
| `BudgetedDeductionsNet` | Budgeted Deductions | Currency | Global |  |  |
| `BudgetedNetAmountDueGross` | Budgeted Net Amount Due (NPT-PP) | Currency | Global |  |  |
| `BudgetedNetAmountDueNet` | Budgeted Net Amount Due (NPT-PP) | Currency | Global |  |  |
| `BudgetedNetPassThroughGross` | Budgeted Net Pass-Through (ST2*PRR) | Currency | Global |  |  |
| `BudgetedNetPassThroughNet` | Budgeted Net Pass-Through (ST2*PRR) | Currency | Global |  |  |
| `BudgetedNonControllableExpensesGross` | Budgeted Non-Controllable Expenses | Currency | Global |  |  |
| `BudgetedNonControllableExpensesNet` | Budgeted Non-Controllable Expenses | Currency | Global |  |  |
| `BudgetedPassThroughGross` | Budgeted Pass-Through (ST1+AF%+AF+A) | Currency | Global |  |  |
| `BudgetedPassThroughNet` | Budgeted Pass-Through (ST1+AF%+AF+A) | Currency | Global |  |  |
| `BudgetedPrePaidAmount` | Budgeted Pre Paid Amount | Currency | Global |  |  |
| `BudgetedRecoveriesGross` | Budgeted Recoveries | Currency | Global |  |  |
| `BudgetedRecoveriesNet` | Budgeted Recoveries | Currency | Global |  |  |
| `BudgetedSubTotal1Gross` | Budgeted Sub Total #1 (C+NC-D) | Currency | Global |  |  |
| `BudgetedSubTotal1Net` | Budgeted Sub Total #1 (C+NC-D) | Currency | Global |  |  |
| `BudgetedSubTotal2Gross` | Budgeted Sub Total #2 (PT-R) | Currency | Global |  |  |
| `BudgetedSubTotal2Net` | Budgeted Sub Total #2 (PT-R) | Currency | Global |  |  |
| `CapAmountChangeValue` | Cap Amount Per-Period Change (Value) | Currency | Global |  |  |
| `CatchUpPaymentAmount` | Catch Up Payment Amount | Currency | Global |  |  |
| `CurrentEscrowPayment` | Current Escrow Payment | Currency | Global |  |  |
| `EscalationAmountIncrease` | Escalation Amount Increase | Currency | Global |  |  |
| `GrossupRate` | Grossup Rate | Currency | Global |  |  |
| `MaximumValue` | Maximum Value | Currency | Global |  |  |
| `MinimumValue` | Minimum Value | Currency | Global |  |  |
| `NewEscalationPayment` | New Escalation Payment | Currency | Global |  |  |
| `PriorApprovedAdditionsGross` | Prior Approved Additions | Currency | Global |  |  |
| `PriorApprovedAdditionsNet` | Prior Approved Additions | Currency | Global |  |  |
| `PriorApprovedAdminFeePercentageAmountGrossNoZeroDef` | Prior Approved Admin Fee Percentage Amount | Currency | Global |  |  |
| `PriorApprovedAdminFeePercentageAmountNetNoZeroDef` | Prior Approved Admin Fee Percentage Amount | Currency | Global |  |  |
| `PriorApprovedAdministrationFeesGross` | Prior Approved Administration Fees | Currency | Global |  |  |
| `PriorApprovedAdministrationFeesNet` | Prior Approved Administration Fees | Currency | Global |  |  |
| `PriorApprovedCapAmountGrossNoZeroDef` | Prior Approved Cap Amount | Currency | Global |  |  |
| `PriorApprovedCapAmountNetNoZeroDef` | Prior Approved Cap Amount | Currency | Global |  |  |
| `PriorApprovedControllableExpensesGross` | Prior Approved Controllable Expenses | Currency | Global |  |  |
| `PriorApprovedControllableExpensesNet` | Prior Approved Controllable Expenses | Currency | Global |  |  |
| `PriorApprovedDeductionsGross` | Prior Approved Deductions | Currency | Global |  |  |
| `PriorApprovedDeductionsNet` | Prior Approved Deductions | Currency | Global |  |  |
| `PriorApprovedNetAmountDueGrossNoZeroDef` | Prior Approved Net Amount Due (NPT-PP) | Currency | Global |  |  |
| `PriorApprovedNetAmountDueNetNoZeroDef` | Prior Approved Net Amount Due (NPT-PP) | Currency | Global |  |  |
| `PriorApprovedNetPassThroughCOREFirmOnlyGrossNoZeroDef` | Prior Approved Net Pass-Through (ST2*PRR) Duplicate | Currency | Global |  |  |
| `PriorApprovedNetPassThroughCOREFirmOnlyNetNoZeroDef` | Prior Approved Net Pass-Through (ST2*PRR) Duplicate | Currency | Global |  |  |
| `PriorApprovedNetPassThroughGrossNoZeroDef` | Prior Approved Net Pass-Through (ST2*PRR) | Currency | Global |  |  |
| `PriorApprovedNetPassThroughNetNoZeroDef` | Prior Approved Net Pass-Through (ST2*PRR) | Currency | Global |  |  |
| `PriorApprovedNonControllableExpensesGross` | Prior Approved Non-Controllable Expenses | Currency | Global |  |  |
| `PriorApprovedNonControllableExpensesNet` | Prior Approved Non-Controllable Expenses | Currency | Global |  |  |
| `PriorApprovedPassThroughGrossNoZeroDef` | Prior Approved Pass-Through (ST1+AF%+AF+A) | Currency | Global |  |  |
| `PriorApprovedPassThroughNetNoZeroDef` | Prior Approved Pass-Through (ST1+AF%+AF+A) | Currency | Global |  |  |
| `PriorApprovedPrePaidAmountGross` | Prior Approved Pre Paid Amount | Currency | Global |  |  |
| `PriorApprovedPrePaidAmountNet` | Prior Approved Pre Paid Amount | Currency | Global |  |  |
| `PriorApprovedRecoveriesGross` | Prior Approved Recoveries | Currency | Global |  |  |
| `PriorApprovedRecoveriesNet` | Prior Approved Recoveries | Currency | Global |  |  |
| `PriorApprovedSubTotal1GrossNoZeroDef` | Prior Approved Sub Total #1 (C+NC-D) | Currency | Global |  |  |
| `PriorApprovedSubTotal1NetNoZeroDef` | Prior Approved Sub Total #1 (C+NC-D) | Currency | Global |  |  |
| `PriorApprovedSubTotal2GrossNoZeroDef` | Prior Approved Sub Total #2 (PT-R) | Currency | Global |  |  |
| `PriorApprovedSubTotal2NetNoZeroDef` | Prior Approved Sub Total #2 (PT-R) | Currency | Global |  |  |
| `PriorBudgetedAdditionsGross` | Prior Budgeted Additions | Currency | Global |  |  |
| `PriorBudgetedAdditionsNet` | Prior Budgeted Additions | Currency | Global |  |  |
| `PriorBudgetedAdminFeePercentageAmountGrossNoZeroDef` | Prior Budgeted Admin Fee Percentage Amount | Currency | Global |  |  |
| `PriorBudgetedAdminFeePercentageAmountNetNoZeroDef` | Prior Budgeted Admin Fee Percentage Amount | Currency | Global |  |  |
| `PriorBudgetedAdministrationFeesGross` | Prior Budgeted Administration Fees | Currency | Global |  |  |
| `PriorBudgetedAdministrationFeesNet` | Prior Budgeted Administration Fees | Currency | Global |  |  |
| `PriorBudgetedCapAmountGrossNoZeroDef` | Prior Budgeted Cap Amount | Currency | Global |  |  |
| `PriorBudgetedCapAmountNetNoZeroDef` | Prior Budgeted Cap Amount | Currency | Global |  |  |
| `PriorBudgetedControllableExpensesGross` | Prior Budgeted Controllable Expenses | Currency | Global |  |  |
| `PriorBudgetedControllableExpensesNet` | Prior Budgeted Controllable Expenses | Currency | Global |  |  |
| `PriorBudgetedDeductionsGross` | Prior Budgeted Deductions | Currency | Global |  |  |
| `PriorBudgetedDeductionsNet` | Prior Budgeted Deductions | Currency | Global |  |  |
| `PriorBudgetedNetAmountDueGrossNoZeroDef` | Prior Budgeted Net Amount Due (NPT-PP) | Currency | Global |  |  |
| `PriorBudgetedNetAmountDueNetNoZeroDef` | Prior Budgeted Net Amount Due (NPT-PP) | Currency | Global |  |  |
| `PriorBudgetedNetPassThroughCOREFirmOnlyGrossNoZeroDef` | Prior Budgeted Net Pass-Through (ST2*PRR) Duplicate | Currency | Global |  |  |
| `PriorBudgetedNetPassThroughCOREFirmOnlyNetNoZeroDef` | Prior Budgeted Net Pass-Through (ST2*PRR) Duplicate | Currency | Global |  |  |
| `PriorBudgetedNetPassThroughGrossNoZeroDef` | Prior Budgeted Net Pass-Through (ST2*PRR) | Currency | Global |  |  |
| `PriorBudgetedNetPassThroughNetNoZeroDef` | Prior Budgeted Net Pass-Through (ST2*PRR) | Currency | Global |  |  |
| `PriorBudgetedNonControllableExpensesGross` | Prior Budgeted Non-Controllable Expenses | Currency | Global |  |  |
| `PriorBudgetedNonControllableExpensesNet` | Prior Budgeted Non-Controllable Expenses | Currency | Global |  |  |
| `PriorBudgetedPassThroughGrossNoZeroDef` | Prior Budgeted Pass-Through (ST1+AF%+AF+A) | Currency | Global |  |  |
| `PriorBudgetedPassThroughNetNoZeroDef` | Prior Budgeted Pass-Through (ST1+AF%+AF+A) | Currency | Global |  |  |
| `PriorBudgetedPrePaidAmountGross` | Prior Budgeted Pre Paid Amount | Currency | Global |  |  |
| `PriorBudgetedPrePaidAmountNet` | Prior Budgeted Pre Paid Amount | Currency | Global |  |  |
| `PriorBudgetedRecoveriesGross` | Prior Budgeted Recoveries | Currency | Global |  |  |
| `PriorBudgetedRecoveriesNet` | Prior Budgeted Recoveries | Currency | Global |  |  |
| `PriorBudgetedSubTotal1GrossNoZeroDef` | Prior Budgeted Sub Total #1 (C+NC-D) | Currency | Global |  |  |
| `PriorBudgetedSubTotal1NetNoZeroDef` | Prior Budgeted Sub Total #1 (C+NC-D) | Currency | Global |  |  |
| `PriorBudgetedSubTotal2GrossNoZeroDef` | Prior Budgeted Sub Total #2 (PT-R) | Currency | Global |  |  |
| `PriorBudgetedSubTotal2NetNoZeroDef` | Prior Budgeted Sub Total #2 (PT-R) | Currency | Global |  |  |
| `PriorReportedAdditionsGross` | Prior Reported Additions | Currency | Global |  |  |
| `PriorReportedAdditionsNet` | Prior Reported Additions | Currency | Global |  |  |
| `PriorReportedAdminFeePercentageAmountGrossNoZeroDef` | Prior Reported Admin Fee Percentage Amount | Currency | Global |  |  |
| `PriorReportedAdminFeePercentageAmountNetNoZeroDef` | Prior Reported Admin Fee Percentage Amount | Currency | Global |  |  |
| `PriorReportedAdministrationFeesGross` | Prior Reported Administration Fees | Currency | Global |  |  |
| `PriorReportedAdministrationFeesNet` | Prior Reported Administration Fees | Currency | Global |  |  |
| `PriorReportedCapAmountGrossNoZeroDef` | Prior Reported Cap Amount | Currency | Global |  |  |
| `PriorReportedCapAmountNetNoZeroDef` | Prior Reported Cap Amount | Currency | Global |  |  |
| `PriorReportedControllableExpensesGross` | Prior Reported Controllable Expenses | Currency | Global |  |  |
| `PriorReportedControllableExpensesNet` | Prior Reported Controllable Expenses | Currency | Global |  |  |
| `PriorReportedDeductionsGross` | Prior Reported Deductions | Currency | Global |  |  |
| `PriorReportedDeductionsNet` | Prior Reported Deductions | Currency | Global |  |  |
| `PriorReportedNetAmountDueGrossNoZeroDef` | Prior Reported Net Amount Due (NPT-PP) | Currency | Global |  |  |
| `PriorReportedNetAmountDueNetNoZeroDef` | Prior Reported Net Amount Due (NPT-PP) | Currency | Global |  |  |
| `PriorReportedNetPassThroughCOREFirmOnlyGrossNoZeroDef` | Prior Reported Net Pass-Through (ST2*PRR) Duplicate | Currency | Global |  |  |
| `PriorReportedNetPassThroughCOREFirmOnlyNetNoZeroDef` | Prior Reported Net Pass-Through (ST2*PRR) Duplicate | Currency | Global |  |  |
| `PriorReportedNetPassThroughGrossNoZeroDef` | Prior Reported Net Pass-Through (ST2*PRR) | Currency | Global |  |  |
| `PriorReportedNetPassThroughNetNoZeroDef` | Prior Reported Net Pass-Through (ST2*PRR) | Currency | Global |  |  |
| `PriorReportedNonControllableExpensesGross` | Prior Reported Non-Controllable Expenses | Currency | Global |  |  |
| `PriorReportedNonControllableExpensesNet` | Prior Reported Non-Controllable Expenses | Currency | Global |  |  |
| `PriorReportedPassThroughGrossNoZeroDef` | Prior Reported Pass-Through (ST1+AF%+AF+A) | Currency | Global |  |  |
| `PriorReportedPassThroughNetNoZeroDef` | Prior Reported Pass-Through (ST1+AF%+AF+A) | Currency | Global |  |  |
| `PriorReportedPrePaidAmountGross` | Prior Reported Pre Paid Amount | Currency | Global |  |  |
| `PriorReportedPrePaidAmountNet` | Prior Reported Pre Paid Amount | Currency | Global |  |  |
| `PriorReportedRecoveriesGross` | Prior Reported Recoveries | Currency | Global |  |  |
| `PriorReportedRecoveriesNet` | Prior Reported Recoveries | Currency | Global |  |  |
| `PriorReportedSubTotal1GrossNoZeroDef` | Prior Reported Sub Total #1 (C+NC-D) | Currency | Global |  |  |
| `PriorReportedSubTotal1NetNoZeroDef` | Prior Reported Sub Total #1 (C+NC-D) | Currency | Global |  |  |
| `PriorReportedSubTotal2GrossNoZeroDef` | Prior Reported Sub Total #2 (PT-R) | Currency | Global |  |  |
| `PriorReportedSubTotal2NetNoZeroDef` | Prior Reported Sub Total #2 (PT-R) | Currency | Global |  |  |
| `ProposedCatchUpPaymentAmount` | Proposed Catch Up Payment Amount | Currency | Global |  |  |
| `ProposedEscalationPayment` | Proposed Escalation Payment | Currency | Global |  |  |
| `RAVarianceAdditionsGross` | R-A Variance - Additions | Currency | Global |  |  |
| `RAVarianceAdditionsNet` | R-A Variance - Additions | Currency | Global |  |  |
| `RAVarianceAdminFeePercentageAmountGross` | R-A Variance - Admin Fee Percentage Amount | Currency | Global |  |  |
| `RAVarianceAdminFeePercentageAmountNet` | R-A Variance - Admin Fee Percentage Amount | Currency | Global |  |  |
| `RAVarianceAdministrationFeesGross` | R-A Variance - Administration Fees | Currency | Global |  |  |
| `RAVarianceAdministrationFeesNet` | R-A Variance - Administration Fees | Currency | Global |  |  |
| `RAVarianceCapAmountGross` | R-A Variance - Cap Amount | Currency | Global |  |  |
| `RAVarianceCapAmountNet` | R-A Variance - Cap Amount | Currency | Global |  |  |
| `RAVarianceControllableExpensesGross` | R-A Variance - Controllable Expenses | Currency | Global |  |  |
| `RAVarianceControllableExpensesNet` | R-A Variance - Controllable Expenses | Currency | Global |  |  |
| `RAVarianceDeductionsGross` | R-A Variance - Deductions | Currency | Global |  |  |
| `RAVarianceDeductionsNet` | R-A Variance - Deductions | Currency | Global |  |  |
| `RAVarianceNetAmountDueGross` | R-A Variance - Net Amount Due (NPT-PP) | Currency | Global |  |  |
| `RAVarianceNetAmountDueNet` | R-A Variance - Net Amount Due (NPT-PP) | Currency | Global |  |  |
| `RAVarianceNetPassThroughGross` | R-A Variance - Net Pass-Through (ST2*PRR) | Currency | Global |  |  |
| `RAVarianceNetPassThroughNet` | R-A Variance - Net Pass-Through (ST2*PRR) | Currency | Global |  |  |
| `RAVarianceNonControllableExpensesGross` | R-A Variance - Non-Controllable Expenses | Currency | Global |  |  |
| `RAVarianceNonControllableExpensesNet` | R-A Variance - Non-Controllable Expenses | Currency | Global |  |  |
| `RAVariancePassThroughGross` | R-A Variance - Pass-Through (ST1+AF%+AF+A) | Currency | Global |  |  |
| `RAVariancePassThroughNet` | R-A Variance - Pass-Through (ST1+AF%+AF+A) | Currency | Global |  |  |
| `RAVariancePrePaidAmountGross` | R-A Variance - Pre Paid Amount | Currency | Global |  |  |
| `RAVariancePrePaidAmountNet` | R-A Variance - Pre Paid Amount | Currency | Global |  |  |
| `RAVarianceRecoveriesGross` | R-A Variance - Recoveries | Currency | Global |  |  |
| `RAVarianceRecoveriesNet` | R-A Variance - Recoveries | Currency | Global |  |  |
| `RAVarianceSubTotal1Gross` | R-A Variance - Sub Total #1 (C+NC-D) | Currency | Global |  |  |
| `RAVarianceSubTotal1Net` | R-A Variance - Sub Total #1 (C+NC-D) | Currency | Global |  |  |
| `RAVarianceSubTotal2Gross` | R-A Variance - Sub Total #2 (PT-R) | Currency | Global |  |  |
| `RAVarianceSubTotal2Net` | R-A Variance - Sub Total #2 (PT-R) | Currency | Global |  |  |
| `RPVarianceAdditionsGross` | R-P Variance - Additions | Currency | Global |  |  |
| `RPVarianceAdditionsNet` | R-P Variance - Additions | Currency | Global |  |  |
| `RPVarianceAdminFeePercentageAmountGross` | R-P Variance - Admin Fee Percentage Amount | Currency | Global |  |  |
| `RPVarianceAdminFeePercentageAmountNet` | R-P Variance - Admin Fee Percentage Amount | Currency | Global |  |  |
| `RPVarianceAdministrationFeesGross` | R-P Variance - Administration Fees | Currency | Global |  |  |
| `RPVarianceAdministrationFeesNet` | R-P Variance - Administration Fees | Currency | Global |  |  |
| `RPVarianceCapAmountGross` | R-P Variance - Cap Amount | Currency | Global |  |  |
| `RPVarianceCapAmountNet` | R-P Variance - Cap Amount | Currency | Global |  |  |
| `RPVarianceControllableExpensesGross` | R-P Variance - Controllable Expenses | Currency | Global |  |  |
| `RPVarianceControllableExpensesNet` | R-P Variance - Controllable Expenses | Currency | Global |  |  |
| `RPVarianceDeductionsGross` | R-P Variance - Deductions | Currency | Global |  |  |
| `RPVarianceDeductionsNet` | R-P Variance - Deductions | Currency | Global |  |  |
| `RPVarianceNetAmountDueGross` | R-P Variance - Net Amount Due (NPT-PP) | Currency | Global |  |  |
| `RPVarianceNetAmountDueNet` | R-P Variance - Net Amount Due (NPT-PP) | Currency | Global |  |  |
| `RPVarianceNetPassThroughGross` | R-P Variance - Net Pass-Through (ST2*PRR) | Currency | Global |  |  |
| `RPVarianceNetPassThroughNet` | R-P Variance - Net Pass-Through (ST2*PRR) | Currency | Global |  |  |
| `RPVarianceNonControllableExpensesGross` | R-P Variance - Non-Controllable Expenses | Currency | Global |  |  |
| `RPVarianceNonControllableExpensesNet` | R-P Variance - Non-Controllable Expenses | Currency | Global |  |  |
| `RPVariancePassThroughGross` | R-P Variance - Pass-Through (ST1+AF%+AF+A) | Currency | Global |  |  |
| `RPVariancePassThroughNet` | R-P Variance - Pass-Through (ST1+AF%+AF+A) | Currency | Global |  |  |
| `RPVariancePrePaidAmountGross` | R-P Variance - Pre Paid Amount | Currency | Global |  |  |
| `RPVariancePrePaidAmountNet` | R-P Variance - Pre Paid Amount | Currency | Global |  |  |
| `RPVarianceRecoveriesGross` | R-P Variance - Recoveries | Currency | Global |  |  |
| `RPVarianceRecoveriesNet` | R-P Variance - Recoveries | Currency | Global |  |  |
| `RPVarianceSubTotal1Gross` | R-P Variance - Sub Total #1 (C+NC-D) | Currency | Global |  |  |
| `RPVarianceSubTotal1Net` | R-P Variance - Sub Total #1 (C+NC-D) | Currency | Global |  |  |
| `RPVarianceSubTotal2Gross` | R-P Variance - Sub Total #2 (PT-R) | Currency | Global |  |  |
| `RPVarianceSubTotal2Net` | R-P Variance - Sub Total #2 (PT-R) | Currency | Global |  |  |
| `ReportedAdditionsGross` | Reported Additions | Currency | Global |  |  |
| `ReportedAdditionsNet` | Reported Additions | Currency | Global |  |  |
| `ReportedAdjustmentAmount` | Reported Adjustment Amount | Currency | Global |  |  |
| `ReportedAdminFeePercentageAmountGross` | Reported Admin Fee Percentage Amount | Currency | Global |  |  |
| `ReportedAdminFeePercentageAmountNet` | Reported Admin Fee Percentage Amount | Currency | Global |  |  |
| `ReportedAdministrationFeesGross` | Reported Administration Fees | Currency | Global |  |  |
| `ReportedAdministrationFeesNet` | Reported Administration Fees | Currency | Global |  |  |
| `ReportedCapAmountNoZeroDef` | Reported Cap Amount | Currency | Global |  |  |
| `ReportedControllableExpensesGross` | Reported Controllable Expenses | Currency | Global |  |  |
| `ReportedControllableExpensesNet` | Reported Controllable Expenses | Currency | Global |  |  |
| `ReportedDeductionsGross` | Reported Deductions | Currency | Global |  |  |
| `ReportedDeductionsNet` | Reported Deductions | Currency | Global |  |  |
| `ReportedNetAmountDueGross` | Reported Net Amount Due (NPT-PP) | Currency | Global |  |  |
| `ReportedNetAmountDueNet` | Reported Net Amount Due (NPT-PP) | Currency | Global |  |  |
| `ReportedNetPassThroughCOREFirmOnlyGross` | Reported Net Pass-Through (ST2*PRR) Duplicate | Currency | Global |  |  |
| `ReportedNetPassThroughCOREFirmOnlyNet` | Reported Net Pass-Through (ST2*PRR) Duplicate | Currency | Global |  |  |
| `ReportedNetPassThroughGross` | Reported Net Pass-Through (ST2*PRR) | Currency | Global |  |  |
| `ReportedNetPassThroughNet` | Reported Net Pass-Through (ST2*PRR) | Currency | Global |  |  |
| `ReportedNonControllableExpensesGross` | Reported Non-Controllable Expenses | Currency | Global |  |  |
| `ReportedNonControllableExpensesNet` | Reported Non-Controllable Expenses | Currency | Global |  |  |
| `ReportedPassThroughGross` | Reported Pass-Through (ST1+AF%+AF+A) | Currency | Global |  |  |
| `ReportedPassThroughNet` | Reported Pass-Through (ST1+AF%+AF+A) | Currency | Global |  |  |
| `ReportedPrePaidAmount` | Reported Pre Paid Amount | Currency | Global |  |  |
| `ReportedRecoveriesGross` | Reported Recoveries | Currency | Global |  |  |
| `ReportedRecoveriesNet` | Reported Recoveries | Currency | Global |  |  |
| `ReportedRevisedNetAmountDueGross` | Reported Revised Amount Due (Net+Adj) | Currency | Global |  |  |
| `ReportedRevisedNetAmountDueNet` | Reported Revised Amount Due (Net+Adj) | Currency | Global |  |  |
| `ReportedSubTotal1Gross` | Reported Sub Total #1 (C+NC-D) | Currency | Global |  |  |
| `ReportedSubTotal1Net` | Reported Sub Total #1 (C+NC-D) | Currency | Global |  |  |
| `ReportedSubTotal2Gross` | Reported Sub Total #2 (PT-R) | Currency | Global |  |  |
| `ReportedSubTotal2Net` | Reported Sub Total #2 (PT-R) | Currency | Global |  |  |
| `TenantSavingsAmount` | Tenant Savings Amount | Currency | Global |  |  |

### Rates & percentages (148)

Percentage inputs and computed rates.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ABVarianceAdminFeePercentageGross` | A-B Variance - Admin Fee Percentage | Percentage | Global |  |  |
| `ABVarianceAdminFeePercentageNet` | A-B Variance - Admin Fee Percentage | Percentage | Global |  |  |
| `ABVarianceProRataShareRateGross` | A-B Variance - Pro Rata Share Rate | Percentage | Global |  |  |
| `ABVarianceProRataShareRateNet` | A-B Variance - Pro Rata Share Rate | Percentage | Global |  |  |
| `APVarianceAdminFeePercentageGross` | A-P Variance - Admin Fee Percentage | Percentage | Global |  |  |
| `APVarianceAdminFeePercentageNet` | A-P Variance - Admin Fee Percentage | Percentage | Global |  |  |
| `APVariancePctAdditionsGross` | A-P Variance % - Additions | Percentage | Global |  |  |
| `APVariancePctAdditionsNet` | A-P Variance % - Additions | Percentage | Global |  |  |
| `APVariancePctAdminFeePercentageAmountGross` | A-P Variance % - Admin Fee Percentage Amount | Percentage | Global |  |  |
| `APVariancePctAdminFeePercentageAmountNet` | A-P Variance % - Admin Fee Percentage Amount | Percentage | Global |  |  |
| `APVariancePctAdminFeePercentageGross` | A-P Variance % - Admin Fee Percentage | Percentage | Global |  |  |
| `APVariancePctAdminFeePercentageNet` | A-P Variance % - Admin Fee Percentage | Percentage | Global |  |  |
| `APVariancePctAdministrationFeesGross` | A-P Variance % - Administration Fees | Percentage | Global |  |  |
| `APVariancePctAdministrationFeesNet` | A-P Variance % - Administration Fees | Percentage | Global |  |  |
| `APVariancePctCapAmountGross` | A-P Variance % - Cap Amount | Percentage | Global |  |  |
| `APVariancePctCapAmountNet` | A-P Variance % - Cap Amount | Percentage | Global |  |  |
| `APVariancePctControllableExpensesGross` | A-P Variance % - Controllable Expenses | Percentage | Global |  |  |
| `APVariancePctControllableExpensesNet` | A-P Variance % - Controllable Expenses | Percentage | Global |  |  |
| `APVariancePctDeductionsGross` | A-P Variance % - Deductions | Percentage | Global |  |  |
| `APVariancePctDeductionsNet` | A-P Variance % - Deductions | Percentage | Global |  |  |
| `APVariancePctGLAGross` | A-P Variance % - GLA | Percentage | Global |  |  |
| `APVariancePctGLANet` | A-P Variance % - GLA | Percentage | Global |  |  |
| `APVariancePctNetAmountDueGross` | A-P Variance % - Net Amount Due (NPT-PP) | Percentage | Global |  |  |
| `APVariancePctNetAmountDueNet` | A-P Variance % - Net Amount Due (NPT-PP) | Percentage | Global |  |  |
| `APVariancePctNetPassThroughGross` | A-P Variance % - Net Pass-Through (ST2*PRR) | Percentage | Global |  |  |
| `APVariancePctNetPassThroughNet` | A-P Variance % - Net Pass-Through (ST2*PRR) | Percentage | Global |  |  |
| `APVariancePctNonControllableExpensesGross` | A-P Variance % - Non-Controllable Expenses | Percentage | Global |  |  |
| `APVariancePctNonControllableExpensesNet` | A-P Variance % - Non-Controllable Expenses | Percentage | Global |  |  |
| `APVariancePctPassThroughGross` | A-P Variance % - Pass-Through (ST1+AF%+AF+A) | Percentage | Global |  |  |
| `APVariancePctPassThroughNet` | A-P Variance % - Pass-Through (ST1+AF%+AF+A) | Percentage | Global |  |  |
| `APVariancePctPrePaidAmountGross` | A-P Variance % - Pre Paid Amount | Percentage | Global |  |  |
| `APVariancePctPrePaidAmountNet` | A-P Variance % - Pre Paid Amount | Percentage | Global |  |  |
| `APVariancePctProRataShareRateGross` | A-P Variance % - Pro Rata Share Rate | Percentage | Global |  |  |
| `APVariancePctProRataShareRateNet` | A-P Variance % - Pro Rata Share Rate | Percentage | Global |  |  |
| `APVariancePctRecoveriesGross` | A-P Variance % - Recoveries | Percentage | Global |  |  |
| `APVariancePctRecoveriesNet` | A-P Variance % - Recoveries | Percentage | Global |  |  |
| `APVariancePctRentableAreaGross` | A-P Variance % - Rentable Area | Percentage | Global |  |  |
| `APVariancePctRentableAreaNet` | A-P Variance % - Rentable Area | Percentage | Global |  |  |
| `APVariancePctSubTotal1Gross` | A-P Variance % - Sub Total #1 (C+NC-D) | Percentage | Global |  |  |
| `APVariancePctSubTotal1Net` | A-P Variance % - Sub Total #1 (C+NC-D) | Percentage | Global |  |  |
| `APVarianceProRataShareRateGross` | A-P Variance - Pro Rata Share Rate | Percentage | Global |  |  |
| `APVarianceProRataShareRateNet` | A-P Variance - Pro Rata Share Rate | Percentage | Global |  |  |
| `ApprovedAdminFeePercentage` | Approved Admin Fee Percentage | Percentage | Global |  |  |
| `ApprovedProRataShareRate` | Approved Pro Rata Share Rate | Percentage | Global |  |  |
| `BPVarianceAdminFeePercentageGross` | B-P Variance - Admin Fee Percentage | Percentage | Global |  |  |
| `BPVarianceAdminFeePercentageNet` | B-P Variance - Admin Fee Percentage | Percentage | Global |  |  |
| `BPVariancePctAdditionsGross` | B-P Variance % - Additions | Percentage | Global |  |  |
| `BPVariancePctAdditionsNet` | B-P Variance % - Additions | Percentage | Global |  |  |
| `BPVariancePctAdminFeePercentageAmountGross` | B-P Variance % - Admin Fee Percentage Amount | Percentage | Global |  |  |
| `BPVariancePctAdminFeePercentageAmountNet` | B-P Variance % - Admin Fee Percentage Amount | Percentage | Global |  |  |
| `BPVariancePctAdminFeePercentageGross` | B-P Variance% - Admin Fee Percentage | Percentage | Global |  |  |
| `BPVariancePctAdminFeePercentageNet` | B-P Variance% - Admin Fee Percentage | Percentage | Global |  |  |
| `BPVariancePctAdministrationFeesGross` | B-P Variance % - Administration Fees | Percentage | Global |  |  |
| `BPVariancePctAdministrationFeesNet` | B-P Variance % - Administration Fees | Percentage | Global |  |  |
| `BPVariancePctCapAmountGross` | B-P Variance % - Cap Amount | Percentage | Global |  |  |
| `BPVariancePctCapAmountNet` | B-P Variance % - Cap Amount | Percentage | Global |  |  |
| `BPVariancePctControllableExpensesGross` | B-P Variance % - Controllable Expenses | Percentage | Global |  |  |
| `BPVariancePctControllableExpensesNet` | B-P Variance % - Controllable Expenses | Percentage | Global |  |  |
| `BPVariancePctDeductionsGross` | B-P Variance % - Deductions | Percentage | Global |  |  |
| `BPVariancePctDeductionsNet` | B-P Variance % - Deductions | Percentage | Global |  |  |
| `BPVariancePctGLAGross` | B-P Variance % - GLA | Percentage | Global |  |  |
| `BPVariancePctGLANet` | B-P Variance % - GLA | Percentage | Global |  |  |
| `BPVariancePctNetAmountDueGross` | B-P Variance % - Net Amount Due (NPT-PP) | Percentage | Global |  |  |
| `BPVariancePctNetAmountDueNet` | B-P Variance % - Net Amount Due (NPT-PP) | Percentage | Global |  |  |
| `BPVariancePctNetPassThroughGross` | B-P Variance % - Net Pass-Through (ST2*PRR) | Percentage | Global |  |  |
| `BPVariancePctNetPassThroughNet` | B-P Variance % - Net Pass-Through (ST2*PRR) | Percentage | Global |  |  |
| `BPVariancePctNonControllableExpensesGross` | B-P Variance % - Non-Controllable Expenses | Percentage | Global |  |  |
| `BPVariancePctNonControllableExpensesNet` | B-P Variance % - Non-Controllable Expenses | Percentage | Global |  |  |
| `BPVariancePctPassThroughGross` | B-P Variance % - Pass-Through (ST1+AF%+AF+A) | Percentage | Global |  |  |
| `BPVariancePctPassThroughNet` | B-P Variance % - Pass-Through (ST1+AF%+AF+A) | Percentage | Global |  |  |
| `BPVariancePctPrePaidAmountGross` | B-P Variance % - Pre Paid Amount | Percentage | Global |  |  |
| `BPVariancePctPrePaidAmountNet` | B-P Variance % - Pre Paid Amount | Percentage | Global |  |  |
| `BPVariancePctProRataShareRateGross` | B-P Variance % - Pro Rata Share Rate | Percentage | Global |  |  |
| `BPVariancePctProRataShareRateNet` | B-P Variance % - Pro Rata Share Rate | Percentage | Global |  |  |
| `BPVariancePctRecoveriesGross` | B-P Variance % - Recoveries | Percentage | Global |  |  |
| `BPVariancePctRecoveriesNet` | B-P Variance % - Recoveries | Percentage | Global |  |  |
| `BPVariancePctRentableAreaGross` | B-P Variance % - Rentable Area | Percentage | Global |  |  |
| `BPVariancePctRentableAreaNet` | B-P Variance % - Rentable Area | Percentage | Global |  |  |
| `BPVariancePctSubTotal1Gross` | B-P Variance % - Sub Total #1 (C+NC-D) | Percentage | Global |  |  |
| `BPVariancePctSubTotal1Net` | B-P Variance % - Sub Total #1 (C+NC-D) | Percentage | Global |  |  |
| `BPVariancePctSubTotal2Gross` | B-P Variance % - Sub Total #2 (PT-R) | Percentage | Global |  |  |
| `BPVariancePctSubTotal2Net` | B-P Variance % - Sub Total #2 (PT-R) | Percentage | Global |  |  |
| `BPVarianceProRataShareRateGross` | B-P Variance - Pro Rata Share Rate | Percentage | Global |  |  |
| `BPVarianceProRataShareRateNet` | B-P Variance - Pro Rata Share Rate | Percentage | Global |  |  |
| `BudgetedAdminFeePercentage` | Budgeted Admin Fee Percentage | Percentage | Global |  |  |
| `BudgetedProRataShareRate` | Budgeted Pro Rata Share Rate | Percentage | Global |  |  |
| `CapAmountChangePercent` | Cap Amount Per-Period Change (Percent) | Percentage | Global |  |  |
| `CapPercentage` | Cap Percentage | Percentage | Global |  |  |
| `EscalationPercentage` | Escalation Percentage | Percentage | Global |  |  |
| `OccupancyAdjustedThreshold` | Occupancy Factor | Percentage | Global |  |  |
| `PriorApprovedAdminFeePercentageGross` | Prior Approved Admin Fee Percentage | Percentage | Global |  |  |
| `PriorApprovedAdminFeePercentageNet` | Prior Approved Admin Fee Percentage | Percentage | Global |  |  |
| `PriorApprovedProRataShareRateGross` | Prior Approved Pro Rata Share Rate | Percentage | Global |  |  |
| `PriorApprovedProRataShareRateNet` | Prior Approved Pro Rata Share Rate | Percentage | Global |  |  |
| `PriorBudgetedAdminFeePercentageGross` | Prior Budgeted Admin Fee Percentage | Percentage | Global |  |  |
| `PriorBudgetedAdminFeePercentageNet` | Prior Budgeted Admin Fee Percentage | Percentage | Global |  |  |
| `PriorBudgetedProRataShareRateGross` | Prior Budgeted Pro Rata Share Rate | Percentage | Global |  |  |
| `PriorBudgetedProRataShareRateNet` | Prior Budgeted Pro Rata Share Rate | Percentage | Global |  |  |
| `PriorReportedAdminFeePercentageGross` | Prior Reported Admin Fee Percentage | Percentage | Global |  |  |
| `PriorReportedAdminFeePercentageNet` | Prior Reported Admin Fee Percentage | Percentage | Global |  |  |
| `PriorReportedProRataShareRateGross` | Prior Reported Pro Rata Share Rate | Percentage | Global |  |  |
| `PriorReportedProRataShareRateNet` | Prior Reported Pro Rata Share Rate | Percentage | Global |  |  |
| `RAVarianceAdminFeePercentageGross` | R-A Variance - Admin Fee Percentage | Percentage | Global |  |  |
| `RAVarianceAdminFeePercentageNet` | R-A Variance - Admin Fee Percentage | Percentage | Global |  |  |
| `RAVarianceProRataShareRateGross` | R-A Variance - Pro Rata Share Rate | Percentage | Global |  |  |
| `RAVarianceProRataShareRateNet` | R-A Variance - Pro Rata Share Rate | Percentage | Global |  |  |
| `RPVarianceAdminFeePercentageGross` | R-P Variance - Admin Fee Percentage | Percentage | Global |  |  |
| `RPVarianceAdminFeePercentageNet` | R-P Variance - Admin Fee Percentage | Percentage | Global |  |  |
| `RPVariancePctAdditionsGross` | R-P Variance % - Additions | Percentage | Global |  |  |
| `RPVariancePctAdditionsNet` | R-P Variance % - Additions | Percentage | Global |  |  |
| `RPVariancePctAdminFeePercentageAmountGross` | R-P Variance % - Admin Fee Percentage Amount | Percentage | Global |  |  |
| `RPVariancePctAdminFeePercentageAmountNet` | R-P Variance % - Admin Fee Percentage Amount | Percentage | Global |  |  |
| `RPVariancePctAdminFeePercentageGross` | R-P Variance % - Admin Fee Percentage | Percentage | Global |  |  |
| `RPVariancePctAdminFeePercentageNet` | R-P Variance % - Admin Fee Percentage | Percentage | Global |  |  |
| `RPVariancePctAdministrationFeesGross` | R-P Variance % - Administration Fees | Percentage | Global |  |  |
| `RPVariancePctAdministrationFeesNet` | R-P Variance % - Administration Fees | Percentage | Global |  |  |
| `RPVariancePctCapAmountGross` | R-P Variance % - Cap Amount | Percentage | Global |  |  |
| `RPVariancePctCapAmountNet` | R-P Variance % - Cap Amount | Percentage | Global |  |  |
| `RPVariancePctControllableExpensesGross` | R-P Variance % - Controllable Expenses | Percentage | Global |  |  |
| `RPVariancePctControllableExpensesNet` | R-P Variance % - Controllable Expenses | Percentage | Global |  |  |
| `RPVariancePctDeductionsGross` | R-P Variance % - Deductions | Percentage | Global |  |  |
| `RPVariancePctDeductionsNet` | R-P Variance % - Deductions | Percentage | Global |  |  |
| `RPVariancePctGLAGross` | R-P Variance % - GLA | Percentage | Global |  |  |
| `RPVariancePctGLANet` | R-P Variance % - GLA | Percentage | Global |  |  |
| `RPVariancePctNetAmountDueGross` | R-P Variance % - Net Amount Due (NPT-PP) | Percentage | Global |  |  |
| `RPVariancePctNetAmountDueNet` | R-P Variance % - Net Amount Due (NPT-PP) | Percentage | Global |  |  |
| `RPVariancePctNetPassThroughGross` | R-P Variance % - Net Pass-Through (ST2*PRR) | Percentage | Global |  |  |
| `RPVariancePctNetPassThroughNet` | R-P Variance % - Net Pass-Through (ST2*PRR) | Percentage | Global |  |  |
| `RPVariancePctNonControllableExpensesGross` | R-P Variance % - Non-Controllable Expenses | Percentage | Global |  |  |
| `RPVariancePctNonControllableExpensesNet` | R-P Variance % - Non-Controllable Expenses | Percentage | Global |  |  |
| `RPVariancePctPassThroughGross` | R-P Variance % - Pass-Through (ST1+AF%+AF+A) | Percentage | Global |  |  |
| `RPVariancePctPassThroughNet` | R-P Variance % - Pass-Through (ST1+AF%+AF+A) | Percentage | Global |  |  |
| `RPVariancePctPrePaidAmountGross` | R-P Variance % - Pre Paid Amount | Percentage | Global |  |  |
| `RPVariancePctPrePaidAmountNet` | R-P Variance % - Pre Paid Amount | Percentage | Global |  |  |
| `RPVariancePctProRataShareRateGross` | R-P Variance % - Pro Rata Share Rate | Percentage | Global |  |  |
| `RPVariancePctProRataShareRateNet` | R-P Variance % - Pro Rata Share Rate | Percentage | Global |  |  |
| `RPVariancePctRecoveriesGross` | R-P Variance % - Recoveries | Percentage | Global |  |  |
| `RPVariancePctRecoveriesNet` | R-P Variance % - Recoveries | Percentage | Global |  |  |
| `RPVariancePctRentableAreaGross` | R-P Variance % - Rentable Area | Percentage | Global |  |  |
| `RPVariancePctRentableAreaNet` | R-P Variance % - Rentable Area | Percentage | Global |  |  |
| `RPVariancePctSubTotal1Gross` | R-P Variance % - Sub Total #1 (C+NC-D) | Percentage | Global |  |  |
| `RPVariancePctSubTotal1Net` | R-P Variance % - Sub Total #1 (C+NC-D) | Percentage | Global |  |  |
| `RPVariancePctSubTotal2Gross` | R-P Variance % - Sub Total #2 (PT-R) | Percentage | Global |  |  |
| `RPVariancePctSubTotal2Net` | R-P Variance % - Sub Total #2 (PT-R) | Percentage | Global |  |  |
| `RPVarianceProRataShareRateGross` | R-P Variance - Pro Rata Share Rate | Percentage | Global |  |  |
| `RPVarianceProRataShareRateNet` | R-P Variance - Pro Rata Share Rate | Percentage | Global |  |  |
| `ReportedAdminFeePercentage` | Reported Admin Fee Percentage | Percentage | Global |  |  |
| `ReportedProRataShareRate` | Reported Pro Rata Share Rate | Percentage | Global |  |  |

### Quantities (45)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ABVarianceGLAGross` | A-B Variance - GLA | Number | Global |  |  |
| `ABVarianceGLANet` | A-B Variance - GLA | Number | Global |  |  |
| `ABVarianceRentableAreaGross` | A-B Variance - Rentable Area | Number | Global |  |  |
| `ABVarianceRentableAreaNet` | A-B Variance - Rentable Area | Number | Global |  |  |
| `APVarianceGLAGross` | A-P Variance - GLA | Number | Global |  |  |
| `APVarianceGLANet` | A-P Variance - GLA | Number | Global |  |  |
| `APVarianceRentableAreaGross` | A-P Variance - Rentable Area | Number | Global |  |  |
| `APVarianceRentableAreaNet` | A-P Variance - Rentable Area | Number | Global |  |  |
| `ApprovedGLA` | Approved GLA | Number | Global |  |  |
| `ApprovedRentableArea` | Approved Rentable Area | Number | Global |  |  |
| `BPVarianceGLAGross` | B-P Variance - GLA | Number | Global |  |  |
| `BPVarianceGLANet` | B-P Variance - GLA | Number | Global |  |  |
| `BPVarianceRentableAreaGross` | B-P Variance - Rentable Area | Number | Global |  |  |
| `BPVarianceRentableAreaNet` | B-P Variance - Rentable Area | Number | Global |  |  |
| `BudgetedGLA` | Budgeted GLA | Number | Global |  |  |
| `BudgetedRentableArea` | Budgeted Rentable Area | Number | Global |  |  |
| `CatchUpNumberOfMonths` | Catch Up Number of Months | 2-Digit Number | Global |  |  |
| `ExpenseRecoveryID` | Expense Recovery RecID | Number | Global |  |  |
| `ExpenseRecoveryID` | Expense Recovery RecID | Number | Global |  |  |
| `ExpenseRecoveryID` | Expense Recovery RecID | Number | Global |  |  |
| `ExpenseRecoveryID` | Expense Recovery RecID | Number | Global |  |  |
| `NumDaysInRecoveryPeriod` | Number of Days In Period | Number | Global |  |  |
| `PriorApprovedGLAGross` | Prior Approved GLA | Number | Global |  |  |
| `PriorApprovedGLANet` | Prior Approved GLA | Number | Global |  |  |
| `PriorApprovedRentableAreaGross` | Prior Approved Rentable Area | Number | Global |  |  |
| `PriorApprovedRentableAreaNet` | Prior Approved Rentable Area | Number | Global |  |  |
| `PriorBudgetedGLAGross` | Prior Budgeted GLA | Number | Global |  |  |
| `PriorBudgetedGLANet` | Prior Budgeted GLA | Number | Global |  |  |
| `PriorBudgetedRentableAreaGross` | Prior Budgeted Rentable Area | Number | Global |  |  |
| `PriorBudgetedRentableAreaNet` | Prior Budgeted Rentable Area | Number | Global |  |  |
| `PriorReportedGLAGross` | Prior Reported GLA | Number | Global |  |  |
| `PriorReportedGLANet` | Prior Reported GLA | Number | Global |  |  |
| `PriorReportedRentableAreaGross` | Prior Reported Rentable Area | Number | Global |  |  |
| `PriorReportedRentableAreaNet` | Prior Reported Rentable Area | Number | Global |  |  |
| `RAVarianceGLAGross` | R-A Variance - GLA | Number | Global |  |  |
| `RAVarianceGLANet` | R-A Variance - GLA | Number | Global |  |  |
| `RAVarianceRentableAreaGross` | R-A Variance - Rentable Area | Number | Global |  |  |
| `RAVarianceRentableAreaNet` | R-A Variance - Rentable Area | Number | Global |  |  |
| `RPVarianceGLAGross` | R-P Variance - GLA | Number | Global |  |  |
| `RPVarianceGLANet` | R-P Variance - GLA | Number | Global |  |  |
| `RPVarianceRentableAreaGross` | R-P Variance - Rentable Area | Number | Global |  |  |
| `RPVarianceRentableAreaNet` | R-P Variance - Rentable Area | Number | Global |  |  |
| `RecoveryPeriodDaysNoZeroDef` | Recovery Period Days | Number | Global |  |  |
| `ReportedGLA` | Reported GLA | Number | Global |  |  |
| `ReportedRentableArea` | Reported Rentable Area | Number | Global |  |  |

### Dates & timestamps (5)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BeginDate` | Begin Date | Date | Global |  |  |
| `DateReceived` | Date Received | Date | Global |  |  |
| `EndDate` | End Date | Date | Global |  |  |
| `ReconciledDate` | Reconciled Date | Date | Global |  |  |
| `TenantDueDate` | Tenant Due Date | Date | Global |  |  |

### Flags (2)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `IsRecoveryCapEscalationNonCum` | Is Escalation Non-Cumulative | Boolean | Global |  |  |
| `ReconciledFlag` | Reconciled? | Boolean | Global |  |  |

### Text & notes (5)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BaseYear` | Base Year | Text | Global |  |  |
| `Notes` |  | Text | Global |  |  |
| `RecoveryExclusions` | Recovery Exclusions | Text | Global |  |  |
| `RecoveryPeriod` | Recovery Period | Text | Global |  |  |
| `Section` |  | Text | Global |  |  |

### Audit & record keeping (9)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Expense Recovery ClientID | Text | Global | yes |  |
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` | Rev Number | Number | Global |  |  |
