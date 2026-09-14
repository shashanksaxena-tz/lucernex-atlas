---
title: Search and filtering
tags: [feature, search, api]
evidence: Observed
---

The largest undocumented area, because `PLForm.jsp` serves **37 of 105** routed screens. Three
mechanisms exist and they are **not layers of one feature**.

1. **Per-placement**, in [[PageLayoutField]]`.JSONConfigText`. Ten list/search keys, and the striking
   number is **`IncludeInSearch` on just 9 placements tenant-wide** — so search participation is
   configured **per field per layout**, not per entity or per field.
   `ColumnWidthInList` 667 · `ShowColumnTotal` 146 · `rowsPerPage` 26 · `DisableRowEditorInList` 27.
2. **Layout-level run-mode filters**, in [[PageLayoutFilter]] — **zero rows in BBW**. Built and
   unused.
3. **The API**: [[fiql]], with `fields` mandatory and a **413** ceiling.

Lists carry two narrowing controls side by side — a typed filter row *and* a separate top-right
`Search:` box. Inline row editing is the default (`DisableRowEditorInList` turns it off).

Three per-placement option filters are used **once each**: `limitBy_CodeContactTypeID`,
`limitBy_ExpenseTypeName`, `limitBy_CodeJobFunctionID`.

`Issue.SearchField (Text)` is a denormalised search column, which suggests some search is served by
precomputed text. *(Inferred.)*

[`features/search-filtering/`](../../docs/features/search-filtering/README.md)
