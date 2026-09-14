# Part

*16 fields · module: Assets, Equipment & Maintenance · Postgres: `part`*

An equipment/maintenance parts-catalog record — cost, manufacturer, and model number, supporting the Equipment/Assets maintenance workflow. 16 Global fields under Company Items.

Source: `data-fields/part.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 16 |
| Fields with a vendor definition | 16 of 16 inventoried |
| Physical tables | `part` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 16 (16 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 2 other records |
| Tenancy position | firm_global |
| Rules that name it | 3 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### Lands in part

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 16 fields carry a vendor definition

**Observed.** 16 of this record's 16 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one source in the corpus that explains fields rather than listing them.

### 2 fields marked required

**Observed.** The inventory marks 2 of this record's fields Required. Across the whole inventory that is 606 fields, which independently corroborates the 603 the corpus had derived from the Data Fields catalogue — two sources, arrived at separately, agreeing to within three.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [LAY-R-174](../rules/LAY-R-174.md) | A custom list has a Type — `Standard` (2634) or `Part` (2635) — sharing machinery with the Parts and Inventory module. · Observed · 006 | Observed |
| [AST-R-014](../rules/AST-R-014.md) | Input: `LinkIssuePart.IssueID` + `.AssetID` (typed `Equipment ID`) + `.PartID` + `.Quantity` + `.CostPerPart` + `.TotalCost` + `.SerialNumber` — an object in the `projects-capital` module, not this one. Effect: The practical path from a `Wo | Derived |
| [AST-R-015](../rules/AST-R-015.md) | Input: `Part.QuantityOnHand`, `.QuantityOnOrder`, `.ParLevel`, `.OrderToLevel` — single counters on the catalog record, with no `FacilityID`/warehouse column anywhere in this module. Effect: A tenant with parts stocked at multiple locations | Derived |

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `VendorID` | Vendor ID | Select the vendor who supplies this part from this field. | Employer ID | Global |  | `part.VendorID · TEXT` | [Employer](Employer.md) |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeAssetCategoryIDList` | Maintenance Categories | Select the maintenance categories that this part belongs to from this field. | Dropdown (Asset Category Code) | Global |  | `part.CodeAssetCategoryIDList · TEXT` | Asset Category Code |

### Money (1)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Cost` |  | Enter the unit cost of the part in this field. | Currency | Global |  | `part.Cost · TEXT` |  |

### Quantities (6)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `OrderToLevel` | Order To Level | Enter the maximum quantity you want to have on hand to meet your needs. | Number | Global |  | `part.OrderToLevel · TEXT` |  |
| `ParLevel` | Par Level | Enter the minimum quantity you want to have on hand to meet your needs. Lx will send out an alert if the Par Level is greater than the Order to Level minus the Quantity on Hand and the Quantity on Order. Par Level = Order to Level - (Quantity on Hand + Quantity on Order) | Number | Global |  | `part.ParLevel · TEXT` |  |
| `PartID` | Part RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `part.PartID · VARCHAR(64) NOT NULL` |  |
| `QuantityOnHand` | Quantity On Hand | Enter the quantity of this part on hand. This field is updated when you place an order using a parts custom list. | Number | Global |  | `part.QuantityOnHand · TEXT` |  |
| `QuantityOnOrder` | Quantity On Order | Enter the quantity of this part on order. | Number | Global |  | `part.QuantityOnOrder · TEXT` |  |
| `WarrantyPeriodInDays` | Warranty Period In Days | Enter the warranty period in days for this part. | Number | Global |  | `part.WarrantyPeriodInDays · TEXT` |  |

### Text & notes (4)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Manufacturer` |  | Enter the manufacturer of the part in this field. | Text | Global |  | `part.Manufacturer · TEXT` |  |
| `ModelNumber` | Model Number | Enter the model number of the part in this field. | Text | Global |  | `part.ModelNumber · TEXT` |  |
| `PartName` | Part Name | Enter the part name in this field. | Text | Global | yes | `part.PartName · TEXT` |  |
| `PartPhoto` | Part Photo | This field contains a photo of the part. Photos can be uploaded after the part record has been saved for the first time. | Text | Global |  | `part.PartPhoto · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Part ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `part.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `part.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `part.ModifiedDate · TEXT` |  |
