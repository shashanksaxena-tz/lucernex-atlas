---
title: "Q-BBW-15 — Is a partial write transactional?"
tags: [open-question, api]
evidence: Observed
status: open
---

Writes return `ImportResults` with `successes[]` and `errors[]`, so
[[finding-http-200-is-not-success|HTTP 200 does not mean success]].

**Two things follow that are not established:**

1. **What is the full `ImportError` vocabulary?** A caller that must inspect `errors[]` needs to know
   what can appear there.
2. **Is a partial write transactional, or does it leave a half-created aggregate?**

The second is the dangerous one. The request body is a recursive `BusinessObject` with nested
`children[]`, so **a contract and its children go in one call** — and the
[[screen-contract-wizard|wizard]] additionally
[[finding-wizard-writes-two-entities|writes across two entities]]. If a partial failure leaves the
[[Facility]] dates moved and no [[Contract]] created, the failure mode is worse than a rejection.

There is **no dry-run parameter**, and the UI defaults to *stop on first error*.

### How to settle it

The `ImportError` / `ImportResults` schemas are in the captured OpenAPI spec and can be read now.
**Determining transactionality requires a write**, which is out of scope under
[[method-read-only-exploration]].
