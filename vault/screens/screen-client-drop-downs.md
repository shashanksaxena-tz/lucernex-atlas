---
title: "Client Drop Downs"
tags: [screen, administration,configuration,reference-data]
evidence: Observed
---

`/en/admin/CustomCodeTableEdit.jsp`

![The firm's own registry — "Displaying 1 - 15 of 38", every row with edit and delete. Note the fourth column truncated at "Smar…": that is the Smart List Parent, and nothing uses it.](../assets/screenshots/bbw-admin/28-client-drop-downs.jpg)
`docs/assets/screenshots/bbw-admin/28-client-drop-downs.jpg` · `af-admin/29-client-drop-downs.jpg`

**38 tenant-authored tables at [[tenant-bbw|BBW]]**, 27 at [[tenant-american-freight|AF]], with full
create/edit/delete. See [[client-drop-down]].

Two of them carry disproportionate weight: **`Lease Status`**, where
[[contract-lifecycle|the contract lifecycle actually lives]], and **`Lease Admin Request Type`**, which
drives **44 of 54** [[conditional-field]] clauses.

**All 38 have `ParentCustomCodeTableID` empty** — the cascading capability exists and is used nowhere.

![A value's audit log — Old Value, New Value, Field, Action, Item ID.](../assets/screenshots/drop-downs/client-drop-downs-value-audit-log.png)
`docs/assets/screenshots/drop-downs/client-drop-downs-value-audit-log.png`

The [[audit-trail]] is field-level here as everywhere.

All screens: [[map-of-screens]] · caveat: [[caveat-viewport]]
