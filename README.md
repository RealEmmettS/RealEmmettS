<!-- ====================================================================== -->
<!--  EMMETT SHAUGHNESSY - GITHUB PROFILE                                   -->
<!--                                                                        -->
<!--  GitHub-safe SHAUGHV surface. No JavaScript, no CSS, no inline SVG,    -->
<!--  no GitHub Actions. Built from GFM, sanitizer-safe HTML, live badges,  -->
<!--  shields, and theme-aware image URLs.                                  -->
<!-- ====================================================================== -->

<div align="center">

<h1>EMMETT SHAUGHNESSY</h1>

<strong>DIGITAL CRAFTSMAN</strong>

**Rust diagnostics / agent tooling / full-stack product systems.**

I build operational software that survives real installers, real users, and real release loops. Current focus: Qube TX, WB-300, Magic Pantry, shaughv-code, and QorkMe.

<table width="100%">
<tr>
<td align="center" width="25%"><strong>CRATES<br>INSTALLERS</strong><br><sub>Rust CLIs<br>Installers</sub></td>
<td align="center" width="25%"><strong>AGENT<br>WORKFLOWS</strong><br><sub>Codex skills<br>Git control</sub></td>
<td align="center" width="25%"><strong>PRODUCT<br>SYSTEMS</strong><br><sub>Mobile web<br>Realtime AI</sub></td>
<td align="center" width="25%"><strong>CLIENT<br>DELIVERY</strong><br><sub>Qube TX<br>Data work</sub></td>
</tr>
</table>

[![Website](https://img.shields.io/badge/WEBSITE-204F20?logo=About.me&logoColor=F5E0C5)](https://emmettshaughnessy.com)
[![Qube TX](https://img.shields.io/badge/QUBE_TX-F5E0C5?labelColor=204F20&logoColor=204F20)](https://qubetx.com)
[![Resume](https://img.shields.io/badge/RESUME-204F20?logo=readdotcv&logoColor=F5E0C5)](https://resume.emmetts.dev)
[![Email](https://img.shields.io/badge/EMAIL-F5E0C5?labelColor=204F20&logo=maildotru&logoColor=204F20)](mailto:hey@emmetts.dev)

</div>

<details>
<summary><kbd> Jump to </kbd></summary>

&nbsp;

[`LATEST SHIPS`](#latest-ships) &nbsp;&middot;&nbsp; [`SELECTED SYSTEMS`](#selected-systems) &nbsp;&middot;&nbsp; [`STACK`](#stack) &nbsp;&middot;&nbsp; [`NUMBERS`](#numbers) &nbsp;&middot;&nbsp; [`WORKSHOP ARCHIVE`](#workshop-archive) &nbsp;&middot;&nbsp; [`COLOPHON`](#colophon)

</details>

---

## LATEST SHIPS

> [!NOTE]
> **JULY 2026, selected proof**
>
> &middot; **Agent task system, now standalone.** My multi-agent loop runs a coding agent against an MCP-backed task queue while Claude Code hooks handle heartbeat, check-in, checkout, and stalled-task detection. The task and workplace-memory layer is now extracted into shaughv-tasks, a dual-surface Claude Code + Codex plugin that installs on its own in any agent. [shaughv-tasks](https://github.com/RealEmmettS/shaughv-tasks).
>
> &middot; **goose, a Rust desktop companion.** A native desktop pet rebuilt from scratch in Rust across fifteen milestones: a task state machine with wander and idle behavior, bundled original audio, hover and click hit-testing, foreign-window perching, multi-monitor appearance, and quiet-hours scheduling, all driven from a CLI/TUI control plane with installer preflight. [Repository](https://github.com/RealEmmettS/goose).
>
> &middot; **Data platform reliability.** Hardened a production data-sync platform: webhook-driven freshness signals that replace poll-recency false-alerts, pre-MERGE source de-duplication to stop "matched multiple source rows" failures, financial ledger parity views with duplicate-key triage, and a restored weekly delete-reconciliation cadence. Python sync workers on Azure Functions and Container Apps Jobs over SQL Server. [Project notes](#workshop-archive).

---

## SELECTED SYSTEMS

<table>
<tr>
<td width="11%" valign="top"><strong>001</strong><br><sub>SYSTEMS</sub></td>
<td width="61%" valign="top">

### [Qube TX](https://qubetx.com)
`Rust` `TypeScript` `Next.js` `CLI`

Diagnostics tooling and web studio work centered on Rust CLIs, installers, updater reliability, and the marketing surfaces that explain them. TR-300 has shipped as a canonical crate with native Windows distribution, cross-platform collector hardening, installer hash checks, profile-write safeguards, and single-install migration cleanup.

</td>
<td width="28%" valign="top">

**Evidence**

[TR-300](https://github.com/QubeTX/qube-machine-report)<br>
[Qube TX site](https://github.com/QubeTX/QubeTX_Landing)<br>
[SpeedQX](https://github.com/QubeTX/speedtest)

</td>
</tr>
<tr>
<td width="11%" valign="top"><strong>002</strong><br><sub>WORKFLOW</sub></td>
<td width="61%" valign="top">

### [WB-300](https://github.com/QubeTX/qube-workbranch-view)
`Rust` `TUI` `Git` `Agents`

A terminal control tower for agent-driven development. It derives branch hierarchy from commit topology, exposes a `wb300.agent.v2` JSON contract, sends OS notifications on important state changes, and gives coding agents a shared map of the workbranch system.

</td>
<td width="28%" valign="top">

**Evidence**

[Repository](https://github.com/QubeTX/qube-workbranch-view)<br>
`v2.0.0` topology model<br>
Machine-wide tree view

</td>
</tr>
<tr>
<td width="11%" valign="top"><strong>003</strong><br><sub>MOBILE</sub></td>
<td width="61%" valign="top">

### Magic Pantry
`Expo` `React Native` `Supabase` `Anthropic`

A rebuilt cross-platform pantry app on Supabase, Expo, Realtime, RLS, and AI edge functions. Recent work made the list offline-first and collaborative, with durable queue replay, row-level merge rules, AI categorization, recipe generation, URL import, substitutions, and App Store-ready auth flows.

</td>
<td width="28%" valign="top">

**Evidence**

Offline queue<br>
Realtime merge<br>
AI list helpers

</td>
</tr>
<tr>
<td width="11%" valign="top"><strong>004</strong><br><sub>AGENTS</sub></td>
<td width="61%" valign="top">

### [shaughv-code](https://github.com/RealEmmettS/shaughv-code)
`Codex` `Skills` `MCP` `Design`

My personal Codex plugin and skill library. It packages practical operating systems for design, reasoning, security review, audio, Mistral API work, human changelogs, branch control, status lines, image work, storage, handoffs, and summary conventions into one portable repository. The task and workplace-memory skills now also ship separately as shaughv-tasks.

</td>
<td width="28%" valign="top">

**Evidence**

[Repository](https://github.com/RealEmmettS/shaughv-code)<br>
`v0.25.0` plugin<br>
[shaughv-tasks](https://github.com/RealEmmettS/shaughv-tasks)

</td>
</tr>
<tr>
<td width="11%" valign="top"><strong>005</strong><br><sub>WEB</sub></td>
<td width="61%" valign="top">

### [QorkMe](https://qork.me)
`Next.js` `Supabase` `Rust` `Analytics`

A URL shortener with custom aliases, click analytics, admin reporting, a public shorten API, and the `qork` Rust CLI. The current system includes installer cards, source attribution, analytics RPCs, pure-CSS charts, and a cleaner Qube TX design language across the product.

</td>
<td width="28%" valign="top">

**Evidence**

[Live app](https://qork.me)<br>
[qork CLI](https://github.com/QubeTX/qork)<br>
Admin analytics

</td>
</tr>
</table>

---

## STACK

<table width="100%">
<tr>
<td width="18%" align="center"><strong>001</strong><br><sub>SYSTEMS</sub></td>
<td><code>Rust CLIs</code> &middot; <code>native installers</code> &middot; <code>update paths</code></td>
</tr>
<tr>
<td align="center"><strong>002</strong><br><sub>WEB</sub></td>
<td><code>Next.js products</code> &middot; <code>studio surfaces</code> &middot; <code>admin consoles</code></td>
</tr>
<tr>
<td align="center"><strong>003</strong><br><sub>MOBILE</sub></td>
<td><code>Expo apps</code> &middot; <code>realtime lists</code> &middot; <code>store-ready auth</code></td>
</tr>
<tr>
<td align="center"><strong>004</strong><br><sub>AI WORKFLOWS</sub></td>
<td><code>agent orchestration</code> &middot; <code>MCP task queues</code> &middot; <code>review loops</code></td>
</tr>
<tr>
<td align="center"><strong>005</strong><br><sub>CLOUD DATA</sub></td>
<td><code>SQL Server pipelines</code> &middot; <code>Azure queues</code> &middot; <code>freshness + observability</code></td>
</tr>
</table>

### Working Set

![Rust](https://img.shields.io/badge/Rust-204F20?logo=rust&logoColor=F5E0C5)
![TypeScript](https://img.shields.io/badge/TypeScript-204F20?logo=typescript&logoColor=F5E0C5)
![Python](https://img.shields.io/badge/Python-204F20?logo=python&logoColor=F5E0C5)
![FastAPI](https://img.shields.io/badge/FastAPI-204F20?logo=fastapi&logoColor=F5E0C5)
![Next.js](https://img.shields.io/badge/Next.js-204F20?logo=nextdotjs&logoColor=F5E0C5)
![React Native](https://img.shields.io/badge/React_Native-204F20?logo=react&logoColor=F5E0C5)
![Supabase](https://img.shields.io/badge/Supabase-204F20?logo=supabase&logoColor=F5E0C5)
![Azure](https://img.shields.io/badge/Azure-204F20?logo=microsoftazure&logoColor=F5E0C5)
![Vercel](https://img.shields.io/badge/Vercel-204F20?logo=vercel&logoColor=F5E0C5)
![Codex](https://img.shields.io/badge/Codex-204F20?logo=openai&logoColor=F5E0C5)
![Anthropic](https://img.shields.io/badge/Anthropic-204F20?logo=anthropic&logoColor=F5E0C5)

---

## NUMBERS

<div align="center">

[![Profile views](https://komarev.com/ghpvc/?username=RealEmmettS&color=204F20&labelColor=F5E0C5&label=PROFILE+VIEWS)](https://github.com/RealEmmettS)
[![Followers](https://img.shields.io/github/followers/RealEmmettS?color=204F20&labelColor=F5E0C5&logo=github&logoColor=204F20&label=FOLLOWERS)](https://github.com/RealEmmettS?tab=followers)
[![Last push](https://img.shields.io/github/last-commit/RealEmmettS/RealEmmettS?color=204F20&labelColor=F5E0C5&logo=git&logoColor=204F20&label=LAST+PUSH)](https://github.com/RealEmmettS/RealEmmettS/commits/master)
![Public repos](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.github.com%2Fusers%2FRealEmmettS&query=%24.public_repos&label=PUBLIC+REPOS&color=204F20&labelColor=F5E0C5)
![Total stars](https://img.shields.io/github/stars/RealEmmettS?affiliations=OWNER&color=204F20&labelColor=F5E0C5&label=TOTAL+STARS)
![On GitHub since](https://img.shields.io/badge/ON+GITHUB+SINCE-2017-204F20?labelColor=F5E0C5)

</div>

<br>

<table align="center" width="100%">
<tr>
<td width="50%" align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com?user=RealEmmettS&background=204F20&stroke=F5E0C5&ring=F5E0C5&fire=F5E0C5&currStreakNum=F5E0C5&sideNums=F5E0C5&currStreakLabel=F5E0C5&sideLabels=F5E0C5&dates=F5E0C5">
  <img alt="GitHub streak" src="https://streak-stats.demolab.com?user=RealEmmettS&background=F5E0C5&stroke=204F20&ring=204F20&fire=204F20&currStreakNum=204F20&sideNums=204F20&currStreakLabel=204F20&sideLabels=204F20&dates=204F20">
</picture>

</td>
<td width="50%" align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api/top-langs/?username=RealEmmettS&layout=compact&langs_count=10&hide=html,css&size_weight=0.5&count_weight=0.5&bg_color=204F20&title_color=F5E0C5&text_color=F5E0C5&border_color=F5E0C5">
  <img alt="Top languages, weighted blend of bytes-of-code and commit frequency" src="https://github-readme-stats.vercel.app/api/top-langs/?username=RealEmmettS&layout=compact&langs_count=10&hide=html,css&size_weight=0.5&count_weight=0.5&bg_color=F5E0C5&title_color=204F20&text_color=204F20&border_color=204F20">
</picture>

</td>
</tr>
</table>

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-activity-graph.vercel.app/graph?username=RealEmmettS&bg_color=204F20&color=F5E0C5&line=F5E0C5&point=F5E0C5&area=true&area_color=F5E0C5&hide_border=false&border_color=F5E0C5&custom_title=COMMITS+OVER+52+WEEKS">
  <img alt="Commits over 52 weeks" src="https://github-readme-activity-graph.vercel.app/graph?username=RealEmmettS&bg_color=F5E0C5&color=204F20&line=204F20&point=204F20&area=true&area_color=204F20&hide_border=false&border_color=204F20&custom_title=COMMITS+OVER+52+WEEKS">
</picture>

</div>

---

## WORKSHOP ARCHIVE

<details>
<summary><strong>Release ledger,</strong> selected depth</summary>

&nbsp;

- **TR-300 v3.17.0.** Migrate-cleanup detects and removes previous install kinds when installing through a new channel, so Windows installer, cargo, and bare-binary installs do not fight each other. It follows the v3.16.0 stability pass across collectors, output, builds, install/update behavior, self-update reliability, and test coverage.
- **QubeTX_Landing v3.2.0.** The studio site added a self-documenting design-system page, live terminal kit, downloadable brand kit, ScrollTrace, stat count-ups, and a denser product-line story.
- **Magic Pantry 2.0.2.** Offline-first durability and realtime merge sit on top of Phases I-L: smart entry, recipe library, substitutions, sort modes, store-ready auth, EAS production wiring, and Supabase migration tooling.
- **shaughv-code v0.25.0.** The skill bundle now spans design, audio, Mistral, Quiver, security, changelogs, branch control, image work, storage, handoff, learning, productivity, and TT;DR summaries.
- **qork CLI v1.1.1.** The terminal shortener ships native installers, liveness checks, `qork help`, origin-aware uninstall, installer-preferred updates, and source attribution back into QorkMe analytics.

</details>

<details>
<summary><strong>Secondary surfaces,</strong> public workshop</summary>

&nbsp;

- **SHAUGHV brand system.** `shaughv-cdn` hosts versioned brand assets, fonts, and static/animated mark drop-ins behind a manifest at [`cdn.shaughv.com/tree.json`](https://cdn.shaughv.com/tree.json). `shaughv_vintage` carries the cream-and-sage personal portfolio variant, Pretext text fitting, scrollspy, dot-field motion, and project-level automation.
- **Agent task plugin.** [`shaughv-tasks`](https://github.com/RealEmmettS/shaughv-tasks) is the task-queue and workplace-memory system split out of `shaughv-code` into its own dual-surface Claude Code + Codex plugin, distributed through both marketplaces and `npx skills add`.
- **goose.** [`goose`](https://github.com/RealEmmettS/goose) is a Rust desktop-companion app remade for modern computing with original bundled assets, a milestone-driven engine (task state machine, audio, hit-testing, foreign-window perch, multi-monitor), and a CLI/TUI control plane.
- **Video and media.** `italy-trip-video` is a Remotion birthday-trip slideshow with timed captions and a CapCut polish path. It was scaffolded through the video workflow in `shaughv-code`.
- **Web tools.** `qrgen` is a QR-code generator and AI styling surface with a SHAUGHV product UI. `realtime2_test` is an OpenAI Realtime API voice-agent prototype with pure shared handlers across Express and Vercel functions.
- **Qube TX surfaces.** [`qube-machine-report-homepage`](https://github.com/QubeTX/qube-machine-report-homepage), [`qube-reports-executables`](https://github.com/QubeTX/qube-reports-executables), SpeedQX, nd300, and SD-300 sit around the main diagnostics product line.
- **Client and artist sites.** [Dorsey 2026](https://github.com/QubeTX/dorsey_2026_BETA) rebuilds a touring musician's web presence on the modern Next.js / React / Tailwind stack while preserving the original visual language.

</details>

<details>
<summary><strong>Private systems,</strong> summarized without repo links</summary>

&nbsp;

- **Data platform reliability.** Webhook-driven freshness signals over poll-recency to end false-stale alerts, pre-MERGE source de-duplication to stop "matched multiple source rows" failures, financial ledger parity views with duplicate-key triage, orphaned high-volume poller recovery, and a restored weekly delete-reconciliation cadence. Python sync workers on Azure Functions and Container Apps Jobs over SQL Server, with Service Bus queues and App Insights observability.
- **Reporting and pipeline tooling.** A reporting backend with regenerate flows, tightened date-input validation, audit events that make silent failures observable, and CSS-token guard tests; plus pipeline-monitor UI work for external-API rate-limit backoff and consistent server-side query timeouts. Python / FastAPI and React / TypeScript on Azure Container Apps and Static Web Apps.
- **Multi-agent orchestration layer.** An internal MCP task queue coordinating human and coding-agent work: operator priority lists exposed through MCP read tools, Claude Code hooks for heartbeat / check-in / checkout and liveness, stalled-task detection, a dashboard answer-bridge, and same-origin CSRF guards on the write routes.
- **Scorecards and operator surfaces.** Snapshot charts, scoped office filters, triage views with hide-done defaults, operator-aware task updates, and internal tool distribution through a team plugin.

</details>

---

## COLOPHON

<details>
<summary><strong>What this README actually does,</strong> the profile renderer catalogue</summary>

&nbsp;

This profile is a GitHub-safe SHAUGHV translation: type-forward, proof-first, cream/forest only, and built inside GitHub's markdown sanitizer. The page avoids custom CSS, JavaScript, inline SVG, iframes, forms, new-tab attributes, and repo-local Actions.

| Technique | Where it is used here |
|---|---|
| Static text lockup | Hero identity and footer close |
| `&lt;picture&gt;` + `prefers-color-scheme` | Streak card, top-langs card, activity graph |
| GFM alert (`> [!NOTE]`) | `LATEST SHIPS` |
| `<details>` / `<summary>` | TOC, archive sections, colophon |
| HTML tables | Hero proof strip, selected systems, paired stats cards |
| Live shields | Contact pills, profile metrics, stack badges |
| Theme-aware widget cards | Streak, top languages, activity graph |
| Heading auto-anchors | TOC links |
| HTML entities | Mid-dot separators, non-breaking spacing, escaped symbols |

Blocked by design: inline SVG, script tags, style attributes, class attributes, iframes, forms, video, audio, and new-tab target attributes. Everything visible here is plain markdown, sanitizer-safe HTML, live badges, or a parameterized image URL.

Deferred unless this repo's no-Actions rule changes: generated contribution animations, lowlighter-style metrics dashboards, 3D contribution grids, and WakaTime cards.

Renderer references: [html-pipeline](https://github.com/gjtorikian/html-pipeline) and [GitHub dark/light images guidance](https://github.blog/developer-skills/github/how-to-make-your-images-in-markdown-on-github-adjust-for-dark-mode-and-light-mode/).

</details>

---

<div align="center">

**BUILDING RELIABLE SYSTEMS**

<sub>HEY@EMMETTS.DEV &middot; EMMETTSHAUGHNESSY.COM</sub>

</div>
