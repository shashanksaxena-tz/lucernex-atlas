---
title: Projects and capital
tags: [module, projects]
evidence: Derived
---

**23 objects · 376 fields · rules `PRJ-R-001`…`PRJ-R-014`**

The product's **generic scheduling and issue-tracking engine**, reused across capital-project
delivery, real-estate deal steps and workflow triggers. Note the [[Project]] record itself is filed
under [[module-platform-tenancy]], not here.

Entities: [[Task]] · [[TaskGroup]] · [[TaskItem]] · [[Issue]]

- **[[Task]], [[TaskGroup]] and [[TaskItem]] are three byte-identical 37-field tables**, and all 18
  `Task/Group ID` columns across three modules resolve to [[TaskGroup]] **alone**
  ([[rule-PRJ-R-001]]).
- [[TaskGroup]] carries **two separate graphs over the same rows** — the WBS hierarchy and the CPM
  dependency network ([[rule-PRJ-R-006]]).
- `ProcessTimeline` omits every hierarchy, dependency and resource field: it is a **flat milestone
  list, not a schedule network** ([[rule-PRJ-R-002]]).
- The deal pipeline **reuses `TaskGroup` directly** — it has no scheduling engine of its own
  ([[rule-PRJ-R-013]]).
- `CodeProblem` and `CodeResponsibleParty` show **zero edges** in the 972-edge graph
  ([[rule-PRJ-R-014]]).

Largely **out of scope by decision** — no BRD covers projects or capital programs, and the BRDs place
construction management in a separate legacy product. See [[finding-punch-list-out-of-scope]].

Rules: [[rules-projects-capital]] ·
[`modules/projects-capital/`](../../docs/modules/projects-capital/README.md)
