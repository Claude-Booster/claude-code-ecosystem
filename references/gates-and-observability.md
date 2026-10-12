---
last_verified: 2026-10-12
volatility: low
verify_horizon_days: 7
primary_sources:
  - https://code.claude.com/docs/en/hooks
  - https://code.claude.com/docs/en/agent-sdk/observability
---

# Gates and Observability

Snapshot 2026-10-12.

## Contents
- Hooks as the enforcement layer
- OpenTelemetry
- AI code review tool selection
- The productivity evidence

## Hooks as the enforcement layer

`[VERIFIED]` CLAUDE.md is advisory; hooks and permissions are deterministic. **PreToolUse is the primary security checkpoint.**

Base layer every serious setup should have, wired to hooks:

- lint
- typecheck
- test
- security scan (Snyk, Semgrep, or CodeQL)

Design notes that hold up in practice:

- **Stdlib-only gate scripts.** A gate that fails because a dependency drifted is worse than no gate.
- **Deterministic exit codes.** The hook contract is binary; ambiguity defeats the purpose.
- **Gate on the smallest unit that can fail.** PostToolUse per-edit catches problems while the agent still has context to fix them; end-of-session gates catch them after the reasoning is gone.
- **Prohibitions belong here, not in prose.** "Never touch `migrations/`" as a PreToolUse deny is enforcement; the same sentence in CLAUDE.md is a suggestion.

## OpenTelemetry

`[VERIFIED]` Built into the Claude Code CLI. The Agent SDK emits no telemetry of its own. It passes env config through to the CLI child process, and the CLI does the exporting. Metrics, log events and traces go over OTLP to any backend, and each signal has its own switch. Everything is off until `CLAUDE_CODE_ENABLE_TELEMETRY=1` is set. **Traces are beta** and also need `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1`. Span names and attributes "may change between releases." The span tree is `claude_code.interaction` → `llm_request` / `tool` (→ `tool.blocked_on_user`, `tool.execution`) / `hook`. Subagent spans nest under the parent's `claude_code.tool` span. Spans carry `session.id` by default. `prompt.id` is an **event-only** attribute that ties log events to a prompt. It is not on spans or metrics. In traces, the `claude_code.interaction` root span does that job.

`[VERIFIED]` No application code is required, only environment variables, set either in the process environment or per call via `options.env`. In TypeScript, `options.env` *replaces* the inherited environment, so spread `...process.env` into it. Do not use the `console` exporter under the SDK, because stdout is the SDK's message channel. Export errors fail silently unless `CLAUDE_CODE_OTEL_DIAG_STDERR=1` is set (v2.1.179+). This is still the recommended production default.

**Backends in use:** Langfuse (official Claude Code plugin plus OpenInference `ClaudeAgentSDKInstrumentation`), LangSmith, Helicone, Arize Phoenix (OSS OpenInference reference), OpenObserve, Future AGI.

`[VERIFIED]` Attach end-user identity as `OTEL_RESOURCE_ATTRIBUTES` (e.g. `enduser.id=…,tenant.id=…`, percent-encoded) on each `query()` call. The built-in identity attributes identify the *credential*, not the end user. With end-user identity attached, `tool_decision`, `tool_result`, `mcp_server_connection` and `permission_mode_changed` events become a per-user audit trail you can send to a SIEM. This is the usual prerequisite for chargeback.

**Threshold:** turn this on past ~5 engineers, or immediately if there's any chargeback or compliance requirement.

## AI code review tool selection

Read the benchmark caveat before using these numbers: **most are vendor-run.**

`[VENDOR]` Greptile's own July 2025 benchmark (50 real-world PRs, 5 repos): Greptile caught **82%** of bugs, Cursor Bugbot 58%, Copilot 54%, CodeRabbit 44%, Graphite 6%. The same benchmark logged ~11 false positives per run for Greptile vs ~2 for CodeRabbit.

`[DISPUTED]` The Signal65 "Evaluating AI Code Review Tools" study (March 2026) is heavily CodeRabbit-branded/-promoted (the widely circulated infographic is published as "CodeRabbit — Evaluating AI Code Review Tools") with no independent-sponsorship disclosure, so it does not support an "independent" / `[REPORTED]` framing. The precision number for Cursor Bugbot (**95.95%**) checks out, but **CodeRabbit effectively tied it at 95.88%**, and the study's own conclusion crowns CodeRabbit as the overall winner — so "Cursor Bugbot posted the highest precision in the field" is a 0.07-point edge, not a differentiator.

Both can be true — they measure recall and precision respectively. Translate for the user rather than quoting either as "best":

| Tool | Strength | Trade-off | Fit |
|---|---|---|---|
| **CodeRabbit** | broadest coverage, lowest noise, most adopted; GitHub/GitLab/Bitbucket/Azure DevOps | middling depth | small teams wanting one tool |
| **Greptile** | deepest bug-catching via full-codebase indexing | accept more false positives | growth-stage teams that can absorb noise |
| **Cursor Bugbot** | highest precision, leanest | Cursor-native; `[VENDOR]` Usage-based pricing (~$1.00–1.50/run per Cursor's help center) was **announced May 11, 2026**, with existing customers migrating at their next renewal **on/after June 8, 2026** — so "June 2026" is the rollout, not the announcement. Source is Cursor's own help center, which supports `[VENDOR]`, not `[VERIFIED]` (no independent reproduction of the per-run cost). A June 2026 update also made Bugbot ~22% cheaper per run and added a `/review` command and effort levels. | teams already on Cursor |
| **Sentry Seer** | strongest on high/critical severity | narrow | production-incident focus |
| Claude `/review`, GitHub PR review action | in-loop, no extra vendor | not a substitute for a dedicated reviewer | everyone, as a first pass |

`[VERIFIED]` **Cursor agreed to acquire Graphite**, announced **December 19, 2025** (cash + equity, undisclosed terms). Graphite continues as an independent product with the same team. No 2026 report of Graphite or its Diamond reviewer shutting down was found. (The line as written never names the acquirer or the target, so it is unreadable out of context.)

`[REPORTED]` Consensus growth-stage setup: Greptile plus a bug-focused tool. Small teams: CodeRabbit alone.

**Deterministic gates remain the non-negotiable base layer regardless.** An AI reviewer is a second opinion, not a replacement for tests that pass or fail.

## The productivity evidence

Cite this when a user is scaling agent usage without scaling review.

`[VERIFIED]` Anthropic's June 2026 research, **"Agentic coding and persistent returns to expertise"** (published June 16, 2026) — ~400,000 sessions across 235,000 users, Oct 2025–Apr 2026. (The underlying stats are confirmed: intermediate+ sessions reach verified success 28–33% of the time; novices reach it ~15%; novices abandon 19% of sessions vs 5–7% for everyone else.)

- A session rated intermediate or above reaches **verified success only 28–33% of the time**
- **Novices abandon 19% of troubled sessions** versus 5–7% for everyone else

The delta is scaffolding and expertise, not prompt quality. This is the strongest available argument for the gate-and-context discipline in this reference.

`[REPORTED]` Faros AI, "The Acceleration Whiplash" — telemetry from ~22,000 developers across 4,000+ teams:

| Metric | Change |
|---|---|
| Median time in PR review | +441.5% |
| Incidents per PR | +242.7% |
| Bugs per developer | +54% |
| Code churn | +861% |
| PRs merged with no review at all | +31.3% |

Read this as: agentic speed shifts cost downstream onto review and incidents unless gate discipline keeps pace. **Rising incidents mean tighten gates, not loosen them** — the opposite of the intuitive response.

## Common anti-patterns

Named by the community, in rough order of frequency:

1. **Context rot** — the primary failure mode; degraded quality as the window fills
2. Over-stuffed CLAUDE.md
3. MCP server bloat
4. Unreviewed diffs
5. Runaway token spend from subagent fan-out and autocompact cascades
6. Approval fatigue — broad permissions plus reflexive click-through defeats the permission model entirely
7. "Vibe coding" anything beyond a throwaway MVP
