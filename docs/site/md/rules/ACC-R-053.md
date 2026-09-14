# ACC-R-053 — Accrual transaction tax handling

*Lease Accounting & Payments · Observed*

**- `TaxesIncludedFlag = false` ⇒ `TotalAmount = PeriodAmount + Σ TaxAmountN`, `TotalAmount` read-only. - `TaxesIncludedFlag = true` ⇒ `PeriodAmount` becomes disabled, the system subtracts the tax amounts from the period amount, and `TotalAmount` becomes editable.**

Both branches are stated verbatim by the vendor.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | `AccrualTransaction` entry |
| What it reads | `PeriodAmount`, `TaxAmount1` … `TaxAmount4`, `TaxesIncludedFlag` |
| The test | - `TaxesIncludedFlag = false` ⇒ `TotalAmount = PeriodAmount + Σ TaxAmountN`, `TotalAmount` read-only. - `TaxesIncludedFlag = true` ⇒ `PeriodAmount` becomes disabled, the system subtracts the tax amounts from the period amount, and `TotalAmount` becomes editable |

## What it constrains

[AccrualTransaction](../entities/AccrualTransaction.md)

## Confidence

Observed — both branches are stated in the definitions of `TaxesIncludedFlag`, `PeriodAmount` and `TotalAmount`

---

Source: `docs/modules/accounting/rules.md`
