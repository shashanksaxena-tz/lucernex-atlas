---
title: The foreign-key graph
tags: [concept, data-model, core]
evidence: Derived
---

**972 FK-typed columns** of the 7,421 fields, of which 912 resolve to one of the 223 objects and
**60 are unresolved** (they point into configuration metadata — [[type-system]]). That gives
**701 distinct object-to-object edges** plus **13 self-references**.

**167 of 223 objects have in-degree zero.** The graph is extremely top-heavy:

| Object | Referencing objects | FK columns |
|---|---:|---:|
| [[Member]] | 161 | 290 |
| [[ProjectEntity]] | 161 | 163 |
| [[Contract]] | 61 | 62 |
| [[Employer]] | 30 | 40 |
| [[StateProvinceCountry]] | 22 | 26 |
| [[Jurisdiction]] | 16 | 17 |
| [[Covenant]] | 15 | 15 |
| [[ContractAmendment]] · [[Asset]] | 13 | 13 · 14 |
| [[Region]] | 12 | **34** |

**[[Member]]'s hub status is an illusion** — 240 of its 290 columns are the
[[audit-trail|`CreatedByID`/`ModifiedByID`]] pair. One cross-cutting concern, not 161 relationships.

The 13 self-references are where hierarchy and versioning live:
`Contract.MasterContractID`, `Parcel.MasterParcelID`, `TaskGroup.ParentTaskID` **and**
`TaskGroup.TskPredVal_PredecessorTaskID` ([[TaskGroup|two graphs on one table]]),
`Member.SupervisorID`, `Program.OrgChartProgramID`, `PaymentTransaction.AppliedToPayTranID`,
`RETransaction.RelatedTransactionID`, `CustomCodeField.ParentCustomCodeFieldID`, and — tellingly —
`WorkFlow.WorkFlowTemplateID` and `WorkFlowStep.WorkFlowTemplateStepID`, which is how
[[workflow-template|templates and instances share tables]].

**The graph under-counts by about 9%** — see [[finding-fk-graph-undercounts]]. And it misses
[[soft-reference|soft references]] entirely.

Source: [`data-model/foreign-key-graph.md`](../../docs/data-model/foreign-key-graph.md)
