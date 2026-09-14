---
title: "Manage Forms"
tags: [screen, administration,configuration,workflow]
evidence: Observed
---

`/en/admin/FirmCodeEdit.jsp?includeType=Manage&TableType=2035`

![The form types. Look at the route: this is the generic code-table editor with `TableType=2035`. A Form is an Issue Type.](../assets/screenshots/bbw-admin/05-manage-forms.jpg)
`docs/assets/screenshots/bbw-admin/05-manage-forms.jpg` · `af-admin/06-manage-forms.jpg`

![Expanded to show every layout under every form type. An N-step workflow carries N+1 layouts, and this is where the 42 hidden form layouts live.](../assets/screenshots/forms/manage-forms-expanded-all-layouts.jpg)
`docs/assets/screenshots/forms/manage-forms-expanded-all-layouts.jpg`

**The route is the finding.** `Manage Forms` administers [[code-table]] `TableType = 2035`
(`Issue Type Code`) — so **[[form-vs-page|a Form *is* an Issue Type]]** ([[rule-LAY-R-161]]).

Six form types at [[tenant-bbw|BBW]]: `ASC 842 Tracking`, `Change Request`, `Lease Admin Request`,
`QC Request`, `User Request`, `Vendor Changes (Integration)`.

**This screen is the only route to the 42 form layouts** — [[finding-form-layouts-are-hidden]] — and
therefore the only route to where [[conditional-field|conditional fields]] are actually used.

Attachability is **11 `IsValidFor…` booleans** on [[CodeIssueType]].

See [[feature-workflows-forms]]

All screens: [[map-of-screens]] · caveat: [[caveat-viewport]]
