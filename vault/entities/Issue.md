---
title: Issue
tags: [entity, workflow, projects, core]
evidence: Observed
---

**`issue` · 56 fields · [[module-projects-capital]]**

The generic request/ticket record underneath a great deal of the product. A
[[form-vs-page|Form *is* an Issue Type]], so every submitted request form is an `Issue` row.

- Only **4 of its 56 fields are tenant-admin-configurable**; the other 52 are schema-only
  ([[rule-PRJ-R-004]]).
- `ServiceRequest` and `WorkOrder` are each **1:1 with an underlying Issue** — and the schema export
  types the link as untyped `Text`, so the FK graph misses it entirely ([[rule-AST-R-012]]).
- Parts consumed on a job are recorded **against the Issue, not the WorkOrder**:
  `WorkOrder → Issue → LinkIssuePart` ([[rule-AST-R-014]], [[rule-PRJ-R-009]]).
- `Issue.SearchField (Text)` is a denormalised search column — evidence that some search is served by
  precomputed text. *(Inferred.)*
- Out-degree 7 targets across 14 columns.

`Issue.LAR_RequestType` — a field on an Issue, driven by a [[client-drop-down]] — is the single driver
behind **44 of 54** [[conditional-field]] clauses in [[tenant-bbw|BBW]].

See [[CodeIssueType]]
