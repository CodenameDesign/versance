# Versance Coworker — style v9: context

Context: black and white with orange, mono labels, dark / light. Based on the Sanity references (three images).

**Files in this folder**

- `tokens.css` — the design variables this style uses (colour, type, radius, spacing, elevation, motion).
- `components.css` — the base component rules, driven by the tokens.
- `specimen.html` — the style rendered live from its real components (with the dark / light button).
- `view-design-system.html`, `view-tokens.html`, `view-components.html` — readable pages for this document and the two CSS files, each with a Back arrow (generated from them by `../tools/viewers.py`).
- `../screens/screens.css` — this style's overrides on top of the tokens and components; `../screens/*.html` are the 8 pages that hold the 19 screens (use the "All screens" list in the top-left).

**Lineage:** v6's sharp structure, re-coloured from the Sanity references, with a dark / light toggle.

## 1. Identity

- **Look:** stark black and white with one vivid orange `#FF4A00`; sharp corners and no shadows; dense halftone dots on the page behind the panel; corner crop marks around the panel; dotted rules between list rows and above the footer; hairline `#D9D9D4` (light) / `#2C2C2C` (dark) card borders and solid black / white rules on key controls.
- **Type:** Inter for text (headings regular weight, tight tracking, "Hi," 40px) and **IBM Plex Mono** for labels: the orange header bar (company name), EDIT, `[ NEW CHAT ]`, bracketed tags, chips (uppercase), placeholder, dates, link text, risk badges, help sub-heads.
- **Orange header bar** (like "CURRENT CONTEXT: LEARN, DOCS"): company name in mono on orange with a black `EDIT` tag.
- **Controls:** primary button orange with black text (inverts to ink on hover); send is a round ink button (white arrow), orange on hover; toggle is a square switch (orange when on); active tab is inverted (ink on paper); help panel is a black screen with orange mono sub-heads.
- **Highlights:** quoted phrases use a yellow `#FFD84A` marker; risk badges: High = orange, Medium = yellow, both with black text and a black border.
- **Dark / light toggle:** square sun / moon button in the panel (above the user avatar). Sets `data-theme="dark"` on `<html>`, is remembered in `localStorage` (so it carries between pages), and can be forced with `?theme=dark`.
  - Dark values: page `#0A0A0A`, panel `#101010`, cards `#161616`, fills `#1E1E1E`, ink `#F4F4F1`, muted `#A3A39E`; orange unchanged; send turns light.

## 2. Colours

Measured from the 19 rendered screens: every fill, text, icon, line and gradient stop that appears. The token column names the variable that holds that value, or says the style sets it directly. Colours used on only 1–2 elements are left out as minor tints.

### Light theme

**Surfaces and fills**

| Colour | Token | Used on |
|---|---|---|
| `#FFFFFF` | `--bg`, `--card`, `--inv-ink` | 475 elements |
| `#FF4A00` | `--accent`, `--orange` | 88 elements |
| `#D9DDE5` | set directly in this style | 67 elements |
| `#F2F2EF` | `--fill` | 55 elements |
| `#FFD84A` | `--mk` | 4 elements |

**Text and icons**

| Colour | Token | Used on |
|---|---|---|
| `#0B0B0B` | `--ink`, `--inv-bg`, `--strong` | 1640 elements |
| `#5C5C58` | `--muted` | 165 elements |
| `#8E8E89` | `--dotline`, `--faint` | 98 elements |
| `#000000` | set directly in this style | 20 elements |

**Lines and outlines**

| Colour | Token | Used on |
|---|---|---|
| `#D9D9D4` | `--line` | 285 elements |

**Gradient stops**

| Colour | Token | Used on |
|---|---|---|
| `#C4C4BE` | `--dots` | 19 elements |

### Dark theme

**Surfaces and fills**

| Colour | Token | Used on |
|---|---|---|
| `#161616` | `--card` | 302 elements |
| `#FF4A00` | `--accent`, `--orange` | 88 elements |
| `#D9DDE5` | set directly in this style | 67 elements |
| `#1E1E1E` | `--fill` | 55 elements |
| `#101010` | `--panel` | 19 elements |
| `#FFD84A` | `--mk` | 4 elements |

**Text and icons**

| Colour | Token | Used on |
|---|---|---|
| `#F4F4F1` | `--ink`, `--inv-bg`, `--strong` | 1419 elements |
| `#0B0B0B` | `--text-info`, `--text-selected` | 200 elements |
| `#A3A39E` | `--muted` | 165 elements |
| `#0A0A0A` | `--bg`, `--inv-ink` | 123 elements |
| `#75756F` | `--faint` | 80 elements |
| `#FFFFFF` | `--risk-on` | 31 elements |
| `#000000` | set directly in this style | 21 elements |

**Lines and outlines**

| Colour | Token | Used on |
|---|---|---|
| `#2C2C2C` | `--line` | 286 elements |
| `#4C4C48` | `--dotline` | 18 elements |

**Gradient stops**

| Colour | Token | Used on |
|---|---|---|
| `#2E2E2E` | `--dots` | 19 elements |

**Interaction-state colours** (hover, pressed, focus, disabled; not visible in the static screens)

| Token | Value |
|---|---|
| `--accent-hover` | `#E04200` |
| `--accent-on` | `#111111` |
| `--accent-pressed` | `#C93508` |
| `--accent-tint-15` | `#FFE1D1` |
| `--accent-tint-25` | `#FFC9AD` |
| `--accent-tint-8` | `#FFF1E8` |
| `--amber-tint` | `#F4E4B8` |
| `--green-tint` | `#CFE0DE` |

**Not rendered:** 25 further colour variables in `tokens.css` (`--accent-grad`, `--accent-grad-diag`, `--accent-wash`, `--amber-grad`, `--amber-ink`, `--coral-grad`, `--exception-dark`, `--green-grad`, `--hover`, `--line-soft`, `--mark`, `--pane`, `--risk-high`, `--risk-medium`, `--soft-wash`, `--tag-filing`, `--tag-news`, `--tag-transcript`, `--tag-web`, `--teal-grad`, `--teal-ink`, `--teal-tint`, `--violet-grad`, `--violet-ink`, `--violet-tint`) are carried over from earlier styles. They are still referenced by base rules that this style overrides, so they are kept in the file under "Carried over", but none appears on a screen.

## 3. Type

Families: **IBM Plex Mono**, **Inter**. Sizes below are the rendered values on the 19 screens.

| Role | Family | Size | Weight | Tracking | Case |
|---|---|---|---|---|---|
| Display ("Hi,") | Inter | 40px | 400 | -1.6px | — |
| Lead | Inter | 18px | 400 | -0.18px | — |
| Pane title | Inter | 18px | 400 | -0.36px | — |
| Report title | Inter | 26px | 400 | -0.78px | — |
| Finding title | Inter | 14px | 600 | — | — |
| Body | Inter | 14px | 400 | — | — |
| Header bar | IBM Plex Mono | 12px | 500 | 0.24px | uppercase |
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
- **Focus:** buttons and other clickable controls take `2px solid #FF4A00` with a 2px offset and keep their own radius; text fields show no ring, only their 1px border changes colour; the composer container adds nothing.
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
