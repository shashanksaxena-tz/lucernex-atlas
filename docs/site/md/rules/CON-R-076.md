# CON-R-076 — 6. Alternate rent and offsets

*Contracts & Leases · Derived*

**A ScheduledOffset is drawn down: a landlord credit (TotalAmount, CapAmountPerMonth) is drawn down over time against named expense group/types, via APPLY_OFFSETS.**

A ScheduledOffset is drawn down: a landlord credit (TotalAmount, CapAmountPerMonth) is drawn down over time against named expense group/types, via APPLY_OFFSETS.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | A `ScheduledOffset` is drawn down |
| Stated as | `TotalAmount`, `CapAmountPerMonth`, `CapPercent`, `AmountAllocated`, `AmountNotAllocated`, `LinkSchedOffsetExpGrpType`, `APPLY_OFFSETS` |
| Stated as | A landlord credit is drawn down over time, capped per month, against named expense group/types |
| Stated as | Draw-down |
| Stated as | Derived |

## What it constrains

[ScheduledOffset](../entities/ScheduledOffset.md), [LinkSchedOffsetExpGrpType](../entities/LinkSchedOffsetExpGrpType.md)

---

Source: `docs/modules/contracts/rules.md`
