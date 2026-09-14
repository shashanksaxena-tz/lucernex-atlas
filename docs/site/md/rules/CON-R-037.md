# CON-R-037 — 3. Recurring expense: setup and schedule

*Contracts & Leases · Observed*

**CalculateScheduleAmounts is invoked: the schedule's amounts are recomputed in place from the clause, its escalation and its tax configuration.**

CalculateScheduleAmounts is invoked: the schedule's amounts are recomputed in place from the clause, its escalation and its tax configuration.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | `CalculateScheduleAmounts` is invoked |
| Stated as | The `ExpenseSetup` + its escalation + tax config |
| Stated as | Recomputes the schedule's amounts in place |
| Stated as | Updated L1 rows |
| Stated as | Observed |

## What it constrains

[ExpenseSetup](../entities/ExpenseSetup.md)

---

Source: `docs/modules/contracts/rules.md`
