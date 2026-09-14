# CON-R-039 — 3. Recurring expense: setup and schedule

*Contracts & Leases · Observed*

**An expense is split across vendors: ExpenseVendorAllocation apportions one clause's payments across vendors by percentage; CHANGE_EXPENSE_ALLOCATION_VENDOR rewrites it.**

An expense is split across vendors: ExpenseVendorAllocation apportions one clause's payments across vendors by percentage; CHANGE_EXPENSE_ALLOCATION_VENDOR rewrites it.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Splitting an expense across vendors |
| Stated as | `ExpenseVendorAllocation.VendorID`, `.PaymentPercentage`, `.APVendorNumber`, `.ExpenseSetupID` |
| Stated as | Allocates one clause's payments across vendors by percentage; `CHANGE_EXPENSE_ALLOCATION_VENDOR` rewrites it |
| Stated as | Vendor allocation set |
| Stated as | Observed |

## What it constrains

[ExpenseVendorAllocation](../entities/ExpenseVendorAllocation.md)

Columns named: `ExpenseVendorAllocation.VendorID`

---

Source: `docs/modules/contracts/rules.md`
