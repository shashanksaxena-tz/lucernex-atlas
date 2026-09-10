# WorkFlowStep — Data Fields

The runtime instance of one workflow step executing against a real record — computed alert/warn/due dates for approvers and assignees, checkout tracking (CheckedOutByMemberID), and a pointer back to the WorkFlowTemplateStep it was instantiated from. 53 Global fields spanning Statics and Workflow groups.

**Table Association:** `WorkFlowStep` &nbsp;·&nbsp; **Total fields:** 53 (Global: 53, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| CheckedOutByMemberID | `CheckedOutByMemberID` | `sTYPE_MEMBER` | Global | No | No |  | Statics / Hidden |
| CheckedOutDate | `CheckedOutDate` | `sTYPE_DATE` | Global | No | No |  | Statics / Hidden |
| ComputedAlertDateApprovers | `ComputedAlertDateApprovers` | `sTYPE_DATE` | Global | No | No |  | Statics / Hidden |
| ComputedAlertDateAssignees | `ComputedAlertDateAssignees` | `sTYPE_DATE` | Global | No | No |  | Statics / Hidden |
| ComputedDueDateNotification | `ComputedDueDateNotification` | `sTYPE_DATE` | Global | No | No |  | Statics / Hidden |
| ComputedWarnDateApprovers | `ComputedWarnDateApprovers` | `sTYPE_DATE` | Global | No | No |  | Statics / Hidden |
| ComputedWarnDateAssignees | `ComputedWarnDateAssignees` | `sTYPE_DATE` | Global | No | No |  | Statics / Hidden |
| Workflow Template Step | `WorkFlowTemplateStepID` | `sTYPE_WORK_FLOW_TEMPLATE_STEP` | Global | No | No |  | Statics / Workflow |
| Associated Task | `TaskID` | `sTYPE_TASK` | Global | No | No |  | Workflow / Workflow Step (All) |
| Associated Task Name | `TaskName` | `sTYPE_TEXT` | Global | No | No |  | Workflow / Workflow Step (All) |
| Complete Date | `CompleteDate` | `sTYPE_DATE` | Global | No | No |  | Workflow / Workflow Step (All) |
| Current Step Members | `CurrentStepMemberIDList` | `sTYPE_MEMBER` | Global | No | No |  | Workflow / Workflow Step (All) |
| Days Until Alert Approvers | `DaysUntilAlertApprovers` | `sTYPE_NUMBER` | Global | No | No |  | Workflow / Workflow Step (All) |
| Days Until Alert Assignees | `DaysUntilAlertAssignees` | `sTYPE_NUMBER` | Global | No | No |  | Workflow / Workflow Step (All) |
| Days Until Warn Approvers | `DaysUntilWarnApprovers` | `sTYPE_NUMBER` | Global | No | No |  | Workflow / Workflow Step (All) |
| Days Until Warn Assignees | `DaysUntilWarnAssignees` | `sTYPE_NUMBER` | Global | No | No |  | Workflow / Workflow Step (All) |
| Due Date | `DueDate` | `sTYPE_DATE` | Global | No | No |  | Workflow / Workflow Step (All) |
| Duration Days Approvers | `DurationDaysApprovers` | `sTYPE_NUMBER` | Global | No | No |  | Workflow / Workflow Step (All) |
| Duration Days Assignees | `DurationDaysAssignees` | `sTYPE_NUMBER` | Global | No | No |  | Workflow / Workflow Step (All) |
| EMail Alert Approvers | `EMailAlertApprovers` | `sTYPE_BOOLEAN` | Global | No | No |  | Workflow / Workflow Step (All) |
| EMail Alert Assignees | `EMailAlertAssignees` | `sTYPE_BOOLEAN` | Global | No | No |  | Workflow / Workflow Step (All) |
| Email Message | `EMailMessage` | `sTYPE_TEXTAREA` | Global | No | No |  | Workflow / Workflow Step (All) |
| Enable For Dashboard | `EnableForDashboard` | `sTYPE_BOOLEAN` | Global | No | No |  | Workflow / Workflow Step (All) |
| Enable For Email | `EnableForEMail` | `sTYPE_BOOLEAN` | Global | No | No |  | Workflow / Workflow Step (All) |
| Is Completed? | `IsCompleted` | `sTYPE_BOOLEAN` | Global | No | No |  | Workflow / Workflow Step (All) |
| Is Form Step | `IsFormStep` | `sTYPE_BOOLEAN` | Global | No | No |  | Workflow / Workflow Step (All) |
| Is Notify Closed? | `IsNotifyClosed` | `sTYPE_BOOLEAN` | Global | No | No |  | Workflow / Workflow Step (All) |
| Issue | `IssueID` | `sTYPE_ISSUE` | Global | No | No |  | Workflow / Workflow Step (All) |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Workflow / Workflow Step (All) |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Workflow / Workflow Step (All) |
| Page Layout Approvers | `PageLayoutApproversID` | `sTYPE_PAGE_LAYOUT` | Global | No | No |  | Workflow / Workflow Step (All) |
| Page Layout Assignees | `PageLayoutAssigneesID` | `sTYPE_PAGE_LAYOUT` | Global | No | No |  | Workflow / Workflow Step (All) |
| Prior Submit By Member | `PriorSubmitByMemberID` | `sTYPE_MEMBER` | Global | No | No |  | Workflow / Workflow Step (All) |
| Prior Submit For Approval Date | `PriorSubmitForApprovalDate` | `sTYPE_DATE` | Global | No | No |  | Workflow / Workflow Step (All) |
| Priority | `Priority` | `sTYPE_NUMBER` | Global | No | No |  | Workflow / Workflow Step (All) |
| Re Do? | `IsReDo` | `sTYPE_YES_NO_RADIO` | Global | Yes | No |  | Workflow / Workflow Step (All) |
| Read Only? | `IsReadOnly` | `sTYPE_YES_NO_RADIO` | Global | Yes | No |  | Workflow / Workflow Step (All) |
| Start Date | `StartDate` | `sTYPE_DATE` | Global | No | No |  | Workflow / Workflow Step (All) |
| Step Name | `WorkFlowStepName` | `sTYPE_TEXT` | Global | No | No |  | Workflow / Workflow Step (All) |
| Step Number | `StepNumber` | `sTYPE_NUMBER` | Global | Yes | No |  | Workflow / Workflow Step (All) |
| Step Status | `CodeWorkFlowStatusID` | `sCODE_WORK_FLOW_STATUS` | Global | Yes | No |  | Workflow / Workflow Step (All) |
| Submit For Approval By Member | `SubmitForApprovalByMemberID` | `sTYPE_MEMBER` | Global | No | No |  | Workflow / Workflow Step (All) |
| Submit For Approval By Member Name | `SubmitForApprovalByMemberName` | `sTYPE_TEXT` | Global | No | No |  | Workflow / Workflow Step (All) |
| Submit For Approval Date | `SubmitForApprovalDate` | `sTYPE_DATE` | Global | No | No |  | Workflow / Workflow Step (All) |
| WF Approver Due Date | `DueDateApprovers` | `sTYPE_DATE` | Global | No | No |  | Workflow / Workflow Step (All) |
| WF Approver(s) | `ApproverMemberIDList` | `sTYPE_MEMBER` | Global | No | No |  | Workflow / Workflow Step (All) |
| WF Assignee Due Date | `DueDateAssignees` | `sTYPE_DATE` | Global | No | No |  | Workflow / Workflow Step (All) |
| WF Assignee(s) | `AssigneeMemberIDList` | `sTYPE_MEMBER` | Global | No | No |  | Workflow / Workflow Step (All) |
| WF Notify List | `NotifieeMemberIDList` | `sTYPE_MEMBER` | Global | No | No |  | Workflow / Workflow Step (All) |
| WF Step Notification Link | `WFStepNotificationLink` | `sTYPE_TEXT` | Global | No | No |  | Workflow / Workflow Step (All) |
| Work Flow | `WorkFlowID` | `sTYPE_WORK_FLOW` | Global | Yes | No |  | Workflow / Workflow Step (All) |
| Work Flow Step ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Workflow / Workflow Step (All) |
| Work Flow Step RecID | `WorkFlowStepID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Workflow / Workflow Step (All) |
