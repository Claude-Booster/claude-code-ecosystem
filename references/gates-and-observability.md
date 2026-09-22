---
last_verified: 2026-09-22
volatility: low
verify_horizon_days: 7
primary_sources:
  - https://code.claude.com/docs/en/hooks
  - https://code.claude.com/docs/en/agent-sdk/observability
---

# Gates and Observability

Snapshot 2026-09-19.

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

`[VERIFIED]` Built into both the Claude Code CLI and the Agent SDK. Exports traces, metrics, and log events over OTLP to any backend. Native span tree covers interaction → llm_request → tool → subagent nesting, with `session.id` and `prompt.id` correlation.

Zero application code required. This is the recommended production default — reach for a vendor SDK only if you need something OTel doesn't carry.

**Backends in use:** Langfuse (official Claude Code plugin plus OpenInference `ClaudeAgentSDKInstrumentation`), LangSmith, Helicone, Arize Phoenix (OSS OpenInference reference), OpenObserve, Future AGI.

Attach a user identifier via hooks or OTel resource attributes to get per-developer cost dashboards — the usual prerequisite for chargeback.

**Threshold:** turn this on past ~5 engineers, or immediately if there's any chargeback or compliance requirement.

## AI code review tool selection

Read the benchmark caveat before using these numbers: **most are vendor-run.**

`[VENDOR]` Greptile's own July 2025 benchmark (50 real-world PRs, 5 repos): Greptile caught **82%** of bugs, Cursor Bugbot 58%, Copilot 54%, CodeRabbit 44%, Graphite 6%. The same benchmark logged ~11 false positives per run for Greptile vs ~2 for CodeRabbit.

`[REPORTED]` Independent Signal65 testing tells a different story on precision: **Cursor Bugbot posted the highest precision in the field (~95.95%, only 3 false positives)** while finding ~23% fewer true positives than CodeRabbit.

Both can be true — they measure recall and precision respectively. Translate for the user rather than quoting either as "best":

| Tool | Strength | Trade-off | Fit |
|---|---|---|---|
| **CodeRabbit** | broadest coverage, lowest noise, most adopted; GitHub/GitLab/Bitbucket/Azure DevOps | middling depth | small teams wanting one tool |
| **Greptile** | deepest bug-catching via full-codebase indexing | accept more false positives | growth-stage teams that can absorb noise |
| **Cursor Bugbot** | highest precision, leanest | Cursor-native; `[VERIFIED]` moved to usage-based pricing ~$1–1.50/review June 2026 | teams already on Cursor |
| **Sentry Seer** | strongest on high/critical severity | narrow | production-incident focus |
| Claude `/review`, GitHub PR review action | in-loop, no extra vendor | not a substitute for a dedicated reviewer | everyone, as a first pass |

`[VERIFIED]` Cursor acquired Graphite in December 2025.

`[REPORTED]` Consensus growth-stage setup: Greptile plus a bug-focused tool. Small teams: CodeRabbit alone.

**Deterministic gates remain the non-negotiable base layer regardless.** An AI reviewer is a second opinion, not a replacement for tests that pass or fail.

## The productivity evidence

Cite this when a user is scaling agent usage without scaling review.

`[VERIFIED]` Anthropic's June 2026 research, "How Claude Code is used in practice" — ~400,000 sessions across 235,000 users, Oct 2025–Apr 2026:

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
