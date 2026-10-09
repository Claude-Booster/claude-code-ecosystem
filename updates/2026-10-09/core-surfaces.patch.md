# Patch: core-surfaces.md
verified_against: 2026-10-09
searches_run: 8
verdict: CHANGED

## Changed

### Model lineup — three new models superseded the entire current-generation table
The file's "Models and routing" table predates the 5.5 generation. Opus 5.5 shipped on the file's own last-verified date (2026-09-22), and Sonnet 5.5 and Haiku 5.5 landed after it. The rows for Opus 5, Sonnet 5, and Haiku 4.5 are no longer the current tier.
- was:
  ```
  | Opus 5 | 2026-07-24 | $5 / $25 | hard multi-file reasoning, architecture |
  | Sonnet 5 | 2026-06-30 | $2 / $10 | daily driver |
  | Haiku 4.5 | 2025-10 | ~$1 / $5 | subagent fan-out, mechanical edits |
  ```
- now:
  ```
  | Opus 5.5 | 2026-09-22 | $4 / $20 | hard multi-file reasoning, architecture; the default |
  | Sonnet 5.5 | 2026-09-28 | $2 / $10 | daily driver |
  | Haiku 5.5 | 2026-10-07 | $0.10 / $0.50 (≤100K prompt; $0.50 / $2.50 beyond) | subagent fan-out, mechanical edits |
  ```
- source: https://www.anthropic.com/news (release dates), https://platform.claude.com/docs/en/about-claude/pricing (prices), https://code.claude.com/docs/en/model-config (version history: v2.1.280 opus→5.5, v2.1.284 sonnet→5.5, v2.1.293 haiku→5.5)
- confidence: [VERIFIED]

### Haiku pricing model is now prompt-length-tiered
- was: `| Haiku 4.5 | 2025-10 | ~$1 / $5 | subagent fan-out, mechanical edits |`
- now: Haiku 5.5 is priced by prompt length — $0.10/$0.50 per Mtok for prompts up to 100K tokens, $0.50/$2.50 beyond. A single flat rate no longer describes the Haiku tier.
- source: https://platform.claude.com/docs/en/about-claude/pricing
- confidence: [VERIFIED]

### Default model — Pro no longer defaults to Sonnet; everything defaults to Opus 5.5
This is the highest-impact correction: the file says Pro/Team Standard default to Sonnet. As of v2.1.280 every first-party plan and the three Anthropic-operated/partner clouds default to Opus 5.5.
- was: "Max, Team Premium, Enterprise, and the Anthropic API default to Opus 5. Pro and Team Standard default to Sonnet 5. Microsoft Foundry defaults to Sonnet 4.5."
- now: "`[VERIFIED]` Pro, Max, Team, Enterprise, and the Anthropic API — plus Claude Platform on AWS, Amazon Bedrock, and Google Cloud's Agent Platform — default to Opus 5.5. Microsoft Foundry still defaults to Sonnet 4.5."
- source: https://code.claude.com/docs/en/model-config
- confidence: [VERIFIED]

### Legacy pinnable set now includes Opus 5 and Sonnet 5
- was: "Legacy Opus 4.5–4.8 and Sonnet 4.5/4.6 remain pinnable by model ID."
- now: "Legacy Opus 4.5–4.8 and 5, and Sonnet 4.5/4.6 and 5, remain pinnable by model ID."
- source: https://code.claude.com/docs/en/model-config (pinning / `modelOverrides` / version history)
- confidence: [VERIFIED]

## Status changes

### Opus 5, Sonnet 5, Haiku 4.5 — superseded, not dead
None archived/renamed/acquired. Opus 5, Sonnet 5, and Haiku 4.5 are all still served and pinnable by ID; they moved from "current" to "legacy." Captured in Changed above. No tool in the file was found archived, renamed, defunct, or acquired.

## New entries

The genuinely new things in this file's model category — Opus 5.5, Sonnet 5.5, Haiku 5.5 — are folded into the table replacement under Changed rather than listed separately, since they displace existing rows. No new entry in the other categories (extension primitives, IDE/CI, remote control, multi-agent, enterprise) cleared the bar within the 17-day window; primary sources and searches surfaced nothing new there.

## Could not verify

### GitHub Action "Supports `/review` and `/fix`"
- The file states the action "Supports `/review` and `/fix`." The current primary doc (https://code.claude.com/docs/en/github-actions) documents PR review through the `code-review` **plugin/skill** invoked via the `prompt` input with `--comment`, and treats automatic review as a separate product (/docs/en/code-review). It does not mention `/review` or `/fix` as action-level commands anywhere in the page. I could not confirm these slash commands still exist as described, nor source a clean replacement wording for `/fix`. Searched the github-actions primary doc in full; found the skill-based review flow instead. Flag for a human — likely stale, becomes [DISPUTED] on merge.

## No longer relevant

### Sonnet 5 pricing-permanence note
- "`[VERIFIED]` Sonnet 5 pricing was made permanent 2026-08-10, cancelling a planned increase to $3/$15." — Still accurate (the pricing page confirms the cancelled Sept 1 increase), but Sonnet 5 is now a legacy model and Sonnet 5.5 is the current Sonnet at the same $2/$10. Recommend condensing to a one-line footnote or dropping, as the historical pricing-scare detail no longer informs a current decision.
- source (still-true basis): https://platform.claude.com/docs/en/about-claude/pricing (footnote 3)
