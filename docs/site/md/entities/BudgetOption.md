# BudgetOption

*13 fields · module: Budgeting, Cost Tracking & Bidding — OUT OF SCOPE · Postgres: `budget_option`*

A selectable alternative version of a budget-column entity type.

Source: `data-fields/budget-ancillary-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 13 |
| Catalogued fields | 12 (12 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 4 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Out of scope by decision

**Observed.** Its module is excluded from the rebuild. It stays in the census so impact analysis through the relationship graph is never silently wrong at the boundary, but nothing here is being built.

## Fields

### Relationships (foreign keys) (3)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BudgetOptionTemplateID` | Budget Option Template | Entity ID | Global | yes | [ProjectEntity](ProjectEntity.md) |
| `CreatedByMemberID` | Created By Member | Member ID | Global | yes | [Member](Member.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Quantities (2)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BudgetOptionID` | Budget Option RecID | Number | Global |  |  |
| `BudgetOptionTemplatePEID` | Budget Option Template PEID | Number | Global |  |  |

### Text & notes (4)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BotEntityType` | Bot Entity Type | Text | Global | yes |  |
| `BudgetColumnID` | Budget Column | Text | Global | yes |  |
| `BudgetOptionName` | Budget Option Name | Text | Global |  |  |
| `InitializedFromBudgetColumnID` | Initialized From Budget Column | Text | Global |  |  |

### Audit & record keeping (4)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Budget Option ClientID | Text | Global | yes |  |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
