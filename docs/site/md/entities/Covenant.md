# Covenant

*44 fields · module: Contracts & Leases · Postgres: `covenant`*

A lease covenant/compliance obligation (financial ratio tests, use restrictions, exclusivity clauses) tied to a Contract — covenant amount/area, category, and an associated document reference for the underlying clause. 45 fields (38 Global, 7 Firm) spanning Contract and Wizard groups, and one of the entities the user named as expected — the Firm extension here likely reflects tenant-specific covenant categories not in the base platform list.

Source: `data-fields/covenant.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 44 |
| Fields with a vendor definition | 35 of 56 inventoried |
| Physical tables | `covenant` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 45 (38 global, 7 firm) |
| Physical tables | 1 |
| Referenced by | 15 keys from 15 record types |
| Points at | 6 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 4 |

## What to know before rebuilding this

### 7 tenant custom columns

**Observed.** This record carries 7 physical Firm_-prefixed columns — tenant custom fields are real columns, not rows in a value store, so adding one is a DDL change. That is direct evidence for database-per-tenant and against a shared schema.

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### 7 catalogued Firm-scope fields

**Observed.** Of 45 catalogued fields on this record, 7 are Firm scope — defined by this tenant rather than shipped by the platform. Firm-scope definitions are RGAF rows carrying IsGlobal, FirmID and IsClientExtensionField.

### Lands in covenant

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 35 fields carry a vendor definition

**Observed.** 35 of this record's 56 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: 1 disagree of 43 comparable

**Observed.** Over the 43 fields both captures contain, they agree on 42. The exceptions are ContractID. Estate-wide there are 43 such fields and every one runs the same way — catalogue-required, inventory-not — and they are 34 ContractID, 8 ProjectEntityID and 1 ShortName: the owner foreign key. Parenthood is enforced by the application, not by the database.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [ACC-R-019](../rules/ACC-R-019.md) | the covenant amount is pulled into the accounting assumptions and the accounting schedule only if `CodeAccountingAdjustmentTypeID` ∈ {`Purchase Option`, `Cancellation Option`, `Residual Value Guarantee`} | Observed |
| [ACC-R-020](../rules/ACC-R-020.md) | `SLSummary.NeedsRecalculation := true` | Observed |
| [ACC-R-026](../rules/ACC-R-026.md) | the stated percentage of the amount is allocated to a secondary schedule; the remainder to the primary | Observed |
| [CON-R-129](../rules/CON-R-129.md) | Liability scope: Covenant.HoldAmountInSchedLiability excludes a covenant amount from the ASC 842 scheduled liability. | Observed |

## Fields

### Relationships (foreign keys) (5)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AmendmentID` | Amendment | Select the amendment that the record is associated with from this field. The Amendment field is not relevant when you initially create your contract. However, if you are adding covenants to your contract and you want to associate a covenant with an amendment, you would select the amendment from this field. | Contract Amendment ID | Global |  | `covenant.AmendmentID · TEXT` | [ContractAmendment](ContractAmendment.md) |
| `AssociatedDocumentID` | Associated Document | The ID of a document associated with this record. | Document ID | Global |  | `covenant.AssociatedDocumentID · TEXT` | [Document](Document.md) |
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global | yes | `covenant.ContractID · TEXT` | [Contract](Contract.md) |
| `FolderID` | Folder | The folder ID of the document connected to the covenant. | Folder ID | Global |  | `covenant.FolderID · TEXT` | [Folder](Folder.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `covenant.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DocumentIDList` | Documents | This is a generic field that allows you to add documents a record. | Document List | Global |  | `covenant.DocumentIDList · TEXT` |  |

### Coded values (drop-downs) (12)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeASC842ScheduleID` | ASC 842 Schedule | The ASC 842 Schedule field is where you select the ASC 842 schedule you want to associate with a record. This field is functional, and changing its value on the Accounting Assumptions page, the Covenants page, or the Recurring Expenses page will set the Recalc? flag to YES. | Dropdown (ASC 842 Schedule Type) | Global |  | `covenant.CodeASC842ScheduleID · TEXT` | ASC 842 Schedule Type |
| `CodeAccountingAdjustmentTypeID` | Accounting Adjustment Type | If this covenant is related to an accounting adjustment such as a purchase option, cancellation, or residual value guarantee select the appropriate accounting adjustment type from this field. | Dropdown (Accounting Adjustment Type Code) | Global |  | `covenant.CodeAccountingAdjustmentTypeID · TEXT` | Accounting Adjustment Type Code |
| `CodeBuildingAreaUnitID` | Building Area Unit | Select the units you are using to measure your area from this field. This field should pre-populate with the area unit you selected when creating your contract. | Dropdown (Building Area Unit Code) | Global |  | `covenant.CodeBuildingAreaUnitID · TEXT` | Building Area Unit Code |
| `CodeCovenantCategoryID` | Covenant Category | The covenant category is the third level of categorization for covenants. Categories are the children of types, and the grandchildren of groups. The category is typically used to indicate whether this is part of the original agreement or an amendment. | Dropdown (Covenant Category Code) | Global |  | `covenant.CodeCovenantCategoryID · TEXT` | Covenant Category Code |
| `CodeCovenantGroupID` | Covenant Group | The covenant group is the first level of categorization for covenants. Groups are the parents of types, and the grandparents of categories. It is our best practice recommendation to always specify the Group and Type of a covenant to simplify reporting. | Dropdown (Covenant Group Code) | Global |  | `covenant.CodeCovenantGroupID · TEXT` | Covenant Group Code |
| `CodeCovenantStatusID` | Covenant Status | Select the status of the covenant from this field. Example statuses include "Active" or "Expired". | Dropdown (Covenant Status Code) | Global |  | `covenant.CodeCovenantStatusID · TEXT` | Covenant Status Code |
| `CodeCovenantTemplateID` | Covenant Template | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Dropdown (Covenant Template Code) | Global |  | `covenant.CodeCovenantTemplateID · TEXT` | Covenant Template Code |
| `CodeCovenantTypeID` | Covenant Type | The covenant type is the second level of categorization for covenants. Types are the children of groups, and the parents of categories. It is our best practice recommendation to always specify the Group and Type of a covenant to simplify reporting. | Dropdown (Covenant Type Code) | Global |  | `covenant.CodeCovenantTypeID · TEXT` | Covenant Type Code |
| `CodeCurrencyTypeID` | Currency Type | The Currency Type field allows you to select a currency type to be used on a record. | Dropdown (Currency Type Code) | Global |  | `covenant.CodeCurrencyTypeID · TEXT` | Currency Type Code |
| `CodeIFRS16ScheduleID` | IFRS 16 Schedule | The IFRS 16 Schedule field is where you select the IFRS 16 schedule you want to associate with a record. This field is functional, and changing its value on the Accounting Assumptions page, the Covenants page, or the Recurring Expenses page will set the Recalc? flag to YES. | Dropdown (IFRS 16 Schedule Type) | Global |  | `covenant.CodeIFRS16ScheduleID · TEXT` | IFRS 16 Schedule Type |
| `Firm_RadiusUnit` | Radius Unit |  | Dropdown (Custom Field) | Firm |  | `covenant.Firm_RadiusUnit · TEXT` | Custom Field |
| `Firm_TerminationRight` | Termination Right |  | Dropdown (Custom Field) | Firm |  | `covenant.Firm_TerminationRight · TEXT` | Custom Field |

### Money (5)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CovenantAmount` | Covenant Amount | If there is a financial amount associated with this covenant, enter the amount in this field. This amount will be pulled into your accounting assumptions and accounting schedule if the covenant has one of three accounting adjustment types: Purchase Option, Cancellation Option, or Residual Value guarantee. | Currency | Global |  | `covenant.CovenantAmount · TEXT` |  |
| `Firm_BuyoutAmount` | Buyout Amount |  | Currency | Firm |  | `covenant.Firm_BuyoutAmount · TEXT` |  |
| `Firm_SalesThreshold` | Sales Threshold |  | Currency | Firm |  | `covenant.Firm_SalesThreshold · TEXT` |  |
| `ThirdPartyRVGAmount` | Portion Guaranteed By 3rd Party | The total value of the residual value guarantee, positive or negative. This field only appears if a Covenant Type of Residual Value Guarantee is created. | Currency | Global |  | `covenant.ThirdPartyRVGAmount · TEXT` |  |
| `TotalRVGAmount` | Total Residual Value Guarantee | The residual value guarantee amount which is guaranteed by a third party, positive or negative. This field only appears if a Covenant Type of Residual Value Guarantee is created. | Currency | Global |  | `covenant.TotalRVGAmount · TEXT` |  |

### Rates & percentages (1)

Percentage inputs and computed rates.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `SecondaryRentSchedAllocPercent` | Covenant Secondary Rent Schedule Allocation Percent | If you will be allocating a percentage of a covenant expense to a secondary schedule, enter the allocation percentage in this field. | Percentage | Global |  | `covenant.SecondaryRentSchedAllocPercent · TEXT` |  |

### Quantities (3)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CovenantArea` | Covenant Area | Enter the rentable area in this field. This field can be used to enter the rentable area of the contract or the total rentable area of the property. | Number | Global |  | `covenant.CovenantArea · TEXT` |  |
| `CovenantID` | Covenant RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `covenant.CovenantID · VARCHAR(64) NOT NULL` |  |
| `Firm_RadiusAmount` | Radius Amount |  | Number | Firm |  | `covenant.Firm_RadiusAmount · TEXT` |  |

### Dates & timestamps (1)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CovenantDate` | Covenant Date | Enter the effective date of the covenant in this field. | Date | Global |  | `covenant.CovenantDate · TEXT` |  |

### Flags (3)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ExistsFlag` | Exists? | Select this check box to indicate that the covenant currently exists in the lease. A common use case for this check box is for customers who implement standard covenants for their contracts. However, these customers may have existing leases that do not have some of these standard covenants. These standard covenants could be applied to their contracts on a global level at implementation, but the customer could indicate that the covenant does not currently exist on a specific contract by clearing the Covenant Exists? check box. Then, when it is time for the customer to renegotiate the contract, they can quickly and easily see which covenants should be negotiated in the new contract. | Boolean | Global |  | `covenant.ExistsFlag · TEXT` |  |
| `HoldAmountInSchedLiability` | Hold Amount in Rent Schedule Liability |  | Boolean | Global |  | `covenant.HoldAmountInSchedLiability · TEXT` |  |
| `StandardLanguageFlag` | Standard Language? | Select this check box if the language of the covenant is standard for all of your leases. | Boolean | Global |  | `covenant.StandardLanguageFlag · TEXT` |  |

### Text & notes (10)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BaseName` | File Name | This field displays the file name of the file attached to the record. | Text | Global |  | `covenant.BaseName · TEXT` |  |
| `CovenantGroupTypeName` | Covenant Group/Type Name | This field returns "Group Type : Group Name" for the Covenant. | Text | Global |  | `covenant.CovenantGroupTypeName · TEXT` |  |
| `Firm_CovenantDocument` | Document |  | Text | Firm |  | `covenant.Firm_CovenantDocument · TEXT` |  |
| `Firm_Penalty` | Penalty |  | Text | Firm |  | `covenant.Firm_Penalty · TEXT` |  |
| `LineNumber` | Line Number | Enter the line number where the covenant appears in the document attached to the covenant record in this field. | Text | Global |  | `covenant.LineNumber · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `covenant.Notes · TEXT` |  |
| `PageNumber` | Page Number | Enter the page number where the covenant appears in the document attached to the covenant record in this field. | Text | Global |  | `covenant.PageNumber · TEXT` |  |
| `ParagraphNumber` | Paragraph Number | Enter the paragraph number where the covenant appears in the document attached to the covenant record in this field. | Text | Global |  | `covenant.ParagraphNumber · TEXT` |  |
| `SectionNumber` | Section Number | Enter the section of the lease document that this covenant is from in this field. | Text | Global |  | `covenant.SectionNumber · TEXT` |  |
| `StandardLanguageVersion` | Standard Language Version | Enter the form or version number of the covenant in this field. | Text | Global |  | `covenant.StandardLanguageVersion · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Covenant ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `covenant.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `covenant.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `covenant.ModifiedDate · TEXT` |  |

## What points here (15 keys)

| Record type | Via column |
|---|---|
| [Allowance](Allowance.md) | `CovenantID` |
| [CoTenancy](CoTenancy.md) | `CovenantID` |
| [ContractTerm](ContractTerm.md) | `CovenantID` |
| [ExpenseAccrualSetup](ExpenseAccrualSetup.md) | `CovenantID` |
| [ExpenseRecovery](ExpenseRecovery.md) | `CovenantID` |
| [ExpenseSetup](ExpenseSetup.md) | `CovenantID` |
| [FinancialAdjustment](FinancialAdjustment.md) | `CovenantID` |
| [Insurance](Insurance.md) | `CovenantID` |
| [KeyDate](KeyDate.md) | `CovenantID` |
| [PercentageRent](PercentageRent.md) | `CovenantID` |
| [RETransaction](RETransaction.md) | `KickoffCovenantID` |
| [Responsibility](Responsibility.md) | `CovenantID` |
| [Scenario](Scenario.md) | `CovenantID` |
| [SecurityDeposit](SecurityDeposit.md) | `CovenantID` |
| [UseBasedRent](UseBasedRent.md) | `CovenantID` |
