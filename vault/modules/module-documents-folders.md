---
title: Documents and folders
tags: [module, documents]
evidence: Observed
---

**10 objects · 99 fields · rules `DOC-R-001`…`DOC-R-011`** — the smallest in-scope module, and **the
count is the finding**: four of the ten objects are 1-to-3-field stubs.

Universal in reach — every [[ProjectEntity]] root gets a `Documents` and a `Binders` tab — and
**11,905 documents in the live tenant, the largest single collection in the product**.

Entities: [[Document]] · [[Folder]]

Three gaps worth knowing before scoping:

- **`DocumentMarkup` has one field.** Markup content is not captured in this schema at all
  ([[rule-DOC-R-010]]). Cause unresolved.
- **No object anywhere in the 223-object census backs the universally visible "Binders" tab.** It
  routes to `CommitteeDocuments/PECommPkg.jsp` ("Committee Packages") and matches nothing.
- **Correspondence is asymmetric.** Received-email attachments become ordinary Documents; there is no
  equivalent for sent mail ([[rule-DOC-R-011]]), and `EMailSentLog` is a one-field stub.

`FolderTemplate` is a stub whose real metadata lives in the [[virtual-projection|`VirtualTemplateFolder`]]
projection, with the same **11 `IsValidFor*` flags** as [[CodeIssueType]].

**No Documents, Binders or Correspondence screen was ever opened.**

Rules: [[rules-documents-folders]] ·
[`modules/documents-folders/`](../../docs/modules/documents-folders/README.md)
