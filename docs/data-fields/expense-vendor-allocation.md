# ExpenseVendorAllocation — Data Fields

Allocation of a recoverable expense to a specific paying vendor — AP vendor number and begin/end date. 15 Global fields under Contract.

**Table Association:** `ExpenseVendorAllocation` &nbsp;·&nbsp; **Total fields:** 15 (Global: 15, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| AP Vendor Number | `APVendorNumber` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Vendor Allocation |
| Begin Date | `BeginDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Expense Vendor Allocation |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | Yes | No |  | Contract / Expense Vendor Allocation |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Expense Vendor Allocation |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Expense Vendor Allocation |
| End Date | `EndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Expense Vendor Allocation |
| Expense Setup | `ExpenseSetupID` | `sTYPE_EXPENSE_SETUP` | Global | Yes | No |  | Contract / Expense Vendor Allocation |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Expense Vendor Allocation |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Expense Vendor Allocation |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Expense Vendor Allocation |
| Payment Percentage | `PaymentPercentage` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Expense Vendor Allocation |
| Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Expense Vendor Allocation |
| Vendor | `VendorID` | `sTYPE_VENDOR` | Global | Yes | No |  | Contract / Expense Vendor Allocation |
| Vendor Allocation ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Expense Vendor Allocation |
| Vendor Allocation RecID | `ExpenseVendorAllocationID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Expense Vendor Allocation |
