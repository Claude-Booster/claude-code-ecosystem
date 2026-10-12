# Patch: gates-and-observability.md
verified_against: 2026-10-12
searches_run: 7
verdict: CHANGED

## Changed

### OTel traces are beta and off by default
- was: `[VERIFIED]` Built into both the Claude Code CLI and the Agent SDK. Exports traces, metrics, and log events over OTLP to any backend. Native span tree covers interaction → llm_request → tool → subagent nesting, with `session.id` and `prompt.id` correlation.
- now: `[VERIFIED]` Built into the Claude Code CLI. The Agent SDK emits no telemetry of its own. It passes env config through to the CLI child process, and the CLI does the exporting. Metrics, log events and traces go over OTLP to any backend, and each signal has its own switch. Everything is off until `CLAUDE_CODE_ENABLE_TELEMETRY=1` is set. **Traces are beta** and also need `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1`. Span names and attributes "may change between releases." The span tree is `claude_code.interaction` → `llm_request` / `tool` (→ `tool.blocked_on_user`, `tool.execution`) / `hook`. Subagent spans nest under the parent's `claude_code.tool` span. Spans carry `session.id` by default. `prompt.id` is an **event-only** attribute that ties log events to a prompt. It is not on spans or metrics. In traces, the `claude_code.interaction` root span does that job.
- source: https://code.claude.com/docs/en/agent-sdk/observability ; https://code.claude.com/docs/en/monitoring-usage
- confidence: [VERIFIED]

### "Zero application code" needs a qualifier
- was: Zero application code required. This is the recommended production default — reach for a vendor SDK only if you need something OTel doesn't carry.
- now: `[VERIFIED]` No application code is required, only environment variables, set either in the process environment or per call via `options.env`. In TypeScript, `options.env` *replaces* the inherited environment, so spread `...process.env` into it. Do not use the `console` exporter under the SDK, because stdout is the SDK's message channel. Export errors fail silently unless `CLAUDE_CODE_OTEL_DIAG_STDERR=1` is set (v2.1.179+). This is still the recommended production default.
- source: https://code.claude.com/docs/en/agent-sdk/observability
- confidence: [VERIFIED]

### Per-user attribution mechanism
- was: Attach a user identifier via hooks or OTel resource attributes to get per-developer cost dashboards — the usual prerequisite for chargeback.
- now: `[VERIFIED]` Attach end-user identity as `OTEL_RESOURCE_ATTRIBUTES` (e.g. `enduser.id=…,tenant.id=…`, percent-encoded) on each `query()` call. The built-in identity attributes identify the *credential*, not the end user. With end-user identity attached, `tool_decision`, `tool_result`, `mcp_server_connection` and `permission_mode_changed` events become a per-user audit trail you can send to a SIEM. This is the usual prerequisite for chargeback.
- source: https://code.claude.com/docs/en/agent-sdk/observability
- confidence: [VERIFIED]

### Graphite line is missing its subject
- was: `[VERIFIED]` Confirmed: deal announced **December 19, 2025** (cash + equity, undisclosed terms; Graphite to continue as a standalone product). No change needed — listed only to record it was re-verified.
- now: `[VERIFIED]` **Cursor agreed to acquire Graphite**, announced **December 19, 2025** (cash + equity, undisclosed terms). Graphite continues as an independent product with the same team. No 2026 report of Graphite or its Diamond reviewer shutting down was found. (The line as written never names the acquirer or the target, so it is unreadable out of context.)
- source: https://cursor.com/blog/graphite ; https://techcrunch.com/2025/12/19/cursor-continues-acquisition-spree-with-graphite-deal
- confidence: [VERIFIED]

## Status changes

### Cursor (Bugbot's vendor) is now owned by SpaceX
- was: (not in file) Cursor Bugbot appears in the table with no ownership note.
- now: `[REPORTED]` SpaceX acquired Anysphere, Cursor's parent: purchase right announced Apr 21, 2026, exercise announced Jun 16, 2026, all-stock, closed **Aug 14, 2026**. Cursor runs as a wholly owned subsidiary and Bugbot is still sold. This is not a breaking change for Bugbot users. Note that the Wikipedia article is internally inconsistent, naming the parent as "SpaceX" in the body and "SpaceXAI" in the infobox. This predates the 2026-10-09 verification but was missing from the file.
- source: https://en.wikipedia.org/wiki/Cursor_(company)
- confidence: [REPORTED]

## New entries

### Hook timeouts fail open by default
- now: `[VERIFIED]` If a `command`, `http` or `mcp_tool` hook times out or fails, it does **not** block by default. Set `"onFailure": "block"` (Claude Code v2.1.295+) to make gates fail closed. Exit 1 is non-blocking, so use exit 2 (or JSON `permissionDecision: "deny"`) for enforcement. A silent exit 0 does not approve the call; the normal permission flow still applies.
- source: https://code.claude.com/docs/en/hooks
- confidence: [VERIFIED]
- why include: the file's "deterministic exit codes" and "PreToolUse is the primary security checkpoint" advice is wrong without this. A slow gate script quietly lets the call through unless `onFailure: "block"` is set.

### `if` path-matching semantics changed
- now: `[VERIFIED]` From v2.1.214, the hook `if` matcher `Edit(src/**)` matches only the top-level `src` directory. Use `Edit(**/src/**)` to match at any depth.
- source: https://code.claude.com/docs/en/hooks
- confidence: [VERIFIED]
- why include: the file's own example ("Never touch `migrations/`" as a PreToolUse deny) misses nested paths under the new matching rule.

## Could not verify
none found

## No longer relevant
none found
