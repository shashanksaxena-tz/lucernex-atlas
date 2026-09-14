---
title: "DOC-R-009 — One audit row spans three template kinds"
tags: [rule, documents-folders]
evidence: Observed
---

**`DOC-R-009`** · [[module-documents-folders]] · **Observed**

A single `FolderTemplateAudit` row records **folder, budget and task templates applied together** — so
template application is one event, not three.

See [[rules-documents-folders]] for the full register.
