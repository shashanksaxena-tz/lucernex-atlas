# LandPurchaseSummary

*35 fields · module: Facilities, Locations & Sites · Postgres: `land_purchase_summary`*

The land-acquisition deal record for ground purchases — asking price, acreage, and commencement date, anchoring the Purchase Management group alongside Ownership and DevelopmentPlan. 34 Global fields.

Source: `data-fields/land-purchase-summary.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 35 |
| Fields with a vendor definition | 6 of 35 inventoried |
| Physical tables | `land_purchase_summary` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 34 (34 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 2 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 1 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in land_purchase_summary

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 6 fields carry a vendor definition

**Observed.** 6 of this record's 35 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: the captures agree

**Observed.** Over the 34 fields both the Data Fields catalogue and the field inventory contain, the two agree on every one. 1 are marked required.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [FAC-R-018](../rules/FAC-R-018.md) | Input: `Ownership`, `SiteSurvey`, `LandPurchaseSummary`, `LinkLandPurchaseInspection`, `DemographicResults` carry `ProjectEntityID` and no hard-typed FK to `Facility`/`Location`/`Parcel`. Effect: In principle any of these can attach to any  | Derived |

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ProjectEntityID` |  |  | Entity ID | — |  | `land_purchase_summary.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Soft references (10)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `EnvironmentalEngineerID` | Environment Engineer |  | Contact | Global |  | `land_purchase_summary.EnvironmentalEngineerID · TEXT` |  |
| `FinanceAgentID` | Finance Agent |  | Contact | Global |  | `land_purchase_summary.FinanceAgentID · TEXT` |  |
| `OwnerBrokerID` | Purchaser Broker |  | Contact | Global |  | `land_purchase_summary.OwnerBrokerID · TEXT` |  |
| `OwnerID` | Purchaser |  | Contact | Global |  | `land_purchase_summary.OwnerID · TEXT` |  |
| `OwnerLawyerID` | Purchaser Attorney |  | Contact | Global |  | `land_purchase_summary.OwnerLawyerID · TEXT` |  |
| `OwnerSigneeID` | Purchaser Signee |  | Contact | Global |  | `land_purchase_summary.OwnerSigneeID · TEXT` |  |
| `SellerBrokerID` | Selling Broker |  | Contact | Global |  | `land_purchase_summary.SellerBrokerID · TEXT` |  |
| `SellerID` | Seller |  | Contact | Global |  | `land_purchase_summary.SellerID · TEXT` |  |
| `SellerLawyerID` | Seller's Lawyer |  | Contact | Global |  | `land_purchase_summary.SellerLawyerID · TEXT` |  |
| `SellerSigneeID` | Seller Signee |  | Contact | Global |  | `land_purchase_summary.SellerSigneeID · TEXT` |  |

### Money (5)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AskingPrice` | Asking Price |  | Currency | Global |  | `land_purchase_summary.AskingPrice · TEXT` |  |
| `BuyingCommissionAmount` | Purchaser Commission |  | Currency | Global |  | `land_purchase_summary.BuyingCommissionAmount · TEXT` |  |
| `EarnestMoney` | Earnest money |  | Currency | Global |  | `land_purchase_summary.EarnestMoney · TEXT` |  |
| `SalePrice` | Sales Price |  | Currency | Global |  | `land_purchase_summary.SalePrice · TEXT` |  |
| `SellingCommissionAmount` | Seller Commission |  | Currency | Global |  | `land_purchase_summary.SellingCommissionAmount · TEXT` |  |

### Quantities (5)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Acreage` |  |  | 5-Digit Number | Global |  | `land_purchase_summary.Acreage · TEXT` |  |
| `LandPurchaseSummaryID` | Purchase Summary RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `land_purchase_summary.LandPurchaseSummaryID · VARCHAR(64) NOT NULL` |  |
| `SurveyReviewDays` | Survey Review Period |  | Number | Global |  | `land_purchase_summary.SurveyReviewDays · TEXT` |  |
| `TitleReviewDays` | Title Review Period |  | Number | Global |  | `land_purchase_summary.TitleReviewDays · TEXT` |  |
| `WaiverDays` | Waiver Period |  | Number | Global |  | `land_purchase_summary.WaiverDays · TEXT` |  |

### Dates & timestamps (8)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AmendedCommencementDate` | Amended Commencement Date |  | Date | Global |  | `land_purchase_summary.AmendedCommencementDate · TEXT` |  |
| `ClosingDate` | Expected contract signing date |  | Date | Global |  | `land_purchase_summary.ClosingDate · TEXT` |  |
| `CommencementDate` | Commencement Date |  | Date | Global |  | `land_purchase_summary.CommencementDate · TEXT` |  |
| `EarnestMoneyHardDate` | Earnest Money Hard Date |  | Date | Global |  | `land_purchase_summary.EarnestMoneyHardDate · TEXT` |  |
| `EffectiveDate` | Effective Date |  | Date | Global |  | `land_purchase_summary.EffectiveDate · TEXT` |  |
| `FacilityOpenDate` | Expected Store Opening Date |  | Date | Global |  | `land_purchase_summary.FacilityOpenDate · TEXT` |  |
| `SignedPurchaserDate` | Date Purchaser Signed |  | Date | Global |  | `land_purchase_summary.SignedPurchaserDate · TEXT` |  |
| `SignedSellerDate` | Date Seller Signed |  | Date | Global |  | `land_purchase_summary.SignedSellerDate · TEXT` |  |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ContractOptions` | Contract Options |  | Text | Global |  | `land_purchase_summary.ContractOptions · TEXT` |  |
| `Description` | Property Description | Write a description of the record. | Text | Global |  | `land_purchase_summary.Description · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `land_purchase_summary.Notes · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Purchase Summary ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `land_purchase_summary.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `land_purchase_summary.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `land_purchase_summary.ModifiedDate · TEXT` |  |
