---
last_verified: 2026-09-22
volatility: medium
verify_horizon_days: 7
primary_sources:
  - https://github.com/modelcontextprotocol/servers
  - https://code.claude.com/docs/en/mcp
---

# MCP Servers

Snapshot 2026-09-19.

## Contents
- Selection rule
- The essential set
- Second tier
- Archived / do not recommend
- Registries and gateways
- Security

## Selection rule

Every active MCP server injects its tool definitions into **every turn**. A heavy server can cost 18K+ tokens per turn `[REPORTED]`. This means:

- Start with zero. Add one server, justify it, measure `/context`, repeat.
- Prefer a **Skill** if the workflow doesn't need live external data. Skills load only on description match.
- Scope tools per client where the server supports it. Serena in particular ships a large tool surface.
- Project-scoped `.mcp.json` beats global config — servers a project doesn't need shouldn't load.

When a user complains about context exhaustion or degraded quality, check server count before anything else.

## The essential set

| Server | Maintainer | What it does | Note |
|---|---|---|---|
| **Serena** | Oraios AI (MIT) | LSP-backed symbol-level code retrieval and editing; persistent project memory | Highest leverage on large codebases. `[REPORTED]` ~19–24k stars. Launch with a scoped tool set or it becomes the most common self-inflicted context wound. |
| **Context7** | Upstash | live, version-specific library documentation | Fixes the stale-API-surface failure mode |
| **Playwright** | Microsoft (official) | browser automation | Enables the write-UI → drive-browser → verify loop |
| **GitHub MCP** | GitHub | issues, PRs, repo ops | |
| One DB server | varies | schema introspection, queries | **Use a read-only role.** A write-capable DSN is a footgun. |

That's the whole default set. Five servers is already a lot.

## Second tier

Add only on a concrete need: Chrome DevTools MCP, Figma, Sentry, Linear, Jira/Atlassian, Notion, Supabase, Slack, Firecrawl, **Exa** (`[REPORTED]` most-used web-search server for coding agents).

Official reference servers still maintained: Filesystem (directory-scoped, foundational), Fetch, Sequential Thinking, Memory, Git.

## Archived / do not recommend

`[VERIFIED]` The **official Postgres reference server is archived**. The `modelcontextprotocol/servers` repo split into current and archived sets. Recommend a maintained alternative such as Postgres MCP Pro instead, always with a read-only role.

Check archive status before recommending any reference server by memory — the split moved several.

## Registries and gateways

**Registries:** the official MCP registry (`[REPORTED]` 17,000+ servers), plus community directories — claudedirectory.org, mcp.directory, LobeHub, awesome-mcp-servers.

**Gateways** (worth it past ~5 servers or any multi-user setup): MintMCP, MCP Manager, Aptible MCP Gateway, Obot. They centralize the trust boundary: server allowlisting, tool-level access control, audit logging, credential management.

## Security

This is the part to take seriously. MCP's tool-description field is unsanitized input that reaches the model.

**Tool poisoning** — malicious instructions embedded in tool *metadata*, loaded at session init before any visible work happens.

**Indirect prompt injection** — malicious instructions in tool *outputs*. Worse than poisoning in one respect: descriptions get a connect-time review, outputs get none.

`[VERIFIED]` Hasan et al. 2025 (arXiv:2506.13538) surveyed 1,899 open-source MCP servers: **7.2% contained general security vulnerabilities, 5.5% exhibited MCP-specific tool-poisoning vectors.**

`[VERIFIED]` CSA research note, July 2026: leading IDEs — Cursor, Claude Code, Gemini CLI, Copilot, Amazon Q — auto-execute project-defined MCP servers with developer-level OS privileges and no process isolation.

**Controls that converge across NSA/CISA-adjacent guidance (June 2026) and Microsoft's state-of-MCP-security (2026):**

- OAuth 2.1 + PKCE + audience-bound tokens
- Treat `.mcp.json` changes as production code review — a repo that ships its own MCP config is a supply-chain vector
- Isolate servers holding sensitive credentials
- Scan tool descriptions, not just tool code
- Minimize active servers (also the context argument — the incentives align here)

**Practical answer when a user asks "is this MCP server safe?":** you cannot tell from the name. Check maintainer, whether it's in the official registry, what credentials it wants, and whether the repo's `.mcp.json` was authored by someone other than the user.
