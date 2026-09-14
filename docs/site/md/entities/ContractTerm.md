# ContractTerm

*26 fields · module: Contracts & Leases · Postgres: `contract_term`*

One renewal/extension term option on a lease — average rent per area unit and area-unit basis, linked to Amendment and Covenant, appearing under both Contract and Wizard (the guided lease-entry flow). 29 fields (26 Global, 3 Firm).

Source: `data-fields/contract-term.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 26 |
| Fields with a vendor definition | 21 of 26 inventoried |
| Physical tables | `contract_term` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 29 (26 global, 3 firm) |
| Physical tables | 1 |
| Referenced by | 5 keys from 5 record types |
| Points at | 5 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 4 |

## What to know before rebuilding this

### 3 tenant custom columns

**Observed.** This record carries 3 physical Firm_-prefixed columns — tenant custom fields are real columns, not rows in a value store, so adding one is a DDL change. That is direct evidence for database-per-tenant and against a shared schema.

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### 3 catalogued Firm-scope fields

**Observed.** Of 29 catalogued fields on this record, 3 are Firm scope — defined by this tenant rather than shipped by the platform. Firm-scope definitions are RGAF rows carrying IsGlobal, FirmID and IsClientExtensionField.

### Lands in contract_term

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 21 fields carry a vendor definition

**Observed.** 21 of this record's 26 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 1 of this record's fields required; the Data Fields catalogue marks 2; 1 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [ACC-R-016](../rules/ACC-R-016.md) | - `TermLength = ExpireDate − CommenceDate` (the contractual term); - `LikelyTermLength` = length through the last term marked Likely on `Abstract Info > Terms`; - `LastLikelyOptionDate` = end date of the last likely term; - `TestTermLength` | Observed |
| [CON-R-028](../rules/CON-R-028.md) | A contract term option is created: the Terms Wizard generates N ContractTerm rows of a stated length from a stated start. | Observed |
| [CON-R-029](../rules/CON-R-029.md) | Accruing over an option term: only terms flagged IncludeTermForAccruals participate in accrual schedules. | Observed |
| [CON-R-128](../rules/CON-R-128.md) | Accrual scope: only ContractTerm rows flagged IncludeTermForAccruals are accrued. | Observed |

## Fields

### Relationships (foreign keys) (4)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AmendmentID` | Amendment | Select the amendment that the record is associated with from this field. | Contract Amendment ID | Global |  | `contract_term.AmendmentID · TEXT` | [ContractAmendment](ContractAmendment.md) |
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global | yes | `contract_term.ContractID · TEXT` | [Contract](Contract.md) |
| `CovenantID` | Covenant | Select the covenant that the record is associated with from this field. | Covenant ID | Global |  | `contract_term.CovenantID · TEXT` | [Covenant](Covenant.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `contract_term.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (3)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeBuildingAreaUnitID` | Building Area Unit | Select the units you are using to measure your area from this field. This field should pre-populate with the area unit you selected when creating your contract. | Dropdown (Building Area Unit Code) | Global |  | `contract_term.CodeBuildingAreaUnitID · TEXT` | Building Area Unit Code |
| `CodeTermStatusID` | Term Status | Select the term status from this field. Selecting Likely from this field will trigger the Recalc? flag to YES. | Dropdown (Term Status Code) | Global |  | `contract_term.CodeTermStatusID · TEXT` | Term Status Code |
| `CodeTermTypeID` | Term Type | Select the term type from this field. | Dropdown (Term Type Code) | Global |  | `contract_term.CodeTermTypeID · TEXT` | Term Type Code |

### Money (1)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AvgRentPerAreaUnit` | Average Rent Per Area Unit |  | Currency | Global |  | `contract_term.AvgRentPerAreaUnit · TEXT` |  |

### Quantities (4)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ContractTermID` | Term RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `contract_term.ContractTermID · VARCHAR(64) NOT NULL` |  |
| `Firm_OptionRentPSF` | Option Rent PSF |  | Number | Firm |  | `contract_term.Firm_OptionRentPSF · TEXT` |  |
| `LengthOfTerm` | Length | This field is read-only and information-only. It displays the length of the term. | Number | Global |  | `contract_term.LengthOfTerm · TEXT` |  |
| `RentableArea` | Rentable Area | The Rentable Area field must be populated in order for the system to calculate your rate. The system will remember your rentable area and populate this field whenever it is present on a page. If you are not going to use rentable area, do not enter 0. Leave this field blank. | Number | Global |  | `contract_term.RentableArea · TEXT` |  |

### Dates & timestamps (4)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BeginDate` | Coverage Period Begin Date | The Begin Date field allows you to select a begin date for the record. | Date | Global |  | `contract_term.BeginDate · TEXT` |  |
| `EndDate` | Coverage Period End Date | The End Date field allows you to select an end date for the record. | Date | Global |  | `contract_term.EndDate · TEXT` |  |
| `PaymentBeginDate` | Payment Begin Date | The date that payments on a contract begin. The system will not generate payments outside the payment begin / end dates. In order to have payments outside the payment begin / end date, you will have to extend your contract. | Date | Global |  | `contract_term.PaymentBeginDate · TEXT` |  |
| `PaymentEndDate` | Payment End Date | The date that payments on a contract end. The system will not generate payments outside the payment begin / end dates. In order to have payments outside the payment begin / end date, you will have to extend your contract. | Date | Global |  | `contract_term.PaymentEndDate · TEXT` |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `IncludeTermForAccruals` | Include Term For Accruals? | Select the Include in Accruals? check box to flag this term as needing to be included in your accrued expense savings. | Boolean | Global |  | `contract_term.IncludeTermForAccruals · TEXT` |  |

### Text & notes (6)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ClientNumber` | Client Number | The term number. Enter the term number in 2-digit format for example, the first term would be entered as 01. | Text | Global |  | `contract_term.ClientNumber · TEXT` |  |
| `Description` |  | Write a description of the record. | Text | Global |  | `contract_term.Description · TEXT` |  |
| `Firm_TermDocument` | Document |  | Text | Firm |  | `contract_term.Firm_TermDocument · TEXT` |  |
| `Firm_TermPage` | Page |  | Text | Firm |  | `contract_term.Firm_TermPage · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `contract_term.Notes · TEXT` |  |
| `Section` |  | Enter the section of the covenant that pertains to this record in this field. | Text | Global |  | `contract_term.Section · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Term ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `contract_term.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `contract_term.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `contract_term.ModifiedDate · TEXT` |  |

## What points here (5 keys)

| Record type | Via column |
|---|---|
| [Contract](Contract.md) | `NextAvailableTermID` |
| [ExpenseSchedule](ExpenseSchedule.md) | `ContractTermID` |
| [KeyDate](KeyDate.md) | `ContractTermID` |
| [RETransaction](RETransaction.md) | `KickoffContractTermID` |
| [Scenario](Scenario.md) | `ContractTermID` |
