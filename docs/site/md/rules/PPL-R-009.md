# PPL-R-009 — A member's routable identity is three independent axes

*People & Parties · Observed*

**A person can be selected by class, by title (global or entity-specific), or by reporting-line position, and these three do not have to agree with each other.**

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | Any workflow, task, or notification routing rule |
| What it reads | `Member.CodeUserClassID`, `Member.CodeJobTitleID` (default) / `LinkMemberProjectEntity.CodeJobTitleIDList`/`AssignedCodeJobTitleIDList` (per-entity override), `Member.SupervisorID` (org chart) |
| What it writes | A person can be selected by class, by title (global or entity-specific), or by reporting-line position, and these three do not have to agree with each other |

## What it constrains

[Member](../entities/Member.md), [LinkMemberProjectEntity](../entities/LinkMemberProjectEntity.md)

Columns named: `Member.CodeUserClassID`, `Member.CodeJobTitleID`, `LinkMemberProjectEntity.CodeJobTitleIDList`, `Member.SupervisorID`

## Confidence

Observed — `security-model.md`, cross-referencing `../workflow/routing-and-approvals.md` §2 without re-deriving it

---

Source: `docs/modules/people-parties/rules.md`
