# CON-R-036 — 3. Recurring expense: setup and schedule

*Contracts & Leases · Observed*

**A partial first or last period occurs: CodeProrationMethodID governs it, and the schedule's own FirstPaymentAmount / LastPaymentAmount carry the prorated stub amounts.**

A partial first or last period occurs: CodeProrationMethodID governs it, and the schedule's own FirstPaymentAmount / LastPaymentAmount carry the prorated stub amounts.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | A partial first or last period |
| Stated as | `CodeProrationMethodID`, `ExpenseSchedule.FirstPaymentAmount`, `LastPaymentAmount` |
| Stated as | Stub periods carry their own prorated amounts |
| Stated as | Stub amounts |
| Stated as | Observed |

## What it constrains

[ExpenseSchedule](../entities/ExpenseSchedule.md)

Columns named: `ExpenseSchedule.FirstPaymentAmount`

---

Source: `docs/modules/contracts/rules.md`
