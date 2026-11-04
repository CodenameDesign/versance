# Capture report: https://www.versance.ai/

Captured 2026-11-04T05:09:12.870Z with page-capture 0.1.0 (148.0.7778.96) in 211 s. Widths measured: 1440, 1024, 768, 390 px.

## Summary

- Elements captured: 1299
- Stylesheets: 34; CSS rules written: 2753; unused font subsets skipped: 236
- Files in assets/: 38; downloads that failed: 0
- Interaction states captured: 3 (1 listbox, 2 dialog); attempts that showed nothing: 13
- Hover/focus/active: 39 element signatures probed, 36 change on a pseudo-state
- Draft tokens: 123
- Redaction: 0 replacements; leak check searched 0 original values in all text outputs and found 0

## Fidelity: replica vs original

Both are loaded in the same browser; the original is measured live (already redacted), the replica from its own files with every external request blocked.

| Width | Elements compared | With style differences | Properties different | Boxes off by >0.75 px | Pixels different | Page height (orig / replica) |
|---|---|---|---|---|---|---|
| 1440 | 1102 | 15 (1.36%) | 80 of 22705 | 232 | 21982 (0.2544%) | 6465 / 6459 |
| 1024 | 1102 | 15 (1.36%) | 80 of 22706 | 232 | 19073 (0.3104%) | 6465 / 6459 |
| 768 | 1102 | 15 (1.36%) | 80 of 22592 | 232 | 15367 (0.3335%) | 6465 / 6459 |
| 390 | 1102 | 18 (1.63%) | 109 of 22641 | 244 | 49506 (2.1156%) | 6465 / 6459 |

### Differences at 1440 px

- `grid-template-rows`: 7 elements; e.g. `162px 0px 5780.81px 521.797px` vs `162px 0px 5774.81px 521.797px`
- `border-block-end-style`: 4 elements; e.g. `solid` vs `(default)`
- `border-block-end-width`: 4 elements; e.g. `1px` vs `(default)`
- `border-block-start-style`: 4 elements; e.g. `solid` vs `(default)`
- `border-block-start-width`: 4 elements; e.g. `1px` vs `(default)`
- `border-bottom-style`: 4 elements; e.g. `solid` vs `(default)`
- `border-bottom-width`: 4 elements; e.g. `1px` vs `(default)`
- `border-inline-end-style`: 4 elements; e.g. `solid` vs `(default)`
- box `div` original [0,0,1440,6464.61] vs replica [0,0,1440,6458.61]
- box `div.main_MF` original [0,0,1440,6464.61] vs replica [0,0,1440,6458.61]
- box `div._7xVID.pageBackground_k2rwv` original [0,0,1440,6464.61] vs replica [0,0,1440,6458.61]

### Differences at 1024 px

- `grid-template-rows`: 7 elements; e.g. `162px 0px 5780.81px 521.797px` vs `162px 0px 5774.81px 521.797px`
- `border-block-end-style`: 4 elements; e.g. `solid` vs `(default)`
- `border-block-end-width`: 4 elements; e.g. `1px` vs `(default)`
- `border-block-start-style`: 4 elements; e.g. `solid` vs `(default)`
- `border-block-start-width`: 4 elements; e.g. `1px` vs `(default)`
- `border-bottom-style`: 4 elements; e.g. `solid` vs `(default)`
- `border-bottom-width`: 4 elements; e.g. `1px` vs `(default)`
- `border-inline-end-style`: 4 elements; e.g. `solid` vs `(default)`
- box `div` original [0,0,1024,6464.61] vs replica [0,0,1024,6458.61]
- box `div.main_MF` original [0,0,1024,6464.61] vs replica [0,0,1024,6458.61]
- box `div._7xVID.pageBackground_k2rwv` original [0,0,1024,6464.61] vs replica [0,0,1024,6458.61]

### Differences at 768 px

- `grid-template-rows`: 7 elements; e.g. `162px 0px 5780.81px 521.797px` vs `162px 0px 5774.81px 521.797px`
- `border-block-end-style`: 4 elements; e.g. `solid` vs `(default)`
- `border-block-end-width`: 4 elements; e.g. `1px` vs `(default)`
- `border-block-start-style`: 4 elements; e.g. `solid` vs `(default)`
- `border-block-start-width`: 4 elements; e.g. `1px` vs `(default)`
- `border-bottom-style`: 4 elements; e.g. `solid` vs `(default)`
- `border-bottom-width`: 4 elements; e.g. `1px` vs `(default)`
- `border-inline-end-style`: 4 elements; e.g. `solid` vs `(default)`
- box `div` original [0,0,768,6464.61] vs replica [0,0,768,6458.61]
- box `div.main_MF` original [0,0,768,6464.61] vs replica [0,0,768,6458.61]
- box `div._7xVID.pageBackground_k2rwv` original [0,0,980,6464.61] vs replica [0,0,980,6458.61]

### Differences at 390 px

- `grid-template-rows`: 7 elements; e.g. `162px 0px 5780.81px 521.797px` vs `162px 0px 5774.81px 521.797px`
- `border-block-end-style`: 4 elements; e.g. `solid` vs `(default)`
- `border-block-end-width`: 4 elements; e.g. `1px` vs `(default)`
- `border-block-start-style`: 4 elements; e.g. `solid` vs `(default)`
- `border-block-start-width`: 4 elements; e.g. `1px` vs `(default)`
- `border-bottom-style`: 4 elements; e.g. `solid` vs `(default)`
- `border-bottom-width`: 4 elements; e.g. `1px` vs `(default)`
- `border-inline-end-style`: 4 elements; e.g. `solid` vs `(default)`
- box `div` original [0,0,390,6464.61] vs replica [0,0,390,6458.61]
- box `div.main_MF` original [0,0,390,6464.61] vs replica [0,0,390,6458.61]
- box `div._7xVID.pageBackground_k2rwv` original [0,0,980,6464.61] vs replica [0,0,980,6458.61]

### Offline and errors

- External requests the replica tried to make (all blocked): 0
- Failed local requests (404 etc.): 0
- Page errors in the replica: 0

### Hover, focus, active

Same forced pseudo-states applied to both: 74 state(s) with a change compared, 72 identical, 2 different.

- `span.s__5CjnXs.se5p61l` active: original `{"color":["rgb(204, 211, 255)","rgb(205, 212, 255)"],"border-block-end-color":["rgb(204, 211, 255)","rgb(205, 212, 255)"],"border-block-start-color":["rgb(204, ` vs replica `{}`
- `span.s__49ESpn.smGGlF_.swbumPU` active: original `{}` vs replica `{"color":["rgb(204, 211, 255)","rgb(205, 212, 255)"],"border-block-end-color":["rgb(204, 211, 255)","rgb(205, 212, 255)"],"border-block-start-color":["rgb(204, `

### Interaction states replayed in the replica

| State | Kind | Trigger | Opened | Roots found | Elements differing in style | Boxes off >2 px | Settle ms (orig / replica) | Closed |
|---|---|---|---|---|---|---|---|---|
| s1 | listbox | `Department` | yes | 1/1 | 0 of 40 | 40 | 52.6 / 113.7 | yes |
| s2 | dialog | `Cookie Settings` | yes | 1/1 | 13 of 58 | 5 | 47.9 / 39.2 | yes |
| s3 | dialog | `Accept` | yes | 1/1 | 13 of 58 | 5 | 46.5 / 31.1 | yes |

Examples of state style differences:

- s2 `font-family`: `HelveticaNeue, "Helvetica Neue", helvetica, Sans-Serif` vs `HelveticaNeue, "Helvetica Neue", helvetica, sans-serif`
- s2 `font-family`: `HelveticaNeue, "Helvetica Neue", helvetica, Sans-Serif` vs `HelveticaNeue, "Helvetica Neue", helvetica, sans-serif`
- s2 `font-family`: `HelveticaNeue, "Helvetica Neue", helvetica, Sans-Serif` vs `HelveticaNeue, "Helvetica Neue", helvetica, sans-serif`
- s2 `inset-inline-end`: `1px` vs `25px`
- s3 `font-family`: `HelveticaNeue, "Helvetica Neue", helvetica, Sans-Serif` vs `HelveticaNeue, "Helvetica Neue", helvetica, sans-serif`
- s3 `font-family`: `HelveticaNeue, "Helvetica Neue", helvetica, Sans-Serif` vs `HelveticaNeue, "Helvetica Neue", helvetica, sans-serif`

## Interaction states

| State | Kind | Trigger (action) | Parent | Appear ms | Settle ms | Exit ms | Closed by | Motion |
|---|---|---|---|---|---|---|---|---|
| s1 | listbox | `Department` (click) |  | 7.1 | 52.6 | 12.2 | Escape | none detected |
| s2 | dialog | `Cookie Settings` (click) |  | 6.1 | 47.9 | 12.8 | Escape | none detected |
| s3 | dialog | `Accept` (click) |  | 8.8 | 46.5 | 12.5 | Escape | none detected |

Attempts without a captured state: 2 navigated, 13 nothing-appeared, 2 not-actionable. Native `<select>` and date inputs open a browser-drawn popup that is not in the page and cannot be captured.

Blocked while interacting (page tried to write): `POST https://px.ads.linkedin.com/wa/`, `POST https://frog.wix.com/`, `POST https://analytics.google.com/g/collect`, `POST https://sentry-next.wixpress.com/api/68/envelope/`, `POST https://d.adroll.com/onp/EY4X5P6LURGFFAWV464EIM/VG73ZOREDJERFPBHZ6J67Z`, `POST https://tools.versance.ai/api/sync`

## Redaction

Rules: 0 selectors, 2 patterns, 0 literals; links: keep.

No replacements were needed.

Full list (location and replacement, never the original) in `redaction-report.json`. Redaction is pattern-based: review the pull request for personal data it did not recognise.

## Design tokens

See `tokens.draft.css` (exact values measured from computed styles; names are placeholders).

Color: 17 | Font: 52 | Radius: 7 | Shadow: 5 | Spacing: 30 | Motion: 9 | Layers: 3

## Not captured / limits

- 4 iframes found: their contents are not captured (the boxes are kept)
- 2 element(s) a script had added to the <head> (tracking pixels, for instance) were left out: the original never shows them, and in the replica they would sit in the page and push it down
- 185 non-GET request(s) were blocked while interacting (the page tried to write data); popups that need them may be incomplete
- Page scripts are not kept: behaviour other than the recorded popup states (sorting, typing, validation, data loading) is not reproduced.
- Popup contents are static snapshots: a calendar shows the month that was open, a menu the items it had.
