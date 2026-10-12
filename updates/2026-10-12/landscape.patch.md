# Patch: landscape.md
verified_against: 2026-10-12
searches_run: 14
verdict: CHANGED

## Changed

### Codex CLI default model
- was: `Default GPT-5.x.`
- now: `[VERIFIED]` By default Codex CLI uses its "recommended model", currently **gpt-6.1-sol** (also listed: gpt-6-luna, gpt-6-astra). gpt-5.5 leaves Codex for ChatGPT sign-in on 2026-10-14. gpt-5.4 and gpt-5.4-mini were retired 2026-08-31.
- source: https://learn.chatgpt.com/docs/models (redirected from https://developers.openai.com/codex/models)
- confidence: [VERIFIED]

### OpenCode star count
- was: `[REPORTED] ~95–100k stars, 75+ providers, multi-session, privacy-first`
- now: `[VERIFIED]` ~213k GitHub stars as of 2026-10-12. The repo moved from sst/opencode to anomalyco/opencode, and the old path redirects. The rest of the line stays as written.
- source: https://api.github.com/repos/anomalyco/opencode
- confidence: [VERIFIED]

### Pi star count and repo location
- was: `[REPORTED] 50k+ stars.`
- now: `[VERIFIED]` ~114k GitHub stars as of 2026-10-12. The repo is now earendil-works/pi, and badlogic/pi-mono redirects there.
- source: https://api.github.com/repos/earendil-works/pi
- confidence: [VERIFIED]

### Kilo Code user count
- was: `~1.5M users`
- now: `[VENDOR]` "more than 3 million developers" across VS Code, JetBrains, web and CLI, from the acquisition press release of 2026-07-15. GitHub shows ~27.6k stars on Kilo-Org/kilocode.
- source: https://sdtimes.com/agentic-engineering/anaconda-acquires-kilo-code-to-power-the-trillion-token-enterprise/
- confidence: [VENDOR]

### Amp desktop app and ownership
- was: `| **Amp** | agentic (Sourcegraph) | … Shipped a desktop app Sept 2026. |`
- now: `[VENDOR]` Amp is an independent company: "Amp Frontier Corporation", spun out of Sourcegraph in Dec 2025, with the npm package renamed `@ampcode/cli` on 2026-05-14. The macOS (and iOS) app was announced on **2026-08-28**, and from 2026-09-24 the Mac app runs local threads without a terminal. On **2026-10-10** Amp announced "Use your Claude Pro/Max plan in Amp", free and available to everyone.
- source: https://ampcode.com/chronicle (entries /news/amp-on-ios-and-macos, /news/the-mac-app-is-your-runner, /news/use-your-claude-plan)
- confidence: [VENDOR]

### Continue final version
- was: `| **Continue** | v2.0 is final | maintenance only |`
- now: `[VERIFIED]` The last release is **v2.1.0** (2026-06-19), published the same day as v2.0.0. The last main-branch commit, on 2026-07-21, removed the docs sign-in link because the login flow was retired. Maintenance-only still holds.
- source: https://api.github.com/repos/continuedev/continue/releases
- confidence: [VERIFIED]

### Gemini CLI successor naming
- was: `enterprise (Code Assist) only; Antigravity is the successor platform`
- now: `[VERIFIED]` The named successor is **Antigravity CLI**, part of Antigravity 2.0 and announced at I/O 2026. Gemini CLI still serves Code Assist Standard/Enterprise, Google Cloud, and paid Gemini API key users. The open-source google-gemini/gemini-cli repo is not archived and still ships nightlies (v0.65.0-nightly, 2026-10-12).
- source: https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/ ; https://api.github.com/repos/google-gemini/gemini-cli/releases
- confidence: [VERIFIED]

### Cursor parallel-agent limit (now has a source, tag unchanged)
- was: `[REPORTED] up to 8 parallel jobs`
- now: `[REPORTED]` A Cursor staff reply on the forum says the concurrent Cloud Agents limit is 8 on Pro. Cursor's own docs don't confirm it.
- source: https://forum.cursor.com/t/cloud-agent-reaches-creation-limit-when-theres-none-created/154204
- confidence: [REPORTED]

## Status changes

### Cursor acquired by SpaceX
- was: `| **Cursor** | AI IDE | … Acquired Graphite. The IDE-empire play. |` (no mention of a change of ownership)
- now: `[REPORTED]` SpaceX exercised its option on 2026-06-16, an all-stock deal for Anysphere at about $60B. The deal closed **2026-08-14**, and Cursor is now a wholly owned subsidiary being folded into SpaceXAI. The 2026 shifts paragraph "Consolidation and capital" should list this, and "The IDE-empire play" framing should be revisited.
- source: https://www.cnbc.com/2026/04/21/spacex-says-it-can-buy-cursor-later-this-year-for-60-billion-or-pay-10-billion-for-our-work-together.html ; https://news.bloomberglaw.com/mergers-and-acquisitions/spacex-completes-its-60-billion-cursor-acquisition
- confidence: [REPORTED]. The SEC 8-K is cited on Wikipedia, but I did not fetch it. Fetching it would justify [VERIFIED].

### Kilo Code acquired by Anaconda
- was: `[REPORTED] the Cline→Roo→Kilo fork tree's resolution point.` / "ended with Kilo as the live branch"
- now: `[REPORTED]` Anaconda acquired Kilo Code, announced **2026-07-15**, terms undisclosed. Kilo's products and plans are unchanged for now. The release does not formally commit to keeping Kilo open source. Kilo is still the live branch of the fork tree, but it is now owned by Anaconda. Add it to "Consolidation and capital".
- source: https://sdtimes.com/agentic-engineering/anaconda-acquires-kilo-code-to-power-the-trillion-token-enterprise/ ; https://devops.com/anaconda-acquires-kilo-code/
- confidence: [REPORTED]

### Aider is effectively dormant
- was: `| **Aider** | OSS terminal | Git-native pair programmer, model-agnostic. Still the cleanest mental model for small changes. |` and "Want minimal surface area → Aider or Pi"
- now: `[VERIFIED]` Not archived, but the last GitHub release is v0.86.0 (2025-08-09). The last commit, on 2026-05-22, only added Claude model names, and there has been no activity since. Tag it as maintenance or dormant before recommending it. Pi is the active pick for minimal surface area.
- source: https://api.github.com/repos/Aider-AI/aider/releases ; https://api.github.com/repos/Aider-AI/aider/commits
- confidence: [VERIFIED]

### Goose moved org
- was: `**Goose**` (adjacent niches; implicitly block/goose)
- now: `[VERIFIED]` The repo is now **aaif-goose/goose**, and block/goose redirects there. It is active, with ~55k stars.
- source: https://api.github.com/repos/aaif-goose/goose
- confidence: [VERIFIED]

### Forge renamed
- was: `**Forge**`
- now: `[VERIFIED]` The repo is now **tailcallhq/forgecode** ("ForgeCode"), and antinomyhq/forge redirects there. It is active.
- source: https://api.github.com/repos/tailcallhq/forgecode
- confidence: [VERIFIED]

### Confirmed, no change
- Roo Code: the GitHub repo is archived (`archived: true`, last push 2026-05-15). https://api.github.com/repos/RooCodeInc/Roo-Code
- Claude Flow → Ruflo: ruvnet/claude-flow redirects to ruvnet/ruflo. https://api.github.com/repos/ruvnet/ruflo

## New entries

### Antigravity CLI (Google)
- now: `[VERIFIED]` Antigravity CLI is Google's terminal agent, written in Go with background multi-agent orchestration. It replaces Gemini CLI for individual and AI Pro/Ultra users. Reported as not open source.
- source: https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/
- confidence: [VERIFIED] for the transition. [REPORTED] for "not open source" (https://letsdatascience.com/news/google-replaces-gemini-cli-with-antigravity-cli-574b2056).
- why: The file calls "Gemini CLI/Antigravity" a serious terminal entrant but never names the actual CLI product users are moved to.

### Muse Code (Meta)
- now: `[REPORTED]` Meta's first terminal coding agent, released in beta in Aug 2026 on Muse Spark 1.2. It runs parallel subagents in git worktrees and keeps a local event log. Pay-as-you-go, about $1.25 / $4.25 per M tokens. `[VENDOR]` Terminal-Bench 2.1: 82.9%, against 86.7% for Claude Code on Opus 5.
- source: https://decrypt.co/375001/muse-code-meta-ai-coding-agent-claude-code-and-codex ; https://www.verdict.co.uk/meta-releases-muse-code-ai/
- confidence: [REPORTED]
- why: It is a direct new frontier-lab entrant in the terminal category the file calls "the battleground". It predates 2026-10-09 but was missed.

### Grok Build (xAI / SpaceXAI)
- now: `[VENDOR]` A terminal coding agent. Beta in May 2026, open-sourced under Apache-2.0 on 2026-07-15 (xai-org/grok-build), with support for skills, plugins, hooks and MCP. `[REPORTED]` The beta uploaded repositories to Google Cloud. Upload was disabled by default and the uploaded data deleted on 2026-07-12.
- source: https://x.ai/blog/grok-build-open-source ; https://www.gigazine.net/gsc_news/en/20260716-grok-build-open-source
- confidence: [VENDOR] / [REPORTED]
- why: It is an open-source terminal agent from a frontier lab, now under the same SpaceX parent as Cursor. The privacy incident matters to anyone recommending it.

## Could not verify

- **Amp "Use your Claude Pro/Max plan" (2026-10-10) and Anthropic's 2026-04-04 policy.** The policy blocks Pro/Max subscriptions from third-party agents (see evidence-ledger.md). I found only Amp's chronicle summary, and the article URL I guessed (/news/use-your-claude-plan-in-amp) returned 404. I found no Anthropic-side source saying whether this is sanctioned. Needs a human check before either file states it as fact.
- **Codex CLI "native Windows support and its own sandbox as of March 2026" `[VERIFIED]`.** Not re-checked this run. No contradicting evidence found.
- **Augment "#1 on SWE-Bench Pro" `[VENDOR]`.** Still only Augment's own post (https://augmentcode.com/blog/auggie-tops-swe-bench-pro, April 2026: 51.80% on Opus 4.5). Morph reports a conflicting Claude Code figure on the same benchmark (~34.8% vs Augment's 49.75%) and a different task count (731 vs 1,865). Keep `[VENDOR]`. Do not upgrade it.
- **Factory $5B `[VERIFIED]`.** The $200M at $5B round (Sept 2026) is consistent across secondary sources. The lead investor conflicts (Sequoia vs Khosla), and an unconfirmed Jul 2026 $4B extension circulates. Neither is in the file, so the claim is unchanged. I did not re-fetch a primary source this run.
- **Muse Code launch date.** Sources give Aug 5 and Aug 12, 2026.

## No longer relevant

- **The "Gemini CLI" row in The field.** It duplicates the status-table entry, and its differentiator (1M context) now belongs to Antigravity/Code Assist. Delete the row and fold the context note into the Antigravity row.
