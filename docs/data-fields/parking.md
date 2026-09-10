# Parking — Data Fields

Parking-facility detail under a Facility record — currency type and description for parking-related costs/revenue. 18 Global fields under Facility.

**Table Association:** `Parking` &nbsp;·&nbsp; **Total fields:** 18 (Global: 18, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Facility / Parking |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Facility / Parking |
| Currency Type | `CodeCurrencyTypeID` | `sCODE_CURRENCY_TYPE` | Global | No | No |  | Facility / Parking |
| Description | `Description` | `sTYPE_TEXT` | Global | No | No |  | Facility / Parking |
| Facility | `FacilityID` | `sTYPE_FACILITY` | Global | Yes | No |  | Facility / Parking |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Facility / Parking |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Facility / Parking |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Facility / Parking |
| Parking ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Facility / Parking |
| Parking Denominator | `CodeParkingDenominatorID` | `sCODE_DENOMINATOR` | Global | No | No |  | Facility / Parking |
| Parking Group | `CodeParkingGroupID` | `sCODE_PARKING_GROUP` | Global | No | No |  | Facility / Parking |
| Parking Location | `ParkingLocation` | `sTYPE_TEXT` | Global | No | No |  | Facility / Parking |
| Parking Number Spaces | `ParkingNumberSpaces` | `sTYPE_NUMBER` | Global | No | No |  | Facility / Parking |
| Parking Rate Per | `ParkingRatePer` | `sTYPE_MONEY` | Global | No | No |  | Facility / Parking |
| Parking RecID | `ParkingID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Facility / Parking |
| Parking Spaces Description | `ParkingSpaceDescr` | `sTYPE_TEXT` | Global | No | No |  | Facility / Parking |
| Parking Type | `CodeParkingTypeID` | `sCODE_PARKING_TYPE` | Global | No | No |  | Facility / Parking |
| Rev Number | `RevNumber` | `sTYPE_NUMBER` | Global | No | No |  | Facility / Parking |
