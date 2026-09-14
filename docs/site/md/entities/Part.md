# Part

*16 fields · module: Assets, Equipment & Maintenance · Postgres: `part`*

An equipment/maintenance parts-catalog record — cost, manufacturer, and model number, supporting the Equipment/Assets maintenance workflow. 16 Global fields under Company Items.

Source: `data-fields/part.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 16 |
| Catalogued fields | 16 (16 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 2 other records |
| Tenancy position | firm_global |
| Rules that name it | 3 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [LAY-R-174](../rules/LAY-R-174.md) | A custom list has a Type — `Standard` (2634) or `Part` (2635) — sharing machinery with the Parts and Inventory module. · Observed · 006 | Observed |
| [AST-R-014](../rules/AST-R-014.md) | Input: `LinkIssuePart.IssueID` + `.AssetID` (typed `Equipment ID`) + `.PartID` + `.Quantity` + `.CostPerPart` + `.TotalCost` + `.SerialNumber` — an object in the `projects-capital` module, not this one. Effect: The practical path from a `Wo | Derived |
| [AST-R-015](../rules/AST-R-015.md) | Input: `Part.QuantityOnHand`, `.QuantityOnOrder`, `.ParLevel`, `.OrderToLevel` — single counters on the catalog record, with no `FacilityID`/warehouse column anywhere in this module. Effect: A tenant with parts stocked at multiple locations | Derived |

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `VendorID` | Vendor ID | Employer ID | Global |  | [Employer](Employer.md) |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeAssetCategoryIDList` | Maintenance Categories | Dropdown (Asset Category Code) | Global |  | Asset Category Code |

### Money (1)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Cost` |  | Currency | Global |  |  |

### Quantities (6)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `OrderToLevel` | Order To Level | Number | Global |  |  |
| `ParLevel` | Par Level | Number | Global |  |  |
| `PartID` | Part RecID | Number | Global |  |  |
| `QuantityOnHand` | Quantity On Hand | Number | Global |  |  |
| `QuantityOnOrder` | Quantity On Order | Number | Global |  |  |
| `WarrantyPeriodInDays` | Warranty Period In Days | Number | Global |  |  |

### Text & notes (4)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Manufacturer` |  | Text | Global |  |  |
| `ModelNumber` | Model Number | Text | Global |  |  |
| `PartName` | Part Name | Text | Global | yes |  |
| `PartPhoto` | Part Photo | Text | Global |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Part ClientID | Text | Global | yes |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
