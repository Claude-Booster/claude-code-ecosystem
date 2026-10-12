# Patch: orchestration.md
verified_against: 2026-10-12
searches_run: 28
verdict: CHANGED

## Changed

### Subscription policy: third-party apps can use subscription limits again
- was: `[VERIFIED]` **2026-04-04: Anthropic blocked Pro/Max subscribers from using their subscriptions with most third-party agent frameworks.** … "the single most important practical fact in this file"
- now: `[VERIFIED]` The 2026-04-04 restriction on piping Pro/Max limits through third-party frameworks (e.g. OpenClaw) is historical. Anthropic's support page says that on 2026-06-15 it "paused the previously-announced changes to Claude Agent SDK usage". Its 2026-10-07 update says "You can still use the Claude Agent SDK, `claude -p`, and third-party apps with your subscription limits." Separately, from 2026-10-07 Max and Team plans include monthly API credits: Max 5x $100, Max 20x $200, Team $20 per Standard seat and $100 per Premium seat, pooled and capped at $500. Pro gets none. The credits cover API, Agent SDK and Managed Agents usage via a Console org API key, not interactive Claude Code. The bullet list of consequences ("pushed toward API billing", "may not work on a subscription plan") should be softened to match. Keep "ask which plan the user is on."
- source: https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan ; https://support.claude.com/en/articles/17154008-monthly-api-credits-for-max-and-team-plans ; April event: https://thenextweb.com/news/anthropic-openclaw-claude-subscription-ban-cost/
- confidence: [VERIFIED] (Anthropic support pages)

### Spec Kit star count
- was: `| **GitHub Spec Kit** | … | ~87k |`
- now: ~141k `[REPORTED]` (GitHub live count 140.9k on 2026-10-12)
- source: https://github.com/github/spec-kit
- confidence: [REPORTED]

### OpenSpec star count
- was: `| **OpenSpec** | … | ~39k, [REPORTED] +863% over six months |`
- now: ~72k `[REPORTED]` (GitHub live count 71.7k). The "+863% over six months" growth figure has no primary source. Drop it or recompute it.
- source: https://github.com/Fission-AI/OpenSpec
- confidence: [REPORTED]

### BMAD-METHOD star count
- was: `| **BMAD-METHOD** | … | ~44k |`
- now: ~54k `[REPORTED]` (GitHub live count 54.0k). The README announces a V7 preview alpha with an ETA of 2026-10-16.
- source: https://github.com/bmad-code-org/BMAD-METHOD
- confidence: [REPORTED]

### Task Master star count
- was: `growth stalled, [REPORTED] ~+18%`
- now: ~28k `[REPORTED]` (GitHub live count 28.2k). The MIT + Commons Clause licensing note is confirmed in the repo README.
- source: https://github.com/eyaltoledano/claude-task-master
- confidence: [REPORTED]

### Omnara pricing
- was: `| **Omnara** | YC S25, voice via LiveKit, [REPORTED] ~$9–20/mo | relay sees your code … |`
- now: `[VENDOR]` "$0 platform fee". You can bring your own model keys and machines, or pay as you go with Omnara credits (models at provider token rates, machines by active time). Self-hosting is free. The vendor also now offers a hosted "Omnara Cloud". The ~$9–20/mo figure is no longer on the vendor site. The relay caveat still applies to the hosted path.
- source: https://www.omnara.com/
- confidence: [VENDOR]

### Merge artifacts in the file body (editorial)
- was: (1) A paragraph starting "Agent OS shipped **v3** (repositioned Jan 2026)…" sits between table rows in "Spec-driven development". It breaks the Markdown table, and it contains patch commentary ("worth correcting", "the 2026-09-22 snapshot"). (2) The Ruflo paragraph ends with "'Essentially unchanged' still holds; the ~31k aggregator figure remains stale. Only the headline number needs a nudge. GitHub is authoritative here.." These are leftover instructions from an earlier patch, not reference content.
- now: Move Agent OS out of the table into a short note: "Agent OS v3 (Builder Methods, Jan 2026): ~70% of the framework stripped; defers spec-writing to Plan Mode and keeps a thin standards layer. Active, ~5.5k stars `[REPORTED]`." Trim the Ruflo line to "~74k stars `[REPORTED]` (GitHub live count 74.4k)."
- source: https://github.com/buildermethods/agent-os ; https://github.com/ruvnet/ruflo
- confidence: [REPORTED]

## Status changes

### Terragon is defunct (listed as a live option)
- was: `| **Terragon** | cloud VM | |`
- now: `[VERIFIED]` Terragon has shut down. All sandboxes were terminated and the code was released as an as-is open-source snapshot with no maintenance. The shutdown page points users to Claude Code on the web and Codex web. Remove it from the table, or move it to a "defunct" note. Exact shutdown date: see Could not verify.
- source: https://www.terragonlabs.com/ (page title "Terragon Shutdown") ; https://github.com/terragon-labs/terragon-oss
- confidence: [VERIFIED]

### Crystal is deprecated and replaced by Nimbalyst (listed as "active")
- was: `| **Crystal** | open-source desktop | active | parallel sessions, each in its own worktree |`
- now: `[VERIFIED]` The README reads "Crystal Is Now Nimbalyst … has been deprecated and replaced by Nimbalyst. Deprecated: February 2026." Delete the row, or merge it into the existing Nimbalyst row as "(successor to Crystal)".
- source: https://github.com/stravu/crystal
- confidence: [VERIFIED]

### Vibe Kanban README now says "sunsetting"
- was: `[VERIFIED] **BloopAI shut down 2026-04-10**; community-maintained since`
- now: `[VERIFIED]` BloopAI shut down on 2026-04-10. The repo README now says "Vibe Kanban is sunsetting." The shutdown post says the project continues as open source and community-maintained, local-only after hosted services ended. The README names no official community fork. Keep the maintenance-status warning.
- source: https://github.com/BloopAI/vibe-kanban ; https://vibekanban.com/blog/shutdown
- confidence: [VERIFIED]

## New entries

### First-party agent teams, background agents and forks
- now: `[VERIFIED]` Claude Code now ships these built in: agent teams (a coordinated group of sessions that Claude spawns and supervises), background agents (many independent sessions monitored from one place), cross-session messaging, `isolation: worktree` for subagents, and forks via `/subtask` (v2.1.212+). The defaults are nesting depth 3 and 20 concurrent subagents.
- source: https://code.claude.com/docs/en/sub-agents
- confidence: [VERIFIED]
- why: "The prior question" and the worktree-manager section currently mention only plan mode. First-party worktree isolation and agent teams now cover the core use case of several third-party tools here, so this belongs in the "check first-party first" framing.

## Could not verify

- **Terragon shutdown date.** The OSS snapshot README dates its notice 2026-01-16. A search summary of terragonlabs.com gives 2026-02-09. Fetching the page directly returned only the title, and `/shutdown` returned 404. Record it as `[DISPUTED]`: 2026-01-16 vs 2026-02-09.
- **Scope of "third-party apps" in Anthropic's 2026-10-07 support text.** The support page doesn't define the term. The Agent SDK docs still say third-party developers may not offer claude.ai login or rate limits "unless previously approved". Searched support.claude.com, code.claude.com and anthropic.com. Whether *any* framework may use subscription limits, or only approved ones, is unresolved, so `[DISPUTED]` on the scope.
- **Earlier credit figures.** A 2026-05-14 Techstrong article reported a "reversal" with $20 Pro and $100 Max 5x Agent SDK credits, citing only an X post. The current Anthropic page says Pro gets no credits. Treat the May report as superseded. It has no primary source.
- **Conductor "free with your own subscription".** conductor.build is live (release 0.90.0, macOS only) but its pricing is on a separate page that I couldn't read. Not confirmed.
- **Ruflo 84.8% SWE-bench audit.** No new source found either way. Keep it as `[DISPUTED]`.

## No longer relevant

- **"`[REPORTED]` +863% over six months" (OpenSpec):** this growth figure from an aggregator has no primary source and is now stale. The live star count says more.
- **"growth stalled, `[REPORTED]` ~+18%" (Task Master):** same problem, a percentage with no source. Replace it with the live star count above.
- **Empty table rows (GSD, SuperClaude; "Abralo, Superset, Emdash, VibeTree"; CCGram / CCBot):** they have no shape, fit, status or caveat. Either fill them in or delete them, because they cost context and give no guidance.
