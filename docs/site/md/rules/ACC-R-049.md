# ACC-R-049 — Final asset amount / residual carve-out

*Lease Accounting & Payments · Observed*

**these four fields are "only made available on Finance contracts". `FinalAssetDate` defaults to the schedule end date; a later date amortizes beyond the schedule end.**

Only available on finance contracts. The final-asset date defaults to the schedule end date; a later date amortises beyond it.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | schedule generation on a Finance contract |
| What it reads | `SLSummary.FinalAssetAmount`, `.FinalAssetAllocPercent`, `.FinalAssetDate`, `.SLRemainingAssetBalance` |
| The test | these four fields are "only made available on Finance contracts". `FinalAssetDate` defaults to the schedule end date; a later date amortizes beyond the schedule end |
| What it writes | the asset balance remaining after the schedule end date |

## The wording it rests on

> only made available on Finance contracts

## What it constrains

[SLSummary](../entities/SLSummary.md)

Columns named: `SLSummary.FinalAssetAmount`

## Confidence

Observed for the Finance-only restriction and the `FinalAssetDate` default. ⚠ `SLRemainingAssetBalance` is magnitude-typed: 0–100 defaults to Percentage, ≥ 100.01 defaults to Currency, and the user can override — so the stored number does not carry its unit. --- ## H. Approval, posting, and the accrual sub-engine

---

Source: `docs/modules/accounting/rules.md`
