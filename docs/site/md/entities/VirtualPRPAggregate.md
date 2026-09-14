# VirtualPRPAggregate

*16 fields · module: Variable Rent (Percentage / Use-Based) & Sales · Postgres: `virtual_p_r_p_aggregate`*

An aggregated percentage-rent obligation projection across a contract's full term — current offset amount and current percentage rent obligation/paid. 15 Global fields under Contract.

Source: `data-fields/virtual-prp-aggregate.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 16 |
| Fields with a vendor definition | 15 of 16 inventoried |
| Physical tables | `virtual_p_r_p_aggregate` |
| Replication database | `lxr_drp_bbw` |
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

### Lands in virtual_p_r_p_aggregate

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 15 fields carry a vendor definition

**Observed.** 15 of this record's 16 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-061](../rules/CON-R-061.md) | Offsets are applied: VariableRentOffset and ScheduledOffset, applied via APPLY_OFFSETS, reduce the rent-year obligation. | Observed |
| [CON-R-062](../rules/CON-R-062.md) | Rent already paid is credited: PRPRentDue = PRPTotalRent − SalesPeriodRentPaid − offsets. | Inferred |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global |  | `virtual_p_r_p_aggregate.ContractID · TEXT` | [Contract](Contract.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `virtual_p_r_p_aggregate.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (4)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeBillingFrequencyID` | Billing Frequency | The payment frequency for the percentage rent record. The Payment Frequency field controls how often you can generate rent or generate payments. | Dropdown (Frequency Code) | Global |  | `virtual_p_r_p_aggregate.CodeBillingFrequencyID · TEXT` | Frequency Code |
| `CodeExpenseGroupID` | Expense Group | The Expense Group field allows you to associate your record with a pre-configured expense group. Expense groups are used to categorize expense types. | Dropdown (Expense Group Code) | Global |  | `virtual_p_r_p_aggregate.CodeExpenseGroupID · TEXT` | Expense Group Code |
| `CodeExpenseTypeID` | Expense Type | The Expense Type field allows you to associate your record with a pre-configured expense type. Expense Types are used to associate records with lease accounting schedules, AP export numbers, expense accrual accounts, percentage rent accrual accounts, and real estate tax accounts. | Dropdown (Expense Type Code) | Global |  | `virtual_p_r_p_aggregate.CodeExpenseTypeID · TEXT` | Expense Type Code |
| `CodePercentageRentTypeID` | Percentage Rent Type | The percentage rent calculation model. | Dropdown (Percentage Rent Type Code) | Global |  | `virtual_p_r_p_aggregate.CodePercentageRentTypeID · TEXT` | Percentage Rent Type Code |

### Money (5)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CurrentRentDue` | Current Percentage Rent | The total rent due for the last period before any forecasts come into play. This field is calculated as Rent Obligation - Rent Paid. | Currency | Global |  | `virtual_p_r_p_aggregate.CurrentRentDue · TEXT` |  |
| `CurrentRentObligation` | Current Percentage Rent Obligation | The total rent obligation for the last period before any forecasts come into play. This value is used in calculating the rent due. | Currency | Global |  | `virtual_p_r_p_aggregate.CurrentRentObligation · TEXT` |  |
| `CurrentRentPaid` | Current Percentage Rent Paid | The total rent paid for this percentage rent period. This field looks at all periods, regardless of if they are Actual or Forecast. This value is used in calculating the rent due. | Currency | Global |  | `virtual_p_r_p_aggregate.CurrentRentPaid · TEXT` |  |
| `NetSalesRentDue` | Net Percentage Rent Due | The net sales rent due for the last period before any forecasts come into play. This value is calculated as Current Rent Due - Offset. | Currency | Global |  | `virtual_p_r_p_aggregate.NetSalesRentDue · TEXT` |  |
| `VariableRentOffsetAmount` | Current Offset Amount | The Variable Rent Offset for the given percentage rent period. Offset caps are reflected in the returned value. | Currency | Global |  | `virtual_p_r_p_aggregate.VariableRentOffsetAmount · TEXT` |  |

### Dates & timestamps (4)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `PeriodBeginDate` | Period Begin Date | The begin date of the period. | Date | Global |  | `virtual_p_r_p_aggregate.PeriodBeginDate · TEXT` |  |
| `PeriodEndDate` | Period End Date | The end date of the period. | Date | Global |  | `virtual_p_r_p_aggregate.PeriodEndDate · TEXT` |  |
| `RentYearBeginDate` | Rent Year Begin Date | The begin date of the rental year. | Date | Global |  | `virtual_p_r_p_aggregate.RentYearBeginDate · TEXT` |  |
| `RentYearEndDate` | Rent Year End Date | The end date of the rental year. | Date | Global |  | `virtual_p_r_p_aggregate.RentYearEndDate · TEXT` |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `RentYearHasAltRent` | Rent Year Has Alternate Rent? | Indicates whether some or all of the rent year is affected by Alt Rent. | Boolean | Global |  | `virtual_p_r_p_aggregate.RentYearHasAltRent · TEXT` |  |
