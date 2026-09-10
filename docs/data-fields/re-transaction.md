# RETransaction — Data Fields

The formal real-estate transaction record once a Scenario converts into an active deal — approved capital budget, deal schedule, and begin date. 30 Global fields under RE Transaction; sits between Scenario (evaluation) and Contract (executed lease) in the deal lifecycle.

**Table Association:** `RETransaction` &nbsp;·&nbsp; **Total fields:** 30 (Global: 30, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Active Deal Step(s) | `ActiveDealStepTaskIDList` | `sTYPE_TASK` | Global | No | No |  | RE Transaction / RE Transaction Info |
| Approved Capital Budget | `ApprovedCapitalBudget` | `sTYPE_MONEY` | Global | No | No |  | RE Transaction / RE Transaction Info |
| Begin Date | `BeginDate` | `sTYPE_DATE` | Global | No | No |  | RE Transaction / RE Transaction Info |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | RE Transaction / RE Transaction Info |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | RE Transaction / RE Transaction Info |
| Deal Schedule | `DealSchedule` | `sTYPE_TASK` | Global | No | No |  | RE Transaction / RE Transaction Info |
| Deal Steps | `DealStepSchedule` | `sTYPE_MINISCHEDULE` | Global | No | No |  | RE Transaction / RE Transaction Info |
| Documents | `DocumentIDList` | `sTYPE_DOCUMENT_LIST` | Global | No | No |  | RE Transaction / RE Transaction Info |
| End Date | `EndDate` | `sTYPE_DATE` | Global | No | No |  | RE Transaction / RE Transaction Info |
| Facility | `FacilityID` | `sTYPE_FACILITY` | Global | No | No |  | RE Transaction / RE Transaction Info |
| Kickoff Contract Covenant | `KickoffCovenantID` | `sTYPE_COVENANT` | Global | No | No |  | RE Transaction / RE Transaction Info |
| Kickoff Contract Key Date | `KickoffKeyDateID` | `sTYPE_KEY_DATE` | Global | No | No |  | RE Transaction / RE Transaction Info |
| Kickoff Contract Term | `KickoffContractTermID` | `sTYPE_CONTRACT_TERM` | Global | No | No |  | RE Transaction / RE Transaction Info |
| Kickoff Scenario | `KickoffScenarioID` | `sTYPE_SCENARIO` | Global | No | No |  | RE Transaction / RE Transaction Info |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | RE Transaction / RE Transaction Info |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | RE Transaction / RE Transaction Info |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | RE Transaction / RE Transaction Info |
| Number of Scenarios | `NumberOfScenarios` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | RE Transaction / RE Transaction Info |
| Preferred Scenario | `PreferredScenarioID` | `sTYPE_SCENARIO` | Global | No | No |  | RE Transaction / RE Transaction Info |
| Preferred Scenario Covenant Notes | `PreferredScenarioCovenantNotes` | `sTYPE_TEXTAREA` | Global | No | No |  | RE Transaction / RE Transaction Info |
| Preferred Scenario Deal Type | `PreferredScenarioCodeDealTypeID` | `sCODE_SCENARIO_DEAL_TYPE` | Global | No | No |  | RE Transaction / RE Transaction Info |
| Program | `ProgramID` | `sTYPE_PROGRAM` | Global | Yes | No |  | RE Transaction / RE Transaction Info |
| RE Transaction ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | RE Transaction / RE Transaction Info |
| RE Transaction RecID | `RETransactionID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | RE Transaction / RE Transaction Info |
| Related Transaction | `RelatedTransactionID` | `sTYPE_RE_TRANSACTION` | Global | No | No |  | RE Transaction / RE Transaction Info |
| Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | RE Transaction / RE Transaction Info |
| Selected Scenario | `SelectedScenarioID` | `sTYPE_SCENARIO` | Global | No | No |  | RE Transaction / RE Transaction Info |
| Transaction Manager | `AssigneeMemberID` | `sTYPE_MEMBER` | Global | No | No |  | RE Transaction / RE Transaction Info |
| Transaction Name | `TransactionName` | `sTYPE_TEXT` | Global | Yes | No |  | RE Transaction / RE Transaction Info |
| Transaction Status | `CodeRETransactionStatusID` | `sCODE_RE_TRANSACTION_STATUS` | Global | No | No |  | RE Transaction / RE Transaction Info |
