# CodeAssetCategory

*6 fields · module: Assets, Equipment & Maintenance · Postgres: `code_asset_category`*

Master asset-category reference record — GL number and sub-account mapping for a category of equipment/assets.

Source: `data-fields/code-reference-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 6 |
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

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [AST-R-007](../rules/AST-R-007.md) | Input: `Asset.CodeAssetCategoryID` (labelled Maintenance Category) and `Asset.CodeDesc_CodeAssetCategoryID` (labelled Account #), both FKs to `CodeAssetCategory`. Effect: The same code table serves a maintenance-classification role and a GL | Observed |
| [AST-R-008](../rules/AST-R-008.md) | Input: `CodeAssetCategory.GLNumber`, `.SubAccount`, `.DNEAmount`, alongside `ShortName`/ `ActualLongName`/`Inactive`. Effect: Selecting an asset category also selects a GL account, a sub-account, and a per-category spending ceiling (`DNEAmo | Observed |

## Fields

### Money (1)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DNEAmount` | DNE Amount | Currency | Global |  |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Inactive` |  | Boolean | — |  |  |

### Text & notes (4)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ActualLongName` |  | Text | — |  |  |
| `GLNumber` | GL Number | Text | Global |  |  |
| `ShortName` |  | Text | — |  |  |
| `SubAccount` | Sub Account | Text | Global |  |  |
