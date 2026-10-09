I have enough to produce the patch. Key findings verified against primary sources: Serena's license is not MIT, its star count has moved, the reference-server list has shifted, and—most significantly—the Claude Code docs (a primary source) now document default-on MCP tool search that defers tool definitions, which directly contradicts the premise of the file's entire Selection rule section.

```markdown
# Patch: mcp-servers.md
verified_against: 2026-10-09
searches_run: 16
verdict: NEEDS_HUMAN

Reason for NEEDS_HUMAN: The "Selection rule" section is built on the premise that
"Every active MCP server injects its tool definitions into every turn." A primary
source (code.claude.com/docs/en/mcp) now documents MCP **tool search**, enabled by
default, which defers tool definitions and loads only tool names + server
instructions at session start. The section's framing and its headline cost
argument no longer hold by default. Whether to rewrite that framing is a human
call, so it is flagged rather than restructured. Discrete sourced corrections are
below.

## Changed

### Selection rule premise: tool definitions are no longer loaded every turn by default
- was: "Every active MCP server injects its tool definitions into **every turn**. A heavy server can cost 18K+ tokens per turn `[REPORTED]`."
- now: In Claude Code, **MCP tool search is enabled by default**: "Only tool names and server instructions load at session start, so adding more MCP servers has minimal impact on your context window." Full tool definitions are deferred and fetched on demand. Upfront injection (and the ~18K-tokens-per-turn cost) now applies only when tool search is disabled or unsupported — e.g. `ENABLE_TOOL_SEARCH=false`, a non-first-party `ANTHROPIC_BASE_URL`, Microsoft Foundry on Azure, or pre-4.5 models. `[VERIFIED]`
- source: https://code.claude.com/docs/en/mcp
- confidence: [VERIFIED]

### Serena license is GPL-3.0, not MIT
- was: "**Serena** | Oraios AI (MIT) | LSP-backed symbol-level code retrieval and editing..."
- now: Serena is licensed per component: the Serena application is **GPL-3.0-or-later**; only `src/solidlsp` (SolidLSP) is MIT. The README states "Distributions combining both are as a whole subject to the GPL." Describing it flatly as "MIT" is wrong. `[VERIFIED]`
- source: https://raw.githubusercontent.com/oraios/serena/main/README.md
- confidence: [VERIFIED]

### Serena star count
- was: "`[REPORTED]` ~19–24k stars."
- now: "`[REPORTED]` ~30k stars" (GitHub shows ~30.1k as of 2026-10-09).
- source: https://github.com/oraios/serena
- confidence: [REPORTED]

### Maintained reference-server list is incomplete
- was: "Official reference servers still maintained: Filesystem (directory-scoped, foundational), Fetch, Sequential Thinking, Memory, Git."
- now: The current maintained reference-server set is **Everything, Fetch, Filesystem, Git, Memory, Sequential Thinking, and Time**. The file omits **Time** (and the demo-oriented **Everything**).
- source: https://github.com/modelcontextprotocol/servers
- confidence: [VERIFIED]

## Status changes

### Brave Search reference server replaced by an official Brave server
- was: (not named individually in the file; covered by the general "the split moved several" note)
- now: The archived Brave Search reference server has been **replaced by an official `@brave/brave-search-mcp-server`**. `[VERIFIED]`
- source: https://github.com/modelcontextprotocol/servers
- confidence: [VERIFIED]

### Slack reference server now third-party maintained
- was: "Second tier: ... Slack ..."
- now: Slack remains recommendable, but the old reference server is archived and is **now maintained by Zencoder** (plus an official hosted `mcp.slack.com`). Not dead — re-homed. `[VERIFIED]`
- source: https://github.com/modelcontextprotocol/servers
- confidence: [VERIFIED]

Note: The Postgres-archived claim (line 53) still holds `[VERIFIED]`; the full
archived set is now 13 reference servers (incl. GitHub, GitLab, Slack, Sentry,
Puppeteer, SQLite). The file's "check archive status... the split moved several"
guidance remains accurate — the essential-set "GitHub MCP" entry correctly refers
to GitHub's own live `github/github-mcp-server`, not the archived reference one.

## New entries

### MCP tool search (Claude Code) — mechanism, not a server
- This is not a server but belongs in the Selection rule section as the thing that
  changed it. Clears the bar because the section's core advice ("measure
  `/context`", "check server count before anything else") must now account for
  deferral being on by default, with knobs (`ENABLE_TOOL_SEARCH`, per-server/per-tool
  `alwaysLoad`) that a reader needs to know exist.
- source: https://code.claude.com/docs/en/mcp
- confidence: [VERIFIED]

## Could not verify

### Exa as "most-used web-search server for coding agents"
- The file tags this `[REPORTED]`. Searched for usage/telemetry data behind the
  "most-used" claim and found none. Exa is clearly a leading coding-agent search
  server (built into OpenCode; markets exa-code for Cursor/Claude Code), but
  ranking it "most used" has no primary source, and a competing benchmark
  (Artificial Analysis Search Index) places Parallel Search marginally ahead of
  Exa on quality. No clear winner on "most used." Recommend downgrading to
  [DISPUTED] or softening to "a leading" unless a usage source surfaces.
- searched: "Exa MCP most used web search server coding agents 2026"
- source(s) found: https://parallel.ai/articles/best-web-search-mcp , https://glama.ai/mcp/servers/@exa-labs/exa-mcp-server/inspect

### Registry "17,000+ servers"
- Still literally true (count has grown, not shrunk), so not moved to Changed.
  Third-party analyses of the registry API disagree widely by counting unit
  (~16,967 latest-version servers in mid-July 2026; ~30,375 unique servers by a
  Sept 2026 analysis; ~99k server+version records). All are aggregator-derived; I
  could not reach registry.modelcontextprotocol.io directly to confirm. The "+"
  keeps the claim honest; flag only that the figure is drifting upward and its
  sourcing is weak. Keep `[REPORTED]`.
- searched: "official MCP registry number of servers 2026"

## No longer relevant
none found
```
