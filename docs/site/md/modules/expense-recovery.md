# Expense Recovery (CAM / Reconciliation)

*In scope for the rebuild*

Landlord operating-expense recovery and CAM reconciliation. Physically remarkable: ExpenseRecovery is 565 fields split across four PG tables.

|  | Count |
|---|---|
| Record types | 3 |
| Fields | 618 |
| Keys in | 0 |
| Keys out | 13 |
| Rules | 0 |

## Record types

| Record type | Postgres table | Fields | Referenced by |
|---|---|---|---|
| [ExpenseRecovery](../entities/ExpenseRecovery.md) | `expense_recovery_part1,expense_recovery_part2,expense_recovery_part3,expense_recovery_part4` | 565 | 0 |
| [ExpenseRecoveryItem](../entities/ExpenseRecoveryItem.md) | `expense_recovery_item` | 47 | 0 |
| [ExpenseRecoveryItemMapping](../entities/ExpenseRecoveryItemMapping.md) | `expense_recovery_item_mapping` | 6 | 0 |
