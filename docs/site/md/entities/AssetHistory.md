# AssetHistory

*13 fields · module: Assets, Equipment & Maintenance · Postgres: `asset_history`*

A point-in-time snapshot of an Asset's financial state, letting the platform show what an asset's values were before a later recalculation.

Source: `data-fields/audit-history-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 13 |
| Fields with a vendor definition | 13 of 13 inventoried |
| Physical tables | — |
| Replication database | — |
| Catalogued fields | 13 (13 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 3 other records |
| Tenancy position | firm_global |
| Rules that name it | 1 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### 13 fields carry a vendor definition

**Observed.** 13 of this record's 13 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: the captures agree

**Observed.** Over the 13 fields both the Data Fields catalogue and the field inventory contain, the two agree on every one. 3 are marked required.

### 13 fields excluded from extraction

**Observed.** Observed of the loader. The inventory marks 13 of this record's fields as not extracted to PostgreSQL, so the replication target creates no column for them. They still exist in Lx; anything reading the replica rather than the product will not see them.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [AST-R-016](../rules/AST-R-016.md) | Input: `AssetHistory.ProjectEntityID` and `.FromProjectEntityID`, both typed the soft `Entity` type rather than the hard `Entity ID` type. Effect: The object behaves as an entity-scoped snapshot of an `Asset`'s state, but escapes the mechan | Derived |

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AssetID` | Asset | The asset ID of the associated equipment asset. | Equipment ID | Global | yes | not extracted | [Asset](Asset.md) |

### Soft references (2)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `FromProjectEntityID` | From Entity | The entity that the asset was moved from. | Entity | Global |  | not extracted |  |
| `ProjectEntityID` | To Entity | The ProjectEntityID is the Base Entity System Identifier for associated tasks, folders, documents, forms, and other records. It is assigned automatically by the system, and is not editable. | Entity | Global | yes | not extracted |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AssetHistoryID` | Asset History RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | not extracted |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `MoveInDate` | Move In Date | The date that the asset was moved to the entity. | Date | Global |  | not extracted |  |
| `MoveOutDate` | Move Out Date | The date that the asset was removed from the entity. | Date | Global |  | not extracted |  |

### Text & notes (1)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Notes` |  | Add any notes about the record. | Text | Global |  | not extracted |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Asset History ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | not extracted |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | not extracted | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | not extracted |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | not extracted | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | not extracted |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | Global |  | not extracted |  |
