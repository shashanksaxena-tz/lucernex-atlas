---
title: Computed fields are rendered, not stored
tags: [finding, contracts, data-model]
evidence: Observed
---

On a rendered contract, `Term Length` reads **"5 years 16 days"** — prose, derived at paint time, not
a stored value.

In the [[screen-contract-wizard|creation wizard]] the same field is an `input[type=hidden]`, alongside
`Contract_Firm_FixturingPeriod` and `Contract_Firm_LatestCommencementDate` — **derived during the
wizard rather than captured**.

This matters twice over:

- **A field-by-field migration will carry computed values as if they were data**, and they will then
  drift from the dates that produce them.
- `computed-vs-input-fields.md` classifies **666 accounting fields** INPUT / COMPUTED / CODE-TABLE
  with per-row evidence — and **these are date-family equivalents it does not cover**. The
  classification is incomplete in a dimension nobody had checked.

The general shape is [[setup-schedule-transaction]]'s **projection** layer taken down to the field
level: [[virtual-projection|whole objects]] are computed, and so are individual fields inside
persisted ones.

See [[ContractTerm]] · [[module-accounting]]
