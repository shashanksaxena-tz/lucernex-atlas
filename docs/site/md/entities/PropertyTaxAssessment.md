# PropertyTaxAssessment

*25 fields · module: Property Tax · Postgres: `property_tax_assessment`*

The underlying assessed value detail for a Parcel — land, improvements, and adjustment components of the total assessment, feeding PropertyTaxBill and PropertyTaxSummary. 24 Global fields under Parcel.

Source: `data-fields/property-tax-assessment.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 25 |
| Catalogued fields | 24 (24 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 2 keys from 2 record types |
| Points at | 6 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 2 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [FAC-R-014](../rules/FAC-R-014.md) | Input: All six `PropertyTax*` objects (`PropertyTaxAppeal`, `PropertyTaxAppealAward`, `PropertyTaxAssessment`, `PropertyTaxBill`, `PropertyTaxDetail`, `PropertyTaxSummary`) carry a `ParcelID` FK and no `FacilityID`/`ContractID`. Confidence: | Observed |
| [TAX-R-001](../rules/TAX-R-001.md) | Trigger: Assessment create/save. Input: `PropertyTaxAssessment.PropertyTaxSummaryID`. | Observed |

## Fields

### Relationships (foreign keys) (4)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AppraiserID` | Appraiser | Employer ID | Global |  | [Employer](Employer.md) |
| `ParcelID` | Parcel | Parcel ID | Global | yes | [Parcel](Parcel.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |
| `PropertyTaxSummaryID` | Property Tax Summary | Property Tax Summary ID | Global | yes | [PropertyTaxSummary](PropertyTaxSummary.md) |

### Money (7)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AppraisalValue` | Appraisal Value | Currency | Global |  |  |
| `AssessmentAmountAdjustments` | Assessment - Adjustments | Currency | Global |  |  |
| `AssessmentAmountImprovements` | Assessment - Improvements | Currency | Global |  |  |
| `AssessmentAmountLand` | Assessment - Land | Currency | Global |  |  |
| `AssessmentAmountOther` | Assessment - Other | Currency | Global |  |  |
| `AssessmentAmountTotal` | Assessment Amount Total | Currency | Global |  |  |
| `MarketValue` | Market Value | Currency | Global |  |  |

### Rates & percentages (1)

Percentage inputs and computed rates.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AssessmentPercentage` | Assessment Percentage | Percentage | Global |  |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `PropertyTaxAssessmentID` | Property Tax Assessment RecID | Number | Global |  |  |

### Dates & timestamps (3)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AppraisalDate` | Appraisal Date | Date | Global |  |  |
| `EffectiveDate` | Effective Date | Date | Global |  |  |
| `EndDate` | End Date | Date | Global |  |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AutoCalcFlag` | Auto Calc? | Boolean | Global |  |  |

### Text & notes (2)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Description` |  | Text | Global |  |  |
| `Notes` |  | Text | Global |  |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Property Tax Assessment ClientID | Text | Global | yes |  |
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` | Rev Number | Number | Global |  |  |

## What points here (2 keys)

| Record type | Via column |
|---|---|
| [PropertyTaxAppeal](PropertyTaxAppeal.md) | `PropertyTaxAssessmentID` |
| [PropertyTaxBill](PropertyTaxBill.md) | `PropertyTaxAssessmentID` |
