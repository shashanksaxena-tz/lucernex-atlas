---
title: "CON-R-131 — Every landed column is TEXT"
tags: [rule, contracts]
evidence: Observed
---

**`CON-R-131`** · [[module-contracts]] · **Observed**

All **1,163** landed Postgres columns are `TEXT`, except **31** `VARCHAR(64)` primary keys. Money
included.

**Every value must be parsed on ingest** — which collides directly with ASG Edge+'s Constitution §4.4
rule that financial code uses `BigDecimal` and never `double`. The parse is where precision is lost if
anyone gets it wrong.

See [[rules-contracts]] for the full register.
