# ACC-R-041 — Short-term / long-term split

*Lease Accounting & Payments · Observed*

**``` Forward12MonthAssetChange[n] = Σ asset amortization, periods n+1 … n+12 Forward12MonthLiabilityChange[n] = Σ liability amortization, periods n+1 … n+12 ShortTermRentExpense[n] = Σ rent expense, next 12 months LongTermRentExpense[n] = Σ rent expense beyond 12 months LongTermLiability[n] =….**

Five formulas covering the twelve-month-forward changes and the long-term remainder.

## Stated for a rule engine

|  |  |
|---|---|
| What it computes | ``` Forward12MonthAssetChange[n] = Σ asset amortization, periods n+1 … n+12 Forward12MonthLiabilityChange[n] = Σ liability amortization, periods n+1 … n+12 ShortTermRentExpense[n] = Σ rent expense, next 12 months LongTermRentExpense[n] = Σ rent expense beyond 12 months LongTermLiability[n] = LiabilityAmount[n] − shortTermLiability[n] ``` |

## The wording it rests on

> the change in the asset balance from period n + 1 to period n + 12

## What it constrains

[SLSummary](../entities/SLSummary.md), [SLPeriod](../entities/SLPeriod.md)

Columns named: `SLSummary.Forward12MonthAssetChange`, `SLPeriod.Forward12MonthAssetChange`

## Confidence

Observed for all five. ⚠ Note `SLSummary.Forward12MonthAssetChange` is defined differently from `SLPeriod.Forward12MonthAssetChange`: the summary version is "the change in the asset balance from period n + 1 to period n + 12", the period version is "the sum of the asset amortization for the next 12 months." Whether these are the same number expressed two ways is an open question

---

Source: `docs/modules/accounting/rules.md`
