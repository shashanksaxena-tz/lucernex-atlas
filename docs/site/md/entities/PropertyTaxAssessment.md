# PropertyTaxAssessment

*25 fields · module: Property Tax · Postgres: `property_tax_assessment`*

The underlying assessed value detail for a Parcel — land, improvements, and adjustment components of the total assessment, feeding PropertyTaxBill and PropertyTaxSummary. 24 Global fields under Parcel.

Source: `data-fields/property-tax-assessment.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 25 |
| Fields with a vendor definition | 24 of 25 inventoried |
| Physical tables | `property_tax_assessment` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 24 (24 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 2 keys from 2 record types |
| Points at | 6 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 2 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in property_tax_assessment

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 24 fields carry a vendor definition

**Observed.** 24 of this record's 25 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one source in the corpus that explains fields rather than listing them.

### 3 fields marked required

**Observed.** The inventory marks 3 of this record's fields Required. Across the whole inventory that is 606 fields, which independently corroborates the 603 the corpus had derived from the Data Fields catalogue — two sources, arrived at separately, agreeing to within three.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [FAC-R-014](../rules/FAC-R-014.md) | Input: All six `PropertyTax*` objects (`PropertyTaxAppeal`, `PropertyTaxAppealAward`, `PropertyTaxAssessment`, `PropertyTaxBill`, `PropertyTaxDetail`, `PropertyTaxSummary`) carry a `ParcelID` FK and no `FacilityID`/`ContractID`. Confidence: | Observed |
| [TAX-R-001](../rules/TAX-R-001.md) | Trigger: Assessment create/save. Input: `PropertyTaxAssessment.PropertyTaxSummaryID`. | Observed |

## Fields

### Relationships (foreign keys) (4)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AppraiserID` | Appraiser | Select the appraiser from this field. | Employer ID | Global |  | `property_tax_assessment.AppraiserID · TEXT` | [Employer](Employer.md) |
| `ParcelID` | Parcel | The Parcel ID of the parcel record that this tax assessment record is associated with. | Parcel ID | Global | yes | `property_tax_assessment.ParcelID · TEXT` | [Parcel](Parcel.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `property_tax_assessment.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |
| `PropertyTaxSummaryID` | Property Tax Summary | The property tax summary ID of the property tax summary record this record is associated with. | Property Tax Summary ID | Global | yes | `property_tax_assessment.PropertyTaxSummaryID · TEXT` | [PropertyTaxSummary](PropertyTaxSummary.md) |

### Money (7)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AppraisalValue` | Appraisal Value | Enter the appraised value of the parcel in this field. | Currency | Global |  | `property_tax_assessment.AppraisalValue · TEXT` |  |
| `AssessmentAmountAdjustments` | Assessment - Adjustments | Enter any adjustments to assessment into this field. | Currency | Global |  | `property_tax_assessment.AssessmentAmountAdjustments · TEXT` |  |
| `AssessmentAmountImprovements` | Assessment - Improvements | Enter the assessed value of any improvements. | Currency | Global |  | `property_tax_assessment.AssessmentAmountImprovements · TEXT` |  |
| `AssessmentAmountLand` | Assessment - Land | Enter the assessed value of the land. | Currency | Global |  | `property_tax_assessment.AssessmentAmountLand · TEXT` |  |
| `AssessmentAmountOther` | Assessment - Other | Enter any other assessment values in this field. | Currency | Global |  | `property_tax_assessment.AssessmentAmountOther · TEXT` |  |
| `AssessmentAmountTotal` | Assessment Amount Total | Enter the assessment total in this field. | Currency | Global |  | `property_tax_assessment.AssessmentAmountTotal · TEXT` |  |
| `MarketValue` | Market Value | Enter the market value of the parcel in this field. | Currency | Global |  | `property_tax_assessment.MarketValue · TEXT` |  |

### Rates & percentages (1)

Percentage inputs and computed rates.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AssessmentPercentage` | Assessment Percentage | Enter the assessment percentage in this field as a percentage value. Typically the assessment percentage is a percentage of the parcel's appraised value usually 80 or 100%. | Percentage | Global |  | `property_tax_assessment.AssessmentPercentage · TEXT` |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `PropertyTaxAssessmentID` | Property Tax Assessment RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `property_tax_assessment.PropertyTaxAssessmentID · VARCHAR(64) NOT NULL` |  |

### Dates & timestamps (3)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AppraisalDate` | Appraisal Date | Enter the date that the parcel was appraised in this field. | Date | Global |  | `property_tax_assessment.AppraisalDate · TEXT` |  |
| `EffectiveDate` | Effective Date | Enter the effective date of the tax assessment in this field. | Date | Global |  | `property_tax_assessment.EffectiveDate · TEXT` |  |
| `EndDate` | End Date | The End Date field allows you to select an end date for the record. | Date | Global |  | `property_tax_assessment.EndDate · TEXT` |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AutoCalcFlag` | Auto Calc? | This field is not implemented. | Boolean | Global |  | `property_tax_assessment.AutoCalcFlag · TEXT` |  |

### Text & notes (2)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Description` |  | Write a description of the record. | Text | Global |  | `property_tax_assessment.Description · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `property_tax_assessment.Notes · TEXT` |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Property Tax Assessment ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `property_tax_assessment.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `property_tax_assessment.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `property_tax_assessment.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `property_tax_assessment.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `property_tax_assessment.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | Global |  | `property_tax_assessment.RevNumber · TEXT` |  |

## What points here (2 keys)

| Record type | Via column |
|---|---|
| [PropertyTaxAppeal](PropertyTaxAppeal.md) | `PropertyTaxAssessmentID` |
| [PropertyTaxBill](PropertyTaxBill.md) | `PropertyTaxAssessmentID` |
