---
title: "Manage Work Flows"
tags: [screen, administration,workflow]
evidence: Observed
---

`/en/workflow/WorkFlowTemplateEdit.jsp`

![The template list. 13 at BBW against 4 at American Freight — and the "v1"/"v2" suffixes are the entire versioning mechanism.](../assets/screenshots/bbw-admin/08-manage-work-flows.jpg)
`docs/assets/screenshots/bbw-admin/08-manage-work-flows.jpg` · `af-admin/09-manage-work-flows.jpg`

![Every template expanded to its steps. Every row in the Type column reads "Form". There is not one Task step anywhere.](../assets/screenshots/workflow/manage-workflow-expanded-all-steps.jpg)
`docs/assets/screenshots/workflow/manage-workflow-expanded-all-steps.jpg`

**13 templates, 62 steps** at [[tenant-bbw|BBW]]. Step lists were read out of the grid store's
`expandedHtml` field, so **no template had to be opened in edit mode** — [[method-bulk-json-endpoint]].

Four findings come off this screen:

- [[finding-no-task-step-anywhere]] — every row reads `Form`, and `TaskTemplate = 0`.
- [[finding-form-workflow-not-1-1]] — 13 workflows against 6 form types.
- [[finding-workflow-versioning-is-naming]] — suffixes and a sentence in a description field.
- [[finding-routing-is-to-named-people]] — the `Approver` column is a list of individuals, deliberately
  **not recorded in this corpus** ([[method-omitting-identities]]).

Every row carries `edit | delete | add task step | add form step`, and the task link builds a URL with
a literal `&StepType=Task` — which is how the step-type vocabulary was settled.

See [[WorkFlowTemplate]] · [[feature-workflows-forms]]

All screens: [[map-of-screens]] · caveat: [[caveat-viewport]]
