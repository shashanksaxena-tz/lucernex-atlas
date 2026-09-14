# PPL-R-013 — Approval-amount bands exist on `Member` but are read by no observed workflow field

*People & Parties · Derived*

**No `WorkFlowTemplateStep`/`WorkFlowTemplateStepAction` field reads these columns (exhaustive check, `../workflow/step-actions.md`/`routing-and-approvals.md`).**

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | Any attempt to implement amount-banded approval routing (route high-value payments to a different approver than low-value ones) |
| What it reads | `Member.PaymentApprovalMinAmount`/`MaxAmount`, `RecurringApprovalMinAmount`/`MaxAmount`, and the two `Equip*` pairs |
| The test | No `WorkFlowTemplateStep`/`WorkFlowTemplateStepAction` field reads these columns (exhaustive check, `../workflow/step-actions.md`/`routing-and-approvals.md`) |
| What it writes | These fields may be vestigial, may be read by application logic outside the schema dump, or may be populated but unused in the live tenant. Do not assume amount-banded routing works end-to-end without confirming a live step reads them |

## What it constrains

[Member](../entities/Member.md), [WorkFlowTemplateStep](../entities/WorkFlowTemplateStep.md), [WorkFlowTemplateStepAction](../entities/WorkFlowTemplateStepAction.md)

Columns named: `Member.PaymentApprovalMinAmount`

## Confidence

Derived — `../workflow/routing-and-approvals.md` OQ-19, carried here because the fields themselves are this module's own

---

Source: `docs/modules/people-parties/rules.md`
