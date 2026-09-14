# ACC-R-062 — Approver resolution

*Lease Accounting & Payments · Observed*

**all three ASC 842 steps use `Member` — a named approver, resolved at configuration time rather than by org-chart position.**

All three steps resolve their approver as a named Member, even though the platform also supports routing by job title or org-chart position.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | a workflow step activates |
| What it reads | the step's `Approval Level` ∈ {`Member`, `Job Title`, `Ad Hoc`} |
| The test | all three ASC 842 steps use `Member` — a named approver, resolved at configuration time rather than by org-chart position |

## What it constrains

[Member](../entities/Member.md), [Contract](../entities/Contract.md), [Asset](../entities/Asset.md)

## Rules it cites

[ACC-R-025](ACC-R-025.md), [ACC-R-027](ACC-R-027.md), [ACC-R-030](ACC-R-030.md), [ACC-R-055](ACC-R-055.md)

## Confidence

Observed. - Cross-reference: the GraphQL `AssigneeType` enum (`ALL`, `PARENT`, `REGION1`, `REGION2`, `MARKET`, `JOB_TITLE`) shows the platform supports position-based routing generally; the ASC 842 workflow does not use it. (Source: `docs/data-model/graphql-api.md`.) --- ## Rules that intentionally do not exist Stating these explicitly, because their absence is itself a finding. --- ## Open questions Ranked by how badly they block the rule engine. Items added or resolved by the 2026-09-10 live capture are marked (new) / (resolved). 0a. (resolved 2026-09-10) What are the schedule-type code table values? — `ASC 842 Schedule Type Code` (2162) has one row, `842 Rent`, with `Don't Amortize Asset Value` unchecked; `Straight Line Schedule Type Code` (2161) and `IFRS 16 Schedule Type Code` (2163) are empty. Consequences fold into `ACC-R-025`, `ACC-R-027` and `ACC-R-030` above. 0b. (resolved) Where does `GaapAmortizeMode` bind? — `P

---

Source: `docs/modules/accounting/rules.md`
