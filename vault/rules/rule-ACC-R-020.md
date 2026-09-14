---
title: "ACC-R-020 — Schedule-type changes flag recalculation"
tags: [rule, accounting]
evidence: Observed
---

**`ACC-R-020`** · [[module-accounting]] · **Observed**

Changing the ASC 842 / IFRS 16 schedule type on **Assumptions, [[Covenant|Covenants]] or Recurring
Expenses** sets [[SLSummary]]`.NeedsRecalculation`.

The engine **marks itself stale and waits for a human** — see
[[finding-engine-is-button-driven]]. Note [[Contract]]'s 120 rollup fields have no equivalent flag
([[rule-CON-R-026]]).

See [[rules-accounting]] for the full register.
