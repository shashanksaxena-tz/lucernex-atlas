---
title: RETransaction
tags: [entity, portfolio, deal-pipeline]
evidence: Observed
---

**`r_e_transaction` · 31 fields · [[module-portfolio-transactions]]**

The formal real-estate transaction, once a [[Scenario]] converts to a live deal. Middle of the
pre-lease chain: [[PotentialProject]] → `RETransaction` → [[Scenario]].

- `ProgramID` is **required** — a transaction must belong to a Portfolio ([[rule-POR-R-013]]).
- `RelatedTransactionID` is a self-reference.
- Out-degree 8 targets across 14 columns.
- Its deal schedules reuse [[TaskGroup]] directly — no scheduling engine of its own
  ([[rule-PRJ-R-013]]).

Four code tables classify overlapping aspects of this one pipeline — `Deal Type Code` (`2024`),
`RE Transaction Status Code` (`2057`), `Scenario Deal Type Code` (`2059`), `Scenario Type Code`
(`2060`) — and **none of their row values has ever been captured** ([[rule-POR-R-005]]).
