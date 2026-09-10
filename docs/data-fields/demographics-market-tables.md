# Demographics & Site-Selection Reference Tables

These 6 tables (52 fields, all Global) support site-selection analysis — the same discipline SiteSurvey (78 fields, standalone) captures at the individual-site level, but here modeled as reusable geography (`Region`, `DMA`) and reusable study/report definitions (`DemographicStudyArea`, `DemographicReport`, `DemographicFact`, `DemographicResults`) that can be run against many candidate sites rather than hard-coded to one survey's fixed mile-radius bands.

**Entities in this file:** 6 &nbsp;·&nbsp; **Total fields:** 52 (Global: 52, Firm: 0)

| Entity | Fields (G/F) | One-line role |
|---|---|---|
| `DemographicResults` | 11 (11/0) | A saved demographic analysis output for a site — name, description, and an attached results document. |
| `DemographicReport` | 10 (10/0) | A demographic report definition tied to a market area, the report-level wrapper around DemographicResults/DemographicFact data. |
| `DemographicFact` | 10 (10/0) | One data point within a demographic report, with an ordering sequence for display. |
| `Region` | 8 (8/0) | A geographic region in the portfolio hierarchy — parent/previous region linkage and operating status, referenced by LinkRegionManager and LinkRegionMarket. |
| `DMA` | 7 (7/0) | A Designated Market Area (a standard US media-market geography) reference record, used for site-selection demographic comparison. |
| `DemographicStudyArea` | 6 (6/0) | The trade-area definition used for a demographic study — radius in miles or drive time in minutes, an alternative to SiteSurvey's fixed 1/3/5-mile bands. |

Field type codes are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Entity | Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|---|
| DemographicResults | Demographic Results ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Demographics Criteria / Demographic Results |
| DemographicResults | Demographic Results Description | `Description` | `sTYPE_TEXTAREA` | Global | No | No |  | Demographics Criteria / Demographic Results |
| DemographicResults | Demographic Results Document | `DocumentID` | `sTYPE_DOCUMENT` | Global | No | No |  | Demographics Criteria / Demographic Results |
| DemographicResults | Demographic Results Name | `DemographicResultsName` | `sTYPE_TEXT` | Global | No | No |  | Demographics Criteria / Demographic Results |
| DemographicResults | Demographic Results RecID | `DemographicResultsID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Demographics Criteria / Demographic Results |
| DemographicResults | Demographic Results Type | `CodeDemographicResultsTypeID` | `sCODE_DEMOGRAPHIC_RESULTS_TYPE` | Global | Yes | No |  | Demographics Criteria / Demographic Results |
| DemographicResults | Results Status | `CodeResultsStatusID` | `sCODE_RESULTS_STATUS` | Global | Yes | No |  | Demographics Criteria / Demographic Results |
| DemographicResults | Temp Location | `TempLocation` | `sTYPE_TEXT` | Global | No | No |  | Demographics Criteria / Demographic Results |
| DemographicResults | Third Party Vendor | `CodeThirdPartyVendorID` | `sCODE_THIRD_PARTY_VENDOR` | Global | No | No |  | Demographics Criteria / Demographic Results |
| DemographicResults | Time Finished | `TimeFinished` | `sTYPE_TIME` | Global | No | No |  | Demographics Criteria / Demographic Results |
| DemographicResults | Time Initiated | `TimeInitiated` | `sTYPE_TIME` | Global | No | No |  | Demographics Criteria / Demographic Results |
| DemographicReport | Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Demographics Criteria / Audit Info |
| DemographicReport | Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Demographics Criteria / Audit Info |
| DemographicReport | Demographic Report ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Demographics Criteria / Demographics Report |
| DemographicReport | Demographic Report RecID | `DemographicReportID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Demographics Criteria / Demographics Report |
| DemographicReport | Market Area | `CodeMarketAreaID` | `sCODE_MARKET_AREA` | Global | No | No |  | Demographics Criteria / Demographics Report |
| DemographicReport | Market Type | `CodeMarketTypeID` | `sCODE_MARKET_TYPE` | Global | No | No |  | Demographics Criteria / Demographics Report |
| DemographicReport | Name | `DemographicReportName` | `sTYPE_TEXT` | Global | Yes | No |  | Demographics Criteria / Demographics Report |
| DemographicReport | Prototype | `PrototypeID` | `sTYPE_PROTOTYPE` | Global | No | No |  | Demographics Criteria / Demographics Report |
| DemographicReport | Region | `RegionID` | `sTYPE_REGION` | Global | No | No |  | Demographics Criteria / Demographics Report |
| DemographicReport | Trade Area | `TradeArea` | `sTYPE_TEXT` | Global | No | No |  | Demographics Criteria / Demographics Report |
| DemographicFact | Computed Sequence Number | `ComputedSequenceNumber` | `sTYPE_NUMBER` | Global | No | No |  | Demographics Criteria / Demographic Fact |
| DemographicFact | Demographic Fact ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Demographics Criteria / Demographic Fact |
| DemographicFact | Demographic Fact RecID | `DemographicFactID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Demographics Criteria / Demographic Fact |
| DemographicFact | Is Ordered? | `IsOrdered` | `sTYPE_BOOLEAN` | Global | No | No |  | Demographics Criteria / Demographic Fact |
| DemographicFact | Market Demographics | `CodeMarketDemographicsID` | `sCODE_MARKET_DEMOGRAPHICS` | Global | Yes | No |  | Demographics Criteria / Demographic Fact |
| DemographicFact | Order Record Name | `OrderRecordName` | `sTYPE_TEXT` | Global | No | No |  | Demographics Criteria / Demographic Fact |
| DemographicFact | Order Record Type | `OrderRecordType` | `sTYPE_TEXT` | Global | No | No |  | Demographics Criteria / Demographic Fact |
| DemographicFact | Parent ID | `ParentID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Demographics Criteria / Demographic Fact |
| DemographicFact | Previous ID | `PreviousID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Demographics Criteria / Demographic Fact |
| DemographicFact | Weighting | `Weighting` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Demographics Criteria / Demographic Fact |
| Region | Operating Status | `OperatingStatus` | `sTYPE_OPERATING_STATUS` | Global | Yes | No |  | Statics / Hidden |
| Region | Parent Region | `ParentRegionID` | `sTYPE_REGION` | Global | No | No |  | Statics / Hidden |
| Region | Previous Region | `PreviousRegionID` | `sTYPE_REGION` | Global | No | No |  | Statics / Hidden |
| Region | Region Description | `Description` | `sTYPE_TEXT` | Global | No | No |  | Statics / Hidden |
| Region | Region Manager Names | `ManagerIDList` | `sTYPE_MEMBER` | Global | No | No |  | Statics / Hidden |
| Region | Region Member Names | `MemberIDList` | `sTYPE_MEMBER` | Global | No | No |  | Statics / Hidden |
| Region | Region Name | `RegionName` | `sTYPE_TEXT` | Global | Yes | No |  | Statics / Hidden |
| Region | Region Program | `ProgramID` | `sTYPE_PROGRAM` | Global | Yes | No |  | Statics / Hidden |
| DMA | DMA ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Summary Information / DMA |
| DMA | DMA Name | `DMAName` | `sTYPE_TEXT` | Global | Yes | No |  | Summary Information / DMA |
| DMA | DMA Number | `DMANumber` | `sTYPE_NUMBER` | Global | Yes | No |  | Summary Information / DMA |
| DMA | DMA RecID | `DMAID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Summary Information / DMA |
| DMA | Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Summary Information / DMA |
| DMA | Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Summary Information / DMA |
| DMA | Short Name | `ShortName` | `sTYPE_TEXT` | Global | Yes | No |  | Summary Information / DMA |
| DemographicStudyArea | Area Drive Time In Minutes | `AreaDriveTimeInMinutes` | `sTYPE_NUMBER` | Global | No | No |  | Demographics Criteria / Demographic Study Area |
| DemographicStudyArea | Area Radius | `AreaRadius` | `sTYPE_NUMBER` | Global | No | No |  | Demographics Criteria / Demographic Study Area |
| DemographicStudyArea | Demographic Study Area ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Demographics Criteria / Demographic Study Area |
| DemographicStudyArea | Demographic Study Area Name | `DemographicStudyAreaName` | `sTYPE_TEXT` | Global | Yes | No |  | Demographics Criteria / Demographic Study Area |
| DemographicStudyArea | Demographic Study Area RecID | `DemographicStudyAreaID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Demographics Criteria / Demographic Study Area |
| DemographicStudyArea | Radius Unit | `CodeRadiusUnitID` | `sCODE_DISTANCE_UNIT` | Global | No | No |  | Demographics Criteria / Demographic Study Area |
