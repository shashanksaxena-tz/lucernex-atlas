---
title: "Manage Custom Lists"
tags: [screen, administration,configuration]
evidence: Observed
---

`/en/admin/CustomListEdit.jsp`

![The list index. Six lists, all Type "Standard", each with exactly one layout.](../assets/screenshots/custom-lists/manage-custom-lists-index.png)
`docs/assets/screenshots/custom-lists/manage-custom-lists-index.png`

![Editing a list's fields. This is a record-type builder, not a picklist editor — each list gets its own field namespace.](../assets/screenshots/custom-lists/manage-custom-lists-edit-fields.png)
`docs/assets/screenshots/custom-lists/manage-custom-lists-edit-fields.png`

**Not a picklist master.** A [[custom-list|tenant-authored mini record type]] with its own fields, its
own layout and a parent binding.

- The Add-item Type dropdown offers `Standard` (`value="2634"`) and `Part` (`value="2635"`).
- Each list gets its own field namespace (`CRL_*`, `OpEx*`) on a shared script object
  [[ClientListRow]] — **and `ClientListRow`'s 24 columns carry none of those prefixes**.
- The editor is `/en/issue/LayoutEditor.jsp?layoutMode=sublist&PageLayoutID={id}`.

Mechanically it is a [[form-vs-page|Form]] with `CodeIssueType.IsWorkFlow` off — so this screen and
[[screen-manage-forms]] are two views over one [[code-table]].

See [[feature-custom-lists]]

All screens: [[map-of-screens]] · caveat: [[caveat-viewport]]
