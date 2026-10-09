<p align="center">
  <img src="assets/banner.svg" alt="claude-code-ecosystem — field reference for the Claude Code tooling ecosystem" width="900"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/snapshot-2026--09--19-388BFD?style=flat-square&labelColor=0D1117" alt="snapshot 2026-09-19"/>
  <img src="https://img.shields.io/badge/verified-2026--09--22-3FB950?style=flat-square&labelColor=0D1117" alt="last verified 2026-09-22"/>
  <img src="https://img.shields.io/badge/horizon-7_days-E3B341?style=flat-square&labelColor=0D1117" alt="verify every 7 days"/>
  <img src="https://img.shields.io/badge/license-MIT-6E7681?style=flat-square&labelColor=0D1117" alt="MIT"/>
</p>

---

A **weekly-verified** reference [skill](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) for the Claude Code tooling ecosystem — what tools exist, what each layer does, how they compose, and which ones to skip. Every non-obvious claim carries a confidence tag (`[VERIFIED]`, `[REPORTED]`, `[VENDOR]`, `[DISPUTED]`) and a source. The reference files are structured, not prose — meant to be read by a model, not a marketing team.

## Install

```bash
git clone https://github.com/Claude-Booster/claude-code-ecosystem \
  ~/.claude/skills/claude-code-ecosystem
```

Claude Code auto-discovers skills in `~/.claude/skills/`. Once cloned, the skill loads on description match — no further configuration.

To invoke it explicitly in a session:

```
/claude-code-ecosystem what MCP servers should I add?
```

## What's inside

Eight reference files, each with `last_verified` and `verify_horizon_days` front matter. When a file is past its horizon, treat `[VOLATILE]` claims as unverified until the next refresh run.

| File | Covers |
|---|---|
| [`core-surfaces.md`](references/core-surfaces.md) | CLI, models, pricing, IDE integrations, GitHub Actions, Bedrock / Vertex / Foundry |
| [`mcp-servers.md`](references/mcp-servers.md) | MCP server selection, registries, gateways, tool poisoning and injection attacks |
| [`skills-and-plugins.md`](references/skills-and-plugins.md) | Skills ecosystem, authoring conventions, plugins, marketplaces |
| [`orchestration.md`](references/orchestration.md) | Spec-driven dev, multi-agent frameworks, worktree managers, session control planes |
| [`context-and-cost.md`](references/context-and-cost.md) | CLAUDE.md conventions, AGENTS.md, memory tools, usage monitors, rate limits |
| [`gates-and-observability.md`](references/gates-and-observability.md) | Hooks as enforcement, OpenTelemetry, AI code review tool selection |
| [`landscape.md`](references/landscape.md) | Cursor, Codex CLI, Cline, Amp, Factory — architecture and current status |
| [`evidence-ledger.md`](references/evidence-ledger.md) | Known fabrications, disputed figures, verified primary sources |

## Routing

Read one file. Read a second only if the first genuinely doesn't answer the question.

| Question is about | Read |
|---|---|
| CLI primitives · models · pricing · IDE · GitHub Actions | `core-surfaces` |
| MCP server selection · registries · gateways · MCP security | `mcp-servers` |
| Skills · plugins · marketplaces · authoring conventions | `skills-and-plugins` |
| Multi-agent · spec-driven dev · frameworks · worktrees | `orchestration` |
| CLAUDE.md · memory · usage monitors · rate limits · spend | `context-and-cost` |
| Hooks · OpenTelemetry · AI code review tools | `gates-and-observability` |
| Cursor · Codex CLI · Cline · Amp · other CLIs | `landscape` |
| Whether a specific number or claim is trustworthy | `evidence-ledger` |

## Staying current

Each reference file is re-verified on a 7-day horizon. Two ways to run it:

**Locally (manual):**

```bash
# Which reference files are past their verify window (offline, no API cost)
python3 scripts/check_refs.py

# Headless Claude re-verifies the stale files → patches in updates/YYYY-MM-DD/
./scripts/refresh.sh
```

`refresh.sh` never edits `references/` — it only emits review patches. Apply what you accept and **bump `last_verified`** in the file's front matter (forgetting that bump silently stops the loop), or run `python3 scripts/apply_patches.py` to apply them automatically.

**On CI (automatic):** the [`reference-auto-refresh`](.github/workflows/reference-staleness.yml) workflow runs every Monday (05:00 UTC). It detects stale files, runs `refresh.sh`, applies the patches, and lands the result as an **auto-merge PR** that merges once the `verify` check passes.

### Self-hosting the refresh loop (forks)

The CI loop needs secrets and repo settings that cloning does **not** create. Without them the Monday run silently does nothing.

**Secrets** — repo → Settings → Secrets and variables → Actions:

| Secret | Purpose |
|---|---|
| `CLAUDE_CODE_OAUTH_TOKEN` | Auth for the headless Claude that re-verifies the files |
| `REFRESH_APP_ID` / `REFRESH_APP_PRIVATE_KEY` | A **GitHub App** (repo permissions **Contents: Read & write** + **Pull requests: Read & write**, *installed on the repo*). The job opens the PR with the App token on purpose — a `GITHUB_TOKEN`-authored PR does **not** trigger the `verify` check, so auto-merge would hang forever |
| `BLOCKED_PATTERNS` | Only if you also run the `verify` commit-guard workflow — the restricted-identifier regex it scans for |

**Repo settings:**

- **Allow auto-merge: ON** and **squash merging allowed** (Settings → General → Pull Requests) — the job uses `gh pr merge --squash --auto`.
- **Branch protection** on the default branch **requiring the `verify` status check**, so auto-merge waits for it. The App-authored PR satisfies the check legitimately, so no bypass is needed even with `enforce_admins`.

**Gotcha — registration:** a workflow's schedule only fires once GitHub Actions has *registered* it. A workflow that arrives via a bulk history push and has no `push:` trigger may never register. If `gh workflow list` doesn't show `reference-auto-refresh`, push a trivial edit to the workflow file on the default branch to force registration.

## Security note

This repo ships [`.claude/settings.json`](.claude/settings.json) with a `Bash(./scripts/refresh.sh*)` allow rule so the refresh script runs without a prompt. Review it before trusting project-level Claude Code settings in any session — a repo's `.claude/settings.json` is a [known attack surface](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-59536).

## License

MIT
