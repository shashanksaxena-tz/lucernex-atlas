# Space — Data Fields

A leasable space/suite record within a Facility — area unit and Contract linkage, more granular than Facility itself for multi-tenant buildings. 26 Global fields under Facility.

**Table Association:** `Space` &nbsp;·&nbsp; **Total fields:** 26 (Global: 26, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Building Area Unit | `CodeBuildingAreaUnitID` | `sCODE_BUILDING_AREA_UNIT` | Global | No | No |  | Facility / Space |
| Client Number | `ClientNumber` | `sTYPE_TEXT` | Global | No | No |  | Facility / Space |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | No | No |  | Facility / Space |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Facility / Space |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Facility / Space |
| Description | `Description` | `sTYPE_TEXT` | Global | No | No |  | Facility / Space |
| Effective Date | `EffectiveDate` | `sTYPE_DATE` | Global | No | No |  | Facility / Space |
| Facility | `FacilityID` | `sTYPE_FACILITY` | Global | Yes | No |  | Facility / Space |
| Floor Number | `FloorNumber` | `sTYPE_TEXT` | Global | No | No |  | Facility / Space |
| Gross Area | `GrossArea` | `sTYPE_AREA` | Global | No | No |  | Facility / Space |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Facility / Space |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Facility / Space |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Facility / Space |
| Rentable Area | `RentableArea` | `sTYPE_AREA` | Global | No | No |  | Facility / Space |
| Rev Number | `RevNumber` | `sTYPE_NUMBER` | Global | No | No |  | Facility / Space |
| Room Number | `RoomNumber` | `sTYPE_TEXT` | Global | No | No |  | Facility / Space |
| Space ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Facility / Space |
| Space Group | `CodeSpaceGroupID` | `sCODE_SPACE_GROUP` | Global | No | No |  | Facility / Space |
| Space Name | `SpaceName` | `sTYPE_TEXT` | Global | Yes | No |  | Facility / Space |
| Space RecID | `SpaceID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Facility / Space |
| Space Status | `CodeSpaceStatusID` | `sCODE_SPACE_STATUS` | Global | No | No |  | Facility / Space |
| Space Type | `CodeSpaceTypeID` | `sCODE_SPACE_TYPE` | Global | No | No |  | Facility / Space |
| Space Use | `CodeSpaceUseID` | `sCODE_SPACE_USE` | Global | No | No |  | Facility / Space |
| Suite Number | `SuiteNumber` | `sTYPE_TEXT` | Global | No | No |  | Facility / Space |
| Total Head Count | `TotalHeadCount` | `sTYPE_NUMBER` | Global | No | No |  | Facility / Space |
| Usable Area | `UsableArea` | `sTYPE_AREA` | Global | No | No |  | Facility / Space |
