<!-- ====================================================================== -->
<!--  EMMETT SHAUGHNESSY · GITHUB PROFILE                                   -->
<!--                                                                        -->
<!--  Hand-built within the limits of GitHub's markdown sanitizer.          -->
<!--  No JavaScript, no CSS, no inline SVG, no GitHub Actions.              -->
<!--  Every dynamic element is GFM, a sanitizer-safe HTML tag, or a         -->
<!--  parameterized image URL rendered live on every page load.             -->
<!--                                                                        -->
<!--  Scroll to the COLOPHON at the bottom for the full catalogue of        -->
<!--  techniques used in this file.                                         -->
<!-- ====================================================================== -->

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://capsule-render.vercel.app/api?type=waving&color=204F20&height=200&section=header&text=EMMETT%20SHAUGHNESSY&fontColor=F5E0C5&fontSize=52&fontAlignY=38&desc=DIGITAL%20CRAFTSMAN&descSize=16&descAlignY=58&descAlign=50&animation=fadeIn">
  <img alt="Emmett Shaughnessy, Digital Craftsman" src="https://capsule-render.vercel.app/api?type=waving&color=F5E0C5&height=200&section=header&text=EMMETT%20SHAUGHNESSY&fontColor=204F20&fontSize=52&fontAlignY=38&desc=DIGITAL%20CRAFTSMAN&descSize=16&descAlignY=58&descAlign=50&animation=fadeIn">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&duration=2400&pause=1200&color=F5E0C5&center=true&vCenter=true&width=640&lines=full-stack+developer+%C2%B7+rust+%2B+typescript;founder%2C+qube+tx+%C2%B7+diagnostics+%26+web+studio;building+magic+pantry%2C+dorsey+2026%2C+shaughv+os;shipping+reliable+systems+since+2017">
  <img alt="full-stack developer · rust + typescript · founder, qube tx · building magic pantry, dorsey 2026, shaughv os · shipping reliable systems since 2017" src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&duration=2400&pause=1200&color=204F20&center=true&vCenter=true&width=640&lines=full-stack+developer+%C2%B7+rust+%2B+typescript;founder%2C+qube+tx+%C2%B7+diagnostics+%26+web+studio;building+magic+pantry%2C+dorsey+2026%2C+shaughv+os;shipping+reliable+systems+since+2017">
</picture>

<br>

[![Profile views](https://komarev.com/ghpvc/?username=RealEmmettS&style=for-the-badge&color=204F20&labelColor=F5E0C5&label=PROFILE+VIEWS)](https://github.com/RealEmmettS)
[![Followers](https://img.shields.io/github/followers/RealEmmettS?style=for-the-badge&color=204F20&labelColor=F5E0C5&logo=github&logoColor=204F20&label=FOLLOWERS)](https://github.com/RealEmmettS?tab=followers)
[![Last push](https://img.shields.io/github/last-commit/RealEmmettS/RealEmmettS?style=for-the-badge&color=204F20&labelColor=F5E0C5&logo=git&logoColor=204F20&label=LAST+PUSH)](https://github.com/RealEmmettS/RealEmmettS/commits/master)
[![Stars](https://img.shields.io/github/stars/RealEmmettS?style=for-the-badge&affiliations=OWNER%2CCOLLABORATOR&color=204F20&labelColor=F5E0C5&label=STARS)](https://github.com/RealEmmettS?tab=repositories&sort=stargazers)

<br>

I build full-stack products, Rust diagnostics, and the systems that ship them. Currently a workshop of Qube TX, Magic Pantry, and Dorsey 2026.

[![Website](https://img.shields.io/badge/WEBSITE-204F20?style=for-the-badge&logo=About.me&logoColor=F5E0C5)](https://emmettshaughnessy.com)
[![Qube TX](https://img.shields.io/badge/QUBE_TX-F5E0C5?style=for-the-badge&labelColor=204F20&logoColor=204F20)](https://qubetx.com)
[![Resume](https://img.shields.io/badge/RESUME-204F20?style=for-the-badge&logo=readdotcv&logoColor=F5E0C5)](https://resume.emmetts.dev)
[![Email](https://img.shields.io/badge/EMAIL-F5E0C5?style=for-the-badge&labelColor=204F20&logo=maildotru&logoColor=204F20)](mailto:hey@emmetts.dev)

</div>

<details>
<summary><kbd> Jump to </kbd></summary>

&nbsp;

[`NOW`](#now) &nbsp;&middot;&nbsp; [`CURRENT WORK`](#current-work) &nbsp;&middot;&nbsp; [`STACK`](#stack) &nbsp;&middot;&nbsp; [`NUMBERS`](#numbers) &nbsp;&middot;&nbsp; [`COLOPHON`](#colophon)

</details>

---

## NOW

> [!NOTE]
> **MAY 2026, actively shipping**
>
> &middot; **TR-300 v3.14.x**, Windows hardening (vswhere + winget MSVC preflight, Display-formatted errors)
> &middot; **Magic Pantry**, Phase H account self-service + sharing hardening for App Store launch
> &middot; **Dorsey 2026**, secondary-route parity and final QA on the Next.js 16 / React 19 rebuild

---

## CURRENT WORK

<table>
<tr>
<td width="50%" valign="top">

### [Qube TX](https://qubetx.com)
**Diagnostics tooling & web studio**

`Rust` `TypeScript` `Next.js` `CLI`

A growing ecosystem of Rust CLI diagnostics tools, all published to crates.io under canonical names. TR-300 is on the v3.14.x line as the `tr300` crate, recently hardened for Windows: a vswhere preflight that auto-installs MSVC Build Tools via winget so `cargo install` succeeds on a fresh machine, an execution-policy preflight, and a Display-formatted error path that maps native error codes to actionable advice. [`qube-network-diagnostics`](https://github.com/QubeTX/qube-network-diagnostics) (nd300 v3.0.x) ships hardened network-fix safety, an evidence-driven fix-loop with per-action stabilization windows, and a cargo-first / installer-fallback self-update chain that cleans up non-cargo installs on upgrade. [`qube-system-diagnostics`](https://github.com/QubeTX/qube-system-diagnostics) (SD-300, published as the `tr300-tui` crate) has a stabilized updater and runner-compatible release metadata. Around the CLIs sit the web surfaces: [`QubeTX_Landing`](https://github.com/QubeTX/QubeTX_Landing) and [`qube-machine-report-homepage`](https://github.com/QubeTX/qube-machine-report-homepage) (per-platform install one-liners, admin/sudo notes, and a chained `tr300 install` that writes the shell-profile alias and auto-run line in one paste), plus the multi-provider [SpeedQX](https://github.com/QubeTX/speedtest) web app (bootstrap CIs, inverse-variance weighted aggregation, RFC 3550 jitter) and offline installer bundles ([`qube-reports-executables`](https://github.com/QubeTX/qube-reports-executables)). Also where most freelance / client work lives.

</td>
<td width="50%" valign="top">

### [QorkMe](https://qork.me)
**URL shortener**

`Next.js` `TypeScript` `Supabase` `Tailwind`

Custom aliases, click analytics, and a clean redirect layer on a Next.js + Supabase stack. Hardened Supabase RLS (INSERT policy on clicks, `SECURITY DEFINER` increment, owner-only UPDATE/DELETE, revoked TRUNCATE from anon/authenticated), bounded the URL redirect cache, optimized AdminLinksTable maxClicks, consolidated to a Makira-only typeface, and refreshed the admin dashboard.

</td>
</tr>
<tr>
<td width="50%" valign="top">

### shaughvOS
**Custom diagnostics OS**

`Shell` `Linux` `Build Pipelines`

Lightweight Debian-based diagnostics OS with Shaughv branding. The v1.20.0 line stabilized install + startup validation behind a focus-smoke shellcheck gate and a release-newline check, on top of v1.19.x's CLI-first boot, working `/usr/local/bin/` desktop shortcuts, Tailscale + Tor Browser pre-installs, an `autologin` command decoupled from `desktop on/off`, and apt-mark drift fixes. The full ~400-tool IT + security toolset is scoped and queued behind the stability work.

</td>
<td width="50%" valign="top">

### [Dorsey 2026](https://github.com/QubeTX/dorsey_2026_BETA)
**Music artist site**

`Next.js 16` `React 19` `Tailwind v4` `Framer Motion`

A full rebuild of a touring artist's site on Next.js 16 / React 19 / Tailwind v4, with shadcn/ui components and Framer Motion choreography. Pivoted from a custom Jazz-Bauhaus reinterpretation to a faithful recreation of the live leonleedorsey.com visual language: header / footer reworked, home / about / music / store / videos / contact and several press / gear pages rebuilt, mobile nav swapped to a full-screen white sheet, and Squarespace media imported locally to avoid hotlinking. Currently in secondary route parity and final QA.

</td>
</tr>
<tr>
<td width="50%" valign="top">

### Magic Pantry
**Cross-platform pantry app**

`Expo` `React Native` `Supabase` `Anthropic`

Full rebuild of the Magic Pantry app, migrated off the prior Replit + Express + Drizzle + Modelfarm stack onto Supabase (Postgres + Auth + RLS + Realtime) with Expo SDK 55 / React Native 0.83 / React 19.2 / React Navigation v7 / TanStack Query v5. AI features (item categorization on Claude Haiku 4.5, recipe generation on Sonnet 4.6, URL recipe import via Firecrawl v2 + Sonnet 4.6, plus a service-role `delete-account` for App Store compliance) run through edge functions. Phase H wired full account self-service: forgot / reset / change password, change username, signup-confirmation flow with 60s-cooldown resend, end-to-end via `magicpantry://` deep links for App Store launch, and tightened sharing so non-owner projections drop emails entirely and `findUserByUsernameOrEmail` returns username + id only. RLS helpers live in a `private` schema, `citext` was moved out of `public`, and usernames are `citext` for case-insensitive uniqueness.

</td>
<td width="50%" valign="top">

### [Personal Site](https://emmettshaughnessy.com)
**Portfolio & writing**

`TypeScript` `Next.js` `Tailwind` `Vercel`

Professional showcase, project index, and technical writing on a Next.js stack with a Pretext-powered responsive text layer, Lenis-driven smooth scroll, Anime.js choreography, and a forced-dark `/works` route whose filter rail wraps instead of scrolling on narrow viewports. Vercel Analytics in production; recent passes covered design-system docs, an explicit pre-push checklist in `CLAUDE.md`, and a Claude Code GitHub workflow with `pull-requests: write` so the bot can actually post its reviews.

</td>
</tr>
</table>

<details>
<summary><strong>Also in the workshop,</strong> a dozen more repos &amp; surfaces</summary>

&nbsp;

Web surfaces around the Qube TX ecosystem ([`QubeTX_Landing`](https://github.com/QubeTX/QubeTX_Landing), [`qube-machine-report-homepage`](https://github.com/QubeTX/qube-machine-report-homepage), [`qube-reports-executables`](https://github.com/QubeTX/qube-reports-executables) for offline installers), the [SpeedQX](https://github.com/QubeTX/speedtest) web speed-test app and its parallel Expo / React Native port (v2.0 technician-grade accuracy overhaul, network metadata, jitter breakdown, bootstrap CI, inverse-variance weighting), `shaughv_vintage` (vintage-leaning personal portfolio with a Pretext-powered responsive text layer and a consolidated nav + project-card a11y pass), a print-tuned [`resume-2026`](https://resume.emmetts.dev) on Makira / Personal-Vogue that auto-deploys via GitHub Pages, [Time](https://github.com/RealEmmettS/time) (atomic-clock alternative to time.gov with a Marzullo-uncertainty-based watch score), Remotion-based programmatic video experiments, MDX docs sites, and a rotating cast of small utilities (timer, qrgen, csv tools, countdown apps, movie list).

</details>

---

## STACK

```mermaid
%%{init: {'theme':'forest'}}%%
mindmap
  root((WHAT<br/>I BUILD))
    WEB
      Next.js apps
      Studio surfaces
      Marketing sites
    SYSTEMS
      Rust CLIs
      Debian images
      Build pipelines
    MOBILE
      Expo apps
      React Native
      iPad / iPhone
    BACKEND
      Supabase
      Edge functions
      AI integrations
```

<br>

### 2026 release timeline

| Quarter | Month | Shipped |
|:---:|:---:|---|
| **Q1** | **Jan** | TR-300 v3.12, QorkMe RLS hardening |
|        | **Feb** | Magic Pantry, Supabase migration |
|        | **Mar** | shaughvOS v1.18, CLI-first boot |
| **Q2** | **Apr** | Magic Pantry Phase G, auth flows |
|        | **May** | TR-300 v3.14 Windows, Magic Pantry Phase H, Dorsey 2026 port |

<br>

### Languages
![Rust](https://img.shields.io/badge/Rust-204F20?style=flat-square&logo=rust&logoColor=F5E0C5)
![TypeScript](https://img.shields.io/badge/TypeScript-204F20?style=flat-square&logo=typescript&logoColor=F5E0C5)
![JavaScript](https://img.shields.io/badge/JavaScript-204F20?style=flat-square&logo=javascript&logoColor=F5E0C5)
![Python](https://img.shields.io/badge/Python-204F20?style=flat-square&logo=python&logoColor=F5E0C5)
![Shell](https://img.shields.io/badge/Shell-204F20?style=flat-square&logo=gnubash&logoColor=F5E0C5)
![Swift](https://img.shields.io/badge/Swift-204F20?style=flat-square&logo=swift&logoColor=F5E0C5)

### Frameworks &amp; libraries
![Next.js](https://img.shields.io/badge/Next.js-204F20?style=flat-square&logo=nextdotjs&logoColor=F5E0C5)
![React](https://img.shields.io/badge/React-204F20?style=flat-square&logo=react&logoColor=F5E0C5)
![Tailwind v4](https://img.shields.io/badge/Tailwind_v4-204F20?style=flat-square&logo=tailwindcss&logoColor=F5E0C5)
![shadcn/ui](https://img.shields.io/badge/shadcn%2Fui-204F20?style=flat-square&logo=shadcnui&logoColor=F5E0C5)
![Framer Motion](https://img.shields.io/badge/Framer_Motion-204F20?style=flat-square&logo=framer&logoColor=F5E0C5)
![Expo](https://img.shields.io/badge/Expo-204F20?style=flat-square&logo=expo&logoColor=F5E0C5)
![Node.js](https://img.shields.io/badge/Node.js-204F20?style=flat-square&logo=nodedotjs&logoColor=F5E0C5)
![Remotion](https://img.shields.io/badge/Remotion-204F20?style=flat-square&logo=remotion&logoColor=F5E0C5)

### Cloud &amp; infrastructure
![Vercel](https://img.shields.io/badge/Vercel-204F20?style=flat-square&logo=vercel&logoColor=F5E0C5)
![Cloudflare](https://img.shields.io/badge/Cloudflare-204F20?style=flat-square&logo=cloudflare&logoColor=F5E0C5)
![AWS](https://img.shields.io/badge/AWS-204F20?style=flat-square&logo=amazonaws&logoColor=F5E0C5)
![Firebase](https://img.shields.io/badge/Firebase-204F20?style=flat-square&logo=firebase&logoColor=F5E0C5)
![Supabase](https://img.shields.io/badge/Supabase-204F20?style=flat-square&logo=supabase&logoColor=F5E0C5)

<details>
<summary><strong>More on what I'm building right now,</strong> full breakdown</summary>

&nbsp;

- **TR-300 Windows hardening.** On the v3.14.x line for the `tr300` crate: vswhere preflight that auto-installs MSVC Build Tools via winget so cargo install succeeds on a fresh box, an execution-policy preflight, and a Display-formatted error path that maps native error codes to actionable advice. The TR-300 install one-liner now chains `tr300 install` so a single paste also writes the shell-profile alias and auto-run line.
- **Magic Pantry.** Replit to Supabase migration plus Phase H: account self-service (forgot / reset / change password, change username, signup-confirmation flow with 60s-cooldown resend, `magicpantry://` deep links) and a sharing-hardening pass that scopes shared-list member projections to usernames-only and keeps emails out of the user-lookup API. RLS helpers in a `private` schema, `citext` moved out of `public`, Realtime, and Anthropic + Firecrawl edge functions for categorization / recipe generation / URL recipe import / account deletion.
- **nd300 + SD-300.** `qube-network-diagnostics` v3.0.x hardened the network-fix loop with per-action stabilization windows and a cargo-first / installer-fallback self-update chain that cleans up non-cargo installs on upgrade; `qube-system-diagnostics` republished as the canonical `tr300-tui` crate with stabilized updater and runner-compatible release metadata. Both on an automated crates-publish pipeline with CI version checks.
- **shaughvOS.** Debian-based diagnostics OS on the v1.20.0 line: install / startup validation, a focus-smoke shellcheck gate, release-newline check, CLI-first boot, working desktop shortcuts via `/usr/local/bin/` symlinks, Tailscale + Tor Browser pre-installs, and an `autologin` command decoupled from `desktop on/off`.
- **Dorsey 2026.** Touring artist's site rebuild on Next.js 16 / React 19 / Tailwind v4; in secondary route parity and final QA on the leonleedorsey.com port with imported Squarespace media.
- **Modern web stacks.** Next.js 16 / React 19 / Tailwind v4 / shadcn/ui builds for client sites and Qube TX surfaces (refreshed `qube-machine-report-homepage` with the chained one-liner installer, MSVC auto-install preflight on Windows, and per-platform admin / sudo notes), deployed on Vercel.
- **Full-stack product work.** QorkMe on Next.js + Supabase with hardened RLS (INSERT policy on clicks, `SECURITY DEFINER` increment, owner-only writes, revoked TRUNCATE), a bounded URL redirect cache with FIFO eviction, an O(N)-fix on `AdminLinksTable` maxClicks, and a consolidated Makira-only typography pass.
- **Cross-platform mobile.** Expo / React Native across Magic Pantry and the SpeedQX port carrying the v2.0 technician-grade accuracy overhaul (bootstrap CIs, inverse-variance weighting, AIM scores, byte-weighted progress) from the web app onto iPhone / iPad.
- **AI-assisted workflows.** Pairing Claude / Codex agents into real product development; release pipelines moved from foreground `gh run watch` to non-blocking Monitor poll-loops, with `gh --jq` keeping the diff portable across machines without local jq.
- **Technical consulting.** Pragmatic, end-to-end solutions for client work through Qube TX.

</details>

---

## NUMBERS

<div align="center">

![Public repos](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.github.com%2Fusers%2FRealEmmettS&query=%24.public_repos&style=for-the-badge&label=PUBLIC+REPOS&color=204F20&labelColor=F5E0C5)
![Total stars](https://img.shields.io/github/stars/RealEmmettS?style=for-the-badge&affiliations=OWNER&color=204F20&labelColor=F5E0C5&label=TOTAL+STARS)
![Public gists](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.github.com%2Fusers%2FRealEmmettS&query=%24.public_gists&style=for-the-badge&label=PUBLIC+GISTS&color=204F20&labelColor=F5E0C5)
![Following](https://img.shields.io/github/following/RealEmmettS?style=for-the-badge&color=204F20&labelColor=F5E0C5&label=FOLLOWING)
![On GitHub since](https://img.shields.io/badge/ON+GITHUB+SINCE-2017-204F20?style=for-the-badge&labelColor=F5E0C5)

</div>

<br>

<table align="center" width="100%">
<tr>
<td width="50%" align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-streak-stats.demolab.com?user=RealEmmettS&background=204F20&stroke=F5E0C5&ring=F5E0C5&fire=F5E0C5&currStreakNum=F5E0C5&sideNums=F5E0C5&currStreakLabel=F5E0C5&sideLabels=F5E0C5&dates=F5E0C5">
  <img alt="GitHub streak" src="https://github-readme-streak-stats.demolab.com?user=RealEmmettS&background=F5E0C5&stroke=204F20&ring=204F20&fire=204F20&currStreakNum=204F20&sideNums=204F20&currStreakLabel=204F20&sideLabels=204F20&dates=204F20">
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

<br>

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-profile-trophy.vercel.app/?username=RealEmmettS&theme=chalk&no-frame=true&no-bg=true&column=7&rank=SECRET,SSS,SS,S,AAA,AA,A&margin-w=4">
  <img alt="GitHub trophies" src="https://github-profile-trophy.vercel.app/?username=RealEmmettS&theme=flat&no-frame=true&no-bg=true&column=7&rank=SECRET,SSS,SS,S,AAA,AA,A&margin-w=4">
</picture>

</div>

---

## COLOPHON

<details>
<summary><strong>What this README actually does,</strong> the full catalogue of techniques</summary>

&nbsp;

This profile is a working demo of what GitHub's markdown renderer and HTML sanitizer currently allow inside a profile README. Every technique here is plain markdown, sanitizer-safe HTML, or a parameterized image URL: no GitHub Actions, no JavaScript, no CSS, no inline SVG, no Camo-bypassing tricks.

| Technique | Where it's used here |
|---|---|
| `<picture>` + `prefers-color-scheme` | Hero banner, typing SVG, streak card, top-langs card, activity graph, trophy row, footer banner |
| GFM alert (`> [!NOTE]`) | The `NOW` block |
| `<details>` / `<summary>` (interactive) | TOC, workshop list, focus deep-dive, this colophon |
| Mermaid `mindmap` (themed `forest`) | `STACK` diagram |
| Markdown table (bold-cell headers) | 2026 release timeline |
| Heading auto-anchors | TOC jump links (`#now`, `#current-work`, etc.) |
| `<kbd>` semantic tag | TOC summary chip |
| Camo-proxied animated SVGs | Capsule banner (SMIL `fadeIn`), typing SVG (CSS animation) |
| Live dynamic shields | Public repos and public gists pulled from the GitHub API via `dynamic/json` queries; followers, last-push, stars, total stars, following pulled from shields' GitHub endpoints |
| Live widget cards | `komarev` views, github-readme-streak-stats, top-langs (size + count blended for recency), activity-graph, profile-trophy |
| Custom-themed shields | Every badge tuned to a two-color palette: forest `#204F20`, cream `#F5E0C5` |
| `<table>` for grid layout | 2&times;3 projects, paired streak + languages |
| HTML comments | Source-only annotations at the top of this file |
| HTML entities (`&middot;`, `&nbsp;`, `&amp;`) | Body copy and inline separators |

**Things the GitHub sanitizer blocks, that this README respects:** inline `<svg>`, `<script>`, `<style>`, `<iframe>`, `<form>`, `<button>`, `<video>`, `<audio>`, `class=`, `style=`, `target=_blank`. Everything is either pre-rendered server-side into an SVG and proxied through Camo, or written with one of the &sim;14 tags on the sanitizer's allowlist.

**Deferred to a future automation pass** (each needs a GitHub Action this repo doesn't yet have): the Platane/snk contribution-snake animation, lowlighter/metrics SVG dashboard, yoshi389111/github-profile-3d-contrib isometric grid, and a WakaTime card.

Sources for the renderer constraints: [html-pipeline](https://github.com/gjtorikian/html-pipeline) &middot; [GitHub blog on dark/light images](https://github.blog/developer-skills/github/how-to-make-your-images-in-markdown-on-github-adjust-for-dark-mode-and-light-mode/) &middot; [GitHub Mermaid docs](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams).

</details>

---

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://capsule-render.vercel.app/api?type=waving&color=204F20&height=140&section=footer&text=BUILDING+RELIABLE+SYSTEMS&fontColor=F5E0C5&fontSize=22&fontAlignY=70&desc=EMMETT%40EMMETTS.DEV+%C2%B7+EMMETTSHAUGHNESSY.COM&descSize=12&descAlignY=88&descAlign=50">
  <img alt="Building reliable systems · emmett@emmetts.dev · emmettshaughnessy.com" src="https://capsule-render.vercel.app/api?type=waving&color=F5E0C5&height=140&section=footer&text=BUILDING+RELIABLE+SYSTEMS&fontColor=204F20&fontSize=22&fontAlignY=70&desc=EMMETT%40EMMETTS.DEV+%C2%B7+EMMETTSHAUGHNESSY.COM&descSize=12&descAlignY=88&descAlign=50">
</picture>
