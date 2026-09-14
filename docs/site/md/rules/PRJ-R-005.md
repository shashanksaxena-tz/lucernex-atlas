# PRJ-R-005

*Capital Projects & Scheduling · Derived*

**A task's dates need working-day calculation · `HolidaySchedule` → `HolidayDate`, `Program.DefaultHolidayScheduleID` (`portfolio-transactions`), `Program.DefaultWorkWeekends`, `TaskGroup.TaskEndsCodeDayOfWeekID` · The portfolio's default calendar and weekend policy feed every task's duration math,….**

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | A task's dates need working-day calculation |
| Stated as | `HolidaySchedule` → `HolidayDate`, `Program.DefaultHolidayScheduleID` (`portfolio-transactions`), `Program.DefaultWorkWeekends`, `TaskGroup.TaskEndsCodeDayOfWeekID` |
| Stated as | The portfolio's default calendar and weekend policy feed every task's duration math, overridable per task via `TaskEndsCodeDayOfWeekID`. |
| Stated as | Derived |

## What it constrains

[HolidaySchedule](../entities/HolidaySchedule.md), [HolidayDate](../entities/HolidayDate.md), [Program](../entities/Program.md), [TaskGroup](../entities/TaskGroup.md)

Columns named: `Program.DefaultHolidayScheduleID`, `Program.DefaultWorkWeekends`, `TaskGroup.TaskEndsCodeDayOfWeekID`

---

Source: `docs/modules/projects-capital/rules.md`
