# ACC-R-026 — Secondary schedule allocation

*Lease Accounting & Payments · Observed*

**the stated percentage of the amount is allocated to a secondary schedule; the remainder to the primary.**

A stated percentage goes to a secondary schedule; the remainder is assumed to go to the primary.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | an `AcctingAssumptionAdjust` or `Covenant` carries a secondary allocation |
| What it reads | `AcctingAssumptionAdjust.SecondaryRentSchedAllocPercent`, `Covenant.SecondaryRentSchedAllocPercent` |
| What it computes | the stated percentage of the amount is allocated to a secondary schedule; the remainder to the primary |

## The wording it rests on

> If the expense setup has a secondary schedule allocation percentage, enter the allocation in this field

## What it constrains

[AcctingAssumptionAdjust](../entities/AcctingAssumptionAdjust.md), [Covenant](../entities/Covenant.md)

Columns named: `AcctingAssumptionAdjust.SecondaryRentSchedAllocPercent`, `Covenant.SecondaryRentSchedAllocPercent`

## Confidence

Observed that the fields exist and mean an allocation percentage ("If the expense setup has a secondary schedule allocation percentage, enter the allocation in this field"); Inferred that the remainder goes to the primary

---

Source: `docs/modules/accounting/rules.md`
