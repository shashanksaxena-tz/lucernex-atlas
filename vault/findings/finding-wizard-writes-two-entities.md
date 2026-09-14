---
title: Contract creation writes across two entities
tags: [finding, contracts, api]
evidence: Observed
---

Step 1 of the [[screen-contract-wizard|contract creation wizard]] collects 35 fields. Alongside the
`Contract_*` fields it carries **`Facility_OpenDate` and `Facility_CloseDate`**.

> **The contract wizard updates the [[Facility]] record in the same step.**

**A rebuild treating creation as a single-aggregate transaction will not reproduce it.**

The [[rest-business-object|REST]] surface makes the mechanism plausible: the request body is a
recursive `BusinessObject` with nested `children[]`, so a contract and records around it can be
written in one call. Whether that write is transactional is
[[q-bbw-15-import-results|not established]], and it matters here more than anywhere — a half-created
contract that has already moved the facility's dates is worse than a failed one.

Two more things the wizard settles:

- **Steps 3 and 4 are [[contract-template|template cloning]], not data entry.**
- **Some fields are computed, not entered.** `TermLength`, `Contract_Firm_FixturingPeriod` and
  `Contract_Firm_LatestCommencementDate` render as `input[type=hidden]` — see
  [[finding-computed-fields-render-as-prose]].

Open: [[q-bbw-09-contract-templates]]
