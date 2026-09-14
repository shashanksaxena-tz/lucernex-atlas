# CON-R-117 — 9. Payment lifecycle

*Contracts & Leases · Observed*

**A payment is fully matched: PaymentTransaction.IsInvoiceReconciled is set when the three-way match completes.**

A payment is fully matched: PaymentTransaction.IsInvoiceReconciled is set when the three-way match completes.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | A payment is fully matched |
| Stated as | `PaymentTransaction.IsInvoiceReconciled` |
| Stated as | Set when the three-way match completes |
| Stated as | Reconciled flag |
| Stated as | Observed |

## What it constrains

[PaymentTransaction](../entities/PaymentTransaction.md)

Columns named: `PaymentTransaction.IsInvoiceReconciled`

---

Source: `docs/modules/contracts/rules.md`
