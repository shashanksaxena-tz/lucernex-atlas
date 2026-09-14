---
title: Workflows and forms
tags: [feature, workflow]
evidence: Observed
---

Concepts: [[workflow-template]] · [[workflow-step]] · [[form-vs-page]]

| | [[tenant-american-freight\|AF]] | [[tenant-bbw\|BBW]] |
|---|---:|---:|
| Workflow templates | 4 | **13** |
| Steps | 19 | **62** |
| Form types | 4 | **6** |
| `Task` steps | **0** | **0** |

Reading two tenants **refutes what one tenant appeared to prove**:

- **[[finding-form-workflow-not-1-1]]** — only 4 of 13 BBW workflow names match a form; 9 match none;
  2 form types have no workflow.
- **[[finding-no-task-step-anywhere]]** — every one of the 62 steps is type `Form`, and BBW has
  `TaskTemplate = 0`.
- **[[finding-workflow-versioning-is-naming]]** — `Lease Admin Request` base/`v1`/`v2` = 8/8/10 steps,
  and the current one has **fewer steps than the version it replaced**.
- **[[finding-routing-is-to-named-people]]** — two approval levels exist (`Ad Hoc`, `Member`) and
  `Member` resolves to a list of individuals.
- Workflows are **tenant-authored**, not [[publish-and-fork|forked]] — no clustered id-offset block,
  unlike the layouts.

**Two JavaScript escape hatches exist and neither has been read**: `IsEnabledLxJSCode` on a step
action, and `Conditional Workflow JS` on a workflow ([[q-bbw-06-conditional-workflow-js]]).

BBW's two `Implementation Workflow` templates are the **first direct evidence anywhere** for BRD-24's
abstraction path — see [[finding-maker-checker-pairs]].

Screens: [[screen-manage-work-flows]] · [[screen-manage-forms]]

[`features/workflows-forms/`](../../docs/features/workflows-forms/README.md)
