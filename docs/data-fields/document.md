# Document — Data Fields

The document/file metadata record used across the platform — author, checkout status (Checked Out By Member, Checked Out Date) for document locking during edits. 22 Global fields under Documents.

**Table Association:** `Document` &nbsp;·&nbsp; **Total fields:** 22 (Global: 22, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Documents / Audit Info |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Documents / Audit Info |
| Author | `AuthoredByPersonID` | `sTYPE_PERSON` | Global | No | No |  | Documents / General Information |
| Author Name | `AuthorName` | `sTYPE_TEXT` | Global | No | No |  | Documents / General Information |
| Checked Out By Member | `CheckedOutByMemberID` | `sTYPE_MEMBER` | Global | No | No |  | Documents / General Information |
| Checked Out Date | `CheckedOutDate` | `sTYPE_DATE` | Global | No | No |  | Documents / General Information |
| Conversion Status | `CodeDocumentConvertStatusID` | `sCODE_DOCUMENT_CONVERT_STATUS` | Global | Yes | No |  | Documents / General Information |
| Description | `Description` | `sTYPE_TEXT` | Global | No | No |  | Documents / General Information |
| Document RecID | `DocumentID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Documents / General Information |
| Document Type | `CodeDocumentTypeID` | `sCODE_DOCUMENT_TYPE` | Global | Yes | No |  | Documents / General Information |
| Download Link | `DownloadLink` | `sTYPE_DOCUMENT_VIEWLINK` | Global | No | No |  | Documents / General Information |
| File Created Date | `FileCreatedDate` | `sTYPE_TIME` | Global | Yes | No |  | Documents / General Information |
| File Name | `BaseName` | `sTYPE_TEXT` | Global | Yes | No |  | Documents / General Information |
| File Size | `FileSize` | `sTYPE_NUMBER` | Global | No | No |  | Documents / General Information |
| Folder | `SubFolderPath` | `sTYPE_TEXT` | Global | No | No |  | Documents / General Information |
| Has Markups? | `HasMarkups` | `sTYPE_BOOLEAN` | Global | No | No |  | Documents / General Information |
| Is Checked Out? | `IsCheckedOut` | `sTYPE_BOOLEAN` | Global | No | No |  | Documents / General Information |
| Is Latest Version? | `IsLatestVersion` | `sTYPE_BOOLEAN` | Global | No | No |  | Documents / General Information |
| Parent Folder | `ParentFolderID` | `sTYPE_FOLDER` | Global | Yes | No |  | Documents / General Information |
| Parent Folder Name | `ParentFolderName` | `sTYPE_TEXT` | Global | No | No |  | Documents / General Information |
| Released? | `ReadyForRelease` | `sTYPE_CHECKBOX` | Global | Yes | No |  | Documents / General Information |
| Version | `Version` | `sTYPE_NUMBER` | Global | Yes | No |  | Documents / General Information |
