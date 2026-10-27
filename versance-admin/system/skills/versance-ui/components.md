# Components

Specs for the Versance admin components. Each lists the values; build with the tokens in `design-tokens.md`.

## Admin shell

Dark left nav with the Versance logo and pill items, and a content area. Collapses to a top bar below 720px, where the menu opens inside the header and pushes the page down.

| Property | Value |
| --- | --- |
| Sidebar | fill var(--color-ink), width var(--sidebar-width) (the web app's 230px), sticky and full height; logo 160px wide, padding 24px |
| Item | pill (var(--radius-pill)), 13px / 600, padding 7.5px 12px, 12px side margin, hover white at 12%, 120ms |
| Active item | white at 18% fill; no side bar |
| Main | padding var(--page-padding), white on the Public and System pages |
| Mobile | at 720px the sidebar becomes a 64px top bar; the arrow button opens the menu inside the header |

```css
.side{width:var(--sidebar-width);background:var(--color-ink);color:var(--color-surface)}
.side nav a{margin:0 12px 4px;padding:7.5px 12px;border-radius:var(--radius-pill);font:600 var(--font-size-nav)/var(--line-height-nav) var(--font-family)}
```

## Buttons

Extension buttons: 8px radius, 14px text. One primary, an outline for secondary actions, a near-black pill.

| Property | Value |
| --- | --- |
| Base | padding var(--pad-btn), 1px var(--color-border) border, radius var(--radius-sm), var(--font-size-md); hover border and text var(--color-primary), 120ms |
| Primary (.p) | fill var(--color-primary), white text; hover var(--color-primary-hover); pressed var(--color-primary-dark) |
| Primary disabled | fill var(--color-primary-tint-25), white text, not-allowed |
| Outline (.o) | var(--color-primary) text, 1px var(--color-primary-tint-25) border; disabled tints lighter |
| Dark pill (.dark) | fill var(--color-ink), white text, radius var(--radius-pill): the one deliberate non-indigo control (Web Search On) |
| Tile button | var(--color-surface-alt) fill, no border, full width (Upload a document) |
| Focus | var(--focus-ring) with a 2px offset on every button, link and role=button |

```css
.btn{display:inline-flex;align-items:center;gap:6px;padding:var(--pad-btn);border:1px solid var(--color-border);border-radius:var(--radius-sm);transition:border-color var(--duration-fast),color var(--duration-fast)}
.btn:hover{border-color:var(--color-primary);color:var(--color-primary)}
.btn.p{background:var(--color-primary);border-color:var(--color-primary);color:#fff}
.btn.p:hover{background:var(--color-primary-hover)}
```

## Pills and tabs

Pill-shaped chips and tabs. Selected state is the pale indigo tint.

| Property | Value |
| --- | --- |
| Pill | padding var(--pad-pill), radius var(--radius-pill), var(--color-surface-alt) fill, var(--color-text-muted) text; hover var(--color-border) fill and black text |
| Selected pill | var(--color-primary-tint-15) fill, var(--color-primary) text, weight 600 |
| Tab strip | 4px padding, #E6E6E6 fill, radius var(--radius-box); tab padding 4px 12px, pill radius; active tab white with black text |
| Web app pill (.cpill.on) | var(--color-success-bg) fill and var(--color-success-text) text, 12.5px |

```css
.cpill{display:inline-flex;gap:7px;padding:var(--pad-pill);border-radius:var(--radius-pill);background:var(--color-surface-alt);color:var(--color-text-muted)}
.cpill.is-selected{background:var(--color-primary-tint-15);color:var(--color-primary);font-weight:600}
```

## Toggle and send

The 26 x 15 toggle and the round send button.

| Property | Value |
| --- | --- |
| Toggle | 26 x 15px, radius var(--radius-pill), var(--color-border) off, var(--color-primary) on; 11px white knob, 2px inset, 180ms; the web app's on colour is var(--color-success) |
| Send | 36px circle, var(--color-primary) fill, white icon; hover var(--color-primary-hover); disabled var(--color-primary-tint-25) until there is content |
| Web app send | var(--color-success-bg) fill with var(--color-success-text) icon; hover fills var(--color-success) with white |

```css
.tog{width:26px;height:15px;border-radius:var(--radius-pill);background:var(--color-border)}
.tog.on{background:var(--color-primary)}
.send-btn{width:36px;height:36px;border-radius:50%;background:var(--color-primary);color:#fff}
```

## Fields

Text input and select: 10px radius, 1px border that turns indigo on focus (no ring).

| Property | Value |
| --- | --- |
| Field | padding 10px 14px, 1px var(--color-border) border, radius var(--radius-box), white; placeholder var(--color-text-faint) italic |
| Focus | border var(--color-primary) only: no outline, no offset |
| Select | padding 12px 14px, same border and radius; keeps the focus ring |

```css
.field{width:100%;padding:10px 14px;border:1px solid var(--color-border);border-radius:var(--radius-box)}
.field:focus{border-color:var(--color-primary);outline:none}
```

## Icon rail

The extension's vertical rail of 30px icon buttons, with a count badge.

| Property | Value |
| --- | --- |
| Rail | var(--rail-width) wide, 10px gap, centred |
| Button | 30px, radius var(--radius-box), white; hover var(--color-primary-tint-8); active var(--color-primary) fill with white icon |
| Badge | 14px minimum, var(--color-primary) fill, white 9px / 700, top-right; on the active button it inverts (white fill, indigo text) |

```css
.rail-btn{width:30px;height:30px;border-radius:var(--radius-box)}
.rail-btn.active{background:var(--color-primary);color:#fff}
```

## Pane, tile and card

Surfaces in the extension: the grey tool pane, dismissible tiles and bordered cards.

| Property | Value |
| --- | --- |
| Pane | var(--color-page-bg) (#F9F9F9) |
| Tile | var(--color-surface-alt) fill, radius var(--radius-panel), padding 16px 40px 16px 16px; a 20px round close button top right (indigo, hover var(--color-primary-tint-15)) |
| Info tile | white with a 1px var(--color-surface-alt) border |
| Card | white, 1px var(--color-border) border, radius var(--radius-panel), padding 12px 14px |
| Web app card | var(--color-surface-alt) fill, radius 16px, padding 18px 20px, 13px / 600 muted heading |

```css
.card{background:var(--color-surface);border:1px solid var(--color-border);border-radius:var(--radius-panel);padding:12px 14px}
```

## Source tags and severity

Small solid tags for the source of an answer, and uppercase severity pills.

| Property | Value |
| --- | --- |
| Source tag | 10px / 700, letter-spacing .4px, white on colour, padding 3px 8px, radius var(--radius-tag) |
| Colours | filing var(--color-primary) (the web app uses var(--color-tag-filing-app)), transcript var(--color-tag-transcript), web var(--color-text-muted), news var(--color-amber) |
| Severity | 12px / 700 uppercase, letter-spacing .02em, white on colour, padding 4px 10px, pill; High var(--color-danger), Medium var(--color-warning) |
| Low risk | no style is defined: no reference design shows one |

```css
.tg{font:700 10px var(--font-family);letter-spacing:.4px;padding:3px 8px;border-radius:var(--radius-tag);color:#fff}
.risk{font:700 12px var(--font-family);text-transform:uppercase;padding:4px 10px;border-radius:var(--radius-pill);color:#fff}
```

## Citation, rows and info text

The inline citation chip, document rows and the indigo help text.

| Property | Value |
| --- | --- |
| Citation | 16px minimum, var(--color-primary-tint-15) fill, var(--color-primary) 10px / 700, radius var(--radius-cite) |
| Doc row | padding 10px 4px, 1px var(--color-surface-alt) divider; hover var(--color-primary-tint-8); date in var(--color-text-muted), tabular numbers |
| Info text | var(--color-primary); title 18px / 700 (line 1.25), sub-heads 14px / 700 |
| Link | var(--color-primary), underlined; hover var(--color-primary-hover) |

```css
.cite{min-width:16px;height:16px;padding:0 4px;background:var(--color-primary-tint-15);color:var(--color-primary);border-radius:var(--radius-cite);font:700 10px var(--font-family)}
```

## Web app sidebar

The web app's white sidebar: the New button and the pill nav items (these are the web app's own values, not the admin's).

| Property | Value |
| --- | --- |
| Sidebar | 230px wide, var(--color-surface), padding 20px, hairline var(--color-border) on the right |
| New button | pill, var(--color-surface-alt) fill, 13px / 500, a 20px black round plus icon; hover var(--color-border) |
| Nav button | pill, 14px, var(--color-text-muted); hover var(--color-surface-alt) and black; 6px gap between items |
| Active | var(--app-nav-active) (#C7E2F0) fill, black text, weight 600 |

```css
.navbtn{display:flex;gap:9px;padding:7.5px 10px;border-radius:999px;color:var(--color-text-muted)}
.navbtn.active{background:var(--app-nav-active);color:#000;font-weight:600}
```

## Web app composer

The web app's message box: 20px radius, mono text, pill row below.

| Property | Value |
| --- | --- |
| Box | white, 1px var(--color-border) border, radius 20px, var(--shadow), padding 16px 16px 13px |
| Text | var(--font-family-mono) 15px / 1.55, placeholder var(--color-text-faint) |
| Send | 36px circle bottom right, var(--color-success-bg) fill, var(--color-success-text) icon |

```css
.composer{background:#fff;border:1px solid var(--color-border);border-radius:20px;box-shadow:var(--shadow);padding:16px 16px 13px}
```

## Icon link

The admin's quiet action: a text link with an 18px icon, no fill or border.

| Property | Value |
| --- | --- |
| Text | var(--font-size-md) / 600, var(--color-primary), no underline at rest |
| Icon | 18px Material icon in currentColor, 4px from the text |
| Hover | var(--color-primary-hover) with a 2px-offset underline, 150ms |
| Focus | 2px outline var(--color-primary) |
| Where | versance-admin/admin/admin.css (.ilink) |

```css
.ilink{display:inline-flex;align-items:center;gap:var(--space-1);color:var(--color-primary);font:600 var(--font-size-md)/var(--line-height-md) var(--font-family)}
.ilink:hover{color:var(--color-primary-hover);text-decoration:underline;text-underline-offset:2px}
```

## List table with developer row

The Public page list: group heading rows, one row per page, a twisty that opens the route, source files and spec link.

| Property | Value |
| --- | --- |
| Head cell | 11px / 600 uppercase, letter-spacing .04em, 1px var(--color-surface-alt) rule |
| Body cell | 14px / 21px, padding 8px, 51px rows |
| Group row | bold 14px heading with a 20px chevron that folds the group's rows; the count sits at the right |
| Developer box | var(--color-page-bg), 1px var(--color-border), radius var(--radius-sm), padding 16px |

```css
table{border-collapse:collapse;width:100%}
th{font:600 var(--font-size-thead)/var(--line-height-thead) var(--font-family);text-transform:uppercase;letter-spacing:.04em}
td{padding:8px;font-size:var(--font-size-table);border-bottom:1px solid var(--color-surface-alt)}
```
