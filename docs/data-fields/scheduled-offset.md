# ScheduledOffset — Data Fields

A pre-scheduled (as opposed to variable) rent offset — cap amount per month/percent and allocation tracking. 18 Global fields under Contract.

**Table Association:** `ScheduledOffset` &nbsp;·&nbsp; **Total fields:** 18 (Global: 18, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Amount Allocated | `AmountAllocated` | `sTYPE_MONEY` | Global | No | No |  | Contract / Scheduled Offsets |
| Amount Not Allocated | `AmountNotAllocated` | `sTYPE_MONEY` | Global | No | No |  | Contract / Scheduled Offsets |
| Begin Date | `BeginDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Scheduled Offsets |
| Cap Amount Per Month | `CapAmountPerMonth` | `sTYPE_MONEY` | Global | No | No |  | Contract / Scheduled Offsets |
| Cap Percent | `CapPercent` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Scheduled Offsets |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | Yes | No |  | Contract / Scheduled Offsets |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Scheduled Offsets |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Scheduled Offsets |
| Currency Type | `CodeCurrencyTypeID` | `sCODE_CURRENCY_TYPE` | Global | No | No |  | Contract / Scheduled Offsets |
| End Date | `EndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Scheduled Offsets |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Scheduled Offsets |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Scheduled Offsets |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Scheduled Offsets |
| Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Scheduled Offsets |
| Scheduled Offset ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Scheduled Offsets |
| Scheduled Offset RecID | `ScheduledOffsetID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Scheduled Offsets |
| Total Amount | `TotalAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Scheduled Offsets |
| Vendor | `VendorID` | `sTYPE_VENDOR` | Global | No | No |  | Contract / Scheduled Offsets |
