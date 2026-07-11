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
> &middot; **Internal data platform, self-serve financials.** Widened a financial reporting dataset to full column parity with its source system and backfilled roughly 525K historical rows across two tenants with dollar totals preserved exactly. Then stood up a FastAPI gateway on Azure Container Apps (managed identity to Azure SQL, keyset pagination, strict input allowlisting) so a business-critical spreadsheet refreshes live over identity instead of a direct database connection, clearing the path to retire an internet-open SQL firewall rule.
>
> &middot; **Native Rust CLI for the internal agent platform.** Built the core of a token-free terminal client for an internal MCP task-orchestration system: a hand-rolled streaming HTTP/SSE transport verified against a live server, OAuth 2.0 / PKCE login with OS-keyring tokens, full parity across the server's tool surface, and a numpad-driven TUI triage cockpit. It rides a three-OS CI grid with a supply-chain gate, cross-platform installers published to Azure Blob Storage.
>
> &middot; **ND-300 / SpeedQX, measurement honesty.** The Qube TX network-diagnostics line shipped a statistical-integrity pass across the Rust CLI, website, and iOS app: it withholds the cross-provider agreement figure on low-source runs, names upstream rate limits plainly instead of surfacing them as parse errors, short-circuits redundant probes into an already-tripped limiter, and cleared a RUSTSEC advisory. [Repository](https://github.com/QubeTX/qube-network-diagnostics).

---

## SELECTED SYSTEMS

<table>
<tr>
<td width="11%" valign="top"><strong>001</strong><br><sub>SYSTEMS</sub></td>
<td width="61%" valign="top">

### [Qube TX](https://qubetx.com)
`Rust` `TypeScript` `Next.js` `CLI`

Diagnostics tooling and web studio work centered on Rust CLIs, installers, updater reliability, and the marketing surfaces that explain them. The line now spans machine reporting (TR-300) and network diagnostics (ND-300 / SpeedQX): a cross-platform CLI with 25 deep network checks and a six-provider merged speed test with confidence intervals, unified under the SpeedQX Methodology 4.0 spec and a recent statistical-integrity pass that withholds low-confidence agreement stats and names upstream rate limits plainly. Both ship as canonical crates with native Windows distribution, cross-platform collector hardening, installer hash checks, and single-install migration cleanup.

</td>
<td width="28%" valign="top">

**Evidence**

[TR-300](https://github.com/QubeTX/qube-machine-report)<br>
[ND-300](https://github.com/QubeTX/qube-network-diagnostics)<br>
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

A rebuilt cross-platform pantry app on Supabase, Expo, Realtime, RLS, and AI edge functions. It is now in store-release prep with a signed Android build and full listing assets, an offline-first collaborative list with durable queue replay and row-level merge, and an AI layer on Sonnet 5 for categorization, recipe generation, substitutions, and schema-aware URL import.

</td>
<td width="28%" valign="top">

**Evidence**

Store-ready build<br>
Sonnet 5 AI layer<br>
Recipe URL import

</td>
</tr>
<tr>
<td width="11%" valign="top"><strong>004</strong><br><sub>AGENTS</sub></td>
<td width="61%" valign="top">

### [shaughv-code](https://github.com/RealEmmettS/shaughv-code)
`Codex` `Skills` `MCP` `Design`

My personal Codex and Claude Code plugin and skill library. It packages practical operating systems for design, reasoning, security review, audio, Mistral API work, human changelogs, branch control, status lines, image work, storage, handoffs, and summary conventions into one portable repository. Recent releases rebuilt the usage-statusline with live burn-rate bars, trend arrows, and a git-branch readout, then scoped the subagent-model-preference skill to Claude only and dropped it from the Codex package build. The task and workplace-memory skills also ship separately as shaughv-tasks.

</td>
<td width="28%" valign="top">

**Evidence**

[Repository](https://github.com/RealEmmettS/shaughv-code)<br>
`v0.32.0` plugin<br>
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
<td><code>SQL Server pipelines</code> &middot; <code>managed-identity data gateways</code> &middot; <code>freshness + observability</code></td>
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
- **Magic Pantry, store push.** A signed Android build, Play Store listing art and device screenshots, and a standing review account now sit on top of the offline-first realtime core, with the AI recipe trio moved to Sonnet 5 adaptive high-effort and recipe-URL import rebuilt around a schema.org JSON-LD fast path.
- **ND-300 / SpeedQX v3.5.x.** The Qube TX network-diagnostics CLI (`nd300` + `speedqx`) reached a hardening release: 25 deep network checks, a six-provider merged speed test (M-Lab NDT7/MSAK, Apple networkQuality, LibreSpeed, Cloudflare, fast.com) with inverse-variance weighting and bootstrap confidence intervals, an evidence-driven auto-remediation fix loop, and a Windows installer matrix with hardened self-update. SpeedQX Methodology 4.0 pins the measurement spec byte-identical across the website, app, and CLI; the latest pass withholds the I-squared agreement figure on low-source runs, names M-Lab Locate rate limits honestly, short-circuits redundant probes, and cleared a RUSTSEC advisory across CLI 3.5.2, website 3.0.11, and iOS 2.1.0.
- **shaughv-code v0.32.0.** Rebuilt the usage-statusline (live context and burn-rate bars, trend arrows, threshold coloring, eighth-block precision, worktree-aware git branch and thinking-level readout), then scoped the subagent-model-preference skill to Claude only and excluded it from the Codex package build so the exclusion is enforced identically on regenerate and validate. The bundle spans design, audio, Mistral, Quiver, security, changelogs, branch control, image work, storage, handoff, learning, productivity, and TT;DR summaries.
- **qork CLI v1.1.1.** The terminal shortener ships native installers, liveness checks, `qork help`, origin-aware uninstall, installer-preferred updates, and source attribution back into QorkMe analytics.

</details>

<details>
<summary><strong>Secondary surfaces,</strong> public workshop</summary>

&nbsp;

- **SHAUGHV brand system.** `shaughv-cdn` hosts versioned brand assets, fonts, and static/animated mark drop-ins behind a manifest at [`cdn.shaughv.com/tree.json`](https://cdn.shaughv.com/tree.json). `shaughv_vintage` carries the cream-and-sage personal portfolio variant, Pretext text fitting, scrollspy, dot-field motion, and project-level automation.
- **Agent task plugin.** [`shaughv-tasks`](https://github.com/RealEmmettS/shaughv-tasks) is the task-queue and workplace-memory system split out of `shaughv-code` into its own dual-surface Claude Code + Codex plugin. Its 0.2.0 platform release added milestones, verification gates, shared multi-board support with safety guards, and a secure store, and it is distributed through both marketplaces and `npx skills add`.
- **goose.** [`goose`](https://github.com/RealEmmettS/goose) is a Rust desktop-companion app remade for modern computing with original bundled assets, a milestone-driven engine (task state machine, audio, hit-testing, foreign-window perch, multi-monitor), and a CLI/TUI control plane, now with cross-platform CI across its M16 to M18 readiness track (macOS universal-binary checks, headless Linux and Wayland smoke tests).
- **Video and media.** `italy-trip-video` is a Remotion birthday-trip slideshow with timed captions and a CapCut polish path. It was scaffolded through the video workflow in `shaughv-code`.
- **Web tools.** `qrgen` is a QR-code generator and AI styling surface with a SHAUGHV product UI. `realtime2_test` is an OpenAI Realtime API voice-agent prototype with pure shared handlers across Express and Vercel functions.
- **Qube TX surfaces.** [`qube-machine-report-homepage`](https://github.com/QubeTX/qube-machine-report-homepage), [`qube-reports-executables`](https://github.com/QubeTX/qube-reports-executables), the [ND-300 network-diagnostics CLI](https://github.com/QubeTX/qube-network-diagnostics), [SpeedQX](https://github.com/QubeTX/speedtest), and SD-300 sit around the main diagnostics product line.
- **Client and artist sites.** [Dorsey 2026](https://github.com/QubeTX/dorsey_2026_BETA) rebuilds a touring musician's web presence on the modern Next.js / React / Tailwind stack while preserving the original visual language.

</details>

<details>
<summary><strong>Private systems,</strong> summarized without repo links</summary>

&nbsp;

- **Agent-orchestration tooling.** Native Rust CLIs (two-crate Cargo workspaces) for an internal MCP task-orchestration platform, CI-gated from the first commit: formatting, linting, a three-OS test grid, an MSRV job, and a supply-chain gate. Between them they carry OAuth 2.0 / PKCE auth with OS-keyring tokens, a hand-rolled streaming HTTP/SSE MCP transport verified against a live server, full parity across the server's tool surface, a client-side validator of roughly thirty rules that rejects malformed writes before the network, a hermetic harness that boots a throwaway server for true end-to-end tests, a numpad-driven TUI triage cockpit, and a one-command dispatch that prepares a git worktree and launches a coding agent. Cross-platform installers build in CI and publish to Azure Blob Storage behind a signed checksum manifest via federated identity (OIDC).
- **Shipping and platform infrastructure.** Migrated CI and deploys for roughly nine repositories off hosted GitHub Actions onto a self-hosted, Docker-free runner running as a KEDA-scaled Azure Container Apps consumption job, after exhausted shared Actions minutes had frozen releases: swapped a Docker-based static-web-app deploy for the SWA CLI, moved image builds to managed ACR, and repointed the org-wide reusable CI gate, pilot-first behind an operator sign-off. Also cleared a static-web-app staging-environment cap that had blocked all PR previews and stood up multi-region uptime monitoring with 2-of-3-region failure alerting on an existing telemetry resource.
- **Data platform reliability.** Widened a financial reporting dataset to full column parity with its source system, backfilled roughly 525K historical rows across two tenants with dollar totals preserved exactly, and materialized integrated views the workbook reads directly. Resumed a paused Azure Container Apps ingestion tier with rate-limit-aware polling against an external REST API and verified a full day with no HTTP 429 recurrence; triaged a failing weekly full-reconcile gap-healing job; and audited an upstream API's monthly changelog against only the endpoints in use to confirm no regression. Python sync workers over SQL Server with Service Bus queues and App Insights observability.
- **Security and access hardening.** Stood up a FastAPI data-gateway Container App (managed identity to Azure SQL, Entra-gated auth, keyset pagination, strict input allowlisting) as the path to move a business-critical spreadsheet off a direct database connection and retire an internet-open SQL firewall rule. Ran a security sweep that closed a live unauthenticated data-browse endpoint, rotated an OAuth client secret committed to a tracked file, and purged personal data from git history. Proved Entra ID app-role, per-identity authorization on a shared MCP endpoint with a one-row canary before any sensitive labor data landed.
- **Reporting product and embedded AI.** Gave an in-report AI chat agent confirm-gated write access through Claude tool-use so it edits structured answers and settings that propagate into the rendered narrative, with full change attribution. Migrated the default model to a newer Sonnet-class Claude model with token streaming, reworked per-report chat into a shared attributed transcript, and added a CDN-first cross-user media cache with webhook-driven freshness and upstream-throttle protection. Python / FastAPI and React / TypeScript on Azure Container Apps and Static Web Apps.
- **Operator and projection surfaces.** Fixed a row-shift correctness bug in a spreadsheet-backed projection tool by keying pinned cells to a stable project code via XLOOKUP, unblocking an unattended daily cloud refresh scoped to a least-privilege Microsoft Graph permission. Shipped WCAG-AA tri-state dark-mode token systems across multiple products and upstreamed them into the canonical internal design system.

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
