---
title: "ACC-R-013 — A locked financial test is immutable"
tags: [rule, accounting]
evidence: Observed
---

**`ACC-R-013`** · [[module-accounting]] · **Observed**

A locked [[ContractFinancialTest]] **cannot be modified or deleted**. Supersede it by creating a new
row.

So lease classification history is **append-only** — consistent with the module's general
delete-and-regenerate posture ([[rule-CON-R-010]]) and with
[[finding-schedules-are-approved-not-published|irreversible approval]].

See [[rules-accounting]] for the full register.
