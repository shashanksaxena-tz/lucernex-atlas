---
title: "Q-BBW-20 — What is the intended Lease Status sequence?"
tags: [open-question, contracts, business]
evidence: Observed
status: open
---

**Answered:** the [[contract-lifecycle]] lives in `Lease Status`, a firm-defined
[[client-drop-down]], with four of BRD-24's five stages present.

**What remains open is a business question with a design consequence.**

[[finding-lifecycle-has-no-ordering|`SortOrder` is null on all seven values]], so **the platform
stores no ordering, no transitions and no state machine.** The sequence exists only as convention.

> **A rebuild modelling an ordered state machine is making a decision, not migrating one.**

Two specifics to put in front of whoever owns BRD-24:

- **`Active` is absent as a standalone value** — it appears only inside the compound
  `Closed - Active`.
- **Two stages the BRD does not name exist in production**: `Future Possession` and
  `Accounting Purposes Only` (which suggests contracts carried for ASC 842 measurement while
  operationally dormant).

### How to settle it

Confirm the intended sequence, and whether the compounds are two states or one.

Note the vocabulary does exist elsewhere in the product: `Facility Status Code` carries `Open`,
`Closed` and `Possession` — on the [[Facility]], not the lease.
