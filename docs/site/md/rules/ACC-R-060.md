# ACC-R-060 — ⚠ Schedules are not auto-published

*Lease Accounting & Payments · Observed*

**on completion of step 3, `SLSummary.IsApproved := true` (`ACC-R-050`).**

Generate, review, ASG approval, client approval. A schedule therefore has a state, not a flag — and only the final state is representable in the database.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | an ASC 842 schedule is generated and submitted for review |
| What it writes | on completion of step 3, `SLSummary.IsApproved := true` (`ACC-R-050`) |
| Process | the tenant runs a live workflow named "ASC 842 Schedule Review/Approval", three ordered steps, every step `Type = Form`, every step `Approval Level = Member`: |
| Rebuild note | ⚠ This is the single most consequential live finding for this module. The accounting engine's output is not published by the calculation. It is generated, reviewed once, approved by ASG, then approved by the client — a two-party sign-off with an internal review ahead of it. A schedule therefore has a state, not a Boolean: `draft → submitted → under review → ASG-approved → client-approved`. Nothing in the offline schema sh |

## The wording it rests on

> ASC 842 Schedule Review/Approval

## What it constrains

[SLSummary](../entities/SLSummary.md)

Columns named: `SLSummary.IsApproved`

## Rules it cites

[ACC-R-050](ACC-R-050.md)

## Confidence

Observed for the workflow, its three steps, their order, their approval levels and their bound layouts (`Manage Work Flows`, `/en/workflow/WorkFlowTemplateEdit.jsp`, tenant build `26.08.0.46`, 2026-09-10). Derived for the link to `SLSummary.IsApproved` — the workflow and the flag are the only two approval mechanisms in the product and it would be strange for them to be unrelated, but the binding column was not observed

---

Source: `docs/modules/accounting/rules.md`
