# Versance Coworker — style v1: baseline

Baseline: Figtree, light, one indigo accent. Light only. Based on the Versance web app and the 19 extension reference designs.

**Files in this folder**

- `tokens.css` — the design variables this style uses (colour, type, radius, spacing, elevation, motion).
- `components.css` — the base component rules, driven by the tokens.
- `specimen.html` — the style rendered live from its real components.
- `view-design-system.html`, `view-tokens.html`, `view-components.html` — readable pages for this document and the two CSS files, each with a Back arrow (generated from them by `../tools/viewers.py`).
- `../screens/screens.css` — this style's overrides on top of the tokens and components; `../screens/*.html` are the 8 pages that hold the 19 screens (use the "All screens" list in the top-left).

**Lineage:** Started from the Versance web app (`Versance — Talk to Edgar.html`) and the 19 extension reference designs.

## 1. Identity

- **One accent, `#324EFE`.** It is used for every accent role: toggle ON, the active rail tile, primary buttons (Export Report), the count badge, focus rings, selected states, links and info / help text. Pale tints of it (`#CCD3FF` for disabled and low-emphasis buttons, `#E0E4FF` for selected states, `#EFF1FF` for hover) cover the quieter states, and hover / pressed values (`#2C45E0`, `#263BC1`) are derived from it.
- **No second hue.** The one deliberate exception is the near-black `#0A1922` "Web Search On" pill.
- **Structure from the web app:** Figtree, pill-shaped chips and tabs, 8px buttons, 10px inputs, 12px cards, light grey `#F3F5F9` fills and hairline `#D9DDE5` borders.
- **Annotation values win inside the extension:** help / info text, links and selected states use the accent; the right tool pane is `#F9F9F9`; body text is 14px; the help title is 18px bold and sub-heads are 14px bold.
- **Severity:** High `#DC2927` and Medium `#F59D0A` (the web app has no severity colours).
- **Light only.** The reference designs show no dark mode.
- **Composer:** `+`, the text field and send sit in one row, with Web Search and Export Conversation in a row below.

## 2. Colours

Measured from the 19 rendered screens: every fill, text, icon, line and gradient stop that appears. The token column names the variable that holds that value, or says the style sets it directly. Colours used on only 1–2 elements are left out as minor tints.

**Surfaces and fills**

| Colour | Token | Used on |
|---|---|---|
| `#FFFFFF` | `--accent-on`, `--bg`, `--panel` | 447 elements |
| `#F3F5F9` | `--hover`, `--line-soft` | 107 elements |
| `#D9DDE5` | `--line` | 100 elements |
| `#F9F9F9` | `--pane` | 47 elements |
| `#E6E6E6` | set directly in this style | 15 elements |
| `#F0F0F0` | set directly in this style | 15 elements |
| `#F3F3F3` | set directly in this style | 15 elements |
| `#EFF1FF` | `--accent-tint-8` | 4 elements |

**Text and icons**

| Colour | Token | Used on |
|---|---|---|
| `#000000` | `--ink` | 1024 elements |
| `#65728E` | `--muted`, `--tag-web` | 154 elements |
| `#324EFE` | `--accent`, `--tag-filing`, `--text-info` | 140 elements |
| `#CCD3FF` | `--accent-tint-25` | 99 elements |
| `#8D96AA` | `--faint` | 86 elements |
| `#0A1922` | `--exception-dark` | 19 elements |

**Lines and outlines**

| Colour | Token | Used on |
|---|---|---|
| `#E0E4FF` | `--accent-tint-15` | 14 elements |
| `#E4E8FF` | set directly in this style | 3 elements |

**Interaction-state colours** (hover, pressed, focus, disabled; not visible in the static screens)

| Token | Value |
|---|---|
| `--accent-hover` | `#2C45E0` |
| `--accent-pressed` | `#263BC1` |

**Not rendered:** 2 further colour variables in `tokens.css` (`--tag-news`, `--tag-transcript`) are carried over from earlier styles. They are still referenced by base rules that this style overrides, so they are kept in the file under "Carried over", but none appears on a screen.

## 3. Type

Families: **Figtree**. Sizes below are the rendered values on the 19 screens.

| Role | Family | Size | Weight | Tracking | Case |
|---|---|---|---|---|---|
| Display ("Hi,") | Figtree | 28px | 600 | — | — |
| Lead | Figtree | 18px | 400 | — | — |
| Pane title | Figtree | 14px | 600 | — | — |
| Report title | Figtree | 22px | 600 | — | — |
| Finding title | Figtree | 14px | 600 | — | — |
| Body | Figtree | 14px | 400 | — | — |
| Header bar | Figtree | 14px | 500 | — | uppercase |
| Section label | Figtree | 14px | 400 | — | — |
| Meta / dates | Figtree | 14px | 400 | — | — |
| Chip | Figtree | 14px | 400 | — | — |
| Tab | Figtree | 14px | 400 | — | — |
| Button | Figtree | 14px | 400 | — | — |
| Link | Figtree | 14px | 400 | — | — |
| Tag | Figtree | 12px | 400 | — | — |
| Risk badge | Figtree | 12px | 700 | 0.24px | uppercase |

## 4. Shape, depth and glass

| Component | Radius | Border | Shadow | Backdrop blur |
|---|---|---|---|---|
| Panel | 24px | 0px none | yes | — |
| Chat card | 16px | 0px none | none | — |
| Composer | 0px | 0px none | none | — |
| Cards | 12px | 1px | none | — |
| Intro tile | 12px | 0px none | none | — |
| Header bar | 10px | 0px none | none | — |
| Buttons | 8px | 1px | none | — |
| Chips | 999px | 0px none | none | — |
| Text fields | 10px | 1px | none | — |
| Toggle | 999px | 0px none | none | — |
| Rail tiles | 10px | 0px none | none | — |
| Send button | 50% | 0px none | none | — |
| Tags | 6px | 0px none | none | — |

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
