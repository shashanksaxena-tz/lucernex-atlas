# CON-R-062 — Step 7 — rent due and posting (``, `CON-R-063`)

*Contracts & Leases · Inferred*

**Rent already paid is credited: PRPRentDue = PRPTotalRent − SalesPeriodRentPaid − offsets.**

Rent already paid is credited: PRPRentDue = PRPTotalRent − SalesPeriodRentPaid − offsets.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Computed |
| Stated as | Posted |
| Stated as | `AccrualAmountThisPeriod` |
| Stated as | `PostedAccrualAmountThisPeriod` |
| Stated as | `AccrualAmountPriorPeriods` |
| Stated as | `PostedAccrualAmountPriorPeriods` |

## What it constrains

[VirtualPRPAggregate](../entities/VirtualPRPAggregate.md), [AccrualTransaction](../entities/AccrualTransaction.md), [PaymentTransaction](../entities/PaymentTransaction.md), [VirtualPRAccrualPeriod](../entities/VirtualPRAccrualPeriod.md), [AlternateRentSchedule](../entities/AlternateRentSchedule.md), [VirtualExpenseForecastPeriod](../entities/VirtualExpenseForecastPeriod.md)

Columns named: `VirtualPRPAggregate.CurrentRentPaid`, `VirtualExpenseForecastPeriod.IgnoreAlternateRent`

---

Source: `docs/modules/contracts/percentage-rent.md`
