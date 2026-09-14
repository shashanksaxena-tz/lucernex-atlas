---
title: The security ladder
tags: [concept, security, core]
evidence: Observed
---

Privilege is granted to a **user class** over four kinds of thing, one per tab of `Manage Security`,
on a five-value ladder.

| Surface | What is secured | Levels |
|---|---|---|
| Page Access | navigation and layout pages | `NoAccess` `View` `Edit` `Delete` `Default` |
| Actions | **70 named verbs** | no `Delete` |
| Field Security | **6,553 individual fields** | no `Delete` |
| Budget Columns | budget columns | *(not read)* |

**`Default` means *inherit* — "not explicitly granted" — not "granted."** Reading it as an effective
grant is what produced and then destroyed a confident hypothesis about
[[finding-root-renders-iff-record-exists|why a navigation root fails to render]].

**Read-only is `View` on a field.** That is why the [[data-field-catalog]]'s uniform `ReadOnly = No`
across all 6,158 leaves is correct rather than anomalous: definition-level and per-class grant measure
different questions.

Scale, for anyone planning to migrate it: `SecurityFieldSecurity.jsp` is a **5.0 MB page** with 6,553
field nodes and **26,212 radio inputs**.

[[Security]] itself has **no physical table** — it is a computed read-only projection of the editable
[[UserClassSecurity]] grant, and the two declare 21 fields each, identical name for name
([[rule-PLT-R-006]]).

One trap: `Is ReadOnly?` and `Read Only?` on that page are **names of secured data fields**, not
access levels.

Source: [`features/security-access/`](../../docs/features/security-access/README.md)
