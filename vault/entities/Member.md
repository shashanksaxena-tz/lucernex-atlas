---
title: Member
tags: [entity, people, core]
evidence: Observed
---

**`member` · 81 fields · [[module-people-parties]]**

An internal user account with a login. **The most-referenced record in the schema — 161 objects, 290
FK columns** — and that number is misleading.

**240 of the 290 (83%) are the universal `CreatedByID` / `ModifiedByID`
[[audit-trail|audit-stamp]] pair.** One cross-cutting concern, not 161 relationships
([[rule-PPL-R-007]]). The genuine business and routing edges number **50**.

`Member` is [[Person]]'s 37-field block **plus 44** login, security and approval columns, on a shared
`PersonID` — see [[Person]], which is a second supertype.

A member's routable identity is **three independent axes**: user class, job title, and the supervisor
org chart ([[rule-PPL-R-009]]). And yet:

- **Production routing barely uses the apparatus** — 17 of 19 live steps at
  [[tenant-american-freight|AF]] route to a **named Member** ([[rule-PPL-R-012]]). See
  [[finding-routing-is-to-named-people]].
- Its **eight approval-amount band columns are read by no observed workflow field**
  ([[rule-PPL-R-013]]). Built, unused.

`Member.SupervisorID` is a self-reference. `MemberAudit` is login/session audit, a different thing from
the field-change [[audit-trail]].

**No real member name appears anywhere in this vault** — [[method-omitting-identities]].
