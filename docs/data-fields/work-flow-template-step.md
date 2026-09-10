# WorkFlowTemplateStep — Data Fields

One approval step within a reusable workflow template — approver/assignee configuration exposed as four parallel list-type fields per role (Approver Job Title List, Approver Member List, Approver Type, Approver User Class List) so a single step can route to a named person, a job title, a user class, or a mix. 59 Global fields under Company Items; this is template design-time metadata, distinct from WorkFlowStep which is the runtime instance of a step actually executing against a real contract or task.

**Table Association:** `WorkFlowTemplateStep` &nbsp;·&nbsp; **Total fields:** 59 (Global: 59, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Approver Job Title List | `ApproverJobTitleIDList` | `sCODE_JOB_TITLE` | Global | No | No |  | Company Items / Work Flow Template Step |
| Approver Member List | `ApproverMemberIDList` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Work Flow Template Step |
| Approver Type | `ApproverType` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Work Flow Template Step |
| Approver User Class List | `ApproverUserClassIDList` | `sCODE_USER_CLASS` | Global | No | No |  | Company Items / Work Flow Template Step |
| Assignee Job Title List | `AssigneeJobTitleIDList` | `sCODE_JOB_TITLE` | Global | No | No |  | Company Items / Work Flow Template Step |
| Assignee Member List | `AssigneeMemberIDList` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Work Flow Template Step |
| Assignee Type | `AssigneeType` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Work Flow Template Step |
| Assignee User Class List | `AssigneeUserClassIDList` | `sCODE_USER_CLASS` | Global | No | No |  | Company Items / Work Flow Template Step |
| Associated Task Name | `TaskName` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Work Flow Template Step |
| At Complete Approver 1 ID | `RunAtCompleteApprover1ID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Work Flow Template Step |
| At Complete Approver 2 ID | `RunAtCompleteApprover2ID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Work Flow Template Step |
| At Complete Scheduled Job 1 ID | `runAtCompleteScheduledJob1ID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Work Flow Template Step |
| At Complete Scheduled Job 2 ID | `runAtCompleteScheduledJob2ID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Work Flow Template Step |
| At Start Approver 1 ID | `RunAtStartApprover1ID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Work Flow Template Step |
| At Start Approver 2 ID | `RunAtStartApprover2ID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Work Flow Template Step |
| At Start Scheduled Job 1 ID | `runAtStartScheduledJob1ID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Work Flow Template Step |
| At Start Scheduled Job 2 ID | `runAtStartScheduledJob2ID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Work Flow Template Step |
| Automatically Adjust Task Dates to WF Step | `AutoAdjustTaskDates` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Company Items / Work Flow Template Step |
| Automatically Transition to Next Step | `AutoLaunchNextStep` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Company Items / Work Flow Template Step |
| Cancel Task When Step is Canceled | `SetTaskCanceled` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Company Items / Work Flow Template Step |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Work Flow Template Step |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Company Items / Work Flow Template Step |
| Days Until Alert Approvers | `DaysUntilAlertApprovers` | `sTYPE_NUMBER` | Global | No | No |  | Company Items / Work Flow Template Step |
| Days Until Alert Assignees | `DaysUntilAlertAssignees` | `sTYPE_NUMBER` | Global | No | No |  | Company Items / Work Flow Template Step |
| Days Until Notification | `DaysUntilNotification` | `sTYPE_NUMBER` | Global | No | No |  | Company Items / Work Flow Template Step |
| Days Until Warn Approvers | `DaysUntilWarnApprovers` | `sTYPE_NUMBER` | Global | No | No |  | Company Items / Work Flow Template Step |
| Days Until Warn Assignees | `DaysUntilWarnAssignees` | `sTYPE_NUMBER` | Global | No | No |  | Company Items / Work Flow Template Step |
| Description | `Description` | `sTYPE_TEXTAREA` | Global | No | No |  | Company Items / Work Flow Template Step |
| Is a Form Step (vs Task Step) | `IsFormStep` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Work Flow Template Step |
| Layout To Use With Approvers | `PageLayoutApproversID` | `sTYPE_FORM_PAGE_LAYOUT` | Global | No | No |  | Company Items / Work Flow Template Step |
| Layout To Use With Assignees | `PageLayoutAssigneesID` | `sTYPE_FORM_PAGE_LAYOUT` | Global | No | No |  | Company Items / Work Flow Template Step |
| Mark Task In Progress When Step Starts | `SetTaskInProcess` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Company Items / Work Flow Template Step |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Work Flow Template Step |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Company Items / Work Flow Template Step |
| Notifiee Job Title List | `NotifieeJobTitleIDList` | `sCODE_JOB_TITLE` | Global | No | No |  | Company Items / Work Flow Template Step |
| Notifiee Member List | `NotifieeMemberIDList` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Work Flow Template Step |
| Notifiee Type | `NotifieeType` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Work Flow Template Step |
| Notifiee User Class List | `NotifieeUserClassIDList` | `sCODE_USER_CLASS` | Global | No | No |  | Company Items / Work Flow Template Step |
| Notify Step Approvers When Started | `NotifyStepApproversStarted` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Company Items / Work Flow Template Step |
| Notify Step Assignees When Started | `NotifyStepAssigneesStarted` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Company Items / Work Flow Template Step |
| Number of Days For Assignees to Act | `DurationDaysAssignees` | `sTYPE_NUMBER` | Global | No | No |  | Company Items / Work Flow Template Step |
| Number of Days for Approvers to Act | `DurationDaysApprovers` | `sTYPE_NUMBER` | Global | No | No |  | Company Items / Work Flow Template Step |
| Reassign Approvers Job Title List | `ReassignApproversJobTitleIDList` | `sCODE_JOB_TITLE` | Global | No | No |  | Company Items / Work Flow Template Step |
| Reassign Assignees Job Title List | `ReassignAssigneesJobTitleIDList` | `sCODE_JOB_TITLE` | Global | No | No |  | Company Items / Work Flow Template Step |
| Relative Priority | `Priority` | `sTYPE_NUMBER` | Global | No | No |  | Company Items / Work Flow Template Step |
| Requires Approvers? | `ComputedRequiresApprovers` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Work Flow Template Step |
| Requires Assignees? | `ComputedRequiresAssignees` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Work Flow Template Step |
| Rev Number | `RevNumber` | `sTYPE_NUMBER` | Global | No | No |  | Company Items / Work Flow Template Step |
| Should Alert Approvers? | `EMailAlertApprovers` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Work Flow Template Step |
| Should Email Assignees? | `EMailAlertAssignees` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Work Flow Template Step |
| Should Send Email? | `EnableForEMail` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Work Flow Template Step |
| Step Enabled for Dashboard | `EnableForDashboard` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Work Flow Template Step |
| Step Name | `WorkFlowTemplateStepName` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / Work Flow Template Step |
| Step Number | `StepNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | Yes | No |  | Company Items / Work Flow Template Step |
| Text of Email to Send | `EMailMessage` | `sTYPE_TEXTAREA` | Global | No | No |  | Company Items / Work Flow Template Step |
| Unassigned Approver | `UnassignedApproverID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Work Flow Template Step |
| Work Flow Template | `WorkFlowTemplateID` | `sTYPE_WORK_FLOW_TEMPLATE` | Global | Yes | No |  | Company Items / Work Flow Template Step |
| Work Flow Template Step ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / Work Flow Template Step |
| Work Flow Template Step RecID | `WorkFlowTemplateStepID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Work Flow Template Step |
