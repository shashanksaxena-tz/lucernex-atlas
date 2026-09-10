# WorkFlow — Data Fields

The active workflow instance running against a real trigger object (Trigger CodeSQLTable, Trigger Object) — the runtime record one level above WorkFlowStep. 20 Global fields under Statics and Workflow.

**Table Association:** `WorkFlow` &nbsp;·&nbsp; **Total fields:** 20 (Global: 20, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Trigger CodeSQLTable | `TriggerCodeSQLTableID` | `sCODE_SQLTABLE` | Global | No | No |  | Statics / Hidden |
| Trigger Object | `TriggerObjectID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Statics / Hidden |
| Workflow Template | `WorkFlowTemplateID` | `sTYPE_WORK_FLOW_TEMPLATE` | Global | Yes | No |  | Statics / Workflow |
| Ad Hoc Assignee | `AdhocMemberID` | `sTYPE_PE_MEMBER` | Global | No | No |  | Workflow / Workflow Summary Info (All) |
| Closed Date | `ClosedDate` | `sTYPE_DATE` | Global | No | No |  | Workflow / Workflow Summary Info (All) |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Workflow / Workflow Summary Info (All) |
| Inactive? | `Inactive` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Workflow / Workflow Summary Info (All) |
| Initiated By Member | `InitiatedByMemberID` | `sTYPE_MEMBER` | Global | No | No |  | Workflow / Workflow Summary Info (All) |
| Is Completed? | `IsCompleted` | `sTYPE_BOOLEAN` | Global | No | No |  | Workflow / Workflow Summary Info (All) |
| Kick Off Form | `KickOffIssueID` | `sTYPE_ISSUE` | Global | No | No |  | Workflow / Workflow Summary Info (All) |
| Kick Off Task | `KickOffTaskID` | `sTYPE_TASK` | Global | No | No |  | Workflow / Workflow Summary Info (All) |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Workflow / Workflow Summary Info (All) |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Workflow / Workflow Summary Info (All) |
| Name | `WorkFlowName` | `sTYPE_TEXT` | Global | Yes | No |  | Workflow / Workflow Summary Info (All) |
| Number Of Days Open | `NumberOfDaysOpen` | `sTYPE_NUMBER` | Global | No | No |  | Workflow / Workflow Summary Info (All) |
| Priority | `WorkFlowCodePriorityID` | `sCODE_PRIORITY` | Global | Yes | No |  | Workflow / Workflow Summary Info (All) |
| Status | `CodeWorkFlowStatusID` | `sCODE_WORK_FLOW_STATUS` | Global | Yes | No |  | Workflow / Workflow Summary Info (All) |
| WF Approver List | `WFApproverList` | `sTYPE_WORK_FLOW_APPROVER_LIST` | Global | No | No |  | Workflow / Workflow Summary Info (All) |
| Work Flow ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Workflow / Workflow Summary Info (All) |
| Work Flow RecID | `WorkFlowID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Workflow / Workflow Summary Info (All) |
