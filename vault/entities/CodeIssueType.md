---
title: CodeIssueType
tags: [entity, configuration, workflow, layouts]
evidence: Observed
---

**`TableType 2035` · 19 columns · [[code-table]] `Issue Type Code`**

The row that defines a [[form-vs-page|Form]]. `Manage Forms` is literally
`FirmCodeEdit.jsp?…TableType=2035`.

Two columns carry all the weight:

- **`IsWorkFlow`** — the *only* thing separating a Form from a [[custom-list]]. Manage Forms and
  Manage Custom Lists are two views over one code table.
- **11 `IsValidFor…` booleans** — which entity types the form may attach to, including
  `IsValidForEquipContract`. A row of booleans, not a join table. The same eleven flags appear on
  folder templates and on the `VirtualTemplate*` [[virtual-projection|projections]].

Six values at [[tenant-bbw|BBW]]: `ASC 842 Tracking`, `Change Request`, `Lease Admin Request`,
`QC Request`, `User Request`, `Vendor Changes (Integration)`.

It is one of the counterexamples that **refutes the 2000/3000 band hypothesis** — 2000-band, 19
fields, thoroughly behaviour-bearing. See [[code-table]].

`2035` is also one of only two tables rendering **no `Inactive` column** at all.

See [[finding-form-workflow-not-1-1]] · [[screen-manage-forms]]
