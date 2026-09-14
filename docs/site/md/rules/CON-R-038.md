# CON-R-038 — 3. Recurring expense: setup and schedule

*Contracts & Leases · Observed*

**An expense is split across organizations: ExpenseAllocation apportions one clause across organizations by percentage.**

An expense is split across organizations: ExpenseAllocation apportions one clause across organizations by percentage.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Splitting an expense across orgs |
| Stated as | `ExpenseAllocation.OrganizationID`, `.AllocationPercentage`, `.ExpenseSetupID` |
| Stated as | Allocates one clause across organizations by percentage |
| Stated as | Allocation set |
| Stated as | Observed |

## What it constrains

[ExpenseAllocation](../entities/ExpenseAllocation.md)

Columns named: `ExpenseAllocation.OrganizationID`

---

Source: `docs/modules/contracts/rules.md`
