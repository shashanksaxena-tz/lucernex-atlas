# CON-R-040 — 4. Escalations

*Contracts & Leases · Derived*

**An escalation step falls due: a step occurs every EscalationPeriod × CodeFrequencyID units inside the clause's BeginDate..EndDate window.**

An escalation step falls due: a step occurs every EscalationPeriod × CodeFrequencyID units inside the clause's BeginDate..EndDate window.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | An escalation step falls due |
| Stated as | `ExpenseEscalation.EscalationPeriod`, `CodeFrequencyID`, `BeginDate`, `EndDate` |
| Stated as | A step occurs every `EscalationPeriod` × frequency units inside the window |
| Stated as | Step dates |
| Stated as | Derived |

## What it constrains

[ExpenseEscalation](../entities/ExpenseEscalation.md)

Columns named: `ExpenseEscalation.EscalationPeriod`

---

Source: `docs/modules/contracts/rules.md`
