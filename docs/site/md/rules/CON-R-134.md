# CON-R-134 — 11. Typing and integrity rules for the rebuild (Constitution §4.4)

*Contracts & Leases · Observed*

**Migrating any parent-child edge: seven FKs are declared Text rather than typed, though the target's proper FK type exists elsewhere in the same schema; model them as real FKs with an orphan-handling policy.**

Migrating any parent-child edge: seven FKs are declared Text rather than typed, though the target's proper FK type exists elsewhere in the same schema; model them as real FKs with an orphan-handling policy.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Migrating any parent-child edge |
| Stated as | Seven `Text`-typed FKs (`PaymentTransaction.ExpenseRecoveryID`, `.ScheduledOffsetID`, `ExpenseSchedule.Previous/NextExpenseScheduleID`, `ExpenseAccrualSchedule.ExpenseAccrualSetupID`, `AccrualTransaction.ExpenseAccrualSetupID`, `ExpenseRecoveryItem.ExpenseRecoveryID`, `LandlordInvoiceItem.LandlordInvoiceID`, `LinkLandlordInvPaymentTxn.LandlordInvoiceItemID`) |
| Stated as | Declared `Text` rather than a typed FK, though the target's FK type exists elsewhere |
| Stated as | Model as real FKs; define an orphan-handling policy |
| Stated as | Observed |

## What it constrains

[PaymentTransaction](../entities/PaymentTransaction.md), [ExpenseAccrualSchedule](../entities/ExpenseAccrualSchedule.md), [AccrualTransaction](../entities/AccrualTransaction.md), [ExpenseRecoveryItem](../entities/ExpenseRecoveryItem.md), [LandlordInvoiceItem](../entities/LandlordInvoiceItem.md), [LinkLandlordInvPaymentTxn](../entities/LinkLandlordInvPaymentTxn.md)

Columns named: `PaymentTransaction.ExpenseRecoveryID`, `ExpenseAccrualSchedule.ExpenseAccrualSetupID`, `AccrualTransaction.ExpenseAccrualSetupID`, `ExpenseRecoveryItem.ExpenseRecoveryID`, `LandlordInvoiceItem.LandlordInvoiceID`, `LinkLandlordInvPaymentTxn.LandlordInvoiceItemID`

---

Source: `docs/modules/contracts/rules.md`
