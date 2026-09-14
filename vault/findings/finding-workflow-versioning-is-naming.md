---
title: Workflow versioning is a naming convention, not a feature
tags: [finding, workflow]
evidence: Observed
---

The current [[WorkFlowTemplate|template]] is the **unsuffixed** one; `v1` and `v2` are archived
predecessors.

| | Steps |
|---|---:|
| `Lease Admin Request` (current) | **8** |
| `Lease Admin Request v2` (archived 03.26.26) | 10 |
| `Lease Admin Request v1` (archived 09.22.25) | 8 |

**So the current workflow has fewer steps than the version it replaced** — which is exactly the kind
of thing an auditor asks about.

> **The archival fact is recorded as free text in the description field** — *"Workflow has been
> archived and replaced on 09.22.25"* — **not as a status, an effective-date range, or a supersession
> foreign key.**

**A rebuild needing auditable workflow versioning cannot copy this.** It must model version, effective
dates and supersession as first-class fields.

Note the contrast with [[three-publish-tiers|the vendor's own configuration packages]], which *do*
carry `Version`, `Min Version` and `Released`. The discipline exists in the product. It is simply not
applied here.

Workflows are also **tenant-authored rather than [[publish-and-fork|forked]]** — only 2 of AF's 4
templates share a name with BBW's 13, and there is **no clustered id-offset block**. So this is not a
case of a versioned template set drifting; each tenant wrote its own.

See [[feature-workflows-forms]]
