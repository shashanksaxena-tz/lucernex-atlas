# Folder — Data Fields

A document-management folder — downloadable flag and folder-template linkage, the container Document records live in. 16 Global fields under Documents.

**Table Association:** `Folder` &nbsp;·&nbsp; **Total fields:** 16 (Global: 16, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Description | `Description` | `sTYPE_TEXTAREA` | Global | No | No |  | Documents / Folders |
| Downloadable | `IsFolderDownloadableByMember` | `sTYPE_BOOLEAN` | Global | No | No |  | Documents / Folders |
| Folder ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Documents / Folders |
| Folder RecID | `FolderID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Documents / Folders |
| Folder Template Name | `FolderTemplateName` | `sTYPE_TEXT` | Global | No | No |  | Documents / Folders |
| Full Folder List | `SubFolderPath` | `sTYPE_FULL_FOLDER_LIST` | Global | No | No |  | Documents / Folders |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Documents / Folders |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Documents / Folders |
| Name | `FolderName` | `sTYPE_TEXT` | Global | Yes | No |  | Documents / Folders |
| Parent Folder | `ParentFolderID` | `sTYPE_FOLDER` | Global | No | No |  | Documents / Folders |
| Path Name | `SubFolderPath` | `sTYPE_TEXT` | Global | No | No |  | Documents / Folders |
| Previous Folder | `PreviousFolderID` | `sTYPE_FOLDER` | Global | No | No |  | Documents / Folders |
| Readable | `IsFolderReadableByMember` | `sTYPE_BOOLEAN` | Global | No | No |  | Documents / Folders |
| Subscriber Job Titles | `SubscriptionCodeJobTitleIDList` | `sCODE_JOB_TITLE` | Global | No | No |  | Documents / Folders |
| Uploadable | `IsFolderUploadableByMember` | `sTYPE_BOOLEAN` | Global | No | No |  | Documents / Folders |
| Uploadable Only | `IsFolderUploadOnlyByMember` | `sTYPE_BOOLEAN` | Global | No | No |  | Documents / Folders |
