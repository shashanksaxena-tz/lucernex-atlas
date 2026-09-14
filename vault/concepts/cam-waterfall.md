---
title: The CAM waterfall
tags: [concept, contracts, expense-recovery]
evidence: Observed
---

Common Area Maintenance recovery — the landlord's expense pass-through — is the one financial
subsystem that **does not follow the [[setup-schedule-transaction]] pattern**, and it is the largest
object in the product: [[ExpenseRecovery]], **565 fields** across four physical tables, a
9-perspective × 19-measure × Gross/Net cross-product.

The six-step waterfall is recoverable exactly, from Lx's own on-screen labels:

| Step | Formula | Rule |
|---|---|---|
| Sub Total #1 | `C + NC − D` | [[rule-CON-R-080]] |
| Pass-Through | `ST1 + AF% + AF + A` | `CON-R-081` |
| Sub Total #2 | `PT − R` | `CON-R-082` |
| Net Pass-Through | `ST2 × PRR` | `CON-R-083` |
| Net Amount Due | `NPT − PP` | `CON-R-084` |
| Reconciled Net Amount Due | `NAD + Adj` | `CON-R-086` |

**Where the recovery cap clamps in this sequence is not observable**, and the prior — controllables
only — is Inferred and unresolved ([[rule-CON-R-094]]). That is a real gap: cap placement changes the
number.

Property tax is modelled as a recoverable expense, not a simple landlord bill:
[[PropertyTaxSummary]] carries `CodeRecoveryGroupID` and `CodeRecoveryTypeID` ([[rule-TAX-R-009]]).

This is also where ASG's own customisation concentrates —
**147 of 205 [[firm-custom-field|firm fields]] are CAM clauses on [[Contract]]**.

Source: [`modules/contracts/cam-waterfall.md`](../../docs/modules/contracts/cam-waterfall.md) ·
[`modules/contracts/expense-recovery-cam.md`](../../docs/modules/contracts/expense-recovery-cam.md)
