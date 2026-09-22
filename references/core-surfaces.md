---
last_verified: 2026-09-22
volatility: high
verify_horizon_days: 7
primary_sources:
  - https://code.claude.com/docs/en/model-config
  - https://code.claude.com/docs/en/github-actions
  - https://www.anthropic.com/news
---

# Core Surfaces (First-Party)

Snapshot 2026-09-19.

## Contents
- Extension primitives
- Models and routing
- IDE, GitHub, and CI
- Web, desktop, mobile, Cowork
- Remote control
- Multi-agent (official)
- Enterprise deployment

## Extension primitives

All official, listed cheapest-context-first:

| Primitive | Location | Loads when | Use for |
|---|---|---|---|
| CLAUDE.md | repo root, subdirs, `~/.claude/` | always | durable pointers and gotchas |
| Skills | `.claude/skills/<name>/SKILL.md` | on description match | repeatable workflows |
| Slash commands | `.claude/commands/` | on invocation | parameterized prompts |
| Subagents | `.claude/agents/` | on delegation | isolated context for a subtask |
| Hooks | `.claude/settings.json` | lifecycle events | deterministic enforcement |
| Output styles | settings | session | response shape |
| MCP servers | `.mcp.json` | session start | reaching external systems |
| Plugins | `~/.claude/plugins/` | on install | bundling all of the above |

Built-in commands worth knowing: `/init`, `/compact`, `/context`, `/review`, `/security-review`, `/usage`, `/status`, `/cost`, `/rewind` (also Esc-Esc for checkpoints).

`[VERIFIED]` **Hooks are the only deterministic guardrail.** Anthropic's own guidance states CLAUDE.md is advisory by construction — the model follows it most of the time — and that real enforcement requires hooks and permissions. PreToolUse is the primary security checkpoint. The frequently-quoted "70% vs 100%" compliance split is community framing, not an Anthropic figure `[REPORTED]`.

**Headless mode:** `claude -p "<prompt>" --allowedTools <list>` for scripted/CI use. The **Claude Agent SDK** wraps the same loop programmatically (runs the CLI as a child process) and emits OpenTelemetry natively.

## Models and routing

`[VERIFIED]` against official docs at snapshot. `[VOLATILE]` — model lineups shift quarterly.

| Model | Released | Input / Output per Mtok | Use for |
|---|---|---|---|
| Fable 5.1 | Mythos tier | — | explicit selection only, never a default |
| Opus 5 | 2026-07-24 | $5 / $25 | hard multi-file reasoning, architecture |
| Sonnet 5 | 2026-06-30 | $2 / $10 | daily driver |
| Haiku 4.5 | 2025-10 | ~$1 / $5 | subagent fan-out, mechanical edits |

Legacy Opus 4.5–4.8 and Sonnet 4.5/4.6 remain pinnable by model ID.

`[VERIFIED]` **There is no single global default** — it is plan- and provider-dependent. Max, Team Premium, Enterprise, and the Anthropic API default to Opus 5. Pro and Team Standard default to Sonnet 5. Microsoft Foundry defaults to Sonnet 4.5.

`[VERIFIED]` Sonnet 5 pricing was made permanent 2026-08-10, cancelling a planned increase to $3/$15.

`[DISPUTED]` Many blogs assert "Opus 4.8 is the default" or "Sonnet 4.6 is current." Both were briefly true earlier in 2026 and are now stale. Do not repeat them.

## IDE, GitHub, and CI

- **VS Code** and **JetBrains** extensions are official. VS Code gained screen-reader/accessibility support in 2026.
- **GitHub Action:** `anthropics/claude-code-action@v1`. `[VERIFIED]` Two auto-detected modes — *interactive* (waits for an `@claude` trigger phrase in issues/PRs) and *automation* (runs a supplied prompt). Install via `/install-github-app`. Supports `/review` and `/fix`.
- Automatic PR Code Review is a **distinct product** requiring the official GitHub app, not the same thing as the action.
- `[VERIFIED]` **Self-hosted runners:** `claude self-hosted-runner`, public beta for Team/Enterprise — run sessions on your own compute.

## Web, desktop, mobile, Cowork

- Claude Code runs at `claude.ai/code` (clone, edit, open PRs with no local setup), plus desktop and mobile apps.
- **Cowork** — "Claude Code without the code." Research preview 2026-01-12, GA 2026-04-09. By Sept 2026 runs on web and mobile with remote cloud-sandbox execution as default. Shares Projects and Artifacts with Chat. Isolated Linux VM (Apple Virtualization on macOS, QEMU/KVM on Linux).

`[VERIFIED]` **Cowork compliance gap:** as of May 2026 Cowork activity was excluded from Audit Logs, Compliance API, and Data Exports. Flag this for any regulated-industry user.

`[VERIFIED]` **Known CVEs:** CVE-2025-59536 (malicious hooks planted in a repo's `.claude/settings.json`), CVE-2026-21852 (API key exfiltration via `ANTHROPIC_BASE_URL`). Both make cloning untrusted repos with broad permissions a live risk, not a hypothetical one.

## Remote control

First-party, replacing most community bridges:

| Feature | Shipped | What it does |
|---|---|---|
| Remote Control | 2026 | drive a local CLI session from the Claude mobile app |
| Channels | 2026-03-20 | control sessions from Telegram/Discord; iMessage added 2026-03-26 |
| Dispatch | 2026 | message a task from phone, spawns a Desktop session |

If a user is building a custom Telegram/Slack control plane, check whether Channels already covers it.

## Multi-agent (official)

Progression, each more autonomous:

1. **Subagents** — isolated context windows, stable, general availability.
2. **Agent Teams** — experimental. Gated behind `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`, invoked with `/team`. Shipped in the Opus 4.6 era.
3. **Dynamic workflows** — research preview. Claude writes an orchestration script on the fly and fans out coordinated subagents. `[REPORTED]` Jarred Sumner credited dynamic workflows plus adversarial code review for rewriting Bun from Zig to Rust in six days.

Also: background tasks, checkpointing, sandboxing.

## Enterprise deployment

`[VERIFIED]` Officially supported: **Amazon Bedrock**, **Google Vertex AI** (now branded Google Cloud's Agent Platform), **Claude Platform on AWS**, **Microsoft Foundry**, and generic **LLM gateways/proxies** via `ANTHROPIC_BASE_URL` / `ANTHROPIC_AUTH_TOKEN`.

Gateway model discovery: `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1`. LiteLLM is documented, with an explicit Anthropic disclaimer that third-party gateways are neither endorsed nor audited.

`[DISPUTED]` **"Anthropic Foundry" is not a product.** Secondary sources conflating this with Microsoft Foundry are wrong. Correct the user if they use the term.
