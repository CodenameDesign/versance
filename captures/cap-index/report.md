# Capture report: https://www.versance.ai/

Captured 2026-11-04T03:02:23.364Z with page-capture 0.1.0 (148.0.7778.96) in 213 s. Widths measured: 1440, 1024, 768, 390 px.

## Summary

- Elements captured: 1300
- Stylesheets: 34; CSS rules written: 2753; unused font subsets skipped: 236
- Files in assets/: 48; downloads that failed: 0
- Interaction states captured: 2 (1 listbox, 1 popover); attempts that showed nothing: 8
- Hover/focus/active: 39 element signatures probed, 36 change on a pseudo-state
- Draft tokens: 123
- Redaction: 0 replacements; leak check searched 0 original values in all text outputs and found 0

## Fidelity: replica vs original

Both are loaded in the same browser; the original is measured live (already redacted), the replica from its own files with every external request blocked.

| Width | Elements compared | With style differences | Properties different | Boxes off by >0.75 px | Pixels different | Page height (orig / replica) |
|---|---|---|---|---|---|---|
| 1440 | 1102 | 15 (1.36%) | 80 of 22705 | 1006 | 427492 (4.9478%) | 6465 / 6470 |
| 1024 | 1102 | 15 (1.36%) | 80 of 22705 | 1006 | 335451 (5.4598%) | 6465 / 6470 |
| 768 | 1102 | 15 (1.36%) | 80 of 22591 | 1006 | 255726 (5.5496%) | 6465 / 6470 |
| 390 | 1102 | 18 (1.63%) | 109 of 22640 | 1018 | 185943 (7.9463%) | 6465 / 6470 |

### Differences at 1440 px

- `grid-template-rows`: 7 elements; e.g. `162px 0px 5780.81px 521.797px` vs `162px 0px 5774.81px 521.797px`
- `border-block-end-style`: 4 elements; e.g. `solid` vs `(default)`
- `border-block-end-width`: 4 elements; e.g. `1px` vs `(default)`
- `border-block-start-style`: 4 elements; e.g. `solid` vs `(default)`
- `border-block-start-width`: 4 elements; e.g. `1px` vs `(default)`
- `border-bottom-style`: 4 elements; e.g. `solid` vs `(default)`
- `border-bottom-width`: 4 elements; e.g. `1px` vs `(default)`
- `border-inline-end-style`: 4 elements; e.g. `solid` vs `(default)`
- box `div` original [0,0,1440,6464.61] vs replica [0,11,1440,6458.61]
- box `div.main_MF` original [0,0,1440,6464.61] vs replica [0,11,1440,6458.61]
- box `div.SCROLL_TO_TOP.ignore-focus.qe3oTb` original [0,0,1440,0] vs replica [0,11,1440,0]

### Differences at 1024 px

- `grid-template-rows`: 7 elements; e.g. `162px 0px 5780.81px 521.797px` vs `162px 0px 5774.81px 521.797px`
- `border-block-end-style`: 4 elements; e.g. `solid` vs `(default)`
- `border-block-end-width`: 4 elements; e.g. `1px` vs `(default)`
- `border-block-start-style`: 4 elements; e.g. `solid` vs `(default)`
- `border-block-start-width`: 4 elements; e.g. `1px` vs `(default)`
- `border-bottom-style`: 4 elements; e.g. `solid` vs `(default)`
- `border-bottom-width`: 4 elements; e.g. `1px` vs `(default)`
- `border-inline-end-style`: 4 elements; e.g. `solid` vs `(default)`
- box `div` original [0,0,1024,6464.61] vs replica [0,11,1024,6458.61]
- box `div.main_MF` original [0,0,1024,6464.61] vs replica [0,11,1024,6458.61]
- box `div.SCROLL_TO_TOP.ignore-focus.qe3oTb` original [0,0,1024,0] vs replica [0,11,1024,0]

### Differences at 768 px

- `grid-template-rows`: 7 elements; e.g. `162px 0px 5780.81px 521.797px` vs `162px 0px 5774.81px 521.797px`
- `border-block-end-style`: 4 elements; e.g. `solid` vs `(default)`
- `border-block-end-width`: 4 elements; e.g. `1px` vs `(default)`
- `border-block-start-style`: 4 elements; e.g. `solid` vs `(default)`
- `border-block-start-width`: 4 elements; e.g. `1px` vs `(default)`
- `border-bottom-style`: 4 elements; e.g. `solid` vs `(default)`
- `border-bottom-width`: 4 elements; e.g. `1px` vs `(default)`
- `border-inline-end-style`: 4 elements; e.g. `solid` vs `(default)`
- box `div` original [0,0,768,6464.61] vs replica [0,11,768,6458.61]
- box `div.main_MF` original [0,0,768,6464.61] vs replica [0,11,768,6458.61]
- box `div.SCROLL_TO_TOP.ignore-focus.qe3oTb` original [0,0,768,0] vs replica [0,11,768,0]

### Differences at 390 px

- `grid-template-rows`: 7 elements; e.g. `162px 0px 5780.81px 521.797px` vs `162px 0px 5774.81px 521.797px`
- `border-block-end-style`: 4 elements; e.g. `solid` vs `(default)`
- `border-block-end-width`: 4 elements; e.g. `1px` vs `(default)`
- `border-block-start-style`: 4 elements; e.g. `solid` vs `(default)`
- `border-block-start-width`: 4 elements; e.g. `1px` vs `(default)`
- `border-bottom-style`: 4 elements; e.g. `solid` vs `(default)`
- `border-bottom-width`: 4 elements; e.g. `1px` vs `(default)`
- `border-inline-end-style`: 4 elements; e.g. `solid` vs `(default)`
- box `div` original [0,0,390,6464.61] vs replica [0,11,390,6458.61]
- box `div.main_MF` original [0,0,390,6464.61] vs replica [0,11,390,6458.61]
- box `div.SCROLL_TO_TOP.ignore-focus.qe3oTb` original [0,0,390,0] vs replica [0,11,390,0]

### Offline and errors

- External requests the replica tried to make (all blocked): 0
- Failed local requests (404 etc.): 0
- Page errors in the replica: 0

### Hover, focus, active

Same forced pseudo-states applied to both: 74 state(s) with a change compared, 71 identical, 3 different.

- `span.s__5CjnXs.se5p61l` active: original `{"color":["rgb(204, 211, 255)","rgb(207, 213, 255)"],"border-block-end-color":["rgb(204, 211, 255)","rgb(207, 213, 255)"],"border-block-start-color":["rgb(204, ` vs replica `{}`
- `div.sSKx7K5` active: original `{"color":["rgb(204, 211, 255)","rgb(207, 213, 255)"],"border-block-end-color":["rgb(204, 211, 255)","rgb(207, 213, 255)"],"border-block-start-color":["rgb(204, ` vs replica `{}`
- `span.s__49ESpn.smGGlF_.swbumPU` active: original `{"color":["rgb(204, 211, 255)","rgb(205, 212, 255)"],"border-block-end-color":["rgb(204, 211, 255)","rgb(205, 212, 255)"],"border-block-start-color":["rgb(204, ` vs replica `{}`

### Interaction states replayed in the replica

| State | Kind | Trigger | Opened | Roots found | Elements differing in style | Boxes off >2 px | Settle ms (orig / replica) | Closed |
|---|---|---|---|---|---|---|---|---|
| s1 | listbox | `Department` | yes | 1/1 | 10 of 40 | 40 | 95.1 / 162.3 | yes |
| s2 | popover | `Cookie Settings` | NO (nothing opened for s2) | 0/1 | 0 of 0 | 0 | 147.6 / n/a | n/a |

Examples of state style differences:

- s1 `background-color`: `rgb(255, 245, 240)` vs `rgb(255, 255, 255)`
- s1 `bottom`: `-247px` vs `-244px`
- s1 `inset-block-end`: `-247px` vs `-244px`
- s1 `font-family`: `wfont_a3f637_3f0d4ffb6bdc4c1cb6dc005c9dadbf65, wf_3f0d4ffb6bdc4c1cb6dc005c9, orig_inter_regular` vs `wfont_57a328_056b0e780fbb4e609d5cfb92039e33d9, wf_056b0e780fbb4e609d5cfb920, orig_inter_18_pt_light`

## Interaction states

| State | Kind | Trigger (action) | Parent | Appear ms | Settle ms | Exit ms | Closed by | Motion |
|---|---|---|---|---|---|---|---|---|
| s1 | listbox | `Department` (click) |  | 9.1 | 95.1 | 13.6 | Escape | none detected |
| s2 | popover | `Cookie Settings` (click) |  | 7.9 | 147.6 | n/a | outside-click | none detected |

Attempts without a captured state: 1 navigated, 4 not-actionable, 8 nothing-appeared. Native `<select>` and date inputs open a browser-drawn popup that is not in the page and cannot be captured.

Blocked while interacting (page tried to write): `POST https://px.ads.linkedin.com/wa/`, `POST https://analytics.google.com/g/collect`, `POST https://tools.versance.ai/api/sync`, `POST https://frog.wix.com/`, `POST https://d.adroll.com/onp/EY4X5P6LURGFFAWV464EIM/VG73ZOREDJERFPBHZ6J67Z`, `POST https://www.google.com/g/collect`

## Redaction

Rules: 0 selectors, 0 patterns, 0 literals; links: keep.

No replacements were needed.

Full list (location and replacement, never the original) in `redaction-report.json`. Redaction is pattern-based: review the pull request for personal data it did not recognise.

## Design tokens

See `tokens.draft.css` (exact values measured from computed styles; names are placeholders).

Color: 17 | Font: 52 | Radius: 7 | Shadow: 5 | Spacing: 30 | Motion: 9 | Layers: 3

## Not captured / limits

- 4 iframes found: their contents are not captured (the boxes are kept)
- 156 non-GET request(s) were blocked while interacting (the page tried to write data); popups that need them may be incomplete
- Page scripts are not kept: behaviour other than the recorded popup states (sorting, typing, validation, data loading) is not reproduced.
- Popup contents are static snapshots: a calendar shows the month that was open, a menu the items it had.
