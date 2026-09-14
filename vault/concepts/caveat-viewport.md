---
title: "Caveat: a screenshot is evidence only for what is in the frame"
tags: [caveat, method, meta]
evidence: Observed
---

These are **ExtJS viewport applications**. Grids scroll *inside* the page, not with it, so a
screenshot never shows more rows than the viewport happened to hold. The grids are also wider than the
capture, and **the right edge is exactly where row-action columns, pagination and required asterisks
live**.

**Check for truncation before inferring absence.** This rule exists because an inference was published
and then withdrawn after a `*` turned out to be cropped out of frame.

Where a grid's data can be read as JSON, the JSON is the primary evidence and the screenshot is
illustration. Nearly every count in this vault comes from a bulk JSON endpoint, not from counting rows
in a picture:

```
{page}.jsp?ajaxList=true&ajax=true&popupList=true&BOType={type}&start=0&limit=5000
```

which returns `{totalCount, topics[]}` and enumerates a whole screen in one request.

Two related traps live next door: [[method-fetch-is-not-render]] and [[method-cheap-signals]].

Applies to every note in [[map-of-screens]].

Source: [`CONVENTIONS.md`](../../docs/CONVENTIONS.md)
