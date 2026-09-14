# PropertyTaxAppeal

*41 fields · module: Property Tax · Postgres: `property_tax_appeal`*

A property-tax assessment appeal filed against a Parcel — filing date, appraisal fee, attorney fee, and the resulting assessment reduction, anchoring a sub-family (PropertyTaxAppealAward) for tracking the appeal's financial outcome. 40 Global fields under Parcel.

Source: `data-fields/property-tax-appeal.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 41 |
| Fields with a vendor definition | 40 of 41 inventoried |
| Physical tables | `property_tax_appeal` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 40 (40 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 1 keys from 1 record types |
| Points at | 5 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 4 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in property_tax_appeal

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 40 fields carry a vendor definition

**Observed.** 40 of this record's 41 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one source in the corpus that explains fields rather than listing them.

### 3 fields marked required

**Observed.** The inventory marks 3 of this record's fields Required. Across the whole inventory that is 606 fields, which independently corroborates the 603 the corpus had derived from the Data Fields catalogue — two sources, arrived at separately, agreeing to within three.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

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

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ParcelID` | Parcel | The parcel ID that this property tax appeal record is associated with. | Parcel ID | Global | yes | `property_tax_appeal.ParcelID · TEXT` | [Parcel](Parcel.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `property_tax_appeal.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |
| `PropertyTaxAssessmentID` | Property Tax Assessment | The tax assessment ID of the tax assessment this appeal is associated with. | Property Tax Assessment ID | Global | yes | `property_tax_appeal.PropertyTaxAssessmentID · TEXT` | [PropertyTaxAssessment](PropertyTaxAssessment.md) |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `TaxAttorneyID` | Tax Attorney | The ID of the tax attorney. | Contact | Global |  | `property_tax_appeal.TaxAttorneyID · TEXT` |  |

### Coded values (drop-downs) (4)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeExpenseGroupID` | Expense Group | The Expense Group field allows you to associate your record with a pre-configured expense group. Expense groups are used to categorize expense types. | Dropdown (Expense Group Code) | Global |  | `property_tax_appeal.CodeExpenseGroupID · TEXT` | Expense Group Code |
| `CodeExpenseTypeID` | Expense Type | The Expense Type field allows you to associate your record with a pre-configured expense type. Expense Types are used to associate records with lease accounting schedules, AP export numbers, expense accrual accounts, percentage rent accrual accounts, and real estate tax accounts. | Dropdown (Expense Type Code) | Global |  | `property_tax_appeal.CodeExpenseTypeID · TEXT` | Expense Type Code |
| `CodeTaxAppealResultID` | Tax Appeal Result | Select the appeal result from this field. | Dropdown (Tax Appeal Result Code) | Global |  | `property_tax_appeal.CodeTaxAppealResultID · TEXT` | Tax Appeal Result Code |
| `CodeTaxAppealStatusID` | Tax Appeal Status | Select the appeal status from this field. | Dropdown (Tax Appeal Status Code) | Global |  | `property_tax_appeal.CodeTaxAppealStatusID · TEXT` | Tax Appeal Status Code |

### Money (20)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AppraisalFee` | Appraisal Fee | Enter the appraiser's fee in this field. | Currency | Global |  | `property_tax_appeal.AppraisalFee · TEXT` |  |
| `AssessmentReduction` | Assessment Reduction | Enter the total reduction of the assessment in this field. | Currency | Global |  | `property_tax_appeal.AssessmentReduction · TEXT` |  |
| `AttorneyFee` | Attorney Fee | Enter the attorney fee in this field. | Currency | Global |  | `property_tax_appeal.AttorneyFee · TEXT` |  |
| `CertifiedAssessment` | Certified Assessment | Enter the certified assessment in this field. | Currency | Global |  | `property_tax_appeal.CertifiedAssessment · TEXT` |  |
| `NetTaxReduction` | Net Tax Reduction | The net tax reduction. | Currency | Global |  | `property_tax_appeal.NetTaxReduction · TEXT` |  |
| `PriorAssessment` | Prior Assessment | This field displays the total of the prior assessment. | Currency | Global |  | `property_tax_appeal.PriorAssessment · TEXT` |  |
| `PriorYearAssessment` | Prior Year Assessment | Enter the prior year's assessment in this field. | Currency | Global |  | `property_tax_appeal.PriorYearAssessment · TEXT` |  |
| `ProposedAssessment` | Proposed Assessment | Enter the proposed assessment in this field. | Currency | Global |  | `property_tax_appeal.ProposedAssessment · TEXT` |  |
| `ReducedAssessment` | Reduced Assessment | The reduced assessment. | Currency | Global |  | `property_tax_appeal.ReducedAssessment · TEXT` |  |
| `RefundFeeAmount` | Refund Fee Amount | Enter any fee refund amounts in this field. | Currency | Global |  | `property_tax_appeal.RefundFeeAmount · TEXT` |  |
| `RenderedAssessment` | Rendered Assessment | Enter the rendered assessment in this field. | Currency | Global |  | `property_tax_appeal.RenderedAssessment · TEXT` |  |
| `RevisedAdjustmentAmount` | Revised Adjustment Amount | This field displays the total revised adjustment amount. | Currency | Global |  | `property_tax_appeal.RevisedAdjustmentAmount · TEXT` |  |
| `RevisedAssessAmtAdjustments` | Revised Assessment - Adjustments | Enter the total of any adjustments in this field. | Currency | Global |  | `property_tax_appeal.RevisedAssessAmtAdjustments · TEXT` |  |
| `RevisedAssessAmtImprovements` | Revised Assessment - Improvements | Enter the revised assessment for improvements in this field. | Currency | Global |  | `property_tax_appeal.RevisedAssessAmtImprovements · TEXT` |  |
| `RevisedAssessmentAmount` | Revised Assessment Amount | This field displays the total revised assessment amount. | Currency | Global |  | `property_tax_appeal.RevisedAssessmentAmount · TEXT` |  |
| `RevisedAssessmentAmountLand` | Revised Assessment - Land | Enter the revised assessment for the land in this field. | Currency | Global |  | `property_tax_appeal.RevisedAssessmentAmountLand · TEXT` |  |
| `RevisedAssessmentAmountOther` | Revised Assessment - Other | Enter other revised assessment amounts in this field. | Currency | Global |  | `property_tax_appeal.RevisedAssessmentAmountOther · TEXT` |  |
| `RevisedTaxAmount` | Revised Tax Amount | Enter your revised tax amount in this field. | Currency | Global |  | `property_tax_appeal.RevisedTaxAmount · TEXT` |  |
| `TaxAttorneyFee` | Tax Attorney Fee | Enter the tax attorney's fee in this field. | Currency | Global |  | `property_tax_appeal.TaxAttorneyFee · TEXT` |  |
| `TaxReduction` | Tax Reduction | The tax reduction. | Currency | Global |  | `property_tax_appeal.TaxReduction · TEXT` |  |

### Quantities (2)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AppealYear` | Appeal Year | Select the appeal year from this field. | Number | Global |  | `property_tax_appeal.AppealYear · TEXT` |  |
| `PropertyTaxAppealID` | Property Tax Appeal RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `property_tax_appeal.PropertyTaxAppealID · VARCHAR(64) NOT NULL` |  |

### Dates & timestamps (4)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AppealFiledDate` | Appeal Filed Date | Enter the date the appeal was filed in this field. | Date | Global |  | `property_tax_appeal.AppealFiledDate · TEXT` |  |
| `EffectiveDate` | Effective Date | Enter the begin date of the appeal period in this field. | Date | Global |  | `property_tax_appeal.EffectiveDate · TEXT` |  |
| `EndDate` | End Date | Enter the end date of the appeal period in this field. | Date | Global |  | `property_tax_appeal.EndDate · TEXT` |  |
| `NewAssessmentDate` | New Assessment Date | The new assessment date. | Date | Global |  | `property_tax_appeal.NewAssessmentDate · TEXT` |  |

### Text & notes (1)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Notes` |  | Add any notes about the record. | Text | Global |  | `property_tax_appeal.Notes · TEXT` |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Property Tax Appeal ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `property_tax_appeal.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `property_tax_appeal.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `property_tax_appeal.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `property_tax_appeal.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `property_tax_appeal.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | Global |  | `property_tax_appeal.RevNumber · TEXT` |  |

## What points here (1 keys)

| Record type | Via column |
|---|---|
| [PropertyTaxAppealAward](PropertyTaxAppealAward.md) | `PropertyTaxAppealID` |
