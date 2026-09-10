# PaymentReceipt — Data Fields

Money received from a tenant/payer (the inverse of PaymentTransaction) — allocated/unallocated amount and bank account/routing number for the depositing account. 20 Global fields under Contract.

**Table Association:** `PaymentReceipt` &nbsp;·&nbsp; **Total fields:** 20 (Global: 20, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Amount Allocated | `AmountAllocated` | `sTYPE_MONEY` | Global | No | No |  | Contract / Payment Receipt |
| Amount Not Allocated | `AmountNotAllocated` | `sTYPE_MONEY` | Global | No | No |  | Contract / Payment Receipt |
| Bank Account Number | `BankAccountNumber` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Receipt |
| Bank Routing Number | `BankRoutingNumber` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Receipt |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | Yes | No |  | Contract / Payment Receipt |
| Currency Type | `CodeCurrencyTypeID` | `sCODE_CURRENCY_TYPE` | Global | No | No |  | Contract / Payment Receipt |
| Documents | `DocumentIDList` | `sTYPE_DOCUMENT_LIST` | Global | No | No |  | Contract / Payment Receipt |
| Effective Date | `EffectiveDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Payment Receipt |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Payment Receipt |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Payment Receipt |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Payment Receipt |
| Payment Receipt ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Payment Receipt |
| Payment Receipt RecID | `PaymentReceiptID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Payment Receipt |
| Period Month | `PeriodMonth` | `sTYPE_NUMBER` | Global | No | No |  | Contract / Payment Receipt |
| Period Year | `PeriodYear` | `sTYPE_DROPDOWN_YEAR` | Global | No | No |  | Contract / Payment Receipt |
| Posting Date | `PostingDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Payment Receipt |
| Receipt Date | `ReceiptDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Payment Receipt |
| Receipt Number | `ReceiptNumber` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Receipt |
| Receipt Type | `CodeReceiptTypeID` | `sCODE_RECEIPT_TYPE` | Global | No | No |  | Contract / Payment Receipt |
| Received Amount | `ReceivedAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Payment Receipt |
