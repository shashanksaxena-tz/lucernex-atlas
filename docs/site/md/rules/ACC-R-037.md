# ACC-R-037 — Straight-line expense and deferral

*Lease Accounting & Payments · Observed*

**``` PeriodExpenseAmount[n] = total cash rent straight-lined over the schedule life PeriodDeferredAmount[n] = PeriodCashAmount[n] − PeriodExpenseAmount[n] CumulativeDeferredBalance[n] = Σ(1..n) PeriodDeferredAmount ```.**

Expense is the total cash spread evenly; deferral is cash minus expense; the cumulative balance is the running sum.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | period row generation |
| What it computes | ``` PeriodExpenseAmount[n] = total cash rent straight-lined over the schedule life PeriodDeferredAmount[n] = PeriodCashAmount[n] − PeriodExpenseAmount[n] CumulativeDeferredBalance[n] = Σ(1..n) PeriodDeferredAmount ``` |

## The wording it rests on

> The cash rent straight lined over the life of the schedule

## Confidence

Observed — "The cash rent straight lined over the life of the schedule"; "The difference between the period cash rent and straight line rent expense"; "The sum of the deferred rent from the beginning of the schedule to the current period." ⚠ The sign of `PeriodDeferredAmount` (cash − expense, or expense − cash) is not stated; the wording implies cash − expense

---

Source: `docs/modules/accounting/rules.md`
