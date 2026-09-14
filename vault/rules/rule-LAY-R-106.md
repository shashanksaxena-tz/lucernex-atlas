---
title: "LAY-R-106 — A URL bypasses the layout entirely"
tags: [rule, layouts-and-forms]
evidence: Observed
---

**`LAY-R-106`** · [[module-layouts-and-forms]] · **Observed**

A [[PageLayout]] with a **non-blank `URL`** bypasses its field configuration completely and redirects
to that system page.

So a layout in the registry may render nothing it declares. Any inventory that counts placements
without checking `URL` over-counts configured screens.

See [[rules-layouts-and-forms]] for the full register.
