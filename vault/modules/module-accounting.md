---
title: Accounting
tags: [module, accounting]
evidence: Observed
---

**19 objects · 666 classified fields · rules `ACC-R-001`…`ACC-R-062`**

ASC 842, IFRS 16 and straight-line — and they are **not three modules**. See
[[one-engine-three-standards]].

Entities: [[SLSummary]] · [[SLPeriod]] · [[ContractFinancialTest]] · [[AccrualTransaction]] ·
[[PaymentTransaction]] · [[PaymentReceipt]] · [[DiscountRate]] · [[EscalationIndex]] ·
[[ExpenseSetup]] · [[ExpenseSchedule]] · [[ExpenseAccrualSchedule]] · [[ExpenseEscalation]]

What the module settles:

- Classification is a separate 93-field record, and **its polarity is inverted** —
  [[finding-classification-polarity-inverted]].
- A schedule is a candidate that must pass a **three-step approval**, and approval is irreversible —
  [[finding-schedules-are-approved-not-published]].
- The engine is **user-triggered from buttons on a record** —
  [[finding-engine-is-button-driven]].
- It runs **per [[Asset]], not only per [[Contract]]** — [[finding-accounting-runs-per-asset]].
- **Only one standard is configured.** `ASC 842 Schedule Type Code` holds 1 row; the straight-line and
  IFRS 16 tables are empty.
- **The initial asset balance formula is not documented anywhere** ([[rule-ACC-R-033]]). Do not code
  it from the schema.

And the hole underneath: [[finding-discount-rate-table-empty]].

`computed-vs-input-fields.md` classifies **666 accounting fields** INPUT / COMPUTED / CODE-TABLE /
ACTION / DEAD / FK / SYSTEM with per-row evidence — the primary feed for a rule engine.

Rules: [[rules-accounting]] ·
[`modules/accounting/`](../../docs/modules/accounting/README.md)
