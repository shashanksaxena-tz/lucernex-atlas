---
title: A route is not an addressable URL
tags: [finding, navigation, method, trap]
evidence: Observed
---

Sub-screens in Lx are selected by the in-app menu tree, **not by URL**. `EntityInfo.jsp` is the record
shell, loading the active sub-screen into an inner iframe.

It is **not uniform across entity types**, and an earlier revision overstated it:

| Root | Addressability |
|---|---|
| **[[equipment-contract\|Equipment Contract]]** | **None.** Only group heads resolve, and they render their first leaf |
| **[[Contract]]** | **Partial.** 14 of 46 sub-screens have real URLs; 22 silently redirect; 8 are AccessDenied; 2 bounce server-side |

So roughly **a third of Contract's saved links would survive** a migration and **none of Equipment
Contract's would** — a per-entity question, not a global one ([[q-bbw-24-deep-linking]]).

### The methodological half, which is the more valuable half

**Classifying all 46 Contract routes by raw `fetch` reported 36 addressable. Driving the same 46 in a
real browser produced 14.**

The 22-route gap is **client-side JS redirection**: the server returns a full 37–40 KB HTML document,
so `fetch` sees a clean success — and then the page's own script bounces to `EntityInfo.jsp` and
renders the default Summary.

**A fetch-based route audit overstates deep-linkability by more than 2×.**

Without a post-capture URL guard, sweeping all 32 Equipment Contract nodes naively would have produced
**roughly 20 files with distinct, meaningful names all containing the same default Summary page**,
plus six Access Denied pages. They load correctly, are full-size, and look like real screens. **The
corruption would have been near-impossible to detect later.** Every one was caught by a final-URL
check.

See [[method-fetch-is-not-render]] · [[method-cheap-signals]]
