---
title: WorkFlowStepApprover
tags: [entity, workflow, people]
evidence: Observed
---

**`work_flow_step_approver` · 20 fields · [[module-workflow]]**

One named approver's action on a running [[WorkFlowStep]]. Carries action fields; its sibling
`WorkFlowStepAssignee` has **11 columns and none** — assignees do work, approvers decide.

Two failure modes are in the schema, not in the configuration:

- `RequireAllApprovers` **deadlocks with no recovery path** if approvers choose different actions
  ([[rule-WF-R-053]]).
- **Only one prior approval round is retained.** A third round overwrites the second
  ([[rule-WF-R-057]]).

Every approver observed in [[tenant-bbw|BBW]]'s 62 steps is a real individual. **Only counts are
recorded in this corpus** — [[method-omitting-identities]] — and that is also the evidence for
[[finding-routing-is-to-named-people]].
