# ExpenseEscalation

*28 fields · module: Lease Accounting & Payments · Postgres: `expense_escalation`*

An automatic escalation clause on a recoverable expense — base amount/year, cap amount/percentage, and begin date, distinct from CPI-indexed escalation (see the small CPI entity). 27 Global fields under Contract.

Source: `data-fields/expense-escalation.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 28 |
| Fields with a vendor definition | 27 of 28 inventoried |
| Physical tables | `expense_escalation` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 27 (27 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 5 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 3 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in expense_escalation

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 27 fields carry a vendor definition

**Observed.** 27 of this record's 28 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: the captures agree

**Observed.** Over the 27 fields both the Data Fields catalogue and the field inventory contain, the two agree on every one. 3 are marked required.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-030](../rules/CON-R-030.md) | Authoring a recurring expense through the wizard: the wizard's start date, end date, starting amount, amount type and escalation settings materialise ExpenseSetup + ExpenseEscalation + the full ExpenseSchedule in one action. | Observed |
| [CON-R-040](../rules/CON-R-040.md) | An escalation step falls due: a step occurs every EscalationPeriod × CodeFrequencyID units inside the clause's BeginDate..EndDate window. | Derived |
| [CON-R-049](../rules/CON-R-049.md) | Increase/decrease asymmetry: ExpenseSetup.AmountIncreaseCap/AmountDecreaseCap/PercentIncreaseCap/PercentDecreaseCap are a separate, parallel collar to ExpenseEscalation's own min/max, with unspecified precedence between the two. | Observed |

## Fields

### Relationships (foreign keys) (4)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ContractID` | Contract | The Expense Escalation table is no longer used. | Contract ID | Global | yes | `expense_escalation.ContractID · TEXT` | [Contract](Contract.md) |
| `EscalationIndexID` | Escalation Index | The Expense Escalation table is no longer used. | Escalation Index ID | Global |  | `expense_escalation.EscalationIndexID · TEXT` | [EscalationIndex](EscalationIndex.md) |
| `ExpenseSetupID` | Expense Setup | The Expense Escalation table is no longer used. | Expense Setup ID | Global | yes | `expense_escalation.ExpenseSetupID · TEXT` | [ExpenseSetup](ExpenseSetup.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `expense_escalation.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (4)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeEscalationCategoryID` | Escalation Category | The Expense Escalation table is no longer used. | Dropdown (Escalation Category Code) | Global |  | `expense_escalation.CodeEscalationCategoryID · TEXT` | Escalation Category Code |
| `CodeEscalationGroupID` | Escalation Group | The Expense Escalation table is no longer used. | Dropdown (Escalation Group Code) | Global |  | `expense_escalation.CodeEscalationGroupID · TEXT` | Escalation Group Code |
| `CodeEscalationTypeID` | Escalation Type | The Expense Escalation table is no longer used. | Dropdown (Escalation Type Code) | Global |  | `expense_escalation.CodeEscalationTypeID · TEXT` | Escalation Type Code |
| `CodeFrequencyID` | Frequency | The Expense Escalation table is no longer used. | Dropdown (Frequency Code) | Global |  | `expense_escalation.CodeFrequencyID · TEXT` | Frequency Code |

### Money (4)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BaseAmount` | Base Amount | The Expense Escalation table is no longer used. | Currency | Global |  | `expense_escalation.BaseAmount · TEXT` |  |
| `CapAmount` | Cap Amount | The Expense Escalation table is no longer used. | Currency | Global |  | `expense_escalation.CapAmount · TEXT` |  |
| `FixedAmount` | Fixed Amount | The Expense Escalation table is no longer used. | Currency | Global |  | `expense_escalation.FixedAmount · TEXT` |  |
| `StopAmount` | Stop Amount | The Expense Escalation table is no longer used. | Currency | Global |  | `expense_escalation.StopAmount · TEXT` |  |

### Rates & percentages (6)

Percentage inputs and computed rates.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CapPercentage` | Cap Percentage | The Expense Escalation table is no longer used. | Percentage | Global |  | `expense_escalation.CapPercentage · TEXT` |  |
| `IndexBaseFactor` | Index Base Factor | The Expense Escalation table is no longer used. | Percentage | Global |  | `expense_escalation.IndexBaseFactor · TEXT` |  |
| `LifetimeMaxPercentage` | Lifetime Max Percentage | The Expense Escalation table is no longer used. | Percentage | Global |  | `expense_escalation.LifetimeMaxPercentage · TEXT` |  |
| `LifetimeMinPercentage` | Lifetime Min Percentage | The Expense Escalation table is no longer used. | Percentage | Global |  | `expense_escalation.LifetimeMinPercentage · TEXT` |  |
| `PeriodMaxPercentage` | Period Max Percentage | The Expense Escalation table is no longer used. | Percentage | Global |  | `expense_escalation.PeriodMaxPercentage · TEXT` |  |
| `PeriodMinPercentage` | Period Min Percentage | The Expense Escalation table is no longer used. | Percentage | Global |  | `expense_escalation.PeriodMinPercentage · TEXT` |  |

### Quantities (2)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `EscalationPeriod` | Escalation Period | The Expense Escalation table is no longer used. | Number | Global |  | `expense_escalation.EscalationPeriod · TEXT` |  |
| `ExpenseEscalationID` | Escalation RecID | The Expense Escalation table is no longer used. | Number | Global |  | `expense_escalation.ExpenseEscalationID · VARCHAR(64) NOT NULL` |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BeginDate` | Begin Date | The Expense Escalation table is no longer used. | Date | Global |  | `expense_escalation.BeginDate · TEXT` |  |
| `EndDate` | End Date | The Expense Escalation table is no longer used. | Date | Global |  | `expense_escalation.EndDate · TEXT` |  |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BaseYear` | Base Year | The Expense Escalation table is no longer used. | Text | Global |  | `expense_escalation.BaseYear · TEXT` |  |
| `EscalationMethod` | Escalation Method | The Expense Escalation table is no longer used. | Text | Global |  | `expense_escalation.EscalationMethod · TEXT` |  |
| `Notes` |  | The Expense Escalation table is no longer used. | Text | Global |  | `expense_escalation.Notes · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Escalation ClientID | The Expense Escalation table is no longer used. | Text | Global | yes | `expense_escalation.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Expense Escalation table is no longer used. | Member ID | Global |  | `expense_escalation.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Expense Escalation table is no longer used. | Time | Global |  | `expense_escalation.ModifiedDate · TEXT` |  |
