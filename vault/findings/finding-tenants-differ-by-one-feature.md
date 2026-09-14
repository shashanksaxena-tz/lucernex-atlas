---
title: The two tenants differ by one feature, not by general drift
tags: [finding, tenancy, integration]
evidence: Derived
---

An earlier reading held that "[[tenant-bbw|BBW]] is the more advanced fork" and
[[tenant-american-freight|AF]] retains superseded versions. **That overstates it.**

**Almost every BBW-only layout is the `ASG Lease Abstract - *` family** — Contract Term, Covenants,
Expense Schedule, Expense Setup, Key Dates, Percent Rent, Funds and Expenses — which serves the
[[atlas-ai-abstraction|Atlas AI lease-abstraction pipeline]] that BBW has switched on and AF does not
use.

That is a far more precise statement than "drift", and it **changes the rebuild question** from
*"why have these tenants diverged?"* to *"is AI lease abstraction in scope for ASG Edge+?"* —
[[q-bbw-17-ai-abstraction-in-scope]].

Four observations the corpus had recorded separately, with no explanation, are **one feature**:

| Observation | |
|---|---|
| `Allow AI Lease Abstraction` is a [[Firm]] entitlement flag | |
| BBW has seven `ASG Lease Abstract - *` layouts AF lacks | |
| `AI Abstracted` is a value in four status [[code-table\|code tables]] | |
| `AI Abstracted` became **delete-protected** in build `26.09` | |

The last of those **retires the corpus's claim that `AI Abstracted` is "a tenant-added status"** — it
reads as the vendor promoting the path from a tenant convention to shipped functionality. *(Inferred
— the flag change was observed across builds, not the value's origin.)*

The abstraction layouts also match **one for one** the financial layers stepped through by the
`Implementation Workflow - Financial Abstraction` workflow — see [[finding-maker-checker-pairs]].

And the whole difference is visible at all only because **one row exists** —
[[finding-root-renders-iff-record-exists]].

Compare [[finding-publish-then-fork]], which this refines.
