# WorkFlowStepApprover — Data Fields

One named approver's action on a running WorkFlowStep — action comment, action taken, and has-approved flag, the audit trail of an individual approval decision. 19 Global fields under Workflow.

**Table Association:** `WorkFlowStepApprover` &nbsp;·&nbsp; **Total fields:** 19 (Global: 19, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Action Comment | `ActionComment` | `sTYPE_TEXTAREA` | Global | No | No |  | Workflow / Workflow Step Approver (All) |
| Action Taken | `ActionTakenName` | `sTYPE_TEXT` | Global | No | No |  | Workflow / Workflow Step Approver (All) |
| Action Taken Date | `ActionTakenDate` | `sTYPE_DATE` | Global | No | No |  | Workflow / Workflow Step Approver (All) |
| Approver | `MemberID` | `sTYPE_MEMBER` | Global | Yes | No |  | Workflow / Workflow Step Approver (All) |
| Email Sent Status | `EMailSentStatus` | `sTYPE_TEXT` | Global | Yes | No |  | Workflow / Workflow Step Approver (All) |
| Has Approved? | `HasApproved` | `sTYPE_YES_NO_RADIO` | Global | No | No |  | Workflow / Workflow Step Approver (All) |
| Has Taken Action? | `HasTakenAction` | `sTYPE_YES_NO_RADIO` | Global | No | No |  | Workflow / Workflow Step Approver (All) |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Workflow / Workflow Step Approver (All) |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Workflow / Workflow Step Approver (All) |
| Notify Acknowledged Status | `NotifyAcknowledgedStatus` | `sTYPE_TEXT` | Global | Yes | No |  | Workflow / Workflow Step Approver (All) |
| Prior Action Comment | `PriorActionComment` | `sTYPE_TEXTAREA` | Global | No | No |  | Workflow / Workflow Step Approver (All) |
| Prior Action Taken Date | `PriorActionTakenDate` | `sTYPE_DATE` | Global | No | No |  | Workflow / Workflow Step Approver (All) |
| Prior WF Step Action | `PriorWFTemplateStepActionID` | `sTYPE_WORK_FLOW_TEMPLATE_STEP_ACTION` | Global | No | No |  | Workflow / Workflow Step Approver (All) |
| Signature Date | `SignatureDate` | `sTYPE_DATE` | Global | No | No |  | Workflow / Workflow Step Approver (All) |
| WF Step Action | `WorkFlowTemplateStepActionID` | `sTYPE_WORK_FLOW_TEMPLATE_STEP_ACTION` | Global | No | No |  | Workflow / Workflow Step Approver (All) |
| WF Step Approver ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Workflow / Workflow Step Approver (All) |
| WF Step Approver RecID | `WorkFlowStepApproverID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Workflow / Workflow Step Approver (All) |
| Work Flow Step | `WorkFlowStepID` | `sTYPE_WORK_FLOW_STEP` | Global | Yes | No |  | Workflow / Workflow Step Approver (All) |
| Work Flow Template Step | `WorkFlowTemplateStepID` | `sTYPE_WORK_FLOW_TEMPLATE_STEP` | Global | No | No |  | Workflow / Workflow Step Approver (All) |
