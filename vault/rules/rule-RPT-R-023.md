---
title: "RPT-R-023 — Reporting is pivot-shaped, not flat-list"
tags: [rule, reporting]
evidence: Observed
---

**`RPT-R-023`** · [[module-reporting]] · **Observed**

The same [[PageLayoutFilter]] row that filters also **groups** — `RowOrderBy` and `ColumnOrderBy`.

So the reporting model is a **pivot**, not a filtered list. A rebuild offering flat tabular reports
would be offering less than the incumbent, and offering pivots is a different UI problem entirely.

*(Observed, plus Inferred for the pivot reading.)*

See [[rules-reporting]] for the full register.
