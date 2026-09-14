# CodeSLSchedule

*24 fields · module: Lease Accounting & Payments · Postgres: `code_s_l_schedule`*

The pre-ASC-842/pre-IFRS-16 straight-line schedule template, structurally identical to the two standard-specific schedules — Lx evidently kept the legacy SL schedule type alongside both new-standard schedule types rather than replacing it. 21 Global fields under Contract.

Source: `data-fields/code-sl-schedule.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 24 |
| Fields with a vendor definition | 21 of 24 inventoried |
| Physical tables | `code_s_l_schedule` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 21 (21 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 0 other records |
| Tenancy position | firm_global |
| Rules that name it | 0 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### No typed relationships either way

**Derived.** Nothing holds a typed foreign key into this record and it declares none out. Either it is joined by a soft reference the census cannot see, or it is genuinely standalone — worth settling before anything is built on it.

### Lands in code_s_l_schedule

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 21 fields carry a vendor definition

**Observed.** 21 of this record's 24 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Fields

### Flags (2)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DontAmortizeAssetValue` | Don't Amortize Asset Value | When selected, the system will not amortize the asset to zero in the lease accounting schedule. See the Amortization of the Asset in Contracts article in the Lx Online Help for more information. | Boolean | Global |  | `code_s_l_schedule.DontAmortizeAssetValue · TEXT` |  |
| `Inactive` |  |  | Boolean | — |  | `code_s_l_schedule.Inactive · TEXT` |  |

### Text & notes (22)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActualLongName` | Description |  | Text | — |  | `code_s_l_schedule.ActualLongName · TEXT` |  |
| `ExportAcct10Number` | Export Account #10 | Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `code_s_l_schedule.ExportAcct10Number · TEXT` |  |
| `ExportAcct11Number` | Export Account #11 | Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `code_s_l_schedule.ExportAcct11Number · TEXT` |  |
| `ExportAcct12Number` | Export Account #12 | Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `code_s_l_schedule.ExportAcct12Number · TEXT` |  |
| `ExportAcct13Number` | Export Account #13 | Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `code_s_l_schedule.ExportAcct13Number · TEXT` |  |
| `ExportAcct14Number` | Export Account #14 | Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `code_s_l_schedule.ExportAcct14Number · TEXT` |  |
| `ExportAcct15Number` | Export Account #15 | Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `code_s_l_schedule.ExportAcct15Number · TEXT` |  |
| `ExportAcct16Number` | Export Account #16 | Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `code_s_l_schedule.ExportAcct16Number · TEXT` |  |
| `ExportAcct17Number` | Export Account #17 | Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `code_s_l_schedule.ExportAcct17Number · TEXT` |  |
| `ExportAcct18Number` | Export Account #18 | Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `code_s_l_schedule.ExportAcct18Number · TEXT` |  |
| `ExportAcct19Number` | Export Account #19 | Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `code_s_l_schedule.ExportAcct19Number · TEXT` |  |
| `ExportAcct1Number` | Export Account #1 | Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `code_s_l_schedule.ExportAcct1Number · TEXT` |  |
| `ExportAcct20Number` | Export Account #20 | Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `code_s_l_schedule.ExportAcct20Number · TEXT` |  |
| `ExportAcct2Number` | Export Account #2 | Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `code_s_l_schedule.ExportAcct2Number · TEXT` |  |
| `ExportAcct3Number` | Export Account #3 | Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `code_s_l_schedule.ExportAcct3Number · TEXT` |  |
| `ExportAcct4Number` | Export Account #4 | Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `code_s_l_schedule.ExportAcct4Number · TEXT` |  |
| `ExportAcct5Number` | Export Account #5 | Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `code_s_l_schedule.ExportAcct5Number · TEXT` |  |
| `ExportAcct6Number` | Export Account #6 | Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `code_s_l_schedule.ExportAcct6Number · TEXT` |  |
| `ExportAcct7Number` | Export Account #7 | Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `code_s_l_schedule.ExportAcct7Number · TEXT` |  |
| `ExportAcct8Number` | Export Account #8 | Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `code_s_l_schedule.ExportAcct8Number · TEXT` |  |
| `ExportAcct9Number` | Export Account #9 | Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `code_s_l_schedule.ExportAcct9Number · TEXT` |  |
| `ShortName` | Name |  | Text | — |  | `code_s_l_schedule.ShortName · TEXT` |  |
