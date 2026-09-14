---
title: "LAY-R-120 — One layout, two coordinate sets"
tags: [rule, layouts-and-forms]
evidence: Observed
---

**`LAY-R-120`** · [[module-layouts-and-forms]] · **Observed**

One `PageLayoutID` can carry **both** a detail Edit Layout and a grid List Layout, with **separate
coordinate sets**.

[[PageLayoutField]] holds three in parallel — `Edit*`, `View*`, `Header*` — with `-1` meaning "not
placed". So a single placement row describes a field's position in three different renderings, and
[[feature-page-layouts|the two modes keep independent conditional configuration]].

See [[rules-layouts-and-forms]] for the full register.
