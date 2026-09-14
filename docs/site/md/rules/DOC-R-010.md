# DOC-R-010 — DocumentMarkup does not persist markup content in this schema

*Documents, Folders & Correspondence · Observed*

**Input: `DocumentMarkup`'s only field is `ProjectEntityID`; `Document.HasMarkups` is a boolean flag with no visible source of truth for what the markup actually is.**

Input: `DocumentMarkup`'s only field is `ProjectEntityID`; `Document.HasMarkups` is a boolean flag with no visible source of truth for what the markup actually is. Effect: A rebuild cannot port markup annotation data from this schema — it is not captured here, by either genuine product architecture (stored elsewhere) or export limitation. Confidence: Observed (field absence, exhaustive); the explanation for the absence is unresolved — see `data-model.md`.

## What it constrains

[DocumentMarkup](../entities/DocumentMarkup.md), [Document](../entities/Document.md)

Columns named: `Document.HasMarkups`

## Confidence

Observed (field absence, exhaustive); the explanation for the absence is unresolved — see `data-model.md`

---

Source: `docs/modules/documents-folders/rules.md`
