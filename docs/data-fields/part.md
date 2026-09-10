# Part — Data Fields

An equipment/maintenance parts-catalog record — cost, manufacturer, and model number, supporting the Equipment/Assets maintenance workflow. 16 Global fields under Company Items.

**Table Association:** `Part` &nbsp;·&nbsp; **Total fields:** 16 (Global: 16, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Cost | `Cost` | `sTYPE_MONEY` | Global | No | No |  | Company Items / Parts |
| Maintenance Categories | `CodeAssetCategoryIDList` | `sCODE_ASSET_CATEGORY` | Global | No | No |  | Company Items / Parts |
| Manufacturer | `Manufacturer` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Parts |
| Model Number | `ModelNumber` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Parts |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Parts |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Company Items / Parts |
| Order To Level | `OrderToLevel` | `sTYPE_NUMBER` | Global | No | No |  | Company Items / Parts |
| Par Level | `ParLevel` | `sTYPE_NUMBER` | Global | No | No |  | Company Items / Parts |
| Part ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / Parts |
| Part Name | `PartName` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / Parts |
| Part Photo | `PartPhoto` | `sTYPE_PHOTO` | Global | No | No |  | Company Items / Parts |
| Part RecID | `PartID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Parts |
| Quantity On Hand | `QuantityOnHand` | `sTYPE_NUMBER` | Global | No | No |  | Company Items / Parts |
| Quantity On Order | `QuantityOnOrder` | `sTYPE_NUMBER` | Global | No | No |  | Company Items / Parts |
| Vendor ID | `VendorID` | `sTYPE_VENDOR` | Global | No | No |  | Company Items / Parts |
| Warranty Period In Days | `WarrantyPeriodInDays` | `sTYPE_NUMBER` | Global | No | No |  | Company Items / Parts |
