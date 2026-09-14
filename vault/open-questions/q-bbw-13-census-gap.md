---
title: "Q-BBW-13 — What is in the 25 tables the viewer refuses?"
tags: [open-question, data-model]
evidence: Observed
status: open
---

**Largely answered.** Reconciled on physical name, only **6** of the 227 tables are genuine census
gaps, four of them the out-of-scope `Punch List` family — see
[[finding-punch-list-out-of-scope]]. **The in-scope gap is two one-field tables**, `ChangeManage` and
`VirtualTemplateMember`.

**What remains open is field detail for the 25 tables `ShowObjectDetails.jsp` refuses** — and they are
the important set, because they are **the platform's own machinery**: [[PageLayout]],
[[PageLayoutField]], [[PageLayoutFilter]], `CustomCodeTable`, `Dashboard`, `Job Log`, `Audit Master`,
`Notify Template`, `Grid Preference`, the Excel integration trio.

**[[PageLayout]] is still absent from the 223-object census**, and
[[module-reporting|the reporting module's central claim]] — *a report **is** a `PageLayout` row with
`IsReport = true`* — rests on a table the census does not carry. **That is the gap that matters for
rebuilding the layout engine.**

### How to settle it

Pull all 25 over [[rest-business-object|REST]]:
`GET /rest/businessObject/{type}/lxid/{id}?deep=true`. All 25 appear in `GET /rest/firm/types`.

**With a caveat that is not a formality:** the serialiser emits only **populated** columns, so results
are a **lower bound, not a schema**.
