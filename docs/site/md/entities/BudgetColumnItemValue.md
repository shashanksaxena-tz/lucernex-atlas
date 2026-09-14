# BudgetColumnItemValue

*19 fields · module: Budgeting, Cost Tracking & Bidding — OUT OF SCOPE · Postgres: `none exported`*

The actual dollar value at the intersection of a BudgetLineItem and a BudgetColumn — the individual cell in the budget grid. 20 fields under Budget and Statics.

Source: `data-fields/budget-column-item-value.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 19 |
| Catalogued fields | 20 (20 global, 0 firm) |
| Physical tables | 0 |
| Referenced by | 0 keys from 0 record types |
| Points at | 2 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Out of scope by decision

**Observed.** Its module is excluded from the rebuild. It stays in the census so impact analysis through the relationship graph is never silently wrong at the boundary, but nothing here is being built.

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeBudgetChangeReasonID` | Change Reason | Dropdown (Budget Change Reason Code) | Global |  | Budget Change Reason Code |
| `CodeBudgetValueUnitsID` | Units | Dropdown (Budget Value Units Code) | Global |  | Budget Value Units Code |

### Money (3)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `GrandTotalValue` | Total Value | Currency | Global |  |  |
| `ItemValue` | Item Value | Currency | Global |  |  |
| `UnitCost` | Unit Cost | Currency | Global |  |  |

### Quantities (3)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BudgetColumnItemValueID` | Budget Column Item Value RecID | Number | Global |  |  |
| `Quantity` |  | Number | Global |  |  |
| `RawItemValue` | Raw Item Value | Number | Global |  |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BypassLockedCheck` | Bypass Locked Check? | Boolean | Global |  |  |

### Text & notes (6)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BudgetColumnID` | Budget Column | Text | Global | yes |  |
| `BudgetColumnItemValueName` | Budget Column Item Value Name | Text | Global |  |  |
| `BudgetLineItemID` | Budget Line Item | Text | Global | yes |  |
| `BudgetOptionID` | Budget Option | Text | Global |  |  |
| `Description` |  | Text | Global |  |  |
| `LineItemCode` | Line Item Code | Text | Global |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Budget Column ClientID | Text | Global | yes |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
