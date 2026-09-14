# DOC-R-011 — An email's attachments are promoted into ordinary Document/Folder records

*Documents, Folders & Correspondence · Observed*

**Input: `LinkEMailReceivedLogDocument.DocumentID` + `.EMailReceivedLogID`. Effect: A received email's attachments become standard `Document` rows, filed under the ordinary `Folder` hierarchy, rather than living in a separate email-attachment store.**

Input: `LinkEMailReceivedLogDocument.DocumentID` + `.EMailReceivedLogID`. Effect: A received email's attachments become standard `Document` rows, filed under the ordinary `Folder` hierarchy, rather than living in a separate email-attachment store. Confidence: Observed, field list + internal edge resolution (`data-model.md`). No equivalent link exists for `EMailSentLog`, which carries no substantive fields at all — see `data-model.md` §5.

## What it constrains

[LinkEMailReceivedLogDocument](../entities/LinkEMailReceivedLogDocument.md), [Document](../entities/Document.md), [Folder](../entities/Folder.md), [EMailSentLog](../entities/EMailSentLog.md)

Columns named: `LinkEMailReceivedLogDocument.DocumentID`

## Confidence

Observed, field list + internal edge resolution (`data-model.md`). No equivalent link exists for `EMailSentLog`, which carries no substantive fields at all — see `data-model.md` §5

---

Source: `docs/modules/documents-folders/rules.md`
