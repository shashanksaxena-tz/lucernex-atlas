# KeyDate — Data Fields

A tracked deadline/notice date tied to a Contract, Contract Term, or Covenant — action date/period (with a configurable period unit: days, months, etc.), earliest notice date, and coverage period bounds, used to drive renewal, termination, and compliance-notice alerts. 41 fields (31 Global, 10 Firm) under Contract; one of the entities the user specifically flagged, and its 10 Firm fields suggest ASG tracks additional tenant-specific deadline types beyond the base platform set.

**Table Association:** `KeyDate` &nbsp;·&nbsp; **Total fields:** 41 (Global: 31, Firm: 10)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Action Date | `ActionDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Key Date |
| Action Period | `ActionPeriod` | `sTYPE_DATE_DAYS_MATH_OPERATION` | Global | No | No |  | Contract / Key Date |
| Action Period Unit | `CodeActionPeriodUnitID` | `sCODE_TIME_UNIT` | Global | No | No |  | Contract / Key Date |
| Contingency | `Firm_Contingency` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Key Date |
| Contingency Trigger | `Firm_ContingencyTrigger` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Key Date |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | Yes | No |  | Contract / Key Date |
| Contract Term | `ContractTermID` | `sTYPE_CONTRACT_TERM` | Global | No | No |  | Contract / Key Date |
| Covenant | `CovenantID` | `sTYPE_COVENANT` | Global | No | No |  | Contract / Key Date |
| Coverage Period Begin Date | `BeginDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Key Date |
| Coverage Period End Date | `EndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Key Date |
| Description | `Description` | `sTYPE_TEXT` | Global | No | No |  | Contract / Key Date |
| Document | `Firm_KeyDateDocument` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Key Date |
| Earliest Notice Date | `NoticeBeginDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Key Date |
| Earliest Notice Period | `FirstNoticePeriod` | `sTYPE_DATE_DAYS_MATH_OPERATION` | Global | No | No |  | Contract / Key Date |
| Earliest Notice Period Unit | `CodeFirstNoticePeriodUnitID` | `sCODE_TIME_UNIT` | Global | No | No |  | Contract / Key Date |
| Earliest Termination Date | `Firm_KeyDateEarliestTerminationDate` | `sTYPE_DATE` | Firm | No | No |  | Contract / Key Date |
| First Event Begin Date | `FirstEventBeginDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Key Date |
| Fleet Review Decision | `Firm_FleetReviewDecision` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Key Date |
| Frequency | `CodeFrequencyID` | `sCODE_MONTH_FREQUENCY` | Global | No | No |  | Contract / Key Date |
| Is Action Complete? | `ActionComplete` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Key Date |
| Key Date Action | `CodeKeyDateActionID` | `sCODE_KEY_DATE_ACTION` | Global | No | No |  | Contract / Key Date |
| Key Date ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Key Date |
| Key Date Event Table | `KeyDateEventTable` | `sTYPE_TEXT` | Global | No | No |  | Contract / Key Date |
| Key Date Group | `CodeKeyDateGroupID` | `sCODE_KEY_DATE_GROUP` | Global | No | No |  | Contract / Key Date |
| Key Date RecID | `KeyDateID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Key Date |
| Key Date Type | `CodeKeyDateTypeID` | `sCODE_KEY_DATE_TYPE` | Global | No | No |  | Contract / Key Date |
| Last Notice Date | `NoticeEndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Key Date |
| Last Notice Period | `NoticePeriod` | `sTYPE_DATE_DAYS_MATH_OPERATION` | Global | No | No |  | Contract / Key Date |
| Last Notice Period Unit | `CodeNoticePeriodUnitID` | `sCODE_TIME_UNIT` | Global | No | No |  | Contract / Key Date |
| Latest Termination Date | `Firm_KeyDateLatestTerminationDate` | `sTYPE_DATE` | Firm | No | No |  | Contract / Key Date |
| Length | `LengthOfTerm` | `sTYPE_DATE_MATH_OPERATION` | Global | No | No |  | Contract / Key Date |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Key Date |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Key Date |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Key Date |
| Notice Received? | `NoticeReceivedFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Key Date |
| Notice Sent? | `NoticeSentFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Key Date |
| Page | `Firm_KeyDatePage` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Key Date |
| REC Comments | `Firm_RECComments` | `sTYPE_TEXTAREA` | Firm | No | No |  | Contract / Key Date |
| REC Decision | `Firm_RECDecision` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Key Date |
| Section | `Firm_KeyDateSection` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Key Date |
| Tickler Last Notice Date | `TicklerDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Key Date |
