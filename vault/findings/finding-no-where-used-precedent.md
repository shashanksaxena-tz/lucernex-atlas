---
title: "Retraction: code-table delete protection is not a Where-Used check"
tags: [finding, retraction, configuration, asg-edgeplus]
evidence: Observed
---

> **An earlier revision inferred that `delete` is suppressed when a [[code-table]] value is
> referenced — and argued that Lx therefore already performs the "Where Used" check ASG Edge+'s
> `D-07` ruled out of scope, so `MST-015` should be reopened. That inference is withdrawn. It was
> wrong, and the argument built on it should not be acted on.**

Two pieces of evidence retired it.

**1. The difference was a build difference, not a tenant difference.**
[[tenant-american-freight|American Freight]] has since been upgraded to `26.09.0.113` — the same build
[[tenant-bbw|BBW]] runs — and on that build `AI Abstracted` at AF offers edit only, exactly as at BBW.
The asymmetry the inference rested on **no longer exists**.

**2. The mechanism is a per-row boolean, read directly from the renderer.** The Actions column
(`EditDeleteLink`) reads, verbatim:

```js
var q = c.data.isReadOnlyRecord;
if (!q) { /* edit | delete */ } else { /* edit only */ }
```

**There is no count, threshold or usage lookup anywhere in the render path.** `isReadOnlyRecord` is
supplied per row by the server; the `FirmCode` record exposes four fields and no provenance or
reference-count attribute.

**The decisive case:** `TableType 3006` ([[KeyDate|Key Date Type Code]]) contains **two rows both named
`Option`** — `LxBOID 3095` protected, `LxBOID 3116` deletable. **Identical name, opposite flag.** A
reference count cannot produce that. Nor could it produce `Covenant Status Code` (`2157`), where
`Active` is deletable while `AI Abstracted` is protected — the exact inversion of a usage-based rule.

Full scan at AF: **1,140 values — 154 protected, 986 deletable**; 23 tables all-protected, 38
all-deletable, 12 mixed.

**Best current reading (Inferred, not proven):** the flag marks **platform-seeded rows** a firm may
rename but not delete. It fits every mixed table. The discriminating test is whether the same `LxBOID`
ever carries a different flag across tenants — [[q-bbw-01-isreadonlyrecord]].

**What ASG Edge+ should take from this:** the platform does protect seeded values from deletion, and a
rebuild needs that notion — which still bears on `D-07` and `DeactivationPolicy`. But it is **not**
evidence of a Where-Used capability, and **`MST-015` remains unsupported by anything observed here**.

See [[method-cheap-signals]] · [[evidence-labels]]
