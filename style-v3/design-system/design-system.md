# Versance Coworker — style v3: palette

Palette: indigo plus green, coral, teal and violet. Light only. Based on v2 (extra colour).

**Files in this folder**

- `tokens.css` — the design variables this style uses (colour, type, radius, spacing, elevation, motion).
- `components.css` — the base component rules, driven by the tokens.
- `specimen.html` — the style rendered live from its real components.
- `view-design-system.html`, `view-tokens.html`, `view-components.html` — readable pages for this document and the two CSS files, each with a Back arrow (generated from them by `../tools/viewers.py`).
- `../screens/screens.css` — this style's overrides on top of the tokens and components; `../screens/*.html` are the 8 pages that hold the 19 screens (use the "All screens" list in the top-left).

**Lineage:** v2 plus three supporting colours.

## 1. Identity

- **Three supporting colours added to v2's indigo accent**, each with one job: **green** for toggle ON and the send button (`--green-grad`; pale `#CDEBD8` when the field is empty), **coral** for the count badge (`--coral-grad`), and **teal / violet** for icon chips and tags (Compliance = violet tint, SEDAR = teal tint).
- **Indigo `#324EFE` stays the primary accent:** links, the active rail tile, primary buttons, selected states and the focus ring.
- **Backdrop:** a soft indigo / coral / green mesh gradient behind the panel.
- Everything else (28px panel, 16px cards, shadows, spring toggle, tabs, type, motion) is the v2 treatment.

## 2. Colours

Measured from the 19 rendered screens: every fill, text, icon, line and gradient stop that appears. The token column names the variable that holds that value, or says the style sets it directly. Colours used on only 1–2 elements are left out as minor tints.

**Surfaces and fills**

| Colour | Token | Used on |
|---|---|---|
| `#FFFFFF` | `--accent-on`, `--bg`, `--panel` | 465 elements |
| `#D9DDE5` | `--line` | 70 elements |
| `#EEF0FB` | set directly in this style | 52 elements |
| `#CDEBD8` | `--green-tint` | 16 elements |
| `#FFFFFF @ 0.55` | set directly in this style | 15 elements |
| `#FFFFFF @ 0.75` | set directly in this style | 15 elements |

**Text and icons**

| Colour | Token | Used on |
|---|---|---|
| `#000000` | `--ink` | 1019 elements |
| `#65728E` | `--muted` | 181 elements |
| `#324EFE` | `--accent`, `--tag-filing`, `--text-info` | 120 elements |
| `#8D96AA` | `--faint` | 86 elements |
| `#CCD3FF` | `--accent-tint-25` | 81 elements |
| `#0A1922` | `--amber-ink`, `--exception-dark` | 19 elements |
| `#6D3FD6` | `--violet-ink` | 13 elements |
| `#0E8F84` | `--teal-ink` | 7 elements |

**Lines and outlines**

| Colour | Token | Used on |
|---|---|---|
| `#101840 @ 0.06` | set directly in this style | 56 elements |
| `#F3F5F9` | `--hover`, `--line-soft` | 18 elements |
| `#324EFE @ 0.12` | set directly in this style | 14 elements |
| `#101840 @ 0.09` | set directly in this style | 7 elements |
| `#324EFE @ 0.06` | set directly in this style | 6 elements |

**Gradient stops**

| Colour | Token | Used on |
|---|---|---|
| `#5E74FF` | set directly in this style | 20 elements |
| `#2C45E0` | `--accent-hover` | 20 elements |
| `#324EFE @ 0.11` | set directly in this style | 19 elements |
| `#FF5D73 @ 0.09` | set directly in this style | 19 elements |
| `#5AC47E @ 0.09` | set directly in this style | 19 elements |
| `#FAFAFC` | set directly in this style | 19 elements |
| `#F3F4F9` | set directly in this style | 19 elements |
| `#EEEFF4` | set directly in this style | 15 elements |

**Interaction-state colours** (hover, pressed, focus, disabled; not visible in the static screens)

| Token | Value |
|---|---|
| `--accent-pressed` | `#263BC1` |
| `--accent-tint-8` | `#EFF1FF` |
| `--amber-tint` | `#F4E4B8` |

**Not rendered:** 3 further colour variables in `tokens.css` (`--amber-grad`, `--tag-news`, `--tag-web`) are carried over from earlier styles. They are still referenced by base rules that this style overrides, so they are kept in the file under "Carried over", but none appears on a screen.

## 3. Type

Families: **Figtree**. Sizes below are the rendered values on the 19 screens.

| Role | Family | Size | Weight | Tracking | Case |
|---|---|---|---|---|---|
| Display ("Hi,") | Figtree | 32px | 700 | -0.64px | — |
| Lead | Figtree | 18px | 500 | -0.18px | — |
| Pane title | Figtree | 16px | 700 | -0.16px | — |
| Report title | Figtree | 24px | 700 | -0.48px | — |
| Finding title | Figtree | 14px | 600 | — | — |
| Body | Figtree | 14px | 400 | — | — |
| Header bar | Figtree | 14px | 600 | — | uppercase |
| Section label | Figtree | 14px | 400 | — | — |
| Meta / dates | Figtree | 14px | 400 | — | — |
| Chip | Figtree | 14px | 400 | — | — |
| Tab | Figtree | 14px | 400 | — | — |
| Button | Figtree | 14px | 400 | — | — |
| Link | Figtree | 14px | 400 | — | — |
| Tag | Figtree | 12px | 400 | — | — |
| Risk badge | Figtree | 12px | 700 | 0.36px | uppercase |

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
| Chips | 999px | 1px | yes | — |
| Text fields | 14px | 1px | yes | — |
| Toggle | 999px | 0px none | yes | — |
| Rail tiles | 10px | 0px none | yes | — |
| Send button | 50% | 0px none | none | — |
| Tags | 999px | 0px none | none | — |

## 5. Layout

- **Panel:** docked to the right of the browser window, full window height inside a 16px margin; **440px** wide on the compact (Coworker home) screens and **799px** on the expanded screens (chat column + tool pane).
- **Icon rail (right edge):** eight items, top to bottom: **Home**, Research context (with count badge), My filings, CAD library, US library, Compliance, Output Centre, History. Icon-only tiles. The gap between the content and the rail is 24.5px.
- **Composer:** `+`, text field and send in one row; Web Search and Export Conversation in a row below.
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
- **Focus:** buttons and other clickable controls take `2px solid #324EFE` with a 2px offset and keep their own radius; text fields show no ring, only their 1px border changes colour; the composer container adds nothing.
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
