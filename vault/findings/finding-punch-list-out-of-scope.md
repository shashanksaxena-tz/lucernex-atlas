---
title: The census gap is smaller than it looked, and what remains is out of scope
tags: [finding, data-model, scope]
evidence: Observed
---

`ShowObjectDetails.jsp` offers **227** tables against a **223-object** census. An earlier reading
reported *"~34 tables genuinely absent"*, derived by matching **UI labels** against the catalog.
**That number was an artefact of the matching key.**

| Match key | Tables flagged absent |
|---|---:|
| UI label only | 18 |
| **Physical name** | **6** |

**Twelve of the eighteen were label mismatches, not gaps.** Ten are [[virtual-projection|`Virtual*`]]
views the UI renames — and one is **[[ProjectEntity]] itself, labelled *"General Entity Info"***. See
[[caveat-labels-are-tenant-local]] and [[method-cheap-signals]].

**The six genuine omissions:** `ChangeManage` (1 field), `VirtualTemplateMember` (1), and the
four-table **`Punch List` family** (33 fields between them).

**The Punch List family is out of scope by the BRDs' own architecture.** All 38 approved BRDs were
searched: `punch`, `snag`, `defect list` and `site survey` return **zero files**, against a control
term (`contract`) hitting 31 — so the absence is real, not a failed search. More decisively, two BRDs
describe *"the existing ASG Edge system (the deal-making and **construction management** platform)"*
as a **separate product**. Punch List is snagging, which is construction management, so it belongs to
legacy ASG Edge by the BRDs' own statement — **assigned elsewhere, not merely unrequested**.

**Which leaves the in-scope census gap at two one-field tables.**

### The composition is the finding

**31 of 227 undocumented = 6 omissions + the 25 tables the viewer refuses.** The story is a
**viewer withholding its own configuration tables**, not a census that missed things — and the refused
25 are the platform's own machinery: [[PageLayout]], [[PageLayoutField]], [[PageLayoutFilter]],
`CustomCodeTable`, `Dashboard`, `Job Log`, `Audit Master`, `Notify Template`, `Grid Preference`. All
are recoverable over [[rest-business-object|REST]].

Open: [[q-bbw-13-census-gap]]
