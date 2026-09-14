# CON-R-109 — 9. Payment lifecycle

*Contracts & Leases · Observed*

**An expense type is chosen: CodeExpenseTypeID selects both the GL account set and the accounting treatment (CodeASC842ScheduleID, CodeIFRS16ScheduleID, CodeSLScheduleID) in one action.**

An expense type is chosen: CodeExpenseTypeID selects both the GL account set and the accounting treatment (CodeASC842ScheduleID, CodeIFRS16ScheduleID, CodeSLScheduleID) in one action.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | An expense type is chosen |
| Stated as | `CodeExpenseTypeID` → `CodeExpenseType` |
| Stated as | Selects both the GL account set and the accounting treatment (`CodeASC842ScheduleID`, `CodeIFRS16ScheduleID`, `CodeSLScheduleID`) |
| Stated as | GL + treatment |
| Stated as | Observed |

## What it constrains

[CodeExpenseType](../entities/CodeExpenseType.md)

---

Source: `docs/modules/contracts/rules.md`
