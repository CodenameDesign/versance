# Versance Coworker — style v7: dashboard

Dashboard: white surfaces, hairlines, green accent, mono labels. Light only. Based on the Supabase dashboard reference.

**Files in this folder**

- `tokens.css` — the design variables this style uses (colour, type, radius, spacing, elevation, motion).
- `components.css` — the base component rules, driven by the tokens.
- `specimen.html` — the style rendered live from its real components.
- `view-design-system.html`, `view-tokens.html`, `view-components.html` — readable pages for this document and the two CSS files, each with a Back arrow (generated from them by `../tools/viewers.py`).
- `../screens/screens.css` — this style's overrides on top of the tokens and components; `../screens/*.html` are the 8 pages that hold the 19 screens (use the "All screens" list in the top-left).

**Lineage:** v6's structure (hairlines, mono labels), re-skinned from the Supabase dashboard reference.

## 1. Identity

- **Surfaces:** white panel and cards, 1px `#E6E6E6` borders, no shadows; small radii (panel 12px, cards 8px, buttons/inputs/tabs 6px, tags 4px, status pills fully round); dotted backdrop (`#D9D9D9` dots on a 20px grid, page only).
- **Colour:** ink `#171717`; muted `#6B6B6B`; **Supabase green `#3ECF8E`** is the single accent: toggle ON, send button, count badge, link underlines, focus ring, `NEW CHAT`/`NEW REPORT` tag (`#E3F8EE` fill, `#9BE3C3` border, `#0B6B45` text), highlighter tint `#D5F5E7`, logo tile. Primary buttons are green-tinted like "Connect" (`#BFEEDA` fill, `#3ECF8E` border, dark-green text; solid green on hover).
- **Labels and tags:** JetBrains Mono, uppercase, tracked — EDIT, NEW CHAT, section headers ("SOURCES IN THIS CONVERSATION"), citation lines, dates; outlined tags like FREE / PRODUCTION / NANO; risk badges are outlined tinted pills (red / amber).
- **Tiles:** intro icon chips are bordered white icon tiles (36px, 8px radius), like the dashboard's STATUS / COMPUTE tiles. Active rail tile = green-tinted with a green border.
- **Web Search On** stays near-black `#171717`; Off is an outlined white button.
- Inter text; hover/press motion only; typeable input; 24px rail gap (22.5px measured with borders); title spacing rule; success state and low-risk badge still undefined.

## 2. Colours

Measured from the 19 rendered screens: every fill, text, icon, line and gradient stop that appears. The token column names the variable that holds that value, or says the style sets it directly. Colours used on only 1–2 elements are left out as minor tints.

**Surfaces and fills**

| Colour | Token | Used on |
|---|---|---|
| `#FFFFFF` | `--bg`, `--pane`, `--panel` | 413 elements |
| `#D9DDE5` | set directly in this style | 67 elements |
| `#3ECF8E` | `--accent` | 42 elements |
| `#E3F8EE` | `--green-tint` | 34 elements |
| `#FCFCFC` | set directly in this style | 19 elements |
| `#FAFAFA` | set directly in this style | 19 elements |
| `#F5F5F5` | `--hover` | 19 elements |
| `#F0F0F0` | set directly in this style | 17 elements |
| `#D5F5E7` | `--accent-tint-15` | 4 elements |

**Text and icons**

| Colour | Token | Used on |
|---|---|---|
| `#171717` | `--ink`, `--text-info` | 1079 elements |
| `#6B6B6B` | `--muted` | 379 elements |
| `#B0B0B0` | set directly in this style | 100 elements |
| `#0B6B45` | `--text-selected` | 91 elements |
| `#000000` | set directly in this style | 18 elements |
| `#0B3D2A` | `--accent-on` | 16 elements |
| `#4A4A4A` | set directly in this style | 16 elements |
| `#A15C00` | `--amber-ink` | 10 elements |
| `#9A9A9A` | `--faint` | 9 elements |
| `#B42318` | set directly in this style | 3 elements |

**Lines and outlines**

| Colour | Token | Used on |
|---|---|---|
| `#E6E6E6` | `--line` | 182 elements |
| `#D9D9D9` | set directly in this style | 48 elements |
| `#D0D0D0` | set directly in this style | 44 elements |
| `#EFEFEF` | `--line-soft` | 18 elements |
| `#9BE3C3` | set directly in this style | 17 elements |
| `#EAEAEA` | set directly in this style | 16 elements |

**Interaction-state colours** (hover, pressed, focus, disabled; not visible in the static screens)

| Token | Value |
|---|---|
| `--accent-hover` | `#2FBF7F` |
| `--accent-pressed` | `#1FA971` |
| `--accent-tint-8` | `#EEFBF5` |

**Not rendered:** 21 further colour variables in `tokens.css` (`--accent-grad`, `--accent-grad-diag`, `--accent-wash`, `--amber-grad`, `--coral-grad`, `--exception-dark`, `--green-grad`, `--mark`, `--risk-high`, `--risk-medium`, `--soft-wash`, `--tag-filing`, `--tag-news`, `--tag-transcript`, `--tag-web`, `--teal-grad`, `--teal-ink`, `--teal-tint`, `--violet-grad`, `--violet-ink`, `--violet-tint`) are carried over from earlier styles. They are still referenced by base rules that this style overrides, so they are kept in the file under "Carried over", but none appears on a screen.

## 3. Type

Families: **Inter**, **JetBrains Mono**. Sizes below are the rendered values on the 19 screens.

| Role | Family | Size | Weight | Tracking | Case |
|---|---|---|---|---|---|
| Display ("Hi,") | Inter | 36px | 500 | -1.26px | — |
| Lead | Inter | 18px | 500 | -0.18px | — |
| Pane title | Inter | 17px | 500 | -0.255px | — |
| Report title | Inter | 24px | 500 | -0.48px | — |
| Finding title | Inter | 14px | 600 | — | — |
| Body | Inter | 14px | 400 | — | — |
| Header bar | Inter | 14px | 500 | — | uppercase |
| Section label | JetBrains Mono | 11px | 400 | 0.88px | uppercase |
| Meta / dates | JetBrains Mono | 12px | 400 | — | — |
| Chip | Inter | 14px | 400 | — | — |
| Tab | Inter | 14px | 400 | — | — |
| Button | Inter | 14px | 400 | — | — |
| Link | Inter | 14px | 400 | — | — |
| Tag | JetBrains Mono | 11px | 400 | 0.55px | uppercase |
| Risk badge | JetBrains Mono | 11px | 700 | 0.55px | uppercase |

## 4. Shape, depth and glass

| Component | Radius | Border | Shadow | Backdrop blur |
|---|---|---|---|---|
| Panel | 12px | 1px | none | — |
| Chat card | 8px | 1px | none | — |
| Composer | 10px | 1px | none | — |
| Cards | 8px | 1px | none | — |
| Intro tile | 8px | 1px | none | — |
| Header bar | 8px | 1px | none | — |
| Buttons | 6px | 1px | none | — |
| Chips | 8px | 1px | none | — |
| Text fields | 6px | 1px | none | — |
| Toggle | 999px | 0px none | none | — |
| Rail tiles | 10px | 0px none | none | — |
| Send button | 6px | 0px none | none | — |
| Tags | 4px | 1px | none | — |

## 5. Layout

- **Panel:** docked to the right of the browser window, full window height inside a 16px margin; **440px** wide on the compact (Coworker home) screens and **799px** on the expanded screens (chat column + tool pane).
- **Icon rail (right edge):** eight items, top to bottom: **Home**, Research context (with count badge), My filings, CAD library, US library, Compliance, Output Centre, History. Icon-only tiles. The gap between the content and the rail is 22.5px.
- **Composer:** text field on top, a tools row (`+`, `@`, `/`) below with the round send button at the right; Web Search and Export Conversation in a row below.
- **Chat column tabs:** `Coworker` (alone, or beside `Filings` / `Compliance Review`) with a `new chat` / `new report` tag at the right.
- **Header:** company bar at the top of the chat column (name + `edit`, or a search field with `EXIT` while switching); the collapse button sits top-right of the panel.
- **Footer of the tool pane:** "Open Versance.ai" with the logo tile; the user avatar sit at the bottom-right of the panel.

## 6. Behaviour rules (all 19 screens)

- **Home:** the Home button is the first rail item, above Research context, and is highlighted on the four Coworker home screens (101a–101b). There is no forward-arrow button.
- **Help `?`:** shown on a pane title except while that pane's own help card is open (201b, 501aa, 601a, 701a).
- **Right-pane header spacing:** title → first block 16px; title → italic sub-line 4px and sub-line → first block 16px; title → back link 8px and back link → first block 16px.
- **Close ×:** a dismiss × on intro tiles, help cards and the help panel; a remove × on source cards and the reviewed-source chip.
- **Links:** every text link is underlined, 14px; the back links (Switch companies, Exit document) are underlined too; `Clear all` / `Clear` are the quiet grey link.
- **Message box:** a real text input. The send button is disabled until there is text; Enter or the button sends and clears the field; whitespace alone does not enable it.
- **Focus:** buttons and other clickable controls take `2px solid #3ECF8E` with a 2px offset and keep their own radius; text fields show no ring, only their 1px border changes colour; the composer container adds nothing.
- **Motion:** hover and press transitions only; nothing animates on page load.
- **Navigation in the HTML pages:** the "All screens" list (top-left) and, in every style except v1, the `‹ n ›` style switcher (bottom-left). Both are neutral and identical in every style.

## 7. Screens

| State | Screen | Contents |
|---|---|---|
| 101a | Coworker home (compact) | Welcome tile, three prompt chips, composer. |
| 101ab | Company switcher | Recent companies dropdown. |
| 101ac | Company switcher, searching | "Aar" typed; recent + all companies; `EXIT`. |
| 101b | How the Versance Coworker works | Four-step help panel. |
| 102a | Research context | Two toggles, Add a URL / Upload a Document, three source cards. |
| 102aa | Research context, Add a URL | Paste-a-link field with `ADD`; Cancel. |
| 102s | Research context, empty | "No documents added yet." empty state. |
| 201a | Primary Company Filings | Search + filter, filing list. |
| 201b | Primary Company Filings, help | Help card open (no `?`). |
| 401aa | Search Canadian Filings | Find a Company, A–Z, company list. |
| 401ab | Search <Company> Filings | Switch-companies link, filing list with hover action. |
| 411a | Filing viewer | Exit document, Add Document to Context, page preview, prompt chips. |
| 501aa | Compliance review, start | Welcome tile, two action buttons, how-it-works card. |
| 501ab | Compliance review, options | Reviewed source, Country / Regulation / Document Type, Run Report. |
| 501bb | Compliance report | Re-Run Report, Report Generated card, High / Medium findings. |
| 601a | Output Centre, empty | Info card, empty state. |
| 601b | Output Centre | Search + filter, seven report rows with tags. |
| 701a | Conversation History, empty | Info card, "You haven't had any conversations yet." |
| 701b | Conversation History | Search conversations, chat open on the left. |

The red annotation labels and leader lines in the reference designs were specs and never appear in the screens.

## 8. Content notes

- Company names in the mock data (Integra Resources, Australis Capital, Equinox Gold, South Railroad, Company A–C, Aardvark …) are placeholders; the switcher uses "Company Two" (the reference design had a typo).
- The 501ab reference annotation "new copy once you've selected a" is cut off in the reference design; only the visible copy is used.
- The empty History screen reads "You haven't had any conversations yet."
- No success state and no low-risk badge are defined: no reference shows one.
