# ACC-R-032 — Present value of a period payment

*Lease Accounting & Payments · Observed*

**discount the cash payment from the period it is made back to the accounting begin date.**

Discount the payment from its own period back to the accounting begin date. The compounding convention is not documented.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | period row generation |
| What it reads | `SLPeriod.PeriodCashAmount`, the discount rate (ACC-R-001…003), the period offset |
| What it computes | discount the cash payment from the period it is made back to the accounting begin date |
| What it writes | `SLPeriod.PVOfPeriodCashAmount` |

## The wording it rests on

> The Present Value of a future cash payment in today's valuation. This value is discounted to present value from the period that the payment will be made.

## What it constrains

[SLPeriod](../entities/SLPeriod.md), [Asset](../entities/Asset.md)

Columns named: `SLPeriod.PeriodCashAmount`, `SLPeriod.PVOfPeriodCashAmount`, `Asset.CodeCompoundingFrequencyID`

## Rules it cites

[ACC-R-001](ACC-R-001.md)

## Confidence

Observed for the intent — "The Present Value of a future cash payment in today's valuation. This value is discounted to present value from the period that the payment will be made."; Inferred for the compounding convention. `Asset.CodeCompoundingFrequencyID` exists but is undocumented

---

Source: `docs/modules/accounting/rules.md`
