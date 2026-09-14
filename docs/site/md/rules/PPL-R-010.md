# PPL-R-010 — Per-entity job title can override the member's global default

*People & Parties · Inferred*

**Differs from `Member.CodeJobTitleID`.**

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | Job-Title-based routing evaluated in the context of a specific entity |
| What it reads | `LinkMemberProjectEntity.AssignedCodeJobTitleIDList` |
| The test | Differs from `Member.CodeJobTitleID` |
| What it writes | The entity-scoped assignment takes precedence for routing purposes on that entity — Inferred from the column's own definition text (*"the job titles that override the member's default job title"*), not confirmed by a live capture. See `../workflow/routing-and-approvals.md` OQ-24 |

## The wording it rests on

> the job titles that override the member's default job title

## What it constrains

[LinkMemberProjectEntity](../entities/LinkMemberProjectEntity.md), [Member](../entities/Member.md)

Columns named: `LinkMemberProjectEntity.AssignedCodeJobTitleIDList`, `Member.CodeJobTitleID`

## Confidence

Inferred

---

Source: `docs/modules/people-parties/rules.md`
