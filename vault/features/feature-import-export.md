---
title: Import and export
tags: [feature, api, integration, core]
evidence: Observed
---

Concepts: [[rest-business-object]] · [[publish-and-fork]] · [[three-publish-tiers]] ·
[[atlas-ai-abstraction]]

**Four distinct inbound paths, not one**: `POST /rest/firm` (XML bulk), `POST /rest/firm/document`,
`/rest/vendor-lease`, and `/rest/atlas-api`.

- **[[finding-http-200-is-not-success]]** — the trap to design around.
- `synchronous` is **required** on `POST /rest/firm`; `stopOnError` optional; the UI defaults to
  *on first error*; **there is no dry-run parameter**.
- Bulk import **creates parent records implicitly** — importing a [[Facility]] creates its
  [[Location]].
- **`@clientID` is `BOMapClientRecordID`**, and `POST …?allowUpdate=true` is the upsert. Previously
  Inferred, now Observed.
- **No generic bulk *export* endpoint exists** — `POST /rest/firm` has no GET counterpart among the
  160 operations.
- Two staging twins exist in the whole schema: `PaymentTransactionFullImport` (118 fields) and
  `WFStepFullImport` (47).

[[screen-export-configuration|Export Configuration]] is the firm-to-firm publish mechanism and its
clone checkbox **names the [[publish-and-fork]] model in the vendor's own words**.
[[screen-import-best-practice-templates|Import Best Practice Templates]] is the vendor's versioned
channel — the only tier with `Version` / `Min Version` / `Released`.

And [[screen-job-log|Job Log]]'s **818 entries** are the first evidence of the product *running*: a
real XLSX import, `Generate Payments` logged as a user-triggered job, and an **hourly inbound HTTP
integration** ([[q-bbw-19-hourly-integration]]).

[`features/import-export/`](../../docs/features/import-export/README.md)
