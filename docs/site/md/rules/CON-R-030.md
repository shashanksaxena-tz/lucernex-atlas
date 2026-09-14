# CON-R-030 — 3. Recurring expense: setup and schedule

*Contracts & Leases · Observed*

**Authoring a recurring expense through the wizard: the wizard's start date, end date, starting amount, amount type and escalation settings materialise ExpenseSetup + ExpenseEscalation + the full ExpenseSchedule in one action.**

Authoring a recurring expense through the wizard: the wizard's start date, end date, starting amount, amount type and escalation settings materialise ExpenseSetup + ExpenseEscalation + the full ExpenseSchedule in one action.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Authoring a recurring expense |
| Stated as | `ExpenseSetupWizard_StartDate`, `_EndDate`, `_StartingAmout`, `_AmountType`, `_TypeOfEscalation`, `_EscalateEvery`, `_EscalateAmountRate`, `GenerateExpenseSetup` |
| Stated as | The wizard materialises `ExpenseSetup` + `ExpenseEscalation` + the full `ExpenseSchedule` |
| Stated as | Clause + schedule |
| Stated as | Observed |

## What it constrains

[ExpenseSetup](../entities/ExpenseSetup.md), [ExpenseEscalation](../entities/ExpenseEscalation.md), [ExpenseSchedule](../entities/ExpenseSchedule.md)

---

Source: `docs/modules/contracts/rules.md`
