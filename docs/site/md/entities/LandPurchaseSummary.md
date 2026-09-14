# LandPurchaseSummary

*35 fields · module: Facilities, Locations & Sites · Postgres: `land_purchase_summary`*

The land-acquisition deal record for ground purchases — asking price, acreage, and commencement date, anchoring the Purchase Management group alongside Ownership and DevelopmentPlan. 34 Global fields.

Source: `data-fields/land-purchase-summary.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 35 |
| Catalogued fields | 34 (34 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 2 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 1 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [FAC-R-018](../rules/FAC-R-018.md) | Input: `Ownership`, `SiteSurvey`, `LandPurchaseSummary`, `LinkLandPurchaseInspection`, `DemographicResults` carry `ProjectEntityID` and no hard-typed FK to `Facility`/`Location`/`Parcel`. Effect: In principle any of these can attach to any  | Derived |

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Soft references (10)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `EnvironmentalEngineerID` | Environment Engineer | Contact | Global |  |  |
| `FinanceAgentID` | Finance Agent | Contact | Global |  |  |
| `OwnerBrokerID` | Purchaser Broker | Contact | Global |  |  |
| `OwnerID` | Purchaser | Contact | Global |  |  |
| `OwnerLawyerID` | Purchaser Attorney | Contact | Global |  |  |
| `OwnerSigneeID` | Purchaser Signee | Contact | Global |  |  |
| `SellerBrokerID` | Selling Broker | Contact | Global |  |  |
| `SellerID` | Seller | Contact | Global |  |  |
| `SellerLawyerID` | Seller's Lawyer | Contact | Global |  |  |
| `SellerSigneeID` | Seller Signee | Contact | Global |  |  |

### Money (5)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AskingPrice` | Asking Price | Currency | Global |  |  |
| `BuyingCommissionAmount` | Purchaser Commission | Currency | Global |  |  |
| `EarnestMoney` | Earnest money | Currency | Global |  |  |
| `SalePrice` | Sales Price | Currency | Global |  |  |
| `SellingCommissionAmount` | Seller Commission | Currency | Global |  |  |

### Quantities (5)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Acreage` |  | 5-Digit Number | Global |  |  |
| `LandPurchaseSummaryID` | Purchase Summary RecID | Number | Global |  |  |
| `SurveyReviewDays` | Survey Review Period | Number | Global |  |  |
| `TitleReviewDays` | Title Review Period | Number | Global |  |  |
| `WaiverDays` | Waiver Period | Number | Global |  |  |

### Dates & timestamps (8)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AmendedCommencementDate` | Amended Commencement Date | Date | Global |  |  |
| `ClosingDate` | Expected contract signing date | Date | Global |  |  |
| `CommencementDate` | Commencement Date | Date | Global |  |  |
| `EarnestMoneyHardDate` | Earnest Money Hard Date | Date | Global |  |  |
| `EffectiveDate` | Effective Date | Date | Global |  |  |
| `FacilityOpenDate` | Expected Store Opening Date | Date | Global |  |  |
| `SignedPurchaserDate` | Date Purchaser Signed | Date | Global |  |  |
| `SignedSellerDate` | Date Seller Signed | Date | Global |  |  |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ContractOptions` | Contract Options | Text | Global |  |  |
| `Description` | Property Description | Text | Global |  |  |
| `Notes` |  | Text | Global |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Purchase Summary ClientID | Text | Global | yes |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
