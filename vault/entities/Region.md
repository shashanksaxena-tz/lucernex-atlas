---
title: Region
tags: [entity, platform-tenancy, gap]
evidence: Derived
---

**`region` · 1 field · [[module-platform-tenancy]]**

**One declared field, referenced from 12 objects across 34 columns** (`RegionID`, `RootRegionID`,
`SubRegionID`). Eleventh in in-degree on a single-field table.

This is a **known schema-export gap**, not a one-column table ([[rule-PLT-R-009]]). The org-chart
region hierarchy plainly exists — [[Program]] carries `OrgChartProgramID`, the admin has a
[[screen-manage-regions|Manage Regions / Org Chart]] screen — and the export shows one field.

[[rule-PLT-R-014]] generalises the warning: `EntityTemplate`, `MapClientSchedule`, `Notify`,
`ScratchPad`, `AuditTable`, `FolderTemplate` and this are **joins or truncations**. Do not model them
as one-column tables.

Note `Market Area Code` (`TableType 2049`, 213 values — the second-largest code table in the product)
is a `MARKET` routing level and **not** a Region level.
