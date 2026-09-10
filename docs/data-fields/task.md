# Task — Data Fields

A schedule/project task record — baseline vs. actual dates and durations, lead/lag days, and resource unit tracking, the core row of the project-scheduling module (paired with TaskPredecessor for dependency chains). 37 Global fields under Schedule and Statics.

**Table Association:** `Task` &nbsp;·&nbsp; **Total fields:** 37 (Global: 37, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Actual End Date | `TskDone_ActualEndDate` | `sTYPE_DATE` | Global | No | No |  | Schedule / Actual End Date |
| Actual Resource Units | `ActualResourceUnits` | `sTYPE_NUMBER` | Global | No | No |  | Schedule / Actual Resource Units |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Schedule / Audit Info |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Schedule / Audit Info |
| Baseline Duration | `OriginalDuration` | `sTYPE_NUMBER` | Global | No | No |  | Schedule / Baseline Duration |
| Baseline End Date | `OriginalEndDate` | `sTYPE_DATE` | Global | No | No |  | Schedule / Baseline End Date |
| Baseline Lead/Lag Days | `TskPredVal_OriginalLeadLagDays` | `sTYPE_NUMBER` | Global | No | No |  | Schedule / Baseline Lead/Lag Days |
| Baseline Start Date | `OriginalStartDate` | `sTYPE_DATE` | Global | No | No |  | Schedule / Baseline Start Date |
| Baseline with Forecast/Actual End Date | `TskBAndA_NoAccessorConversion` | `sTYPE_TEXT` | Global | No | No |  | Schedule / Baseline with Forecast/Actual End Date |
| Description | `Description` | `sTYPE_TEXTAREA` | Global | No | No |  | Schedule / Comments |
| Days Ahead of Schedule | `DaysAheadOfSchedule` | `sTYPE_NUMBER` | Global | No | No |  | Schedule / Days Ahead of Schedule |
| Forecast End Date | `TskNotDone_ActualEndDate` | `sTYPE_DATE` | Global | No | No |  | Schedule / Forecast End Date |
| Forecast End Date/Complete | `TskNotDoneCompleted_NoAccessorConversion` | `sTYPE_TEXT` | Global | No | No |  | Schedule / Forecast End Date/Complete |
| Forecast/Actual Duration | `ActualDuration` | `sTYPE_NUMBER` | Global | No | No |  | Schedule / Forecast/Actual Duration |
| Forecast/Actual End Date | `ActualEndDate` | `sTYPE_DATE` | Global | No | No |  | Schedule / Forecast/Actual End Date |
| Forecast/Actual Lead/Lag Days | `TskPredVal_ActualLeadLagDays` | `sTYPE_NUMBER` | Global | No | No |  | Schedule / Forecast/Actual Lead/Lag Days |
| Forecast/Actual Start Date | `ActualStartDate` | `sTYPE_DATE` | Global | No | No |  | Schedule / Forecast/Actual Start Date |
| Is Task Group | `IsTaskGroup` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Schedule / Is Task Group |
| Name | `TaskName` | `sTYPE_TEXT` | Global | Yes | No |  | Schedule / Name |
| On Critical Path? | `OnCriticalPath` | `sTYPE_BOOLEAN` | Global | No | No |  | Schedule / On Critical Path? |
| Original Resource Units | `OriginalResourceUnits` | `sTYPE_NUMBER` | Global | No | No |  | Schedule / Original Resource Units |
| Parent Task | `ParentTaskID` | `sTYPE_TASK` | Global | No | No |  | Schedule / Parent Task |
| Percent Complete | `PercentComplete` | `sTYPE_NUMBER` | Global | No | No |  | Schedule / Percent Complete |
| Predecessor Task(s) | `TskPredVal_PredecessorTaskID` | `sTYPE_TASK` | Global | No | No |  | Schedule / Predecessor Task |
| Projected Duration | `ProjectedDuration` | `sTYPE_NUMBER` | Global | No | No |  | Schedule / Projected Duration |
| Projected End Date | `ProjectedEndDate` | `sTYPE_DATE` | Global | No | No |  | Schedule / Projected End Date |
| Projected Lead/Lag Days | `TskPredVal_ProjectedLeadLagDays` | `sTYPE_NUMBER` | Global | No | No |  | Schedule / Projected Lead/Lag Days |
| Projected Resource Units | `ProjectedResourceUnits` | `sTYPE_NUMBER` | Global | No | No |  | Schedule / Projected Resource Units |
| Projected Start Date | `ProjectedStartDate` | `sTYPE_DATE` | Global | No | No |  | Schedule / Projected Start Date |
| Resources | `Assignee_MemberID` | `sTYPE_MEMBER` | Global | No | No |  | Schedule / Resources |
| Alert when task Completes | `EnableForDashboard` | `sTYPE_CHECKBOX` | Global | No | No |  | Schedule / Security Fields |
| Email Message | `EMailMessage` | `sTYPE_TEXTAREA` | Global | No | No |  | Schedule / Security Fields |
| Email when task Completes | `EnableForEMail` | `sTYPE_CHECKBOX` | Global | No | No |  | Schedule / Security Fields |
| Task Ends On Day | `TaskEndsCodeDayOfWeekID` | `sCODE_DAY_OF_WEEK` | Global | No | No |  | Schedule / Task Ends On Day |
| Task RecID | `TaskID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Schedule / Task RecID |
| Task Status | `CodeTaskStatusID` | `sCODE_TASK_STATUS` | Global | No | No |  | Schedule / Task Status |
| Members Assigned to Task | `AssigneeMemberIDList` | `sTYPE_MEMBER` | Global | No | No |  | Statics / Hidden |
