# DMA

*7 fields · module: Facilities, Locations & Sites · Postgres: `d_m_a`*

A Designated Market Area (a standard US media-market geography) reference record, used for site-selection demographic comparison.

Source: `data-fields/demographics-market-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 7 |
| Catalogued fields | 7 (7 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 10 keys from 10 record types |
| Points at | 1 other records |
| Tenancy position | firm_global |
| Rules that name it | 0 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

## Fields

### Quantities (2)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DMAID` | DMA RecID | Number | Global |  |  |
| `DMANumber` | DMA Number | Number | Global | yes |  |

### Text & notes (2)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DMAName` | DMA Name | Text | Global | yes |  |
| `ShortName` | Short Name | Text | Global | yes |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | DMA ClientID | Text | Global | yes |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |

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
