---
title: "Main navigation — the whole product in four roots"
tags: [screen, navigation,end-user]
evidence: Observed
---

`/en/dashboard/DashboardDispatch.jsp — hamburger, top left`

![The four roots, expanded. Notice there is no way to *create* anything here — this is navigation within a record that already exists.](../assets/screenshots/navigation/main-navigation-four-roots.jpg)
`docs/assets/screenshots/navigation/main-navigation-four-roots.jpg`

Read out of the `Lx.ui.MenuTree` ExtJS component. **Four roots — Portfolio, [[Location]],
[[Facility]], [[Contract]] — 24 groups and 81 screens**, 109 nodes at depth 3. [[tenant-bbw|BBW]] adds
a fifth, [[equipment-contract|Equipment Contract]], for 141.

- Every root opens with the same six: `Summary · Members/Contacts · Forms · Work Flow · Documents ·
  Binders`.
- [[Contract]] alone carries **39** of the 81 screens.
- `Accounting Info` keeps the classification test and the rent schedule as **separate** screens —
  because one is a detail form and the other a list ([[finding-two-files-serve-56-percent]]).
- IFRS 16 has a screen and **no configured schedule types** — capability present, unused.

**This tree is not the whole product.** The [[feature-administration|57 admin tools]] are a separate
surface, and **14 menu structures with 892 nodes** exist against the 4–5 that render — see
[[finding-root-renders-iff-record-exists]].

See [[navigation-tree]]

All screens: [[map-of-screens]] · caveat: [[caveat-viewport]]
