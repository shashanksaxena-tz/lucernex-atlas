---
title: "CON-R-103 — Five independent date axes"
tags: [rule, contracts]
evidence: Observed
---

**`CON-R-103`** · [[module-contracts]] · **Observed**

**Posting, effective, due, coverage and settlement dates must all coexist** on a
[[PaymentTransaction]].

A rebuild that collapses any two of them loses a distinction the incumbent uses — most obviously
coverage (what period the money is *for*) versus posting (when it hit the ledger).

See [[rules-contracts]] for the full register.
