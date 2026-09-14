# VirtualUBRPAggregate

*14 fields · module: Variable Rent (Percentage / Use-Based) & Sales · Postgres: `virtual_u_b_r_p_aggregate`*

An aggregated projection of use-based-rent obligation across a contract term, the use-based-rent counterpart to VirtualPRPAggregate.

Source: `data-fields/small-miscellaneous-entities.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 14 |
| Catalogued fields | 13 (13 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 2 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### A computed projection, not a table

**Observed.** Virtual records are calculated at read time rather than stored. They have no primary key to join on and never appear in Firm scope — a tenant cannot customise a projection the platform generates. Treat this as the shape of a query result, not as a table to migrate.

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ContractID` | Contract | Contract ID | Global |  | [Contract](Contract.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (4)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeBillingFrequencyID` | Billing Frequency | Dropdown (Frequency Code) | Global |  | Frequency Code |
| `CodeExpenseGroupID` | Expense Group | Dropdown (Expense Group Code) | Global |  | Expense Group Code |
| `CodeExpenseTypeID` | Expense Type | Dropdown (Expense Type Code) | Global |  | Expense Type Code |
| `CodeUseRentModelTypeID` | Model Type | Dropdown (Use Rent Model Type Code) | Global |  | Use Rent Model Type Code |

### Money (4)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CurrentRentDue` | Current Use Based Rent | Currency | Global |  |  |
| `CurrentRentObligation` | Total Use Based Rent | Currency | Global |  |  |
| `CurrentRentPaid` | Current Use Based Rent Paid | Currency | Global |  |  |
| `NetUseBasedRentDue` | Net Use Based Rent Due | Currency | Global |  |  |

### Dates & timestamps (4)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `PeriodBeginDate` | Period Begin Date | Date | Global |  |  |
| `PeriodEndDate` | Period End Date | Date | Global |  |  |
| `RentYearBeginDate` | Rent Year Begin Date | Date | Global |  |  |
| `RentYearEndDate` | Rent Year End Date | Date | Global |  |  |
