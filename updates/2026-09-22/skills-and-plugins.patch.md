I have enough to compile the patch. Both primary sources fetched, four searches run covering the volatile claims (superpowers stars, frontend-design installs, recent changelog, community marketplace).

```markdown
# Patch: skills-and-plugins.md
verified_against: 2026-09-22
searches_run: 6
verdict: CHANGED

## Changed

### Level-1 metadata cost is tokens, not words
- was: "1. Name + description only — always in context, ~100 words"
- now: "1. Name + description only — always in context, `[VENDOR]` ~100 tokens per Skill (Level 2 SKILL.md body is under ~5k tokens; Level 3 resources cost none until accessed)"
- source: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- confidence: [VENDOR]
- note: The primary source's cost table states "~100 tokens per Skill," not words. The rest of the progressive-disclosure block is unchanged and still accurate.

### Official-marketplace partner integration list has drifted
- was: "~68 partner-built (GitHub, Playwright, Supabase, Figma, Vercel, Linear, Sentry, Stripe, Firebase)"
- now: `[VENDOR]` The official marketplace's External-integrations category now lists: github, gitlab, atlassian (Jira/Confluence), asana, linear, notion, figma, vercel, firebase, supabase, slack, sentry. Playwright and Stripe are no longer listed among the bundled external-integration plugins; gitlab, atlassian, asana, notion, and slack are new.
- source: https://code.claude.com/docs/en/discover-plugins
- confidence: [VENDOR]
- note: This corrects the illustrative partner list only. The aggregate counts ("~100 entries — roughly 33 Anthropic-built and ~68 partner-built") could not be confirmed — see "Could not verify."

## Status changes

none found — no named tool in the file (superpowers, gstack, GSD, Ay-Skills, the vendor skills, pr-review-toolkit, security-guidance, LSP plugins, Langfuse-observability) was found archived, renamed, acquired, or shut down. The official `claude-plugins-official` marketplace, its install/uninstall commands, and the "orgs can sync plugin sets from claude.ai" claim all still match the primary source.

## New entries

### Anthropic's first-party community marketplace (`claude-plugins-community` / `claude-community`)
- now: `[VENDOR]` A second Anthropic-run marketplace now exists alongside the official one: `anthropics/claude-plugins-community` (added manually with `/plugin marketplace add anthropics/claude-plugins-community`, install via `<plugin>@claude-community`). It hosts third-party plugins that passed Anthropic's automated validation and security screening, each pinned to a specific commit SHA; submissions go through clau.de/plugin-directory-submission (the in-app submission forms feed this, not the official marketplace).
- source: https://code.claude.com/docs/en/discover-plugins , https://github.com/anthropics/claude-plugins-community
- confidence: [VENDOR]
- why it clears the bar: The file's "Marketplaces" section lists only third-party community catalogs (buildwithclaude.com, claudemarketplaces.com, aitmpl.com, Agensi) and omits the now-primary first-party curated/screened community tier — a structural gap in exactly the category the section covers.

### Plugin4Shell supply-chain advisory (plugin SHA-pinning bypass)
- now: `[REPORTED]` A vulnerability ("Plugin4Shell", disclosed ~2026-09-17) let a marketplace plugin's auto-update install different code while the pinned commit SHA still appeared honored — git treated a 40-hex branch name as a ref before treating it as an object. Fixed in Claude Code 2.1.179+ (and Codex 0.146.0+). Directly concerns the SHA-pinning / auto-update mechanism this file's "Plugin mechanics" and "Caution" notes describe.
- source: https://code.claude.com/docs/en/changelog , https://singhajit.com/dev-weekly/2026/sep-14-20/claude-code-projects-plugin4shell-gemini-38-live/
- confidence: [REPORTED]
- why it clears the bar: A supply-chain advisory against the marketplace commit-pinning mechanism is the highest-value thing the "Caution: plugins can carry MCP servers" note should sit next to. Honest caveat: it was disclosed ~2 days *before* the 2026-09-19 last_verified date, so this is a gap the prior pass missed rather than a change since — flagging it because the procedure prioritizes security advisories and it is currently absent.

## Could not verify

### Official marketplace entry counts ("~100 entries — roughly 33 Anthropic-built and ~68 partner-built")
- The primary source (discover-plugins) enumerates categories (code intelligence/LSP, external integrations, security-guidance, development workflows, output styles) but publishes no totals. Searched the official docs and the `anthropics/claude-plugins-official` repo listing; found no authoritative count matching or refuting 33/68/~100. Remains `[REPORTED]`; treat as unconfirmed on merge.

### superpowers star count (already `[DISPUTED]`)
- The file cites 94k / 232k / 288k. Fresh search returns *different* disputed figures — 120k+ (May 2026), 170k+ (2026), and one aggregator showing 265.8k — with no primary GitHub API figure surfaced. The dispute persists but the specific numbers in the file are now stale. Stays `[DISPUTED]`; the "do not quote a precise figure" instruction still holds. Source of shifted figures: https://github.com/obra/superpowers/ (star badge, not captured numerically in search).

### Frontend Design "~277k installs mid-2026"
- Independent coverage corroborates the 277k figure ("installed 277,000 times in four months," https://medium.com/design-bootcamp/the-most-installed-design-document-of-2026-is-30-lines-long-6b9a89834bd8), but this is aggregator/press, not a primary Anthropic install-count source. No change needed; remains `[REPORTED]`.

## No longer relevant

none found — the note that pre-built PowerPoint/Excel/Word/PDF skills are unavailable in Claude Code while the claude-api skill ships bundled is explicitly reconfirmed by the primary source and still worth its budget.
```
