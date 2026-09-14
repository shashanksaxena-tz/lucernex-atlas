---
title: "Method: when a signal is cheap, check it against the thing it stands for"
tags: [method, meta]
evidence: Observed
---

The corpus's own governing rule, earned four times over:

> **When a signal is conveniently to hand, that is exactly when to check it against the thing it
> stands for.**

| Wrong signal | Right one | Cost difference |
|---|---|---|
| A column **name** (`PreviousPageLayoutID` → "versioning") | What the values actually link | The name is right there; the join needs building |
| A UI **label** (12 phantom census gaps) | The physical name | The label is on screen; the physical name needs a lookup |
| A **key-union** (`DisplayOption` "only 0 and 288") | The values themselves | One pass versus many |
| A **default parameter** (`showGlobal=true`) | The correct one | No thought versus knowing what the radio means |
| A **network response** (`fetch`: 36 of 46 routes resolve) | What actually renders (**14**) | One request versus driving a browser |

**Cheapness is the warning sign, not the convenience.**

**These failures do not produce errors; they produce clean-looking results** — empty where you
expected empty, complete where you expected complete. Which is why none was caught by the person who
made it.

> **The guard has to be structural, not attentional: state which population you sampled, state how you
> sampled it, and prefer the method that observes the thing a user would see.**

Two more instances that are not in the table: a comparison built around
[[finding-no-layout-level-required|a layout that did not contain the fields being compared]], and a
probe [[method-fetch-is-not-render|structurally incapable of ever observing a rule]].

Every retraction: [[finding-one-row-can-hide-a-module]] ·
[`CONVENTIONS.md`](../../docs/CONVENTIONS.md)
