---
title: Scenario
tags: [entity, portfolio, deal-pipeline]
evidence: Observed
---

**`scenario` · 69 fields · [[module-portfolio-transactions]]**

Comparative what-if deal terms for a prospective site or renewal — the end of the pre-lease pipeline.

Requires `RETransactionID`, `ProjectEntityID` and `ScenarioDealType`; `ScenarioType` is optional
([[rule-POR-R-014]]).

**`Scenario.ContractID` is one-way.** [[Contract]] has no reverse column, so **a signed lease cannot
be traced back to the deal that produced it** ([[rule-POR-R-004]]). Together with
[[PotentialProject]]'s zero inbound edges, that means the whole pre-lease pipeline is
unreconstructible from the record it produces.

Its deal type and [[RETransaction]]'s preferred deal type draw from one code table and **nothing
enforces agreement** ([[rule-POR-R-015]]).
