---
last_verified: 2026-09-22
volatility: high
verify_horizon_days: 7
primary_sources:
  - https://code.claude.com/docs/en/best-practices
  - https://support.claude.com
---

# Context and Cost

Snapshot 2026-09-19.

## Contents
- The four-layer context stack
- CLAUDE.md conventions
- AGENTS.md convergence
- Memory and retrieval tools
- Usage monitors
- Rate limits and spend

## The four-layer context stack

Clean separation, each layer with one job:

1. **AGENTS.md** — durable repo rules shared across agent tools
2. **Session context** — ephemeral, task-specific
3. **CLAUDE.md** — accumulated project memory, Claude-specific
4. **Skills** — reusable capabilities, loaded on match

`[VERIFIED]` Every retrieval source competes for the same finite window. Layering without disclosure discipline crowds out the actual task. This is the mechanism behind most "Claude got worse partway through" reports.

## CLAUDE.md conventions

`[VERIFIED]` Anthropic's large-codebase guidance:

- Keep it **lean and layered** — root file is pointers and gotchas, not documentation
- **Initialize in subdirectories, not repo root**, for large monorepos — `/init` in the directory you're working in
- Give each task the smallest useful context

`[REPORTED]` Community rule of thumb has hardened to **≤200 lines**, with detail moved into `.claude/rules/*.md` scoped by path glob so rules load only for relevant files.

`[VERIFIED]` Anthropic notes Claude tends to over-engineer. Adding an explicit "use the simplest possible approach" line to CLAUDE.md is standard mitigation.

**Encode prohibitions explicitly rather than as advisory prose.** "Never modify files in `generated/`" outperforms "be careful with generated files." But remember the ceiling: CLAUDE.md is advisory regardless of phrasing. Anything that genuinely must not happen belongs in a PreToolUse hook — see `gates-and-observability.md`.

## AGENTS.md convergence

`[VERIFIED]` **Claude Code v2.1.277 (2026-09-18) added native AGENTS.md fallback** — read when no CLAUDE.md is present.

History worth knowing: this followed a 4,000+ upvote GitHub issue, and the long-standing workaround was `ln -s AGENTS.md CLAUDE.md`. If a user still has that symlink, it's now redundant.

AGENTS.md is governed by the Agentic AI Foundation (Linux Foundation, MIT). Recommend it for any repo where more than one agent tool is in use.

## Memory and retrieval tools

| Tool | What it does | Note |
|---|---|---|
| **claude-mem** | auto-captures sessions, compresses, injects into future sessions | `[REPORTED]` #1 trending GitHub Feb 2026 |
| **Serena** | symbol-level code memory plus persistent project memory across sessions | Also the top MCP pick — see `mcp-servers.md` |
| Smart Connections | semantic layer over an Obsidian vault | For users who keep notes there |

Caution the user: auto-injecting memory is the fastest way to reintroduce the context problem you just solved. Injected memory should be small and high-signal or it is net negative.

## Usage monitors

| Tool | Type | Note |
|---|---|---|
| **ccusage** | free npm CLI (ryoppippi) | **The default recommendation.** Reads local JSONL — no account, no API key. `[REPORTED]` now tracks 18+ agent CLIs. |
| **Claude-Code-Usage-Monitor** | Python TUI | burn-rate prediction |
| **ccflare** | web dashboard | |
| **CCSeva** | macOS menu bar | |
| **ccstatusline** | status-line metrics | in-session visibility |
| **Terse** | commercial | The one that *acts* — SIGSTOP/SIGTERM circuit breaker before the next API call |
| claude-token-lens, cc-budget | | |

Built-ins first: `/usage`, `/status`, `/cost`, `/context`. Most users asking about spend need `/context` habits, not a new tool.

`[VERIFIED]` **LiteLLM** enforces org-wide hard budgets at the gateway — the right answer for team-level spend control.

## Rate limits and spend

`[VERIFIED]` Two overlapping windows: a **5-hour rolling session cap** and a **weekly cap**, shared across Claude Code, Claude.ai chat, and Cowork. Plans are defined by multiplier — Pro baseline, Max 5×, Max 20× — not by published token counts.

`[VERIFIED]` **The v2.1.89 release (March 2026) caused widely-reported 3–50× faster rate-limit consumption**, with some Max 20× users exhausting quota within ~70 minutes of reset. If a user reports sudden limit problems, check their CLI version.

`[VERIFIED]` Anthropic's own cost documentation cites roughly **$13/developer/active-day** and **$150–250/developer/month**, with 90% of users below $30/active-day.

`[REPORTED]` Microsoft cancelled most internal Claude Code licenses in one division effective 2026-06-30 — a signal that at organizational scale the bill becomes a defended line item.

**Efficiency practices, highest leverage first:**

1. Aggressive `/clear` between unrelated tasks
2. Model routing — Haiku for fan-out, Sonnet daily, Opus for genuinely hard reasoning
3. Prompt caching — watch cache-creation vs cache-read token split
4. Minimize MCP servers (the context argument and the cost argument are the same argument)
5. Scope requests before sending rather than letting the agent explore
6. Headless `claude -p` with `--allowedTools` for batch work
