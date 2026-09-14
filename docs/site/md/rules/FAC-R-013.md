# FAC-R-013 — The reverse of Contract → Facility is composed as a child grid, not a lookup

*Facilities, Locations & Sites · Observed*

**Effect: From `Facility`'s own Related Fields sidebar, `Contract` does not appear as a related lookup at all; instead the Facility Summary layout embeds an **"ASG Contract List (One to Many List)"** child grid.**

Effect: From `Facility`'s own Related Fields sidebar, `Contract` does not appear as a related lookup at all; instead the Facility Summary layout embeds an **"ASG Contract List (One to Many List)"** child grid. The relationship is asymmetric by cardinality and the UI reflects that asymmetry correctly on both sides. Confidence: Observed (009, screenshot `facility-summary-contracts-one-to-many-list.jpg`).

## The wording it rests on

> ASG Contract List (One to Many List)

## What it constrains

[Facility](../entities/Facility.md), [Contract](../entities/Contract.md)

## Confidence

Observed (009, screenshot `facility-summary-contracts-one-to-many-list.jpg`)

---

Source: `docs/modules/facilities-locations/rules.md`
