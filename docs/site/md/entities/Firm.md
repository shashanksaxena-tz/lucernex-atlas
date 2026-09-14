# Firm

*18 fields · module: Platform & Tenancy · Postgres: `firm`*

The tenant-company configuration record — one row per Lx client firm, holding default page-layout assignments per module (Facility Setup Page, Equipment Contract Setup Page) and default folder security. 24 fields (23 Global, 1 Firm) spanning Company Items, Statics, and Summary Information; this is the master firm-level settings record, not to be confused with the 'Firm' scope of this whole catalog.

Source: `data-fields/firm.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 18 |
| Fields with a vendor definition | 14 of 18 inventoried |
| Physical tables | `firm` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 24 (23 global, 1 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 1 other records |
| Tenancy position | firm_global |
| Rules that name it | 4 |

## What to know before rebuilding this

### 1 tenant custom columns

**Observed.** This record carries 1 physical Firm_-prefixed columns — tenant custom fields are real columns, not rows in a value store, so adding one is a DDL change. That is direct evidence for database-per-tenant and against a shared schema.

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### 1 catalogued Firm-scope fields

**Observed.** Of 24 catalogued fields on this record, 1 are Firm scope — defined by this tenant rather than shipped by the platform. Firm-scope definitions are RGAF rows carrying IsGlobal, FirmID and IsClientExtensionField.

### Lands in firm

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 14 fields carry a vendor definition

**Observed.** 14 of this record's 18 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 1 of this record's fields required; the Data Fields catalogue marks 2; 1 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [LAY-R-181](../rules/LAY-R-181.md) | Setup-page assignment exists at two levels: `Firm` (11 slots, tenant default) and `Program` (18 slots — 11 setup pages + 7 map popups, per Portfolio/Capital Program). Only the Firm level was observed in the UI. | Observed |
| [LAY-R-183](../rules/LAY-R-183.md) | Map Popup Layouts are a third, minimal rendering context, distinct from Summary Page and Wizard. The seven `*MapSetupLayoutID` columns sit on `Program`, not `Firm`, implying portfolio scope. | Observed |
| [PLT-R-004](../rules/PLT-R-004.md) | The new subtype needs a default setup-page-layout assignment, the same way the existing eleven do | Observed |
| [POR-R-001](../rules/POR-R-001.md) | A `Contract` needs a fiscal period, discount rate, or ASC 842 threshold · `Contract.ProgramID` · Resolves to `Program`'s policy fields (`SLDiscountRate`, `FairValueThreshold`, `RemainingEconomicLifeThreshold`, `FiscalYearEnd`, FX rate types | Observed |

## Fields

### Relationships (foreign keys) (11)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CapProgramSetupPageLayoutID` | Capital Program Setup Page | The page layout ID of the first page of the Capital Program Setup Wizard. | item ID | Global |  | `firm.CapProgramSetupPageLayoutID · TEXT` | unresolved |
| `CapProjectSetupPageLayoutID` | Capital Project Setup Page | The page layout ID of the first page of the Capital Project Setup Wizard. | item ID | Global |  | `firm.CapProjectSetupPageLayoutID · TEXT` | unresolved |
| `ContractSetupPageLayoutID` | RE Contract Setup Page | The page layout ID of the first page of the RE Contract Setup Wizard. | item ID | Global |  | `firm.ContractSetupPageLayoutID · TEXT` | unresolved |
| `EquipmentContractSetupPageLayoutID` | Equipment Contract Setup Page | The page layout ID of the first page of the Equipment Contract Setup Wizard. | item ID | Global |  | `firm.EquipmentContractSetupPageLayoutID · TEXT` | unresolved |
| `FacilitySetupPageLayoutID` | Facility Setup Page | The page layout ID of the first page of the Facility Setup Wizard. | item ID | Global |  | `firm.FacilitySetupPageLayoutID · TEXT` | unresolved |
| `LocationSetupPageLayoutID` | Location Setup Page | The page layout ID of the first page of the Location Setup Wizard. | item ID | Global |  | `firm.LocationSetupPageLayoutID · TEXT` | unresolved |
| `OpenProjectSetupPageLayoutID` | Opening Project Setup Page | The page layout ID of the first page of the Project Setup Wizard. | item ID | Global |  | `firm.OpenProjectSetupPageLayoutID · TEXT` | unresolved |
| `ParcelSetupPageLayoutID` | Parcel Setup Page | The page layout ID of the first page of the Parcel Setup Wizard. | item ID | Global |  | `firm.ParcelSetupPageLayoutID · TEXT` | unresolved |
| `PortfolioSetupPageLayoutID` | Portfolio Setup Page | The page layout ID of the first page of the Portfolio Setup Wizard. | item ID | Global |  | `firm.PortfolioSetupPageLayoutID · TEXT` | unresolved |
| `PrototypeSetupPageLayoutID` | Prototype Setup Page | The page layout ID of the first page of the Prototype Setup Wizard. | item ID | Global |  | `firm.PrototypeSetupPageLayoutID · TEXT` | unresolved |
| `SiteSetupPageLayoutID` | Site Setup Page | The page layout ID of the first page of the Site Setup Wizard. | item ID | Global |  | `firm.SiteSetupPageLayoutID · TEXT` | unresolved |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeDefaultFolderSecurityID` | Default Folder Security |  | Dropdown (Security Type Code) | Global | yes | `firm.CodeDefaultFolderSecurityID · TEXT` | Security Type Code |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Firm_HeaderLogo` | Header Logo |  | Text | Firm |  | `firm.Firm_HeaderLogo · TEXT` |  |
| `JSONConfigText` | JSON Configuration |  | Text | Global |  | `firm.JSONConfigText · TEXT` |  |
| `SvcChannelFirmID` | Service Channel FirmID |  | Text | Global |  | `firm.SvcChannelFirmID · TEXT` |  |

### Audit & record keeping (2)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `firm.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `firm.ModifiedDate · TEXT` |  |

### Other (1)

Everything that did not fall into a named group.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CurrentDate` | Current Date | Calculates the current date. | Current Date | Global |  | `firm.CurrentDate · TEXT` |  |
