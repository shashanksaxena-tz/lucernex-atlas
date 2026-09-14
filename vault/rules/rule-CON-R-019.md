---
title: "CON-R-019 — Direction is per clause, not per contract"
tags: [rule, contracts]
evidence: Observed
---

**`CON-R-019`** · [[module-contracts]] · **Observed**

Payable-versus-receivable direction is carried **per clause and per transaction**, never on the
[[Contract]]. **One contract may be both.**

A rebuild that puts a direction flag on the lease header cannot express a sublease that pays rent up
and collects rent down. See [[PaymentTransaction]] · [[PaymentReceipt]].

See [[rules-contracts]] for the full register.
