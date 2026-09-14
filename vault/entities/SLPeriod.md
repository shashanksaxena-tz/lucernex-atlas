---
title: SLPeriod
tags: [entity, accounting]
evidence: Observed
---

**`s_l_period` · 79 fields · [[module-accounting]]**

The period-level detail under [[SLSummary]] — one row per accounting period of a schedule, carrying
the present-valued cash amount that the summary sums.

Carries a nullable `AssetID`, alongside [[SLSummary]] and [[ContractFinancialTest]] — the three
together are [[finding-accounting-runs-per-asset]].

Note the naming collision: the layout `Straight-Line Schedule` primary table resolves **ambiguously**
across `SLSummary`, `SLPeriod` and `CodeSLSchedule`, and pinning it is [[q-bbw-10-straight-line-table]].

A [[fiscal-period|"period"]] here is whatever the firm's fiscal calendar defines, which may be a
4-4-5 quarter or one of 13 slots — not necessarily a month.
