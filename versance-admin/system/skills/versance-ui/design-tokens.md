# Design tokens

Named values for the Versance interface, based on the web app (versance.html) and the extension style-v1. Use the token, never the raw value.

## Colour

| Colour | Token | Hex / value | RGB | Use |
| --- | --- | --- | --- | --- |
| Text | `--color-text` | `#000000` | R0 G0 B0 | body text (--ink) |
| Text muted | `--color-text-muted` | `#65728e` | R101 G114 B142 | labels, captions (--muted) |
| Text faint | `--color-text-faint` | `#8d96aa` | R141 G150 B170 | placeholders, disabled text (--faint) |
| Primary | `--color-primary` | `#324efe` | R50 G78 B254 | the one accent (--accent): links, active states, primary buttons, focus |
| Primary hover | `--color-primary-hover` | `#2c45e0` | R44 G69 B224 | primary hover (--accent-hover) |
| Primary dark | `--color-primary-dark` | `#263bc1` | R38 G59 B193 | primary pressed (--accent-pressed) |
| Primary tint 8 | `--color-primary-tint-8` | `#eff1ff` | R239 G241 B255 | hover on rows and rail buttons (--accent-tint-8) |
| Primary tint 15 | `--color-primary-tint-15` | `#e0e4ff` | R224 G228 B255 | selected pill, citation chip (--accent-tint-15) |
| Primary tint 25 | `--color-primary-tint-25` | `#ccd3ff` | R204 G211 B255 | disabled primary button, low-emphasis outlines (--accent-tint-25) |
| Ink | `--color-ink` | `#0a1922` | R10 G25 B34 | near-black: the admin sidebar and the dark pill button (--exception-dark) |
| Ink soft | `--color-ink-soft` | `#0d2030` | R13 G32 B48 | hover on the dark sidebar (the web app's dark-theme sidebar) |
| Surface | `--color-surface` | `#ffffff` | R255 G255 B255 | cards, menus, inputs (--panel, --bg) |
| Page bg | `--color-page-bg` | `#f9f9f9` | R249 G249 B249 | page tint, code boxes, tool pane (--pane) |
| Surface alt | `--color-surface-alt` | `#f3f5f9` | R243 G245 B249 | chips, tiles, hover fills (--hover) |
| Border | `--color-border` | `#d9dde5` | R217 G221 B229 | borders and rules (--line) |
| Link underline | `--color-link-underline` | `rgba(50, 78, 254, 0.4)` |  | underline on admin links |
| Success | `--color-success` | `#5ac47e` | R90 G196 B126 | the web app's green (--accent, --green): toggle on, "ask" actions |
| Success bg | `--color-success-bg` | `#def3e5` | R222 G243 B229 | pale green fill (--accent-bg) |
| Success text | `--color-success-text` | `#1c6b38` | R28 G107 B56 | text on the pale green (--accent-text) |
| Danger | `--color-danger` | `#dc2927` | R220 G41 B39 | high severity (--risk-high) |
| Warning | `--color-warning` | `#f59d0a` | R245 G157 B10 | medium severity (--risk-medium) |
| Amber | `--color-amber` | `#e2b43d` | R226 G180 B61 | news tag, "create" actions (--tag-news, --amber) |
| Tag filing app | `--color-tag-filing-app` | `#2b40c5` | R43 G64 B197 | filing tag in the web app (--col-filing) |
| Tag transcript | `--color-tag-transcript` | `#ea5b5b` | R234 G91 B91 | transcript tag (--tag-transcript, .tg.transcript) |
| Nav active | `--app-nav-active` | `#c7e2f0` | R199 G226 B240 | active sidebar item fill (.navbtn.active) |
| Accent dark | `--app-accent-dark` | `#3da865` | R61 G168 B101 | accent hover (--accent-d) |
| Dark line | `--app-dark-line` | `#1a3040` | R26 G48 B64 | dark theme borders |
| Dark hover | `--app-dark-hover` | `#152838` | R21 G40 B56 | dark theme hover and chips |
| Dark accent bg | `--app-dark-accent-bg` | `#0d2a18` | R13 G42 B24 | dark theme selected fill |
| Source transcript | `--app-source-transcript` | `#334efe` | R51 G78 B254 | the web app's transcript source colour (--col-transcript), one digit from the extension's indigo |
| Dark accent text | `--app-dark-accent-text` | `#7dd498` | R125 G212 B152 | dark theme accent text |

## Typography

Family `"Figtree", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`; mono `"Roboto Mono", monospace`.

| Token | Size / line height | Weight | Use |
| --- | --- | --- | --- |
| `--font-size-title` | 28px / 34px | 700 | Page title (the web app hero) |
| `--font-size-lg` | 18px / 22.5px | 700 | Help title in the extension |
| `--font-size-md` | 14px / 21px | 400 | Body text, table text |
| `--font-size-nav` | 13px / 20px | 600 | Sidebar items in the admin |
| `--font-size-thead` | 11px / 16px | 600 | Table head: uppercase, letter-spaced |
| `--font-size-caption` | 12px / 18px | 400 | Captions, code badges |

## Shape and elevation

| Token | Value | Use |
| --- | --- | --- |
| `--radius-cite` | 4px | Citation chip |
| `--radius-tag` | 6px | Source tags |
| `--radius-sm` | 8px | Buttons, small cards |
| `--radius-box` | 10px | Inputs, tab strip, rail buttons |
| `--radius-panel` | 12px | Cards and tiles |
| `--radius-pill` | 999px | Pills, tabs, sidebar items, toggles |
| `--radius-round` | 50% | Icon buttons, send button |
| `--shadow-sm` | 0 1px 2px rgba(0, 0, 0, 0.05), 0 3px 10px rgba(0, 0, 0, 0.06) | Resting card in the web app |
| `--shadow` | 0 1px 3px rgba(0, 0, 0, 0.06), 0 6px 20px rgba(0, 0, 0, 0.08) | Composer, menus and popovers |
| `--shadow-lg` | 0 16px 40px rgba(10, 25, 34, 0.3) | Dialogs and the System menu drawer (ours) |

## All tokens

Generated from `tokens.css`, so it is always complete.

| Token | Value | Use | Source |
| --- | --- | --- | --- |
| `--color-text` | `#000000` | body text (--ink) | Web app and extension |
| `--color-text-muted` | `#65728e` | labels, captions (--muted) | Web app and extension |
| `--color-text-faint` | `#8d96aa` | placeholders, disabled text (--faint) | Web app and extension |
| `--color-primary` | `#324efe` | the one accent (--accent): links, active states, primary buttons, focus | Extension style-v1 |
| `--color-primary-hover` | `#2c45e0` | primary hover (--accent-hover) | Extension style-v1 |
| `--color-primary-dark` | `#263bc1` | primary pressed (--accent-pressed) | Extension style-v1 |
| `--color-primary-tint-8` | `#eff1ff` | hover on rows and rail buttons (--accent-tint-8) | Extension style-v1 |
| `--color-primary-tint-15` | `#e0e4ff` | selected pill, citation chip (--accent-tint-15) | Extension style-v1 |
| `--color-primary-tint-25` | `#ccd3ff` | disabled primary button, low-emphasis outlines (--accent-tint-25) | Extension style-v1 |
| `--color-ink` | `#0a1922` | near-black: the admin sidebar and the dark pill button (--exception-dark) | Web app and extension |
| `--color-ink-soft` | `#0d2030` | hover on the dark sidebar (the web app's dark-theme sidebar) | Web app |
| `--color-surface` | `#ffffff` | cards, menus, inputs (--panel, --bg) | Web app and extension |
| `--color-page-bg` | `#f9f9f9` | page tint, code boxes, tool pane (--pane) | Extension style-v1 |
| `--color-surface-alt` | `#f3f5f9` | chips, tiles, hover fills (--hover) | Web app and extension |
| `--color-border` | `#d9dde5` | borders and rules (--line) | Web app and extension |
| `--color-link-underline` | `rgba(50, 78, 254, 0.4)` | underline on admin links | Ours (admin tool) |
| `--color-success` | `#5ac47e` | the web app's green (--accent, --green): toggle on, "ask" actions | Web app |
| `--color-success-bg` | `#def3e5` | pale green fill (--accent-bg) | Web app |
| `--color-success-text` | `#1c6b38` | text on the pale green (--accent-text) | Web app |
| `--color-danger` | `#dc2927` | high severity (--risk-high) | Extension style-v1 |
| `--color-warning` | `#f59d0a` | medium severity (--risk-medium) | Extension style-v1 |
| `--color-amber` | `#e2b43d` | news tag, "create" actions (--tag-news, --amber) | Web app and extension |
| `--color-tag-filing-app` | `#2b40c5` | filing tag in the web app (--col-filing) | Web app |
| `--color-tag-transcript` | `#ea5b5b` | transcript tag (--tag-transcript, .tg.transcript) | Web app and extension |
| `--app-nav-active` | `#c7e2f0` | active sidebar item fill (.navbtn.active) | Web app |
| `--app-accent-dark` | `#3da865` | accent hover (--accent-d) | Web app |
| `--app-dark-line` | `#1a3040` | dark theme borders | Web app |
| `--app-dark-hover` | `#152838` | dark theme hover and chips | Web app |
| `--app-dark-accent-bg` | `#0d2a18` | dark theme selected fill | Web app |
| `--app-source-transcript` | `#334efe` | the web app's transcript source colour (--col-transcript), one digit from the extension's indigo | Web app |
| `--app-dark-accent-text` | `#7dd498` | dark theme accent text | Web app |
| `--font-family` | `"Figtree", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif` | the typeface of the web app and the extension | Web app and extension |
| `--font-family-mono` | `"Roboto Mono", monospace` | the web app composer and code | Web app |
| `--letter-spacing` | `0` | the web app sets none (the hero title uses -0.5px) | Web app |
| `--font-size-md` | `14px` | body text (--fs-body) | Extension style-v1 |
| `--line-height-md` | `21px` | body line height (--lh-body 1.5) | Extension style-v1 |
| `--font-size-lg` | `18px` | help title (--fs-help-h1) | Extension style-v1 |
| `--line-height-lg` | `22.5px` | help title line height (1.25) | Extension style-v1 |
| `--font-size-title` | `28px` | page title (.hero h1) | Web app |
| `--line-height-title` | `34px` | page title line height | Ours (admin tool) |
| `--font-weight-title` | `700` | page title weight | Web app |
| `--font-size-table` | `14px` | table text (--fs-body) | Extension style-v1 |
| `--line-height-table` | `21px` | table line height | Extension style-v1 |
| `--font-size-nav` | `13px` | sidebar item text (.new-btn 13px) | Web app |
| `--line-height-nav` | `20px` | sidebar item line height | Ours (admin tool) |
| `--font-size-thead` | `11px` | table head, uppercase caps (--fs-caps) | Extension style-v1 |
| `--line-height-thead` | `16px` | table head line height | Ours (admin tool) |
| `--font-size-caption` | `12px` | captions, code badges (--fs-small) | Extension style-v1 |
| `--line-height-caption` | `18px` | caption line height | Ours (admin tool) |
| `--font-weight-regular` | `400` | body (--fw-regular) | Extension style-v1 |
| `--font-weight-semibold` | `600` | pane titles, selected pills (--fw-semibold) | Extension style-v1 |
| `--font-weight-bold` | `700` | buttons, tags, nav (--fw-bold) | Extension style-v1 |
| `--line-height-body` | `1.5` | unitless body line height (--lh-body) | Extension style-v1 |
| `--font-weight-thead` | `600` | table head | Extension style-v1 |
| `--radius-cite` | `4px` | citation chip (--r-cite) | Extension style-v1 |
| `--radius-tag` | `6px` | source tags (--r-tag) | Extension style-v1 |
| `--radius-sm` | `8px` | buttons, small cards (--r-btn) | Extension style-v1 |
| `--radius-box` | `10px` | inputs, tab strip (--r-box) | Extension style-v1 |
| `--radius-panel` | `12px` | cards and tiles (--r-panel) | Extension style-v1 |
| `--radius-pill` | `999px` | pills, tabs, sidebar items, toggles | Web app and extension |
| `--radius-round` | `50%` | icon buttons, send button, dots | Extension style-v1 |
| `--space-1` | `4px` | admin scale | Ours (admin tool) |
| `--space-2` | `8px` | admin scale | Ours (admin tool) |
| `--space-3` | `12px` | admin scale | Ours (admin tool) |
| `--space-4` | `16px` | admin scale | Ours (admin tool) |
| `--space-5` | `20px` | web app sidebar padding | Web app |
| `--space-6` | `24px` | admin scale | Ours (admin tool) |
| `--space-8` | `32px` | admin scale | Ours (admin tool) |
| `--pad-btn` | `7px 13px` | button padding (--pad-btn) | Extension style-v1 |
| `--pad-pill` | `6px 12px` | pill padding (--pad-pill) | Extension style-v1 |
| `--page-padding` | `40px` | main area padding | Ours (admin tool) |
| `--card-padding` | `24px` | card padding | Ours (admin tool) |
| `--shadow-sm` | `0 1px 2px rgba(0, 0, 0, 0.05), 0 3px 10px rgba(0, 0, 0, 0.06)` | resting card (--shadow-sm) | Web app |
| `--shadow` | `0 1px 3px rgba(0, 0, 0, 0.06), 0 6px 20px rgba(0, 0, 0, 0.08)` | composer, menus, popovers (--shadow) | Web app |
| `--shadow-sm-dark` | `0 1px 2px rgba(0, 0, 0, 0.3), 0 3px 10px rgba(0, 0, 0, 0.4)` | resting card in the web app dark theme | Web app |
| `--shadow-dark` | `0 1px 3px rgba(0, 0, 0, 0.35), 0 6px 20px rgba(0, 0, 0, 0.5)` | composer and menus in the web app dark theme | Web app |
| `--shadow-lg` | `0 16px 40px rgba(10, 25, 34, 0.3)` | dialogs and the System menu drawer | Ours (admin tool) |
| `--duration-hover` | `0.15s` | colour fades (--dur) | Extension style-v1 |
| `--duration-fast` | `0.12s` | button and nav hover (--dur-fast) | Extension style-v1 |
| `--duration-menu-item` | `0.15s` | same as hover | Extension style-v1 |
| `--ease-standard` | `ease` | transition timing | Ours (admin tool) |
| `--focus-ring` | `2px solid #324efe` | keyboard focus on buttons and links, with a 2px offset (--focus-ring) | Extension style-v1 |
| `--sidebar-width` | `230px` | the web app sidebar width (.sidebar) | Web app |
| `--rail-width` | `40px` | the extension icon rail (--rail-w) | Extension style-v1 |
| `--content-max-width` | `1200px` | admin content width | Ours (admin tool) |

## CSS

```css
/* Versance design tokens: based on the web app (versance.html) and the browser-extension design style-v1 (browser-extension/style-v1/design-system/tokens.css).
   THE ONE SET OF VERSANCE TOKENS. Every other place that carries token values is generated from this file (python3 tools/build_system.py):
   style-v1's tokens.css and the :root blocks of versance.html and edgar/versance.html (through design-tokens/map.json), tokens.json, DESIGN-TOKENS.md, the AI files, the skill's tokens.css and the System pages. Edit values here only.
   Each value is defined once, under one name (no aliases); the web app's and the extension's own names for it are in design-tokens/map.json. Styles v2 to v13 and medicus-01.html are separate design examples with their own CSS and are not part of this set.
   One token per line with its use as the trailing comment.
   Source tag at the start of each comment (tools/audit.py checks [app], [ext] and [both] values against the source files):
     [both] the same value is in versance.html and in style-v1
     [ext]  from style-v1 (the extension: indigo accent, 14px body)
     [app]  from the web app versance.html (:root, white sidebar, green accent)
     [ours] chosen for the admin tool; neither source defines it */
:root {
  /* Color: text */
  --color-text: #000000;                     /* [both] body text (--ink) */
  --color-text-muted: #65728e;               /* [both] labels, captions (--muted) */
  --color-text-faint: #8d96aa;               /* [both] placeholders, disabled text (--faint) */

  /* Color: brand (extension indigo) */
  --color-primary: #324efe;                  /* [ext] the one accent (--accent): links, active states, primary buttons, focus */
  --color-primary-hover: #2c45e0;            /* [ext] primary hover (--accent-hover) */
  --color-primary-dark: #263bc1;             /* [ext] primary pressed (--accent-pressed) */
  --color-primary-tint-8: #eff1ff;           /* [ext] hover on rows and rail buttons (--accent-tint-8) */
  --color-primary-tint-15: #e0e4ff;          /* [ext] selected pill, citation chip (--accent-tint-15) */
  --color-primary-tint-25: #ccd3ff;          /* [ext] disabled primary button, low-emphasis outlines (--accent-tint-25) */

  /* Color: surfaces and lines */
  --color-ink: #0a1922;                      /* [both] near-black: the admin sidebar and the dark pill button (--exception-dark) */
  --color-ink-soft: #0d2030;                 /* [app] hover on the dark sidebar (the web app's dark-theme sidebar) */
  --color-surface: #ffffff;                  /* [both] cards, menus, inputs (--panel, --bg) */
  --color-page-bg: #f9f9f9;                  /* [ext] page tint, code boxes, tool pane (--pane) */
  --color-surface-alt: #f3f5f9;              /* [both] chips, tiles, hover fills (--hover) */
  --color-border: #d9dde5;                   /* [both] borders and rules (--line) */
  --color-link-underline: rgba(50, 78, 254, 0.4); /* [ours] underline on admin links */

  /* Color: status */
  --color-success: #5ac47e;                  /* [app] the web app's green (--accent, --green): toggle on, "ask" actions */
  --color-success-bg: #def3e5;               /* [app] pale green fill (--accent-bg) */
  --color-success-text: #1c6b38;             /* [app] text on the pale green (--accent-text) */
  --color-danger: #dc2927;                   /* [ext] high severity (--risk-high) */
  --color-warning: #f59d0a;                  /* [ext] medium severity (--risk-medium) */
  --color-amber: #e2b43d;                    /* [both] news tag, "create" actions (--tag-news, --amber) */

  /* Color: source tags */
  --color-tag-filing-app: #2b40c5;           /* [app] filing tag in the web app (--col-filing) */
  --color-tag-transcript: #ea5b5b;           /* [both] transcript tag (--tag-transcript, .tg.transcript) */

  /* Color: web app (versance.html) */
  --app-nav-active: #c7e2f0;                 /* [app] active sidebar item fill (.navbtn.active) */
  --app-accent-dark: #3da865;                /* [app] accent hover (--accent-d) */

  /* Color: web app dark theme (reference only: the admin is light) */
  --app-dark-line: #1a3040;                  /* [app] dark theme borders */
  --app-dark-hover: #152838;                 /* [app] dark theme hover and chips */
  --app-dark-accent-bg: #0d2a18;             /* [app] dark theme selected fill */
  --app-source-transcript: #334efe;          /* [app] the web app's transcript source colour (--col-transcript), one digit from the extension's indigo */
  --app-dark-accent-text: #7dd498;           /* [app] dark theme accent text */

  /* Typography */
  --font-family: "Figtree", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; /* [both] the typeface of the web app and the extension */
  --font-family-mono: "Roboto Mono", monospace; /* [app] the web app composer and code */
  --letter-spacing: 0;                       /* [app] the web app sets none (the hero title uses -0.5px) */
  --font-size-md: 14px;                      /* [ext] body text (--fs-body) */
  --line-height-md: 21px;                    /* [ext] body line height (--lh-body 1.5) */
  --font-size-lg: 18px;                      /* [ext] help title (--fs-help-h1) */
  --line-height-lg: 22.5px;                  /* [ext] help title line height (1.25) */
  --font-size-title: 28px;                   /* [app] page title (.hero h1) */
  --line-height-title: 34px;                 /* [ours] page title line height */
  --font-weight-title: 700;                  /* [app] page title weight */
  --font-size-table: 14px;                   /* [ext] table text (--fs-body) */
  --line-height-table: 21px;                 /* [ext] table line height */
  --font-size-nav: 13px;                     /* [app] sidebar item text (.new-btn 13px) */
  --line-height-nav: 20px;                   /* [ours] sidebar item line height */
  --font-size-thead: 11px;                   /* [ext] table head, uppercase caps (--fs-caps) */
  --line-height-thead: 16px;                 /* [ours] table head line height */
  --font-size-caption: 12px;                 /* [ext] captions, code badges (--fs-small) */
  --line-height-caption: 18px;               /* [ours] caption line height */
  --font-weight-regular: 400;                /* [ext] body (--fw-regular) */
  --font-weight-semibold: 600;               /* [ext] pane titles, selected pills (--fw-semibold) */
  --font-weight-bold: 700;                   /* [ext] buttons, tags, nav (--fw-bold) */
  --line-height-body: 1.5;                   /* [ext] unitless body line height (--lh-body) */
  --font-weight-thead: 600;                  /* [ext] table head */

  /* Radius */
  --radius-cite: 4px;                        /* [ext] citation chip (--r-cite) */
  --radius-tag: 6px;                         /* [ext] source tags (--r-tag) */
  --radius-sm: 8px;                          /* [ext] buttons, small cards (--r-btn) */
  --radius-box: 10px;                        /* [ext] inputs, tab strip (--r-box) */
  --radius-panel: 12px;                      /* [ext] cards and tiles (--r-panel) */
  --radius-pill: 999px;                      /* [both] pills, tabs, sidebar items, toggles */
  --radius-round: 50%;                       /* [ext] icon buttons, send button, dots */

  /* Spacing */
  --space-1: 4px;                            /* [ours] admin scale */
  --space-2: 8px;                            /* [ours] admin scale */
  --space-3: 12px;                           /* [ours] admin scale */
  --space-4: 16px;                           /* [ours] admin scale */
  --space-5: 20px;                           /* [app] web app sidebar padding */
  --space-6: 24px;                           /* [ours] admin scale */
  --space-8: 32px;                           /* [ours] admin scale */
  --pad-btn: 7px 13px;                       /* [ext] button padding (--pad-btn) */
  --pad-pill: 6px 12px;                      /* [ext] pill padding (--pad-pill) */
  --page-padding: 40px;                      /* [ours] main area padding */
  --card-padding: 24px;                      /* [ours] card padding */

  /* Elevation */
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05), 0 3px 10px rgba(0, 0, 0, 0.06); /* [app] resting card (--shadow-sm) */
  --shadow: 0 1px 3px rgba(0, 0, 0, 0.06), 0 6px 20px rgba(0, 0, 0, 0.08); /* [app] composer, menus, popovers (--shadow) */
  --shadow-sm-dark: 0 1px 2px rgba(0, 0, 0, 0.3), 0 3px 10px rgba(0, 0, 0, 0.4); /* [app] resting card in the web app dark theme */
  --shadow-dark: 0 1px 3px rgba(0, 0, 0, 0.35), 0 6px 20px rgba(0, 0, 0, 0.5); /* [app] composer and menus in the web app dark theme */
  --shadow-lg: 0 16px 40px rgba(10, 25, 34, 0.3); /* [ours] dialogs and the System menu drawer */

  /* Motion */
  --duration-hover: 0.15s;                   /* [ext] colour fades (--dur) */
  --duration-fast: 0.12s;                    /* [ext] button and nav hover (--dur-fast) */
  --duration-menu-item: 0.15s;               /* [ext] same as hover */
  --ease-standard: ease;                     /* [ours] transition timing */
  --focus-ring: 2px solid var(--color-primary); /* [ext] keyboard focus on buttons and links, with a 2px offset (--focus-ring) */

  /* Layout */
  --sidebar-width: 230px;                    /* [app] the web app sidebar width (.sidebar) */
  --rail-width: 40px;                        /* [ext] the extension icon rail (--rail-w) */
  --content-max-width: 1200px;               /* [ours] admin content width */
}
```
