---
title: Layouts and forms
tags: [module, layouts, core]
evidence: Observed
---

**rules `LAY-R-001`…`018` and `LAY-R-101`…`202`** — 88 in the register.

Four admin concepts running on **shared machinery**: one field registry, one layout record type, one
placement table, one builder driven by a `layoutMode` discriminator. What differs is only what you
point the engine at.

Concepts: [[page-layout-concept]] · [[layout-modes]] · [[layout-chain]] · [[form-vs-page]] ·
[[custom-list]] · [[conditional-field]] · [[data-field-catalog]] · [[action-buttons]]

Entities: [[PageLayout]] · [[PageLayoutField]] · [[PageLayoutFilter]] · [[CodeIssueType]] ·
[[ReportGroupAvailableField]] · [[ClientListRow]] · [[CustomCodeField]]

Findings: [[finding-form-layouts-are-hidden]] · [[finding-no-layout-level-required]] ·
[[finding-layouts-over-projections]] · [[finding-rules-store-labels-not-ids]] ·
[[finding-publish-then-fork]]

Two rules worth reading on their own: **[[rule-LAY-R-106]]** — a layout with a non-blank `URL`
bypasses its field configuration entirely — and **[[rule-LAY-R-192]]**, which sets the precedence
between the three systems that decide whether a field is visible: **security → placement →
condition**.

`Program` carries 18 `sTYPE_PAGE_LAYOUT` columns against `Firm`'s 11, and **only the Firm screen has
ever been opened**.

Rules: [[rules-layouts-and-forms]] ·
[`modules/layouts-and-forms/`](../../docs/modules/layouts-and-forms/README.md)
