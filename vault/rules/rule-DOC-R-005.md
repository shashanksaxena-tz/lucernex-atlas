---
title: "DOC-R-005 — Folders have lineage; documents do not"
tags: [rule, documents-folders]
evidence: Derived
---

**`DOC-R-005`** · [[module-documents-folders]] · **Derived**

[[Folder]] has an explicit `PreviousFolderID` self-reference. **[[Document]] has no lineage column at
all, despite carrying `Version` fields.**

You can tell a document is version 3. You cannot reach version 2.

See [[rules-documents-folders]] for the full register.
