---
title: "POR-R-001 — Portfolio policy resolves before Firm"
tags: [rule, portfolio-transactions]
evidence: Observed
---

**`POR-R-001`** · [[module-portfolio-transactions]] · **Observed**

`Contract.ProgramID` resolves **discount rate, thresholds, fiscal year and FX** at the [[Program]]
level **before** falling back to [[Firm]].

Which is why [[DiscountRate]] carries Portfolio as one of its seven lookup dimensions
([[rule-ACC-R-001]]).

See [[rules-portfolio-transactions]] for the full register.
