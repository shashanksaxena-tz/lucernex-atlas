---
title: "Manage Security"
tags: [screen, administration,security]
evidence: Observed
---

`/en/admin/SecurityPageAccess.jsp?UserClass={id}`

![The Page Access matrix. Careful: it loads on "Default Security", a class that denies almost everything — reading the blank matrix as "unselected" is a trap.](../assets/screenshots/bbw-admin/38-manage-security.jpg)
`docs/assets/screenshots/bbw-admin/38-manage-security.jpg` · `af-admin/39-manage-security.jpg`

Four tabs, four securable kinds — Page Access, **Actions (70 verbs)**, **Field Security (6,553
fields)**, Budget Columns. See [[security-ladder]].

**The class selector is a GET parameter**, so all ten user classes can be read with no UI interaction
at all — which is how [[finding-root-renders-iff-record-exists|page access was eliminated as a gate]].

Three traps on this one screen:

1. **`Default` means *inherit*, not *allowed*.** [[Program]] is `Default` for all ten classes and
   renders for none.
2. **Tabs default to different classes** — Page Access opens on `Default Security` (`7884`), Field
   Security on `System Administrator` (`7885`).
3. **`Is ReadOnly?` and `Read Only?` are names of secured data fields**, not access levels.

Scale: `SecurityFieldSecurity.jsp` is a **5.0 MB page with 26,212 radio inputs**.

All screens: [[map-of-screens]] · caveat: [[caveat-viewport]]
