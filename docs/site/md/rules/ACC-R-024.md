# ACC-R-024 — Recalculation override

*Lease Accounting & Payments · Derived*

**a `RecalcOverrideNotes` row linked by `SLSummaryID`; the id appended to `SLSummary.RecalcOverrideNotesIDList`.**

A note is recorded against the schedule. Whether it clears Recalc? is undocumented.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | a user declines to recalculate a dirty schedule |
| What it reads | free text |
| What it writes | a `RecalcOverrideNotes` row linked by `SLSummaryID`; the id appended to `SLSummary.RecalcOverrideNotesIDList` |

## The wording it rests on

> A free-text note explaining why a financial recalculation was manually overridden — an audit-style justification field

## What it constrains

[RecalcOverrideNotes](../entities/RecalcOverrideNotes.md), [SLSummary](../entities/SLSummary.md)

Columns named: `SLSummary.RecalcOverrideNotesIDList`

## Confidence

Derived — the object exists and is described as "A free-text note explaining why a financial recalculation was manually overridden — an audit-style justification field" (`docs/data-fields/INDEX.md`), but the workflow that creates it is not documented. Whether creating a note clears `NeedsRecalculation` is unknown. --- ## D. Schedule generation

---

Source: `docs/modules/accounting/rules.md`
