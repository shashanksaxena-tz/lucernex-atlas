# DemographicReport

*10 fields · module: Facilities, Locations & Sites · Postgres: `demographic_report`*

A demographic report definition tied to a market area, the report-level wrapper around DemographicResults/DemographicFact data.

Source: `data-fields/demographics-market-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 10 |
| Fields with a vendor definition | 8 of 10 inventoried |
| Physical tables | `demographic_report` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 10 (10 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 3 other records |
| Tenancy position | firm_global |
| Rules that name it | 0 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### Lands in demographic_report

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 8 fields carry a vendor definition

**Observed.** 8 of this record's 10 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: the captures agree

**Observed.** Over the 10 fields both the Data Fields catalogue and the field inventory contain, the two agree on every one. 2 are marked required.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `PrototypeID` | Prototype |  | Prototype ID | Global |  | `demographic_report.PrototypeID · TEXT` | [Prototype](Prototype.md) |
| `RegionID` | Region | Select the region and sub-region from this field. The values that appear in this field depend on the org chart of the portfolio. | Region ID | Global |  | `demographic_report.RegionID · TEXT` | [Region](Region.md) |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeMarketAreaID` | Market Area | This is a default field that is not used for this record type. | Dropdown (Market Area Code) | Global |  | `demographic_report.CodeMarketAreaID · TEXT` | Market Area Code |
| `CodeMarketTypeID` | Market Type | This is a generic field. It is not implemented for this record type. | Dropdown (Market Type Code) | Global |  | `demographic_report.CodeMarketTypeID · TEXT` | Market Type Code |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DemographicReportID` | Demographic Report RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `demographic_report.DemographicReportID · VARCHAR(64) NOT NULL` |  |

### Text & notes (2)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DemographicReportName` | Name |  | Text | Global | yes | `demographic_report.DemographicReportName · TEXT` |  |
| `TradeArea` | Trade Area | Enter the trade area in this field. | Text | Global |  | `demographic_report.TradeArea · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Demographic Report ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `demographic_report.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `demographic_report.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `demographic_report.ModifiedDate · TEXT` |  |
