---
title: "Q-BBW-11 — Can a layout over a projection be written to?"
tags: [open-question, layouts, data-model]
evidence: Derived
status: open
---

Four layouts target a [[virtual-projection|`Virtual*`]] object as their primary table, two of them
top-level Summary Pages — [[finding-layouts-over-projections]].

**The projections have no primary key**, so there is nothing to write back to. The expectation is that
these screens are **structurally read-only**.

> **This decides whether ASG Edge+'s layout engine needs a read-only layout class** — that is, whether
> read-only-ness is a modelled property of a layout, or something the runtime discovers when a save
> fails.

The corpus's position is that it must be **modelled explicitly rather than discovered at runtime**, but
that is a design argument, not an observation of what Lx does.

### How to settle it

Open `ASG Breakpoint Schedule` (98921) in the builder and check whether its fields are editable or
display-only. Inspection alone answers it; **proving** it would require an attempted save, which is a
write ([[method-read-only-exploration]]).
