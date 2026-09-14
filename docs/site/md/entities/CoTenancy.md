# CoTenancy

*27 fields · module: Contracts & Leases · Postgres: `co_tenancy`*

A co-tenancy clause (rent reduction if an anchor tenant vacates) — anchor name, co-tenancy amount/area, and begin date, one of the seven Firm-editable Contract subgroups per 005. 26 Global fields under Contract.

Source: `data-fields/co-tenancy.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 27 |
| Catalogued fields | 26 (26 global, 0 firm) |
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

### Coded values (drop-downs) (4)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeBuildingAreaUnitID` | Building Area Unit | Dropdown (Building Area Unit Code) | Global |  | Building Area Unit Code |
| `CodeCoTenancyGroupID` | Co Tenancy Group | Dropdown (Co Tenancy Group Code) | Global |  | Co Tenancy Group Code |
| `CodeCoTenancyTypeID` | Co Tenancy Type | Dropdown (Co Tenancy Type Code) | Global |  | Co Tenancy Type Code |
| `CodeCurrencyTypeID` | Currency Type | Dropdown (Currency Type Code) | Global |  | Currency Type Code |

### Money (3)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CoTenancyAmount` | Co Tenancy Amount | Currency | Global |  |  |
| `RentReductionAmount` | Rent Reduction Amount | Currency | Global |  |  |
| `Sales` |  | Currency | Global |  |  |

### Rates & percentages (2)

Percentage inputs and computed rates.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `OccupancyPercentage` | Occupancy Percentage | Percentage | Global |  |  |
| `RentReductionPercent` | Rent Reduction Percent | Percentage | Global |  |  |

### Quantities (2)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CoTenancyArea` | Co Tenancy Area | Number | Global |  |  |
| `CoTenancyID` | Co Tenancy RecID | Number | Global |  |  |

### Dates & timestamps (4)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BeginDate` | Begin Date | Date | Global |  |  |
| `EffectiveDate` | Effective Date | Date | Global |  |  |
| `EndDate` | End Date | Date | Global |  |  |
| `RemodelDate` | Remodel Date | Date | Global |  |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `HasRightToTerminate` | Has Right To Terminate? | Boolean | Global |  |  |

### Text & notes (4)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CoTenancyName` | Anchor Name | Text | Global |  |  |
| `Notes` |  | Text | Global |  |  |
| `RentAccount` | Rent Account | Text | Global |  |  |
| `Section` |  | Text | Global |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Co Tenancy ClientID | Text | Global | yes |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
