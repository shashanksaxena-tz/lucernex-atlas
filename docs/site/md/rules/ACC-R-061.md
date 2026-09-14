# ACC-R-061 — What an ASC 842 review request may be raised against

*Lease Accounting & Payments · Observed*

**the form type declares attachability as a Boolean per entity kind. For this form type, only `Portfolio` = Yes and `RE Contract` = Yes; `Capital Program`, `Prototype`, `Location`, `Parcel`, `Site`, `Project`, `Facility`, `Capital Project` and `Equipment Contract` are all `No`.**

Portfolio and RE Contract only; Equipment Contract excluded.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | creating an `ASC 842 Schedule Review/Approval` request |
| The test | the form type declares attachability as a Boolean per entity kind. For this form type, only `Portfolio` = Yes and `RE Contract` = Yes; `Capital Program`, `Prototype`, `Location`, `Parcel`, `Site`, `Project`, `Facility`, `Capital Project` and `Equipment Contract` are all `No` |
| Rebuild note | ⚠ `Equipment Contract` is `No`. Equipment leases generate ASC 842 schedules (`Asset` carries the full classification field set, and `Contract.GenerateFASBSchedule` exists on equipment contracts) but cannot be routed through this review workflow. Either equipment schedules bypass the approval gate entirely, or they are reviewed at the portfolio level. This is a real process gap and is now the top open question below |

## What it constrains

[Prototype](../entities/Prototype.md), [Location](../entities/Location.md), [Parcel](../entities/Parcel.md), [Project](../entities/Project.md), [Facility](../entities/Facility.md), [Asset](../entities/Asset.md), [Contract](../entities/Contract.md)

Columns named: `Contract.GenerateFASBSchedule`

## Confidence

Observed

---

Source: `docs/modules/accounting/rules.md`
