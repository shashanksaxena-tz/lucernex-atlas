# CodeIFRS16Schedule

*24 fields · module: Lease Accounting & Payments · Postgres: `code_i_f_r_s16_schedule`*

The IFRS 16 counterpart to CodeASC842Schedule, structurally identical (same export-account slot pattern) but for the international standard. 21 Global fields under Contract.

Source: `data-fields/code-ifrs16-schedule.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 24 |
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

## Fields

### Flags (2)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DontAmortizeAssetValue` | Don't Amortize Asset Value | Boolean | Global |  |  |
| `Inactive` |  | Boolean | — |  |  |

### Text & notes (22)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ActualLongName` |  | Text | — |  |  |
| `ExportAcct10Number` | Export Account #10 | Text | Global |  |  |
| `ExportAcct11Number` | Export Account #11 | Text | Global |  |  |
| `ExportAcct12Number` | Export Account #12 | Text | Global |  |  |
| `ExportAcct13Number` | Export Account #13 | Text | Global |  |  |
| `ExportAcct14Number` | Export Account #14 | Text | Global |  |  |
| `ExportAcct15Number` | Export Account #15 | Text | Global |  |  |
| `ExportAcct16Number` | Export Account #16 | Text | Global |  |  |
| `ExportAcct17Number` | Export Account #17 | Text | Global |  |  |
| `ExportAcct18Number` | Export Account #18 | Text | Global |  |  |
| `ExportAcct19Number` | Export Account #19 | Text | Global |  |  |
| `ExportAcct1Number` | Export Account #1 | Text | Global |  |  |
| `ExportAcct20Number` | Export Account #20 | Text | Global |  |  |
| `ExportAcct2Number` | Export Account #2 | Text | Global |  |  |
| `ExportAcct3Number` | Export Account #3 | Text | Global |  |  |
| `ExportAcct4Number` | Export Account #4 | Text | Global |  |  |
| `ExportAcct5Number` | Export Account #5 | Text | Global |  |  |
| `ExportAcct6Number` | Export Account #6 | Text | Global |  |  |
| `ExportAcct7Number` | Export Account #7 | Text | Global |  |  |
| `ExportAcct8Number` | Export Account #8 | Text | Global |  |  |
| `ExportAcct9Number` | Export Account #9 | Text | Global |  |  |
| `ShortName` |  | Text | — |  |  |
