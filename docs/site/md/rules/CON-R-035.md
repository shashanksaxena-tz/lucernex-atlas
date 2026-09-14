# CON-R-035 — 3. Recurring expense: setup and schedule

*Contracts & Leases · Derived*

**The clause is flagged IsDailyRent: the period amount is the daily rate multiplied by the day count in the period, rather than a fixed period amount.**

The clause is flagged IsDailyRent: the period amount is the daily rate multiplied by the day count in the period, rather than a fixed period amount.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | `ExpenseSetup.IsDailyRent = true` |
| Stated as | `ExpenseSchedule.DailyRentRate`, period day count |
| Stated as | Amount = daily rate × days in period, rather than a fixed period amount |
| Stated as | Period amount |
| Stated as | Derived |

## What it constrains

[ExpenseSchedule](../entities/ExpenseSchedule.md)

Columns named: `ExpenseSchedule.DailyRentRate`

---

Source: `docs/modules/contracts/rules.md`
