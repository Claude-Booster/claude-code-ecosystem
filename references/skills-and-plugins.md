---
last_verified: 2026-10-12
volatility: medium
verify_horizon_days: 7
primary_sources:
  - https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
  - https://code.claude.com/docs/en/discover-plugins
---

# Skills and Plugins

Snapshot 2026-10-12.

## Contents
- Why Skills displaced MCP
- Authoring conventions
- Notable skill collections
- Plugin mechanics
- Marketplaces and notable plugins

## Why Skills displaced MCP

`[VERIFIED]` Anthropic launched Agent Skills on 2025-10-16 and published the format as an open standard on 2025-12-18 (now hosted at agentskills.io). The file merges these two dates into one. The error was already there before 2026-10-09; nothing changed after that date. By 2026 they are the recommended packaging for repeatable workflows, because of **progressive disclosure**:

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
| `obra/superpowers` | Jesse Vincent's flagship framework — reframes Claude Code as a small dev team: brainstorming, subagent-driven dev, systematic debugging, red/green TDD, skill authoring. MIT. Accepted into Anthropic's marketplace. | `[VERIFIED]` ~298k GitHub stars (297,960 from the GitHub API on 2026-10-12; repo not archived, last push 2026-10-10, MIT). This is a primary source, so the dispute is settled as of this date. The figure is still rising, so quote it with its date. The official catalog also lists Superpowers at `[VENDOR]` 1,009,371 installs, with no "Anthropic verified" badge. |
| `awesome-claude-skills`, `ComposioHQ/awesome-claude-skills` | curated lists | |
`[VERIFIED]` `gsd-build/get-shit-done` was archived by its owner on 2026-06-26 and is read-only. Its README ("GSD Has Moved") names **open-gsd/gsd-core** as the active home. That repo is live: created 2026-05-22, last push 2026-10-12, about 10.4k stars. This happened before 2026-10-09, so it is an existing error, not a new event. The file currently presents an archived project as live. gstack (`garrytan/gstack`) is live: not archived, last push 2026-10-12.
| Vendor skills | Vercel React best-practices, Supabase, Sentry, Trail of Bits static-analysis, n8n, Hookdeck | Usually the highest signal-to-noise — maintained by people who own the API |

## Plugin mechanics

Plugins bundle skills, commands, subagents, hooks, and MCP servers into one versioned installable unit. `[VERIFIED]` Launched 2025-10-09.

```
/plugin marketplace add owner/repo
/plugin install <name>@<marketplace>
```

Installed to `~/.claude/plugins/`. Toggle on and off without touching project config. Orgs can sync plugin sets from claude.ai.

## Marketplaces and notable plugins

**Official** (`claude-plugins-official`, Anthropic-curated): `[VENDOR]` The official web catalog lists **342 plugins** (claude.com/marketplace/plugins header, 2026-10-12). Treat the number as drifting. The docs still say the catalog "changes often, so this page doesn't list it." The Anthropic-built vs. partner-built split (~33/~68) is no longer published anywhere primary; Anthropic's docs now say the catalog "changes often, so this page doesn't list it." Anthropic's own named plugins still include commit-commands, code-review, feature-dev, security-guidance, and the language-server plugins.

**Community marketplaces:** buildwithclaude.com, claudemarketplaces.com, aitmpl.com, Agensi. `[REPORTED]` third-party plugin count reached the thousands by mid-2026.

**Standouts:**

- **Frontend Design** — Anthropic's most-installed plugin, `[VENDOR]` Anthropic's catalog shows **1,134,112 installs** on the Frontend Design detail page (2026-10-12). The detail page also marks it "Anthropic verified" and "Made by Anthropic." The grid page at /marketplace/plugins shows no counts, but each plugin's detail page does, and Anthropic's docs say the web catalog "shows install counts." So the claim that there is no primary count is wrong. On ranking: Frontend Design has more installs than every other detail page checked (Superpowers 1,009,371; Code Review 438,525; Context7 417,801). Not all 342 listings were checked, so keep "most-installed" as `[REPORTED]`. The "most-installed official-marketplace plugin" ranking is still consistently reported. Anchors UI output to design tokens and patterns so results don't read as generic. Relevant to anyone complaining that AI-generated interfaces look templated.
- **pr-review-toolkit** — specialized review subagents
- **security-guidance**
- **LSP plugins** (pyright, etc.) — cheap, high-value; give the agent real symbol resolution
- **Langfuse-observability** — a tracing plugin made by Langfuse and listed in the official marketplace. It does not have the "Anthropic verified" badge. `[VENDOR]` 575 installs (2026-10-12). "Official" should mean "in the official marketplace," not "made by Anthropic." At this install count, its place in "Standouts" is weak.

**Caution:** installing plugins re-creates the MCP bloat problem one level up, since plugins can carry MCP servers. Check what a plugin bundles before installing.
