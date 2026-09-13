# Workflow & Notification Ancillary Tables

These 6 tables (49 fields, all Global) sit beneath the large standalone workflow entities ([WorkFlow](work-flow.md), [WorkFlowStep](work-flow-step.md), [WorkFlowTemplateStep](work-flow-template-step.md), [WorkFlowStepApprover](work-flow-step-approver.md)) and handle the assignee (as opposed to approver) side of a running step, template-time member targeting, and the separate email/dashboard notification subsystem that workflow steps can trigger. `Notify` itself is a single-field stub, included here rather than dropped so every distinct TableAssociation value stays accounted for.

**Entities in this file:** 6 &nbsp;·&nbsp; **Total fields:** 49 (Global: 49, Firm: 0)

| Entity | Fields (G/F) | One-line role |
|---|---|---|
| `NotifyTemplate` | 12 (12/0) | A reusable email/dashboard notification template — trigger table, message body, and channel enablement flags. |
| `IssueResponse` | 11 (11/0) | A reply/answer posted against a bidder Issue (Q&A) during a bid process. |
| `WorkFlowStepAssignee` | 10 (10/0) | One assignee's notification/acknowledgment status on a running WorkFlowStep, parallel to WorkFlowStepApprover for the assignee (rather than approver) role. |
| `WorkFlowTemplateStepMember` | 9 (9/0) | Template-time configuration of which specific Member (or ad-hoc member) fills a WorkFlowTemplateStep role, including org-chart-level targeting. |
| `NotifyTemplateMember` | 6 (6/0) | The recipient list for a NotifyTemplate, targetable by member, job title, or org-chart level. |
| `Notify` | 1 (1/0) | A single-field stub representing an individual fired notification instance. |

Field type codes are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Entity | Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|---|
| NotifyTemplate | Alert type | `AlertType` | `sTYPE_TEXT` | Global | Yes | No |  | Statics / Hidden |
| NotifyTemplate | Code SQL Table of parent record | `CodeSQLTableID` | `sCODE_SQLTABLE` | Global | Yes | No |  | Statics / Hidden |
| NotifyTemplate | Email message | `EMailMessage` | `sTYPE_TEXT` | Global | No | No |  | Statics / Hidden |
| NotifyTemplate | Enable For Email | `EnableForEMail` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Statics / Hidden |
| NotifyTemplate | Enable for dashboard | `EnableForDashboard` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Statics / Hidden |
| NotifyTemplate | Notification Days | `DaysOffsetFromTargetDate` | `sTYPE_UNFORMATTED_NUMBER` | Global | Yes | No |  | Statics / Hidden |
| NotifyTemplate | Notify Template RecID | `NotifyTemplateID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Statics / Hidden |
| NotifyTemplate | Notify template name | `NotifyTemplateName` | `sTYPE_TEXT` | Global | Yes | No |  | Statics / Hidden |
| NotifyTemplate | Primary key of parent record | `ObjectID` | `sTYPE_UNFORMATTED_NUMBER` | Global | Yes | No |  | Statics / Hidden |
| NotifyTemplate | Sub Alert Type | `SubAlertType` | `sTYPE_TEXT` | Global | Yes | No |  | Statics / Hidden |
| NotifyTemplate | Trigger value 1 | `TriggerValue1` | `sTYPE_TEXT` | Global | No | No |  | Statics / Hidden |
| NotifyTemplate | Trigger value 2 | `TriggerValue2` | `sTYPE_TEXT` | Global | No | No |  | Statics / Hidden |
| IssueResponse | Body | `Body` | `sTYPE_TEXT` | Global | No | No |  | Workflow / Issue Response |
| IssueResponse | Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Workflow / Issue Response |
| IssueResponse | Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Workflow / Issue Response |
| IssueResponse | Issue ID | `IssueID` | `sTYPE_ISSUE` | Global | Yes | No |  | Workflow / Issue Response |
| IssueResponse | Issue Response ID | `IssueResponseID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Workflow / Issue Response |
| IssueResponse | Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Workflow / Issue Response |
| IssueResponse | Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Workflow / Issue Response |
| IssueResponse | ProjectEntity ID | `ProjectEntityID` | `sTYPE_PROJECT_ENTITY` | Global | Yes | No |  | Workflow / Issue Response |
| IssueResponse | Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Workflow / Issue Response |
| IssueResponse | Sequence Number | `SequenceNumber` | `sTYPE_TEXT` | Global | Yes | No |  | Workflow / Issue Response |
| IssueResponse | Subject | `Subject` | `sTYPE_TEXT` | Global | Yes | No |  | Workflow / Issue Response |
| WorkFlowStepAssignee | Assignee | `MemberID` | `sTYPE_MEMBER` | Global | Yes | No |  | Workflow / Workflow Step Assignee (All) |
| WorkFlowStepAssignee | Email Sent Status | `EMailSentStatus` | `sTYPE_TEXT` | Global | Yes | No |  | Workflow / Workflow Step Assignee (All) |
| WorkFlowStepAssignee | Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Workflow / Workflow Step Assignee (All) |
| WorkFlowStepAssignee | Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Workflow / Workflow Step Assignee (All) |
| WorkFlowStepAssignee | Notify Acknowledged Status | `NotifyAcknowledgedStatus` | `sTYPE_TEXT` | Global | Yes | No |  | Workflow / Workflow Step Assignee (All) |
| WorkFlowStepAssignee | Step Member Responsibility | `StepMemberResponsibility` | `sTYPE_TEXT` | Global | Yes | No |  | Workflow / Workflow Step Assignee (All) |
| WorkFlowStepAssignee | WF Step Assignee ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Workflow / Workflow Step Assignee (All) |
| WorkFlowStepAssignee | WF Step Assignee RecID | `WorkFlowStepAssigneeID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Workflow / Workflow Step Assignee (All) |
| WorkFlowStepAssignee | Work Flow Step | `WorkFlowStepID` | `sTYPE_WORK_FLOW_STEP` | Global | Yes | No |  | Workflow / Workflow Step Assignee (All) |
| WorkFlowStepAssignee | Work Flow Template Step | `WorkFlowTemplateStepID` | `sTYPE_WORK_FLOW_TEMPLATE_STEP` | Global | No | No |  | Workflow / Workflow Step Assignee (All) |
| WorkFlowTemplateStepMember | Adhoc Member ID | `AdhocMemberID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Statics / Hidden |
| WorkFlowTemplateStepMember | Is Adhoc? | `IsAdhoc` | `sTYPE_BOOLEAN` | Global | No | No |  | Statics / Hidden |
| WorkFlowTemplateStepMember | WF Template Step Member | `MemberID` | `sTYPE_MEMBER` | Global | No | No |  | Statics / Hidden |
| WorkFlowTemplateStepMember | WF Template Step Member Job Title | `CodeJobTitleID` | `sCODE_JOB_TITLE` | Global | No | No |  | Statics / Hidden |
| WorkFlowTemplateStepMember | WF Template Step Member Org Chart Level | `OrgChartLevel` | `sTYPE_NUMBER` | Global | No | No |  | Statics / Hidden |
| WorkFlowTemplateStepMember | WF Template Step Member RecID | `WorkFlowTemplateStepMemberID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Statics / Hidden |
| WorkFlowTemplateStepMember | WF Template Step Member Responsibility | `StepMemberResponsibility` | `sTYPE_TEXT` | Global | Yes | No |  | Statics / Hidden |
| WorkFlowTemplateStepMember | WF Template Step Member Step | `WorkFlowTemplateStepID` | `sTYPE_WORK_FLOW_TEMPLATE_STEP` | Global | Yes | No |  | Statics / Hidden |
| WorkFlowTemplateStepMember | WF Template Step Member User Class | `CodeUserClassID` | `sCODE_USER_CLASS` | Global | No | No |  | Statics / Hidden |
| NotifyTemplateMember | Notify Job Title | `CodeJobTitleID` | `sCODE_JOB_TITLE` | Global | No | No |  | Statics / Hidden |
| NotifyTemplateMember | Notify Member | `MemberID` | `sTYPE_MEMBER` | Global | No | No |  | Statics / Hidden |
| NotifyTemplateMember | Notify Org Chart Level | `OrgChartLevel` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Statics / Hidden |
| NotifyTemplateMember | Notify Template | `NotifyTemplateID` | `sTYPE_NOTIFY_TEMPLATE` | Global | Yes | No |  | Statics / Hidden |
| NotifyTemplateMember | Notify Template Member | `NotifyTemplateMemberID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Statics / Hidden |
| NotifyTemplateMember | Notify User Class | `CodeUserClassID` | `sCODE_USER_CLASS` | Global | No | No |  | Statics / Hidden |
| Notify | Notify RecID | `NotifyID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Statics / Hidden |
