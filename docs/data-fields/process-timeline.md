# ProcessTimeline — Data Fields

A generic milestone/phase timeline attached to a Location or ProjectEntity — actual vs. baseline vs. original end dates and duration, spanning the Location and Milestones groups since timelines apply to both site selection and construction phases. 30 Global fields.

**Table Association:** `ProcessTimeline` &nbsp;·&nbsp; **Total fields:** 30 (Global: 30, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Process Timeline RecID | `ProcessTimelineID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Location / Audit Info |
| Actual End Date | `TskDone_ActualEndDate` | `sTYPE_DATE` | Global | No | No |  | Milestones / Actual End Date |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Milestones / Audit Info |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Milestones / Audit Info |
| Baseline Duration | `OriginalDuration` | `sTYPE_NUMBER` | Global | No | No |  | Milestones / Baseline Duration |
| Original End Date | `OriginalEndDate` | `sTYPE_DATE` | Global | No | No |  | Milestones / Baseline End Date |
| Baseline Lead/Lag Days | `TskPredVal_OriginalLeadLagDays` | `sTYPE_NUMBER` | Global | No | No |  | Milestones / Baseline Lead/Lag Days |
| Baseline Start Date | `OriginalStartDate` | `sTYPE_DATE` | Global | No | No |  | Milestones / Baseline Start Date |
| Baseline with Forecast/Actual End Date | `TskBAndA_NoAccessorConversion` | `sTYPE_TEXT` | Global | No | No |  | Milestones / Baseline with Forecast/Actual End Date |
| Description | `Description` | `sTYPE_TEXTAREA` | Global | No | No |  | Milestones / Comments |
| Days Ahead of Schedule | `DaysAheadOfSchedule` | `sTYPE_NUMBER` | Global | No | No |  | Milestones / Days Ahead of Schedule |
| Forecast End Date | `TskNotDone_ActualEndDate` | `sTYPE_DATE` | Global | No | No |  | Milestones / Forecast End Date |
| Forecast End Date/Complete | `TskNotDoneCompleted_NoAccessorConversion` | `sTYPE_TEXT` | Global | No | No |  | Milestones / Forecast End Date/Complete |
| Forecast/Actual Duration | `ActualDuration` | `sTYPE_NUMBER` | Global | No | No |  | Milestones / Forecast/Actual Duration |
| Forecast/Actual End Date | `ActualEndDate` | `sTYPE_DATE` | Global | No | No |  | Milestones / Forecast/Actual End Date |
| Forecast/Actual Lead/Lag Days | `TskPredVal_ActualLeadLagDays` | `sTYPE_NUMBER` | Global | No | No |  | Milestones / Forecast/Actual Lead/Lag Days |
| Forecast/Actual Start Date | `ActualStartDate` | `sTYPE_DATE` | Global | No | No |  | Milestones / Forecast/Actual Start Date |
| Milestone Name | `ProcessTimelineTemplateName` | `sTYPE_TEXT` | Global | No | No |  | Milestones / Milestone Name |
| Task Status | `CodeTaskStatusID` | `sCODE_TASK_STATUS` | Global | No | No |  | Milestones / Milestone Status |
| Percent Complete | `PercentComplete` | `sTYPE_NUMBER` | Global | No | No |  | Milestones / Percent Complete |
| Projected Duration | `ProjectedDuration` | `sTYPE_NUMBER` | Global | No | No |  | Milestones / Projected Duration |
| Projected End Date | `ProjectedEndDate` | `sTYPE_DATE` | Global | No | No |  | Milestones / Projected End Date |
| Projected Lead/Lag Days | `TskPredVal_ProjectedLeadLagDays` | `sTYPE_NUMBER` | Global | No | No |  | Milestones / Projected Lead/Lag Days |
| Projected Start Date | `ProjectedStartDate` | `sTYPE_DATE` | Global | No | No |  | Milestones / Projected Start Date |
| Remaining Days | `RemainingDays` | `sTYPE_NUMBER` | Global | No | No |  | Milestones / Remaining Days |
| Members | `Assignee_MemberID` | `sTYPE_MEMBER` | Global | No | No |  | Milestones / Resources |
| Alert when task Completes | `EnableForDashboard` | `sTYPE_CHECKBOX` | Global | No | No |  | Milestones / Security Fields |
| Email Message | `EMailMessage` | `sTYPE_TEXTAREA` | Global | No | No |  | Milestones / Security Fields |
| Email when task Completes | `EnableForEMail` | `sTYPE_CHECKBOX` | Global | No | No |  | Milestones / Security Fields |
| Task Name | `TaskName` | `sTYPE_TEXT` | Global | No | No |  | Milestones / Task Name |
