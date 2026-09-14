# CON-R-118 — 9. Payment lifecycle

*Contracts & Leases · Observed*

**Money is received: there is no FK or link table from PaymentReceipt to PaymentTransaction — only allocated/unallocated totals on each side.**

Money is received: there is no FK or link table from PaymentReceipt to PaymentTransaction — only allocated/unallocated totals on each side.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Money is received |
| Stated as | `PaymentReceipt.ReceivedAmount`, `.AmountAllocated`, `.AmountNotAllocated`, `RECONCILE_RECEIPT` |
| Stated as | There is no FK or link table from `PaymentReceipt` to `PaymentTransaction` — only allocated/unallocated totals on each side |
| Stated as | Receipt allocation |
| Stated as | Observed (by absence) — schema gap |

## What it constrains

[PaymentReceipt](../entities/PaymentReceipt.md), [PaymentTransaction](../entities/PaymentTransaction.md)

Columns named: `PaymentReceipt.ReceivedAmount`

---

Source: `docs/modules/contracts/rules.md`
