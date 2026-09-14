---
title: A Form is an Issue Type
tags: [concept, layouts, workflow, core]
evidence: Observed
---

The cleanest distinction in the product, and it is not obvious from the admin menu:

- A **Page** presents an entity that already exists.
- A **Form** is an **Issue Type** — a tenant-defined *request* type, with one layout per
  [[workflow-step]]. `Manage Forms` is literally `FirmCodeEdit.jsp?TableType=2035`, i.e. the
  [[code-table]] `Issue Type Code`, edited through the generic code-table editor.
- A **[[custom-list]]** is a Form *without* the workflow. `CodeIssueType.IsWorkFlow` is the only
  thing separating them, so Manage Forms and Manage Custom Lists are two views over one code table.

[[tenant-bbw|BBW]] has **6 form types**: `ASC 842 Tracking`, `Change Request`, `Lease Admin Request`,
`QC Request`, `User Request`, `Vendor Changes (Integration)`.

Attachability — which entity types a form can hang off — is **11 `IsValidFor…` boolean columns** on
[[CodeIssueType]], one of them `IsValidForEquipContract`. A row of booleans, not a join table. The
same eleven flags appear on folder templates and on the `VirtualTemplate*` projections.

**The 1:1 claim is dead.** The workflow module recorded "four live workflows, 1:1 with four form
types" — true at [[tenant-american-freight|American Freight]] (4 and 4), false at BBW (13 workflows
against 6 form types, with only 4 names matching and 2 form types carrying no workflow at all). It was
a coincidence of one tenant. See [[finding-form-workflow-not-1-1]].

Form layouts are where [[conditional-field|conditional fields]] actually live —
[[finding-form-layouts-are-hidden]].

Source: [`modules/layouts-and-forms/forms-vs-pages-vs-layouts.md`](../../docs/modules/layouts-and-forms/forms-vs-pages-vs-layouts.md)
