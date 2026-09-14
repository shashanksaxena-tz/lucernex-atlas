# CodeAssetCategory

*6 fields · module: Assets, Equipment & Maintenance · Postgres: `code_asset_category`*

Master asset-category reference record — GL number and sub-account mapping for a category of equipment/assets.

Source: `data-fields/code-reference-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 6 |
| Fields with a vendor definition | 3 of 6 inventoried |
| Physical tables | `code_asset_category` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 3 (3 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 0 other records |
| Tenancy position | firm_global |
| Rules that name it | 2 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### No typed relationships either way

**Derived.** Nothing holds a typed foreign key into this record and it declares none out. Either it is joined by a soft reference the census cannot see, or it is genuinely standalone — worth settling before anything is built on it.

### Lands in code_asset_category

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 3 fields carry a vendor definition

**Observed.** 3 of this record's 6 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [AST-R-007](../rules/AST-R-007.md) | Input: `Asset.CodeAssetCategoryID` (labelled Maintenance Category) and `Asset.CodeDesc_CodeAssetCategoryID` (labelled Account #), both FKs to `CodeAssetCategory`. Effect: The same code table serves a maintenance-classification role and a GL | Observed |
| [AST-R-008](../rules/AST-R-008.md) | Input: `CodeAssetCategory.GLNumber`, `.SubAccount`, `.DNEAmount`, alongside `ShortName`/ `ActualLongName`/`Inactive`. Effect: Selecting an asset category also selects a GL account, a sub-account, and a per-category spending ceiling (`DNEAmo | Observed |

## Fields

### Money (1)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DNEAmount` | DNE Amount | Enter the do not exceed amount in this field. | Currency | Global |  | `code_asset_category.DNEAmount · TEXT` |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Inactive` |  |  | Boolean | — |  | `code_asset_category.Inactive · TEXT` |  |

### Text & notes (4)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActualLongName` | Description |  | Text | — |  | `code_asset_category.ActualLongName · TEXT` |  |
| `GLNumber` | GL Number | Enter the general ledger number associated with this category in this field. | Text | Global |  | `code_asset_category.GLNumber · TEXT` |  |
| `ShortName` | Name |  | Text | — |  | `code_asset_category.ShortName · TEXT` |  |
| `SubAccount` | Sub Account | Enter the sub account number associated with this category in this field. | Text | Global |  | `code_asset_category.SubAccount · TEXT` |  |
