# SalesExclusionCap

*23 fields · module: Variable Rent (Percentage / Use-Based) & Sales · Postgres: `sales_exclusion_cap`*

A cap limiting how much sales can be excluded from percentage-rent calculation (e.g., online/catalog sales exclusions) — cap amount/percent and begin date. 22 Global fields under Contract.

Source: `data-fields/sales-exclusion-cap.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 23 |
| Catalogued fields | 22 (22 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 1 keys from 1 record types |
| Points at | 4 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 3 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-052](../rules/CON-R-052.md) | An exclusion applies: rawExcluded = salesOfType × SalesExclusion.ExclusionRate. | Derived |
| [CON-R-053](../rules/CON-R-053.md) | Exclusions share a cap group (ExclusionGroupCapID): PRPGrossExcludedAmount sums the raw excluded amounts within the group, before the cap. | Derived |
| [CON-R-054](../rules/CON-R-054.md) | A cap group is evaluated: PRPComputedCapAmount = min(CapAmount, PRPGrossSalesAmount × CapPercent) — the effective cap, whichever binds first. | Inferred |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ContractID` | Contract | Contract ID | Global | yes | [Contract](Contract.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (3)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeCurrencyTypeID` | Currency Type | Dropdown (Currency Type Code) | Global |  | Currency Type Code |
| `CodeExclusionCapID` | Exclusion Cap | Dropdown (Exclusion Cap Code) | Global | yes | Exclusion Cap Code |
| `CodeSalesGroupID` | Sales Group | Dropdown (Sales Group) | Global |  | Sales Group |

### Money (1)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CapAmount` | Cap Amount | Currency | Global |  |  |

### Rates & percentages (1)

Percentage inputs and computed rates.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CapPercent` | Cap Percent | Percentage | Global |  |  |

### Quantities (7)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `PRPComputedCapAmount` | PRP Computed Cap Amount | Number | Global |  |  |
| `PRPExcessExcludedAmount` | PRP Excess Excluded Amount | Number | Global |  |  |
| `PRPGrossExcludedAmount` | PRP Gross Excluded Amount | Number | Global |  |  |
| `PRPGrossSalesAmount` | PRP Gross Sales Amount | Number | Global |  |  |
| `PRPNetExcludedAmount` | PRP Net Excluded Amount | Number | Global |  |  |
| `SPExcludedAmount` | SP Excluded Amount | Number | Global |  |  |
| `SalesExclusionCapID` | Exclusion Cap RecID | Number | Global |  |  |

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

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Exclusion Cap ClientID | Text | Global | yes |  |
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` | Rev Number | Number | Global |  |  |

## What points here (1 keys)

| Record type | Via column |
|---|---|
| [SalesExclusion](SalesExclusion.md) | `ExclusionGroupCapID` |
