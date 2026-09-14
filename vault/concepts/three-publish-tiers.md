---
title: Three publish tiers — and only one is versioned
tags: [concept, tenancy, configuration]
evidence: Observed
---

Configuration moves along three distinct channels, and the discipline drops off a cliff between the
first and the second.

| Tier | Mechanism | Versioned | Lineage kept |
|---|---|:--:|:--:|
| **Accruent → firm** | [[screen-import-best-practice-templates\|Import Best Practice Templates]] | **Yes** — `Version` / `Min Version` / `Released` | unknown |
| **Firm → firm, env → env** | [[screen-export-configuration\|Export Configuration]] XML, [[publish-and-fork\|clone or move]] | **No** | **No** — clone discards it |
| **Within a firm** | direct layout editing | No | — |

The vendor tier is the closest prior art available for the [[hub-and-spoke]] publish rule that is not
yet written down anywhere. A package carrying a **`Min Version`** is a real compatibility contract
between a configuration package and the platform release it installs onto, and `Released` separates
published from draft. That is the shape of *"never more than one version behind"*, already
implemented — **at the wrong tier for ASG**.

**And the gap is precisely where ASG operates.** ASG publishes its layout set into each client tenant
through the *unversioned, lineage-less* tier. That is the whole explanation for
[[finding-publish-then-fork]].

Two further observations from the same screen: **package dependencies are prose, not modelled**
(*"IMPORTANT: Import the Budget Package first"* appears twice, with nothing enforcing it), and a
**dev → Train → production progression** is assumed.

**Note what is absent.** All seven vendor packages target bidding, budgets, cost tracking, RFI and
folder templates — very nearly the exact set ASG Edge+ has ruled out of scope. Accruent ships **no**
best-practice package for lease accounting, contracts or ASC 842. The channel exists; it is empty for
the product's core.

Source: [`tenants/bbw-vs-american-freight.md` §20](../../docs/tenants/bbw-vs-american-freight.md)
