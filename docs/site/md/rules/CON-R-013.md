# CON-R-013 — 1. The Clause / Schedule / Transaction / Projection pattern

*Contracts & Leases · Observed*

**An escalation step is materialised: L1 rows form a doubly-linked list; each row carries PreviousAnnualAmount/AnnualAmount/NextAnnualAmount.**

An escalation step is materialised: L1 rows form a doubly-linked list; each row carries PreviousAnnualAmount/AnnualAmount/NextAnnualAmount.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | An escalation step is materialised |
| Stated as | `PreviousExpenseScheduleID`, `NextExpenseScheduleID` |
| Stated as | L1 rows form a doubly-linked list; each row carries `PreviousAnnualAmount`/`AnnualAmount`/`NextAnnualAmount` |
| Stated as | Auditable step chain |
| Stated as | Observed |

---

Source: `docs/modules/contracts/rules.md`
