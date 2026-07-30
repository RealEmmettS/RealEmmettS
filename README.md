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

I build operational software that survives real installers, real users, and real release loops. Current focus: shipping the Magic Pantry mobile app to the iOS App Store, the Qube TX diagnostics line and its published CLI lifecycle contract, and portable agent and MCP tooling.

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
> &middot; **Magic Pantry v2.0.4, into the iOS App Store.** The rebuilt cross-platform pantry app moved from store prep into active App Store submission: TestFlight builds live through build 20 and App Review readiness verified. The v2.0.4 candidate adds saved-recipe source links, keyboard-safe list actions, and category/import fixes on top of the offline-first realtime core and Sonnet 5 AI layer.
>
> &middot; **Google Health MCP v0.3.0, hardened auth and transport.** The public TypeScript Model Context Protocol server moved to a stateless JWT auth provider, added a DPoP-capable Google credential fallback, and upgraded its transport to MCP SDK v2, on top of the encrypted sync and trend surfaces already in production. The release also adds a downloadable mark and platform-paired connector setup. [Repository](https://github.com/RealEmmettS/Google-Health-MCP)
>
> &middot; **shaughv-code 1.1.1, new default type system.** My portable Codex and Claude Code kit shipped 1.1.0 and 1.1.1 on top of the 1.0 stable plugin contract, promoting Makira and Gail Rock to the default type system and making the CDN skill fully manifest-driven. It keeps the self-routing orchestration and the brand, reasoning, security, media, release, and workflow skills in one bundle. [Repository](https://github.com/RealEmmettS/shaughv-code)

---

## SELECTED SYSTEMS

<table>
<tr>
<td width="11%" valign="top"><strong>001</strong><br><sub>SYSTEMS</sub></td>
<td width="61%" valign="top">

### [Qube TX](https://qubetx.com)
`Rust` `Installers` `Security` `CI`

Diagnostics tooling and web studio work centered on Rust CLIs that stay honest from hardware probe to public installer. The current line spans TR-300 v4.2.2 machine reporting, ND-300 v3.7.3 network diagnostics / SpeedQX, and SD-300 v3.1.3 system diagnostics, a dual-frontend product with a native desktop GUI, a system-tray app with background monitoring, transparent cross-platform icons, and safe in-app and tray-driven self-updates. Install, update, rollback, and uninstall behavior now has a published, immutable reference contract. Releases preserve proven installer ownership, fail closed on ambiguous state, pin exact artifacts after versionless discovery, ship signed/notarized macOS packages plus native Windows channels, keep published version tags immutable, and qualify reinstalls, rollback, checksums, and attestations on hosted targets and physical Windows hardware.

</td>
<td width="28%" valign="top">

**Evidence**

[TR-300 v4.2.2](https://github.com/QubeTX/qube-machine-report/releases/tag/v4.2.2)<br>
[ND-300 v3.7.3](https://github.com/QubeTX/qube-network-diagnostics/releases/tag/v3.7.3)<br>
[SD-300 v3.1.3](https://github.com/QubeTX/qube-system-diagnostics/releases/tag/v3.1.3)<br>
[Lifecycle contract](https://github.com/QubeTX/qube-cli-lifecycle-contract)

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

A rebuilt cross-platform pantry app on Supabase, Expo, Realtime, RLS, and AI edge functions. The v2.0.4 candidate is in active iOS App Store submission, with TestFlight builds live through build 20 and App Review readiness verified. It ships an offline-first collaborative list with durable queue replay and row-level merge, saved-recipe source links, and an AI layer on Sonnet 5 for categorization, recipe generation, substitutions, and schema-aware URL import.

</td>
<td width="28%" valign="top">

**Evidence**

iOS App Store submission<br>
v2.0.4, TestFlight build 20<br>
Sonnet 5 AI layer

</td>
</tr>
<tr>
<td width="11%" valign="top"><strong>004</strong><br><sub>AGENTS</sub></td>
<td width="61%" valign="top">

### [shaughv-code](https://github.com/RealEmmettS/shaughv-code)
`Codex` `Skills` `MCP` `Design`

My portable Codex and Claude Code operating kit. shaughv-code reached 1.1.1 on a documented plugin contract with self-routing orchestration, promoting Makira and Gail Rock to the default type system and making the CDN skill manifest-driven, on top of brand design, critical thinking, security, audio, image, Git, release, and workflow skills plus shared MCP integrations and a loop-escape convergence-recovery skill for agents that stall in retry loops. shaughv-tasks reached 1.1.0 with evidence-aware task contracts on scoped convergence: titled project boards, milestone-aware queues, verification gates, multi-board safety, and secure local storage. It runs as the shared board across the diagnostics line, goose, and the Google Health MCP server.

</td>
<td width="28%" valign="top">

**Evidence**

[Repository](https://github.com/RealEmmettS/shaughv-code)<br>
[Skills manifest](https://github.com/RealEmmettS/shaughv-code/blob/main/.codex-plugin/plugin.json)<br>
[shaughv-tasks v1.1.0](https://github.com/RealEmmettS/shaughv-tasks/blob/main/.claude-plugin/plugin.json)

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
<td><code>Azure SQL + data gateways</code> &middot; <code>managed-identity + OIDC deploys</code> &middot; <code>self-hosted CI + observability</code></td>
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
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-204F20?logo=githubactions&logoColor=F5E0C5)
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
<td width="100%" align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com?user=RealEmmettS&background=204F20&stroke=F5E0C5&ring=F5E0C5&fire=F5E0C5&currStreakNum=F5E0C5&sideNums=F5E0C5&currStreakLabel=F5E0C5&sideLabels=F5E0C5&dates=F5E0C5">
  <img alt="GitHub streak" src="https://streak-stats.demolab.com?user=RealEmmettS&background=F5E0C5&stroke=204F20&ring=204F20&fire=204F20&currStreakNum=204F20&sideNums=204F20&currStreakLabel=204F20&sideLabels=204F20&dates=204F20">
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

- **SD-300 v3.1.3.** Shipped transparent cross-platform app icons, an art-directed transparent-corner macOS mark, an unchanged monochrome tray identity, and deterministic icon validation across the dual-frontend system-diagnostics product, on top of the native desktop GUI, system-tray background monitoring, and safe self-updates. Full local and hosted six-target release gates passed.
- **Qube CLI Lifecycle v2.** Published a public, reference-only behavioral contract for Qube CLI install, update, rollback, and uninstall, released as an immutable contract version so the diagnostics line has a single documented lifecycle spec.
- **Google Health MCP v0.3.0.** Moved the public TypeScript Model Context Protocol server to a stateless JWT auth provider, added a DPoP-capable Google credential fallback, and upgraded transport to MCP SDK v2, on top of encrypted sync, trend surfaces, a Claude token handoff, and a vintage SHAUGHV health web surface. Ships a downloadable mark and platform-paired connector setup, running in production and bundled into shaughv-code.
- **Goose v1.3.7.** Hardened Windows update delivery with transport-safe updater archive paths, the update helper owning the runtime restart, and a tray completion notification, on top of detached startup, single-instance handling, and notification-area recovery, then moved its shared task board to shaughv-tasks 1.0.2.
- **ND-300 / SpeedQX v3.7.3.** Added a signed, notarized, stapled universal PKG as the direct macOS channel while keeping a byte-identical DMG bridge for immutable older updaters. The 32-asset release passed hosted Intel/Apple Silicon, public Windows-origin, checksum, attestation, and physical Windows update gates.
- **TR-300 v4.2.2.** Moved ambiguous native Mac ownership checks ahead of package payload mutation, kept Windows current and legacy asset contracts distinct, and made generated PKG lifecycle scripts part of the release lint gate.
- **shaughv-code 1.1.1 / shaughv-tasks 1.1.0.** The skills bundle reached 1.1.1 on a documented plugin contract and self-routing orchestration, promoting Makira and Gail Rock to the default type system and making the CDN skill manifest-driven on top of the brand, reasoning, security, media, release, and workflow toolkit; the task plugin reached 1.1.0 with evidence-aware task contracts over scoped convergence, titled project boards, and verification gates, running as the shared board across the diagnostics repos, goose, and the Google Health MCP server.
- **Magic Pantry v2.0.4, App Store submission.** Moved from store prep into active iOS App Store submission with TestFlight builds live through build 20 and App Review readiness verified, adding saved-recipe source links, keyboard-safe list actions, and category/import fixes on top of the offline-first realtime core and Sonnet 5 AI layer.

</details>

<details>
<summary><strong>Secondary surfaces,</strong> public workshop</summary>

&nbsp;

- **SHAUGHV brand system.** `shaughv-cdn` hosts versioned brand assets, fonts, and static/animated mark drop-ins behind a manifest at [`cdn.shaughv.com/tree.json`](https://cdn.shaughv.com/tree.json). `shaughv_vintage` carries the cream-and-sage personal portfolio variant, Pretext text fitting, scrollspy, dot-field motion, and project-level automation.
- **Agent task plugin.** [`shaughv-tasks`](https://github.com/RealEmmettS/shaughv-tasks) is the task-queue and workplace-memory system split out of `shaughv-code`. Version 1.1.0 adds evidence-aware task contracts over the stable line: titled project boards, milestones, verification gates, shared multi-board safety, secure local storage, and bundle upgrades on every task start across marketplace and skills-only installs.
- **Health data MCP.** [`Google-Health-MCP`](https://github.com/RealEmmettS/Google-Health-MCP) is a public TypeScript Model Context Protocol server that brings Google Health data into agent workflows with encrypted sync, trend surfaces, OAuth hardening, and a Claude token handoff. Version 0.3.0 runs in production with stateless JWT auth, a DPoP credential fallback, and MCP SDK v2 transport behind a vintage SHAUGHV health surface.
- **goose.** [`goose`](https://github.com/RealEmmettS/goose) is a Rust desktop companion rebuilt for modern operating systems with the original bundled assets, a milestone-driven engine, audio, hit-testing, foreign-window perch, multi-monitor support, and a CLI/TUI control plane. Native releases are qualified across Windows, macOS, and Linux.
- **Video and media.** `italy-trip-video` is a Remotion birthday-trip slideshow with timed captions and a CapCut polish path. It was scaffolded through the video workflow in `shaughv-code`.
- **Web tools.** `qrgen` is a QR-code generator and AI styling surface with a SHAUGHV product UI. `realtime2_test` is an OpenAI Realtime API voice-agent prototype with pure shared handlers across Express and Vercel functions.
- **Qube TX surfaces.** [`qube-machine-report-homepage`](https://github.com/QubeTX/qube-machine-report-homepage), [`qube-reports-executables`](https://github.com/QubeTX/qube-reports-executables), the [ND-300 network-diagnostics CLI](https://github.com/QubeTX/qube-network-diagnostics), [SpeedQX](https://github.com/QubeTX/speedtest), and SD-300 sit around the main diagnostics product line.
- **Client and artist sites.** [Dorsey 2026](https://github.com/QubeTX/dorsey_2026_BETA) rebuilds a touring musician's web presence on the modern Next.js / React / Tailwind stack while preserving the original visual language.

</details>

<details>
<summary><strong>Private systems,</strong> summarized without repo links</summary>

&nbsp;

- **Agent orchestration.** Rust MCP clients and ratatui control surfaces with OAuth 2.0 / PKCE, keyring storage, SSE transport, preflight validation, hermetic end-to-end tests, and one-command worktree/agent dispatch. CI produces cross-platform, self-updating per-user installers through federated cloud identity.
- **Shipping infrastructure.** Moved multi-repository CI and deploys to a self-hosted, scale-to-zero cloud runner, then tightened reusable gates with linting, secret scanning, dual review, OIDC, and multi-region alerts. Preview environments and production deploys remain token-minimized.
- **Data reliability.** Hardened Python/FastAPI and SQL Server pipelines with deduplication, transactional error logging, managed identity, strict query allowlists, keyset pagination, queue-driven sync, rate-limit-aware polling, and Azure observability. Restored self-serve refresh paths and guarded view swaps against empty publishes.
- **Security and access.** Closed unauthenticated browse paths, purged committed secrets, rotated credentials, moved agents behind operator-only completion gates, and proved Entra app-role authorization with a canary before sensitive workloads.
- **Embedded AI and operator surfaces.** Built confirm-gated Claude tool use into a React/FastAPI reporting surface with shared attributed transcripts, streaming, CDN caching, webhook freshness, and WCAG-AA dark-mode tokens.

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
| `&lt;picture&gt;` + `prefers-color-scheme` | Streak card, activity graph |
| GFM alert (`> [!NOTE]`) | `LATEST SHIPS` |
| `<details>` / `<summary>` | TOC, archive sections, colophon |
| HTML tables | Hero proof strip, selected systems, stats card |
| Live shields | Contact pills, profile metrics, stack badges |
| Theme-aware widget cards | Streak, activity graph |
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
