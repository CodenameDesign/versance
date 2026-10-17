# Versance Coworker — style v8: workspace

Workspace: cream canvas, orange-red and blue. Light only. Based on the Replit references (four images).

**Files in this folder**

- `tokens.css` — the design variables this style uses (colour, type, radius, spacing, elevation, motion).
- `components.css` — the base component rules, driven by the tokens.
- `specimen.html` — the style rendered live from its real components.
- `view-design-system.html`, `view-tokens.html`, `view-components.html` — readable pages for this document and the two CSS files, each with a Back arrow (generated from them by `../tools/viewers.py`).
- `../screens/screens.css` — this style's overrides on top of the tokens and components; `../screens/*.html` are the 8 pages that hold the 19 screens (use the "All screens" list in the top-left).

**Lineage:** v5's structure, re-coloured and re-shaped from the Replit references.

## 1. Identity

- **Canvas:** warm cream `#F7F6F3` with a dot grid (`#DAD7CF`, 20px) on the page; the panel is a soft rounded card (22px) with a diffuse shadow; inner cards are white, 12–16px radius, hairline `#EFEDE7` borders.
- **Orange-red `#F5400C`** (like "Get started" / "Create Account"): primary buttons (hover `#D93500`), the count badge, and the logo mark on a pale orange tile.
- **Blue `#0079F2`:** send button (8px radius, pale grey when empty, like the reference's arrow), toggle ON, text-field focus border, links (underlined), focus ring.
- **Light-blue info cards** (like "Invite a friend, earn $20"): intro tiles, help cards, the "How it works" panel and empty-state cards use `#E3EEFD` fill, `#CFE0F8` border, `#0B4FA8` text, with a blue × to dismiss.
- **Segmented toggle:** grey track `#EFEDE8` with a white active pill and a soft shadow (Design | Build); the active rail tile is light blue like the reference's "Draw" mode.
- **Chips/tags:** warm-grey rounded chips (`#F1EFEA`); `chtag` blue / orange tints; risk badges tinted red / amber.
- **Composer:** white rounded card, tools row `+ @ /`, small blue send, joined to a warm strip holding Web Search + Export.

## 2. Colours

Measured from the 19 rendered screens: every fill, text, icon, line and gradient stop that appears. The token column names the variable that holds that value, or says the style sets it directly. Colours used on only 1–2 elements are left out as minor tints.

**Surfaces and fills**

| Colour | Token | Used on |
|---|---|---|
| `#FFFFFF` | `--accent-on`, `--bg`, `--panel` | 388 elements |
| `#D9DDE5` | set directly in this style | 67 elements |
| `#F1EFEA` | `--hover` | 62 elements |
| `#F7F6F3` | set directly in this style | 55 elements |
| `#E3EEFD` | set directly in this style | 33 elements |
| `#EFEDE8` | set directly in this style | 20 elements |
| `#FFE8DF` | set directly in this style | 19 elements |
| `#CFCBC1` | set directly in this style | 11 elements |
| `#FFE9A8` | set directly in this style | 3 elements |

**Text and icons**

| Colour | Token | Used on |
|---|---|---|
| `#3A3935` | set directly in this style | 520 elements |
| `#1E1D1B` | `--ink` | 438 elements |
| `#6A6862` | `--muted` | 414 elements |
| `#B3B0A8` | set directly in this style | 97 elements |
| `#0063C7` | `--accent-hover` | 83 elements |
| `#0B4FA8` | `--text-info`, `--text-selected` | 69 elements |
| `#F5400C` | set directly in this style | 34 elements |
| `#000000` | set directly in this style | 18 elements |
| `#0079F2` | `--accent` | 18 elements |
| `#9B9890` | `--faint` | 12 elements |
| `#B33000` | set directly in this style | 7 elements |

**Lines and outlines**

| Colour | Token | Used on |
|---|---|---|
| `#EFEDE7` | `--line-soft` | 128 elements |
| `#E6E3DC` | `--line` | 60 elements |
| `#CFE0F8` | set directly in this style | 12 elements |
| `#E0DDD5` | set directly in this style | 9 elements |
| `#FBD3C5` | set directly in this style | 7 elements |
| `#BFD7F7` | set directly in this style | 3 elements |

**Gradient stops**

| Colour | Token | Used on |
|---|---|---|
| `#DAD7CF` | set directly in this style | 19 elements |

**Interaction-state colours** (hover, pressed, focus, disabled; not visible in the static screens)

| Token | Value |
|---|---|
| `--accent-pressed` | `#0050A3` |
| `--accent-tint-25` | `#BCD9F8` |
| `--accent-tint-8` | `#EEF5FD` |
| `--amber-tint` | `#F4E4B8` |
| `--green-tint` | `#CFE0DE` |

**Not rendered:** 21 further colour variables in `tokens.css` (`--accent-grad`, `--accent-grad-diag`, `--accent-wash`, `--amber-grad`, `--amber-ink`, `--coral-grad`, `--exception-dark`, `--green-grad`, `--mark`, `--pane`, `--soft-wash`, `--tag-filing`, `--tag-news`, `--tag-transcript`, `--tag-web`, `--teal-grad`, `--teal-ink`, `--teal-tint`, `--violet-grad`, `--violet-ink`, `--violet-tint`) are carried over from earlier styles. They are still referenced by base rules that this style overrides, so they are kept in the file under "Carried over", but none appears on a screen.

## 3. Type

Families: **Inter**. Sizes below are the rendered values on the 19 screens.

| Role | Family | Size | Weight | Tracking | Case |
|---|---|---|---|---|---|
| Display ("Hi,") | Inter | 32px | 600 | -0.96px | — |
| Lead | Inter | 18px | 500 | -0.18px | — |
| Pane title | Inter | 16px | 600 | -0.24px | — |
| Report title | Inter | 24px | 600 | -0.6px | — |
| Finding title | Inter | 14px | 600 | — | — |
| Body | Inter | 14px | 400 | — | — |
| Header bar | Inter | 14px | 500 | — | uppercase |
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
| Panel | 22px | 1px | yes | — |
| Chat card | 16px | 1px | yes | — |
| Composer | 16px | 1px | yes | — |
| Cards | 12px | 1px | none | — |
| Intro tile | 12px | 1px | yes | — |
| Header bar | 12px | 1px | none | — |
| Buttons | 8px | 1px | none | — |
| Chips | 10px | 1px | none | — |
| Text fields | 10px | 1px | none | — |
| Toggle | 999px | 0px none | none | — |
| Rail tiles | 10px | 0px none | none | — |
| Send button | 8px | 0px none | none | — |
| Tags | 6px | 0px none | none | — |

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
- **Focus:** buttons and other clickable controls take `2px solid #0079F2` with a 2px offset and keep their own radius; text fields show no ring, only their 1px border changes colour; the composer container adds nothing.
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
