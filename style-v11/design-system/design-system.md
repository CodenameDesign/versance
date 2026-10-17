# Versance Coworker — style v11: data

Data: forest, mint and lime, notched cards, dark / light. Based on the Spade references (five images).

**Files in this folder**

- `tokens.css` — the design variables this style uses (colour, type, radius, spacing, elevation, motion).
- `components.css` — the base component rules, driven by the tokens.
- `specimen.html` — the style rendered live from its real components (with the dark / light button).
- `view-design-system.html`, `view-tokens.html`, `view-components.html` — readable pages for this document and the two CSS files, each with a Back arrow (generated from them by `../tools/viewers.py`).
- `../screens/screens.css` — this style's overrides on top of the tokens and components; `../screens/*.html` are the 8 pages that hold the 19 screens (use the "All screens" list in the top-left).

**Lineage:** v9's structure (dark / light toggle, mono labels), re-coloured from the Spade references.

## 1. Identity

- **Palette:** deep forest `#17301F`, mint `#C4EAC6`, **lime `#B4F26B`** (the single bright accent: active rail tile, toggle ON, send, primary buttons, `NEW CHAT` tag, alphabet pick, icon chips, highlighter), pale-green paper `#F3F8EC` / `#FBFDF8`, hairline `#D3E2CA`, ink `#14210F`. Dark mode: page `#121D14`, panel `#18281B`, cards `#1D3022`, text `#E4F2DC`; lime stays.
- **Shapes:** chamfered panel corners (24px, 1px line); **corner-notch triangles** (7px) on every card, like the stat cards; sharp card corners; pale-green grid lines (68px) on the page behind the panel.
- **Labels:** IBM Plex Mono uppercase, with a **▸** marker on the header, section labels, citation lines, tags, and the `NEW CHAT / NEW REPORT` tag (mono heads on the help panel too).
- **Header:** forest bar with mint mono text, lime `▸` and a lime `EDIT` tag.
- **Help panel:** forest screen with lime mono sub-heads (like the dark "Analytics & AI" section).
- **Buttons/tags:** primary = lime with dark text (like "Send offers"), hover = forest; tags are forest chips with mint text; risk badges: High = orange-peach, Medium = yellow, both with a dark border.
- **Type:** Inter with very tight headline tracking (-0.045em), "Hi," 46px, report title 30px.
- **Toggle:** same as v9 — sun / moon button above the avatar, remembered between pages, `?theme=dark` to force.

## 2. Colours

Measured from the 19 rendered screens: every fill, text, icon, line and gradient stop that appears. The token column names the variable that holds that value, or says the style sets it directly. Colours used on only 1–2 elements are left out as minor tints.

### Light theme

**Surfaces and fills**

| Colour | Token | Used on |
|---|---|---|
| `#FFFFFF` | `--card`, `--risk-on` | 307 elements |
| `#B4F26B` | `--accent`, `--orange` | 131 elements |
| `#17301F` | `--inv-bg` | 99 elements |
| `#D9DDE5` | set directly in this style | 67 elements |
| `#E9F2E0` | `--fill` | 55 elements |
| `#F3F8EC` | `--bg` | 30 elements |
| `#FBFDF8` | `--panel` | 19 elements |
| `#D7F59A` | set directly in this style | 3 elements |

**Text and icons**

| Colour | Token | Used on |
|---|---|---|
| `#14210F` | `--ink`, `--strong` | 1697 elements |
| `#55694F` | `--muted` | 165 elements |
| `#8CA085` | `--faint` | 83 elements |
| `#C4EAC6` | `--inv-ink` | 57 elements |
| `#000000` | set directly in this style | 18 elements |
| `#DDEFD9` | set directly in this style | 5 elements |

**Lines and outlines**

| Colour | Token | Used on |
|---|---|---|
| `#D3E2CA` | `--line` | 291 elements |
| `#A9BFA0` | `--dotline` | 18 elements |

**Gradient stops**

| Colour | Token | Used on |
|---|---|---|
| `#DCE9D2` | `--dots` | 38 elements |

### Dark theme

**Surfaces and fills**

| Colour | Token | Used on |
|---|---|---|
| `#1D3022` | `--card` | 302 elements |
| `#B4F26B` | `--accent`, `--orange` | 126 elements |
| `#D9DDE5` | set directly in this style | 67 elements |
| `#C4EAC6` | `--inv-bg` | 64 elements |
| `#223A28` | `--fill` | 55 elements |
| `#121D14` | `--bg` | 30 elements |
| `#18281B` | `--panel` | 19 elements |
| `#27472F` | set directly in this style | 17 elements |
| `#17301F` | set directly in this style | 6 elements |
| `#FFFFFF` | `--risk-on` | 5 elements |

**Text and icons**

| Colour | Token | Used on |
|---|---|---|
| `#E4F2DC` | `--ink` | 1264 elements |
| `#14210F` | `--inv-ink` | 270 elements |
| `#A4BBA0` | `--muted` | 165 elements |
| `#7A927A` | `--faint` | 83 elements |
| `#000000` | set directly in this style | 18 elements |
| `#DDEFD9` | set directly in this style | 5 elements |

**Lines and outlines**

| Colour | Token | Used on |
|---|---|---|
| `#2E4934` | `--line` | 292 elements |
| `#4A6B50` | `--dotline` | 18 elements |
| `#3B6B47` | set directly in this style | 17 elements |

**Gradient stops**

| Colour | Token | Used on |
|---|---|---|
| `#CFE8C5` | `--strong` | 202 elements |
| `#213427` | `--dots` | 38 elements |

**Interaction-state colours** (hover, pressed, focus, disabled; not visible in the static screens)

| Token | Value |
|---|---|
| `--accent-hover` | `#9ED55E` |
| `--accent-on` | `#111111` |
| `--accent-pressed` | `#89B851` |
| `--accent-tint-15` | `#F4FDE9` |
| `--accent-tint-25` | `#ECFCDA` |
| `--accent-tint-8` | `#F9FEF3` |
| `--amber-tint` | `#F4E4B8` |
| `--green-tint` | `#CFE0DE` |

**Not rendered:** 27 further colour variables in `tokens.css` (`--accent-grad`, `--accent-grad-diag`, `--accent-wash`, `--amber-grad`, `--amber-ink`, `--coral-grad`, `--exception-dark`, `--green-grad`, `--hover`, `--line-soft`, `--mark`, `--pane`, `--risk-high`, `--risk-medium`, `--soft-wash`, `--tag-filing`, `--tag-news`, `--tag-transcript`, `--tag-web`, `--teal-grad`, `--teal-ink`, `--teal-tint`, `--text-info`, `--text-selected`, `--violet-grad`, `--violet-ink`, `--violet-tint`) are carried over from earlier styles. They are still referenced by base rules that this style overrides, so they are kept in the file under "Carried over", but none appears on a screen.

## 3. Type

Families: **IBM Plex Mono**, **Inter**. Sizes below are the rendered values on the 19 screens.

| Role | Family | Size | Weight | Tracking | Case |
|---|---|---|---|---|---|
| Display ("Hi,") | Inter | 46px | 500 | -2.07px | — |
| Lead | Inter | 18px | 500 | -0.81px | — |
| Pane title | Inter | 18px | 500 | -0.81px | — |
| Report title | Inter | 30px | 500 | -1.35px | — |
| Finding title | Inter | 14px | 600 | — | — |
| Body | Inter | 14px | 400 | — | — |
| Header bar | IBM Plex Mono | 12px | 500 | 0.72px | uppercase |
| Section label | IBM Plex Mono | 11px | 400 | 0.66px | uppercase |
| Meta / dates | IBM Plex Mono | 12px | 400 | — | — |
| Chip | IBM Plex Mono | 12px | 400 | 0.24px | uppercase |
| Tab | Inter | 14px | 400 | — | — |
| Button | Inter | 14px | 400 | — | — |
| Link | IBM Plex Mono | 12.5px | 400 | — | — |
| Tag | IBM Plex Mono | 11px | 400 | 0.44px | uppercase |
| Risk badge | IBM Plex Mono | 11px | 700 | 0.55px | uppercase |

## 4. Shape, depth and glass

| Component | Radius | Border | Shadow | Backdrop blur |
|---|---|---|---|---|
| Panel | 0px | 1px | none | — |
| Chat card | 0px | 1px | none | — |
| Composer | 0px | 1px | none | — |
| Cards | 0px | 1px | none | — |
| Intro tile | 0px | 1px | none | — |
| Header bar | 0px | 1px | none | — |
| Buttons | 0px | 1px | none | — |
| Chips | 0px | 1px | none | — |
| Text fields | 0px | 1px | none | — |
| Toggle | 0px | 1px | none | — |
| Rail tiles | 0px | 1px | none | — |
| Send button | 50% | 0px none | none | — |
| Tags | 0px | 1px | none | — |

## 5. Layout

- **Panel:** docked to the right of the browser window, full window height inside a 16px margin; **440px** wide on the compact (Coworker home) screens and **799px** on the expanded screens (chat column + tool pane).
- **Icon rail (right edge):** eight items, top to bottom: **Home**, Research context (with count badge), My filings, CAD library, US library, Compliance, Output Centre, History. Icon-only tiles. The gap between the content and the rail is 22.5px.
- **Composer:** text field on top, a tools row (`+`, `@`, `/`) below with the round send button at the right; Web Search and Export Conversation in a row below.
- **Chat column tabs:** `Coworker` (alone, or beside `Filings` / `Compliance Review`) with a `new chat` / `new report` tag at the right.
- **Header:** company bar at the top of the chat column (name + `edit`, or a search field with `EXIT` while switching); the collapse button sits top-right of the panel.
- **Footer of the tool pane:** "Open Versance.ai" with the logo tile; the user avatar and the dark / light button sit at the bottom-right of the panel.

## 6. Behaviour rules (all 19 screens)

- **Home:** the Home button is the first rail item, above Research context, and is highlighted on the four Coworker home screens (101a–101b). There is no forward-arrow button.
- **Help `?`:** shown on a pane title except while that pane's own help card is open (201b, 501aa, 601a, 701a).
- **Right-pane header spacing:** title → first block 16px; title → italic sub-line 4px and sub-line → first block 16px; title → back link 8px and back link → first block 16px.
- **Close ×:** a dismiss × on intro tiles, help cards and the help panel; a remove × on source cards and the reviewed-source chip.
- **Links:** every text link is underlined, 14px; the back links (Switch companies, Exit document) are underlined too; `Clear all` / `Clear` are the quiet grey link.
- **Message box:** a real text input. The send button is disabled until there is text; Enter or the button sends and clears the field; whitespace alone does not enable it.
- **Focus:** buttons and other clickable controls take `2px solid #B4F26B` with a 2px offset and keep their own radius; text fields show no ring, only their 1px border changes colour; the composer container adds nothing.
- **Motion:** hover and press transitions only; nothing animates on page load.
- **Navigation in the HTML pages:** the "All screens" list (top-left) and, in every style except v1, the `‹ n ›` style switcher (bottom-left). Both are neutral and identical in every style.
- **Dark / light:** the sun / moon button above the avatar sets `data-theme` on `<html>`, is remembered in `localStorage` and can be forced with `?theme=dark`.

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
