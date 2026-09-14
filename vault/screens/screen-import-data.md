---
title: "Import Data"
tags: [screen, administration,import-export,api]
evidence: Observed
---

`/en/admin/Messenger.jsp`

![The generic bulk import. Note the error-handling radio defaults to "On first error" — and there is no dry-run option anywhere on this screen.](../../docs/assets/screenshots/bbw-admin/12-import-data.jpg)
`docs/assets/screenshots/bbw-admin/12-import-data.jpg` · `af-admin/13-import-data.jpg`

The UI over `POST /rest/firm` — an XML form post, one of
[[feature-import-export|four distinct inbound paths]].

- `synchronous` is **required**; `stopOnError` is optional and the UI defaults to *on first error*.
- **There is no dry-run parameter.**
- **It creates parent records implicitly** — importing a [[Facility]] creates its [[Location]].
- The upsert key is `BOMapClientRecordID`, addressed as `/clientid/{id}` and confirmed by
  `?allowUpdate=true`.

**And the trap**: [[finding-http-200-is-not-success]].

Shares the "Messenger" subsystem with [[screen-export-configuration]] — one subsystem, two screens.

All screens: [[map-of-screens]] · caveat: [[caveat-viewport]]
