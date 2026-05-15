# Profile README Design System

The contract for editing `README.md` in this repo (the `RealEmmettS/RealEmmettS` profile README that renders on Emmett's GitHub profile page). Any agent or human editing the README must follow these rules so the visual language, voice, and structure stay coherent across refreshes.

This file is not the design system for the portfolio site at `emmetts.dev`. That lives separately, packaged as the **SHAUGHV Design System** (`SHAUGHV Design System.zip` on the author's machine, or shipped with each project repo). The profile README borrows the SHAUGHV palette and voice but operates under different constraints (GitHub's markdown sanitizer) and a deliberately narrower visual vocabulary.

---

## Hard rules

These are non-negotiable. If a future change violates any of them, the change is wrong, even if it "looks fine."

1. **Two colors only.** Forest `#204F20` and cream `#F5E0C5`. Do not introduce gold, orange, black, grey, or any other hue, anywhere, even as a "tiny accent." This rule overrides any color the SHAUGHV master design system suggests.
2. **No em dashes** (`—` or `&mdash;`) anywhere in body copy. Use comma, period, colon, semicolon, slash, or mid-dot (`·` / `&middot;`) instead. This rule overrides the SHAUGHV master design system, which permits em dashes for metadata pairs.
3. **No emoji.** None. Not in headings, not in bullets, not in summaries, not in commit messages that appear in the README.
4. **No GitHub Actions in this repo.** Automation that refreshes project content lives elsewhere and pushes here. Do not add `.github/workflows/`.
5. **Sanitizer-safe HTML only.** No inline `<svg>`, `<script>`, `<style>`, `<iframe>`, `<form>`, `<button>`, `<video>`, `<audio>`. No `class=`, `style=`, or `target="_blank"` attributes (all silently stripped). See [GitHub renderer constraints](#github-renderer-constraints) below.
6. **Curly apostrophes are not required here.** The SHAUGHV master design system requires curly apostrophes in portfolio copy, but the external automation that refreshes this README writes straight apostrophes and would clobber any curly ones. Use straight `'` and `"` so the page stays consistent between refreshes.

---

## Color palette

The entire README uses two colors:

| Token | Hex | Used as |
|---|---|---|
| Forest | `#204F20` | Dark surface in dark-mode widgets; primary text and pill color in light-mode widgets; logo / icon color on cream pills |
| Cream | `#F5E0C5` | Light surface in light-mode widgets; primary text on forest pills; logo / icon color on forest pills |

**Standard shield pattern** (one URL, renders on both GitHub light and dark themes):

```
&color=204F20&labelColor=F5E0C5&logoColor=204F20
```

Forest fill on the right (value) section, cream on the left (label) section, dark logo. This is the default. Invert (`color=F5E0C5&labelColor=204F20&logoColor=204F20`) only when you need visual variety in a row of related pills (e.g., the contact pill row alternates).

**Standard `<picture>` pattern** for any widget that supports `bg_color` / `text_color` parameters:

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="...&bg_color=204F20&text_color=F5E0C5&border_color=F5E0C5...">
  <img alt="..." src="...&bg_color=F5E0C5&text_color=204F20&border_color=204F20...">
</picture>
```

Dark mode source is forest-on-cream-text, light mode default is cream-on-forest-text. Every widget that ships with a bg-color parameter must be wrapped this way.

---

## GitHub renderer constraints

Locked-in reference, verified against the `html-pipeline` sanitizer source and GitHub's official April 2025 dark/light images blog post. Do not assume a tag works without checking this table.

| Capability | Status | Notes |
|---|---|---|
| `<picture>` + `<source media="(prefers-color-scheme: dark)">` | OFFICIAL | The canonical way to swap an image between GitHub themes. Use this everywhere. |
| `#gh-dark-mode-only` / `#gh-light-mode-only` URL fragments | DEPRECATED | Removed from official docs in April 2025. Do not use. |
| `<details>` / `<summary>` | WORKS | Genuine click-to-expand. Put a blank line after `<summary>` to re-enable markdown inside. |
| `<table>` / `<tr>` / `<td>` + `width`, `align`, `valign` | WORKS | Standard for grid layout. Collapses to single column on mobile. |
| `<div align="center">` | WORKS | The only sanctioned alignment hook. |
| `<sub>`, `<sup>`, `<kbd>`, `<samp>`, `<var>` | WORKS | `<kbd>` is the only semantic "keyboard" rendering. |
| `<a name>` / `<a id>` + auto-anchored headings | WORKS | Auto-anchors are lowercase + hyphens. Link via `[label](#section-name)`. |
| HTML comments (`<!-- -->`) | WORKS | Invisible in render, visible in raw source. Use them sparingly. |
| GFM alerts (`> [!NOTE]`, `> [!TIP]`, `> [!IMPORTANT]`, `> [!WARNING]`, `> [!CAUTION]`) | WORKS | Native colored callouts. `[!NOTE]` is the only one used here. |
| Mermaid code fences | WORKS | `flowchart`, `mindmap`, `timeline`, `gitGraph`, `sequenceDiagram`, `classDiagram`, `stateDiagram-v2`, `erDiagram`, `journey`, `gantt`, `pie`, `requirementDiagram` all render. `%%{init: {'theme':'...'}}%%` directive honored. `click` JS callbacks blocked. |
| Animated SVGs from third-party services | WORKS via Camo | SMIL `<animate>` and CSS animations inside SVG both render. Camo cache TTL ~31 days, practical staleness ~24h. |
| Inline `<svg>` | BLOCKED | Not on the sanitizer allowlist. Must use `<img src="*.svg">`. |
| `<script>`, `<style>`, `<iframe>`, `<form>`, `<input>`, `<button>`, `<video>`, `<audio>` | BLOCKED | Not on the allowlist. |
| `class=`, `style=`, `target="_blank"` | STRIPPED | Silently removed. No CSS at all. |
| `<center>` element | UNCLEAR | Untested. Use `<div align="center">` instead. |
| SVG `<script>` element | BLOCKED at browser | `<img>`-loaded SVGs cannot execute scripts (browser policy, not GitHub). |

---

## Voice and copy rules

- **Body copy is sentence case.** "I build full-stack products" not "I Build Full-Stack Products."
- **Section headings are UPPERCASE.** `## NOW`, `## CURRENT WORK`, `## STACK`, `## NUMBERS`, `## COLOPHON`. This pulls from the SHAUGHV Makira-uppercase casing rule.
- **Badge labels are UPPERCASE** with `+` between words, e.g., `&label=PROFILE+VIEWS`, `&label=LAST+PUSH`, `&label=TOTAL+STARS`.
- **Project card titles are Title Case** (e.g., "Magic Pantry", "Personal Site") with a sentence-case tagline beneath in bold.
- **Em dashes are forbidden.** Replace each with the appropriate punctuation:
  - Parenthetical aside → comma pair or parentheses
  - Two-clause connection → period (split sentence) or colon (if explanatory)
  - List item separator → comma or mid-dot (`·`)
  - Range or pairing → comma or slash
- **Mid-dot (`·` / `&middot;`) is the inline separator** for metadata pairs and list-style strings, e.g., `EMMETT@EMMETTS.DEV · EMMETTSHAUGHNESSY.COM`, `bootstrap CIs · inverse-variance weighting · AIM scores`.
- **Slash (`/`)** is the separator for related-but-distinct items in inline lists, e.g., `Next.js / React / Tailwind`, `forgot / reset / change password`.
- **No exclamation marks** except where a markdown image syntax requires one (`![alt](src)`).
- **End every bullet with a period** in the focus list. Each bullet is a complete sentence.
- **Project descriptions in the table** are one continuous paragraph, not bulleted. Code names get backticks (`` `tr300` ``, `` `cargo install` ``, `` `magicpantry://` ``). Cross-repo references use markdown links to the actual GitHub URL.
- **Tense:** present perfect for shipped work ("hardened the network-fix loop"), present continuous for active work ("currently in secondary route parity").

---

## Section structure: the seven movements

The README opens to seven blocks in this exact order. Do not reorder. Do not insert new top-level sections without weighing what to drop.

```
1. HERO          banner, typing SVG, status pulse, bio, contact pills
2. TOC           collapsible jump-nav (<details>)
3. NOW           GFM [!NOTE] with this-week shipping bullets
4. CURRENT WORK  2x3 project table + collapsible workshop list
5. STACK         Mermaid mindmap + release timeline table + 3 badge rows + collapsible focus deep-dive
6. NUMBERS       dynamic shield row + streak/top-langs pair + full-width activity graph
7. COLOPHON      collapsible <details> catalogue of techniques used, then footer banner
```

Each section is separated by a single `---` horizontal rule on its own line, with blank lines before and after.

---

## Component templates

For each pattern in the README, the exact markup and URL template, with the parts a future editor might need to change marked clearly.

### 1. Hero banner (capsule-render)

Wrapped in `<div align="center">`. The `<picture>` element switches between forest-on-cream-text (dark mode) and cream-on-forest-text (light mode). Animation is `fadeIn` (SMIL).

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://capsule-render.vercel.app/api?type=waving&color=204F20&height=200&section=header&text=EMMETT%20SHAUGHNESSY&fontColor=F5E0C5&fontSize=52&fontAlignY=38&desc=DIGITAL%20CRAFTSMAN&descSize=16&descAlignY=58&descAlign=50&animation=fadeIn">
  <img alt="Emmett Shaughnessy, Digital Craftsman" src="https://capsule-render.vercel.app/api?type=waving&color=F5E0C5&height=200&section=header&text=EMMETT%20SHAUGHNESSY&fontColor=204F20&fontSize=52&fontAlignY=38&desc=DIGITAL%20CRAFTSMAN&descSize=16&descAlignY=58&descAlign=50&animation=fadeIn">
</picture>
```

Reference: [capsule-render docs](https://github.com/kyechan99/capsule-render). The `type=waving` is the only variant we use; do not switch to `slice`, `cylinder`, `egg`, etc.

### 2. Typing SVG

Cycles four tagliner lines. Lines are joined by `;` and URL-encoded. Mid-dot is `%C2%B7`, comma is `%2C`, ampersand is `%26`.

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&duration=2400&pause=1200&color=F5E0C5&center=true&vCenter=true&width=640&lines=LINE1;LINE2;LINE3;LINE4">
  <img alt="LINE1 · LINE2 · LINE3 · LINE4" src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&duration=2400&pause=1200&color=204F20&center=true&vCenter=true&width=640&lines=LINE1;LINE2;LINE3;LINE4">
</picture>
```

To update the lines: replace `LINE1;LINE2;LINE3;LINE4` in both URLs with URL-encoded text. Always update both the dark `srcset` and the light `src` together. Always update the `alt` attribute to match. Always use `Fira+Code` as the font.

### 3. Status pulse (4 shields, single row)

```markdown
[![Profile views](https://komarev.com/ghpvc/?username=RealEmmettS&style=for-the-badge&color=204F20&labelColor=F5E0C5&label=PROFILE+VIEWS)](https://github.com/RealEmmettS)
[![Followers](https://img.shields.io/github/followers/RealEmmettS?style=for-the-badge&color=204F20&labelColor=F5E0C5&logo=github&logoColor=204F20&label=FOLLOWERS)](https://github.com/RealEmmettS?tab=followers)
[![Last push](https://img.shields.io/github/last-commit/RealEmmettS/RealEmmettS?style=for-the-badge&color=204F20&labelColor=F5E0C5&logo=git&logoColor=204F20&label=LAST+PUSH)](https://github.com/RealEmmettS/RealEmmettS/commits/master)
[![Stars](https://img.shields.io/github/stars/RealEmmettS?style=for-the-badge&affiliations=OWNER%2CCOLLABORATOR&color=204F20&labelColor=F5E0C5&label=STARS)](https://github.com/RealEmmettS?tab=repositories&sort=stargazers)
```

### 4. Contact pills (4 pills, single row)

```markdown
[![Website](https://img.shields.io/badge/WEBSITE-204F20?style=for-the-badge&logo=About.me&logoColor=F5E0C5)](https://emmettshaughnessy.com)
[![Qube TX](https://img.shields.io/badge/QUBE_TX-F5E0C5?style=for-the-badge&labelColor=204F20&logoColor=204F20)](https://qubetx.com)
[![Resume](https://img.shields.io/badge/RESUME-204F20?style=for-the-badge&logo=readdotcv&logoColor=F5E0C5)](https://resume.emmetts.dev)
[![Email](https://img.shields.io/badge/EMAIL-F5E0C5?style=for-the-badge&labelColor=204F20&logo=maildotru&logoColor=204F20)](mailto:hey@emmetts.dev)
```

Note the alternation: forest / cream / forest / cream. Maintains visual rhythm.

### 5. TOC

```html
<details>
<summary><kbd> Jump to </kbd></summary>

&nbsp;

[`NOW`](#now) &nbsp;&middot;&nbsp; [`CURRENT WORK`](#current-work) &nbsp;&middot;&nbsp; [`STACK`](#stack) &nbsp;&middot;&nbsp; [`NUMBERS`](#numbers) &nbsp;&middot;&nbsp; [`COLOPHON`](#colophon)

</details>
```

The blank line and `&nbsp;` after `<summary>` are required for the markdown inside to parse. Anchors are auto-generated from headings (lowercase + hyphens).

### 6. NOW block (GFM alert)

```markdown
> [!NOTE]
> **MAY 2026, actively shipping**
>
> &middot; **PROJECT NAME**, one-line description of what is shipping
> &middot; **PROJECT NAME**, one-line description of what is shipping
> &middot; **PROJECT NAME**, one-line description of what is shipping
```

Three bullets max. Each bullet starts with `&middot; **Bold project name**, ` then the description. The month/year header is bold and uppercase. Update the month string when a new month begins.

### 7. Project card (inside the 2x3 CURRENT WORK table)

Each cell in the table follows this shape:

```markdown
<td width="50%" valign="top">

### [Project Name](https://project-url.com)
**Short tagline in sentence case**

`Tech1` `Tech2` `Tech3` `Tech4`

Continuous paragraph describing what the project is and what is shipping. Include `code identifiers`, [cross-repo links](https://github.com/Org/repo) where relevant. End with a period.

</td>
```

To add a new project: insert a `<td>` cell into the table (mind the row structure: 2 cells per `<tr>`). To remove a project: delete the `<td>` and rebalance rows. The automation that refreshes content writes directly into these cells, so do not change the `<td width="50%" valign="top">` scaffold or the `### [name](url)` heading shape.

### 8. Workshop list (`<details>`)

```html
<details>
<summary><strong>Also in the workshop,</strong> a dozen more repos &amp; surfaces</summary>

&nbsp;

One continuous paragraph listing all secondary projects, with markdown links to each, mid-dots and slashes between, ending with a period.

</details>
```

### 9. Mermaid mindmap (STACK)

```
%%{init: {'theme':'forest'}}%%
mindmap
  root((WHAT<br/>I BUILD))
    BRANCH1
      Leaf 1a
      Leaf 1b
      Leaf 1c
    BRANCH2
      Leaf 2a
      Leaf 2b
      Leaf 2c
```

`'theme':'forest'` is the built-in Mermaid theme used. Do not switch to `dark`, `default`, `neutral`, or a custom theme. Four branches × 3 leaves is the maximum density that still renders cleanly; if you need to add a fifth branch, redistribute leaves.

### 10. Release timeline (markdown table)

```markdown
| Quarter | Month | Shipped |
|:---:|:---:|---|
| **Q1** | **Jan** | Release 1, Release 2 |
|        | **Feb** | Release 1, Release 2 |
|        | **Mar** | Release 1 |
| **Q2** | **Apr** | Release 1, Release 2 |
|        | **May** | Release 1, Release 2, Release 3 |
```

`Quarter` and `Month` are bold. `Shipped` is plain. Quarter only appears on the first month of that quarter (leave subsequent rows' Quarter cell blank). Items in `Shipped` are comma-separated.

### 11. Badge rows (Languages / Frameworks / Cloud)

All badges follow the same template:

```markdown
![Name](https://img.shields.io/badge/Name-204F20?style=flat-square&logo=SLUG&logoColor=F5E0C5)
```

Three subsections under `## STACK`:
- `### Languages` (6 badges)
- `### Frameworks &amp; libraries` (8 badges)
- `### Cloud &amp; infrastructure` (5 badges)

The slug must be a valid [simple-icons](https://simpleicons.org) identifier. Note: `gnubash` (not `gnu-bash`), `nodedotjs` (not `node.js`), `nextdotjs` (not `next.js`), `amazonaws` (not `amazon-aws`). To add a new badge, copy the line, change the display name and slug, keep all other params identical.

### 12. Focus deep-dive (`<details>`)

```html
<details>
<summary><strong>More on what I'm building right now,</strong> full breakdown</summary>

&nbsp;

- **Topic heading.** Detailed sentence-form description ending in a period.
- **Topic heading.** Detailed sentence-form description ending in a period.
...
</details>
```

Each bullet starts with a bold heading followed by a period, then continues in sentence case. Periods end every bullet.

### 13. Dynamic stat shields (NUMBERS row)

Five shields in `<div align="center">`. Two pull live from the GitHub API via `shields.io/badge/dynamic/json`. The rest use shields.io's built-in GitHub endpoints.

```markdown
![Public repos](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.github.com%2Fusers%2FRealEmmettS&query=%24.public_repos&style=for-the-badge&label=PUBLIC+REPOS&color=204F20&labelColor=F5E0C5)
![Total stars](https://img.shields.io/github/stars/RealEmmettS?style=for-the-badge&affiliations=OWNER&color=204F20&labelColor=F5E0C5&label=TOTAL+STARS)
![Public gists](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.github.com%2Fusers%2FRealEmmettS&query=%24.public_gists&style=for-the-badge&label=PUBLIC+GISTS&color=204F20&labelColor=F5E0C5)
![Following](https://img.shields.io/github/following/RealEmmettS?style=for-the-badge&color=204F20&labelColor=F5E0C5&label=FOLLOWING)
![On GitHub since](https://img.shields.io/badge/ON+GITHUB+SINCE-2017-204F20?style=for-the-badge&labelColor=F5E0C5)
```

The `dynamic/json` queries use JSONPath (`$.public_repos`, `$.public_gists`). The `since 2017` shield is static; update the year if the user's join date is wrong.

### 14. Streak card

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-streak-stats.demolab.com?user=RealEmmettS&background=204F20&stroke=F5E0C5&ring=F5E0C5&fire=F5E0C5&currStreakNum=F5E0C5&sideNums=F5E0C5&currStreakLabel=F5E0C5&sideLabels=F5E0C5&dates=F5E0C5">
  <img alt="GitHub streak" src="https://github-readme-streak-stats.demolab.com?user=RealEmmettS&background=F5E0C5&stroke=204F20&ring=204F20&fire=204F20&currStreakNum=204F20&sideNums=204F20&currStreakLabel=204F20&sideLabels=204F20&dates=204F20">
</picture>
```

Every per-component color (`stroke`, `ring`, `fire`, `currStreakNum`, `sideNums`, `currStreakLabel`, `sideLabels`, `dates`) must be the foreground color of that mode. The `fire` parameter is intentionally not orange.

### 15. Top languages card

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api/top-langs/?username=RealEmmettS&layout=compact&langs_count=10&hide=html,css&size_weight=0.5&count_weight=0.5&bg_color=204F20&title_color=F5E0C5&text_color=F5E0C5&border_color=F5E0C5">
  <img alt="Top languages, weighted blend of bytes-of-code and commit frequency" src="https://github-readme-stats.vercel.app/api/top-langs/?username=RealEmmettS&layout=compact&langs_count=10&hide=html,css&size_weight=0.5&count_weight=0.5&bg_color=F5E0C5&title_color=204F20&text_color=204F20&border_color=204F20">
</picture>
```

The `size_weight=0.5&count_weight=0.5` blend is deliberate: it weights commit frequency alongside bytes-of-code, which surfaces *recent* activity better than the default pure-bytes weighting. Do not change those weights without a reason.

### 16. Activity graph

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-activity-graph.vercel.app/graph?username=RealEmmettS&bg_color=204F20&color=F5E0C5&line=F5E0C5&point=F5E0C5&area=true&area_color=F5E0C5&hide_border=false&border_color=F5E0C5&custom_title=COMMITS+OVER+52+WEEKS">
  <img alt="Commits over 52 weeks" src="https://github-readme-activity-graph.vercel.app/graph?username=RealEmmettS&bg_color=F5E0C5&color=204F20&line=204F20&point=204F20&area=true&area_color=204F20&hide_border=false&border_color=204F20&custom_title=COMMITS+OVER+52+WEEKS">
</picture>
```

Full-width inside a `<div align="center">`. Title stays `COMMITS+OVER+52+WEEKS` (upper case, plus-separated).

### 17. Colophon

```html
<details>
<summary><strong>What this README actually does,</strong> the full catalogue of techniques</summary>

&nbsp;

Intro paragraph explaining what the README is.

| Technique | Where it's used here |
|---|---|
| ... | ... |

Closing notes on what is blocked and what is deferred.

</details>
```

The technique-catalogue table is the heart of the colophon. Add a row whenever a new technique is introduced; remove a row whenever one is dropped.

### 18. Footer banner

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://capsule-render.vercel.app/api?type=waving&color=204F20&height=140&section=footer&text=BUILDING+RELIABLE+SYSTEMS&fontColor=F5E0C5&fontSize=22&fontAlignY=70&desc=EMMETT%40EMMETTS.DEV+%C2%B7+EMMETTSHAUGHNESSY.COM&descSize=12&descAlignY=88&descAlign=50">
  <img alt="Building reliable systems · emmett@emmetts.dev · emmettshaughnessy.com" src="https://capsule-render.vercel.app/api?type=waving&color=F5E0C5&height=140&section=footer&text=BUILDING+RELIABLE+SYSTEMS&fontColor=204F20&fontSize=22&fontAlignY=70&desc=EMMETT%40EMMETTS.DEV+%C2%B7+EMMETTSHAUGHNESSY.COM&descSize=12&descAlignY=88&descAlign=50">
</picture>
```

Mirror of the header banner with `section=footer`. Tagline is `BUILDING+RELIABLE+SYSTEMS`. Description is the two contact strings, separated by a mid-dot (`%C2%B7`).

---

## How to do common edits

### Add a new active project to the `CURRENT WORK` table

1. Identify which row has only one cell, or add a new `<tr>` if all rows are full.
2. Use the [Project card](#7-project-card-inside-the-2x3-current-work-table) template.
3. Keep the table balanced. Each row has exactly two `<td>` cells.
4. Update the [Mermaid mindmap](#9-mermaid-mindmap-stack) under `STACK` if the new project introduces a new branch or leaf.

### Update the `NOW` block for a new week

Replace the three bullets inside the `> [!NOTE]` block. Keep:
- The `**MONTH YEAR, actively shipping**` header (update the month).
- Exactly three bullets, each `&middot; **Bold project**, description`.

### Add a new release to the timeline

Add a row to the table. If the new release falls in a quarter that already has rows, leave the `Quarter` cell blank. If it starts a new quarter, bold the quarter cell.

### Add a new badge to a stack row

Copy the standard badge line. Change:
- The display name (after `badge/`, before `-204F20`).
- The simple-icons slug (after `logo=`).
- Leave `204F20`, `flat-square`, `F5E0C5` unchanged.

### Add a new stat shield to the NUMBERS row

Use either the `dynamic/json` pattern (for any field from `https://api.github.com/users/RealEmmettS`) or shields.io's built-in `/github/<endpoint>/<user>` pattern. Keep the colors `204F20` / `F5E0C5`. Add the corresponding row to the colophon table.

### Add a new widget card

1. Find a service that supports SVG output with color parameters.
2. Wrap it in `<picture>` with dark / light variants.
3. Use `bg_color=204F20` + foreground `F5E0C5` for dark; `bg_color=F5E0C5` + foreground `204F20` for light.
4. Add an `alt` attribute.
5. Add a row to the colophon describing what it does.

### Change a heading name

If a heading rename breaks an automation selector, update the automation, not the heading. The README's structure (heading names included) is the source of truth.

---

## Forbidden patterns

Things that have been tried, considered, or asked for and rejected:

- **Any third color** beyond forest + cream. No gold, no orange, no black, no grey. Even as a 1% accent.
- **Em dashes**, anywhere. See [hard rules](#hard-rules).
- **Emoji**, anywhere. Including the `[!NOTE]` callout icon ` (GitHub renders that itself, do not type emoji in the body).
- **Inline `<svg>`** elements (stripped by sanitizer).
- **`<script>`, `<style>`, `<iframe>`, `<form>`, `<button>`** (all stripped).
- **`class=`, `style=`, `target="_blank"`** attributes (all stripped).
- **The `github-readme-stats` main stats card** (`github-readme-stats.vercel.app/api?...`). The icon-per-row layout was tested and looks out of place. The streak and top-langs cards from the same service are fine because their layouts work.
- **The `github-profile-trophy` widget.** The cartoon trophy icons don't fit. Tested and removed.
- **GitHub Actions in this repo.** Refresh automation lives elsewhere.
- **Per-project `<details>` wrapping inside `CURRENT WORK`.** Tested and rejected: hides information that should be scannable.
- **The 3D contribution view, the snake game, the lowlighter/metrics dashboard.** All would need Actions, which are out of scope here. Noted in the colophon as deferred.
- **Capsule-render variants other than `type=waving`.** Tested. The wave is the only shape that fits the page.
- **Mermaid themes other than `forest` for the mindmap.** Other themes look out of palette.
- **Curly apostrophes** (the SHAUGHV master design system requires them, but the refresh automation writes straight quotes; mixing them produces visible inconsistency).

---

## Pre-push checklist

Before committing any change to `README.md`:

1. **No em dashes.** Search the file for `—` and `&mdash;`. Both must return zero matches.
2. **No emoji.** Visual scan of section headings, summaries, and bullet markers.
3. **No forbidden hex.** Search for `C2A83E` (gold), `FF5E1A` (orange), `090909` (black), `000000`, `FFFFFF`. All must return zero matches.
4. **Every `<picture>` has both `<source>` and `<img>`.** No naked `<source>` blocks (would render nothing in light mode).
5. **Every `<picture>` image has an `alt` attribute.** Required for screen readers and broken-image fallbacks.
6. **Every dark `srcset` has a matching light `src`.** Color parameters inverted (`204F20` / `F5E0C5` swapped).
7. **Headings auto-anchor.** If a heading is renamed, update any TOC link that pointed to its old anchor.
8. **Mermaid blocks parse.** Visual check on a feature branch render before merging.
9. **No `target="_blank"` or `style=` or `class=` attributes** (sanitizer strips silently, but visible in source is a smell).
10. **Colophon updated.** If a new technique was added or an old one removed, the colophon table reflects it.

If any check fails, fix before pushing. The refresh automation runs daily and will lock in whatever is on `master`, so a violation that ships is harder to roll back than one caught before the push.

---

## Reference URLs

External services this README depends on:

| Service | What it does | Docs |
|---|---|---|
| `capsule-render.vercel.app` | Hero and footer wave banners | [github.com/kyechan99/capsule-render](https://github.com/kyechan99/capsule-render) |
| `readme-typing-svg.demolab.com` | Cycling typing animation | [github.com/DenverCoder1/readme-typing-svg](https://github.com/DenverCoder1/readme-typing-svg) |
| `komarev.com/ghpvc` | Profile views counter | [github.com/antonkomarev/github-profile-views-counter](https://github.com/antonkomarev/github-profile-views-counter) |
| `img.shields.io` | All shield badges, including `dynamic/json` for live API queries | [shields.io](https://shields.io) |
| `github-readme-streak-stats.demolab.com` | Streak card | [github.com/DenverCoder1/github-readme-streak-stats](https://github.com/DenverCoder1/github-readme-streak-stats) |
| `github-readme-stats.vercel.app/api/top-langs` | Top languages card | [github.com/anuraghazra/github-readme-stats](https://github.com/anuraghazra/github-readme-stats) |
| `github-readme-activity-graph.vercel.app` | Activity sparkline | [github.com/ashutosh00710/github-readme-activity-graph](https://github.com/ashutosh00710/github-readme-activity-graph) |
| `api.github.com` | Source of truth for `dynamic/json` shields (public_repos, public_gists) | [docs.github.com/rest](https://docs.github.com/rest) |

If any of these services break or change their URL contract, the README will render broken-image icons until the URLs are updated. None of these are under our control; the trade-off for live data without an Action is third-party dependence.

---

## Sanitizer sources

Constraint authority for this design system:

- **html-pipeline** (GitHub's markdown sanitizer): [github.com/gjtorikian/html-pipeline](https://github.com/gjtorikian/html-pipeline) — the allowlist of tags and attributes.
- **GitHub blog on dark/light images** (April 2025): [github.blog/developer-skills/github/how-to-make-your-images-in-markdown-on-github-adjust-for-dark-mode-and-light-mode/](https://github.blog/developer-skills/github/how-to-make-your-images-in-markdown-on-github-adjust-for-dark-mode-and-light-mode/) — canonical method for theme-adaptive imagery.
- **GitHub Mermaid docs**: [docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams) — supported diagram types and theming.
- **GitHub anonymized URLs (Camo)**: [docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-anonymized-urls](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-anonymized-urls) — the image proxy that serves every external SVG.
