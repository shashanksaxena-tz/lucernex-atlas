# ExpenseEscalation

*28 fields · module: Lease Accounting & Payments · Postgres: `expense_escalation`*

An automatic escalation clause on a recoverable expense — base amount/year, cap amount/percentage, and begin date, distinct from CPI-indexed escalation (see the small CPI entity). 27 Global fields under Contract.

Source: `data-fields/expense-escalation.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 28 |
| Catalogued fields | 27 (27 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 5 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 3 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-030](../rules/CON-R-030.md) | Authoring a recurring expense through the wizard: the wizard's start date, end date, starting amount, amount type and escalation settings materialise ExpenseSetup + ExpenseEscalation + the full ExpenseSchedule in one action. | Observed |
| [CON-R-040](../rules/CON-R-040.md) | An escalation step falls due: a step occurs every EscalationPeriod × CodeFrequencyID units inside the clause's BeginDate..EndDate window. | Derived |
| [CON-R-049](../rules/CON-R-049.md) | Increase/decrease asymmetry: ExpenseSetup.AmountIncreaseCap/AmountDecreaseCap/PercentIncreaseCap/PercentDecreaseCap are a separate, parallel collar to ExpenseEscalation's own min/max, with unspecified precedence between the two. | Observed |

## Fields

### Relationships (foreign keys) (4)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ContractID` | Contract | Contract ID | Global | yes | [Contract](Contract.md) |
| `EscalationIndexID` | Escalation Index | Escalation Index ID | Global |  | [EscalationIndex](EscalationIndex.md) |
| `ExpenseSetupID` | Expense Setup | Expense Setup ID | Global | yes | [ExpenseSetup](ExpenseSetup.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (4)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeEscalationCategoryID` | Escalation Category | Dropdown (Escalation Category Code) | Global |  | Escalation Category Code |
| `CodeEscalationGroupID` | Escalation Group | Dropdown (Escalation Group Code) | Global |  | Escalation Group Code |
| `CodeEscalationTypeID` | Escalation Type | Dropdown (Escalation Type Code) | Global |  | Escalation Type Code |
| `CodeFrequencyID` | Frequency | Dropdown (Frequency Code) | Global |  | Frequency Code |

### Money (4)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BaseAmount` | Base Amount | Currency | Global |  |  |
| `CapAmount` | Cap Amount | Currency | Global |  |  |
| `FixedAmount` | Fixed Amount | Currency | Global |  |  |
| `StopAmount` | Stop Amount | Currency | Global |  |  |

### Rates & percentages (6)

Percentage inputs and computed rates.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CapPercentage` | Cap Percentage | Percentage | Global |  |  |
| `IndexBaseFactor` | Index Base Factor | Percentage | Global |  |  |
| `LifetimeMaxPercentage` | Lifetime Max Percentage | Percentage | Global |  |  |
| `LifetimeMinPercentage` | Lifetime Min Percentage | Percentage | Global |  |  |
| `PeriodMaxPercentage` | Period Max Percentage | Percentage | Global |  |  |
| `PeriodMinPercentage` | Period Min Percentage | Percentage | Global |  |  |

### Quantities (2)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `EscalationPeriod` | Escalation Period | Number | Global |  |  |
| `ExpenseEscalationID` | Escalation RecID | Number | Global |  |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BeginDate` | Begin Date | Date | Global |  |  |
| `EndDate` | End Date | Date | Global |  |  |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BaseYear` | Base Year | Text | Global |  |  |
| `EscalationMethod` | Escalation Method | Text | Global |  |  |
| `Notes` |  | Text | Global |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Escalation ClientID | Text | Global | yes |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
