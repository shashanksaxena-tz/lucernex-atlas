# DevelopmentSlot — Data Fields

A build-out slot within a development pipeline plan — assigned broker/project, current revenue weeks, and duration, feeding ProgramRevenueWeeks reporting. 30 Global fields under RE Planner.

**Table Association:** `DevelopmentSlot` &nbsp;·&nbsp; **Total fields:** 30 (Global: 30, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Assigned Broker | `BrokerMemberID` | `sTYPE_MEMBER` | Global | No | No |  | RE Planner / Targets |
| Assigned Project | `ProjectName` | `sTYPE_TEXT` | Global | No | No |  | RE Planner / Targets |
| Broker Message | `BrokerMessage` | `sTYPE_TEXTAREA` | Global | No | No |  | RE Planner / Targets |
| Current Revenue Weeks | `ActualRevenueWeeks` | `sTYPE_NUMBER` | Global | No | No |  | RE Planner / Targets |
| Development Plan | `DevelopmentPlanID` | `sTYPE_DEVELOPMENT_PLAN` | Global | Yes | No |  | RE Planner / Targets |
| Duration | `Duration` | `sTYPE_NUMBER` | Global | No | No |  | RE Planner / Targets |
| EndDate | `EndDate` | `sTYPE_DATE` | Global | Yes | No |  | RE Planner / Targets |
| Market Area | `CodeMarketAreaID` | `sCODE_MARKET_AREA` | Global | Yes | No |  | RE Planner / Targets |
| Market Type | `CodeMarketTypeID` | `sCODE_MARKET_TYPE` | Global | No | No |  | RE Planner / Targets |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | RE Planner / Targets |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | RE Planner / Targets |
| Name | `DevelopmentSlotName` | `sTYPE_TEXT` | Global | Yes | No |  | RE Planner / Targets |
| Original Planned Open Date | `OriginalEndDate` | `sTYPE_DATE` | Global | No | No |  | RE Planner / Targets |
| Parent Region | `RootRegionID` | `sTYPE_ROOT_REGION` | Global | No | No |  | RE Planner / Targets |
| Planned Open Date | `BaselineEndDate` | `sTYPE_DATE` | Global | No | No |  | RE Planner / Targets |
| Planned Package Date | `PlannedPackageDate` | `sTYPE_DATE` | Global | No | No |  | RE Planner / Targets |
| Portfolio | `ProgramID` | `sTYPE_PROGRAM` | Global | Yes | No |  | RE Planner / Targets |
| Prototype | `PrototypeID` | `sTYPE_PROTOTYPE` | Global | No | No |  | RE Planner / Targets |
| Region | `RegionID` | `sTYPE_REGION` | Global | Yes | No |  | RE Planner / Targets |
| Slot Duration | `SlotDuration` | `sTYPE_NUMBER` | Global | No | No |  | RE Planner / Targets |
| Slot Entity | `ProjectPEID` | `sTYPE_PROJECT_ENTITY` | Global | No | No |  | RE Planner / Targets |
| Store Phase | `CodeStorePhaseID` | `sCODE_STORE_PHASE` | Global | No | No |  | RE Planner / Targets |
| Sub Region | `SubRegionID` | `sTYPE_SUBREGION` | Global | No | No |  | RE Planner / Targets |
| Target ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | RE Planner / Targets |
| Target End Date | `SlotEndDate` | `sTYPE_DATE` | Global | No | No |  | RE Planner / Targets |
| Target RecID | `DevelopmentSlotID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | RE Planner / Targets |
| Target Start Date | `SlotStartDate` | `sTYPE_DATE` | Global | No | No |  | RE Planner / Targets |
| Target Type | `CodeSlotTypeID` | `sCODE_SLOT_TYPE` | Global | No | No |  | RE Planner / Targets |
| Task Template Project Entity ID | `TaskTemplatePEID` | `sTYPE_TASK_TEMPLATE` | Global | No | No |  | RE Planner / Targets |
| Trade Area | `TradeArea` | `sTYPE_TEXT` | Global | No | No |  | RE Planner / Targets |
