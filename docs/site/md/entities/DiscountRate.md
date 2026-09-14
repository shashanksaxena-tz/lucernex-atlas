# DiscountRate

*16 fields · module: Lease Accounting & Payments · Postgres: `discount_rate`*

A named discount-rate configuration (by country and accounting method) used in NPV/present-value calculations across ContractFinancialTest and ProFormaBudget. 16 Global fields under Company Items.

Source: `data-fields/discount-rate.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 16 |
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

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [ACC-R-001](../rules/ACC-R-001.md) | resolve Portfolio-level rate first; if none exists, Firm-level rate. Do not read the contract-level rate | Observed |
| [ACC-R-004](../rules/ACC-R-004.md) | a blank `CodeAccountingMethodID` matches both Finance and Operating. `MinSchedMons`/`MaxSchedMons` bound the schedule length in months for which the rate applies | Observed |
| [CON-R-022](../rules/CON-R-022.md) | Determining the discount rate: look up DiscountRate by accounting method + contract use + geography + a min/max-scheduled-months band, and stamp it onto Contract.DiscountRate. | Derived |

## Fields

### Relationships (foreign keys) (4)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CountryID` | Country | Country, State, County ID | Global |  | [StateProvinceCountry](StateProvinceCountry.md) |
| `CountryIDList` | Country List | Country, State, County ID | Global |  | [StateProvinceCountry](StateProvinceCountry.md) |
| `ProgramID` | Program | Portfolio ID | Global |  | [Program](Program.md) |
| `StateProvinceIDList` | State Province | Country, State, County ID | Global |  | [StateProvinceCountry](StateProvinceCountry.md) |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeAccountingMethodID` | Accounting Method | Dropdown (Accounting Method Code) | Global |  | Accounting Method Code |
| `CodeContractUseID` | Contract Use | Dropdown (Contract Use Code) | Global |  | Contract Use Code |

### Rates & percentages (1)

Percentage inputs and computed rates.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DiscountRate` | Discount Rate | Percentage | Global | yes |  |

### Quantities (2)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `MaxSchedMons` | Maximum Schedule Length (months) | Number | Global | yes |  |
| `MinSchedMons` | Minimum Schedule Length (months) | Number | Global | yes |  |

### Dates & timestamps (1)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `EffectiveThroughDate` | Effective End Date | Date | Global | yes |  |

### Text & notes (1)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Notes` |  | Text | Global |  |  |

### Audit & record keeping (5)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` | Rev Number | Number | Global |  |  |
