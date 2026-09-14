---
title: WorkFlow
tags: [entity, workflow]
evidence: Observed
---

**`work_flow` · 19 fields · [[module-workflow]]**

A running workflow instance, against a real trigger object. Stored in the **same tables** as its
[[WorkFlowTemplate|template]], distinguished by the self-reference `WorkFlow.WorkFlowTemplateID` — see
[[workflow-template]].

`WorkFlow.KickOffTaskID` points at [[TaskGroup]], which corroborates the GraphQL
`KickOffMethod.TASK` enum value ([[rule-PRJ-R-012]]).

Closing it (`CloseWorkFlow`) sets `IsCompleted`, `ClosedDate` and a terminal status, and fires three
template notification flags ([[rule-WF-R-062]]).

**Where workflow *status* lives is still open** — `Work Flow Status Code` is **not among the 207**
[[code-table|code tables]]. The three nearest candidates are `Approval Status Code` (`2081`),
`Last Action Status Code` (`2082`) and `Decision Status Code` (`2025`).
