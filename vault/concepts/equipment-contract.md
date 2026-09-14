---
title: Equipment Contract
tags: [concept, contracts, accounting, equipment]
evidence: Observed
---

[[tenant-bbw|BBW]]'s fifth navigation root, absent at [[tenant-american-freight|American Freight]].
It is the vendor drawing its own line between **generic lease accounting** and **retail property
management** — which is the exact line ASG Edge+ has to draw for itself.

It mirrors [[Contract]] and then subtracts: 26 screens against 39.

| Group | Contract | Equipment Contract | Dropped |
|---|---:|---:|---|
| Details | 7 | 5 | `Binders`, `Schedule` |
| Abstract Info | 8 | 7 | `Co-Tenancy` |
| Payment Info | 12 | 7 | `Alternate Rent`, `Invoices`, `Recoveries`, `Percentage Rent`, `Sales` |
| Accounting Info | 7 | 6 | `Capital Lease Test` |
| **Accrual Info** | **4** | **absent — whole group** | all four |

`Recurring Expenses` is **renamed** `Recurring Payments`, not dropped — equipment pays rent, it does
not recover expenses.

**What survives untouched is the entire accounting engine**: `Straight-Line Rent`,
`Accounting Assumptions`, `ASC 842 Test`, `ASC 842 Rent Schedule`, `IFRS 16 Rent Schedule`, plus
`Terms`, `Amendments`, `Covenants`, `Key Dates`, `Insurance`, `Security Deposit`, `Allowances`,
`Transactions`, `Receipts`. Everything dropped is retail-property-specific. This confirms by
construction that [[finding-accounting-runs-per-asset|the lease-accounting engine runs per equipment
asset]], where the earlier evidence was three nullable foreign keys to [[Asset]].

**There is no `EquipmentContract` table.** Not in the 223-object census, not in the 227-table picker,
not among the 25 refused tables. Equipment contracts are [[Contract]] rows discriminated by
`ProjectEntityTypeName = 'Equipment Contract'`. `GET /rest/businessObject/EquipmentContract` returns
2,017 links to the same `Contract` records — an alias.

One dropped item is not retail-specific and deserves an answer: [[q-bbw-02-capital-lease-test]].

Caveat on every screen of it: [[caveat-one-equipment-contract]].

Source: [`features/equipment-contracts/`](../../docs/features/equipment-contracts/README.md)
