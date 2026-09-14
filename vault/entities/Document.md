---
title: Document
tags: [entity, documents]
evidence: Observed
---

**`document` · 23 fields · [[module-documents-folders]]**

File metadata with author and checkout locking. **11,905 documents in the live tenant — the largest
single collection in the product.** Referenced by 10 objects.

- A Document must belong to **exactly one [[Folder]]**; a save is blocked without `ParentFolderID`
  ([[rule-DOC-R-001]]).
- `ReadyForRelease` is a **required release gate**, independent of the `IsCheckedOut` editing lock
  ([[rule-DOC-R-003]]).
- It has `Version` fields but **no lineage column** — unlike `Folder`, which has an explicit
  `PreviousFolderID` ([[rule-DOC-R-005]]). You can tell a document is version 3; you cannot reach
  version 2.

Received-email attachments are promoted into ordinary Document rows; **there is no equivalent for sent
mail** ([[rule-DOC-R-011]]).
