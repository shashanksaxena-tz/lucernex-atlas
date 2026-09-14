---
title: Publish and fork
tags: [concept, tenancy, configuration, core]
evidence: Observed
---

ASG maintains **one standard configuration set and deploys a copy into each client tenant**, where it
is re-keyed and then drifts. The product names the mechanism itself, on the
[[screen-export-configuration|Export Configuration]] screen:

> ☐ **Clone these layouts in this firm and environment** (new layouts/fields created when this xml is
> imported)
> *Do not check this if you are moving layouts, forms,… from one environment to another or one firm
> to another*

| Mode | Effect |
|---|---|
| **Clone** checked | New layouts and fields created on import — **new ids** |
| **Clone** unchecked | Moving between environments or firms — **identity preserved** |

ASG exported its template set and imported it with **Clone checked**. That is exactly why
[[finding-publish-then-fork|80 layouts match by name and none by id]], with the offsets clustered in
one narrow band.

**The failure mode is the finding.** Clone-on-import leaves the copy with **no pointer back to the
original** — no source id, no version stamp. Two tenants diverged silently, and the only way to tell
they came from one source is to join on name and notice the id offset. ASG Edge+ should keep the
lineage Lx discards.

The estate actually runs **three** distribution models, and telling them apart matters as much as the
pattern:

| Model | Applies to | Signature |
|---|---|---|
| **Platform-seeded and shared** | navigation nodes, the 227-table catalog | identical ids across tenants |
| **Published, then forked** | [[page-layout-concept|page layouts]], [[code-table]] values | matching names, disjoint ids |
| **Tenant-authored** | [[workflow-template|workflow templates]] | names mostly differ, no id pattern |

Treating a published-then-forked surface as tenant-authored loses the template; treating it as
platform-seeded loses the fork. See also [[three-publish-tiers]].

Source: [`tenants/bbw-vs-american-freight.md` §19](../../docs/tenants/bbw-vs-american-freight.md)
