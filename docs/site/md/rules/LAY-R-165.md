# LAY-R-165 — F. Forms

*Configuration, Layouts, Forms & Reporting · Observed*

**Forms are the workflow engine's rendering surface, bound at two levels: `WorkFlowTemplate.PageLayoutID` is the single kick-off/Submit form for the whole workflow, while `WorkFlowTemplateStep.PageLayoutApproversID` and `.PageLayoutAssigneesID` bind an approver-facing and an assignee-facing layout….**

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Forms are the workflow engine's rendering surface, bound at two levels: `WorkFlowTemplate.PageLayoutID` is the single kick-off/Submit form for the whole workflow, while `WorkFlowTemplateStep.PageLayoutApproversID` and `.PageLayoutAssigneesID` bind an approver-facing and an assignee-facing layout per step. A workflow with N steps therefore carries N+1 layouts. Different participants see a different form for the same record at the same step. |
| Stated as | Observed (columns + vendor Definition text) |
| Stated as | `all-fields.csv`; `_xlsx_feature_list.txt` |

## What it constrains

[WorkFlowTemplate](../entities/WorkFlowTemplate.md), [WorkFlowTemplateStep](../entities/WorkFlowTemplateStep.md)

Columns named: `WorkFlowTemplate.PageLayoutID`, `WorkFlowTemplateStep.PageLayoutApproversID`

---

Source: `docs/modules/layouts-and-forms/rules.md`
