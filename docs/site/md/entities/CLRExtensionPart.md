# CLRExtensionPart

*24 fields · module: Configuration, Layouts, Forms & Reporting · Postgres: `c_l_r_extension_part`*

Not covered by the Data Fields catalogue: this record type appears in the 223-object census but has no row in the catalogue of 6,158 configurable fields, so nothing in the corpus explains it in the vendor's own words. What is known is structural — 24 declared fields, filed under Configuration, Layouts, Forms & Reporting, 0 foreign keys pointing at it.

Source: `_lucernex_objects_summary.txt`

## At a glance

|  | Value |
|---|---|
| Fields declared | 24 |
| Catalogued fields | not in the catalogue |
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
| `AssetID` |  | Equipment ID | — |  | [Asset](Asset.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |
| `ReportGroupAvailableFieldID` |  | Report/Form Field ID | — |  | [ReportGroupAvailableField](ReportGroupAvailableField.md) |
| `SalesVendorID` |  | Employer ID | — |  | [Employer](Employer.md) |

### Soft references (3)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `PartID` |  | Part | — |  |  |
| `PartPackageID` |  | Parts Package | — |  |  |
| `RelatedPEID` |  | Entity | — |  |  |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeSQLTableID` |  | Dropdown (SQL Table Code) | — |  | SQL Table Code |

### Money (7)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BudgetColumnItemValueID` |  | Currency | — |  |  |
| `CostPerPart` |  | Currency | — |  |  |
| `SubValue` |  | Currency | — |  |  |
| `SubValue2` |  | Currency | — |  |  |
| `SubValue3` |  | Currency | — |  |  |
| `SubValue4` |  | Currency | — |  |  |
| `SubValue5` |  | Currency | — |  |  |

### Quantities (5)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ClientListRowID` |  | Number | — |  |  |
| `ObjectID` |  | Number | — |  |  |
| `PartPackageQuantity` |  | Number | — |  |  |
| `PartQuantity` |  | Number | — |  |  |
| `PurchaseOrderLineSeqNum` |  | Number | — |  |  |

### Text & notes (1)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BudgetLineItemID` |  | Text | — |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` |  | Text | — |  |  |
| `ModifiedByID` |  | Member ID | — |  | [Member](Member.md) |
| `ModifiedDate` |  | Time | — |  |  |
