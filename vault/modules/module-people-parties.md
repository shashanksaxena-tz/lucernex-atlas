---
title: People and parties
tags: [module, people]
evidence: Derived
---

**10 objects · 301 fields · rules `PPL-R-001`…`PPL-R-013`**

Everyone the system knows about — and the load-bearing finding is that **[[Person]] is a second
supertype**, alongside [[ProjectEntity]].

Entities: [[Member]] · [[Person]] · [[NonMember]] · [[Employer]] · [[Organization]]

- [[Person]] and [[NonMember]] are **field-for-field identical**; [[Member]] is that block plus 44
  login columns, on a shared `PersonID` ([[rule-PPL-R-001]]).
- **There is no `Vendor`, `Landlord` or `Tenant` object.** All three are [[Employer]]
  ([[rule-PPL-R-004]]).
- [[Member]] has **290 inbound FKs and 240 of them are [[audit-trail|audit stamps]]**
  ([[rule-PPL-R-007]]).
- A member's routable identity is three axes — and **production routing barely uses them**
  ([[finding-routing-is-to-named-people]]).
- The eight approval-amount band columns on [[Member]] are read by **no** observed workflow field
  ([[rule-PPL-R-013]]).

**The module's largest evidence gap:** six Member Administration admin routes are Observed and **none
of the six screens was opened**.

Rules: [[rules-people-parties]] ·
[`modules/people-parties/`](../../docs/modules/people-parties/README.md)
