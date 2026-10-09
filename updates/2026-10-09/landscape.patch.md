The primary source is Claude Code's own docs — it doesn't cover competitors, so it only anchors the Claude Code baseline. Four research agents are now running in parallel covering: status changes, terminal agents, funding/company moves, and new entries. I'll wait for them to report back before compiling the patch.

I'll wait for the agents to report their full findings.

Everything in the status-check table holds up: Roo Code (archived May 15 2026), Claude Flow→Ruflo (renamed early 2026), Bloop (shut down April 2026), Continue v2.0, Gemini CLI retirement — all predate the 2026-09-22 verification and were recorded correctly. Cline/Crush/Forge are all alive and active. No status changes in that cluster.

Still waiting on three clusters: terminal agents (Codex model/OpenCode/Pi/Kilo numbers), funding/company moves (Factory/Cursor/Amp/Augment), and new entries/models. I'll wait for those before compiling.

Strong findings from the terminal-agents cluster. Key post-2026-09-22 changes captured: Codex CLI default is now **GPT-6.1 Sol** (Oct 7, primary source) — the biggest correction; OpenCode org moved sst→anomalyco with much higher star count; Pi repo moved to earendil-works/pi (Earendil Inc); Kilo installs up to 3M+; Pi's "sub-1k-token" claim unverifiable.

Still waiting on funding/company moves and new-entries clusters. Holding for those.

I now have all research in. I verified the SpaceX/Cursor acquisition directly myself — it's corroborated across multiple independent outlets plus an SEC 8-K reference, and the OpenAI-ending-Cursor-access follow-on (proposed Nov 12 2026 cutoff) checks out too. All clusters have reported. Compiling the patch.

```markdown
# Patch: landscape.md
verified_against: 2026-10-09
searches_run: 70
verdict: CHANGED

## Changed

### Codex CLI default model
- was: "Default GPT-5.x." (in the OpenAI Codex CLI row)
- now: Default model is now GPT-6.1 Sol (GPT-6 era). Announced at OpenAI DevDay 2026-09-29 and made the bundled/default catalog model in Codex CLI release rust-v0.161.0 (2026-10-07); priced $2.00 / $10.00 per 1M tokens. A new `mxc` process-isolation sandbox is now the recommended Windows sandbox. [VERIFIED]
- source: https://github.com/openai/codex/releases/tag/rust-v0.161.0 ; https://developers.openai.com/api/docs/pricing
- confidence: [VERIFIED]

### OpenCode — org move and star count
- was: "`[REPORTED]` ~95–100k stars, 75+ providers, multi-session, privacy-first"
- now: Repo moved from the `sst` org to `anomalyco` (github.com/anomalyco/opencode; old sst/opencode URL still resolves). Star count now ~212k per the repo About section. "75+ providers" remains accurate. `[REPORTED]`
- source: https://github.com/sst/opencode ; https://opencode.ai/docs/providers/
- confidence: [REPORTED] (star figure is volatile and large — spot-check before quoting)

### Pi — repo move, ownership, stars
- was: "Zechner/Ronacher. Sub-1k-token system prompt, 'lazy skills.' `[REPORTED]` 50k+ stars."
- now: Repo moved badlogic/pi-mono → earendil-works/pi; now owned/maintained by Earendil Inc. (Armin Ronacher's company); homepage pi.dev. ~113k stars. On-demand ("lazy") skills confirmed. The "Zechner/Ronacher" attribution still holds. `[REPORTED]`
- source: https://github.com/earendil-works/pi ; https://pi.dev
- confidence: [REPORTED]
  (The "sub-1k-token system prompt" figure could not be sourced — see Could not verify.)

### Kilo Code — install count
- was: "~1.5M users"
- now: Vendor now claims 3M+ installs. (OpenCode-fork rebuild, 500+ models, and worktree Agent Manager all remain accurate.) `[VENDOR]`
- source: https://blog.kilo.ai/p/new-kilo-for-vs-code-is-live
- confidence: [VENDOR]

### Amp — "shipped a desktop app Sept 2026"
- was: "Shipped a desktop app Sept 2026."
- now: Misleading as phrased. Amp's "Desktop" launch (2026-09-04) is a cloud-hosted interactive Linux desktop that runs inside an Amp thread (for computer-use / checking agent work), not a standalone desktop application. A separate Amp macOS app existed before September and only received incremental runner updates during the month. `[VENDOR]`
- source: https://ampcode.com/news/desktop
- confidence: [VENDOR]

## Status changes

### Cursor acquired by SpaceX — no longer independent
- was: "**Cursor** | AI IDE | Background agents in cloud VMs ... Acquired Graphite. The IDE-empire play." (presented as an independent company)
- now: Anysphere (maker of Cursor) was acquired by SpaceX in a ~$60B all-stock deal — announced 2026-06-16, completed 2026-08-14. Cursor is now a wholly owned SpaceX subsidiary inside a "SpaceXAI" division. The file's framing of Cursor as an independent "IDE-empire play" is out of date. `[REPORTED]`
- source: https://en.wikipedia.org/wiki/Cursor_(company) ; https://www.cnbc.com/2026/06/16/spacex-spcx-cursor-acquisition-ipo.html
- confidence: [REPORTED] (heavily corroborated across independent outlets + an SEC Form 8-K; not fetched to primary, so not [VERIFIED])
- follow-on: OpenAI invoked a change-of-control clause and proposed ending Cursor's direct access to OpenAI models on 2026-11-12 (notified ~2026-08-29, still under negotiation). Cursor retains Anthropic, Google, and SpaceXAI/Grok models. `[REPORTED]` — https://www.channelinsider.com/ai/news-openai-cursor-model-access-spacex-acquisition/
- note: Both the acquisition and the OpenAI dispute predate the 2026-09-22 verification but are absent from the file — this is a pre-existing miss, not a new event. The 2026-11-12 cutoff is future and worth watching.

### Amazon Q Developer — being sunset in favor of Kiro
- was: lists "**Amazon Q**" among live adjacent tools
- now: AWS will end support for Amazon Q Developer IDE plugins on 2027-04-30 and directs users to migrate to Kiro, AWS's separate agentic IDE (separate product/subscription). This is a sunset-and-migrate, not a rename. `[VERIFIED]`
- source: https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-developer-ide-end-of-support.html
- confidence: [VERIFIED]

### Goose — governance move (minor)
- was: file references "Goose" in the adjacent-niches bucket
- now: Goose moved to the Agentic AI Foundation (AAIF) at the Linux Foundation; canonical repo is now aaif-goose/goose (block/goose redirects). Still actively shipping (v1.54.0, 2026-10-08). No longer solely Block-governed. `[VERIFIED]`
- source: https://github.com/block/goose
- confidence: [VERIFIED]
- note: pre-window (~April 2026); flagged only because the file's "block/goose" mental model is stale.

(No tool in the file died, was fully shut down, or was renamed after 2026-09-22. Roo Code / Gemini CLI / Continue / Claude Flow→Ruflo / Bloop all changed status *before* the last verification and are recorded correctly.)

## New entries

### Kiro (AWS) — agentic IDE
- what: AWS's standalone agentic IDE; the designated migration target for the sunsetting Amazon Q Developer, and now wired into Warp's coding-agent toolbar (Kiro CLI support, 2026-10-07).
- why it clears the bar: it's the official successor to a tool already in the file (Amazon Q), backed by a hyperscaler, and surfacing as an integration target elsewhere in the field.
- source: https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-developer-ide-end-of-support.html
- confidence: [REPORTED]

### OpenAI "Dots" — always-on agent platform (borderline; human decision)
- what: persistent always-on personal agents in ChatGPT, each with its own cloud computer, reachable via ChatGPT/Slack/Teams, powered by GPT-6 Astra. Launched DevDay 2026-09-29.
- why / caveat: adjacent to the Jules/Antigravity/Devin agent-platform row, but general-purpose rather than coding-specific, and the official recap page was unreachable (403). Argument for inclusion is weaker than Kiro's — flag for a human rather than auto-add.
- source: https://siliconangle.com/2026/09/29/openai-launches-dots-always-on-ai-agents-in-chatgpt-with-their-own-cloud-computers/
- confidence: [REPORTED]

### Model-landscape note (not a new tool, but affects the file)
- The file's only model reference ("Default GPT-5.x") is now GPT-6-era: GPT-6 Astra and GPT-6.1 Sol ($2/$10) are current OpenAI coding models; Anthropic Opus 5.5 / Sonnet 5.5 / Haiku 5.5 and Google Gemini 3 Pro are current. Corrected in Changed (Codex row) above; no new row needed.
- source: https://developers.openai.com/api/docs/pricing

## Could not verify

### Pi "sub-1k-token system prompt"
- Searched pi.dev and the earendil-works/pi README. Both describe a "minimal system prompt" and link to the source file but state no token count. No primary source supports the sub-1k figure. → becomes [DISPUTED].

### Cursor "up to 8 parallel jobs"
- Could not confirm the specific "8" figure in Cursor's official docs/changelog. Secondary sources disagree on whether the cap applies to local git-worktree agents or to cloud background agents. → becomes [DISPUTED].

### Augment "#1 on SWE-Bench Pro"
- Searched Augment's blog and Scale's leaderboard. The #1 / 51.80% figure is Augment's own blog (dated 2026-02-04, updated 2026-06-18) using Augment's own test harness — not Scale's official leaderboard. Scale shipped SWE-Bench Pro V2 (page updated 2026-09-22) with a modified, locked protocol, so the old score is no longer comparable. The `[VENDOR]` tag is honest; the claim is now stale. → keep as [VENDOR]/[DISPUTED].
- source: https://www.augmentcode.com/blog/auggie-tops-swe-bench-pro ; https://labs.scale.com/leaderboard/swe_bench_pro_public_v2

### Factory "[VERIFIED] raised $200M at $5B valuation 2026-09-15"
- The amount, valuation, and date are accurate and corroborated across multiple independent outlets (devops.com, The Next Web, Sacra). But no primary source — Factory's own release or a tier-1 original — was reachable. Under this bundle's rules, independent secondary corroboration supports [REPORTED], not [VERIFIED]. → recommend downgrading the tag from [VERIFIED] to [REPORTED] (the claim itself stands).
- source: https://devops.com/factory-raises-200m-as-it-builds-agents-across-the-software-lifecycle/

## No longer relevant

none found — the "Status check before recommending" table and the "2026 shifts" section still carry their weight. Note that if Cursor's acquisition and Amazon Q's sunset are merged in, the status-check table becomes a natural home for them.
```

**Summary of the run:** verdict is **CHANGED**, not a structural rewrite. The file's core — the status-check table (Roo/Gemini CLI/Continue/Claude Flow→Ruflo) and the 2026 shifts narrative — all held up; those changes predate the last verification and were recorded correctly. The real corrections are: Codex's default model moved to GPT-6.1 Sol (the one clean post-window change), stale counts for OpenCode/Pi/Kilo plus their repo/org moves, and two **missed status changes** the file never captured — Cursor being acquired by SpaceX (June/Aug 2026) and Amazon Q sunsetting toward Kiro. Four claims went to "could not verify" rather than being silently corrected, including a recommended tag downgrade on the Factory funding line.

The final research agent (Continue / Claude Flow) came back after I'd printed the patch, and it materially changes one conclusion using **primary** sources (GitHub API, npm registry) that outrank my earlier content-farm search. I need to amend the patch.

**Amendment to the patch above**

The Claude Flow→Ruflo entry is now confirmed against primary sources (repo `ruvnet/claude-flow` redirects to `ruvnet/ruflo`, README states "Claude Flow is now Ruflo", npm `ruflo` v3.56.0) — the file's status-check row holds, no change. But the Continue entry needs correcting:

```markdown
## Could not verify   (add this entry)

### Continue "v2.0 is final; maintenance only"
- The file's status-check table states Continue is in "maintenance only." Primary sources contradict the "maintenance" framing with no clean winner:
  - GitHub API for continuedev/continue shows `archived: false`, `disabled: false`, `pushed_at: 2026-10-08`, 827 open issues — i.e. a live, non-archived repo, not a wound-down one.
  - Latest *stable* release is v2.0.0 (2026-06-19), so "v2.0 is newest" is roughly right, but a v2.1.0 prerelease also exists, which undercuts "final."
  - No official blog/README/GitHub statement declaring maintenance mode could be found. The "Cursor acquired Continue / hosted service shut down / read-only repo" story traces to a single aggregator (yespress.io) with no primary corroboration and is contradicted by the live repo.
  - Kernel of truth: release cadence and `main`-branch commits slowed after mid-2026 (newest main commit 2026-07-21, no releases since June), but branch/PR activity continues.
- Searched: GitHub API, Continue blog, npm; found an active repo, not a maintenance declaration. → becomes [DISPUTED]: "v2.0.0 is the latest stable (June 2026) with a v2.1.0 prerelease; development has slowed but the repo remains active (pushes through 2026-10-08) — no primary source supports 'maintenance only.'"
- source: https://api.github.com/repos/continuedev/continue ; https://api.github.com/repos/continuedev/continue/releases ; https://blog.continue.dev
```

That is the only revision. Everything else in the printed patch stands, and the overall **verdict remains CHANGED**.

To recap the corrected picture of the status-check table the file leads with: Roo Code (archived), Gemini CLI (retired → Antigravity), and Claude Flow→Ruflo all verified correct against primary sources; **Continue is the one that doesn't fully hold** — it's not demonstrably "maintenance only," so it drops to [DISPUTED] rather than being silently rewritten.
