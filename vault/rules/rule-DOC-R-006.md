---
title: "DOC-R-006 — Folder security is scoped only through the folder"
tags: [rule, documents-folders]
evidence: Observed
---

**`DOC-R-006`** · [[module-documents-folders]] · **Observed**

`FolderSecurity` carries **no `ProjectEntityID`** — so access control does not inherit from the entity
the folder hangs off. A separate axis from [[security-ladder|the four securable surfaces]].

See [[rules-documents-folders]] for the full register.
