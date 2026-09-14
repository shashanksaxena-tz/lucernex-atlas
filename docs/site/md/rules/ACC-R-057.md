# ACC-R-057 — 28-day proration of partial first and last periods

*Lease Accounting & Payments · Observed*

**when true, prorate the partial period on a 28-day multiplier; and "If you have a partial period that is greater than or equal to 28 days, it will be considered a whole period by the system and will not prorate.".**

Interacts with the amortisation basis: inert on Per Day columns.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | schedule generation where the first or last period is partial |
| What it reads | `Program.SLProrate35As28` (`Boolean`); the partial period's day count |
| The test | when true, prorate the partial period on a 28-day multiplier; and "If you have a partial period that is greater than or equal to 28 days, it will be considered a whole period by the system and will not prorate." |
| Scope restriction | "This setting only impacts values calculated per period" — i.e. it interacts with `ACC-R-056`: it is inert on columns set to `PER_DAY` |

## The wording it rests on

> If you have a partial period that is greater than or equal to 28 days, it will be considered a whole period by the system and will not prorate.

## What it constrains

[Program](../entities/Program.md)

Columns named: `Program.SLProrate35As28`

## Rules it cites

[ACC-R-056](ACC-R-056.md)

## Confidence

Observed

---

Source: `docs/modules/accounting/rules.md`
