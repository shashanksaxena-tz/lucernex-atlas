# BidderIssue — Data Fields

One bidder's response to a BidPackage — conditioned bid amount and allow-conditioning flag, letting a bidder submit a qualified rather than firm bid. 20 Global fields under Specialized Forms.

**Table Association:** `BidderIssue` &nbsp;·&nbsp; **Total fields:** 20 (Global: 20, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Allow Conditioning | `AllowConditioning` | `sTYPE_CHECKBOX` | Global | Yes | No |  | Specialized Forms / Bidder |
| Bid Package | `BidPackageID` | `sTYPE_BID_PACKAGE` | Global | Yes | No |  | Specialized Forms / Bidder |
| Bidder Issue ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Specialized Forms / Bidder |
| Bidder Issue Issue | `IssueID` | `sTYPE_ISSUE` | Global | Yes | No |  | Specialized Forms / Bidder |
| Bidder Issue RecID | `BidderIssueID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Specialized Forms / Bidder |
| Conditioned Bid Amount | `ConditionedBidAmount` | `sTYPE_MONEY` | Global | No | No |  | Specialized Forms / Bidder |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Specialized Forms / Bidder |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Specialized Forms / Bidder |
| Extended Bid Close Date | `ExtendedBidCloseDate` | `sTYPE_DATE` | Global | No | No |  | Specialized Forms / Bidder |
| Is Bid Invite Accepted? | `IsBidInviteAccepted` | `sTYPE_YES_NO_RADIO` | Global | No | No |  | Specialized Forms / Bidder |
| Is Winning Bid? | `IsWinningBid` | `sTYPE_BOOLEAN` | Global | No | No |  | Specialized Forms / Bidder |
| Member | `MemberIDList` | `sTYPE_MEMBER` | Global | No | No |  | Specialized Forms / Bidder |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Specialized Forms / Bidder |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Specialized Forms / Bidder |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Specialized Forms / Bidder |
| Notification Date | `NotificationDate` | `sTYPE_DATE` | Global | No | No |  | Specialized Forms / Bidder |
| Number | `SequenceNumber` | `sTYPE_TEXT` | Global | Yes | No |  | Specialized Forms / Bidder |
| Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Specialized Forms / Bidder |
| Submitted Bid Amount | `SubmittedBidAmount` | `sTYPE_MONEY` | Global | No | No |  | Specialized Forms / Bidder |
| Vendor | `UniqueVendorID` | `sTYPE_EMPLOYER` | Global | Yes | No |  | Specialized Forms / Bidder |
