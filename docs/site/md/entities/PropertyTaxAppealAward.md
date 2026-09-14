# PropertyTaxAppealAward

*18 fields · module: Property Tax · Postgres: `property_tax_appeal_award`*

The financial outcome of a PropertyTaxAppeal — actual/estimated award date and award/award-fee amount. 17 Global fields under Parcel.

Source: `data-fields/property-tax-appeal-award.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 18 |
| Catalogued fields | 17 (17 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 6 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 3 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [FAC-R-014](../rules/FAC-R-014.md) | Input: All six `PropertyTax*` objects (`PropertyTaxAppeal`, `PropertyTaxAppealAward`, `PropertyTaxAssessment`, `PropertyTaxBill`, `PropertyTaxDetail`, `PropertyTaxSummary`) carry a `ParcelID` FK and no `FacilityID`/`ContractID`. Confidence: | Observed |
| [TAX-R-005](../rules/TAX-R-005.md) | Input: `PropertyTaxAppealAward.PropertyTaxAppealID`. Confidence: Observed (`../../data-fields/property-tax-appeal-award.md`). | Observed |
| [TAX-R-011](../rules/TAX-R-011.md) | Input: No FK from `PropertyTaxAppeal` or `PropertyTaxAppealAward` to `PropertyTaxBill` or `PropertyTaxDetail`. Effect: Reconciling a won appeal's computed reduction (`AssessmentReduction`/`TaxReduction`/`NetTaxReduction`) against bills alre | Derived |

## Fields

### Relationships (foreign keys) (4)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ParcelID` | Parcel | Parcel ID | Global | yes | [Parcel](Parcel.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |
| `PropertyTaxAppealID` | Property Tax Appeal | Property Tax Appeal ID | Global | yes | [PropertyTaxAppeal](PropertyTaxAppeal.md) |
| `VendorID` | Vendor | Employer ID | Global |  | [Employer](Employer.md) |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeTaxPaidToID` | Tax Paid To | Dropdown (Tax Paid To Code) | Global |  | Tax Paid To Code |
| `CodeTaxRefundTypeID` | Tax Refund Type | Dropdown (Tax Refund Type Code) | Global |  | Tax Refund Type Code |

### Money (2)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AwardAmount` | Award Amount | Currency | Global |  |  |
| `AwardFeeAmount` | Award Fee Amount | Currency | Global |  |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `PropertyTaxAppealAwardID` | Property Tax Appeal Award RecID | Number | Global |  |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ActualAwardDate` | Actual Award Date | Date | Global |  |  |
| `EstimatedAwardDate` | Estimated Award Date | Date | Global |  |  |

### Text & notes (1)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Notes` |  | Text | Global |  |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Property Tax Appeal Award ClientID | Text | Global | yes |  |
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` | Rev Number | Number | Global |  |  |
