---
title: Complex
tags: [entity, facilities]
evidence: Derived
---

**`complex` · 45 fields · [[module-facilities-locations]]**

The multi-building complex or campus — a mall, a campus — sitting *above* [[Facility]]. Referenced by
11 objects.

It is structurally odd in two ways that matter:

- **No parent and no `ProjectEntityID`.** It sits above the [[entity-spine]] entirely and classes
  [[entity-scoped-vs-firm-global|firm_global]] ([[rule-FAC-R-009]]).
- **Zero outbound foreign keys.** It points at nothing.

So a Complex is a pure grouping label attached from below, not a container that knows what it
contains. For [[hub-and-spoke]] purposes that puts it on the Hub side with the other 46 firm-global
in-scope objects.

Screens: [[screen-manage-complex]]
