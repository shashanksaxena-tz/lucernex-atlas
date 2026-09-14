# PropertyTaxBill

*32 fields · module: Property Tax · Postgres: `property_tax_bill`*

A property tax bill issued against a Parcel — discount amount/date/rate for early-payment discounts, feeding into PropertyTaxSummary. 31 Global fields under Parcel.

Source: `data-fields/property-tax-bill.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 32 |
| Fields with a vendor definition | 31 of 32 inventoried |
| Physical tables | `property_tax_bill` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 31 (31 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 3 keys from 3 record types |
| Points at | 5 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 3 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in property_tax_bill

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 31 fields carry a vendor definition

**Observed.** 31 of this record's 32 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one source in the corpus that explains fields rather than listing them.

### 3 fields marked required

**Observed.** The inventory marks 3 of this record's fields Required. Across the whole inventory that is 606 fields, which independently corroborates the 603 the corpus had derived from the Data Fields catalogue — two sources, arrived at separately, agreeing to within three.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [FAC-R-014](../rules/FAC-R-014.md) | Input: All six `PropertyTax*` objects (`PropertyTaxAppeal`, `PropertyTaxAppealAward`, `PropertyTaxAssessment`, `PropertyTaxBill`, `PropertyTaxDetail`, `PropertyTaxSummary`) carry a `ParcelID` FK and no `FacilityID`/`ContractID`. Confidence: | Observed |
| [TAX-R-002](../rules/TAX-R-002.md) | Input: `PropertyTaxBill.PropertyTaxAssessmentID`. Effect: A bill is always issued against a specific assessed value, never against the summary directly. | Observed |
| [TAX-R-011](../rules/TAX-R-011.md) | Input: No FK from `PropertyTaxAppeal` or `PropertyTaxAppealAward` to `PropertyTaxBill` or `PropertyTaxDetail`. Effect: Reconciling a won appeal's computed reduction (`AssessmentReduction`/`TaxReduction`/`NetTaxReduction`) against bills alre | Derived |

## Fields

### Relationships (foreign keys) (3)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ParcelID` | Parcel | The parcel ID of the parcel record that this tax bill is associated with. | Parcel ID | Global | yes | `property_tax_bill.ParcelID · TEXT` | [Parcel](Parcel.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `property_tax_bill.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |
| `PropertyTaxAssessmentID` | Property Tax Assessment | The ID of the property tax assessment record that this tax bill is associated with. | Property Tax Assessment ID | Global | yes | `property_tax_bill.PropertyTaxAssessmentID · TEXT` | [PropertyTaxAssessment](PropertyTaxAssessment.md) |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodePropertyTaxStatusID` | Property Tax Status | Select the tax bill status from this field. | Dropdown (Property Tax Status Code) | Global |  | `property_tax_bill.CodePropertyTaxStatusID · TEXT` | Property Tax Status Code |

### Money (7)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DiscountAmount` | Discount Amount | If there is a discount for paying your tax bill early, enter the amount in this field. | Currency | Global |  | `property_tax_bill.DiscountAmount · TEXT` |  |
| `EqualizationValue` | Equalization Value | Enter the equalization value in this field. The equalization value equals the assessed value multiplied by the equalization factor. | Currency | Global |  | `property_tax_bill.EqualizationValue · TEXT` |  |
| `TaxAdjustmentAmount` | Tax Adjustment Amount | Enter any adjustments to your tax amount in this field. | Currency | Global |  | `property_tax_bill.TaxAdjustmentAmount · TEXT` |  |
| `TaxBalanceDue` | Tax Balance Due | Enter your tax balance due in this field. | Currency | Global |  | `property_tax_bill.TaxBalanceDue · TEXT` |  |
| `TaxNetAmount` | Tax Net Amount | Enter your tax net amount in this field. | Currency | Global |  | `property_tax_bill.TaxNetAmount · TEXT` |  |
| `TaxPriorPaidAmount` | Tax Prior Paid Amount | Enter any previously paid tax amounts in this field. | Currency | Global |  | `property_tax_bill.TaxPriorPaidAmount · TEXT` |  |
| `TaxTotalAmount` | Tax Total Amount | Enter the total tax amount in this field. | Currency | Global |  | `property_tax_bill.TaxTotalAmount · TEXT` |  |

### Rates & percentages (4)

Percentage inputs and computed rates.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DiscountRate` | Discount Rate | If there is a discount for paying your tax bill early, enter the rate in this field. | Percentage | Global |  | `property_tax_bill.DiscountRate · TEXT` |  |
| `EqualizationFactor` | Equalization Factor | Enter the equalization factor in this field. Your equalization factor is established by your tax authority. It is a number that is multiplied against the assessed value of the property to determine the value of the property. | Percentage | Global |  | `property_tax_bill.EqualizationFactor · TEXT` |  |
| `TaxMillRate` | Tax Mill Rate | Enter your tax mill rate in this field. The Tax Mill Rate is also sometimes known as a multiplier. The mill rate is the amount of tax payable per dollar of the assessed value of a property (Investopedia.com). The tax authority multiplies this value against the assessed value of your property to determine your tax bill. | Percentage | Global |  | `property_tax_bill.TaxMillRate · TEXT` |  |
| `TaxRate` | Tax Rate | Enter your tax rate in this field. | Percentage | Global |  | `property_tax_bill.TaxRate · TEXT` |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `PropertyTaxBillID` | Property Tax Bill RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `property_tax_bill.PropertyTaxBillID · VARCHAR(64) NOT NULL` |  |

### Dates & timestamps (5)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DiscountDate` | Discount Date | Enter the date you must pay your bill by in order to receive the discount in this field. | Date | Global |  | `property_tax_bill.DiscountDate · TEXT` |  |
| `EffectiveDate` | Effective Date | Enter the begin date of the tax period in this field. | Date | Global |  | `property_tax_bill.EffectiveDate · TEXT` |  |
| `EndDate` | End Date | The End Date field allows you to select an end date for the record. | Date | Global |  | `property_tax_bill.EndDate · TEXT` |  |
| `InvoiceDate` | Invoice Date | Enter the date of the tax invoice in this field. | Date | Global |  | `property_tax_bill.InvoiceDate · TEXT` |  |
| `PaymentDueDate` | Payment Due Date | Enter the payment due date in this field. | Date | Global |  | `property_tax_bill.PaymentDueDate · TEXT` |  |

### Flags (3)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AutoCalcFlag` | Auto Calc? | This field is not implemented. | Boolean | Global |  | `property_tax_bill.AutoCalcFlag · TEXT` |  |
| `HoldFlag` | Hold? | This flag is informational-only. Select this check box to mark this property tax bill as being on hold. | Boolean | Global |  | `property_tax_bill.HoldFlag · TEXT` |  |
| `ProcessedFlag` | Processed? | This flag is triggered when a tax payment is generated for this tax bill. | Boolean | Global |  | `property_tax_bill.ProcessedFlag · TEXT` |  |

### Text & notes (2)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `InvoiceNumber` | Invoice Number | Enter the invoice number in this field. | Text | Global |  | `property_tax_bill.InvoiceNumber · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `property_tax_bill.Notes · TEXT` |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Property Tax Bill ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `property_tax_bill.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `property_tax_bill.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `property_tax_bill.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `property_tax_bill.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `property_tax_bill.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | Global |  | `property_tax_bill.RevNumber · TEXT` |  |

## What points here (3 keys)

| Record type | Via column |
|---|---|
| [PaymentTransaction](PaymentTransaction.md) | `PropertyTaxBillID` |
| [PaymentTransactionFullImport](PaymentTransactionFullImport.md) | `PropertyTaxBillID` |
| [PropertyTaxDetail](PropertyTaxDetail.md) | `PropertyTaxBillID` |
