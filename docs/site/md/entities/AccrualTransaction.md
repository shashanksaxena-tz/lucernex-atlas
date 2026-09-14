# AccrualTransaction

*55 fields · module: Lease Accounting & Payments · Postgres: `accrual_transaction`*

An individual expense-accrual posting tied to a contract, carrying up to eight parallel Account Number fields for GL split coding, matching the same allocation pattern seen in PaymentTransaction. 54 Global fields under Contract.

Source: `data-fields/accrual-transaction.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 55 |
| Catalogued fields | 54 (54 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 5 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 6 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [ACC-R-053](../rules/ACC-R-053.md) | - `TaxesIncludedFlag = false` ⇒ `TotalAmount = PeriodAmount + Σ TaxAmountN`, `TotalAmount` read-only. - `TaxesIncludedFlag = true` ⇒ `PeriodAmount` becomes disabled, the system subtracts the tax amounts from the period amount, and `TotalAmo | Observed |
| [CON-R-062](../rules/CON-R-062.md) | Rent already paid is credited: PRPRentDue = PRPTotalRent − SalesPeriodRentPaid − offsets. | Inferred |
| [CON-R-111](../rules/CON-R-111.md) | Eight-segment coding is applied: AccountNumber1..8 exists on PaymentTransaction/AccrualTransaction but not on CodeExpenseType; whether these are 8 segments of one account or 8 split-coding lines is unresolved. | Inferred |
| [CON-R-119](../rules/CON-R-119.md) | An accrual is posted: AccrualTransaction carries PeriodAmount, PeriodBeginDate/EndDate, PeriodNumber/Year and PostingDate, with its own GL slots, driven by GENERATE_ACCRUALS. | Observed |
| [CON-R-125](../rules/CON-R-125.md) | Any generation or posting: HoldFlag on ExpenseSetup, ExpenseSchedule, ExpenseAccrualSetup, PaymentTransaction or AccrualTransaction is a negative gate at every layer. | Observed |
| [CON-R-134](../rules/CON-R-134.md) | Migrating any parent-child edge: seven FKs are declared Text rather than typed, though the target's proper FK type exists elsewhere in the same schema; model them as real FKs with an orphan-handling policy. | Observed |

## Fields

### Relationships (foreign keys) (3)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ContractID` | Contract | Contract ID | Global | yes | [Contract](Contract.md) |
| `OrganizationID` | Organization | Organization ID | Global |  | [Organization](Organization.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (4)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeCurrencyTypeID` | Currency Type | Dropdown (Currency Type Code) | Global |  | Currency Type Code |
| `CodeExpenseCategoryID` | Expense Category | Dropdown (Expense Category Code) | Global |  | Expense Category Code |
| `CodeExpenseGroupID` | Expense Group | Dropdown (Expense Group Code) | Global |  | Expense Group Code |
| `CodeExpenseTypeID` | Expense Type | Dropdown (Expense Type Code) | Global |  | Expense Type Code |

### Money (6)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `PeriodAmount` | Period Amount | Currency | Global |  |  |
| `TaxAmount1` | Tax Amount #1 | Currency | Global |  |  |
| `TaxAmount2` | Tax Amount #2 | Currency | Global |  |  |
| `TaxAmount3` | Tax Amount #3 | Currency | Global |  |  |
| `TaxAmount4` | Tax Amount #4 | Currency | Global |  |  |
| `TotalAmount` | Total Amount | Currency | Global |  |  |

### Quantities (3)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AccrualTransactionID` | Accrual Transaction RecID | Number | Global |  |  |
| `PeriodNumber` | Period Number | Number | Global |  |  |
| `PeriodYear` | Period Year | Number | Global |  |  |

### Dates & timestamps (3)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `PeriodBeginDate` | Period Begin Date | Date | Global |  |  |
| `PeriodEndDate` | Period End Date | Date | Global |  |  |
| `PostingDate` | Posting Date | Date | Global |  |  |

### Flags (3)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `HoldFlag` | Hold? | Boolean | Global |  |  |
| `ProcessedFlag` | Processed? | Boolean | Global |  |  |
| `TaxesIncludedFlag` | Taxes Included In Amount? | Boolean | Global |  |  |

### Text & notes (27)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `APExportBaseNumber` | AP Export Base Number | Text | Global |  |  |
| `APExportPrepaidNumber` | AP Export Prepaid Number | Text | Global |  |  |
| `AccountNumber1` | Account Number #1 | Text | Global |  |  |
| `AccountNumber2` | Account Number #2 | Text | Global |  |  |
| `AccountNumber3` | Account Number #3 | Text | Global |  |  |
| `AccountNumber4` | Account Number #4 | Text | Global |  |  |
| `AccountNumber5` | Account Number #5 | Text | Global |  |  |
| `AccountNumber6` | Account Number #6 | Text | Global |  |  |
| `AccountNumber7` | Account Number #7 | Text | Global |  |  |
| `AccountNumber8` | Account Number #8 | Text | Global |  |  |
| `AccrualMessage` | Accrual Message | Text | Global |  |  |
| `Description` |  | Text | Global |  |  |
| `ExpAccrualAcct1Number` | Exp Accrual Acct #1 Number | Text | Global |  |  |
| `ExpAccrualAcct2Number` | Exp Accrual Acct #2 Number | Text | Global |  |  |
| `ExpAccrualAcct3Number` | Exp Accrual Acct #3 Number | Text | Global |  |  |
| `ExpAccrualAcct4Number` | Exp Accrual Acct #4 Number | Text | Global |  |  |
| `ExpenseAccrualSetupID` | Expense Accrual Setup | Text | Global |  |  |
| `Notes` |  | Text | Global |  |  |
| `PercentRentAccrualAcct1Number` | Percent Rent Accrual Acct #1 | Text | Global |  |  |
| `PercentRentAccrualAcct2Number` | Percent Rent Accrual Acct #2 | Text | Global |  |  |
| `PercentRentAccrualAcct3Number` | Percent Rent Accrual Acct #3 | Text | Global |  |  |
| `PercentRentAccrualAcct4Number` | Percent Rent Accrual Acct #4 | Text | Global |  |  |
| `RETaxAccrualAcct1Number` | RE Tax Accrual Acct #1 | Text | Global |  |  |
| `RETaxAccrualAcct2Number` | RE Tax Accrual Acct #2 | Text | Global |  |  |
| `RETaxAccrualAcct3Number` | RE Tax Accrual Acct #3 | Text | Global |  |  |
| `RETaxAccrualAcct4Number` | RE Tax Accrual Acct #4 | Text | Global |  |  |
| `SourceEntityTable` | Source Entity Table | Text | Global |  |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Accrual Transaction ClientID | Text | Global | yes |  |
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` | Rev Number | Number | Global |  |  |
