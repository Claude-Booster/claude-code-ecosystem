# Patch: evidence-ledger.md
verified_against: 2026-10-12
searches_run: 10
verdict: CHANGED

## Changed

### Known fabrications: default-model row is out of date
- was: `| "Opus 4.8 is the default model" | Stale. Defaults are plan-dependent; Opus 5 or Sonnet 5 depending on tier. |`
- now: `| "Opus 4.8 is the default model" (or "Opus 5 is the default") | Stale. [VERIFIED] Pro, Max, Team, Enterprise, the Anthropic API, Claude Platform on AWS, Bedrock and Google Cloud's Agent Platform all default to Opus 5.5 (Claude Code v2.1.280+). Only Microsoft Foundry is different: it defaults to Sonnet 4.5. |`
- source: https://code.claude.com/docs/en/model-config
- confidence: [VERIFIED]

### Known fabrications: current-Sonnet row is out of date
- was: `| "Sonnet 4.6 is the current Sonnet" | Stale. Sonnet 5 since 2026-06-30. |`
- now: `| "Sonnet 4.6 / Sonnet 5 is the current Sonnet" | Stale. [VERIFIED] Sonnet 5.5 since 2026-09-28. The `sonnet` alias has resolved to it on the Anthropic API since v2.1.284. Sonnet 5 is legacy. On third-party providers `sonnet` still resolves to older models: Sonnet 4.6 on Claude Platform on AWS, Sonnet 4.5 on Bedrock, Agent Platform and Foundry. |`
- source: https://code.claude.com/docs/en/model-config ; https://www.anthropic.com/news (featured post "Introducing Claude Sonnet 5.5", Sep 28, 2026)
- confidence: [VERIFIED]

### Verified primary sources: model releases and pricing
- was: `- Opus 5 release 2026-07-24 at $5/$25; Sonnet 5 release 2026-06-30 at $2/$10, made permanent 2026-08-10`
- now: `- [VERIFIED] Current lineup (API $/MTok input/output):`
  - `Opus 5.5 (2026-09-22): $4/$20`
  - `Sonnet 5.5 (2026-09-28): $2/$10`
  - `Haiku 5.5 (2026-10-07): $0.10/$0.50 for prompts ≤100K tokens, $0.50/$2.50 above that`
  - `Fable 5.1: $10/$50, never the default on any plan`
  - `Legacy: Opus 5 (released 2026-07-24, $5/$25), Sonnet 5 (released 2026-06-30, $2/$10) and Haiku 4.5 ($1/$5).`
  - `Minimum Claude Code versions: v2.1.280 for Opus 5.5, v2.1.284 for Sonnet 5.5, v2.1.293 for Haiku 5.5.`
- source: https://claude.com/pricing ; https://code.claude.com/docs/en/model-config ; https://www.anthropic.com/news (featured posts dated Sep 22, Sep 28 and Oct 7, 2026)
- confidence: [VERIFIED]

### Verified primary sources: enterprise paths now include a first-party gateway
- was: `- Supported enterprise paths: Bedrock, Vertex AI, Claude Platform on AWS, Microsoft Foundry, LLM gateways`
- now: `- [VERIFIED] Supported enterprise paths: Bedrock, Google Cloud's Agent Platform (formerly Vertex AI in the docs), Claude Platform on AWS, Microsoft Foundry, and a self-hosted first-party "Claude apps gateway" (per-user attribution, OTLP metrics, per-user spend limits). Third-party LLM gateways are also supported. The docs say LiteLLM "is unaffiliated with Anthropic and has not been audited for security."`
- source: https://code.claude.com/docs/en/costs ; https://code.claude.com/docs/en/model-config
- confidence: [VERIFIED]

### Disputed figures: superpowers star count has a new, higher value
- was: `| `obra/superpowers` stars | 94k / 232k (v6.0 release notes) / ~288k | Say "one of the largest community skill collections." Don't pick a number. |`
- now: `| `obra/superpowers` stars | [DISPUTED] 94k / 232k (v6.0 release notes) / ~288k / 298.0k (repo page, 2026-10-12) | Say "one of the largest community skill collections." Don't pick a number. |`
- source: https://github.com/obra/superpowers
- confidence: [DISPUTED]

## Status changes

### Roo Code: archive date confirmed, successors named
- was: `Roo Code archived (May 2026)`
- now: `[VERIFIED] Roo Code shut down and the repo was archived 2026-05-15. The README points users to ZooCode (a community fork) and Cline.`
- source: https://github.com/RooCodeInc/Roo-Code
- confidence: [VERIFIED]

### Planned Agent SDK billing change was paused and replaced by monthly API credits
- was: (absent; the file lists only the 2026-04-04 third-party-framework block)
- now: `[VERIFIED] A separate programmatic-usage budget was announced for 2026-06-15, then paused on 2026-06-15 ("For now, nothing has changed"). On 2026-10-07 Anthropic began rolling out monthly API credits instead, covering the Agent SDK, claude -p, the API and Managed Agents:`
  - `Amounts: Max 5x $100, Max 20x $200, Team Standard $20/seat, Team Premium $100/seat (Team pooled, capped at $500).`
  - `Not eligible: Free, Pro and Enterprise.`
  - `Usage only draws on the credits when run with an API key from a linked Console org. Signed-in plan usage still counts against plan limits.`
  - `The credits don't cover the GitHub Action, IDE extension or desktop app, even with -p.`
- source: https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan ; https://support.claude.com/en/articles/17154008-monthly-api-credits-for-max-and-team-plans
- confidence: [VERIFIED]

## New entries

### Dated status change: the 5.5 model generation
- now: `[VERIFIED] Opus 5.5 (2026-09-22, alias moved in v2.1.280), Sonnet 5.5 (2026-09-28, v2.1.284) and Haiku 5.5 (2026-10-07, v2.1.293) replaced Opus 5, Sonnet 5 and Haiku 4.5 as the alias targets on the Anthropic API.`
- source: https://code.claude.com/docs/en/model-config (Version history) ; https://www.anthropic.com/news
- confidence: [VERIFIED]
- why: the "Dated status changes" line is where readers check for recent breakpoints. A full model generation turned over within three weeks of the snapshot, and nothing in the file reflects it.

### Known fabrication candidate: "Opus 5.5 is 40% cheaper"
- now: `[VENDOR] Anthropic says Opus 5.5 "costs 40% less to run than Opus 5," which is a measure of running cost. The list-price cut is 20% ($5/$25 → $4/$20) [VERIFIED]. Aggregator blogs mix up the two figures.`
- source: https://www.anthropic.com/news ; https://claude.com/pricing
- confidence: [VENDOR] (40%) / [VERIFIED] (list price)
- why: this is the kind of vendor claim the ledger exists to separate from measurement, and it is already being repeated as a price figure (for example techjacksolutions headlines).

## Could not verify

### 2026-04-04 policy blocking Pro/Max subscriptions in third-party agent frameworks
- The 2026-04-04 block is well reported: OpenClaw coverage, plus a quote from Boris Cherny via letsdatascience and how2shout. But the support article's 2026-10-07 update now says: "You can still use the Claude Agent SDK, `claude -p`, and third-party apps with your subscription limits." The Register (2026-05-14) also said third-party tools would draw from a programmatic pool, and that plan was later paused.
- I found no primary Anthropic text that says whether OAuth-token use in third-party *harnesses* such as OpenClaw is still blocked, or whether "third-party apps" means only apps built on the Agent SDK.
- Searched: "Claude Code third-party harness subscription policy OpenClaw Pro Max 2026"; "programmatic usage credit Claude plan Agent SDK" (filtered to support.claude.com, anthropic.com, claude.com, code.claude.com); fetched both support articles and The Register piece.
- Recommend marking `[DISPUTED]` until someone checks current Anthropic ToS or Claude Code legal docs.

### v2.1.89 rate-limit consumption regression (March 2026)
- I fetched the first ~100K characters of the official changelog (it runs through v2.1.296, 2026-10-09). The v2.1.89 entry was outside that range, and no search turned up a primary source in this run. Nothing contradicts the claim, but it has no source as of this run.

### v2.1.277 AGENTS.md support (2026-09-18)
- The v2.1.277 entry was outside the changelog range I fetched. Nearby versions confirm AGENTS.md handling exists: v2.1.290 fixes AGENTS.md attachment for subdirectories. I didn't confirm the exact version and date.

## No longer relevant

- `Sonnet 5 ... made permanent 2026-08-10`: delete the "made permanent" clause. Sonnet 5 is legacy, and Sonnet 5.5 launched at the same $2/$10, so the cancelled price increase no longer affects any decision.

---

Notes for the human reviewer (not part of the patch):
- Several claims held up and need no change: the cost figures (~$13/dev/active-day, $150–250/month, quoted verbatim in the costs doc), Factory's $200M at $5B on 2026-09-15 (Dow Jones via Morningstar), and CVE-2025-59536 (GitHub advisory, High).
- One aggregator, Signalbase, claims Factory was acquired by "Donum" on 2026-09-15. Dow Jones contradicts it, so I left it out.
- I found nothing dated 2026-10-10 or 2026-10-11. Anthropic's newest post is 2026-10-08, a Usage Policy update effective 2026-11-12 that doesn't cover coding-agent terms. The changelog's newest entry is v2.1.296 from 2026-10-09.
- `updates/2026-10-12/evidence-ledger.patch.md` was 0 bytes at the start of this run. I didn't write to it; this output is meant to be captured from stdout.

Sources: [model-config](https://code.claude.com/docs/en/model-config), [pricing](https://claude.com/pricing), [Anthropic news](https://www.anthropic.com/news), [costs](https://code.claude.com/docs/en/costs), [changelog](https://code.claude.com/docs/en/changelog), [Agent SDK with your plan](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan), [Monthly API credits](https://support.claude.com/en/articles/17154008-monthly-api-credits-for-max-and-team-plans), [The Register](https://www.theregister.com/ai-ml/2026/05/14/anthropic-tosses-agents-into-the-api-billing-pool/5240748), [Roo-Code](https://github.com/RooCodeInc/Roo-Code), [superpowers](https://github.com/obra/superpowers), [Morningstar/Dow Jones on Factory](https://morningstar.com/news/dow-jones/202609155753/ai-software-developer-factory-gets-200-million-in-financing-round), [GitHub advisories](https://github.com/advisories?query=claude-code+CVE-2025-59536), [letsdatascience](https://letsdatascience.com/news/anthropic-restricts-claude-subscriptions-from-openclaw-acces-2ee184b2), [techjacksolutions](https://techjacksolutions.com/ai-brief/anthropic-cuts-claude-opus-5-5-api-costs-40-percent-launches/), [Android Authority](https://www.androidauthority.com/claude-haiku-5-5-launched-3720550/)
