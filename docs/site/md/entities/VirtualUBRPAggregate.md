# VirtualUBRPAggregate

*14 fields · module: Variable Rent (Percentage / Use-Based) & Sales · Postgres: `virtual_u_b_r_p_aggregate`*

An aggregated projection of use-based-rent obligation across a contract term, the use-based-rent counterpart to VirtualPRPAggregate.

Source: `data-fields/small-miscellaneous-entities.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 14 |
| Fields with a vendor definition | 13 of 14 inventoried |
| Physical tables | `virtual_u_b_r_p_aggregate` |
| Replication database | `lxr_drp_bbw` |
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

### Lands in virtual_u_b_r_p_aggregate

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 13 fields carry a vendor definition

**Observed.** 13 of this record's 14 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one source in the corpus that explains fields rather than listing them.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global |  | `virtual_u_b_r_p_aggregate.ContractID · TEXT` | [Contract](Contract.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `virtual_u_b_r_p_aggregate.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (4)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeBillingFrequencyID` | Billing Frequency | The payment frequency for the use based rent record. The Payment Frequency field controls how often you can generate rent or generate payments. | Dropdown (Frequency Code) | Global |  | `virtual_u_b_r_p_aggregate.CodeBillingFrequencyID · TEXT` | Frequency Code |
| `CodeExpenseGroupID` | Expense Group | The Expense Group field allows you to associate your record with a pre-configured expense group. Expense groups are used to categorize expense types. | Dropdown (Expense Group Code) | Global |  | `virtual_u_b_r_p_aggregate.CodeExpenseGroupID · TEXT` | Expense Group Code |
| `CodeExpenseTypeID` | Expense Type | The Expense Type field allows you to associate your record with a pre-configured expense type. Expense Types are used to associate records with lease accounting schedules, AP export numbers, expense accrual accounts, percentage rent accrual accounts, and real estate tax accounts. | Dropdown (Expense Type Code) | Global |  | `virtual_u_b_r_p_aggregate.CodeExpenseTypeID · TEXT` | Expense Type Code |
| `CodeUseRentModelTypeID` | Model Type | The model type for the use based rent record. When the Count Based model type is selected, the rent will be calculated as the Unit Resource Rent Rate * the Number of Units Used by the Lessee. When the Share Based model type is selected, the rent will be calculated as the Shared Resource Rent Rate * the Lessee Share. | Dropdown (Use Rent Model Type Code) | Global |  | `virtual_u_b_r_p_aggregate.CodeUseRentModelTypeID · TEXT` | Use Rent Model Type Code |

### Money (4)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CurrentRentDue` | Current Use Based Rent | The total rent due for the last period before any forecasts come into play. Equal to the rent due minus the rent paid. | Currency | Global |  | `virtual_u_b_r_p_aggregate.CurrentRentDue · TEXT` |  |
| `CurrentRentObligation` | Total Use Based Rent | The total rent obligation for the last period before any forecasts come into play. This value is used to calculate the current rent due. | Currency | Global |  | `virtual_u_b_r_p_aggregate.CurrentRentObligation · TEXT` |  |
| `CurrentRentPaid` | Current Use Based Rent Paid | The total rent paid for this use based rent period. This field looks at all periods, regardless of if they are Actual or Forecast. This field is used to calculate the current rent due. | Currency | Global |  | `virtual_u_b_r_p_aggregate.CurrentRentPaid · TEXT` |  |
| `NetUseBasedRentDue` | Net Use Based Rent Due | Net usage rent due for the last period before any forecasts come into play (Current Rent Due - Offset). | Currency | Global |  | `virtual_u_b_r_p_aggregate.NetUseBasedRentDue · TEXT` |  |

### Dates & timestamps (4)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `PeriodBeginDate` | Period Begin Date | The period begin date. | Date | Global |  | `virtual_u_b_r_p_aggregate.PeriodBeginDate · TEXT` |  |
| `PeriodEndDate` | Period End Date | The period end date. | Date | Global |  | `virtual_u_b_r_p_aggregate.PeriodEndDate · TEXT` |  |
| `RentYearBeginDate` | Rent Year Begin Date | The begin date of this Rent Year. This date may not be same as the period begin date if you are in alternate rent. | Date | Global |  | `virtual_u_b_r_p_aggregate.RentYearBeginDate · TEXT` |  |
| `RentYearEndDate` | Rent Year End Date | The end date of this Rent Year. This date may not be same as the period end date if you are in alternate rent. | Date | Global |  | `virtual_u_b_r_p_aggregate.RentYearEndDate · TEXT` |  |
