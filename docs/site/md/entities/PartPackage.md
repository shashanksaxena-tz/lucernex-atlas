# PartPackage

*6 fields · module: Assets, Equipment & Maintenance · Postgres: `part_package`*

A named kit/bundle of parts, the header record above PartPackageItem.

Source: `data-fields/small-miscellaneous-entities.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 6 |
| Fields with a vendor definition | 6 of 6 inventoried |
| Physical tables | `part_package` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 6 (6 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 2 other records |
| Tenancy position | firm_global |
| Rules that name it | 1 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### Lands in part_package

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 6 fields carry a vendor definition

**Observed.** 6 of this record's 6 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: the captures agree

**Observed.** Over the 6 fields both the Data Fields catalogue and the field inventory contain, the two agree on every one. 2 are marked required.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [AST-R-014](../rules/AST-R-014.md) | Input: `LinkIssuePart.IssueID` + `.AssetID` (typed `Equipment ID`) + `.PartID` + `.Quantity` + `.CostPerPart` + `.TotalCost` + `.SerialNumber` — an object in the `projects-capital` module, not this one. Effect: The practical path from a `Wo | Derived |

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `VendorID` | Vendor | Select the vendor associated with this part package from this field. | Employer ID | Global |  | `part_package.VendorID · TEXT` | [Employer](Employer.md) |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `PartPackageID` | Part Package RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `part_package.PartPackageID · VARCHAR(64) NOT NULL` |  |

### Text & notes (1)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `PartPackageName` | Part Package Name | Enter the part package name in this field. | Text | Global | yes | `part_package.PartPackageName · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Part Package ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `part_package.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `part_package.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `part_package.ModifiedDate · TEXT` |  |
