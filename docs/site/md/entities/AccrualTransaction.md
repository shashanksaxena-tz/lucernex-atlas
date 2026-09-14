# AccrualTransaction

*55 fields · module: Lease Accounting & Payments · Postgres: `accrual_transaction`*

An individual expense-accrual posting tied to a contract, carrying up to eight parallel Account Number fields for GL split coding, matching the same allocation pattern seen in PaymentTransaction. 54 Global fields under Contract.

Source: `data-fields/accrual-transaction.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 55 |
| Fields with a vendor definition | 54 of 55 inventoried |
| Physical tables | `accrual_transaction` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 54 (54 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 5 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 6 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in accrual_transaction

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 54 fields carry a vendor definition

**Observed.** 54 of this record's 55 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: 1 disagree of 54 comparable

**Observed.** Over the 54 fields both captures contain, they agree on 53. The exceptions are ContractID. Estate-wide there are 43 such fields and every one runs the same way — catalogue-required, inventory-not — and they are 34 ContractID, 8 ProjectEntityID and 1 ShortName: the owner foreign key. Parenthood is enforced by the application, not by the database.

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

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global | yes | `accrual_transaction.ContractID · TEXT` | [Contract](Contract.md) |
| `OrganizationID` | Organization | Select the organization from which this payment should be debited from this field. | Organization ID | Global |  | `accrual_transaction.OrganizationID · TEXT` | [Organization](Organization.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `accrual_transaction.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (4)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeCurrencyTypeID` | Currency Type | The Currency Type field allows you to select a currency type to be used on a record. | Dropdown (Currency Type Code) | Global |  | `accrual_transaction.CodeCurrencyTypeID · TEXT` | Currency Type Code |
| `CodeExpenseCategoryID` | Expense Category | The Expense Category field allows you to associate your record with a pre-configured expense category. Categories are the children of types, and the grandchildren of groups. | Dropdown (Expense Category Code) | Global |  | `accrual_transaction.CodeExpenseCategoryID · TEXT` | Expense Category Code |
| `CodeExpenseGroupID` | Expense Group | The Expense Group field allows you to associate your record with a pre-configured expense group. Expense groups are used to categorize expense types. | Dropdown (Expense Group Code) | Global |  | `accrual_transaction.CodeExpenseGroupID · TEXT` | Expense Group Code |
| `CodeExpenseTypeID` | Expense Type | The Expense Type field allows you to associate your record with a pre-configured expense type. Expense Types are used to associate records with lease accounting schedules, AP export numbers, expense accrual accounts, percentage rent accrual accounts, and real estate tax accounts. | Dropdown (Expense Type Code) | Global |  | `accrual_transaction.CodeExpenseTypeID · TEXT` | Expense Type Code |

### Money (6)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `PeriodAmount` | Period Amount | Enter the amount that is being accrued for the period in this field. This field will be disabled if you select the Include Taxes in Total Amount? Flag. | Currency | Global |  | `accrual_transaction.PeriodAmount · TEXT` |  |
| `TaxAmount1` | Tax Amount #1 | Enter the primary tax amount in currency in this field. | Currency | Global |  | `accrual_transaction.TaxAmount1 · TEXT` |  |
| `TaxAmount2` | Tax Amount #2 | Enter the secondary tax amount in currency in this field. | Currency | Global |  | `accrual_transaction.TaxAmount2 · TEXT` |  |
| `TaxAmount3` | Tax Amount #3 | Enter the third tax amount in currency in this field. | Currency | Global |  | `accrual_transaction.TaxAmount3 · TEXT` |  |
| `TaxAmount4` | Tax Amount #4 | Enter the fourth tax amount in currency in this field. | Currency | Global |  | `accrual_transaction.TaxAmount4 · TEXT` |  |
| `TotalAmount` | Total Amount | This field will only be editable if the Taxes Included in Amount? flag is selected. The total amount is the period amount plus any taxes. | Currency | Global |  | `accrual_transaction.TotalAmount · TEXT` |  |

### Quantities (3)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AccrualTransactionID` | Accrual Transaction RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `accrual_transaction.AccrualTransactionID · VARCHAR(64) NOT NULL` |  |
| `PeriodNumber` | Period Number | Enter the period number as a two-digit number in this field. | Number | Global |  | `accrual_transaction.PeriodNumber · TEXT` |  |
| `PeriodYear` | Period Year | Select the year of the transaction period from this field. | Number | Global |  | `accrual_transaction.PeriodYear · TEXT` |  |

### Dates & timestamps (3)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `PeriodBeginDate` | Period Begin Date | Enter or use the calendar picker to select the begin date of the transaction period. | Date | Global |  | `accrual_transaction.PeriodBeginDate · TEXT` |  |
| `PeriodEndDate` | Period End Date | Enter or use the calendar picker to select the end date of the transaction period. | Date | Global |  | `accrual_transaction.PeriodEndDate · TEXT` |  |
| `PostingDate` | Posting Date | Enter or use the calendar picker to select the posting date of the transaction. | Date | Global |  | `accrual_transaction.PostingDate · TEXT` |  |

### Flags (3)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `HoldFlag` | Hold? | This flag is informational-only. Select this check box to mark this accrual transaction as being on hold. | Boolean | Global |  | `accrual_transaction.HoldFlag · TEXT` |  |
| `ProcessedFlag` | Processed? | Select this check box once you have processed your accrual transaction. Warning - once you mark a transaction as processed, you cannot change it. | Boolean | Global |  | `accrual_transaction.ProcessedFlag · TEXT` |  |
| `TaxesIncludedFlag` | Taxes Included In Amount? | Select this check box if taxes are included in the value you entered in the Period Amount field. The system will then subtract the tax amounts from the period amount, and the Total Amount field becomes editable. If you need to make changes to the value in the Total Amount field, you may now do so. | Boolean | Global |  | `accrual_transaction.TaxesIncludedFlag · TEXT` |  |

### Text & notes (27)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `APExportBaseNumber` | AP Export Base Number | The account number for your expenses. The account number is configured at the expense type level. | Text | Global |  | `accrual_transaction.APExportBaseNumber · TEXT` |  |
| `APExportPrepaidNumber` | AP Export Prepaid Number | The account number for your prepaid expenses (if applicable). The account number is configured at the expense type level. | Text | Global |  | `accrual_transaction.APExportPrepaidNumber · TEXT` |  |
| `AccountNumber1` | Account Number #1 | This field contains an account number associated with the organization. You can edit these account numbers at the organization-level. | Text | Global |  | `accrual_transaction.AccountNumber1 · TEXT` |  |
| `AccountNumber2` | Account Number #2 | This field contains an account number associated with the organization. You can edit these account numbers at the organization-level. | Text | Global |  | `accrual_transaction.AccountNumber2 · TEXT` |  |
| `AccountNumber3` | Account Number #3 | This field contains an account number associated with the organization. You can edit these account numbers at the organization-level. | Text | Global |  | `accrual_transaction.AccountNumber3 · TEXT` |  |
| `AccountNumber4` | Account Number #4 | This field contains an account number associated with the organization. You can edit these account numbers at the organization-level. | Text | Global |  | `accrual_transaction.AccountNumber4 · TEXT` |  |
| `AccountNumber5` | Account Number #5 | This field contains an account number associated with the organization. You can edit these account numbers at the organization-level. | Text | Global |  | `accrual_transaction.AccountNumber5 · TEXT` |  |
| `AccountNumber6` | Account Number #6 | This field contains an account number associated with the organization. You can edit these account numbers at the organization-level. | Text | Global |  | `accrual_transaction.AccountNumber6 · TEXT` |  |
| `AccountNumber7` | Account Number #7 | This field contains an account number associated with the organization. You can edit these account numbers at the organization-level. | Text | Global |  | `accrual_transaction.AccountNumber7 · TEXT` |  |
| `AccountNumber8` | Account Number #8 | This field contains an account number associated with the organization. You can edit these account numbers at the organization-level. | Text | Global |  | `accrual_transaction.AccountNumber8 · TEXT` |  |
| `AccrualMessage` | Accrual Message | Enter a message for the memo line in this field. | Text | Global |  | `accrual_transaction.AccrualMessage · TEXT` |  |
| `Description` |  | Write a description of the record. | Text | Global |  | `accrual_transaction.Description · TEXT` |  |
| `ExpAccrualAcct1Number` | Exp Accrual Acct #1 Number | This field contains an account number for your expense accruals. The account number is configured at the expense type level. | Text | Global |  | `accrual_transaction.ExpAccrualAcct1Number · TEXT` |  |
| `ExpAccrualAcct2Number` | Exp Accrual Acct #2 Number | This field contains an account number for your expense accruals. The account number is configured at the expense type level. | Text | Global |  | `accrual_transaction.ExpAccrualAcct2Number · TEXT` |  |
| `ExpAccrualAcct3Number` | Exp Accrual Acct #3 Number | This field contains an account number for your expense accruals. The account number is configured at the expense type level. | Text | Global |  | `accrual_transaction.ExpAccrualAcct3Number · TEXT` |  |
| `ExpAccrualAcct4Number` | Exp Accrual Acct #4 Number | This field contains an account number for your expense accruals. The account number is configured at the expense type level. | Text | Global |  | `accrual_transaction.ExpAccrualAcct4Number · TEXT` |  |
| `ExpenseAccrualSetupID` | Expense Accrual Setup | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Text | Global |  | `accrual_transaction.ExpenseAccrualSetupID · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `accrual_transaction.Notes · TEXT` |  |
| `PercentRentAccrualAcct1Number` | Percent Rent Accrual Acct #1 | This field contains an account number for your percent rent accruals. The account number is configured at the expense type level. | Text | Global |  | `accrual_transaction.PercentRentAccrualAcct1Number · TEXT` |  |
| `PercentRentAccrualAcct2Number` | Percent Rent Accrual Acct #2 | This field contains an account number for your percent rent accruals. The account number is configured at the expense type level. | Text | Global |  | `accrual_transaction.PercentRentAccrualAcct2Number · TEXT` |  |
| `PercentRentAccrualAcct3Number` | Percent Rent Accrual Acct #3 | This field contains an account number for your percent rent accruals. The account number is configured at the expense type level. | Text | Global |  | `accrual_transaction.PercentRentAccrualAcct3Number · TEXT` |  |
| `PercentRentAccrualAcct4Number` | Percent Rent Accrual Acct #4 | This field contains an account number for your percent rent accruals. The account number is configured at the expense type level. | Text | Global |  | `accrual_transaction.PercentRentAccrualAcct4Number · TEXT` |  |
| `RETaxAccrualAcct1Number` | RE Tax Accrual Acct #1 | This field contains an account number for your real estate tax accruals. The account number is configured at the expense type level. | Text | Global |  | `accrual_transaction.RETaxAccrualAcct1Number · TEXT` |  |
| `RETaxAccrualAcct2Number` | RE Tax Accrual Acct #2 | This field contains an account number for your real estate tax accruals. The account number is configured at the expense type level. | Text | Global |  | `accrual_transaction.RETaxAccrualAcct2Number · TEXT` |  |
| `RETaxAccrualAcct3Number` | RE Tax Accrual Acct #3 | This field contains an account number for your real estate tax accruals. The account number is configured at the expense type level. | Text | Global |  | `accrual_transaction.RETaxAccrualAcct3Number · TEXT` |  |
| `RETaxAccrualAcct4Number` | RE Tax Accrual Acct #4 | This field contains an account number for your real estate tax accruals. The account number is configured at the expense type level. | Text | Global |  | `accrual_transaction.RETaxAccrualAcct4Number · TEXT` |  |
| `SourceEntityTable` | Source Entity Table | The batch ID for your accrual payment transaction. | Text | Global |  | `accrual_transaction.SourceEntityTable · TEXT` |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Accrual Transaction ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `accrual_transaction.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `accrual_transaction.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `accrual_transaction.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `accrual_transaction.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `accrual_transaction.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | Global |  | `accrual_transaction.RevNumber · TEXT` |  |
