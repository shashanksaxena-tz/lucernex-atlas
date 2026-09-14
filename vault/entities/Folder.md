---
title: Folder
tags: [entity, documents]
evidence: Observed
---

**`folder` · 16 fields · [[module-documents-folders]]**

The document-management folder. Its parent is **optional**, so the folder tree has genuine roots —
unlike [[Document]], whose parent is required ([[rule-DOC-R-004]]).

`FolderSecurity` carries **no `ProjectEntityID`**, so folder access control is scoped only through the
folder itself, not through the entity it hangs off ([[rule-DOC-R-006]]).

`FolderTemplate` is a **one-field stub**; the real template metadata is in the
[[virtual-projection|`VirtualTemplateFolder`]] projection, carrying the same **11 `IsValidFor*`
flags** as [[CodeIssueType]] ([[rule-DOC-R-007]], [[rule-DOC-R-008]]).

`FolderTemplateAudit` records folder, budget **and** task templates applied together in one event
([[rule-DOC-R-009]]).

Screens: [[screen-manage-folder-templates]]
