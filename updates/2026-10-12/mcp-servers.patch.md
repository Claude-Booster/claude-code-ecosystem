I found six corrections, two status changes and three new entries. The patch is below. Two of the corrections need your attention before merging. The tool-search one changes the reasoning of the whole Selection rule section, so it's worth a human look. The Claude Code part of the CSA claim is also contradicted by Claude Code's own docs and becomes `[DISPUTED]`. I counted 11 web searches. The repo's GitHub API calls through `gh`/`curl` failed or were blocked, so I fetched those pages directly instead.

# Patch: mcp-servers.md
verified_against: 2026-10-12
searches_run: 11
verdict: CHANGED

## Changed

### Tool definitions are deferred by default (Selection rule premise)
- was: Every active MCP server injects its tool definitions into **every turn**. A heavy server can cost 18K+ tokens per turn `[REPORTED]`.
- now: `[VERIFIED]` Claude Code turns tool search on by default. MCP tool definitions are held back until needed, and only tool names and server instructions load at session start. All tools still load upfront in these cases:
  - `ENABLE_TOOL_SEARCH=false`
  - `auto` threshold mode, while the definitions total less than 10% of the context window
  - a server set to `alwaysLoad: true`, or a tool marked `_meta["anthropic/alwaysLoad"]`
  - `ANTHROPIC_BASE_URL` pointing to a non-first-party host
  - Azure-hosted Microsoft Foundry
  - models older than the 4.5 generation on Google Cloud's Agent Platform

  In those cases the per-turn cost (the 18K+ figure `[REPORTED]`) still applies. Server instructions and tool descriptions are each cut off at 2,048 characters by default.
- source: https://code.claude.com/docs/en/mcp (section "Scale with MCP tool search" / "Configure tool search")
- confidence: [VERIFIED]
- note: This is not a change made after 2026-10-09. The primary source already contradicted the file's main argument at that date. The follow-on lines need rewording to match, and that is a human edit:
  - "Start with zero… measure `/context`"
  - "check server count before anything else" should become something like "check `alwaysLoad` servers and whether tool search is on"
  - the contrast that Skills load "only on description match"

### Serena license
- was: **Serena** | Oraios AI (MIT)
- now: **Serena** | Oraios AI (GPL-3.0-or-later for the Serena application; its SolidLSP component stays MIT). The licence was split by component in a commit dated 2026-09-14, with a CLA added; the change is not retroactive. `[VERIFIED]`
- source: https://github.com/oraios/serena (README licence section; LICENSE commit `6707cd9`, https://api.github.com/repos/oraios/serena/commits?path=LICENSE)
- confidence: [VERIFIED]

### Serena star count
- was: `[REPORTED]` ~19–24k stars.
- now: `[VERIFIED]` ~30k stars (GitHub repo page, 2026-10-12)
- source: https://github.com/oraios/serena
- confidence: [VERIFIED]

### Serena default tool surface in agent harnesses
- was: Launch with a scoped tool set or it becomes the most common self-inflicted context wound.
- now: `[VENDOR]` Serena's README says its basic file and shell tools (`search_for_pattern`, `replace_content`, `list_dir`, `find_file`, `read_file`, `execute_shell_command`) are "typically disabled by default" when it runs inside harnesses such as Claude Code. Tools can be scoped through YAML at the global, launch-command, project, context and mode levels. Scoping is still advised.
- source: https://github.com/oraios/serena
- confidence: [VENDOR]

### Reference servers still maintained
- was: Official reference servers still maintained: Filesystem (directory-scoped, foundational), Fetch, Sequential Thinking, Memory, Git.
- now: `[VERIFIED]` The current reference servers are Everything (a test server), Fetch, Filesystem, Git, Memory, Sequential Thinking and Time. The archived set is AWS KB Retrieval, Brave Search, EverArt, GitHub, GitLab, Google Drive, Google Maps, PostgreSQL, Puppeteer, Redis, Sentry, Slack and SQLite. Brave Search was replaced by the official `@brave/brave-search-mcp-server`. Slack is now maintained by Zencoder.
- source: https://github.com/modelcontextprotocol/servers
- confidence: [VERIFIED]

### CSA auto-execution claim as it applies to Claude Code
- was: `[VERIFIED]` CSA research note, July 2026: leading IDEs — Cursor, Claude Code, Gemini CLI, Copilot, Amazon Q — auto-execute project-defined MCP servers with developer-level OS privileges and no process isolation.
- now: `[DISPUTED]` The CSA note (2026-07-01) does name Claude Code among IDEs that auto-execute project-defined servers. Claude Code's own docs disagree for interactive use: Claude Code asks for approval before using `.mcp.json` servers, and approvals committed in an untrusted cloned repo are ignored. Project servers do load without a prompt in `claude -p` and Agent SDK runs. The process-isolation part of the CSA claim stands for the other tools named.
- source: https://labs.cloudsecurityalliance.org/research/csa-research-note-mcp-tool-poisoning-auto-execution-20260701/ ; https://code.claude.com/docs/en/mcp
- confidence: [DISPUTED]

## Status changes

### GitHub MCP server v2.0 (compatibility and Go module path changes)
- was: **GitHub MCP** | GitHub | issues, PRs, repo ops | (no note)
- now: `[VERIFIED]` v2.0.0 shipped 2026-10-06. It advertises output schemas only to clients on MCP protocol 2026-07-28 or later, and it does not return compound tools to older clients. v2.0.1 (2026-10-07) is a Go-only breaking change: imports must use `github.com/github/github-mcp-server/v2`. Current release is v2.0.2 (2026-10-08). Renamed tools keep their old names as aliases. Tools can be scoped with `--toolsets` / `GITHUB_TOOLSETS`. The remote endpoint is `https://api.githubcopilot.com/mcp/`.
- source: https://api.github.com/repos/github/github-mcp-server/releases ; https://github.com/github/github-mcp-server
- confidence: [VERIFIED]

### Playwright MCP: vendor now points coding agents to CLI + Skills
- was: **Playwright** | Microsoft (official) | browser automation | Enables the write-UI → drive-browser → verify loop
- now: `[VENDOR]` The project is still active and not archived. Its README now says "If you are using a coding agent, you might benefit from using the CLI+SKILLS instead", and keeps MCP for long-running or exploratory work that needs persistent browser state.
- source: https://github.com/microsoft/playwright-mcp
- confidence: [VENDOR]

All other named servers are still live. Serena, Context7, Playwright, GitHub MCP and Postgres MCP Pro were checked on GitHub, and none is archived (Postgres MCP Pro's last push was 2026-08-17).

## New entries

### First MCP vulnerability on CISA's Known Exploited Vulnerabilities (KEV) list (LiteLLM, CVE-2026-59822)
- now: `[REPORTED]` CVE-2026-59822 is an authentication bypass in LiteLLM's MCP Streamable HTTP endpoint: arbitrary bearer tokens were accepted. It affects versions before 1.84.0, is fixed in 1.84.0 (GHSA-7488-6r32-c95q), and was added to CISA KEV on 2026-09-02. Wiz saw it exploited in the wild.
- source: https://www.wiz.io/blog/off-guard-breaking-litellm-from-authentication-bypass-to-cloud-compromise ; https://aiweekly.co/alerts/cisa-adds-litellm-mcp-auth-bypass-and-six-flaws-to-kev
- confidence: [REPORTED]
- why include: An actively exploited flaw in an MCP gateway backs up the Security section's point that gateways are trust boundaries. That point is currently argued only in the abstract.

### Obot gateway authorization-bypass advisory
- now: `[VENDOR]` Obot's own advisory: the deny list missed `/mcp-connect-composite/`, which reopened an authorization bypass because the earlier GHSA-vw82 fix was incomplete.
- source: https://github.com/obot-platform/obot/security/advisories/GHSA-6fwv-3h4c-37j9
- confidence: [VENDOR]
- why include: Obot is one of the four gateways the file recommends. A gateway advisory belongs next to that recommendation.

### Metadata-only scanners are easy to evade (refines "Scan tool descriptions")
- now: `[VENDOR]` In tests by Pluto Security (2026-09-15), every one of five public MCP scanners returned a clean or zero-finding result in at least one configuration. The scanners were Cisco mcp-scanner, Sentinel, Snyk agent-scan, MCP-Shield and NVIDIA SkillSpector. The tricks used:
  - keeping the malicious code in handlers rather than metadata
  - showing a harmless description to clients that identify as scanners
  - splitting indicators across the description and the parameter schema
  - padding files until they were too big for LLM review

  The suggested fix is layered: review the full source, test in isolation, limit access, and monitor at runtime.
- source: https://pluto.security/blog/malicious-mcp-servers-clean-scans/
- confidence: [VENDOR]
- why include: The control "Scan tool descriptions, not just tool code" can be read as meaning a scan is enough. This shows a clean scan proves little, which fits the file's "you cannot tell from the name" advice.

## Could not verify

- **Official registry "17,000+ servers" `[REPORTED]`:** The registry API (`registry.modelcontextprotocol.io/v0/servers`) gives no total count. The only recent count is one third-party analysis: 30,375 unique servers on 2026-09-10, taken from 99,114 server-version records (https://devtoolhub.com/mcp-registry-by-the-numbers/; the same author posted it on dev.to). The method is not published. "17,000+" probably still holds as a floor, but I can't independently confirm a current figure. Suggest marking it `[DISPUTED]` with both values, or rewording to "tens of thousands".
- **Exa "most-used web-search server for coding agents" `[REPORTED]`:** I found no primary source or usage data, only directory listings and a competitor comparison by Parallel, which says it is biased. I found nothing that contradicts it either.
- **Gateways "MCP Manager" and "Aptible MCP Gateway":** Searches returned nothing about either. MintMCP and Obot are confirmed active.
- **"NSA/CISA-adjacent guidance (June 2026)" and "Microsoft's state-of-MCP-security (2026)":** These are untagged and I didn't check them in this run.
- **Hasan et al. (arXiv:2506.13538):** The figures (1,899 servers, 7.2%, 5.5%) match the current version, v5 dated 2026-04-13. No change, noted here only for completeness.

## No longer relevant

none found
