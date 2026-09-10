# WorkFlowTemplate — Data Fields

The top-level workflow definition (the container for WorkFlowTemplateStep records) — active layout, associated task, and auto-assignment rules for the initiator. 25 Global fields under Company Items.

**Table Association:** `WorkFlowTemplate` &nbsp;·&nbsp; **Total fields:** 25 (Global: 25, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Active Layout | `PageLayoutID` | `sTYPE_FORM_PAGE_LAYOUT` | Global | No | No |  | Company Items / Work Flow Template |
| Associated Task | `TaskName` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Work Flow Template |
| Auto Assign Initiator as Ad Hoc Assignee | `AutoAssignInitiator` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Company Items / Work Flow Template |
| Collaborator Job Title List | `CollaboratorJobTitleIDList` | `sCODE_JOB_TITLE` | Global | No | No |  | Company Items / Work Flow Template |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Work Flow Template |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Company Items / Work Flow Template |
| Default Work Flow Priority | `DefaultWFCodePriorityID` | `sCODE_PRIORITY` | Global | Yes | No |  | Company Items / Work Flow Template |
| Description | `Description` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Work Flow Template |
| Description of KickOff | `KickOffDescription` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Work Flow Template |
| Enable Vendor Collaboration | `EnableVendorCollaboration` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Company Items / Work Flow Template |
| Javascript Source Code | `IsEnabledLxJSCode` | `sTYPE_TEXTAREA` | Global | No | No |  | Company Items / Work Flow Template |
| Kick-off Method | `KickOffMethod` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Work Flow Template |
| Limit By Entity? | `LimitByEntity` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Company Items / Work Flow Template |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Work Flow Template |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Company Items / Work Flow Template |
| Notify All Approvers When Complete? | `NotifyAllApproversComplete` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Company Items / Work Flow Template |
| Notify All Assignees When Complete? | `NotifyAllAssigneesComplete` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Company Items / Work Flow Template |
| Notify Initiator When Complete? | `NotifyInitiatorComplete` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Company Items / Work Flow Template |
| Rev Number | `RevNumber` | `sTYPE_NUMBER` | Global | No | No |  | Company Items / Work Flow Template |
| Status Change ID | `StatusChangeID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Work Flow Template |
| Status Change Type | `StatusChangeType` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Work Flow Template |
| Work Flow Kick-off Record | `KickOffID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Work Flow Template |
| Work Flow Template ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / Work Flow Template |
| Work Flow Template Name | `WorkFlowTemplateName` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / Work Flow Template |
| Work Flow Template RecID | `WorkFlowTemplateID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Work Flow Template |
