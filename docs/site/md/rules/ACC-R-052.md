# ACC-R-052 — Accrual amount derivation

*Lease Accounting & Payments · Observed*

**entering any one of annual amount / period amount / accrual rate auto-populates the other two plus `FirstPaymentAmount` and `LastPaymentAmount`. Rate-based entry requires `RentableArea` to be populated — "If you are not going to use rentable area, do not enter 0. Leave this field blank.".**

Entering any one of the annual amount, period amount or accrual rate auto-fills the other two plus the first and last payment amounts.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | `ExpenseAccrualSchedule` entry |
| What it reads | `AnnualAmount` or `PeriodAmount` or `AccrualRate`; `ExpenseAccrualSetup.RentableArea`; `DailyAccrualRate` when `ExpenseAccrualSetup.IsDailyRent = true` |
| What it computes | entering any one of annual amount / period amount / accrual rate auto-populates the other two plus `FirstPaymentAmount` and `LastPaymentAmount`. Rate-based entry requires `RentableArea` to be populated — "If you are not going to use rentable area, do not enter 0. Leave this field blank." |
| What it writes | `AnnualAmount`, `PeriodAmount`, `AccrualRate`, `FirstPaymentAmount`, `LastPaymentAmount` |

## The wording it rests on

> If you are not going to use rentable area, do not enter 0. Leave this field blank.

## What it constrains

[ExpenseAccrualSchedule](../entities/ExpenseAccrualSchedule.md), [ExpenseAccrualSetup](../entities/ExpenseAccrualSetup.md)

Columns named: `ExpenseAccrualSetup.RentableArea`

## Confidence

Observed — "Enter the annual amount of your accrual in this field. The system will automatically calculate the period amount, the accrual rate, the first period amount, and the last period amount." and the symmetric statement on `PeriodAmount`. ⚠ The blank-vs-zero distinction on `RentableArea` is a real behavioural difference, not a UI nicety

---

Source: `docs/modules/accounting/rules.md`
