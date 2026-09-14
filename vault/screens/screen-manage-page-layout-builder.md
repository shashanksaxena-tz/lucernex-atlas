---
title: "The layout builder"
tags: [screen, administration,layouts]
evidence: Observed
---

`/en/pagebuilder/LayoutEditorAJAX.jsp?formSubmit=editBO&popupEdit=true&buildLayout=true&PageLayoutID={id}`

![An Edit Layout — fields placed on a canvas, with the Available Fields palette on the left.](../assets/screenshots/page-layouts/page-layouts-contract-payments-edit-layout.png)
`docs/assets/screenshots/page-layouts/page-layouts-contract-payments-edit-layout.png`

![The List Layout on the *same* PageLayoutID — separate coordinates, separate conditional configuration.](../assets/screenshots/page-layouts/page-layouts-contract-payments-list-layout.png)
`docs/assets/screenshots/page-layouts/page-layouts-contract-payments-list-layout.png`

One builder for every [[layout-modes|mode]], driven by a `layoutMode` discriminator. The two captures
above are **one record** ([[rule-LAY-R-120]]) — [[PageLayoutField]] holds `Edit*`, `View*` and
`Header*` coordinates in parallel.

The palette is the [[data-field-catalog]] tree, and it links straight into
[[custom-list|Custom Lists]]:

![The Available Fields palette, with its link into Custom Lists.](../assets/screenshots/page-layouts/page-layouts-available-fields-custom-lists-link.png)
`docs/assets/screenshots/page-layouts/page-layouts-available-fields-custom-lists-link.png`

**Three cautions for anyone using this screen as evidence:**

1. **The red asterisk is [[finding-no-layout-level-required|schema-required, not a layout property]]**
   — and red text on a *field label* is an editor affordance that does not reach the end user.
2. **Only one builder can be open per session.** Concurrent iframes collide; any sweep must be serial.
3. **[[method-fetch-is-not-render|Fetching this page finds nothing]]** — `conditionOptions(...)` calls
   are injected client-side.

![Conditional field associations, shown on a placement.](../assets/screenshots/page-layouts/page-layouts-conditional-field-associations.png)
`docs/assets/screenshots/page-layouts/page-layouts-conditional-field-associations.png`

See [[screen-manage-page-layouts]] · [[screen-conditional-filter-editor]]

All screens: [[map-of-screens]] · caveat: [[caveat-viewport]]
