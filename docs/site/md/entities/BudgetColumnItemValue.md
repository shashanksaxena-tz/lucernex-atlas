# BudgetColumnItemValue

*19 fields · module: Budgeting, Cost Tracking & Bidding — OUT OF SCOPE · Postgres: `none exported`*

The actual dollar value at the intersection of a BudgetLineItem and a BudgetColumn — the individual cell in the budget grid. 20 fields under Budget and Statics.

Source: `data-fields/budget-column-item-value.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 19 |
| Fields with a vendor definition | 18 of 19 inventoried |
| Physical tables | — |
| Replication database | — |
| Catalogued fields | 20 (20 global, 0 firm) |
| Physical tables | 0 |
| Referenced by | 0 keys from 0 record types |
| Points at | 2 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### 18 fields carry a vendor definition

**Observed.** 18 of this record's 19 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one source in the corpus that explains fields rather than listing them.

### 3 fields marked required

**Observed.** The inventory marks 3 of this record's fields Required. Across the whole inventory that is 606 fields, which independently corroborates the 603 the corpus had derived from the Data Fields catalogue — two sources, arrived at separately, agreeing to within three.

### 19 fields excluded from extraction

**Observed.** Observed of the loader. The inventory marks 19 of this record's fields as not extracted to PostgreSQL, so the replication target creates no column for them. They still exist in Lx; anything reading the replica rather than the product will not see them.

### Out of scope by decision

**Observed.** Its module is excluded from the rebuild. It stays in the census so impact analysis through the relationship graph is never silently wrong at the boundary, but nothing here is being built.

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ProjectEntityID` |  |  | Entity ID | — |  | not extracted | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeBudgetChangeReasonID` | Change Reason | Select the reason for the change from this field. | Dropdown (Budget Change Reason Code) | Global |  | not extracted | Budget Change Reason Code |
| `CodeBudgetValueUnitsID` | Units | Select the line item unit type from this field. An example unit type could be "pieces", "boxes", or "pallets". | Dropdown (Budget Value Units Code) | Global |  | not extracted | Budget Value Units Code |

### Money (3)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `GrandTotalValue` | Total Value | This field sums the values of the budget line items in a budget group. | Currency | Global |  | not extracted |  |
| `ItemValue` | Item Value | Enter the total value of this line item in this field. | Currency | Global |  | not extracted |  |
| `UnitCost` | Unit Cost | Enter the unit cost of the line item in this field. | Currency | Global |  | not extracted |  |

### Quantities (3)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BudgetColumnItemValueID` | Budget Column Item Value RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | not extracted |  |
| `Quantity` |  | Enter the quantity of the line item in this field. | Number | Global |  | not extracted |  |
| `RawItemValue` | Raw Item Value | When this value is defined, you do not need to enter quantity or unit cost. | Number | Global |  | not extracted |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BypassLockedCheck` | Bypass Locked Check? | This is an internal field that is used to bypass the Locked flag when deleting a budget column. | Boolean | Global |  | not extracted |  |

### Text & notes (6)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BudgetColumnID` | Budget Column | The ID of the budget type. | Text | Global | yes | not extracted |  |
| `BudgetColumnItemValueName` | Budget Column Item Value Name | The line item name. | Text | Global |  | not extracted |  |
| `BudgetLineItemID` | Budget Line Item | The ID of the budget line item. | Text | Global | yes | not extracted |  |
| `BudgetOptionID` | Budget Option | The ID of the budget option. | Text | Global |  | not extracted |  |
| `Description` |  | Write a description of the record. | Text | Global |  | not extracted |  |
| `LineItemCode` | Line Item Code | The line item code. | Text | Global |  | not extracted |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Budget Column ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | not extracted |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | not extracted | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | not extracted |  |
