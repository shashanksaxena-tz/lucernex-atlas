# WorkFlowTemplateStepAction — Data Fields

The button/action definition available at a workflow template step (Approve, Reject, Send Back) — Boolean flags controlling what the action does to the workflow (Should Close Work Flow?, Should Move to Next Step, Should Restart the Step?) plus finance-specific behavior like FIFO pay-app validation and auto-copy of amounts. 39 Global fields under Company Items and Statics.

**Table Association:** `WorkFlowTemplateStepAction` &nbsp;·&nbsp; **Total fields:** 39 (Global: 39, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Action Comment | `ActionComment` | `sTYPE_TEXTAREA` | Global | No | No |  | Company Items / Work Flow Template Step Action |
| Action Name | `WorkFlowTemplateStepActionName` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / Work Flow Template Step Action |
| Action Should Close Work Flow? | `CloseWorkFlow` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Company Items / Work Flow Template Step Action |
| Action Should Disable Edit? | `DisableEditAfterDecision` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Company Items / Work Flow Template Step Action |
| Action Should Move to Next Step Number | `MoveToStepNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Work Flow Template Step Action |
| Action Should Restart the Step? | `RestartStep` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Company Items / Work Flow Template Step Action |
| Apply FIFO Pay App Validation | `FifoPayApp` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Work Flow Template Step Action |
| Auto Clear Amounts | `AutoClearAmounts` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Work Flow Template Step Action |
| Auto Copy Amounts | `AutoCopyAmounts` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Work Flow Template Step Action |
| Bid Award Approval Status | `bidAwdApCodeLastActionStatusID` | `sCODE_LAST_ACTION_STATUS` | Global | No | No |  | Company Items / Work Flow Template Step Action |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Work Flow Template Step Action |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Company Items / Work Flow Template Step Action |
| Description | `Description` | `sTYPE_TEXTAREA` | Global | No | No |  | Company Items / Work Flow Template Step Action |
| Generate Purchase Order Line Sequence Number | `GenPurchOrderLineSeqNum` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Work Flow Template Step Action |
| Is Approval Action? | `IsApprovalAction` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Company Items / Work Flow Template Step Action |
| Javascript Source Code | `IsEnabledLxJSCode` | `sTYPE_TEXTAREA` | Global | No | No |  | Company Items / Work Flow Template Step Action |
| Kick Off Description | `KickOffDescription` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Work Flow Template Step Action |
| Kick Off Work Flow Template | `KickOffWorkFlowTemplateID` | `sTYPE_WORK_FLOW_TEMPLATE` | Global | No | No |  | Company Items / Work Flow Template Step Action |
| Kick Off Work Flow Template Trigger | `KickOffTargetWFTemplateID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Work Flow Template Step Action |
| Last Action Status | `CodeLastActionStatusID` | `sCODE_LAST_ACTION_STATUS` | Global | No | No |  | Company Items / Work Flow Template Step Action |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Work Flow Template Step Action |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Company Items / Work Flow Template Step Action |
| Notify Initiator on Complete? | `NotifyInitiatorComplete` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Company Items / Work Flow Template Step Action |
| Notify Prior Approvers on Complete? | `NotifyPriorApproversComplete` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Company Items / Work Flow Template Step Action |
| Notify Prior Assignees on Complete? | `NotifyPriorAssigneesComplete` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Company Items / Work Flow Template Step Action |
| Notify Step Approvers on Complete? | `NotifyStepApproversComplete` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Company Items / Work Flow Template Step Action |
| Notify Step Assignees on Complete? | `NotifyStepAssigneesComplete` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Company Items / Work Flow Template Step Action |
| Pass Adhoc Assignee To New Work Flow? | `PassAdhocToNewWF` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Company Items / Work Flow Template Step Action |
| Pass Priority To New Work Flow? | `PassPriorityToNewWF` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Company Items / Work Flow Template Step Action |
| Require All Approvers? | `RequireAllApprovers` | `sTYPE_CHECKBOX` | Global | Yes | No |  | Company Items / Work Flow Template Step Action |
| Require Approver Signature | `RequireApproverSig` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Work Flow Template Step Action |
| Rev Number | `RevNumber` | `sTYPE_NUMBER` | Global | No | No |  | Company Items / Work Flow Template Step Action |
| Send Payment Info? | `SendPaymentInfo` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Company Items / Work Flow Template Step Action |
| WF Step Action Entity | `ProjectEntityID` | `sTYPE_PROJECT_ENTITY` | Global | No | No |  | Company Items / Work Flow Template Step Action |
| Work Flow Template Kick Off | `WorkFlowTemplateKickOffID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Work Flow Template Step Action |
| Work Flow Template Step | `WorkFlowTemplateStepID` | `sTYPE_WORK_FLOW_TEMPLATE_STEP` | Global | No | No |  | Company Items / Work Flow Template Step Action |
| Work Flow Template Step Action ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / Work Flow Template Step Action |
| Work Flow Template Step Action RecID | `WorkFlowTemplateStepActionID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Work Flow Template Step Action |
| Workflow Template Step Action | `WorkFlowTemplateStepActionID` | `sTYPE_WORK_FLOW_TEMPLATE_STEP_ACTION` | Global | No | No |  | Statics / Workflow |
