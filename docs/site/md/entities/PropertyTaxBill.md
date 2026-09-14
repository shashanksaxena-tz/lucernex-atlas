# PropertyTaxBill

*32 fields · module: Property Tax · Postgres: `property_tax_bill`*

A property tax bill issued against a Parcel — discount amount/date/rate for early-payment discounts, feeding into PropertyTaxSummary. 31 Global fields under Parcel.

Source: `data-fields/property-tax-bill.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 32 |
| Catalogued fields | 31 (31 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 3 keys from 3 record types |
| Points at | 5 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 3 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [FAC-R-014](../rules/FAC-R-014.md) | Input: All six `PropertyTax*` objects (`PropertyTaxAppeal`, `PropertyTaxAppealAward`, `PropertyTaxAssessment`, `PropertyTaxBill`, `PropertyTaxDetail`, `PropertyTaxSummary`) carry a `ParcelID` FK and no `FacilityID`/`ContractID`. Confidence: | Observed |
| [TAX-R-002](../rules/TAX-R-002.md) | Input: `PropertyTaxBill.PropertyTaxAssessmentID`. Effect: A bill is always issued against a specific assessed value, never against the summary directly. | Observed |
| [TAX-R-011](../rules/TAX-R-011.md) | Input: No FK from `PropertyTaxAppeal` or `PropertyTaxAppealAward` to `PropertyTaxBill` or `PropertyTaxDetail`. Effect: Reconciling a won appeal's computed reduction (`AssessmentReduction`/`TaxReduction`/`NetTaxReduction`) against bills alre | Derived |

## Fields

### Relationships (foreign keys) (3)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ParcelID` | Parcel | Parcel ID | Global | yes | [Parcel](Parcel.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |
| `PropertyTaxAssessmentID` | Property Tax Assessment | Property Tax Assessment ID | Global | yes | [PropertyTaxAssessment](PropertyTaxAssessment.md) |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodePropertyTaxStatusID` | Property Tax Status | Dropdown (Property Tax Status Code) | Global |  | Property Tax Status Code |

### Money (7)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DiscountAmount` | Discount Amount | Currency | Global |  |  |
| `EqualizationValue` | Equalization Value | Currency | Global |  |  |
| `TaxAdjustmentAmount` | Tax Adjustment Amount | Currency | Global |  |  |
| `TaxBalanceDue` | Tax Balance Due | Currency | Global |  |  |
| `TaxNetAmount` | Tax Net Amount | Currency | Global |  |  |
| `TaxPriorPaidAmount` | Tax Prior Paid Amount | Currency | Global |  |  |
| `TaxTotalAmount` | Tax Total Amount | Currency | Global |  |  |

### Rates & percentages (4)

Percentage inputs and computed rates.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DiscountRate` | Discount Rate | Percentage | Global |  |  |
| `EqualizationFactor` | Equalization Factor | Percentage | Global |  |  |
| `TaxMillRate` | Tax Mill Rate | Percentage | Global |  |  |
| `TaxRate` | Tax Rate | Percentage | Global |  |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `PropertyTaxBillID` | Property Tax Bill RecID | Number | Global |  |  |

### Dates & timestamps (5)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DiscountDate` | Discount Date | Date | Global |  |  |
| `EffectiveDate` | Effective Date | Date | Global |  |  |
| `EndDate` | End Date | Date | Global |  |  |
| `InvoiceDate` | Invoice Date | Date | Global |  |  |
| `PaymentDueDate` | Payment Due Date | Date | Global |  |  |

### Flags (3)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AutoCalcFlag` | Auto Calc? | Boolean | Global |  |  |
| `HoldFlag` | Hold? | Boolean | Global |  |  |
| `ProcessedFlag` | Processed? | Boolean | Global |  |  |

### Text & notes (2)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `InvoiceNumber` | Invoice Number | Text | Global |  |  |
| `Notes` |  | Text | Global |  |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Property Tax Bill ClientID | Text | Global | yes |  |
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` | Rev Number | Number | Global |  |  |

## What points here (3 keys)

| Record type | Via column |
|---|---|
| [PaymentTransaction](PaymentTransaction.md) | `PropertyTaxBillID` |
| [PaymentTransactionFullImport](PaymentTransactionFullImport.md) | `PropertyTaxBillID` |
| [PropertyTaxDetail](PropertyTaxDetail.md) | `PropertyTaxBillID` |
