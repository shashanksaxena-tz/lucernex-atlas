---
title: PageLayout
tags: [entity, layouts, core, gap]
evidence: Observed
---

**17 columns over REST (42 in the vendor catalog) · layouts-forms-reporting**

The record behind every screen — see [[page-layout-concept]]. And **it is absent from the 223-object
census**: it is one of the **25 tables the schema viewer refuses**, which is why the reporting
module's central claim (*a report is a `PageLayout` row with `IsReport = true`*) rested on a table
nobody could see.

It was recovered over [[rest-business-object|REST]]:

```
GET /rest/businessObject/PageLayout/lxid/{id}?deep=true
```

**with the caveat that the serialiser emits only populated columns**, so 17 is a lower bound, not a
schema.

Key columns:

- `ParentPageLayoutID` — self-referential, attaches a layout to a navigation node
- `PreviousPageLayoutID` — **a sequence pointer, not a version pointer** ([[layout-chain]])
- `CodeIssueTypeID` — non-null makes it a [[form-vs-page|form layout]]
  ([[finding-form-layouts-are-hidden]])
- `IsReport` — makes it a report ([[rule-RPT-R-001]])
- `LastRunBy` / `LastRunDate` — **a single most-recent run stamp, no history**
- `URL` — non-blank **bypasses the field configuration entirely** and redirects ([[rule-LAY-R-106]])

The tenant holds **1,647 rows** against the 135 in the registries — [[q-bbw-23-1647-layouts]].

See [[PageLayoutField]] · [[PageLayoutFilter]] · [[layout-modes]]
