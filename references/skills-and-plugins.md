---
last_verified: 2026-09-22
volatility: medium
verify_horizon_days: 7
primary_sources:
  - https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
  - https://code.claude.com/docs/en/discover-plugins
---

# Skills and Plugins

Snapshot 2026-09-19.

## Contents
- Why Skills displaced MCP
- Authoring conventions
- Notable skill collections
- Plugin mechanics
- Marketplaces and notable plugins

## Why Skills displaced MCP

`[VERIFIED]` Anthropic launched Agent Skills as an open standard in October 2025. By 2026 they are the recommended packaging for repeatable workflows, because of **progressive disclosure**:

1. Name + description only — always in context, ~100 words
2. SKILL.md body — loads when the description matches
3. Bundled `references/`, `scripts/`, `assets/` — load on demand; scripts execute without loading

MCP servers pay their full token cost every turn. Skills pay almost nothing until needed. So: **MCP for reaching external systems, Skills for everything else.**

Skills are portable across Claude Code, Codex, Cursor, and other agents — the format is an open standard, not Claude-specific.

## Authoring conventions

Community consensus, largely converged:

**Description is a routing rule, not a summary.** It is the only thing always in context and the sole trigger mechanism. Write it to fire at the right moment and not otherwise. Claude under-triggers skills by default, so lean slightly pushy: name the contexts and phrasings explicitly.

**Deterministic work goes in scripts, not prose.** "Be careful to validate X" is advisory. A `validate.py` the skill invokes is enforcement. This is the same principle as hooks-over-CLAUDE.md.

**Keep SKILL.md lean, push detail to reference files.** Under ~500 lines. Past that, add a hierarchy layer with explicit pointers to where the model should go next. Reference files over ~300 lines get their own table of contents.

**One clear job per skill.** Multi-purpose skills trigger unpredictably.

**Concrete worked examples beat abstract rules.** Imperative voice throughout.

**Organize by variant when a skill spans domains** — `references/aws.md`, `references/gcp.md`, etc., so only the relevant one loads.

## Notable skill collections

| Repo | What it is | Signal |
|---|---|---|
| `anthropics/skills` | Official. Skill Creator plus document skills. | Note: the pre-built PowerPoint/Excel/Word/PDF skills are **not** available in Claude Code. The bundled claude-api skill is. |
| `obra/superpowers` | Jesse Vincent's flagship framework — reframes Claude Code as a small dev team: brainstorming, subagent-driven dev, systematic debugging, red/green TDD, skill authoring. MIT. Accepted into Anthropic's marketplace. | `[DISPUTED]` star count. Sources cite 94k, 232k, and 288k. See `evidence-ledger.md` — do not quote a precise figure. |
| `awesome-claude-skills`, `ComposioHQ/awesome-claude-skills` | curated lists | |
| gstack, GSD, Ay-Skills | community frameworks | |
| Vendor skills | Vercel React best-practices, Supabase, Sentry, Trail of Bits static-analysis, n8n, Hookdeck | Usually the highest signal-to-noise — maintained by people who own the API |

## Plugin mechanics

Plugins bundle skills, commands, subagents, hooks, and MCP servers into one versioned installable unit. `[VERIFIED]` Launched 2025-10-09.

```
/plugin marketplace add owner/repo
/plugin install <name>@<marketplace>
```

Installed to `~/.claude/plugins/`. Toggle on and off without touching project config. Orgs can sync plugin sets from claude.ai.

## Marketplaces and notable plugins

**Official** (`claude-plugins-official`, Anthropic-curated): `[REPORTED]` ~100 entries — roughly 33 Anthropic-built (LSP language servers, feature-dev, code-review, commit-commands, security-guidance, frontend-design) and ~68 partner-built (GitHub, Playwright, Supabase, Figma, Vercel, Linear, Sentry, Stripe, Firebase).

**Community marketplaces:** buildwithclaude.com, claudemarketplaces.com, aitmpl.com, Agensi. `[REPORTED]` third-party plugin count reached the thousands by mid-2026.

**Standouts:**

- **Frontend Design** — Anthropic's most-installed plugin, `[REPORTED]` ~277k installs mid-2026. Anchors UI output to design tokens and patterns so results don't read as generic. Relevant to anyone complaining that AI-generated interfaces look templated.
- **pr-review-toolkit** — specialized review subagents
- **security-guidance**
- **LSP plugins** (pyright, etc.) — cheap, high-value; give the agent real symbol resolution
- **Langfuse-observability** — official tracing plugin

**Caution:** installing plugins re-creates the MCP bloat problem one level up, since plugins can carry MCP servers. Check what a plugin bundles before installing.
