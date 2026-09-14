# ACC-R-027 — Schedule-type flag stamping

*Lease Accounting & Payments · Derived*

**`SLSummary.IsSLSchedule` / `.IsASC842Schedule` / `.IsIFRS16Schedule := true` respectively.**

Whichever button ran sets the matching identity flag on the new schedule header.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | `GenerateStraightLineRent` / `GenerateFASBSchedule` / `GenerateIFRS16Schedule` |
| What it writes | `SLSummary.IsSLSchedule` / `.IsASC842Schedule` / `.IsIFRS16Schedule := true` respectively |
| Live state | only `IsASC842Schedule` is reachable today. With the straight-line and IFRS 16 schedule-type tables empty, `GenerateStraightLineRent` and `GenerateIFRS16Schedule` have no schedule type to stamp. Any existing row with `IsSLSchedule` or `IsIFRS16Schedule` true is an orphan whose schedule type was deleted — worth querying as a data-integrity check. Observed for the empty tables; Derived for the consequence |

## The wording it rests on

> This flag indicates that the schedule is a … schedule.

## What it constrains

[SLSummary](../entities/SLSummary.md)

Columns named: `SLSummary.IsSLSchedule`

## Confidence

Derived — the three buttons and the three flags exist and correspond by name; the vendor defines each flag as "This flag indicates that the schedule is a … schedule."

---

Source: `docs/modules/accounting/rules.md`
