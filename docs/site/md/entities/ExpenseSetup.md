# ExpenseSetup

*96 fields · module: Lease Accounting & Payments · Postgres: `expense_setup`*

The recurring-expense billing configuration for a contract (insurance, taxes, CAM billed directly rather than through recovery) — coverage period begin markers for every possible billing frequency (Annual, Q1-Q4, both Semi-Annual halves) so the same setup record can support annual, quarterly, or semi-annual billing without changing schema. 105 fields split 103 Global / 2 Firm, and it appears under both the Contract group and the Wizard group — meaning this configuration also drives a guided lease-setup wizard flow, not just the standing contract record.

Source: `data-fields/expense-setup.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 96 |
| Catalogued fields | 105 (103 global, 2 firm) |
| Physical tables | 1 |
| Referenced by | 10 keys from 10 record types |
| Points at | 6 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 14 |

## What to know before rebuilding this

### 2 tenant custom columns

**Observed.** This record carries 2 physical Firm_-prefixed columns — tenant custom fields are real columns, not rows in a value store, so adding one is a DDL change. That is direct evidence for database-per-tenant and against a shared schema.

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### 2 catalogued Firm-scope fields

**Observed.** Of 105 catalogued fields on this record, 2 are Firm scope — defined by this tenant rather than shipped by the platform. Firm-scope definitions are RGAF rows carrying IsGlobal, FirmID and IsClientExtensionField.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [ACC-R-021](../rules/ACC-R-021.md) | the accounting schedule associated with that expense type is dirtied | Observed |
| [ACC-R-025](../rules/ACC-R-025.md) | each period cash flow is routed to the schedule type its expense type designates for the standard being generated | Derived |
| [CON-R-008](../rules/CON-R-008.md) | Generation is requested: both ExpenseSetup.ReadyForPaymentFlag and ExpenseSchedule.ReadyForPaymentFlag must be true for the row to generate — the fields are observed, the exact gate semantics are inferred. | Observed |
| [CON-R-019](../rules/CON-R-019.md) | Determining payable vs receivable: direction is carried on ExpenseSetup.IsReceivable and PaymentTransaction.IsReceivable, not on the contract, so one contract can be both. | Observed |
| [CON-R-020](../rules/CON-R-020.md) | Resolving a contract's vendors: Contract has no vendor FK; the set is derived from PaymentTransaction.VendorID, ExpenseSetup.VendorID, ExpenseVendorAllocation.VendorID, ScheduledOffset.VendorID, LandlordInvoice.EmployerID and SecurityDeposi | Derived |
| [CON-R-030](../rules/CON-R-030.md) | Authoring a recurring expense through the wizard: the wizard's start date, end date, starting amount, amount type and escalation settings materialise ExpenseSetup + ExpenseEscalation + the full ExpenseSchedule in one action. | Observed |
| [CON-R-032](../rules/CON-R-032.md) | Determining billing frequency: CodeFrequencyID, NumberOfPayments and PaymentDueDay drive the number and spacing of ExpenseSchedule rows. | Derived |
| [CON-R-037](../rules/CON-R-037.md) | CalculateScheduleAmounts is invoked: the schedule's amounts are recomputed in place from the clause, its escalation and its tax configuration. | Observed |
| [CON-R-043](../rules/CON-R-043.md) | An index change is applied: applied = rawChange × ExpenseSetup.CPIMultiplier. | Inferred |
| [CON-R-045](../rules/CON-R-045.md) | ExpenseSetup.IsCPICompounding is set: true escalates from the current amount; false escalates from BaseAmount. | Derived |
| [CON-R-049](../rules/CON-R-049.md) | Increase/decrease asymmetry: ExpenseSetup.AmountIncreaseCap/AmountDecreaseCap/PercentIncreaseCap/PercentDecreaseCap are a separate, parallel collar to ExpenseEscalation's own min/max, with unspecified precedence between the two. | Observed |
| [CON-R-125](../rules/CON-R-125.md) | Any generation or posting: HoldFlag on ExpenseSetup, ExpenseSchedule, ExpenseAccrualSetup, PaymentTransaction or AccrualTransaction is a negative gate at every layer. | Observed |
| [CON-R-126](../rules/CON-R-126.md) | Any generation: ReadyForPaymentFlag on ExpenseSetup and ExpenseSchedule is a positive gate — both must be true. | Observed |
| [CON-R-127](../rules/CON-R-127.md) | Forecast inclusion: only ExpenseSetup rows flagged IncludeInPlanForecast appear in VirtualExpenseForecastPeriod. | Observed |

## Fields

### Relationships (foreign keys) (5)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AmendmentID` | Amendment | Contract Amendment ID | Global |  | [ContractAmendment](ContractAmendment.md) |
| `ContractID` | Contract | Contract ID | Global | yes | [Contract](Contract.md) |
| `CovenantID` | Covenant | Covenant ID | Global |  | [Covenant](Covenant.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |
| `VendorID` | Vendor | Employer ID | Global |  | [Employer](Employer.md) |

### Coded values (drop-downs) (12)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeBuildingAreaUnitID` | Building Area Unit | Dropdown (Building Area Unit Code) | Global |  | Building Area Unit Code |
| `CodeCPIIndexID` | CPI Index | Dropdown (CPI Index Code) | Global |  | CPI Index Code |
| `CodeCurrencyTypeID` | Currency Type | Dropdown (Currency Type Code) | Global |  | Currency Type Code |
| `CodeExpenseAcctID` | Expense Acct | Dropdown (Expense Acct Code) | Global |  | Expense Acct Code |
| `CodeExpenseCategoryID` | Expense Category | Dropdown (Expense Category Code) | Global |  | Expense Category Code |
| `CodeExpenseGroupID` | Expense Group | Dropdown (Expense Group Code) | Global |  | Expense Group Code |
| `CodeExpenseTypeID` | Expense Type | Dropdown (Expense Type Code) | Global |  | Expense Type Code |
| `CodeFrequencyID` | Frequency | Dropdown (Frequency Code) | Global | yes | Frequency Code |
| `CodePaymentMethodID` | Payment Method | Dropdown (Payment Method Code) | Global |  | Payment Method Code |
| `CodePlanForecastBasedOnID` | Plan/Forecast Based On | Dropdown (Plan Forecast Based On Code) | Global |  | Plan Forecast Based On Code |
| `CodePlanForecastGroupID` | Plan/Forecast Group | Dropdown (Plan Forecast Group Code) | Global |  | Plan Forecast Group Code |
| `CodeProrationMethodID` | Proration Method | Dropdown (Proration Method Code) | Global |  | Proration Method Code |

### Money (17)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AmountDecreaseCap` | Amount Decrease Cap | Currency | Global |  |  |
| `AmountIncreaseCap` | Amount Increase Cap | Currency | Global |  |  |
| `CurrentAnnualRent` | Current Annual Rent | Currency | Global |  |  |
| `CurrentMonthlyRent` | Current Monthly Rent | Currency | Global |  |  |
| `CurrentPeriodRent` | Current Period Rent | Currency | Global |  |  |
| `CurrentPeriodTaxAmount1` | Current Period Tax Amount #1 | Currency | Global |  |  |
| `CurrentPeriodTaxAmount2` | Current Period Tax Amount #2 | Currency | Global |  |  |
| `CurrentPeriodTaxAmount3` | Current Period Tax Amount #3 | Currency | Global |  |  |
| `CurrentPeriodTaxAmount4` | Current Period Tax Amount #4 | Currency | Global |  |  |
| `CurrentTaxAmount1` | Current Monthly Tax Amount #1 | Currency | Global |  |  |
| `CurrentTaxAmount2` | Current Monthly Tax Amount #2 | Currency | Global |  |  |
| `CurrentTaxAmount3` | Current Monthly Tax Amount #3 | Currency | Global |  |  |
| `CurrentTaxAmount4` | Current Monthly Tax Amount #4 | Currency | Global |  |  |
| `Firm_TotalCurrentMonthlyRent` | Total Current Monthly Rent | Currency | Firm |  |  |
| `ForecastAdjustment` | Forecast Adjustment | Currency | Global |  |  |
| `PlanAdjustment` | Plan Adjustment | Currency | Global |  |  |
| `SecondaryRentSchedAllocAmount` | Secondary Rent Schedule Allocation Amount | Currency | Global |  |  |

### Rates & percentages (9)

Percentage inputs and computed rates.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ForecastCapPercent` | Forecast Cap Percent | Percentage | Global |  |  |
| `ForecastGrowthPercent` | Forecast Growth Percent | Percentage | Global |  |  |
| `PaymentRate` | Payment Rate | Percentage | Global |  |  |
| `PercentDecreaseCap` | Percent Decrease Cap | Percentage | Global |  |  |
| `PercentIncreaseCap` | Percent Increase Cap | Percentage | Global |  |  |
| `PlanCapPercent` | Plan Cap Percent | Percentage | Global |  |  |
| `PlanGrowthPercent` | Plan Growth Percent | Percentage | Global |  |  |
| `ProRataShareRate` | Pro Rata Share Rate | Percentage | Global |  |  |
| `SecondaryRentSchedAllocPercent` | Secondary Rent Schedule Allocation Percent | Percentage | Global |  |  |

### Quantities (5)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CPIMultiplier` | CPI Multiplier | Number | Global |  |  |
| `ExpenseSetupID` | Expense Setup RecID | Number | Global |  |  |
| `NumberOfPayments` | Number Of Payments | Number | Global |  |  |
| `PaymentDueDay` | Payment Due Day | Number | Global |  |  |
| `RentableArea` | Rentable Area | Number | Global |  |  |

### Dates & timestamps (18)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BeginDate` | Begin Date | Date | Global |  |  |
| `CoverageBeginAnnual` | Coverage Begin Annual | Date | Global |  |  |
| `CoverageBeginQ1` | Coverage Begin Q1 | Date | Global |  |  |
| `CoverageBeginQ2` | Coverage Begin Q2 | Date | Global |  |  |
| `CoverageBeginQ3` | Coverage Begin Q3 | Date | Global |  |  |
| `CoverageBeginQ4` | Coverage Begin Q4 | Date | Global |  |  |
| `CoverageBeginSemiAnnual1` | Coverage Begin Semi Annual 1 | Date | Global |  |  |
| `CoverageBeginSemiAnnual2` | Coverage Begin Semi Annual 2 | Date | Global |  |  |
| `EndDate` | End Date | Date | Global |  |  |
| `FirstPaymentDueDate` | First Payment Due Date | Date | Global |  |  |
| `LastPaymentDueDate` | Last Payment Due Date | Date | Global |  |  |
| `PaymentDueAnnual` | Payment Due Annual | Date | Global |  |  |
| `PaymentDueQ1` | Payment Due Q1 | Date | Global |  |  |
| `PaymentDueQ2` | Payment Due Q2 | Date | Global |  |  |
| `PaymentDueQ3` | Payment Due Q3 | Date | Global |  |  |
| `PaymentDueQ4` | Payment Due Q4 | Date | Global |  |  |
| `PaymentDueSemiAnnual1` | Payment Due Semi Annual 1 | Date | Global |  |  |
| `PaymentDueSemiAnnual2` | Payment Due Semi Annual 2 | Date | Global |  |  |

### Flags (15)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ApplyTax1Flag` | Apply Tax #1? | Boolean | Global |  |  |
| `ApplyTax2Flag` | Apply Tax #2? | Boolean | Global |  |  |
| `ApplyTax3Flag` | Apply Tax #3? | Boolean | Global |  |  |
| `ApplyTax4Flag` | Apply Tax #4? | Boolean | Global |  |  |
| `Firm_CPIIncrease` | CPI Increase | Boolean | Firm |  |  |
| `HoldFlag` | Hold? | Boolean | Global |  |  |
| `IncludeInPlanForecast` | Include in Planning and Forecasting | Boolean | Global |  |  |
| `IsCPICompounding` | Is CPI Compounding? | Boolean | Global |  |  |
| `IsCustomPaymentCoverage` | Custom Payment Coverage | Boolean | Global |  |  |
| `IsDailyRent` | Daily Rent | Boolean | Global |  |  |
| `IsPayArrears` | Pay in Arrears? | Boolean | Global |  |  |
| `IsReceivable` | Is Receivable? | Boolean | Global |  |  |
| `ReadyForPaymentFlag` | Ready For Payment? | Boolean | Global |  |  |
| `ReconcilableExpense` | Reconcilable Expense? | Boolean | Global |  |  |
| `TaxesIncludedFlag` | Taxes Included In Amount? | Boolean | Global |  |  |

### Text & notes (11)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BankAccountNumber` | Bank Account Number | Text | Global |  |  |
| `BankRoutingNumber` | Bank Routing Number | Text | Global |  |  |
| `CPINotes` | CPI Notes | Text | Global |  |  |
| `Description` |  | Text | Global |  |  |
| `InternalReferenceNumber` | Internal Reference Number | Text | Global |  |  |
| `Notes` |  | Text | Global |  |  |
| `PlanForecastNotes` | Planning and Forecasting Notes | Text | Global |  |  |
| `RemitMessage` | Remit Message | Text | Global |  |  |
| `Section` |  | Text | Global |  |  |
| `VendorAccountNumber` | Vendor Account Number | Text | Global |  |  |
| `VendorAllocationList` | Vendor Allocation List | Text | Global |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Expense Setup ClientID | Text | Global | yes |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |

### Other (1)

Everything that did not fall into a named group.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DateRange` | Date Range | Date Range | Global |  |  |

## What points here (10 keys)

| Record type | Via column |
|---|---|
| [AcctingAssumptionAdjust](AcctingAssumptionAdjust.md) | `ExpenseSetupID` |
| [AlternateRentSchedule](AlternateRentSchedule.md) | `ExpenseSetupID` |
| [ExpenseAccrualSetup](ExpenseAccrualSetup.md) | `ExpenseSetupID` |
| [ExpenseAllocation](ExpenseAllocation.md) | `ExpenseSetupID` |
| [ExpenseEscalation](ExpenseEscalation.md) | `ExpenseSetupID` |
| [ExpenseSchedule](ExpenseSchedule.md) | `ExpenseSetupID` |
| [ExpenseVendorAllocation](ExpenseVendorAllocation.md) | `ExpenseSetupID` |
| [PaymentTransaction](PaymentTransaction.md) | `ExpenseSetupID` |
| [PaymentTransactionFullImport](PaymentTransactionFullImport.md) | `ExpenseSetupID` |
| [VirtualExpenseForecastPeriod](VirtualExpenseForecastPeriod.md) | `ExpenseSetupID` |
