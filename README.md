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

I build operational software that survives real installers, real users, and real release loops. Current focus: Qube TX diagnostics, Goose's native desktop lifecycle, and portable agent tooling.

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
> &middot; **SD-300 v2.0.6, hardware truth and installer lifecycle.** Expanded the Rust system-diagnostics CLI with explicit observation/provenance, live-qualified driver and thermal reporting, and managed install/update/uninstall across Windows, macOS, and Linux. The release qualifies channel-preserving updates, deliberate same-scope reinstalls, ownership cleanup, checksums, and already-current behavior across native packages, managed scripts, and Cargo. [Release](https://github.com/QubeTX/qube-system-diagnostics/releases/tag/v2.0.6)
>
> &middot; **Goose v1.3.3, Windows lifecycle hardening.** Shipped the Rust desktop companion with detached CLI startup, single-instance protection across launch aliases, resilient notification-area recovery after Explorer restarts, and read-only update discovery. The latest release detaches the Windows runtime from terminal jobs and resolves host architecture correctly inside app terminals, so long-running sessions survive closing the shell and Windows still picks the right native installer. [Release](https://github.com/RealEmmettS/goose/releases/tag/v1.3.3)
>
> &middot; **shaughv-tasks 1.0, portable agent task boards go stable.** The companion task and workplace-memory layer reached its first stable release, adding titled project boards, board interaction fixes, and bundle upgrades on every task start so dashboards self-repair on resume. It now runs as the shared operating board across the Rust diagnostics line and the goose desktop companion, giving each coding agent the same verified task surface. [shaughv-tasks](https://github.com/RealEmmettS/shaughv-tasks)

---

## SELECTED SYSTEMS

<table>
<tr>
<td width="11%" valign="top"><strong>001</strong><br><sub>SYSTEMS</sub></td>
<td width="61%" valign="top">

### [Qube TX](https://qubetx.com)
`Rust` `Installers` `Security` `CI`

Diagnostics tooling and web studio work centered on Rust CLIs that stay honest from hardware probe to public installer. The current line spans TR-300 v4.2.2 machine reporting, ND-300 v3.7.3 network diagnostics / SpeedQX, and SD-300 v2.0.6 system diagnostics. Recent releases preserve proven installer ownership, fail closed on ambiguous state, pin exact artifacts after versionless discovery, ship signed/notarized macOS packages plus native Windows channels, and qualify migrations, reinstalls, rollback, uninstall, checksums, attestations, and already-current JSON on hosted targets and physical Windows hardware.

</td>
<td width="28%" valign="top">

**Evidence**

[TR-300 v4.2.2](https://github.com/QubeTX/qube-machine-report/releases/tag/v4.2.2)<br>
[ND-300 v3.7.3](https://github.com/QubeTX/qube-network-diagnostics/releases/tag/v3.7.3)<br>
[SD-300 v2.0.6](https://github.com/QubeTX/qube-system-diagnostics/releases/tag/v2.0.6)<br>
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

My portable Codex and Claude Code operating kit. shaughv-code v0.35.0 packages brand design, critical thinking, security, audio, Mistral, image, Git, release, and workflow skills with shared MCP integrations. shaughv-tasks reached its first stable 1.0.1 release: titled project boards, milestone-aware task queues, verification gates, multi-board safety, secure local storage, and bundle upgrades on every task start. It now runs as the shared board across the diagnostics line and goose.

</td>
<td width="28%" valign="top">

**Evidence**

[Repository](https://github.com/RealEmmettS/shaughv-code)<br>
[v0.35.0 manifest](https://github.com/RealEmmettS/shaughv-code/blob/main/.codex-plugin/plugin.json)<br>
[shaughv-tasks v1.0.1](https://github.com/RealEmmettS/shaughv-tasks/blob/main/.claude-plugin/plugin.json)

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

- **SD-300 v2.0.6.** Expanded hardware diagnostics, provenance, driver and thermal reporting, then qualified native and managed update, reinstall, migration, rollback, uninstall, checksum, and already-current paths across the public release lanes.
- **Goose v1.3.3.** Hardened detached Windows startup, single-instance handling, notification-area recovery, read-only update discovery, terminal-host architecture detection, and origin-preserving native installation, then detached the Windows runtime from terminal jobs so sessions outlive the shell.
- **ND-300 / SpeedQX v3.7.3.** Added a signed, notarized, stapled universal PKG as the direct macOS channel while keeping a byte-identical DMG bridge for immutable older updaters. The 32-asset release passed hosted Intel/Apple Silicon, public Windows-origin, checksum, attestation, and physical Windows update gates.
- **TR-300 v4.2.2.** Moved ambiguous native Mac ownership checks ahead of package payload mutation, kept Windows current and legacy asset contracts distinct, and made generated PKG lifecycle scripts part of the release lint gate.
- **shaughv-code v0.35.0 / shaughv-tasks v1.0.1.** The skills bundle now spans the current brand, reasoning, security, media, release, and workflow toolkit; the task plugin reached its first stable 1.0 release with titled project boards, board interaction fixes, and bundle upgrades on every task start, then rolled out as the shared board across the diagnostics repos and goose.
- **Magic Pantry, store push.** A signed Android build and store assets sit on top of the offline-first realtime core, with AI recipe generation and schema-aware URL import prepared for release review.

</details>

<details>
<summary><strong>Secondary surfaces,</strong> public workshop</summary>

&nbsp;

- **SHAUGHV brand system.** `shaughv-cdn` hosts versioned brand assets, fonts, and static/animated mark drop-ins behind a manifest at [`cdn.shaughv.com/tree.json`](https://cdn.shaughv.com/tree.json). `shaughv_vintage` carries the cream-and-sage personal portfolio variant, Pretext text fitting, scrollspy, dot-field motion, and project-level automation.
- **Agent task plugin.** [`shaughv-tasks`](https://github.com/RealEmmettS/shaughv-tasks) is the task-queue and workplace-memory system split out of `shaughv-code`. Version 1.0.1 is the first stable release: titled project boards, milestones, verification gates, shared multi-board safety, secure local storage, and bundle upgrades on every task start across marketplace and skills-only installs.
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
