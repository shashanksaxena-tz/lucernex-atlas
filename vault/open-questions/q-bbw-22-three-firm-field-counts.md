---
title: "Q-BBW-22 — Three sources give three firm-field counts"
tags: [open-question, data-model]
evidence: Observed
status: open
---

| Source | Firm fields |
|---|---:|
| Census (`_lucernex_objects_summary.txt`) | **359** |
| `showGlobal=false` differencing | **298** |
| Catalog (`all-fields.csv`) | **205** |

**They measure different populations and are not reconciled.** They diverge in *both* directions —
[[Contract]] is 258 by the census and 147 by the catalog; [[KeyDate]] is 7 by the census and 10 by the
catalog.

> **No one of them should be quoted as authoritative.**

This is a known, already-documented divergence rather than a new discrepancy: the three field
inventories (census 7,421 · catalog 6,158 · View Object Model 7,047) disagree in both directions and
**none is the physical schema**. See
[`reading-the-census.md`](../../docs/data-model/reading-the-census.md).

### It does not weaken the finding

[[finding-firm-fields-are-physical-columns]] rests on firm fields **being physical columns at all**,
which every inventory agrees on. **Whether it is 205 or 359, adding one is DDL.**

### How to settle it

Determine what each population actually *is* — which scope, which capture parameters, which filter —
**before publishing any firm-field total**.

See [[firm-custom-field]] · [[data-field-catalog]]
