# ACC-R-039 — Accumulated amortization recurrence

*Lease Accounting & Payments · Observed*

**``` CumulativeAssetAmortExpense[1] = PeriodAssetAmortizationExpense[1] CumulativeAssetAmortExpense[n] = PeriodAssetAmortizationExpense[n] + CumulativeAssetAmortExpense[n−1] ```.**

A simple running total, stated verbatim by the vendor.

## Stated for a rule engine

|  |  |
|---|---|
| What it computes | ``` CumulativeAssetAmortExpense[1] = PeriodAssetAmortizationExpense[1] CumulativeAssetAmortExpense[n] = PeriodAssetAmortizationExpense[n] + CumulativeAssetAmortExpense[n−1] ``` |

## Confidence

Observed, stated verbatim

---

Source: `docs/modules/accounting/rules.md`
