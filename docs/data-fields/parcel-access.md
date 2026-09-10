# ParcelAccess — Data Fields

An access easement or right-of-way record on a Parcel — effective/expire date and associated document. 19 Global fields under Parcel.

**Table Association:** `ParcelAccess` &nbsp;·&nbsp; **Total fields:** 19 (Global: 19, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Associated Document | `AssociatedDocumentID` | `sTYPE_DOCUMENT` | Global | No | No |  | Parcel / Parcel Access |
| Effective Date | `EffectiveDate` | `sTYPE_DATE` | Global | No | No |  | Parcel / Parcel Access |
| Exists? | `ExistsFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Parcel / Parcel Access |
| Expire Date | `ExpireDate` | `sTYPE_DATE` | Global | No | No |  | Parcel / Parcel Access |
| File Name | `BaseName` | `sTYPE_TEXT` | Global | No | No |  | Parcel / Parcel Access |
| Folder | `FolderID` | `sTYPE_DOCUMENT` | Global | No | No |  | Parcel / Parcel Access |
| Line Number | `LineNumber` | `sTYPE_TEXT` | Global | No | No |  | Parcel / Parcel Access |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Parcel / Parcel Access |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Parcel / Parcel Access |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Parcel / Parcel Access |
| Page Number | `PageNumber` | `sTYPE_TEXT` | Global | No | No |  | Parcel / Parcel Access |
| Paragraph Number | `ParagraphNumber` | `sTYPE_TEXT` | Global | No | No |  | Parcel / Parcel Access |
| Parcel | `ParcelID` | `sTYPE_PARCEL` | Global | Yes | No |  | Parcel / Parcel Access |
| Parcel Access Category | `CodeParcelAccessCategoryID` | `sCODE_PARCEL_ACCESS_CATEGORY` | Global | No | No |  | Parcel / Parcel Access |
| Parcel Access ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Parcel / Parcel Access |
| Parcel Access Group | `CodeParcelAccessGroupID` | `sCODE_PARCEL_ACCESS_GROUP` | Global | No | No |  | Parcel / Parcel Access |
| Parcel Access RecID | `ParcelAccessID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Parcel / Parcel Access |
| Parcel Access Type | `CodeParcelAccessTypeID` | `sCODE_PARCEL_ACCESS_TYPE` | Global | No | No |  | Parcel / Parcel Access |
| Tickler Date | `TicklerDate` | `sTYPE_DATE` | Global | No | No |  | Parcel / Parcel Access |
