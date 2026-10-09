I have enough to compile the patch. Here is my analysis.

```markdown
# Patch: context-and-cost.md
verified_against: 2026-10-09
searches_run: 13
verdict: CHANGED

## Changed

### CLAUDE.md ≤200 lines is now in Anthropic's own docs
- was: "`[REPORTED]` Community rule of thumb has hardened to **≤200 lines**, with detail moved into `.claude/rules/*.md` scoped by path glob so rules load only for relevant files."
- now: "`[VERIFIED]` Anthropic's cost docs now state the number directly: *"Aim to keep CLAUDE.md under 200 lines by including only essentials."* Anthropic's recommended overflow destination is **skills** (`.claude/skills/`, loaded on demand), not a rules directory. `[REPORTED]` The community `.claude/rules/*.md` path-glob pattern remains a community convention, not a documented Claude Code feature."
- source: https://code.claude.com/docs/en/costs (section "Move instructions from CLAUDE.md to skills")
- confidence: [VERIFIED] for the 200-line figure; [REPORTED] for the `.claude/rules/*.md` mechanism
- note: The 200-line figure may have been in the docs at or before last verification; this is a confidence-tag correction (the number now has primary backing), not necessarily a post-2026-09-22 change. Flagging it because the file still presents the number as community-only.

## Status changes

none found. Spot-checked the named tools:
- **AGENTS.md / Agentic AI Foundation** — governance claim holds. AAIF was formed under the Linux Foundation on 2025-12-09 and AGENTS.md was donated to it; spec is under open (MIT-style) terms. (https://analyticsindiamag.com/ai-news-updates/openai-anthropic-and-block-set-up-agentic-ai-foundation-under-linux-foundation)
- **v2.1.277 (2026-09-18) AGENTS.md fallback** — confirmed: native AGENTS.md read when no CLAUDE.md is present, toggleable in `/config`, not yet on Bedrock/Vertex/Foundry. Still accurate. (https://www.havoptic.com/r/claude-code-2.1.277)
- **ccusage** — still active, still ryoppippi, still local-JSONL / no-API-key. Roster has grown (Codex, Gemini CLI, Copilot CLI, Goose, Amp, Droid, etc.); the "18+ agent CLIs" figure is volatile but not contradicted, so left as-is. (https://raw.githubusercontent.com/ryoppippi/ccusage/main/docs/guide/index.md)
- **claude-mem / Serena** — no archive, rename, or defunct notice found. Both appear live.
- **LiteLLM** — still the named open-source gateway for per-key spend tracking; Anthropic's own costs page still cites it ("Several large enterprises reported using LiteLLM… unaffiliated with Anthropic and has not been audited for security"). Unchanged.

## New entries

### Claude apps gateway — first-party per-user spend limits
- was: (absent) The "Rate limits and spend" / usage section names LiteLLM as "the right answer for team-level spend control" with no first-party alternative.
- now: "`[VERIFIED]` **Claude apps gateway** — Anthropic's own self-hosted gateway now enforces per-developer **daily/weekly/monthly** spend caps (scope: user / IdP group / organization) via an Admin API, returns HTTP 429 `billing_error` when a cap is passed, and surfaces the cap in `/usage`, the status line, and 75%/95% warnings. It is the first-party circuit-breaker equivalent of the LiteLLM pattern."
- source: https://code.claude.com/docs/en/claude-apps-gateway-spend-limits
- confidence: [VERIFIED]
- why it clears the bar: The file's spend section currently frames LiteLLM (a third-party, unaudited tool) as "the right answer" for team spend control. A documented, first-party, Anthropic-native option with hard per-user enforcement directly competes with that recommendation and changes the advice. High-relevance, primary-sourced.

### Max plans carry model-family-specific weekly limits
- was: "`[VERIFIED]` Two overlapping windows: a **5-hour rolling session cap** and a **weekly cap** … Plans are defined by multiplier — Pro baseline, Max 5×, Max 20×."
- now: "`[VERIFIED]` In addition to the all-model session/weekly windows, Claude Code now issues **model-family-specific limit messages** ('You've hit your Opus limit' / 'You've hit your Sonnet limit'), and switching to a model outside that family with `/model` keeps the developer working. The all-model session/weekly caps are not escapable by model switching; the family-specific ones are."
- source: https://code.claude.com/docs/en/costs (section "When a developer asks about a limit")
- confidence: [VERIFIED]
- why it clears the bar: Refines the file's "defined by multiplier, not token counts" claim with a now-documented second axis (per-family caps) that materially changes the practical advice when a user hits a wall — it's the difference between "wait for reset" and "switch model and continue."

## Could not verify

### Graceful stop at the 5-hour limit (with borrowed weekly allowance)
- Reported (~2026-09-25, after last verification): Claude Code now seeks a clean stopping point when the 5-hour window closes mid-task, funded by a small fixed allowance drawn from the weekly quota — Pro gets it once/week, Max/Team Premium each time (weekly quota permitting).
- Searched: Anthropic changelog, release notes, and the `code.claude.com/docs/en/interactive-mode` "Wait for a usage limit to reset" section. The docs confirm a *related but distinct* feature — auto-continue after reset (`autoContinueAtUsageLimit`, v2.1.234+) — but say nothing about a graceful-stop allowance borrowed from the weekly limit.
- Found only: one secondary site (pasqualepillitteri.it, multiple language mirrors) republishing a ClaudeDevs X post dated 2026-09-25. No primary source located.
- Disposition: single secondary source, no primary confirmation → do not promote. Flagging per the no-silent-drop rule.
- source (secondary only): https://pasqualepillitteri.it/en/news/18831/claude-code-graceful-stop-5-hour-limit

## No longer relevant

none found. The two aging historical claims were considered and kept:
- v2.1.89 (March 2026) rate-limit-consumption spike (line 85) — still a specific, actionable "check the CLI version" diagnostic; retained.
- Microsoft license cancellation 2026-06-30 (line 89) — still a valid organizational-scale signal; retained. Revisit at next verification if it keeps aging without a follow-on data point.
```

**Summary of what I found:** the file holds up well. The highest-value items are two **new entries** — Anthropic's first-party **Claude apps gateway** spend-limit enforcement (which competes with the file's LiteLLM recommendation) and the now-documented **model-family-specific limit** behavior — plus one **confidence upgrade** (the ≤200-line CLAUDE.md figure is now in Anthropic's own docs, not just community lore). No tools died or were renamed. The one post-2026-09-22 rate-limit behavior change (graceful stop) couldn't be pinned to a primary source, so it's logged under "Could not verify" rather than promoted. Verdict: **CHANGED**.
