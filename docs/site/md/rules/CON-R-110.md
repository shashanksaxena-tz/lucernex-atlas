# CON-R-110 — 9. Payment lifecycle

*Contracts & Leases · Derived*

**A transaction is posted: all twenty account numbers from CodeExpenseType are snapshotted onto the transaction row, not looked up again at export time.**

A transaction is posted: all twenty account numbers from CodeExpenseType are snapshotted onto the transaction row, not looked up again at export time.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | A transaction is posted |
| Stated as | `CodeExpenseType.APExportBase/Prepaid/Tax1..4Number`, `.ExpAccrualAcct1..4Number`, `.PercentRentAccrualAcct1..4Number`, `.RETaxAccrualAcct1..4Number` |
| Stated as | The account numbers are snapshotted onto the transaction row, not looked up at export |
| Stated as | Frozen GL coding |
| Stated as | Derived |

---

Source: `docs/modules/contracts/rules.md`
