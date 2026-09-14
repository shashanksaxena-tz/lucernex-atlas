# CON-R-152 — §13 Rent generation

*Contracts & Leases · Observed*

**An Expense Setup is generated from · `ExpenseVendorAllocation` rows, each with a `Payment Percentage` and its own begin/end dates · One setup fans out to one transaction per allocation · The vendor split can change mid-term · Observed.**

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | An Expense Setup is generated from |
| Stated as | `ExpenseVendorAllocation` rows, each with a `Payment Percentage` and its own begin/end dates |
| Stated as | One setup fans out to one transaction per allocation |
| Stated as | The vendor split can change mid-term |
| Stated as | Observed |

## What it constrains

[ExpenseVendorAllocation](../entities/ExpenseVendorAllocation.md)

---

Source: `docs/modules/contracts/rules.md`
