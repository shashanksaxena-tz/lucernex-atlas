# VirtualPRPAggregate

*16 fields · module: Variable Rent (Percentage / Use-Based) & Sales · Postgres: `virtual_p_r_p_aggregate`*

An aggregated percentage-rent obligation projection across a contract's full term — current offset amount and current percentage rent obligation/paid. 15 Global fields under Contract.

Source: `data-fields/virtual-prp-aggregate.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 16 |
| Catalogued fields | 15 (15 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 2 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 2 |

## What to know before rebuilding this

### A computed projection, not a table

**Observed.** Virtual records are calculated at read time rather than stored. They have no primary key to join on and never appear in Firm scope — a tenant cannot customise a projection the platform generates. Treat this as the shape of a query result, not as a table to migrate.

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-061](../rules/CON-R-061.md) | Offsets are applied: VariableRentOffset and ScheduledOffset, applied via APPLY_OFFSETS, reduce the rent-year obligation. | Observed |
| [CON-R-062](../rules/CON-R-062.md) | Rent already paid is credited: PRPRentDue = PRPTotalRent − SalesPeriodRentPaid − offsets. | Inferred |

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
| `CodePercentageRentTypeID` | Percentage Rent Type | Dropdown (Percentage Rent Type Code) | Global |  | Percentage Rent Type Code |

### Money (5)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CurrentRentDue` | Current Percentage Rent | Currency | Global |  |  |
| `CurrentRentObligation` | Current Percentage Rent Obligation | Currency | Global |  |  |
| `CurrentRentPaid` | Current Percentage Rent Paid | Currency | Global |  |  |
| `NetSalesRentDue` | Net Percentage Rent Due | Currency | Global |  |  |
| `VariableRentOffsetAmount` | Current Offset Amount | Currency | Global |  |  |

### Dates & timestamps (4)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `PeriodBeginDate` | Period Begin Date | Date | Global |  |  |
| `PeriodEndDate` | Period End Date | Date | Global |  |  |
| `RentYearBeginDate` | Rent Year Begin Date | Date | Global |  |  |
| `RentYearEndDate` | Rent Year End Date | Date | Global |  |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `RentYearHasAltRent` | Rent Year Has Alternate Rent? | Boolean | Global |  |  |
