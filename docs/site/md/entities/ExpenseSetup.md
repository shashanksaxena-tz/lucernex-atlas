# ExpenseSetup

*96 fields · module: Lease Accounting & Payments · Postgres: `expense_setup`*

The recurring-expense billing configuration for a contract (insurance, taxes, CAM billed directly rather than through recovery) — coverage period begin markers for every possible billing frequency (Annual, Q1-Q4, both Semi-Annual halves) so the same setup record can support annual, quarterly, or semi-annual billing without changing schema. 105 fields split 103 Global / 2 Firm, and it appears under both the Contract group and the Wizard group — meaning this configuration also drives a guided lease-setup wizard flow, not just the standing contract record.

Source: `data-fields/expense-setup.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 96 |
| Fields with a vendor definition | 93 of 98 inventoried |
| Physical tables | `expense_setup` |
| Replication database | `lxr_drp_bbw` |
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

### Lands in expense_setup

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 93 fields carry a vendor definition

**Observed.** 93 of this record's 98 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one source in the corpus that explains fields rather than listing them.

### 2 fields marked required

**Observed.** The inventory marks 2 of this record's fields Required. Across the whole inventory that is 606 fields, which independently corroborates the 603 the corpus had derived from the Data Fields catalogue — two sources, arrived at separately, agreeing to within three.

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

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AmendmentID` | Amendment | Select the amendment that the record is associated with from this field. | Contract Amendment ID | Global |  | `expense_setup.AmendmentID · TEXT` | [ContractAmendment](ContractAmendment.md) |
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global | yes | `expense_setup.ContractID · TEXT` | [Contract](Contract.md) |
| `CovenantID` | Covenant | Select the covenant that the record is associated with from this field. | Covenant ID | Global |  | `expense_setup.CovenantID · TEXT` | [Covenant](Covenant.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `expense_setup.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |
| `VendorID` | Vendor | The vendor ID associated with the expense setup. The vendor ID is used in payment transactions created when you generate rent and retro payments. | Employer ID | Global |  | `expense_setup.VendorID · TEXT` | [Employer](Employer.md) |

### Coded values (drop-downs) (12)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeBuildingAreaUnitID` | Building Area Unit | Select the units you are using to measure your area from this field. This field should pre-populate with the area unit you selected when creating your contract. | Dropdown (Building Area Unit Code) | Global |  | `expense_setup.CodeBuildingAreaUnitID · TEXT` | Building Area Unit Code |
| `CodeCPIIndexID` | CPI Index | Select the CPI Index this expense setup should be associated with from this field. If this not a CPI-indexed expense, do not select a CPI Index. | Dropdown (CPI Index Code) | Global |  | `expense_setup.CodeCPIIndexID · TEXT` | CPI Index Code |
| `CodeCurrencyTypeID` | Currency Type | The Currency Type field allows you to select a currency type to be used on a record. | Dropdown (Currency Type Code) | Global |  | `expense_setup.CodeCurrencyTypeID · TEXT` | Currency Type Code |
| `CodeExpenseAcctID` | Expense Acct | This field is no longer in use. | Dropdown (Expense Acct Code) | Global |  | `expense_setup.CodeExpenseAcctID · TEXT` | Expense Acct Code |
| `CodeExpenseCategoryID` | Expense Category | The Expense Category field allows you to associate your record with a pre-configured expense category. Categories are the children of types, and the grandchildren of groups. | Dropdown (Expense Category Code) | Global |  | `expense_setup.CodeExpenseCategoryID · TEXT` | Expense Category Code |
| `CodeExpenseGroupID` | Expense Group | The Expense Group field allows you to associate your record with a pre-configured expense group. Expense groups are used to categorize expense types. | Dropdown (Expense Group Code) | Global |  | `expense_setup.CodeExpenseGroupID · TEXT` | Expense Group Code |
| `CodeExpenseTypeID` | Expense Type | The Expense Type field allows you to associate your record with a pre-configured expense type. Expense Types are used to associate records with lease accounting schedules, AP export numbers, expense accrual accounts, percentage rent accrual accounts, and real estate tax accounts. | Dropdown (Expense Type Code) | Global |  | `expense_setup.CodeExpenseTypeID · TEXT` | Expense Type Code |
| `CodeFrequencyID` | Frequency | Select the payment frequency from this field. This setting will tell the system how often payments for this expense setup should be generated. | Dropdown (Frequency Code) | Global | yes | `expense_setup.CodeFrequencyID · TEXT` | Frequency Code |
| `CodePaymentMethodID` | Payment Method | Select the payment method used for making payments for this expense setup. | Dropdown (Payment Method Code) | Global |  | `expense_setup.CodePaymentMethodID · TEXT` | Payment Method Code |
| `CodePlanForecastBasedOnID` | Plan/Forecast Based On | Select the calculation method for planning and forecasting from this field. You must select an option from this field if you are going to use the Expense Setup option when generating your accruals. See the Lx Online Help for definitions of the calculation methods. | Dropdown (Plan Forecast Based On Code) | Global |  | `expense_setup.CodePlanForecastBasedOnID · TEXT` | Plan Forecast Based On Code |
| `CodePlanForecastGroupID` | Plan/Forecast Group | Select the plan / forecast group this expense setup should be associated with from this field. | Dropdown (Plan Forecast Group Code) | Global |  | `expense_setup.CodePlanForecastGroupID · TEXT` | Plan Forecast Group Code |
| `CodeProrationMethodID` | Proration Method | Select the proration method you want to use for this expense setup from this field. For definitions of the provided options, please see the Lx Online Help. | Dropdown (Proration Method Code) | Global |  | `expense_setup.CodeProrationMethodID · TEXT` | Proration Method Code |

### Money (17)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AmountDecreaseCap` | Amount Decrease Cap | Enter your escalation floor amount in this field. | Currency | Global |  | `expense_setup.AmountDecreaseCap · TEXT` |  |
| `AmountIncreaseCap` | Amount Increase Cap | Enter your escalation ceiling amount in this field. This cap applies to both CPI and non-CPI escalations. | Currency | Global |  | `expense_setup.AmountIncreaseCap · TEXT` |  |
| `CurrentAnnualRent` | Current Annual Rent | The total current annual rent for this expense setup record based on the associated expense schedules, including asset expense schedules. This field ignores alternate rent schedules. | Currency | Global |  | `expense_setup.CurrentAnnualRent · TEXT` |  |
| `CurrentMonthlyRent` | Current Monthly Rent | The total current period rent for this expense setup record based on the associated expense schedules, including asset expense schedules. This field ignores alternate rent schedules. | Currency | Global |  | `expense_setup.CurrentMonthlyRent · TEXT` |  |
| `CurrentPeriodRent` | Current Period Rent | If you use a payment frequency other than monthly, this field displays the period amount. | Currency | Global |  | `expense_setup.CurrentPeriodRent · TEXT` |  |
| `CurrentPeriodTaxAmount1` | Current Period Tax Amount #1 | The current period's primary tax amount total. | Currency | Global |  | `expense_setup.CurrentPeriodTaxAmount1 · TEXT` |  |
| `CurrentPeriodTaxAmount2` | Current Period Tax Amount #2 | The current period's secondary tax amount total. | Currency | Global |  | `expense_setup.CurrentPeriodTaxAmount2 · TEXT` |  |
| `CurrentPeriodTaxAmount3` | Current Period Tax Amount #3 | The current period's third tax amount total. | Currency | Global |  | `expense_setup.CurrentPeriodTaxAmount3 · TEXT` |  |
| `CurrentPeriodTaxAmount4` | Current Period Tax Amount #4 | The current period's fourth tax amount total. | Currency | Global |  | `expense_setup.CurrentPeriodTaxAmount4 · TEXT` |  |
| `CurrentTaxAmount1` | Current Monthly Tax Amount #1 | The current primary tax amount total. | Currency | Global |  | `expense_setup.CurrentTaxAmount1 · TEXT` |  |
| `CurrentTaxAmount2` | Current Monthly Tax Amount #2 | The current secondary tax amount total. | Currency | Global |  | `expense_setup.CurrentTaxAmount2 · TEXT` |  |
| `CurrentTaxAmount3` | Current Monthly Tax Amount #3 | The current third tax amount total. | Currency | Global |  | `expense_setup.CurrentTaxAmount3 · TEXT` |  |
| `CurrentTaxAmount4` | Current Monthly Tax Amount #4 | The current fourth tax amount total. | Currency | Global |  | `expense_setup.CurrentTaxAmount4 · TEXT` |  |
| `Firm_TotalCurrentMonthlyRent` | Total Current Monthly Rent |  | Currency | Firm |  | `expense_setup.Firm_TotalCurrentMonthlyRent · TEXT` |  |
| `ForecastAdjustment` | Forecast Adjustment | Enter a monthly dollar amount that will be added to the new forecast amount. | Currency | Global |  | `expense_setup.ForecastAdjustment · TEXT` |  |
| `PlanAdjustment` | Plan Adjustment | Enter a monthly dollar amount that will be added to the new planned amount. | Currency | Global |  | `expense_setup.PlanAdjustment · TEXT` |  |
| `SecondaryRentSchedAllocAmount` | Secondary Rent Schedule Allocation Amount | If you will be allocating an amount of the expense to a secondary schedule, enter the amount you want to allocate in this field. | Currency | Global |  | `expense_setup.SecondaryRentSchedAllocAmount · TEXT` |  |

### Rates & percentages (9)

Percentage inputs and computed rates.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ForecastCapPercent` | Forecast Cap Percent | Enter the maximum growth percentage that can be applied to the forecast. If this value is populated it will override the growth percent where it is exceeds the cap. | Percentage | Global |  | `expense_setup.ForecastCapPercent · TEXT` |  |
| `ForecastGrowthPercent` | Forecast Growth Percent | Enter the percentage that will be used to calculate the forecast values. | Percentage | Global |  | `expense_setup.ForecastGrowthPercent · TEXT` |  |
| `PaymentRate` | Payment Rate | The value of this field equals the rentable area divided by the total annual rent. | Percentage | Global |  | `expense_setup.PaymentRate · TEXT` |  |
| `PercentDecreaseCap` | Percent Decrease Cap | This field is a placeholder in preparation for an upcoming enhancement. | Percentage | Global |  | `expense_setup.PercentDecreaseCap · TEXT` |  |
| `PercentIncreaseCap` | Percent Increase Cap | Enter the cap of any percentage increases in this field. This field also caps escalations related to CPI-indexed rent increases. | Percentage | Global |  | `expense_setup.PercentIncreaseCap · TEXT` |  |
| `PlanCapPercent` | Plan Cap Percent | Enter the maximum growth percentage that can be applied in the plan. If this value is populated it will override the plan growth percent where it exceeds the cap. | Percentage | Global |  | `expense_setup.PlanCapPercent · TEXT` |  |
| `PlanGrowthPercent` | Plan Growth Percent | Enter the percentage will be used to calculate the plan values. | Percentage | Global |  | `expense_setup.PlanGrowthPercent · TEXT` |  |
| `ProRataShareRate` | Pro Rata Share Rate | Enter the pro rata share for the expense in this field. Pro Rata Share refers to a proportionate share of an expense. For example, many contracts for tenants of indoor malls stipulate that each tenant pay a pre-determined percentage of common area maintenance (CAM) expenses. | Percentage | Global |  | `expense_setup.ProRataShareRate · TEXT` |  |
| `SecondaryRentSchedAllocPercent` | Secondary Rent Schedule Allocation Percent | If you will be allocating a percentage of the expense to a secondary schedule, enter the percentage allocation in this field. | Percentage | Global |  | `expense_setup.SecondaryRentSchedAllocPercent · TEXT` |  |

### Quantities (5)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CPIMultiplier` | CPI Multiplier | Enter your CPI index multiplier in the CPI Multiplier field. The CPI Index Multiplier field follows these rules: A. By default, the value of the CPI Index Multiplier field is 1. B. Any value greater than 0 is allowed. C. If a value of 0 or less is entered, the system returns an error message that reads, The value of the multiplier should be a number greater than zero, with 1 giving the nominal value. | Number | Global |  | `expense_setup.CPIMultiplier · TEXT` |  |
| `ExpenseSetupID` | Expense Setup RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `expense_setup.ExpenseSetupID · VARCHAR(64) NOT NULL` |  |
| `NumberOfPayments` | Number Of Payments | This field is no longer in use. | Number | Global |  | `expense_setup.NumberOfPayments · TEXT` |  |
| `PaymentDueDay` | Payment Due Day | Enter the payment due date in this field. If the payment due date is the last day of the month, enter 0 in this field. | Number | Global |  | `expense_setup.PaymentDueDay · TEXT` |  |
| `RentableArea` | Rentable Area | The Rentable Area field must be populated in order for the system to calculate your rate. The system will remember your rentable area and populate this field whenever it is present on a page. If you are not going to use rentable area, do not enter 0. Leave this field blank. | Number | Global |  | `expense_setup.RentableArea · TEXT` |  |

### Dates & timestamps (18)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BeginDate` | Begin Date | The Begin Date field allows you to select a begin date for the record. | Date | Global |  | `expense_setup.BeginDate · TEXT` |  |
| `CoverageBeginAnnual` | Coverage Begin Annual | Select the date your annual payment coverage begins from this field. | Date | Global |  | `expense_setup.CoverageBeginAnnual · TEXT` |  |
| `CoverageBeginQ1` | Coverage Begin Q1 | Select the date that payment coverage begins for Q1 from this field. | Date | Global |  | `expense_setup.CoverageBeginQ1 · TEXT` |  |
| `CoverageBeginQ2` | Coverage Begin Q2 | Select the date that payment coverage begins for Q2 from this field. | Date | Global |  | `expense_setup.CoverageBeginQ2 · TEXT` |  |
| `CoverageBeginQ3` | Coverage Begin Q3 | Select the date that payment coverage begins for Q3 from this field. | Date | Global |  | `expense_setup.CoverageBeginQ3 · TEXT` |  |
| `CoverageBeginQ4` | Coverage Begin Q4 | Select the date that payment coverage begins for Q4 from this field. | Date | Global |  | `expense_setup.CoverageBeginQ4 · TEXT` |  |
| `CoverageBeginSemiAnnual1` | Coverage Begin Semi Annual 1 | Select the date that the first period of your semiannual payment coverage begins from this field. | Date | Global |  | `expense_setup.CoverageBeginSemiAnnual1 · TEXT` |  |
| `CoverageBeginSemiAnnual2` | Coverage Begin Semi Annual 2 | Select the date that the second period of your semiannual payment coverage begins from this field. | Date | Global |  | `expense_setup.CoverageBeginSemiAnnual2 · TEXT` |  |
| `EndDate` | End Date | The End Date field allows you to select an end date for the record. | Date | Global |  | `expense_setup.EndDate · TEXT` |  |
| `FirstPaymentDueDate` | First Payment Due Date | Select the date that your first payment is due from this field. | Date | Global |  | `expense_setup.FirstPaymentDueDate · TEXT` |  |
| `LastPaymentDueDate` | Last Payment Due Date | Select the date that your last payment is due from this field. | Date | Global |  | `expense_setup.LastPaymentDueDate · TEXT` |  |
| `PaymentDueAnnual` | Payment Due Annual | Select your annual due date from this field. | Date | Global |  | `expense_setup.PaymentDueAnnual · TEXT` |  |
| `PaymentDueQ1` | Payment Due Q1 | Select your payment due date for Q1 from this field. | Date | Global |  | `expense_setup.PaymentDueQ1 · TEXT` |  |
| `PaymentDueQ2` | Payment Due Q2 | Select your payment due date for Q2 from this field. | Date | Global |  | `expense_setup.PaymentDueQ2 · TEXT` |  |
| `PaymentDueQ3` | Payment Due Q3 | Select your payment due date for Q3 from this field. | Date | Global |  | `expense_setup.PaymentDueQ3 · TEXT` |  |
| `PaymentDueQ4` | Payment Due Q4 | Select your payment due date for Q4 from this field. | Date | Global |  | `expense_setup.PaymentDueQ4 · TEXT` |  |
| `PaymentDueSemiAnnual1` | Payment Due Semi Annual 1 | Select your payment due date for your first semiannual period from this field. | Date | Global |  | `expense_setup.PaymentDueSemiAnnual1 · TEXT` |  |
| `PaymentDueSemiAnnual2` | Payment Due Semi Annual 2 | Select your payment due date for your last semiannual period from this field. | Date | Global |  | `expense_setup.PaymentDueSemiAnnual2 · TEXT` |  |

### Flags (15)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ApplyTax1Flag` | Apply Tax #1? | Select this check box to apply tax rate #1 of the associated entity. | Boolean | Global |  | `expense_setup.ApplyTax1Flag · TEXT` |  |
| `ApplyTax2Flag` | Apply Tax #2? | Select this check box to apply tax rate #2 of the associated entity. | Boolean | Global |  | `expense_setup.ApplyTax2Flag · TEXT` |  |
| `ApplyTax3Flag` | Apply Tax #3? | Select this check box to apply tax rate #3 of the associated entity. | Boolean | Global |  | `expense_setup.ApplyTax3Flag · TEXT` |  |
| `ApplyTax4Flag` | Apply Tax #4? | Select this check box to apply tax rate #4 of the associated entity. | Boolean | Global |  | `expense_setup.ApplyTax4Flag · TEXT` |  |
| `Firm_CPIIncrease` | CPI Increase |  | Boolean | Firm |  | `expense_setup.Firm_CPIIncrease · TEXT` |  |
| `HoldFlag` | Hold? | Select this check box to indicate that this payment should be held. This check box is informational-only. | Boolean | Global |  | `expense_setup.HoldFlag · TEXT` |  |
| `IncludeInPlanForecast` | Include in Planning and Forecasting | Select this check box to make this expense available in the planning and forecasting feature in the accruals area. | Boolean | Global |  | `expense_setup.IncludeInPlanForecast · TEXT` |  |
| `IsCPICompounding` | Is CPI Compounding? | This field is a placeholder in preparation for an upcoming enhancement. | Boolean | Global |  | `expense_setup.IsCPICompounding · TEXT` |  |
| `IsCustomPaymentCoverage` | Custom Payment Coverage | Select this check box to enable Custom Payment Coverage for your contract. Please see the Lx Online Help for more information about Custom Payment Coverage. This functionality used to be titled UK Coverage. | Boolean | Global |  | `expense_setup.IsCustomPaymentCoverage · TEXT` |  |
| `IsDailyRent` | Daily Rent | Select this check box if this expense setup uses daily rent. | Boolean | Global |  | `expense_setup.IsDailyRent · TEXT` |  |
| `IsPayArrears` | Pay in Arrears? | Select this check box if your payments will be considered paid at the end of the month. This means that interest expense in a schedule will accrue first before the payment is applied. One very distinct outcome of this is that a schedule that is paid at the beginning of the month should not have an interest expense in its last month. | Boolean | Global |  | `expense_setup.IsPayArrears · TEXT` |  |
| `IsReceivable` | Is Receivable? | Select this check box if the expense setup record is for an accounts receivable item, also known as an income item. | Boolean | Global |  | `expense_setup.IsReceivable · TEXT` |  |
| `ReadyForPaymentFlag` | Ready For Payment? | Select this check box to indicate this transaction is ready to be paid. | Boolean | Global |  | `expense_setup.ReadyForPaymentFlag · TEXT` |  |
| `ReconcilableExpense` | Reconcilable Expense? | Select this check box if the expense is reconcilable. | Boolean | Global |  | `expense_setup.ReconcilableExpense · TEXT` |  |
| `TaxesIncludedFlag` | Taxes Included In Amount? | This flag indicates that taxes are included in the total expense amount, and impacts how the taxes are calculated. | Boolean | Global |  | `expense_setup.TaxesIncludedFlag · TEXT` |  |

### Text & notes (11)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BankAccountNumber` | Bank Account Number | This field is no longer in use. | Text | Global |  | `expense_setup.BankAccountNumber · TEXT` |  |
| `BankRoutingNumber` | Bank Routing Number | This field is no longer in use. | Text | Global |  | `expense_setup.BankRoutingNumber · TEXT` |  |
| `CPINotes` | CPI Notes | This field can be used to annotate your chosen CPI Index with comments. | Text | Global |  | `expense_setup.CPINotes · TEXT` |  |
| `Description` |  | Write a description of the record. | Text | Global |  | `expense_setup.Description · TEXT` |  |
| `InternalReferenceNumber` | Internal Reference Number | Enter the general ledger that this recurring expense will be charged to in this field. This field is information-only. You will still need to configure your account information when you create your expense types and allocations. | Text | Global |  | `expense_setup.InternalReferenceNumber · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `expense_setup.Notes · TEXT` |  |
| `PlanForecastNotes` | Planning and Forecasting Notes | Enter any notes about your planning and forecasting in this field. | Text | Global |  | `expense_setup.PlanForecastNotes · TEXT` |  |
| `RemitMessage` | Remit Message | Enter the message that will appear on the memo line of a check. | Text | Global |  | `expense_setup.RemitMessage · TEXT` |  |
| `Section` |  | Enter the section of the covenant that pertains to this record in this field. | Text | Global |  | `expense_setup.Section · TEXT` |  |
| `VendorAccountNumber` | Vendor Account Number | This field is no longer in use. | Text | Global |  | `expense_setup.VendorAccountNumber · TEXT` |  |
| `VendorAllocationList` | Vendor Allocation List | This field returns a comma-separated list of the vendors associated with an expense setup. | Text | Global |  | `expense_setup.VendorAllocationList · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Expense Setup ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `expense_setup.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `expense_setup.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `expense_setup.ModifiedDate · TEXT` |  |

### Other (1)

Everything that did not fall into a named group.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DateRange` | Date Range | This field is no longer in use. | Date Range | Global |  | `expense_setup.DateRange · TEXT` |  |

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
