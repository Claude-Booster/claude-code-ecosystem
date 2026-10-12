---
last_verified: 2026-10-12
volatility: medium
verify_horizon_days: 7
primary_sources:
  - https://github.com/modelcontextprotocol/servers
  - https://code.claude.com/docs/en/mcp
---

# MCP Servers

Snapshot 2026-10-12.

## Contents
- Selection rule
- The essential set
- Second tier
- Archived / do not recommend
- Registries and gateways
- Security

## Selection rule

`[VERIFIED]` Claude Code turns tool search on by default. MCP tool definitions are held back until needed, and only tool names and server instructions load at session start. All tools still load upfront in these cases: This means:

- Start with zero. Add one server, justify it, measure `/context`, repeat.
- Prefer a **Skill** if the workflow doesn't need live external data. Skills load only on description match.
- Scope tools per client where the server supports it. Serena in particular ships a large tool surface.
- Project-scoped `.mcp.json` beats global config — servers a project doesn't need shouldn't load.

When a user complains about context exhaustion or degraded quality, check server count before anything else.

## The essential set

| Server | Maintainer | What it does | Note |
|---|---|---|---|
| **Serena** | Oraios AI (GPL-3.0-or-later for the Serena application; its SolidLSP component stays MIT). The licence was split by component in a commit dated 2026-09-14, with a CLA added; the change is not retroactive. `[VERIFIED]` | LSP-backed symbol-level code retrieval and editing; persistent project memory | Highest leverage on large codebases. `[VERIFIED]` ~30k stars (GitHub repo page, 2026-10-12) `[VENDOR]` Serena's README says its basic file and shell tools (`search_for_pattern`, `replace_content`, `list_dir`, `find_file`, `read_file`, `execute_shell_command`) are "typically disabled by default" when it runs inside harnesses such as Claude Code. Tools can be scoped through YAML at the global, launch-command, project, context and mode levels. Scoping is still advised. |
| **Context7** | Upstash | live, version-specific library documentation | Fixes the stale-API-surface failure mode |
| `[VENDOR]` The project is still active and not archived. Its README now says "If you are using a coding agent, you might benefit from using the CLI+SKILLS instead", and keeps MCP for long-running or exploratory work that needs persistent browser state. |
| **GitHub MCP** | GitHub | issues, PRs, repo ops | |
| One DB server | varies | schema introspection, queries | **Use a read-only role.** A write-capable DSN is a footgun. |

That's the whole default set. Five servers is already a lot.

## Second tier

Add only on a concrete need: Chrome DevTools MCP, Figma, Sentry, Linear, Jira/Atlassian, Notion, Supabase, Slack, Firecrawl, **Exa** (`[REPORTED]` most-used web-search server for coding agents).

`[VERIFIED]` The current reference servers are Everything (a test server), Fetch, Filesystem, Git, Memory, Sequential Thinking and Time. The archived set is AWS KB Retrieval, Brave Search, EverArt, GitHub, GitLab, Google Drive, Google Maps, PostgreSQL, Puppeteer, Redis, Sentry, Slack and SQLite. Brave Search was replaced by the official `@brave/brave-search-mcp-server`. Slack is now maintained by Zencoder.

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

`[DISPUTED]` The CSA note (2026-07-01) does name Claude Code among IDEs that auto-execute project-defined servers. Claude Code's own docs disagree for interactive use: Claude Code asks for approval before using `.mcp.json` servers, and approvals committed in an untrusted cloned repo are ignored. Project servers do load without a prompt in `claude -p` and Agent SDK runs. The process-isolation part of the CSA claim stands for the other tools named.

**Controls that converge across NSA/CISA-adjacent guidance (June 2026) and Microsoft's state-of-MCP-security (2026):**

- OAuth 2.1 + PKCE + audience-bound tokens
- Treat `.mcp.json` changes as production code review — a repo that ships its own MCP config is a supply-chain vector
- Isolate servers holding sensitive credentials
- Scan tool descriptions, not just tool code
- Minimize active servers (also the context argument — the incentives align here)

**Practical answer when a user asks "is this MCP server safe?":** you cannot tell from the name. Check maintainer, whether it's in the official registry, what credentials it wants, and whether the repo's `.mcp.json` was authored by someone other than the user.
