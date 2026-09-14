# AcctingAssumptionAdjust

*19 fields · module: Lease Accounting & Payments · Postgres: `accting_assumption_adjust`*

A manual adjustment to lease-accounting assumptions used in ASC 842/IFRS 16 calculations — adjustment percent and annual amount, letting an accountant override a calculated assumption. 18 Global fields under Contract.

Source: `data-fields/accting-assumption-adjust.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 19 |
| Fields with a vendor definition | 18 of 19 inventoried |
| Physical tables | `accting_assumption_adjust` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 18 (18 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 3 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 2 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in accting_assumption_adjust

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 18 fields carry a vendor definition

**Observed.** 18 of this record's 19 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: 1 disagree of 18 comparable

**Observed.** Over the 18 fields both captures contain, they agree on 17. The exceptions are ContractID. Estate-wide there are 43 such fields and every one runs the same way — catalogue-required, inventory-not — and they are 34 ContractID, 8 ProjectEntityID and 1 ShortName: the owner foreign key. Parenthood is enforced by the application, not by the database.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [ACC-R-020](../rules/ACC-R-020.md) | `SLSummary.NeedsRecalculation := true` | Observed |
| [ACC-R-026](../rules/ACC-R-026.md) | the stated percentage of the amount is allocated to a secondary schedule; the remainder to the primary | Observed |

## Fields

### Relationships (foreign keys) (3)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global | yes | `accting_assumption_adjust.ContractID · TEXT` | [Contract](Contract.md) |
| `ExpenseSetupID` | Expense Setup | The ExpenseSetupID field is used to associate an accounting assumption adjustment with an expense setup record. | Expense Setup ID | Global |  | `accting_assumption_adjust.ExpenseSetupID · TEXT` | [ExpenseSetup](ExpenseSetup.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `accting_assumption_adjust.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (4)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeASC842ScheduleID` | ASC 842 Schedule | The ASC 842 Schedule field is where you select the ASC 842 schedule you want to associate with a record. This field is functional, and changing its value on the Accounting Assumptions page, the Covenants page, or the Recurring Expenses page will set the Recalc? flag to YES. | Dropdown (ASC 842 Schedule Type) | Global |  | `accting_assumption_adjust.CodeASC842ScheduleID · TEXT` | ASC 842 Schedule Type |
| `CodeFrequencyID` | Frequency | Select the frequency of your payment from this field. | Dropdown (Frequency Code) | Global |  | `accting_assumption_adjust.CodeFrequencyID · TEXT` | Frequency Code |
| `CodeIFRS16ScheduleID` | IFRS 16 Schedule | The IFRS 16 Schedule field is where you select the IFRS 16 schedule you want to associate with a record. This field is functional, and changing its value on the Accounting Assumptions page, the Covenants page, or the Recurring Expenses page will set the Recalc? flag to YES. | Dropdown (IFRS 16 Schedule Type) | Global |  | `accting_assumption_adjust.CodeIFRS16ScheduleID · TEXT` | IFRS 16 Schedule Type |
| `CodeProrationMethodID` | Proration Method | Select a proration method from this field. The proration method you choose tells the system how much a day is worth, when your cost period does not encompass the entirety of the period. | Dropdown (Proration Method Code) | Global |  | `accting_assumption_adjust.CodeProrationMethodID · TEXT` | Proration Method Code |

### Money (5)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AnnualAmount` | Annual Amount | The Annual Amount field is where the system will store the annual amount of the accounting assumption adjustment. The First Payment Amount, Last Payment Amount, and Annual Amount fields will auto-populate depending upon the value you enter in the Payment Amount field and the frequency you select from the Frequency field. | Currency | Global | yes | `accting_assumption_adjust.AnnualAmount · TEXT` |  |
| `FirstPaymentAmount` | First Payment Amount | The First Payment Amount field is where the system will store the first payment amount. The First Payment Amount, Last Payment Amount, and Annual Amount fields will auto-populate depending upon the value you enter in the Payment Amount field and the frequency you select from the Frequency field. | Currency | Global |  | `accting_assumption_adjust.FirstPaymentAmount · TEXT` |  |
| `LastPaymentAmount` | Last Payment Amount | The Last Payment Amount field is where the system will store the last payment amount. The First Payment Amount, Last Payment Amount, and Annual Amount fields will auto-populate depending upon the value you enter in the Payment Amount field and the frequency you select from the Frequency field. | Currency | Global |  | `accting_assumption_adjust.LastPaymentAmount · TEXT` |  |
| `PaymentAmount` | Payment Amount | Enter your payment amount for the accounting assumption adjustment in this field. | Currency | Global | yes | `accting_assumption_adjust.PaymentAmount · TEXT` |  |
| `PaymentRate` | Payment Rate | Enter the payment rate in this field. The payment rate is a currency value: for example, $1.00 per square foot. | Currency | Global |  | `accting_assumption_adjust.PaymentRate · TEXT` |  |

### Rates & percentages (2)

Percentage inputs and computed rates.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AdjustmentPercent` | Adjustment Percent | This field is a placeholder in preparation for an upcoming enhancement. | Percentage | Global |  | `accting_assumption_adjust.AdjustmentPercent · TEXT` |  |
| `SecondaryRentSchedAllocPercent` | Accounting Assumption Adjustment Secondary Rent Schedule Allocation Percent | If the expense setup has a secondary schedule allocation percentage, enter the allocation in this field. | Percentage | Global |  | `accting_assumption_adjust.SecondaryRentSchedAllocPercent · TEXT` |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AcctingAssumptionAdjustID` | Accting Assumption Adjust RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `accting_assumption_adjust.AcctingAssumptionAdjustID · VARCHAR(64) NOT NULL` |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BeginDate` | Begin Date | The Begin Date field allows you to select a begin date for the record. | Date | Global | yes | `accting_assumption_adjust.BeginDate · TEXT` |  |
| `EndDate` | End Date | The End Date field allows you to select an end date for the record. | Date | Global | yes | `accting_assumption_adjust.EndDate · TEXT` |  |

### Text & notes (1)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Notes` |  | Add any notes about the record. | Text | Global |  | `accting_assumption_adjust.Notes · TEXT` |  |

### Audit & record keeping (1)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Accting Assumption Adjust ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `accting_assumption_adjust.BOMapClientRecordID · TEXT` |  |
