---
title: Custom lists
tags: [feature, configuration]
evidence: Observed
---

Concept: [[custom-list]]. Entity: [[ClientListRow]].

A tenant-authored mini record type — **a [[form-vs-page|Form]] without the workflow**.
`CodeIssueType.IsWorkFlow` is the only difference, so Manage Forms and Manage Custom Lists are two
views over one [[code-table]].

Form attachability is **11 `IsValidFor…` boolean columns**, one of them `IsValidForEquipContract` — a
row of booleans, not a join table.

Five lists at [[tenant-american-freight|AF]], six at [[tenant-bbw|BBW]]. `Client Request Log` binds to
[[Program|Portfolio]] with field prefix `CRL_` and layout `96279`; the rest bind to [[Contract]].

**And the storage does not add up** — [[ClientListRow]] has 24 columns, none prefixed, and five
generic `SubValue` slots **all typed `Currency`**, against a list showing 13 leaf fields. Two readings
survive and the corpus recorded it open rather than resolving it.

Screens: [[screen-manage-custom-lists]]

[`features/custom-lists/`](../../docs/features/custom-lists/README.md)
