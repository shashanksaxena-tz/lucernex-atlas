# BidPackage — Data Fields

The competitive-bid solicitation record for a capital project — ranked bidder results (1st Place Bidder Name/Amount, and by pattern 2nd/3rd) plus its own page-layout assignment (Bid Award and Cancellation Layout) and approval-status/date fields for the award decision. 53 Global fields under Specialized Forms; it anchors a large ancillary family (BidPackageTemplate, BidderIssue, BidPackageAlternate/Breakout and their Value variants) that model the line items and alternates within a single bid.

**Table Association:** `BidPackage` &nbsp;·&nbsp; **Total fields:** 53 (Global: 53, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| 1st Place Bidder Name | `FirstPlaceBidderName` | `sTYPE_TEXT` | Global | No | No |  | Specialized Forms / Bid Package |
| 1st Place Bidder Vendor Name | `FirstPlaceBidderVendorName` | `sTYPE_TEXT` | Global | No | No |  | Specialized Forms / Bid Package |
| 1st Place ConditionedAmount | `FirstPlaceConditionedAmount` | `sTYPE_MONEY` | Global | No | No |  | Specialized Forms / Bid Package |
| 1st Place Submitted Amount | `FirstPlaceSubmittedAmount` | `sTYPE_MONEY` | Global | No | No |  | Specialized Forms / Bid Package |
| Bid Award Approval Status | `CodeBidPackageAwardStatusID` | `sCODE_LAST_ACTION_STATUS` | Global | No | No |  | Specialized Forms / Bid Package |
| Bid Award Date | `BidAwardDate` | `sTYPE_TIME` | Global | No | No |  | Specialized Forms / Bid Package |
| Bid Award and Cancellation Layout | `BidAwardLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | No | No |  | Specialized Forms / Bid Package |
| Bid Awarded By | `BidAwardByID` | `sTYPE_MEMBER` | Global | No | No |  | Specialized Forms / Bid Package |
| Bid Budget Column Type | `BidBudgetColumnTypeID` | `sTYPE_BUDGET_COLUMN_TYPE` | Global | No | No |  | Specialized Forms / Bid Package |
| Bid Cancelled By | `BidCancelledByID` | `sTYPE_MEMBER` | Global | No | No |  | Specialized Forms / Bid Package |
| Bid Cancelled Date | `BidCancelledDate` | `sTYPE_TIME` | Global | No | No |  | Specialized Forms / Bid Package |
| Bid Close Date | `BidCloseDate` | `sTYPE_TIME` | Global | No | No |  | Specialized Forms / Bid Package |
| Bid Grace Period | `BidGracePeriod` | `sTYPE_NUMBER` | Global | No | No |  | Specialized Forms / Bid Package |
| Bid Grace Period Time Unit | `CodeBidGracePeriodTimeUnitID` | `sCODE_BID_GRACE_PERIOD_TIME_UNIT` | Global | No | No |  | Specialized Forms / Bid Package |
| Bid Invitation Layout | `BidInvitationLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | No | No |  | Specialized Forms / Bid Package |
| Bid Loss Layout | `BidLossLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | No | No |  | Specialized Forms / Bid Package |
| Bid Open Date | `BidOpenDate` | `sTYPE_TIME` | Global | No | No |  | Specialized Forms / Bid Package |
| Bid Package ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Specialized Forms / Bid Package |
| Bid Package Issue | `IssueID` | `sTYPE_ISSUE` | Global | Yes | No |  | Specialized Forms / Bid Package |
| Bid Package RecID | `BidPackageID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Specialized Forms / Bid Package |
| Bid Package Status | `CodeBidPackageStatusID` | `sCODE_BID_PACKAGE_STATUS` | Global | Yes | No |  | Specialized Forms / Bid Package |
| Bid Package Template | `BidPackageTemplateID` | `sTYPE_BID_PACKAGE_TEMPLATE` | Global | No | No |  | Specialized Forms / Bid Package |
| Bidder Kick Off Page Layout | `BidderKickOffPageLayoutID` | `sTYPE_BIDDER_LAYOUT` | Global | No | No |  | Specialized Forms / Bid Package |
| Budget View | `BudgetViewID` | `sTYPE_BUDGET_VIEW` | Global | No | No |  | Specialized Forms / Bid Package |
| Canceled Bid Notification | `CanceledBidNotification` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Specialized Forms / Bid Package |
| Condition Budget Column Type | `ConditionBudgetColumnTypeID` | `sTYPE_BUDGET_COLUMN_TYPE` | Global | No | No |  | Specialized Forms / Bid Package |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Specialized Forms / Bid Package |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Specialized Forms / Bid Package |
| Enable Unsealed Bidding | `enableUnsealedBidding` | `sTYPE_BOOLEAN` | Global | No | No |  | Specialized Forms / Bid Package |
| Estimate Budget Column Type | `EstimateBudgetColumnTypeID` | `sTYPE_BUDGET_COLUMN_TYPE` | Global | No | No |  | Specialized Forms / Bid Package |
| Estimated Bid Amount | `EstimatedBidAmount` | `sTYPE_MONEY` | Global | No | No |  | Specialized Forms / Bid Package |
| Invite Bidders | `InviteBidders` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Specialized Forms / Bid Package |
| Max Number Of Bids | `MaxNumberOfBids` | `sTYPE_NUMBER` | Global | No | No |  | Specialized Forms / Bid Package |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Specialized Forms / Bid Package |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Specialized Forms / Bid Package |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Specialized Forms / Bid Package |
| Notify All Bidders | `NotifyAllBidders` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Specialized Forms / Bid Package |
| Notify Losing Bidders | `NotifyLosingBidders` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Specialized Forms / Bid Package |
| Notify Winning Bidder | `NotifyWinningBidder` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Specialized Forms / Bid Package |
| Number | `SequenceNumber` | `sTYPE_TEXT` | Global | Yes | No |  | Specialized Forms / Bid Package |
| Number Of Active Bidders | `NumberOfActiveBidders` | `sTYPE_NUMBER` | Global | No | No |  | Specialized Forms / Bid Package |
| Number Of Bid Invites Accepted | `NumberOfBidInvitesAccepted` | `sTYPE_NUMBER` | Global | No | No |  | Specialized Forms / Bid Package |
| Number Of Bid Invites Declined | `NumberOfBidInvitesDeclined` | `sTYPE_NUMBER` | Global | No | No |  | Specialized Forms / Bid Package |
| Number Of Bid Invites Used | `NumberOfBidInvitesUsed` | `sTYPE_NUMBER` | Global | No | No |  | Specialized Forms / Bid Package |
| Number Of Bid Invites Waiting | `NumberOfBidInvitesWaiting` | `sTYPE_NUMBER` | Global | No | No |  | Specialized Forms / Bid Package |
| Pre-Accept Folder Security User Class | `CodePreAcceptFolderSecurityID` | `sCODE_USER_CLASS` | Global | No | No |  | Specialized Forms / Bid Package |
| Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Specialized Forms / Bid Package |
| Total Number Of Bidders | `TotalNumberOfBidders` | `sTYPE_NUMBER` | Global | No | No |  | Specialized Forms / Bid Package |
| Winning Bid | `WinningBidderIssueID` | `sTYPE_BIDDER_ISSUE` | Global | No | No |  | Specialized Forms / Bid Package |
| Winning Bid Member | `WinningBidMemberIDList` | `sTYPE_MEMBER` | Global | No | No |  | Specialized Forms / Bid Package |
| Winning Bid Vendor | `WinningBidVendorID` | `sTYPE_EMPLOYER` | Global | No | No |  | Specialized Forms / Bid Package |
| Winning Conditioned Bid Amount | `WinningConditionedBidAmount` | `sTYPE_MONEY` | Global | No | No |  | Specialized Forms / Bid Package |
| Winning Submitted Bid Amount | `WinningSubmittedBidAmount` | `sTYPE_MONEY` | Global | No | No |  | Specialized Forms / Bid Package |
