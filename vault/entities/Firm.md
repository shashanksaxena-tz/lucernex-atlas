---
title: Firm
tags: [entity, platform-tenancy, tenancy, core]
evidence: Observed
---

**`firm` · 18 fields · [[module-platform-tenancy]]**

The tenant record. Small, and it carries two kinds of thing that matter far beyond its size:

- **Per-entity-type default layout assignments** — 11 `sTYPE_PAGE_LAYOUT` columns, one per subtype,
  overridable per portfolio by [[Program]]'s 18.
- **`Allow X?` entitlement flags**, which visibly gate 13 of 14 menu structures.

The 14th is the exception that broke a model. At [[tenant-american-freight|American Freight]],
`Allow Equipment Contracts? = Yes` and the root still does not render — see
[[finding-root-renders-iff-record-exists]]. The full 71-field record read from `FirmEdit.jsp` also
shows **no `Equipment Contract Setup Page` field at all**, so the catalog's description of `Firm`
holding per-module setup-page assignments is schema-derived and not exposed in the UI.

`Allow AI Lease Abstraction` is one of those flags, and it is one quarter of
[[atlas-ai-abstraction|the AI pipeline finding]].

`FirmID` is the tenant key and is typed `Text` — **there is no `Firm ID` FK type**, so schema-driven
tooling misses the relationship every row has ([[rule-PLT-R-002]]). See [[firm-tenancy]].

Screens: [[screen-manage-company]]
