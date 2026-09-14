---
title: "RPT-R-036 — Reports can select unmaterialised period series"
tags: [rule, reporting]
evidence: Derived
---

**`RPT-R-036`** · [[module-reporting]] · **Derived**

Because [[virtual-projection|`Virtual*`]] objects are computed projections exposed as tables, **reports
can select calculated period series that were never materialised.**

The same capability turns up on the screen side as
[[finding-layouts-over-projections|layouts built on projections]] — so this is not a reporting quirk,
it is how the product treats read models generally.

See [[rules-reporting]] for the full register.
