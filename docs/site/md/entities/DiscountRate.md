# DiscountRate

*16 fields · module: Lease Accounting & Payments · Postgres: `discount_rate`*

A named discount-rate configuration (by country and accounting method) used in NPV/present-value calculations across ContractFinancialTest and ProFormaBudget. 16 Global fields under Company Items.

Source: `data-fields/discount-rate.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 16 |
| Fields with a vendor definition | 16 of 16 inventoried |
| Physical tables | `discount_rate` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 16 (16 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 6 other records |
| Tenancy position | firm_global |
| Rules that name it | 3 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### Empty in both captured tenants

**Observed.** This table holds zero rows in both American Freight and BBW while the ASC 842 engine runs and produces schedules. Where the discount rate actually comes from is unresolved, and it blocks the accounting rebuild.

### Lands in discount_rate

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 16 fields carry a vendor definition

**Observed.** 16 of this record's 16 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: the captures agree

**Observed.** Over the 16 fields both the Data Fields catalogue and the field inventory contain, the two agree on every one. 4 are marked required.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [ACC-R-001](../rules/ACC-R-001.md) | resolve Portfolio-level rate first; if none exists, Firm-level rate. Do not read the contract-level rate | Observed |
| [ACC-R-004](../rules/ACC-R-004.md) | a blank `CodeAccountingMethodID` matches both Finance and Operating. `MinSchedMons`/`MaxSchedMons` bound the schedule length in months for which the rate applies | Observed |
| [CON-R-022](../rules/CON-R-022.md) | Determining the discount rate: look up DiscountRate by accounting method + contract use + geography + a min/max-scheduled-months band, and stamp it onto Contract.DiscountRate. | Derived |

## Fields

### Relationships (foreign keys) (4)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CountryID` | Country | The country this discount rate applies to, if there is only one country. | Country, State, County ID | Global |  | `discount_rate.CountryID · TEXT` | [StateProvinceCountry](StateProvinceCountry.md) |
| `CountryIDList` | Country List | The countries this discount rate applies to, if there are multiple countries. | Country, State, County ID | Global |  | `discount_rate.CountryIDList · TEXT` | [StateProvinceCountry](StateProvinceCountry.md) |
| `ProgramID` | Program | Select the portfolio this discount rate applies to. | Portfolio ID | Global |  | `discount_rate.ProgramID · TEXT` | [Program](Program.md) |
| `StateProvinceIDList` | State Province | The states or provinces this discount rate applies to. | Country, State, County ID | Global |  | `discount_rate.StateProvinceIDList · TEXT` | [StateProvinceCountry](StateProvinceCountry.md) |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeAccountingMethodID` | Accounting Method | Select the accounting method this discount rate should apply to. If you leave the field blank, the discount rate will apply to both Finance and Operating. | Dropdown (Accounting Method Code) | Global |  | `discount_rate.CodeAccountingMethodID · TEXT` | Accounting Method Code |
| `CodeContractUseID` | Contract Use | Select the use type of the lease from this field. | Dropdown (Contract Use Code) | Global |  | `discount_rate.CodeContractUseID · TEXT` | Contract Use Code |

### Rates & percentages (1)

Percentage inputs and computed rates.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DiscountRate` | Discount Rate | Enter the discount rate in this field. | Percentage | Global | yes | `discount_rate.DiscountRate · TEXT` |  |

### Quantities (2)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `MaxSchedMons` | Maximum Schedule Length (months) | Enter the maximum term length in months. | Number | Global | yes | `discount_rate.MaxSchedMons · TEXT` |  |
| `MinSchedMons` | Minimum Schedule Length (months) | Enter the minimum term length in months. | Number | Global | yes | `discount_rate.MinSchedMons · TEXT` |  |

### Dates & timestamps (1)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `EffectiveThroughDate` | Effective End Date | Enter the last date that the discount rate is effective in this field. | Date | Global | yes | `discount_rate.EffectiveThroughDate · TEXT` |  |

### Text & notes (1)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Notes` |  | Add any notes about the record. | Text | Global |  | `discount_rate.Notes · TEXT` |  |

### Audit & record keeping (5)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `discount_rate.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `discount_rate.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `discount_rate.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `discount_rate.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | Global |  | `discount_rate.RevNumber · TEXT` |  |
