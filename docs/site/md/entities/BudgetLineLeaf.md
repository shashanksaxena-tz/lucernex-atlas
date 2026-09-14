# BudgetLineLeaf

*26 fields · module: Budgeting, Cost Tracking & Bidding — OUT OF SCOPE · Postgres: `budget_line_leaf`*

Not covered by the Data Fields catalogue: this record type appears in the 223-object census but has no row in the catalogue of 6,158 configurable fields, so no document describes the record as a whole. What is known is structural — 26 declared fields, filed under Budgeting, Cost Tracking & Bidding — OUT OF SCOPE, 0 foreign keys pointing at it. Its fields are documented even though the record is not: 25 of its 26 inventoried fields carry a definition written by the vendor. Open the field groups below and read them — that is the best account of this record available.

Source: `data-model/pg/bbw-field-inventory.csv`, `_lucernex_objects_summary.txt`

## At a glance

|  | Value |
|---|---|
| Fields declared | 26 |
| Fields with a vendor definition | 25 of 26 inventoried |
| Physical tables | `budget_line_leaf` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | not in the catalogue |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 3 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in budget_line_leaf

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 25 fields carry a vendor definition

**Observed.** 25 of this record's 26 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one source in the corpus that explains fields rather than listing them.

### 5 fields marked required

**Observed.** The inventory marks 5 of this record's fields Required. Across the whole inventory that is 606 fields, which independently corroborates the 603 the corpus had derived from the Data Fields catalogue — two sources, arrived at separately, agreeing to within three.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

### Out of scope by decision

**Observed.** Its module is excluded from the rebuild. It stays in the census so impact analysis through the relationship graph is never silently wrong at the boundary, but nothing here is being built.

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BudgetTemplateID` | Budget Template ID | If there is a budget template associated with this entity, The foreign key of the budget template. | Template ID | — |  | `budget_line_leaf.BudgetTemplateID · TEXT` | [BudgetTemplate](BudgetTemplate.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `budget_line_leaf.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeCSIID` | CSI Code | Select the CSI code from this field. CSI divisions are part of the MasterFormat standard created by the Construction Specifications Institute and Construction Specifications Canada. | Dropdown (CSI Code) | — |  | `budget_line_leaf.CodeCSIID · TEXT` | CSI Code |

### Money (1)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DefaultAmount` | Default Amount | Enter the default amount for this line item in this field. | Currency | — |  | `budget_line_leaf.DefaultAmount · TEXT` |  |

### Rates & percentages (1)

Percentage inputs and computed rates.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `OverrunPercent` | Overrun Percent | The overrun percent is the value of your budget compared to the overrun percentage set for the Project Budget Status Alert setting on the Alerts page. If you do not want to use this functionality, enter 99 in this field and do not select the Alert Enabled check box. | Percentage | — |  | `budget_line_leaf.OverrunPercent · TEXT` |  |

### Quantities (4)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ComputedSequenceNumber` | Computed Sequence Number | The sequence number of the record. Each new record receives the next number in the sequence. | Number | — |  | `budget_line_leaf.ComputedSequenceNumber · TEXT` |  |
| `IsBudgetLineItemGroup` | Is Budget Line Item Group | This field returns TRUE if this budget line item is a group. | Number | — | yes | `budget_line_leaf.IsBudgetLineItemGroup · TEXT` |  |
| `ParentID` | Parent ID | The ID of the parent line item group. | Number | — |  | `budget_line_leaf.ParentID · TEXT` |  |
| `PreviousID` | Previous ID | The ID of the previous budget line item. | Number | — |  | `budget_line_leaf.PreviousID · TEXT` |  |

### Flags (3)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AlertEnabled` | Alert Enabled | Select the Alert Enabled check box if you want to have an alert sent if your budget runs over the percentage set for the Project Budget Status Alert setting on the Alerts page. | Boolean | — | yes | `budget_line_leaf.AlertEnabled · TEXT` |  |
| `IsGroup` | Is Group? | If this value is set to true, this record is a group. | Boolean | — |  | `budget_line_leaf.IsGroup · TEXT` |  |
| `IsOrdered` | Is Ordered? | This field does not impact any current functionality. | Boolean | — |  | `budget_line_leaf.IsOrdered · TEXT` |  |

### Text & notes (11)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BudgetLineItemID` | Budget Line Item RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Text | — |  | `budget_line_leaf.BudgetLineItemID · VARCHAR(64) NOT NULL` |  |
| `BudgetLineItemName` | Budget Line Item Name | Enter the budget line item name in this field. | Text | — | yes | `budget_line_leaf.BudgetLineItemName · TEXT` |  |
| `CategoryCode` | Category Code | Enter the category code for the budget line item in this field. | Text | — |  | `budget_line_leaf.CategoryCode · TEXT` |  |
| `DefinedField1` | Defined Field #1 | This field is a reserved space for client fields. | Text | — |  | `budget_line_leaf.DefinedField1 · TEXT` |  |
| `DefinedField2` | Defined Field #2 | This field is a reserved space for client fields. | Text | — |  | `budget_line_leaf.DefinedField2 · TEXT` |  |
| `Description` |  | Write a description of the record. | Text | — |  | `budget_line_leaf.Description · TEXT` |  |
| `LineItemCode` | Line Item Code | Enter the line item code in this field. Line item codes can include numbers, letters, and special characters. The line item code usually corresponds to codes in your ERP system. If you are integrating with your ERP system, ensure that your line item codes have a line-to-line match with the budget in your ERP system. If you are not planning to integrate with your ERP system, establish a numbering convention for your line item codes. This is important because it simplifies the process of reporting on a line item, because each line item will have a unique code that is easily determined. | Text | — | yes | `budget_line_leaf.LineItemCode · TEXT` |  |
| `OrderRecordName` | Order Record Name | This field does not impact any current functionality. | Text | — |  | `budget_line_leaf.OrderRecordName · TEXT` |  |
| `OrderRecordType` | Order Record Type | This field does not impact any current functionality. | Text | — |  | `budget_line_leaf.OrderRecordType · TEXT` |  |
| `ParentBudgetLineItemID` | Parent Budget Line Item | The ID of the budget line item that is this record's parent. | Text | — |  | `budget_line_leaf.ParentBudgetLineItemID · TEXT` |  |
| `PreviousBudgetLineItemID` | Previous Budget Line Item | The ID of the previous budget line item. | Text | — |  | `budget_line_leaf.PreviousBudgetLineItemID · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Budget Line Item ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | — | yes | `budget_line_leaf.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | — |  | `budget_line_leaf.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | — |  | `budget_line_leaf.ModifiedDate · TEXT` |  |
