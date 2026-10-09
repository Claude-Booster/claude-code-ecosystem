# Patch: skills-and-plugins.md
verified_against: 2026-10-09
searches_run: 8
verdict: CHANGED

## Changed

### Official marketplace entry count
- was: `[REPORTED]` ~100 entries — roughly 33 Anthropic-built (LSP language servers, feature-dev, code-review, commit-commands, security-guidance, frontend-design) and ~68 partner-built (GitHub, Playwright, Supabase, Figma, Vercel, Linear, Sentry, Stripe, Firebase).
- now: `[VENDOR]` The official web catalog lists **341 plugins** (claude.com/marketplace/plugins, "341 plugins" header, 2026-10-09). The Anthropic-built vs. partner-built split (~33/~68) is no longer published anywhere primary; Anthropic's docs now say the catalog "changes often, so this page doesn't list it." Anthropic's own named plugins still include commit-commands, code-review, feature-dev, security-guidance, and the language-server plugins.
- source: https://claude.com/marketplace/plugins , https://code.claude.com/docs/en/plugins/anthropic-marketplaces
- confidence: [VENDOR]

### Frontend Design install count
- was: `[REPORTED]` ~277k installs mid-2026.
- now: `[DISPUTED]` Install figures now conflict across aggregators — ≥277k (Magier), ~829k (June 2026 analysis), and 1.1M+ (ClaudeLog) — with no primary count. Anthropic's own catalog page (claude.com/marketplace/plugins) shows **no install counts at all** as of 2026-10-09, so the number cannot be grounded. The "most-installed official-marketplace plugin" ranking is still consistently reported.
- source: https://claudelog.com/faqs/what-is-frontend-design-skill-in-claude-code/ , https://www.magier.com/blog/how-to-use-the-claude-code-frontend-design-plugin , https://claude.com/marketplace/plugins
- confidence: [DISPUTED]

## Status changes

none found. All named tools remain live: `obra/superpowers` (plus its `obra/superpowers-skills` companion), `anthropics/skills`, Frontend Design, pr-review-toolkit, security-guidance, LSP plugins, and Langfuse-observability. No archive, rename, acquisition, or breaking change surfaced for any of them.

## New entries

### Claude Marketplace (claude.com/marketplace) — launched 2026-09-23
- what: A unified web storefront launched **after** this file's last-verified date, with **2,000+ connectors and plugins** at launch, organized into three sections: connectors/plugins, agents/products (buy Claude-powered software from partners such as CrowdStrike, Cursor, Harvey, Snowflake using committed Anthropic spend — limited preview), and service partners (Accenture, BCG, Deloitte). Launch integration partners named: Atlassian, Google, Microsoft, Notion, Salesforce.
- source: https://code.claude.com/docs/en/plugins/anthropic-marketplaces (links claude.com/marketplace/plugins as the official web catalog) , https://www.ghacks.net/2026/09/27/anthropic-launches-claude-marketplace-with-more-than-2000-connectors-and-plugins/
- confidence: [REPORTED] (press-sourced; Anthropic's own announcement post was not located — the 2,000+ figure is secondary)
- why it clears the bar: It is the largest structural change to this file's "Marketplaces" category since verification, is now the canonical web catalog referenced by Anthropic's own docs, and the file currently has no mention of it. The 2,000+ figure must not be conflated with the 341 plugins in `claude-plugins-official`.

### Anthropic's official community and demo marketplaces
- what: Anthropic now documents **three** first-party marketplaces, not one: official (`claude-plugins-official`), community (repo `anthropics/claude-plugins-community`, marketplace name **`claude-community`**, for third-party author submissions), and demo (repo `anthropics/claude-code`, name **`claude-code-plugins`**, example plugins). The file's "Community marketplaces" line lists only third-party sites (buildwithclaude.com, etc.) and omits Anthropic's own community/demo marketplaces.
- source: https://code.claude.com/docs/en/plugins/anthropic-marketplaces
- confidence: [VERIFIED]
- why it clears the bar: These are first-party marketplaces a reader will encounter by default; the official-vs-community-vs-demo distinction is a common install-command pitfall. (Honest caveat: the demo marketplace predates 2026-09-22, so this is partly a pre-existing omission rather than strictly new; `claude-community` as a named marketplace appears to be the newer addition.)

## Could not verify

- **Anthropic-built vs. partner-built split in the official marketplace (~33 / ~68):** Searched Anthropic docs, the GitHub repo description, and aggregators. Found one undated guide citing "35 Anthropic-developed" plugins (close to the file's 33), but no authoritative current breakdown; the docs explicitly decline to list the catalog. The headline total moved to 341 (see Changed), but the split is unsourced — treat as [DISPUTED] on merge.
- **`obra/superpowers` star count:** Already `[DISPUTED]` in the file. Newest aggregator snapshot is ~271.5k stars (13 Aug 2026, Portuguese-language article), alongside earlier conflicting 2026 figures (121k, 153k, 177k, 179k). Still no primary figure and still a moving target — the file's existing guidance ("do not quote a precise figure") holds; no change needed beyond noting the newest data point.

## No longer relevant

none. The existing sections all still carry weight; nothing is recommended for deletion.
