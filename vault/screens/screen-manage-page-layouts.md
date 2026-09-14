---
title: "Manage Page Layouts"
tags: [screen, administration,layouts]
evidence: Observed
---

`/en/pagebuilder/SummaryEntityPageLayoutEdit.jsp?mode={SEP|SUB|LIST}`

![The layout registry. One record type, three modes, one shared builder — and the two modes missing from this dropdown are where the conditional rules turned out to live.](../assets/screenshots/bbw-admin/09-manage-page-layouts.jpg)
`docs/assets/screenshots/bbw-admin/09-manage-page-layouts.jpg` · `af-admin/10-manage-page-layouts.jpg`

A five-way system on one [[PageLayout]] record type, edited through one shared builder
(`LayoutEditorAJAX.jsp`). Row counts at [[tenant-american-freight|AF]]: Summary Pages **17**,
Sub-pages **31**, List Layouts **40**.

**And 93 is not the total.** `mode=ISSUE` and `mode=FORM` silently fall back to `SEP` —
[[finding-form-layouts-are-hidden|42 form layouts are invisible here]], so the real total is 135.

Four things this screen settles:

- A Summary Page section is a **titled wrapper around an independently-managed Sub-page**
  ([[rule-LAY-R-110]]).
- Layouts host placeable **[[action-buttons|business-action buttons]]**, including a distinct
  *"(Run Report Action)"* kind.
- Setup Pages dropdowns mix `[Global Layout]` platform defaults with `ASG *` tenant overrides — the
  [[entity-scoped-vs-firm-global|two-tier pattern]] again.
- Edit Layout and List Layout keep **independent** [[conditional-field]] configuration on the same
  record ([[rule-LAY-R-120]]).

![The Add Item modal — where a placement is created, and where the "(Run Report Action)" kind shows up.](../assets/screenshots/page-layouts/page-layouts-add-item-modal.png)
`docs/assets/screenshots/page-layouts/page-layouts-add-item-modal.png`

See [[feature-page-layouts]] · [[layout-modes]] · [[screen-layout-changes]]

All screens: [[map-of-screens]] · caveat: [[caveat-viewport]]
