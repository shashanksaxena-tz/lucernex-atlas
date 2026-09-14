---
title: Custom list — a tenant-authored mini record type
tags: [concept, layouts, configuration]
evidence: Observed
---

Not a picklist. A **custom list** is a tenant-authored miniature record type with its own field
namespace, its own [[page-layout-concept|layout]], and a binding to a parent entity — rendered as a
grid on the parent's page. Mechanically it is a [[form-vs-page|Form]] with `CodeIssueType.IsWorkFlow`
switched off.

At [[tenant-american-freight|American Freight]]: five lists. `Client Request Log` on
[[Program|Portfolio]] (field prefix `CRL_`, layout `96279`); `Default Log`, `Funds`,
`Operating Expenses` (prefix `OpEx`), `Reconciliation Log` and `Savings Log` on [[Contract]].
[[tenant-bbw|BBW]] has 6.

**Where the values are stored is unresolved, and the obvious answer does not work.**
[[ClientListRow]] has 24 columns and **not one carries a `CRL_` or `OpEx` prefix**, contradicting the
script names. Its five generic value slots `SubValue`…`SubValue5` are **all typed `Currency`**, which
cannot hold `OpExComments` or a date, and `Operating Expenses` shows 13 leaf fields against a
five-slot cap. Two readings survive — a generic EAV store, or real per-list columns on the
[[firm-custom-field|`Firm_` precedent]]. Recorded open, not resolved.

Source: [`features/custom-lists/`](../../docs/features/custom-lists/README.md) ·
[`admin/006-manage-custom-lists.md`](../../docs/admin/006-manage-custom-lists.md)
