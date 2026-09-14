---
title: AccrualTransaction
tags: [entity, accounting]
evidence: Observed
---

**`accrual_transaction` · 55 fields · [[module-accounting]]**

An individual expense-accrual posting, with **eight parallel GL account fields**.

Its `SourceEntityTable` column, paired with `Source Entity Code` (`TableType 2172`), is the suspected
**polymorphic-association discriminator** — a table name held as data. Worth finding before designing
anything that reads it.

The whole `Accrual Info` group — Accrual Details, Expense Accruals, Transactions, Percentage Rent
Accruals — is **dropped entirely from [[equipment-contract|Equipment Contract]]**, which is the
clearest signal that accruals are part of the retail-property layer rather than generic lease
accounting.

See [[setup-schedule-transaction]] · [[ExpenseAccrualSchedule]]
