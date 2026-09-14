# CON-R-116 — 9. Payment lifecycle

*Contracts & Leases · Observed*

**A match has a difference: VarianceAmount and VarianceReason are stored on the join itself, alongside ReconciliationStatus.**

A match has a difference: VarianceAmount and VarianceReason are stored on the join itself, alongside ReconciliationStatus.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | A match has a difference |
| Stated as | `LinkLandlordInvPaymentTxn.VarianceAmount`, `.VarianceReason`, `.ReconciliationStatus` |
| Stated as | The variance and its explanation are stored on the join |
| Stated as | Explained variance |
| Stated as | Observed |

## What it constrains

[LinkLandlordInvPaymentTxn](../entities/LinkLandlordInvPaymentTxn.md)

Columns named: `LinkLandlordInvPaymentTxn.VarianceAmount`

---

Source: `docs/modules/contracts/rules.md`
