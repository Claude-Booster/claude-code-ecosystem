I have enough to compile the patch. Let me verify one more primary-source detail — whether the OTel traces beta gating is a real change — but I'm confident in the findings. Here is the patch.

```markdown
# Patch: gates-and-observability.md
verified_against: 2026-10-09
searches_run: 12
verdict: CHANGED

## Changed

### Anthropic research — wrong title
- was: `[VERIFIED]` Anthropic's June 2026 research, "How Claude Code is used in practice" — ~400,000 sessions across 235,000 users, Oct 2025–Apr 2026:
- now: `[VERIFIED]` Anthropic's June 2026 research, **"Agentic coding and persistent returns to expertise"** (published June 16, 2026) — ~400,000 sessions across 235,000 users, Oct 2025–Apr 2026. (The underlying stats are confirmed: intermediate+ sessions reach verified success 28–33% of the time; novices reach it ~15%; novices abandon 19% of sessions vs 5–7% for everyone else.)
- source: https://www.anthropic.com/research/claude-code-expertise
- confidence: [VERIFIED]

### Signal65 precision study is not independent — it is CodeRabbit-promoted
- was: `[REPORTED]` Independent Signal65 testing tells a different story on precision: **Cursor Bugbot posted the highest precision in the field (~95.95%, only 3 false positives)** while finding ~23% fewer true positives than CodeRabbit.
- now: `[DISPUTED]` The Signal65 "Evaluating AI Code Review Tools" study (March 2026) is heavily CodeRabbit-branded/-promoted (the widely circulated infographic is published as "CodeRabbit — Evaluating AI Code Review Tools") with no independent-sponsorship disclosure, so it does not support an "independent" / `[REPORTED]` framing. The precision number for Cursor Bugbot (**95.95%**) checks out, but **CodeRabbit effectively tied it at 95.88%**, and the study's own conclusion crowns CodeRabbit as the overall winner — so "Cursor Bugbot posted the highest precision in the field" is a 0.07-point edge, not a differentiator.
- source: https://signal65.com/research/ai/evaluating-ai-code-review-tools-a-real-world-bug-detection-study/ ; https://signal65.com/wp-content/uploads/2026/04/CodeRabbit-Evaluating-AI-Code-Review-Tools-Infographic.pdf
- confidence: [DISPUTED]

### OpenTelemetry traces are now a beta-gated signal, not zero-config
- was: `[VERIFIED]` ... Native span tree covers interaction → llm_request → tool → subagent nesting, with `session.id` and `prompt.id` correlation. ... Zero application code required. This is the recommended production default
- now: `[VERIFIED]` Metrics and log events are zero-config over OTLP, but **traces are a separate beta signal**: they require `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1`, and the docs state "Tracing is in beta. Span names and attributes may change between releases." The span tree is `claude_code.interaction` → `claude_code.llm_request` / `claude_code.tool` / `claude_code.hook`, with subagent `llm_request`/`tool` spans nesting under the parent agent's `claude_code.tool` span; `session.id` correlation is confirmed. The "recommended production default / zero application code" claim holds for metrics and logs, but the span-tree view specifically is beta.
- source: https://code.claude.com/docs/en/agent-sdk/observability
- confidence: [VERIFIED]

## Status changes

### Cursor acquired Graphite — date confirmed, still accurate
- was: `[VERIFIED]` Cursor acquired Graphite in December 2025.
- now: `[VERIFIED]` Confirmed: deal announced **December 19, 2025** (cash + equity, undisclosed terms; Graphite to continue as a standalone product). No change needed — listed only to record it was re-verified.
- source: https://techcrunch.com/2025/12/19/cursor-continues-acquisition-spree-with-graphite-deal
- confidence: [VERIFIED]

### Cursor Bugbot pricing — re-verified, minor date refinement
- was: `[VERIFIED]` moved to usage-based pricing ~$1–1.50/review June 2026
- now: `[VENDOR]` Usage-based pricing (~$1.00–1.50/run per Cursor's help center) was **announced May 11, 2026**, with existing customers migrating at their next renewal **on/after June 8, 2026** — so "June 2026" is the rollout, not the announcement. Source is Cursor's own help center, which supports `[VENDOR]`, not `[VERIFIED]` (no independent reproduction of the per-run cost). A June 2026 update also made Bugbot ~22% cheaper per run and added a `/review` command and effort levels.
- source: https://aicatchup.com/news/cursor-bugbot-3x-faster-review-command-incremental-review ; https://cursor.com/pricing
- confidence: [VENDOR]

## New entries

### Martian Code Review Benchmark — the first large-scale *independent* benchmark
- was: (absent)
- now: `[REPORTED]` The **Martian Code Review Benchmark** (codereview.withmartian.com) is a continuously-updated, open-source-methodology benchmark from Martian (a research lab with ex-DeepMind/Anthropic/Meta staff) scoring ~10 tools against developer behavior across **nearly 300,000 real pull requests**. Its *existence and scale* are well-attested across multiple independent sources.
- source: https://codereview.withmartian.com/ ; https://www.coderabbit.ai/newsroom/coderabbit-tops-ai-code-review-benchmark
- confidence: [REPORTED]
- why it clears the bar: The file's whole AI-code-review section carries the caveat "most are vendor-run." This is the first independent, large-scale (~300K-PR), open-methodology benchmark in the category — exactly the gap the file flags. It belongs here even though its *rankings* are volatile (see below).

### Martian rankings are contested
- now: `[DISPUTED]` Rankings on the Martian benchmark are **not settled**: at least three vendors each published posts crowning themselves #1 on it in 2026, one snapshot printed CodeRabbit at 51.2% F1 while another printed the same tool at 30.3%, and a live-leaderboard snapshot showed **Cubic Dev AI #1 (~64.7% F1)** with **CodeRabbit #2 (~61.9%)**. Report the benchmark's existence, not a leaderboard position.
- source: https://codereview.withmartian.com/ ; https://particula.tech/blog/greptile-vs-coderabbit-vs-qodo-ai-code-review-2026
- confidence: [DISPUTED]

## Could not verify

### Greptile benchmark false-positive counts (~11 vs ~2)
Searched Greptile's current benchmark page (greptile.com/benchmarks). The catch rates in the file (Greptile 82%, Bugbot 58%, Copilot 54%, CodeRabbit 44%, Graphite 6%; July 2025; 50 PRs / 5 repos) are all confirmed on the primary page. But that page reports **no false-positive numbers** — it only says false positives "did not affect the catch rate." The file's "~11 false positives per run for Greptile vs ~2 for CodeRabbit" could not be located on the current primary source; it may have lived on an older blog version. Leave the catch rates as `[VENDOR]` (confirmed); the FP figures should drop to `[DISPUTED]` unless the original blog post is re-located.
- source: https://www.greptile.com/benchmarks

### OTel `prompt.id` correlation
The observability primary source documents `session.id` as the default correlation attribute and describes the interaction→llm_request→tool→subagent span tree, but makes **no mention of a `prompt.id` attribute**. Searched the observability and monitoring docs; found only `session.id` (and W3C `TRACEPARENT`/`trace_id`/`span_id` for application linkage). The file's "`prompt.id` correlation" could not be confirmed and may be stale.
- source: https://code.claude.com/docs/en/agent-sdk/observability

## No longer relevant

none found
```
