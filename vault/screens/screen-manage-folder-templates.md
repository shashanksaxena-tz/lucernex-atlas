---
title: "Manage Folder Templates"
tags: [screen, administration,documents,configuration]
evidence: Observed
---

`/en/admin/FolderTemplateEdit.jsp`

![Folder templates — and the eleven "IsValidFor" flags are the same matrix Forms use.](../assets/screenshots/bbw-admin/44-manage-folder-templates.jpg)
`docs/assets/screenshots/bbw-admin/44-manage-folder-templates.jpg` · `af-admin/48-manage-folder-templates.jpg`

`FolderTemplate` is a **one-field stub**; the real metadata lives in the
[[virtual-projection|`VirtualTemplateFolder`]] projection ([[rule-DOC-R-007]]) — an instance of
[[rule-PLT-R-014]].

**Attachability is eleven `IsValidFor*` booleans — the same matrix as
[[CodeIssueType|Forms]]** ([[rule-DOC-R-008]]). One pattern, three places: forms, folder templates, and
the `VirtualTemplate*` projections.

`FolderTemplateAudit` records folder, **budget and task** templates applied together in one event
([[rule-DOC-R-009]]) — so template application is one operation, not three.

See [[Folder]] · [[module-documents-folders]]

All screens: [[map-of-screens]] · caveat: [[caveat-viewport]]
