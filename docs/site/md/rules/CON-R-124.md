# CON-R-124 — 9. Payment lifecycle

*Contracts & Leases · Observed*

**Bulk payments are imported: PaymentTransactionFullImport mirrors PaymentTransaction's 118 fields with no backing table of its own.**

Bulk payments are imported: PaymentTransactionFullImport mirrors PaymentTransaction's 118 fields with no backing table of its own.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Bulk payments are imported |
| Stated as | `PaymentTransactionFullImport` (118 fields, no PG table) |
| Stated as | A field-for-field staging mirror of `PaymentTransaction` |
| Stated as | Import buffer |
| Stated as | Observed |

## What it constrains

[PaymentTransactionFullImport](../entities/PaymentTransactionFullImport.md), [PaymentTransaction](../entities/PaymentTransaction.md)

---

Source: `docs/modules/contracts/rules.md`
