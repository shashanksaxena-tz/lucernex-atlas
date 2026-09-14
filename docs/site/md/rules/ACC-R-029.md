# ACC-R-029 — GL account denormalization

*Lease Accounting & Payments · Derived*

**copied verbatim onto `SLPeriod.ExportAcct1Number` … `ExportAcct20Number`.**

On creating each period row, the schedule type's twenty account numbers are copied onto it unchanged.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | `SLPeriod` row creation |
| What it reads | the governing schedule type's `ExportAcct1Number` … `ExportAcct20Number` |
| What it writes | copied verbatim onto `SLPeriod.ExportAcct1Number` … `ExportAcct20Number` |

## The wording it rests on

> Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System

## What it constrains

[SLPeriod](../entities/SLPeriod.md)

Columns named: `SLPeriod.ExportAcct1Number`

## Confidence

Derived — the column sets are identical in name and count on the code tables and on `SLPeriod`, and both carry the same vendor definition ("Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System")

---

Source: `docs/modules/accounting/rules.md`
