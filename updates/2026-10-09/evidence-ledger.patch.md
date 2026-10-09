I have enough to produce the patch. The CVEs found all predate the verification date, and no new tool-status change is reliably sourced. The decisive finding is a new 5.5 model generation and a default-model change, confirmed by primary sources.

```markdown
# Patch: evidence-ledger.md
verified_against: 2026-10-09
searches_run: 7
verdict: CHANGED

## Changed

### Default model is now Opus 5.5, not "Opus 5 or Sonnet 5"
- was: `| "Opus 4.8 is the default model" | Stale. Defaults are plan-dependent; Opus 5 or Sonnet 5 depending on tier. |`
- now: `| "Opus 4.8 is the default model" | Stale. The default is Opus 5.5 on Pro, Max, Team, Enterprise, the Anthropic API, Claude Platform on AWS, Amazon Bedrock, and Google Cloud; Microsoft Foundry defaults to Sonnet 4.5. [VERIFIED] |`
- source: https://code.claude.com/docs/en/model-config
- confidence: [VERIFIED]

### Current Sonnet is 5.5, not 5
- was: `| "Sonnet 4.6 is the current Sonnet" | Stale. Sonnet 5 since 2026-06-30. |`
- now: `| "Sonnet 4.6 is the current Sonnet" | Stale. Sonnet 5.5 is the current Sonnet; the `sonnet` alias resolves to Sonnet 5.5 on the Anthropic API. [VERIFIED] |`
- source: https://code.claude.com/docs/en/model-config
- confidence: [VERIFIED]

### Model lineup / defaults bullet predates the 5.5 generation
- was: `- Model lineup, pricing, and plan-dependent defaults (Claude Code model-config docs)`
- now: `- Model lineup, pricing, and plan-dependent defaults (Claude Code model-config docs); current lineup led by Opus 5.5 (default), Sonnet 5.5, Haiku 5.5, and Fable 5.1 as the most capable widely released model [VERIFIED]`
- source: https://code.claude.com/docs/en/model-config
- confidence: [VERIFIED]

## Status changes

The ledger's verification date (2026-09-22) is the exact day Opus 5.5 launched, so
the whole 5.5 generation postdates it. These are additions rather than deaths, so
they appear under New entries. No tool in the file was found archived, renamed,
acquired, or broken since 2026-09-22.

A SpaceX/Anysphere (Cursor) acquisition circulates on aggregator blogs with
conflicting valuations ($3.4B vs $60B) and no primary confirmation — treated as
unverified, not reported. See Could not verify.

## New entries

### Claude Opus 5.5 — the current default model
- now: Opus 5.5 (`claude-opus-5-5`) released 2026-09-22, $4/$20 per MTok (cache read $0.20), 1M context / 128K output; default effort `medium`, thinking cannot be disabled. Now the default across Pro/Max/Team/Enterprise/API. [VERIFIED]
- source: https://platform.claude.com/docs/en/about-claude/pricing ; https://code.claude.com/docs/en/model-config
- confidence: [VERIFIED]
- why it clears the bar: it is the new default model and ~20% cheaper than Opus 5; any current pricing/default statement is wrong without it.

### Claude Sonnet 5.5 — the current Sonnet
- now: Sonnet 5.5 (`claude-sonnet-5-5`), $2/$10 per MTok (cache read $0.10), 1M context / 128K output. Same per-token price as Sonnet 5; `sonnet` alias on the Anthropic API now resolves here. [VERIFIED] (pricing/lineup); release date ~2026-09-28 [REPORTED]
- source: https://platform.claude.com/docs/en/about-claude/pricing ; https://code.claude.com/docs/en/model-config
- confidence: [VERIFIED]
- why it clears the bar: replaces Sonnet 5 as the current Sonnet; the "current Sonnet" fabrication row is about exactly this question.

### Claude Haiku 5.5 — the current Haiku
- now: Haiku 5.5 (`claude-haiku-5-5`) listed in official pricing at $0.10/$0.50 per MTok up to 100K tokens, $0.50/$2.50 over 100K; supported in Claude Code v2.1.293+. [VERIFIED] (pricing/support). GA/release date unclear — primary docs list it as live while third-party news (as of 2026-10-09) still describes it as "coming weeks"; treat the release date as [DISPUTED].
- source: https://platform.claude.com/docs/en/about-claude/pricing ; https://code.claude.com/docs/en/model-config
- confidence: [VERIFIED] for pricing/support; [DISPUTED] for release date
- why it clears the bar: completes the 5.5 generation and is the cheapest current model; relevant to any cost-tier recommendation.

### Fable 5.1 as the most capable widely released model
- now: Fable 5.1 (`claude-fable-5-1`), $10/$50 per MTok, 1M context / 128K output; thinking always on; resolved by the `fable` alias. Not default on any plan. [VERIFIED]
- source: https://platform.claude.com/docs/en/about-claude/pricing ; https://code.claude.com/docs/en/model-config
- confidence: [VERIFIED]
- why it clears the bar: the file names Opus/Sonnet generations but omits the top tier entirely; a user asking "most capable model" would be mis-answered.

## Could not verify

### Sonnet 5 "made permanent 2026-08-10"
What I searched: the official pricing page footnote on Sonnet 5 introductory pricing. It states the $2/$10 pricing announced as introductory "through August 31, 2026" is now standard and the scheduled 2026-09-01 increase to $3/$15 "will not occur." It does not give 2026-08-10 as the date permanence was announced. The claim is not contradicted, but the specific date is unsourced in the primary doc. Flagging per the rules; low stakes.
- source: https://platform.claude.com/docs/en/about-claude/pricing

### SpaceX acquiring Cursor/Anysphere
What I searched: "AI coding tool shutdown acquired October 2026." Found only aggregator/blog coverage (pinggy.io, tech-insider.org) with conflicting valuations ($3.4B vs $60B) and no primary or press-release confirmation. Not strong enough to enter as a status change; recorded here so it is not silently dropped if a human has an independent source.
- source: https://pinggy.io/blog/spacex_cursor_acquisition_developer_guide

## No longer relevant

None recommended for deletion. The historical dated events (BloopAI, Gemini CLI,
Roo Code, etc.) remain accurate anchors, and the volatility index and structural
principles still hold. The Opus 5 / Sonnet 5 release lines stay useful as the
immediate predecessors of the 5.5 generation.
```

**Summary of what changed since 2026-09-22:** A whole new model generation shipped — **Opus 5.5** (now the default, $4/$20), **Sonnet 5.5** ($2/$10), **Haiku 5.5**, alongside **Fable 5.1** as the top tier. The ledger's verification date is literally Opus 5.5's launch day, so it predates all of it. Two "known fabrication" realities are now stale (default model, current Sonnet), and the four new models need entries. No tools died or broke, and no new CVEs landed after the verification date. Verdict: **CHANGED** — the structure still fits, so no human restructuring needed.
