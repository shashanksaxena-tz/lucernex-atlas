---
title: ClientListRow
tags: [entity, configuration, gap]
evidence: Observed
---

**24 columns · layouts-forms-reporting**

The supposed store behind [[custom-list|custom lists]] — and it **does not add up**.

- **Not one of its 24 columns carries a `CRL_` or `OpEx` prefix**, contradicting the script names the
  admin screen shows.
- Its five generic value slots `SubValue` … `SubValue5` are **all typed `Currency`** — which cannot
  hold `OpExComments` or a date.
- `Operating Expenses` shows **13 leaf fields**, against a five-slot cap.

Two readings survive: a generic EAV store the export renders misleadingly, or **real per-list columns**
on the [[firm-custom-field|`Firm_` precedent]]. The second is more likely on that precedent, and the
corpus **recorded it open rather than resolving it**.

Testable in one call:
`GET /rest/businessObject/ClientListRow/lxid/{id}?deep=true`.
