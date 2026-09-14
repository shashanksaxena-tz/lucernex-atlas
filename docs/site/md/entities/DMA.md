# DMA

*7 fields · module: Facilities, Locations & Sites · Postgres: `d_m_a`*

A Designated Market Area (a standard US media-market geography) reference record, used for site-selection demographic comparison.

Source: `data-fields/demographics-market-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 7 |
| Fields with a vendor definition | 7 of 7 inventoried |
| Physical tables | `d_m_a` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 7 (7 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 10 keys from 10 record types |
| Points at | 1 other records |
| Tenancy position | firm_global |
| Rules that name it | 0 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### Lands in d_m_a

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 7 fields carry a vendor definition

**Observed.** 7 of this record's 7 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: the captures agree

**Observed.** Over the 7 fields both the Data Fields catalogue and the field inventory contain, the two agree on every one. 4 are marked required.

## Fields

### Quantities (2)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DMAID` | DMA RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `d_m_a.DMAID · VARCHAR(64) NOT NULL` |  |
| `DMANumber` | DMA Number | Enter the demographic market area number in this field. | Number | Global | yes | `d_m_a.DMANumber · TEXT` |  |

### Text & notes (2)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DMAName` | DMA Name | Enter the demographic market area name in this field. | Text | Global | yes | `d_m_a.DMAName · TEXT` |  |
| `ShortName` | Short Name | Enter a shortened name for the demographic market area in this field. | Text | Global | yes | `d_m_a.ShortName · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | DMA ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `d_m_a.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `d_m_a.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `d_m_a.ModifiedDate · TEXT` |  |

## What points here (10 keys)

| Record type | Via column |
|---|---|
| [BudgetOptionTemplate](BudgetOptionTemplate.md) | `DemographicDMAID` |
| [Contract](Contract.md) | `DemographicDMAID` |
| [Facility](Facility.md) | `DemographicDMAID` |
| [Location](Location.md) | `DemographicDMAID` |
| [Parcel](Parcel.md) | `DemographicDMAID` |
| [PotentialProject](PotentialProject.md) | `DemographicDMAID` |
| [Program](Program.md) | `DemographicDMAID` |
| [Project](Project.md) | `DemographicDMAID` |
| [ProjectEntity](ProjectEntity.md) | `DemographicDMAID` |
| [Prototype](Prototype.md) | `DemographicDMAID` |
