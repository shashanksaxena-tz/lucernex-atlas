---
title: Form layouts are a hidden sub-system — and that is where the rules live
tags: [finding, layouts, workflow]
evidence: Observed
---

The layout registry shows **93** layouts. The real total is **135**.

**42 form layouts are reachable only through Issue Types.** `mode=ISSUE` and `mode=FORM` silently fall
back to `mode=SEP`, so they never appear in the registry at all. What makes a layout a form layout is
a non-null `PageLayoutField.CodeIssueTypeID`.

**This is not a curiosity — it is where the [[conditional-field]] feature actually lives.** A sweep of
the 93 concluded the feature was "wired everywhere and used nowhere". A sweep of all 135 finds
**8 layouts carrying 50 conditional records and 54 criteria clauses**, and **six of the eight are form
layouts**:

| Layout | Kind | Conditions |
|---|---|---:|
| `LAR Submit Lease Admin Request` (98946) | FORM | 19 |
| `LAR Initial Review of Lease Admin Request` (98944) | FORM | 16 |
| `LAR ASG Review of Lease Abstract` (98938) | FORM | 4 |
| `LAR Client Review of Lease Abstract` (98940) | FORM | 3 |
| `LAR Complete Lease Admin Request` (98941) | FORM | 3 |
| `LAR Finalize Lease Admin Request` (98942) | FORM | 3 |
| `ASG Contract Covenants` (98864) | LIST | 1 |
| `ASG Lease Abstract - Covenants` (102250) | LIST | 1 |

**The feature exists in this tenant to make one request form adapt to its request type.** 44 of the 54
clauses are driven by a single field, `Issue.LAR_RequestType` — which is exactly BRD-24's territory.

The scoping gap was **not** the only problem: two of the eight populated layouts sit inside the 93
that were swept. The other half of the failure was
[[method-fetch-is-not-render|a probe that could never have observed a rule]].

See [[form-vs-page]] · [[layout-modes]]
