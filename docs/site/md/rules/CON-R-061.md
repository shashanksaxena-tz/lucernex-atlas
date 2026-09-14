# CON-R-061 — Step 6 — offsets (``)

*Contracts & Leases · Observed*

**Offsets are applied: VariableRentOffset and ScheduledOffset, applied via APPLY_OFFSETS, reduce the rent-year obligation.**

Offsets are applied: VariableRentOffset and ScheduledOffset, applied via APPLY_OFFSETS, reduce the rent-year obligation.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Field |
| Stated as | Role |
| Stated as | `RentYearBeginDate` / `RentYearEndDate` |
| Stated as | The rent year, per `RentYearStartMonth` |
| Stated as | `RentYearHasAltRent(Boolean)` |
| Stated as | An `AlternateRentSchedule` window overlaps this rent year |

## The wording it rests on

> reduce percentage rent by what we paid in CAM this year

## What it constrains

[VirtualPRPAggregate](../entities/VirtualPRPAggregate.md), [VariableRentOffset](../entities/VariableRentOffset.md), [ScheduledOffset](../entities/ScheduledOffset.md), [LinkSchedOffsetExpGrpType](../entities/LinkSchedOffsetExpGrpType.md), [AlternateRentSchedule](../entities/AlternateRentSchedule.md)

---

Source: `docs/modules/contracts/percentage-rent.md`
