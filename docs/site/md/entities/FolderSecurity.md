# FolderSecurity

*3 fields · module: Documents, Folders & Correspondence · Postgres: `folder_security`*

Not covered by the Data Fields catalogue: this record type appears in the 223-object census but has no row in the catalogue of 6,158 configurable fields, so nothing in the corpus explains it in the vendor's own words. What is known is structural — 3 declared fields, filed under Documents, Folders & Correspondence, 0 foreign keys pointing at it.

Source: `_lucernex_objects_summary.txt`

## At a glance

|  | Value |
|---|---|
| Fields declared | 3 |
| Catalogued fields | not in the catalogue |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 0 other records |
| Tenancy position | firm_global |
| Rules that name it | 1 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### No typed relationships either way

**Derived.** Nothing holds a typed foreign key into this record and it declares none out. Either it is joined by a soft reference the census cannot see, or it is genuinely standalone — worth settling before anything is built on it.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [DOC-R-006](../rules/DOC-R-006.md) | Input: `FolderSecurity` carries no `ProjectEntityID` — only `FolderID`, `CodeUserClassID`, and `CodeFolderSecurityTypeID`. Effect: Folder-level access control is scoped entirely through the folder it secures, not separately to any entity. | Observed |

## Fields

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeFolderSecurityTypeID` |  | Dropdown (Security Type Code) | — |  | Security Type Code |
| `CodeUserClassID` |  | Dropdown (User Class) | — |  | User Class |

### Text & notes (1)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `FolderID` |  | Text | — |  |  |
