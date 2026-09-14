---
title: ExpenseRecovery
tags: [entity, contracts, expense-recovery, core]
evidence: Observed
---

**`expense_recovery_part1..part4` · 565 fields · expense-recovery**

**The CAM waterfall itself**, and the second-largest object in the product (7.6% of all fields) —
a 9-perspective × 19-measure × Gross/Net cross-product, spread across four physical tables.

It is the **one financial subsystem that does not follow [[setup-schedule-transaction]]**, which the
contracts module calls out explicitly as its architectural exception.

It has **zero inbound foreign keys** as a module, and both `ExpenseRecoveryID` and `ModifiedDate`
repeat **exactly four times** across its four tables — the signature of the vertical partition.

The six-step arithmetic is recoverable exactly from the product's own on-screen labels — see
[[cam-waterfall]]. What is **not** recoverable is where the recovery cap clamps in that sequence
([[rule-CON-R-094]]).

It has no `docs/modules/` folder of its own; the analysis lives under
[`contracts/expense-recovery-cam.md`](../../docs/modules/contracts/expense-recovery-cam.md).

Dropped entirely from [[equipment-contract]] — equipment pays rent, it does not recover expenses.
