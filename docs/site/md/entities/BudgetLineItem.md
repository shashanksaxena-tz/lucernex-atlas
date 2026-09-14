# BudgetLineItem

*26 fields · module: Budgeting, Cost Tracking & Bidding — OUT OF SCOPE · Postgres: `budget_line_item`*

One line item within a budget template — alert threshold, category code, and template linkage; the line-item layer beneath BudgetColumn/BudgetColumnType. 25 Global fields under Budget.

Source: `data-fields/budget-line-item.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 26 |
| Catalogued fields | 25 (25 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 3 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Out of scope by decision

**Observed.** Its module is excluded from the rebuild. It stays in the census so impact analysis through the relationship graph is never silently wrong at the boundary, but nothing here is being built.

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BudgetTemplateID` | Budget Template ID | Template ID | Global |  | [BudgetTemplate](BudgetTemplate.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeCSIID` | CSI Code | Dropdown (CSI Code) | Global |  | CSI Code |

### Money (1)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DefaultAmount` | Default Amount | Currency | Global |  |  |

### Rates & percentages (1)

Percentage inputs and computed rates.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `OverrunPercent` | Overrun Percent | Percentage | Global |  |  |

### Quantities (4)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ComputedSequenceNumber` | Computed Sequence Number | Number | Global |  |  |
| `IsBudgetLineItemGroup` | Is Budget Line Item Group | Number | Global | yes |  |
| `ParentID` | Parent ID | Number | Global |  |  |
| `PreviousID` | Previous ID | Number | Global |  |  |

### Flags (3)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AlertEnabled` | Alert Enabled | Boolean | Global | yes |  |
| `IsGroup` | Is Group? | Boolean | Global |  |  |
| `IsOrdered` | Is Ordered? | Boolean | Global |  |  |

### Text & notes (11)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BudgetLineItemID` | Budget Line Item RecID | Text | Global |  |  |
| `BudgetLineItemName` | Budget Line Item Name | Text | Global | yes |  |
| `CategoryCode` | Category Code | Text | Global |  |  |
| `DefinedField1` | Defined Field #1 | Text | Global |  |  |
| `DefinedField2` | Defined Field #2 | Text | Global |  |  |
| `Description` |  | Text | Global |  |  |
| `LineItemCode` | Line Item Code | Text | Global | yes |  |
| `OrderRecordName` | Order Record Name | Text | Global |  |  |
| `OrderRecordType` | Order Record Type | Text | Global |  |  |
| `ParentBudgetLineItemID` | Parent Budget Line Item | Text | Global |  |  |
| `PreviousBudgetLineItemID` | Previous Budget Line Item | Text | Global |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Budget Line Item ClientID | Text | Global | yes |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
