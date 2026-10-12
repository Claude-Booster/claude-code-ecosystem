# Patch: context-and-cost.md
verified_against: 2026-10-12
searches_run: 11
verdict: CHANGED

## Changed

### CLAUDE.md length rule is now in Anthropic's own docs
- was: `[REPORTED]` Community rule of thumb has hardened to **≤200 lines**, with detail moved into `.claude/rules/*.md` scoped by path glob so rules load only for relevant files.
- now: `[VERIFIED]` Anthropic's cost docs now say "Aim to keep CLAUDE.md under 200 lines by including only essentials," and recommend moving workflow-specific instructions into skills that load on demand. `[REPORTED]` Moving detail into path-glob-scoped `.claude/rules/*.md` files is still community practice.
- source: https://code.claude.com/docs/en/costs
- confidence: [VERIFIED]

### MCP context cost reason is out of date
- was: 4. Minimize MCP servers (the context argument and the cost argument are the same argument)
- now: 4. Minimize MCP servers. `[VERIFIED]` MCP tool definitions are now deferred by default, so only tool names and server instructions enter context until a tool is used. The per-server context cost is smaller than it was, but still not zero. CLI tools (`gh`, `aws`, `gcloud`) are still more context-efficient, and turning off unused servers through `/mcp` is still the guidance.
- source: https://code.claude.com/docs/en/costs
- confidence: [VERIFIED]

### Terse's kill-switch claim has only the vendor behind it
- was: | **Terse** | commercial | The one that *acts* — SIGSTOP/SIGTERM circuit breaker before the next API call |
- now: | **Terse** | commercial (macOS/Windows, trial then $4.99/mo) | `[VENDOR]` Says it pauses or ends the agent process at a spend ceiling before the next call. I found no independent check of this. |
- source: https://www.terseai.org/claude-code-cost-tracker
- confidence: [VENDOR]

### ccusage source count confirmed by the repo itself
- was: `[REPORTED]` now tracks 18+ agent CLIs.
- now: `[VERIFIED]` The README's "Supported Sources" table lists 18 tools, including Claude Code, Codex, OpenCode, Amp, Gemini CLI, Copilot CLI and Goose.
- source: https://github.com/ccusage/ccusage
- confidence: [VERIFIED]

## Status changes

### claude-mem now pushes a hosted, paid service
- was: | **claude-mem** | auto-captures sessions, compresses, injects into future sessions | `[REPORTED]` #1 trending GitHub Feb 2026 |
- now: `[VERIFIED]` Still active and not archived (v13.x). The installer now asks for a browser sign-in and offers a 30-day trial of the hosted "CMEM Pro" observer. Cloud sync to cmem.ai is available. The README endorses a third-party crypto token ($CMEM). For a privacy-sensitive repo, warn the user that the default setup may send session memory off-machine, and point to the local observer (`--provider host`). `[DISPUTED]` CMEM Pro price: $30/mo in the v13.14.0 release note, $20/mo or $199/yr on a third-party listing.
- source: https://github.com/thedotmack/claude-mem ; https://newreleases.io/project/github/thedotmack/claude-mem/release/v13.14.0
- confidence: [VERIFIED] (README contents); [DISPUTED] (price)

### ccusage repo moved to its own org
- was: **ccusage** | free npm CLI (ryoppippi)
- now: `[VERIFIED]` The canonical repo is now `github.com/ccusage/ccusage`. The npm package is still `ccusage`, and the license is still "MIT © @ryoppippi". The project is active and the recommendation stands; only the URL changed.
- source: https://github.com/ccusage/ccusage
- confidence: [VERIFIED]

## New entries

### First-party Claude apps gateway for per-user spend caps
- now: `[VERIFIED]` Anthropic documents a self-hosted **Claude apps gateway** with per-user usage attribution, OTLP token metrics and per-user spend limits on Bedrock, Vertex (Agent Platform) and Foundry. The same page lists LiteLLM as something "several large enterprises reported using" and says it is "unaffiliated with Anthropic and has not been audited for security."
- source: https://code.claude.com/docs/en/costs
- confidence: [VERIFIED]
- why include: the file names LiteLLM as *the* answer for team spend control. There is now a first-party option, and Anthropic's own docs add a security caveat about LiteLLM.

### `/usage` shows what is eating plan limits
- now: `[VERIFIED]` On Pro/Max/Team/Enterprise, `/usage` breaks down recent usage by skill, subagent, plugin and individual MCP server. It flags behaviors (long context, cache misses) above 10% of usage, and lists the heaviest `/loop` and scheduled tasks. It also has a prompt-cache line (hit share, misses, likely cause). `/insights` writes an HTML report on how you work.
- source: https://code.claude.com/docs/en/costs
- confidence: [VERIFIED]
- why include: it answers "where is my quota going" without a third-party monitor, which supports the file's "built-ins first" advice.

### 2026 limit changes users may mistake for a bug
- now: `[VENDOR]` Anthropic doubled Claude Code's 5-hour limits for Pro, Max, Team and seat-based Enterprise on 2026-05-06, and removed the peak-hours reduction for Pro/Max. `[REPORTED]` A temporary 50% weekly-limit boost ended 2026-09-14. Standard weekly limits were then set 25% above the pre-promotion baseline, which is about 17% below the boosted level.
- source: https://www.anthropic.com/news/higher-limits-spacex ; https://www.bleepingcomputer.com/news/artificial-intelligence/anthropic-is-cutting-claude-codes-current-weekly-limits-by-17-percent/
- confidence: [VENDOR] / [REPORTED]
- why include: the file's only advice for sudden limit problems is "check the CLI version (v2.1.89)." Since 2026-09-14, the policy change is a more likely cause.

## Could not verify

- **claude-token-lens**: searched for it by name, alone and with ccstatusline and cc-budget. No repo or listing found. It may be renamed, gone, or never indexed. Mark `[DISPUTED]` or drop it after a human checks. (cc-budget does exist at https://github.com/boyand/cc-budget. It gives pacing and threshold warnings only, no enforcement.)
- **Max 5× / Max 20× multipliers and limits shared with Cowork**: the support article I fetched (usage-limit-best-practices) covers the 5-hour and weekly windows but doesn't mention multipliers or sharing across products. The costs doc confirms sharing across Claude Code, chat and Cowork only for Team/Enterprise seats. Nothing contradicts the claim, but I couldn't find a primary source for the multipliers in this run.
- **v2.1.89 3–50× faster consumption (March 2026)**: I found no new evidence either way, and no source for it in this run.

## No longer relevant

- **"History worth knowing: … `ln -s AGENTS.md CLAUDE.md` … now redundant"**: the AGENTS.md fallback has been out since 2026-09-18. Cut it to one clause, and spend the space on the new `/config` → "Project instructions" mode setting, which controls whether to load CLAUDE.md only, AGENTS.md fallback, or both.

---

No changes dated after 2026-10-09 turned up. The official changelog ends at v2.1.296 (2026-10-09), and I found no limit or pricing news for 10–11 October. The changes above come from primary sources that the 2026-10-09 snapshot didn't reflect.

Sources: [code.claude.com/docs/en/costs](https://code.claude.com/docs/en/costs), [best-practices](https://code.claude.com/docs/en/best-practices), [changelog](https://code.claude.com/docs/en/changelog), [ccusage/ccusage](https://github.com/ccusage/ccusage), [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem), [terseai.org](https://www.terseai.org/claude-code-cost-tracker), [boyand/cc-budget](https://github.com/boyand/cc-budget), [Anthropic: higher limits](https://www.anthropic.com/news/higher-limits-spacex), [BleepingComputer](https://www.bleepingcomputer.com/news/artificial-intelligence/anthropic-is-cutting-claude-codes-current-weekly-limits-by-17-percent/), [newreleases.io claude-mem v13.14.0](https://newreleases.io/project/github/thedotmack/claude-mem/release/v13.14.0)
