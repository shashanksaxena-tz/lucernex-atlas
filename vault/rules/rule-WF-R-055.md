---
title: "WF-R-055 — The engine can write exactly one field"
tags: [rule, workflow]
evidence: Derived
---

**`WF-R-055`** · [[module-workflow]] · **Derived**

`CodeLastActionStatusID` is **the engine's only field-write capability**.

A workflow in this product **cannot set any other field on any record**. Combined with
[[rule-LAY-R-166e]] — no mechanism for passing values between steps — the engine is a router that
moves work and records a status, and nothing more.

Anything ASG Edge+ needs beyond that is new build.

See [[rules-workflow]] for the full register.
