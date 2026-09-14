# DOC-R-003 — A Document carries an explicit release gate, independent of its checkout lock

*Documents, Folders & Correspondence · Observed*

**Input: `Document.ReadyForRelease`, `Required = Yes`, distinct from `IsCheckedOut`/ `CheckedOutByMemberID`/`CheckedOutDate`. Effect: Every document row must explicitly state whether it counts as released, as a separate fact from whether it is currently locked for editing.**

Input: `Document.ReadyForRelease`, `Required = Yes`, distinct from `IsCheckedOut`/ `CheckedOutByMemberID`/`CheckedOutDate`. Effect: Every document row must explicitly state whether it counts as released, as a separate fact from whether it is currently locked for editing. Confidence: Observed (`../../data-fields/document.md`); what gates the transition (who may set it, whether it can be un-set) is Inferred/unconfirmed.

## What it constrains

[Document](../entities/Document.md)

Columns named: `Document.ReadyForRelease`

## Confidence

Observed (`../../data-fields/document.md`); what gates the transition (who may set it, whether it can be un-set) is Inferred/unconfirmed

---

Source: `docs/modules/documents-folders/rules.md`
