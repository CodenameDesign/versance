# Versance Coworker — style v4: soft monochrome

Soft monochrome: Inter, near-black, deep-green toggle. Light only. Based on the soft-monochrome reference images.

**Files in this folder**

- `tokens.css` — the design variables this style uses (colour, type, radius, spacing, elevation, motion).
- `components.css` — the base component rules, driven by the tokens.
- `specimen.html` — the style rendered live from its real components.
- `view-design-system.html`, `view-tokens.html`, `view-components.html` — readable pages for this document and the two CSS files, each with a Back arrow (generated from them by `../tools/viewers.py`).
- `../screens/screens.css` — this style's overrides on top of the tokens and components; `../screens/*.html` are the 8 pages that hold the 19 screens (use the "All screens" list in the top-left).

**Lineage:** v3's structure, re-coloured from the soft-monochrome references, with a new composer and tabs.

## 1. Identity

- **Font:** Inter (the references are Inter). Switch back by changing `--font` in the v4 block of `screens/screens.css`.
- **Backdrop and cards:** cool-grey gradient backdrop; floating white cards with large diffuse shadows (`--sh-1/2/3`); 28px panel, 20px composer, 16px cards.
- **Colour:** near-black `#1C1C1E` replaces indigo for the primary button, active rail tile and send button; greys `#6E6E73` / `#9A9AA0` for secondary text; **deep green** (gradient `#17B27C` → `#08925F`) for toggle ON and the count badge; **yellow** `#FFF04D` highlighter (`<mark>`) for quoted phrases in compliance findings; risk badges keep their soft red/amber tint.
- **Tabs:** separate rounded tabs (outline = inactive, grey fill = active), not an outer pill.
- **Chips and tags:** grey pills with a hairline border; intro chips and type tags are all neutral grey.
- **Composer:** input on top; tools row `+  @  /` bottom-left; round send bottom-right (mid-grey when empty, near-black when there is text); Web Search and Export sit under the card.
- **Info text, links and × icons:** dark grey / ink, no blue. Links stay underlined.
- **Focus:** buttons 2px solid `#1C1C1E` ring with 2px offset; text fields change only their 1px border to `#1C1C1E`.

## 2. Colours

Measured from the 19 rendered screens: every fill, text, icon, line and gradient stop that appears. The token column names the variable that holds that value, or says the style sets it directly. Colours used on only 1–2 elements are left out as minor tints.

**Surfaces and fills**

| Colour | Token | Used on |
|---|---|---|
| `#FFFFFF` | `--accent-on`, `--bg`, `--panel` | 427 elements |
| `#F1F1F4` | `--hover` | 73 elements |
| `#D9DDE5` | set directly in this style | 67 elements |
| `#EBEBEF` | set directly in this style | 15 elements |
| `#F3F3F6` | set directly in this style | 7 elements |
| `#D3D3D8` | `--accent-tint-25` | 6 elements |
| `#E9F6F0` | set directly in this style | 5 elements |
| `#F4F4F7` | set directly in this style | 4 elements |
| `#EDEDF1` | set directly in this style | 4 elements |
| `#FFF04D` | `--mark` | 3 elements |

**Text and icons**

| Colour | Token | Used on |
|---|---|---|
| `#3A3A3C` | set directly in this style | 525 elements |
| `#1C1C1E` | `--accent`, `--ink`, `--text-selected` | 395 elements |
| `#6E6E73` | `--muted` | 281 elements |
| `#8E8E93` | set directly in this style | 153 elements |
| `#000000` | `--accent-hover`, `--accent-pressed` | 115 elements |
| `#B4B4BA` | set directly in this style | 82 elements |
| `#9A9AA0` | `--faint` | 71 elements |
| `#2C2C2E` | `--text-info` | 20 elements |

**Lines and outlines**

| Colour | Token | Used on |
|---|---|---|
| `#14141E @ 0.06` | set directly in this style | 47 elements |
| `#E6E6EA` | `--accent-tint-15`, `--line` | 26 elements |
| `#EEEEF1` | `--line-soft` | 18 elements |
| `#E8E8EC` | set directly in this style | 13 elements |
| `#14141E @ 0.04` | set directly in this style | 6 elements |

**Gradient stops**

| Colour | Token | Used on |
|---|---|---|
| `#FFFFFF @ 0.9` | set directly in this style | 19 elements |
| `#F2F2F6` | set directly in this style | 19 elements |
| `#E7E7EE` | set directly in this style | 19 elements |
| `#FDFDFE` | set directly in this style | 19 elements |
| `#F6F6F9` | set directly in this style | 19 elements |
| `#48484B` | set directly in this style | 19 elements |
| `#17B27C` | set directly in this style | 19 elements |
| `#08925F` | set directly in this style | 19 elements |

**Interaction-state colours** (hover, pressed, focus, disabled; not visible in the static screens)

| Token | Value |
|---|---|
| `--accent-tint-8` | `#F2F2F5` |
| `--amber-tint` | `#F4E4B8` |
| `--green-tint` | `#CFE8DD` |

**Not rendered:** 16 further colour variables in `tokens.css` (`--accent-wash`, `--amber-grad`, `--amber-ink`, `--coral-grad`, `--exception-dark`, `--pane`, `--tag-filing`, `--tag-news`, `--tag-transcript`, `--tag-web`, `--teal-grad`, `--teal-ink`, `--teal-tint`, `--violet-grad`, `--violet-ink`, `--violet-tint`) are carried over from earlier styles. They are still referenced by base rules that this style overrides, so they are kept in the file under "Carried over", but none appears on a screen.

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
| Header bar | Inter | 14px | 600 | — | uppercase |
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
| Panel | 28px | 0px none | yes | — |
| Chat card | 20px | 0px none | yes | — |
| Composer | 0px | 0px none | none | — |
| Cards | 16px | 1px | yes | — |
| Intro tile | 18px | 1px | yes | — |
| Header bar | 14px | 0px none | yes | — |
| Buttons | 12px | 1px | none | — |
| Chips | 999px | 1px | none | — |
| Text fields | 14px | 1px | none | — |
| Toggle | 999px | 0px none | yes | — |
| Rail tiles | 10px | 0px none | yes | — |
| Send button | 50% | 0px none | none | — |
| Tags | 999px | 1px | none | — |

## 5. Layout

- **Panel:** docked to the right of the browser window, full window height inside a 16px margin; **440px** wide on the compact (Coworker home) screens and **799px** on the expanded screens (chat column + tool pane).
- **Icon rail (right edge):** eight items, top to bottom: **Home**, Research context (with count badge), My filings, CAD library, US library, Compliance, Output Centre, History. Icon-only tiles. The gap between the content and the rail is 24.5px.
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
- **Focus:** buttons and other clickable controls take `2px solid #1C1C1E` with a 2px offset and keep their own radius; text fields show no ring, only their 1px border changes colour; the composer container adds nothing.
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
