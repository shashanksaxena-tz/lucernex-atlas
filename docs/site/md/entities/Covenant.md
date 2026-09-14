# Covenant

*44 fields · module: Contracts & Leases · Postgres: `covenant`*

A lease covenant/compliance obligation (financial ratio tests, use restrictions, exclusivity clauses) tied to a Contract — covenant amount/area, category, and an associated document reference for the underlying clause. 45 fields (38 Global, 7 Firm) spanning Contract and Wizard groups, and one of the entities the user named as expected — the Firm extension here likely reflects tenant-specific covenant categories not in the base platform list.

Source: `data-fields/covenant.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 44 |
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

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AmendmentID` | Amendment | Contract Amendment ID | Global |  | [ContractAmendment](ContractAmendment.md) |
| `AssociatedDocumentID` | Associated Document | Document ID | Global |  | [Document](Document.md) |
| `ContractID` | Contract | Contract ID | Global | yes | [Contract](Contract.md) |
| `FolderID` | Folder | Folder ID | Global |  | [Folder](Folder.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DocumentIDList` | Documents | Document List | Global |  |  |

### Coded values (drop-downs) (12)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeASC842ScheduleID` | ASC 842 Schedule | Dropdown (ASC 842 Schedule Type) | Global |  | ASC 842 Schedule Type |
| `CodeAccountingAdjustmentTypeID` | Accounting Adjustment Type | Dropdown (Accounting Adjustment Type Code) | Global |  | Accounting Adjustment Type Code |
| `CodeBuildingAreaUnitID` | Building Area Unit | Dropdown (Building Area Unit Code) | Global |  | Building Area Unit Code |
| `CodeCovenantCategoryID` | Covenant Category | Dropdown (Covenant Category Code) | Global |  | Covenant Category Code |
| `CodeCovenantGroupID` | Covenant Group | Dropdown (Covenant Group Code) | Global |  | Covenant Group Code |
| `CodeCovenantStatusID` | Covenant Status | Dropdown (Covenant Status Code) | Global |  | Covenant Status Code |
| `CodeCovenantTemplateID` | Covenant Template | Dropdown (Covenant Template Code) | Global |  | Covenant Template Code |
| `CodeCovenantTypeID` | Covenant Type | Dropdown (Covenant Type Code) | Global |  | Covenant Type Code |
| `CodeCurrencyTypeID` | Currency Type | Dropdown (Currency Type Code) | Global |  | Currency Type Code |
| `CodeIFRS16ScheduleID` | IFRS 16 Schedule | Dropdown (IFRS 16 Schedule Type) | Global |  | IFRS 16 Schedule Type |
| `Firm_RadiusUnit` | Radius Unit | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_TerminationRight` | Termination Right | Dropdown (Custom Field) | Firm |  | Custom Field |

### Money (5)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CovenantAmount` | Covenant Amount | Currency | Global |  |  |
| `Firm_BuyoutAmount` | Buyout Amount | Currency | Firm |  |  |
| `Firm_SalesThreshold` | Sales Threshold | Currency | Firm |  |  |
| `ThirdPartyRVGAmount` | Portion Guaranteed By 3rd Party | Currency | Global |  |  |
| `TotalRVGAmount` | Total Residual Value Guarantee | Currency | Global |  |  |

### Rates & percentages (1)

Percentage inputs and computed rates.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `SecondaryRentSchedAllocPercent` | Covenant Secondary Rent Schedule Allocation Percent | Percentage | Global |  |  |

### Quantities (3)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CovenantArea` | Covenant Area | Number | Global |  |  |
| `CovenantID` | Covenant RecID | Number | Global |  |  |
| `Firm_RadiusAmount` | Radius Amount | Number | Firm |  |  |

### Dates & timestamps (1)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CovenantDate` | Covenant Date | Date | Global |  |  |

### Flags (3)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ExistsFlag` | Exists? | Boolean | Global |  |  |
| `HoldAmountInSchedLiability` | Hold Amount in Rent Schedule Liability | Boolean | Global |  |  |
| `StandardLanguageFlag` | Standard Language? | Boolean | Global |  |  |

### Text & notes (10)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BaseName` | File Name | Text | Global |  |  |
| `CovenantGroupTypeName` | Covenant Group/Type Name | Text | Global |  |  |
| `Firm_CovenantDocument` | Document | Text | Firm |  |  |
| `Firm_Penalty` | Penalty | Text | Firm |  |  |
| `LineNumber` | Line Number | Text | Global |  |  |
| `Notes` |  | Text | Global |  |  |
| `PageNumber` | Page Number | Text | Global |  |  |
| `ParagraphNumber` | Paragraph Number | Text | Global |  |  |
| `SectionNumber` | Section Number | Text | Global |  |  |
| `StandardLanguageVersion` | Standard Language Version | Text | Global |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Covenant ClientID | Text | Global | yes |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |

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
