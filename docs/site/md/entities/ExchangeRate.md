# ExchangeRate

*8 fields · module: Platform & Tenancy · Postgres: `exchange_rate`*

A currency exchange rate captured at a point in time for a Contract, supporting multi-currency financial calculations.

Source: `data-fields/small-miscellaneous-entities.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 8 |
| Fields with a vendor definition | 8 of 8 inventoried |
| Physical tables | `exchange_rate` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 8 (8 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 1 other records |
| Tenancy position | firm_global |
| Rules that name it | 1 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### Lands in exchange_rate

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 8 fields carry a vendor definition

**Observed.** 8 of this record's 8 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: the captures agree

**Observed.** Over the 8 fields both the Data Fields catalogue and the field inventory contain, the two agree on every one. 6 are marked required.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [PLT-R-011](../rules/PLT-R-011.md) | The rate used for a calculation is whatever was captured effective as of a given date, not a re-derived live lookup — supports historical reporting without recomputation | Derived |

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global |  | `exchange_rate.ContractID · TEXT` | [Contract](Contract.md) |

### Coded values (drop-downs) (3)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeExchangeRateTypeID` | Exchange Rate Type | Select the type of exchange rate you are creating from the Type field. This field allows you to enter multiple exchange rates for the same fiscal period, giving you greater flexibility in reporting. There are three default exchange rate types: Balance, Period Average, and Cash. You can also create new types to suit your business needs. | Dropdown (Exchange Rate Type Code) | Global | yes | `exchange_rate.CodeExchangeRateTypeID · TEXT` | Exchange Rate Type Code |
| `CodeFromCurrencyTypeID` | From Currency | Select the currency you are converting from from this field. | Dropdown (Currency Type Code) | Global | yes | `exchange_rate.CodeFromCurrencyTypeID · TEXT` | Currency Type Code |
| `CodeToCurrencyTypeID` | To Currency | Select the currency you are converting to from this field. | Dropdown (Currency Type Code) | Global | yes | `exchange_rate.CodeToCurrencyTypeID · TEXT` | Currency Type Code |

### Quantities (2)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ConversionRate` | Exchange Rate | Enter the currency conversion rate you are using in this field. | 5-Digit Number | Global | yes | `exchange_rate.ConversionRate · TEXT` |  |
| `ExchangeRateID` | Exchange Rate RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `exchange_rate.ExchangeRateID · VARCHAR(64) NOT NULL` |  |

### Dates & timestamps (1)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `EffectiveDate` | Effective Date | Enter the effective date of the exchange rate in this field. | Date | Global | yes | `exchange_rate.EffectiveDate · TEXT` |  |

### Audit & record keeping (1)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Exchange Rate ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `exchange_rate.BOMapClientRecordID · TEXT` |  |
