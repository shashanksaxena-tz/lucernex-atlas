# UseBasedRent

*23 fields · module: Variable Rent (Percentage / Use-Based) & Sales · Postgres: `use_based_rent`*

The usage-based rent clause header (e.g., per-unit, per-transaction rent) — billing frequency and currency type, the clause-level record UseBasedRentBreakpoint and VirtualUseBasedRentPeriod project from. 22 Global fields under Contract.

Source: `data-fields/use-based-rent.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 23 |
| Catalogued fields | 22 (22 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 5 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

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
| `RentYearStartMonth` | Rent Year Start Month | Dropdown | Global |  |  |

### Coded values (drop-downs) (8)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeBillingFrequencyID` | Billing Frequency | Dropdown (Frequency Code) | Global |  | Frequency Code |
| `CodeCurrencyTypeID` | Currency Type | Dropdown (Currency Type Code) | Global |  | Currency Type Code |
| `CodeExpenseGroupID` | Expense Group | Dropdown (Expense Group Code) | Global |  | Expense Group Code |
| `CodeExpenseTypeID` | Expense Type | Dropdown (Expense Type Code) | Global |  | Expense Type Code |
| `CodeReportingFrequencyID` | Reporting Frequency | Dropdown (Frequency Code) | Global |  | Frequency Code |
| `CodeUsageGroupID` | Usage Group | Dropdown (Usage Group Code) | Global |  | Usage Group Code |
| `CodeUsageUnitTypeID` | Usage Unit Type | Dropdown (Usage Unit Type Code) | Global |  | Usage Unit Type Code |
| `CodeUseRentModelTypeID` | Model Type | Dropdown (Use Rent Model Type Code) | Global | yes | Use Rent Model Type Code |

### Quantities (3)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `PeriodPaymentDueDays` | Period Payment Due Days | Number | Global |  |  |
| `PeriodReportDueDays` | Period Report Due Days | Number | Global |  |  |
| `UseBasedRentID` | Use Based Rent RecID | Number | Global |  |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BeginDate` | Begin Date | Date | Global |  |  |
| `EndDate` | End Date | Date | Global |  |  |

### Text & notes (2)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Description` |  | Text | Global |  |  |
| `Notes` |  | Text | Global |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Use Based Rent ClientID | Text | Global | yes |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
