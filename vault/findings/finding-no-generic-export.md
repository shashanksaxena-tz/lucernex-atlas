---
title: Configuration round-trips as XML, but there is no generic data export
tags: [finding, api, integration]
evidence: Derived
---

Two asymmetries sit next to each other and are easy to conflate.

**Configuration round-trips.** [[screen-export-configuration|Export Configuration]] produces XML and
`POST /rest/firm` consumes XML, so the [[hub-and-spoke]] publish mechanism that ASG's own workspace
notes record as *"not written down anywhere"* has **working prior art in the incumbent** — see
[[publish-and-fork]].

**Data does not.** `POST /rest/firm` has **no GET counterpart among the 160 REST operations**. There
is no generic bulk export endpoint. Extraction is per-object through
`GET /rest/businessObject/{type}/details`, where [[fiql|`fields` is mandatory and the endpoint returns
413]] if you ask for too many — a real constraint for any migration.

Reporting has the same shape from the other side: ASG requires a **report-to-import round trip**, and
Lx exports field *metadata* only, with **no report-data equivalent** ([[rule-RPT-R-063]]).

And GraphQL cannot help: 490 types, and **no layout, report, chart or rule type at all** — so layouts
and reports **cannot** be migrated through the data API ([[module-reporting]]).

So a migration out of Lx is: configuration by XML export, data by per-object paged REST, and reports
by hand.
