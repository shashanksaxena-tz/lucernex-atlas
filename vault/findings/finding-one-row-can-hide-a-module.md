---
title: The three things this corpus got wrong the same way
tags: [finding, method, meta]
evidence: Observed
---

Four confident readings in this project were published and then retracted. **In every case the wrong
signal was cheaper to read than the right one**, and none of them produced an error — they produced
clean-looking results.

| Wrong signal | Right one | The retraction |
|---|---|---|
| A **column name** — `PreviousPageLayoutID` → "versioning" | What the values actually link | [[layout-chain]] |
| A **UI label** — 12 phantom census gaps | The physical name | [[finding-punch-list-out-of-scope]] |
| A **row-action difference** → "delete is suppressed by reference count" | The renderer's own source | [[finding-no-where-used-precedent]] |
| A **network response** — `fetch` says 36 of 46 routes resolve | What actually renders (**14**) | [[finding-routes-are-not-addressable]] |

Two more of the same family:

- A **default parameter** — `showGlobal=true` — produced *"0 of 205 firm fields exist as a physical
  column"*, the exact opposite of [[finding-firm-fields-are-physical-columns]].
- A **probe that could never have observed the thing** — reading a hidden input's `value` attribute
  from served HTML, when the builder populates it client-side — produced *"854 conditional targets,
  zero populated"* against the true answer of [[finding-form-layouts-are-hidden|8 layouts, 50
  records]].

> **Cheapness is the warning sign, not the convenience.**

The fourth row is the most dangerous, because the other three are obviously *proxies* once you look at
them — a name, a label, a sample — whereas a network response feels like direct evidence. **In this
application, a 200 with a plausible body proves the server answered and nothing about what renders.**

**The guard has to be structural, not attentional:** state which population you sampled, state how you
sampled it, and prefer the method that observes the thing a user would see.

See [[method-cheap-signals]] · [[method-fetch-is-not-render]] · [[evidence-labels]]
