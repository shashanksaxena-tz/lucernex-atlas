---
title: "Q-BBW-09 — What backs a contract template?"
tags: [open-question, contracts, data-model]
evidence: Observed
status: open
---

Steps 3 and 4 of the [[screen-contract-wizard|contract wizard]] clone [[Covenant]] and
[[Responsibility]] entries from a **[[contract-template|contract template]]** — and **no
`ContractTemplate` object exists in the 223-object census**.

So contract templates are a first-class creation mechanism with nothing in the schema backing them.
Either they are ordinary [[Contract]] rows flagged somehow, or there is a table the census does not
carry — and the census is [[finding-punch-list-out-of-scope|known to be missing 25 tables the viewer
refuses]].

### A second question from the same screen

**Step 1 writes `Facility_OpenDate` and `Facility_CloseDate`** — creation spans two entities
([[finding-wizard-writes-two-entities]]). **Is that transactional?** If a half-created contract has
already moved a [[Facility]]'s dates, the failure mode is worse than a rejected create. Related:
[[q-bbw-15-import-results]].

### How to settle it

(a) Run `ShowObjectDetails.jsp` against the source of the wizard-template dropdown.
(b) Open a contract record and check whether the Facility dates round-trip.
