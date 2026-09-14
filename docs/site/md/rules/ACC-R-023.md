# ACC-R-023 — Recalculation audit trail

*Lease Accounting & Payments · Observed*

**`RecalcTriggerDate := today`; `NeedsRecalcModifiedByLastMember := current member`; current member appended to `NeedsRecalcModifiedByMemberIDList`.**

Raising the flag stamps the date, the last user, and appends to the member list.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | `NeedsRecalculation` transitions to true |
| What it writes | `RecalcTriggerDate := today`; `NeedsRecalcModifiedByLastMember := current member`; current member appended to `NeedsRecalcModifiedByMemberIDList` |

## The wording it rests on

> The date that the Recalc? flag was triggered

## Confidence

Observed — "The date that the Recalc? flag was triggered"; "the last member whose action would have caused the Recalc? flag to change"; "all members who have made changes that would cause the Recalc? flag to change."

---

Source: `docs/modules/accounting/rules.md`
