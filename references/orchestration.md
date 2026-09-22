---
last_verified: 2026-09-22
volatility: medium
verify_horizon_days: 7
primary_sources:
  - https://code.claude.com/docs/en/sub-agents
---

# Orchestration

Snapshot 2026-09-19.

## Contents
- The prior question
- Spec-driven development
- Swarm orchestrators
- Worktree and session managers
- Remote control planes
- The subscription policy change

## The prior question

Before recommending anything here: **does the user need orchestration, or do they need context discipline?**

`[VERIFIED]` Claude Code's built-in plan mode now covers most daily work, and Anthropic's own guidance favors simple control loops over complex multi-agent systems. Several 2025-era frameworks visibly lost ground in 2026 as frontier models absorbed their scaffolding — Agent OS was publicly downsized for exactly this reason `[REPORTED]`.

Orchestration earns its token multiplier only when the task has an obvious fan-out shape *and* verification is automatable. Otherwise it is overhead.

## Spec-driven development

The biggest genuine methodology shift of 2026. All of these converge on specify → plan → execute → verify; they differ in weight.

| Framework | Shape | `[REPORTED]` stars | Fit |
|---|---|---|---|
| **GitHub Spec Kit** | governance layer, `/speckit.*` commands, a "constitution" doc | ~87k | Teams needing auditable process. Criticized as slow in the planning phase. |
| **OpenSpec** | lightweight TypeScript; per-change propose/apply/archive as a continuity layer | ~39k, `[REPORTED]` +863% over six months | Fastest-growing. Best fit for brownfield and solo/small-team work. |
| **BMAD-METHOD** | role agents — PO, architect, SM, dev, QA | ~44k | Heavy. Suits users who want simulated team process. |
| **Task Master AI** | PRD → dependency-aware task graph | growth stalled, `[REPORTED]` ~+18% | Cursor-centric. MIT + Commons Clause — check licensing for commercial use. |
| **GSD** | deep execution orchestration | | |
| **Agent OS** | | stagnant | `[REPORTED]` publicly downsized. Do not recommend as current. |
| **SuperClaude** | | | |

**Default recommendation:** plan mode first; OpenSpec when features regularly cross many files; Spec Kit when the organization needs the audit trail.

## Swarm orchestrators

**Ruflo** — formerly **Claude Flow**, by Reuven Cohen (rUv). `[VERIFIED]` Renamed January 2026 to avoid Anthropic trademark conflict. SPARC methodology, hive-mind topology, rewritten toward Rust/WASM. ~73k stars `[REPORTED]` — essentially unchanged; note that several aggregator blogs report ~31k, which is stale. GitHub is authoritative here..

`[DISPUTED]` Ruflo claims 84.8% SWE-bench and 75% cost savings; an independent audit found the figure is produced by `simulate_benchmarks.py`, which adds `random.uniform(-0.05, 0.05)` to hardcoded base rates rather than running the suite, and Ruflo does not appear on the official SWE-bench leaderboard. Do not cite the number as a benchmark result; if mentioned at all, mark it as fabricated/synthetic.

**ECC / Everything Claude Code** — agent-harness optimization system spanning skills, instincts, memory, and security across Claude Code, Codex, and Cursor.

Community sentiment tracks Anthropic's guidance here: high star counts, lower real-world retention than the numbers suggest.

## Worktree and session managers

Very active category. All solve the same problem — running N agents on one repo without them colliding — with different surfaces.

| Tool | Surface | Status | Note |
|---|---|---|---|
| **Conductor** | native macOS app (Melty Labs, YC S24) | active | worktree-per-agent, strong diff/PR flow, free with your own subscription. macOS only. |
| **Crystal** | open-source desktop | active | parallel sessions, each in its own worktree |
| **Claude Squad** | terminal (tmux + worktrees) | active | leanest option; no GUI dependency |
| **Nimbalyst** | cross-platform visual workspace + iOS app, MIT | active | |
| **Sculptor** | Imbue | active | container isolation instead of worktrees — stronger boundary |
| **Vibe Kanban** | agent-agnostic kanban, Apache-2.0 | `[VERIFIED]` **BloopAI shut down 2026-04-10**; community-maintained since | Flag the maintenance status if recommending |
| Abralo, Superset, Emdash, VibeTree | various | | |

Recommend the lightest option that fits: Claude Squad if they live in the terminal, Conductor on macOS if they want a GUI, Nimbalyst if cross-platform matters.

## Remote control planes

`[VERIFIED]` **Check first-party first.** Anthropic's Remote Control, Channels (Telegram/Discord/iMessage), and Dispatch now cover most of what these were built for. See `core-surfaces.md`.

Community options if first-party doesn't fit:

| Tool | Model | Caveat |
|---|---|---|
| **Happy Coder** | free, E2EE, native mobile | |
| **Omnara** | YC S25, voice via LiveKit, `[REPORTED]` ~$9–20/mo | relay sees your code — disqualifying for many enterprise contexts |
| **Terragon** | cloud VM | |
| **Grass** | cloud VM, laptop-off operation | |
| **CCGram / CCBot** | Telegram bridges | |
| DIY | Termius + tmux + Tailscale | most private, most setup |

## The subscription policy change

`[VERIFIED]` **2026-04-04: Anthropic blocked Pro/Max subscribers from using their subscriptions with most third-party agent frameworks.**

This reshaped the orchestration market and is the single most important practical fact in this file. Consequences:

- Heavy orchestration users are pushed toward API billing
- Some tools listed above may not work on a subscription plan — verify before recommending
- The economics of swarm orchestrators changed materially, since they were often justified by flat-rate subscription pricing

Always ask which plan the user is on before recommending a third-party framework.
