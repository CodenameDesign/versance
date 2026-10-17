# Versance Coworker — style v10: notes

Notes: lime backdrop, olive accent, serif titles. Light only. Based on the Granola references (five images, including three AVIFs).

**Files in this folder**

- `tokens.css` — the design variables this style uses (colour, type, radius, spacing, elevation, motion).
- `components.css` — the base component rules, driven by the tokens.
- `specimen.html` — the style rendered live from its real components.
- `view-design-system.html`, `view-tokens.html`, `view-components.html` — readable pages for this document and the two CSS files, each with a Back arrow (generated from them by `../tools/viewers.py`).
- `../screens/screens.css` — this style's overrides on top of the tokens and components; `../screens/*.html` are the 8 pages that hold the 19 screens (use the "All screens" list in the top-left).

**Lineage:** v5's structure, re-coloured from the Granola references, with a serif.

## 1. Identity

- **Backdrop and surfaces:** pale-lime wash (`#B9C74F` with a soft light) behind a warm-paper panel (`#F6F6EF`, 26px radius, big soft shadow); inner chat card white, 20px radius; cards 18px; hairline `#ECEDE2` borders.
- **Type:** **Newsreader** (serif) for titles — "Hi," (44px), pane titles, report heading, finding titles, the company name — and Inter for all body text, buttons and lists, like the reference's serif note titles over a clean sans.
- **Colour:** ink `#24261C`; olive `#6F7F1E` (send, toggle ON, links, focus ring, input focus border); lime `#C9D45E` (active rail tile, logo tile, alphabet pick); lime tints `#EEF1D6` / `#E4EBBE` (icon squares, `new chat` tag, selected states, "Report generated" card); peach `#F8E3CB` accent for the second icon square; dark ink `#24261C` pills for primary buttons (like "Share") and Web Search On.
- **Shapes:** pill inputs, buttons, chips and tabs (999px); rounded icon squares (12px) tinted like "List actions / Write follow-up email".
- **Tabs:** warm track with a white active pill (like "Enhanced"); `new chat` is a lime-tint pill.
- **Composer:** white rounded card with `+ @ /` tools, round olive send (pale lime when empty) and a warm strip for Web Search + Export.

## 2. Colours

Measured from the 19 rendered screens: every fill, text, icon, line and gradient stop that appears. The token column names the variable that holds that value, or says the style sets it directly. Colours used on only 1–2 elements are left out as minor tints.

**Surfaces and fills**

| Colour | Token | Used on |
|---|---|---|
| `#FFFFFF` | `--accent-on`, `--bg`, `--panel` | 428 elements |
| `#D9DDE5` | set directly in this style | 67 elements |
| `#F6F6EF` | set directly in this style | 48 elements |
| `#EEF0DF` | set directly in this style | 38 elements |
| `#C9D45E` | set directly in this style | 38 elements |
| `#E4E6D2` | set directly in this style | 16 elements |
| `#EEEFE3` | set directly in this style | 15 elements |
| `#C8CCB4` | set directly in this style | 11 elements |
| `#6F7F1E` | `--accent` | 7 elements |
| `#D6D8C6` | set directly in this style | 7 elements |
| `#EEF1D6` | set directly in this style | 4 elements |
| `#F1F2E8` | `--hover` | 3 elements |
| `#E8F08A` | set directly in this style | 3 elements |

**Text and icons**

| Colour | Token | Used on |
|---|---|---|
| `#3A3D2B` | set directly in this style | 497 elements |
| `#24261C` | `--ink` | 466 elements |
| `#6E7060` | `--muted` | 430 elements |
| `#1F2A12` | set directly in this style | 92 elements |
| `#B1B3A3` | set directly in this style | 65 elements |
| `#586619` | `--accent-hover` | 51 elements |
| `#4B4E3B` | set directly in this style | 20 elements |
| `#000000` | set directly in this style | 18 elements |
| `#8A4A12` | set directly in this style | 13 elements |
| `#9A9C8B` | `--faint` | 12 elements |
| `#3E4A12` | `--text-info`, `--text-selected` | 7 elements |

**Lines and outlines**

| Colour | Token | Used on |
|---|---|---|
| `#ECEDE2` | set directly in this style | 61 elements |
| `#E4E5DA` | `--line` | 49 elements |
| `#EDEEE4` | `--line-soft` | 48 elements |
| `#DEE0D2` | set directly in this style | 20 elements |
| `#3C4614 @ 0.12` | set directly in this style | 19 elements |
| `#E8E9DC` | set directly in this style | 12 elements |

**Gradient stops**

| Colour | Token | Used on |
|---|---|---|
| `#FFFFFF @ 0.35` | set directly in this style | 19 elements |
| `#B9C74F` | set directly in this style | 19 elements |
| `#AFBE45` | set directly in this style | 19 elements |

**Interaction-state colours** (hover, pressed, focus, disabled; not visible in the static screens)

| Token | Value |
|---|---|
| `--accent-pressed` | `#455113` |
| `--accent-tint-15` | `#E4EBBE` |
| `--accent-tint-8` | `#F0F4DC` |
| `--amber-tint` | `#F4E4B8` |
| `--green-tint` | `#CFE0DE` |

**Not rendered:** 21 further colour variables in `tokens.css` (`--accent-grad`, `--accent-grad-diag`, `--accent-wash`, `--amber-grad`, `--amber-ink`, `--coral-grad`, `--exception-dark`, `--green-grad`, `--mark`, `--pane`, `--soft-wash`, `--tag-filing`, `--tag-news`, `--tag-transcript`, `--tag-web`, `--teal-grad`, `--teal-ink`, `--teal-tint`, `--violet-grad`, `--violet-ink`, `--violet-tint`) are carried over from earlier styles. They are still referenced by base rules that this style overrides, so they are kept in the file under "Carried over", but none appears on a screen.

## 3. Type

Families: **Inter**, **Newsreader**. Sizes below are the rendered values on the 19 screens.

| Role | Family | Size | Weight | Tracking | Case |
|---|---|---|---|---|---|
| Display ("Hi,") | Newsreader | 44px | 500 | -1.1px | — |
| Lead | Newsreader | 19px | 400 | -0.19px | — |
| Pane title | Newsreader | 20px | 500 | -0.2px | — |
| Report title | Newsreader | 28px | 500 | -0.56px | — |
| Finding title | Newsreader | 15.5px | 500 | — | — |
| Body | Inter | 14px | 400 | — | — |
| Header bar | Newsreader | 15px | 500 | 0.15px | uppercase |
| Section label | Inter | 14px | 400 | — | — |
| Meta / dates | Inter | 14px | 400 | — | — |
| Chip | Inter | 14px | 400 | — | — |
| Tab | Inter | 14px | 400 | — | — |
| Button | Inter | 14px | 400 | — | — |
| Link | Inter | 14px | 400 | — | — |
| Tag | Inter | 12px | 400 | — | — |
| Risk badge | Inter | 12px | 700 | 0.36px | uppercase |

## 4. Shape, depth and glass

| Component | Radius | Border | Shadow | Backdrop blur |
|---|---|---|---|---|
| Panel | 26px | 1px | yes | — |
| Chat card | 20px | 1px | yes | — |
| Composer | 22px | 1px | yes | — |
| Cards | 18px | 1px | none | — |
| Intro tile | 20px | 1px | yes | — |
| Header bar | 999px | 1px | yes | — |
| Buttons | 999px | 1px | none | — |
| Chips | 999px | 1px | none | — |
| Text fields | 999px | 1px | none | — |
| Toggle | 999px | 0px none | none | — |
| Rail tiles | 10px | 0px none | none | — |
| Send button | 50% | 0px none | none | — |
| Tags | 999px | 1px | none | — |

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
- **Focus:** buttons and other clickable controls take `2px solid #6F7F1E` with a 2px offset and keep their own radius; text fields show no ring, only their 1px border changes colour; the composer container adds nothing.
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
