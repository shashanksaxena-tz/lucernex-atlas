---
title: "Import Best Practice Templates"
tags: [screen, administration,import-export,tenancy]
evidence: Observed
---

`/en/admin/BestPracticeTemplates.jsp`

![Seven versioned packages, with Version, Min Version and Released columns. This is the only tier of configuration publishing in the entire product that is versioned.](../assets/screenshots/bbw-admin/13-import-best-practice-templates.jpg)
`docs/assets/screenshots/bbw-admin/13-import-best-practice-templates.jpg` · `af-admin/14-import-best-practice-templates.jpg`

**Accruent's own publish channel into a tenant.** Seven configuration packages — layouts, forms and
workflows shipped as units — with `Version`, **`Min Version`** and `Released`.

| Package | Version | Min Version |
|---|---:|---:|
| Bidding Sub-Module Package | 1.8 | 20.10 |
| Budget Package — Site and Project Standard Budget Items | 4.4 | 19.12 |
| Folder Template — RE Contracts | 1.9 | 19.12 |
| Folder Template — Sites and Projects | 2.9 | 19.12 |
| Package — GC Bidding | 1.0 | 19.12 |
| Project Cost Tracking Package | 4.1 | 20.2 |
| Request for Information (RFI) | 2.3 | 19.12 |

**`Min Version` is a real compatibility contract** between a configuration package and the platform
release it installs onto. That is the shape of the Hub→Spoke *"never more than one version behind"*
rule, **already implemented — at the vendor tier, not the tier ASG operates in**. See
[[three-publish-tiers]].

Two weaknesses on the same screen: **package dependencies are prose, not modelled** (*"IMPORTANT:
Import the Budget Package first"*, with nothing enforcing it), and a dev → Train → production
progression is assumed rather than expressed.

**Note what is absent.** All seven target bidding, budgets, cost tracking, RFI and folder templates —
very nearly the exact set ASG Edge+ has ruled out of scope. **Accruent ships no package for lease
accounting, contracts or ASC 842.** The channel exists; it is empty for the product's core.

All screens: [[map-of-screens]] · caveat: [[caveat-viewport]]
