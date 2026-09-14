# VariableRentOffset

*20 fields · module: Lease Accounting & Payments · Postgres: `variable_rent_offset`*

A rent offset tied to a variable expense group/type (rent that adjusts based on a specific expense category rather than CPI or sales). 19 Global fields under Contract.

Source: `data-fields/variable-rent-offset.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 20 |
| Catalogued fields | 19 (19 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 3 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 2 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-061](../rules/CON-R-061.md) | Offsets are applied: VariableRentOffset and ScheduledOffset, applied via APPLY_OFFSETS, reduce the rent-year obligation. | Observed |
| [CON-R-075](../rules/CON-R-075.md) | A VariableRentOffset applies: percentage rent is reduced by amounts paid in a named expense group/type, subject to its own cap. | Derived |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ContractID` | Contract | Contract ID | Global | yes | [Contract](Contract.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (8)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeCurrencyTypeID` | Currency Type | Dropdown (Currency Type Code) | Global |  | Currency Type Code |
| `CodeExpenseGroupID` | Expense Group | Dropdown (Expense Group Code) | Global |  | Expense Group Code |
| `CodeExpenseTypeID` | Expense Type | Dropdown (Expense Type Code) | Global |  | Expense Type Code |
| `CodeOffsetGroupID` | Offset Group | Dropdown (Offset Group Code) | Global |  | Offset Group Code |
| `CodeOffsetTypeID` | Offset Type | Dropdown (Offset Type Code) | Global |  | Offset Type Code |
| `CodePRAggregateExpGroupID` | Aggregate Expense Group | Dropdown (Expense Group Code) | Global |  | Expense Group Code |
| `CodePRAggregateExpTypeID` | Aggregate Expense Type | Dropdown (Expense Type Code) | Global |  | Expense Type Code |
| `CodeSalesGroupID` | Sales Group | Dropdown (Sales Group) | Global |  | Sales Group |

### Money (2)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CapAmount` | Cap Amount | Currency | Global |  |  |
| `FixedOffsetAmount` | Fixed Offset Amount | Currency | Global |  |  |

### Rates & percentages (1)

Percentage inputs and computed rates.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CapPercent` | Cap Percent | Percentage | Global |  |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `VariableRentOffsetID` | Offset RecID | Number | Global |  |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BeginDate` | Begin Date | Date | Global |  |  |
| `EndDate` | End Date | Date | Global |  |  |

### Text & notes (1)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Notes` |  | Text | Global |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Offset ClientID | Text | Global | yes |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
