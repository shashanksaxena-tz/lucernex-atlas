# ACC-R-050 — Approval is irreversible ↑ upgraded

*Lease Accounting & Payments · Observed*

**`SLSummary.IsApproved := true`, and cannot be reversed through the application.**

One-way, and it is the terminus of the workflow.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | the ASC 842 Schedule Review/Approval workflow reaches its third step and the client approver accepts (see `ACC-R-060`) |
| The test | `SLSummary.IsApproved := true`, and cannot be reversed through the application |

## The wording it rests on

> Once a schedule has been approved, it cannot be un-approved.

## Rules it cites

[ACC-R-060](ACC-R-060.md)

## Confidence

Observed — "Once a schedule has been approved, it cannot be un-approved." ⚠ Live capture upgrades this rule materially: `IsApproved` is not a checkbox a user ticks at will. It is the terminus of a three-step, three-approver workflow. A rebuild that models approval as a Boolean setter has modelled the wrong thing

---

Source: `docs/modules/accounting/rules.md`
