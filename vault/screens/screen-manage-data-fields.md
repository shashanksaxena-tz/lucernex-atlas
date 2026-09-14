---
title: "Manage Data Fields"
tags: [screen, administration,configuration]
evidence: Observed
---

`/en/pagebuilder/ReportGroupAvailableFieldEdit.jsp?isGlobal={true|false}`

![The Global scope. 5,953 leaves under 24 top-level groups — and every one of them is read-only to the firm.](../../docs/assets/screenshots/data-fields/manage-data-fields-global.png)
`docs/assets/screenshots/data-fields/manage-data-fields-global.png`

![The Firm scope. 205 leaves, 202 of them beginning `Firm_` — and 147 of the 205 are on Contract alone.](../../docs/assets/screenshots/data-fields/manage-data-fields-firm.png)
`docs/assets/screenshots/data-fields/manage-data-fields-firm.png`

The admin label is *"Manage Data Fields"*; the internal page title is *"Manage Report Group Available
Fields"* — the store is [[ReportGroupAvailableField]].

- Both scopes share **24 top-level groups and 320 subgroups**, and their **leaf paths are entirely
  disjoint**.
- Global **5,953 leaves / 6,297 rows**; Firm **205 leaves / 549 rows**.
- **202 of 205** Firm names start `Firm_`; **0 of 5,953** Global names do.
- Required = Yes: **637** Global, **0** Firm. Read Only = Yes: **0** in both — and that is
  [[security-ladder|correct, not an error]].

**It is read-only to a firm in both tenants**, and
[[finding-firm-fields-are-physical-columns|the reason is DDL]].

See [[data-field-catalog]] · [[feature-data-fields]]

All screens: [[map-of-screens]] · caveat: [[caveat-viewport]]
