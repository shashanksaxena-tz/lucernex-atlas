# ACC-R-001 — Default discount rate resolution ↑ upgraded

*Lease Accounting & Payments · Observed*

**resolve Portfolio-level rate first; if none exists, Firm-level rate. Do not read the contract-level rate.**

Portfolio rate first; firm rate if there is none. The contract-level rate is explicitly not consulted for this default.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | any calculation that needs a discount rate and finds no contract-level override |
| What it reads | `Program.SLDiscountRate` (`sTYPE_PERCENTAGE`, the portfolio-level default); `DiscountRate` rows (scoped by `ProgramID`, `CountryID`/`CountryIDList`/`StateProvinceIDList`, `CodeContractUseID`, `CodeAccountingMethodID`, `MinSchedMons`/`MaxSchedMons`, `EffectiveThroughDate`); `Contract.ProgramID` |
| What it computes | resolve Portfolio-level rate first; if none exists, Firm-level rate. Do not read the contract-level rate |
| What it writes | `Contract.ComputedSLDiscountRate` (`sTYPE_PERCENTAGE`) |

## The wording it rests on

> Lx will first use the discount rate at the Portfolio-level, if it exists, otherwise it will use the rate at the Firm-level. This field will not pull the discount rate from the contract-level.

## What it constrains

[Program](../entities/Program.md), [DiscountRate](../entities/DiscountRate.md), [Contract](../entities/Contract.md)

Columns named: `Program.SLDiscountRate`, `Contract.ProgramID`, `Contract.ComputedSLDiscountRate`

## Confidence

Observed — "Lx will first use the discount rate at the Portfolio-level, if it exists, otherwise it will use the rate at the Firm-level. This field will not pull the discount rate from the contract-level." The portfolio-level column is now named: `Program.SLDiscountRate` — "Enter the default discount rate for your company here. The discount rate is also known as the Interest Rate or Internal Borrower Rate (IBR). To enter a discount rate, enter the number no % or decimal is necessary." ⚠ Note the entry convention: no `%` sign and no decimal point — `5` means 5%, not 0.05. That is a migratio

---

Source: `docs/modules/accounting/rules.md`
