# PropertyTaxAppeal

*41 fields · module: Property Tax · Postgres: `property_tax_appeal`*

A property-tax assessment appeal filed against a Parcel — filing date, appraisal fee, attorney fee, and the resulting assessment reduction, anchoring a sub-family (PropertyTaxAppealAward) for tracking the appeal's financial outcome. 40 Global fields under Parcel.

Source: `data-fields/property-tax-appeal.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 41 |
| Catalogued fields | 40 (40 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 1 keys from 1 record types |
| Points at | 5 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 4 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [FAC-R-014](../rules/FAC-R-014.md) | Input: All six `PropertyTax*` objects (`PropertyTaxAppeal`, `PropertyTaxAppealAward`, `PropertyTaxAssessment`, `PropertyTaxBill`, `PropertyTaxDetail`, `PropertyTaxSummary`) carry a `ParcelID` FK and no `FacilityID`/`ContractID`. Confidence: | Observed |
| [TAX-R-004](../rules/TAX-R-004.md) | Input: `PropertyTaxAppeal.PropertyTaxAssessmentID`. Effect: An appeal always contests one specific dated assessed value, never the ongoing Summary as a whole. | Observed |
| [TAX-R-008](../rules/TAX-R-008.md) | Input: `PropertyTaxSummary.CodeExpenseGroupID`/`.CodeExpenseTypeID`, `PropertyTaxAppeal.CodeExpenseGroupID`/`.CodeExpenseTypeID`. Effect: Selecting an expense type/group on a property-tax record is a GL-routing decision, identical in mechan | Observed |
| [TAX-R-011](../rules/TAX-R-011.md) | Input: No FK from `PropertyTaxAppeal` or `PropertyTaxAppealAward` to `PropertyTaxBill` or `PropertyTaxDetail`. Effect: Reconciling a won appeal's computed reduction (`AssessmentReduction`/`TaxReduction`/`NetTaxReduction`) against bills alre | Derived |

## Fields

### Relationships (foreign keys) (3)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ParcelID` | Parcel | Parcel ID | Global | yes | [Parcel](Parcel.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |
| `PropertyTaxAssessmentID` | Property Tax Assessment | Property Tax Assessment ID | Global | yes | [PropertyTaxAssessment](PropertyTaxAssessment.md) |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `TaxAttorneyID` | Tax Attorney | Contact | Global |  |  |

### Coded values (drop-downs) (4)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeExpenseGroupID` | Expense Group | Dropdown (Expense Group Code) | Global |  | Expense Group Code |
| `CodeExpenseTypeID` | Expense Type | Dropdown (Expense Type Code) | Global |  | Expense Type Code |
| `CodeTaxAppealResultID` | Tax Appeal Result | Dropdown (Tax Appeal Result Code) | Global |  | Tax Appeal Result Code |
| `CodeTaxAppealStatusID` | Tax Appeal Status | Dropdown (Tax Appeal Status Code) | Global |  | Tax Appeal Status Code |

### Money (20)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AppraisalFee` | Appraisal Fee | Currency | Global |  |  |
| `AssessmentReduction` | Assessment Reduction | Currency | Global |  |  |
| `AttorneyFee` | Attorney Fee | Currency | Global |  |  |
| `CertifiedAssessment` | Certified Assessment | Currency | Global |  |  |
| `NetTaxReduction` | Net Tax Reduction | Currency | Global |  |  |
| `PriorAssessment` | Prior Assessment | Currency | Global |  |  |
| `PriorYearAssessment` | Prior Year Assessment | Currency | Global |  |  |
| `ProposedAssessment` | Proposed Assessment | Currency | Global |  |  |
| `ReducedAssessment` | Reduced Assessment | Currency | Global |  |  |
| `RefundFeeAmount` | Refund Fee Amount | Currency | Global |  |  |
| `RenderedAssessment` | Rendered Assessment | Currency | Global |  |  |
| `RevisedAdjustmentAmount` | Revised Adjustment Amount | Currency | Global |  |  |
| `RevisedAssessAmtAdjustments` | Revised Assessment - Adjustments | Currency | Global |  |  |
| `RevisedAssessAmtImprovements` | Revised Assessment - Improvements | Currency | Global |  |  |
| `RevisedAssessmentAmount` | Revised Assessment Amount | Currency | Global |  |  |
| `RevisedAssessmentAmountLand` | Revised Assessment - Land | Currency | Global |  |  |
| `RevisedAssessmentAmountOther` | Revised Assessment - Other | Currency | Global |  |  |
| `RevisedTaxAmount` | Revised Tax Amount | Currency | Global |  |  |
| `TaxAttorneyFee` | Tax Attorney Fee | Currency | Global |  |  |
| `TaxReduction` | Tax Reduction | Currency | Global |  |  |

### Quantities (2)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AppealYear` | Appeal Year | Number | Global |  |  |
| `PropertyTaxAppealID` | Property Tax Appeal RecID | Number | Global |  |  |

### Dates & timestamps (4)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AppealFiledDate` | Appeal Filed Date | Date | Global |  |  |
| `EffectiveDate` | Effective Date | Date | Global |  |  |
| `EndDate` | End Date | Date | Global |  |  |
| `NewAssessmentDate` | New Assessment Date | Date | Global |  |  |

### Text & notes (1)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Notes` |  | Text | Global |  |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Property Tax Appeal ClientID | Text | Global | yes |  |
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` | Rev Number | Number | Global |  |  |

## What points here (1 keys)

| Record type | Via column |
|---|---|
| [PropertyTaxAppealAward](PropertyTaxAppealAward.md) | `PropertyTaxAppealID` |
