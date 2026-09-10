# Audit & History Tables

These 5 tables (45 fields, all Global) record change history and access history rather than current business state — who did what, when, to which record. `AuditColumn` is one level more meta than the rest: it defines *which* columns are tracked, rather than recording a tracked event itself.

**Entities in this file:** 5 &nbsp;·&nbsp; **Total fields:** 45 (Global: 45, Firm: 0)

| Entity | Fields (G/F) | One-line role |
|---|---|---|
| `AuditColumn` | 14 (14/0) | Metadata defining which columns on a table are tracked for audit history — accessor name and audit action per tracked field. |
| `AssetHistory` | 13 (13/0) | A point-in-time snapshot of an Asset's financial state, letting the platform show what an asset's values were before a later recalculation. |
| `MemberAudit` | 11 (11/0) | Login/session audit trail for internal Members — action name, audit date, and impersonation tracking for support access. |
| `DocumentAudit` | 6 (6/0) | Audit trail of actions taken on a Document (view, edit, delete) — action, actor, and date. |
| `LeaseAudit` | 1 (1/0) | A single-field audit-trail stub for lease-level changes; likely a placeholder or minimally-used table relative to the richer Contract audit trail. |

Field type codes are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Entity | Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|---|
| AuditColumn | AccessorName | `AccessorName` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / Audit Info |
| AuditColumn | AuditAction | `AuditAction` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Audit Info |
| AuditColumn | CodeSQLTableID | `CodeSQLTableID` | `sCODE_SQLTABLE` | Global | No | No |  | Company Items / Audit Info |
| AuditColumn | CreatedByID | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Audit Info |
| AuditColumn | CreatedDate | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Company Items / Audit Info |
| AuditColumn | EntityName | `EntityName` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Audit Info |
| AuditColumn | FieldName | `FieldName` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Audit Info |
| AuditColumn | GroupID | `GroupID` | `sTYPE_REPORT_GROUP_DATA` | Global | No | No |  | Company Items / Audit Info |
| AuditColumn | NewValue | `NewValue` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Audit Info |
| AuditColumn | ObjectID | `ObjectID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Audit Info |
| AuditColumn | OldValue | `OldValue` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Audit Info |
| AuditColumn | ProjectEntityID | `ProjectEntityID` | `sTYPE_PROJECT_ENTITY` | Global | No | No |  | Company Items / Audit Info |
| AuditColumn | ScriptName | `ScriptName` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Audit Info |
| AuditColumn | SubGroupID | `SubGroupID` | `sTYPE_REPORT_GROUP_DATA` | Global | No | No |  | Company Items / Audit Info |
| AssetHistory | Asset | `AssetID` | `sTYPE_EQUIPMENT` | Global | Yes | No |  | Equipment/Assets / History |
| AssetHistory | Asset History ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Equipment/Assets / History |
| AssetHistory | Asset History RecID | `AssetHistoryID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Equipment/Assets / History |
| AssetHistory | Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Equipment/Assets / History |
| AssetHistory | Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Equipment/Assets / History |
| AssetHistory | From Entity | `FromProjectEntityID` | `sTYPE_MIXEDENTITY` | Global | No | No |  | Equipment/Assets / History |
| AssetHistory | Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Equipment/Assets / History |
| AssetHistory | Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Equipment/Assets / History |
| AssetHistory | Move In Date | `MoveInDate` | `sTYPE_DATE` | Global | No | No |  | Equipment/Assets / History |
| AssetHistory | Move Out Date | `MoveOutDate` | `sTYPE_DATE` | Global | No | No |  | Equipment/Assets / History |
| AssetHistory | Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Equipment/Assets / History |
| AssetHistory | Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Equipment/Assets / History |
| AssetHistory | To Entity | `ProjectEntityID` | `sTYPE_MIXEDENTITY` | Global | Yes | No |  | Equipment/Assets / History |
| MemberAudit | Action Details | `LogInfo` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Member Audit |
| MemberAudit | Action Name | `CodeMemberActionID` | `sCODE_MEMBER_ACTION` | Global | Yes | No |  | Company Items / Member Audit |
| MemberAudit | Audit Date | `AuditDate` | `sTYPE_TIME` | Global | Yes | No |  | Company Items / Member Audit |
| MemberAudit | Impersonating Member | `ImpersonatingMemberID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Member Audit |
| MemberAudit | Login Status | `CodeLockOutReasonID` | `sCODE_LOCK_OUT_REASON` | Global | No | No |  | Company Items / Member Audit |
| MemberAudit | Member | `MemberID` | `sTYPE_MEMBER` | Global | Yes | No |  | Company Items / Member Audit |
| MemberAudit | Member Audit RecID | `MemberAuditID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Member Audit |
| MemberAudit | Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Member Audit |
| MemberAudit | Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Company Items / Member Audit |
| MemberAudit | Source IP | `SrcIP` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Member Audit |
| MemberAudit | User Agent | `UserAgent` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Member Audit |
| DocumentAudit | Action | `CodeDocumentActionID` | `sCODE_DOCUMENT_ACTION` | Global | Yes | No |  | Documents / Audit History |
| DocumentAudit | Action By Member | `ActionByMemberID` | `sTYPE_MEMBER` | Global | Yes | No |  | Documents / Audit History |
| DocumentAudit | Audit Date | `AuditDate` | `sTYPE_DATE` | Global | Yes | No |  | Documents / Audit History |
| DocumentAudit | Document | `DocumentID` | `sTYPE_DOCUMENT` | Global | Yes | No |  | Documents / Audit History |
| DocumentAudit | Entity | `ProjectEntityID` | `sTYPE_PROJECT_ENTITY` | Global | Yes | No |  | Documents / Audit History |
| DocumentAudit | Folder | `ParentFolderID` | `sTYPE_FOLDER` | Global | No | No |  | Documents / Audit History |
| LeaseAudit | Lease Audit RecID | `LeaseAuditID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Statics / Hidden |
