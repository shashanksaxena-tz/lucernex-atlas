# PropertyTaxAppealAward

*18 fields · module: Property Tax · Postgres: `property_tax_appeal_award`*

The financial outcome of a PropertyTaxAppeal — actual/estimated award date and award/award-fee amount. 17 Global fields under Parcel.

Source: `data-fields/property-tax-appeal-award.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 18 |
| Fields with a vendor definition | 17 of 18 inventoried |
| Physical tables | `property_tax_appeal_award` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 17 (17 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 6 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 3 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in property_tax_appeal_award

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 17 fields carry a vendor definition

**Observed.** 17 of this record's 18 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 3 of this record's fields required; the Data Fields catalogue marks 3; 3 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [FAC-R-014](../rules/FAC-R-014.md) | Input: All six `PropertyTax*` objects (`PropertyTaxAppeal`, `PropertyTaxAppealAward`, `PropertyTaxAssessment`, `PropertyTaxBill`, `PropertyTaxDetail`, `PropertyTaxSummary`) carry a `ParcelID` FK and no `FacilityID`/`ContractID`. Confidence: | Observed |
| [TAX-R-005](../rules/TAX-R-005.md) | Input: `PropertyTaxAppealAward.PropertyTaxAppealID`. Confidence: Observed (`../../data-fields/property-tax-appeal-award.md`). | Observed |
| [TAX-R-011](../rules/TAX-R-011.md) | Input: No FK from `PropertyTaxAppeal` or `PropertyTaxAppealAward` to `PropertyTaxBill` or `PropertyTaxDetail`. Effect: Reconciling a won appeal's computed reduction (`AssessmentReduction`/`TaxReduction`/`NetTaxReduction`) against bills alre | Derived |

## Fields

### Relationships (foreign keys) (4)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ParcelID` | Parcel | The ID of the parcel that this tax appeal award is associated with. | Parcel ID | Global | yes | `property_tax_appeal_award.ParcelID · TEXT` | [Parcel](Parcel.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `property_tax_appeal_award.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |
| `PropertyTaxAppealID` | Property Tax Appeal | The ID of the property tax appeal. | Property Tax Appeal ID | Global | yes | `property_tax_appeal_award.PropertyTaxAppealID · TEXT` | [PropertyTaxAppeal](PropertyTaxAppeal.md) |
| `VendorID` | Vendor | The ID of the vendor associated with the property tax appeal. | Employer ID | Global |  | `property_tax_appeal_award.VendorID · TEXT` | [Employer](Employer.md) |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeTaxPaidToID` | Tax Paid To | An out-of-the-box drop-down menu which can be used to track who the tax was paid to. This field is not on any page layouts by default. | Dropdown (Tax Paid To Code) | Global |  | `property_tax_appeal_award.CodeTaxPaidToID · TEXT` | Tax Paid To Code |
| `CodeTaxRefundTypeID` | Tax Refund Type | An out-of-the-box drop-down menu which can be used to track the type of tax refund. This field is not on any page layouts by default. | Dropdown (Tax Refund Type Code) | Global |  | `property_tax_appeal_award.CodeTaxRefundTypeID · TEXT` | Tax Refund Type Code |

### Money (2)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AwardAmount` | Award Amount | The tax appeal award amount. | Currency | Global |  | `property_tax_appeal_award.AwardAmount · TEXT` |  |
| `AwardFeeAmount` | Award Fee Amount | The fee amount for the tax appeal. | Currency | Global |  | `property_tax_appeal_award.AwardFeeAmount · TEXT` |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `PropertyTaxAppealAwardID` | Property Tax Appeal Award RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `property_tax_appeal_award.PropertyTaxAppealAwardID · VARCHAR(64) NOT NULL` |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActualAwardDate` | Actual Award Date | The date the tax appeal was awarded. | Date | Global |  | `property_tax_appeal_award.ActualAwardDate · TEXT` |  |
| `EstimatedAwardDate` | Estimated Award Date | The estimated award date for the tax appeal. | Date | Global |  | `property_tax_appeal_award.EstimatedAwardDate · TEXT` |  |

### Text & notes (1)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Notes` |  | Add any notes about the record. | Text | Global |  | `property_tax_appeal_award.Notes · TEXT` |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Property Tax Appeal Award ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `property_tax_appeal_award.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `property_tax_appeal_award.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `property_tax_appeal_award.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `property_tax_appeal_award.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `property_tax_appeal_award.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | Global |  | `property_tax_appeal_award.RevNumber · TEXT` |  |
