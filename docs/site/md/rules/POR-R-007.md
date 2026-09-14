# POR-R-007

*Portfolio & Real-Estate Transactions · Derived*

**A rollout program needs capacity tracking · `DevelopmentPlan` → `DevelopmentSlot` → `ProgramRevenueWeeks` · Rolls up filled/unfilled slot and week counts per `Program`. No FK connects a `DevelopmentSlot` to the specific `PotentialProject`/`RETransaction` it is meant to fill — only the generic….**

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | A rollout program needs capacity tracking |
| Stated as | `DevelopmentPlan` → `DevelopmentSlot` → `ProgramRevenueWeeks` |
| Stated as | Rolls up filled/unfilled slot and week counts per `Program`. No FK connects a `DevelopmentSlot` to the specific `PotentialProject`/`RETransaction` it is meant to fill — only the generic `ProjectEntityID`. |
| Stated as | Derived |

## What it constrains

[DevelopmentPlan](../entities/DevelopmentPlan.md), [DevelopmentSlot](../entities/DevelopmentSlot.md), [ProgramRevenueWeeks](../entities/ProgramRevenueWeeks.md), [Program](../entities/Program.md), [PotentialProject](../entities/PotentialProject.md), [RETransaction](../entities/RETransaction.md)

---

Source: `docs/modules/portfolio-transactions/rules.md`
