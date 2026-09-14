# CLRExtensionPart

*24 fields · module: Configuration, Layouts, Forms & Reporting · Postgres: `c_l_r_extension_part`*

Not covered by the Data Fields catalogue: this record type appears in the 223-object census but has no row in the catalogue of 6,158 configurable fields, so no document describes the record as a whole. What is known is structural — 24 declared fields, filed under Configuration, Layouts, Forms & Reporting, 0 foreign keys pointing at it. Its fields are documented even though the record is not: 22 of its 24 inventoried fields carry a definition written by the vendor. Open the field groups below and read them — that is the best account of this record available.

Source: `data-model/pg/bbw-field-inventory.csv`, `_lucernex_objects_summary.txt`

## At a glance

|  | Value |
|---|---|
| Fields declared | 24 |
| Fields with a vendor definition | 22 of 24 inventoried |
| Physical tables | `c_l_r_extension_part` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | not in the catalogue |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 5 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in c_l_r_extension_part

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 22 fields carry a vendor definition

**Observed.** 22 of this record's 24 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Fields

### Relationships (foreign keys) (4)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AssetID` | Equipment | This field allows you to select an asset to associate with a custom list item. | Equipment ID | — |  | `c_l_r_extension_part.AssetID · TEXT` | [Asset](Asset.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `c_l_r_extension_part.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |
| `ReportGroupAvailableFieldID` | List Association Field | The reporting field that is associated with the object. | Report/Form Field ID | — | yes | `c_l_r_extension_part.ReportGroupAvailableFieldID · TEXT` | [ReportGroupAvailableField](ReportGroupAvailableField.md) |
| `SalesVendorID` | Sales Vendor | This field allows you to select a sales vendor from a list. | Employer ID | — |  | `c_l_r_extension_part.SalesVendorID · TEXT` | [Employer](Employer.md) |

### Soft references (3)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `PartID` | Part | This field allows you to select a part record. | Part | — |  | `c_l_r_extension_part.PartID · TEXT` |  |
| `PartPackageID` | Part Package | This field allows you to select a part package record. | Parts Package | — |  | `c_l_r_extension_part.PartPackageID · TEXT` |  |
| `RelatedPEID` | Related Facility | This field allows you to select a related entity. | Entity | — |  | `c_l_r_extension_part.RelatedPEID · TEXT` |  |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeSQLTableID` | Client List Row Type | If this field's value is Part, this is a part custom list. If this field's value is Standard, it is a standard custom list. | Dropdown (SQL Table Code) | — | yes | `c_l_r_extension_part.CodeSQLTableID · TEXT` | SQL Table Code |

### Money (7)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BudgetColumnItemValueID` | Budget | This field allows you to select a budget type to associate with the custom list. | Currency | — |  | `c_l_r_extension_part.BudgetColumnItemValueID · TEXT` |  |
| `CostPerPart` | Cost Per Part | This field allows you to enter the unit cost per part. | Currency | — |  | `c_l_r_extension_part.CostPerPart · TEXT` |  |
| `SubValue` | Budget Cost | This field is used to add a Budget Cost column to the custom list. A currency value entered in this field will impact the budget column this field is associated with. | Currency | — |  | `c_l_r_extension_part.SubValue · TEXT` |  |
| `SubValue2` | Budget Cost 2 | This field is used to add an additional Budget Cost column to the custom list. A currency value entered in this field will impact the budget column this field is associated with. | Currency | — |  | `c_l_r_extension_part.SubValue2 · TEXT` |  |
| `SubValue3` | Budget Cost 3 | This field is used to add an additional Budget Cost column to the custom list. A currency value entered in this field will impact the budget column this field is associated with. | Currency | — |  | `c_l_r_extension_part.SubValue3 · TEXT` |  |
| `SubValue4` | Budget Cost 4 | This field is used to add an additional Budget Cost column to the custom list. A currency value entered in this field will impact the budget column this field is associated with. | Currency | — |  | `c_l_r_extension_part.SubValue4 · TEXT` |  |
| `SubValue5` | Budget Cost 5 | This field is used to add an additional Budget Cost column to the custom list. A currency value entered in this field will impact the budget column this field is associated with. | Currency | — |  | `c_l_r_extension_part.SubValue5 · TEXT` |  |

### Quantities (5)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ClientListRowID` | Client List Row RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | — |  | `c_l_r_extension_part.ClientListRowID · TEXT` |  |
| `ObjectID` | Object RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | — | yes | `c_l_r_extension_part.ObjectID · TEXT` |  |
| `PartPackageQuantity` | Part Package Quantity | This field allows you to enter a quantity of part packages. | Number | — |  | `c_l_r_extension_part.PartPackageQuantity · TEXT` |  |
| `PartQuantity` | Part Quantity | This field allows you to enter a quantity of parts. | Number | — |  | `c_l_r_extension_part.PartQuantity · TEXT` |  |
| `PurchaseOrderLineSeqNum` | Purchase Order Line Sequence Number |  | Number | — |  | `c_l_r_extension_part.PurchaseOrderLineSeqNum · TEXT` |  |

### Text & notes (1)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BudgetLineItemID` | Budget Line Item | This field is related to a future enhancement. | Text | — |  | `c_l_r_extension_part.BudgetLineItemID · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Client List Row ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | — | yes | `c_l_r_extension_part.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | — |  | `c_l_r_extension_part.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | — |  | `c_l_r_extension_part.ModifiedDate · TEXT` |  |
