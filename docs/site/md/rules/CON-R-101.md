# CON-R-101 — Line-item level

*Contracts & Leases · Derived*

**A line item's approved total is computed: ComputedApprovedTotalAmount applies its own admin fee and cap per line item, not only at the header.**

A line item's approved total is computed: ComputedApprovedTotalAmount applies its own admin fee and cap per line item, not only at the header.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | A line item's approved total is computed |
| Stated as | `ApprovedAmount`, `ApprovedAdminFeeAmtNoZeroDef`, `ApprovedAdminFeePrcntNoZeroDef`, `ApprovedCapAmountNoZeroDef`, `ApprovedCapPercentNoZeroDef` |
| Stated as | `ComputedApprovedTotalAmount{,Gross,Net}` — admin fee and cap apply per line item, not only at the header |
| Stated as | Item total |
| Stated as | Derived |

---

Source: `docs/modules/contracts/rules.md`
