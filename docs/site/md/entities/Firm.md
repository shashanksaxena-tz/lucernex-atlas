# Firm

*18 fields · module: Platform & Tenancy · Postgres: `firm`*

The tenant-company configuration record — one row per Lx client firm, holding default page-layout assignments per module (Facility Setup Page, Equipment Contract Setup Page) and default folder security. 24 fields (23 Global, 1 Firm) spanning Company Items, Statics, and Summary Information; this is the master firm-level settings record, not to be confused with the 'Firm' scope of this whole catalog.

Source: `data-fields/firm.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 18 |
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

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CapProgramSetupPageLayoutID` | Capital Program Setup Page | item ID | Global |  | unresolved |
| `CapProjectSetupPageLayoutID` | Capital Project Setup Page | item ID | Global |  | unresolved |
| `ContractSetupPageLayoutID` | RE Contract Setup Page | item ID | Global |  | unresolved |
| `EquipmentContractSetupPageLayoutID` | Equipment Contract Setup Page | item ID | Global |  | unresolved |
| `FacilitySetupPageLayoutID` | Facility Setup Page | item ID | Global |  | unresolved |
| `LocationSetupPageLayoutID` | Location Setup Page | item ID | Global |  | unresolved |
| `OpenProjectSetupPageLayoutID` | Opening Project Setup Page | item ID | Global |  | unresolved |
| `ParcelSetupPageLayoutID` | Parcel Setup Page | item ID | Global |  | unresolved |
| `PortfolioSetupPageLayoutID` | Portfolio Setup Page | item ID | Global |  | unresolved |
| `PrototypeSetupPageLayoutID` | Prototype Setup Page | item ID | Global |  | unresolved |
| `SiteSetupPageLayoutID` | Site Setup Page | item ID | Global |  | unresolved |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeDefaultFolderSecurityID` | Default Folder Security | Dropdown (Security Type Code) | Global | yes | Security Type Code |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Firm_HeaderLogo` | Header Logo | Text | Firm |  |  |
| `JSONConfigText` | JSON Configuration | Text | Global |  |  |
| `SvcChannelFirmID` | Service Channel FirmID | Text | Global |  |  |

### Audit & record keeping (2)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |

### Other (1)

Everything that did not fall into a named group.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CurrentDate` | Current Date | Current Date | Global |  |  |
