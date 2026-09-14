# ExchangeRate

*8 fields · module: Platform & Tenancy · Postgres: `exchange_rate`*

A currency exchange rate captured at a point in time for a Contract, supporting multi-currency financial calculations.

Source: `data-fields/small-miscellaneous-entities.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 8 |
| Catalogued fields | 8 (8 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 1 other records |
| Tenancy position | firm_global |
| Rules that name it | 1 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [PLT-R-011](../rules/PLT-R-011.md) | The rate used for a calculation is whatever was captured effective as of a given date, not a re-derived live lookup — supports historical reporting without recomputation | Derived |

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ContractID` | Contract | Contract ID | Global |  | [Contract](Contract.md) |

### Coded values (drop-downs) (3)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeExchangeRateTypeID` | Exchange Rate Type | Dropdown (Exchange Rate Type Code) | Global | yes | Exchange Rate Type Code |
| `CodeFromCurrencyTypeID` | From Currency | Dropdown (Currency Type Code) | Global | yes | Currency Type Code |
| `CodeToCurrencyTypeID` | To Currency | Dropdown (Currency Type Code) | Global | yes | Currency Type Code |

### Quantities (2)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ConversionRate` | Exchange Rate | 5-Digit Number | Global | yes |  |
| `ExchangeRateID` | Exchange Rate RecID | Number | Global |  |  |

### Dates & timestamps (1)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `EffectiveDate` | Effective Date | Date | Global | yes |  |

### Audit & record keeping (1)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Exchange Rate ClientID | Text | Global | yes |  |
