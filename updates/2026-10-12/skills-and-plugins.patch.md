# Patch: skills-and-plugins.md
verified_against: 2026-10-12
searches_run: 7
verdict: CHANGED

## Changed

### Agent Skills open-standard date
- was: `[VERIFIED]` Anthropic launched Agent Skills as an open standard in October 2025.
- now: `[VERIFIED]` Anthropic launched Agent Skills on 2025-10-16 and published the format as an open standard on 2025-12-18 (now hosted at agentskills.io). The file merges these two dates into one. The error was already there before 2026-10-09; nothing changed after that date.
- source: https://claude.com/blog/skills (post dated October 16, 2025; update note dated December 18, 2025), https://agentskills.io/home
- confidence: [VERIFIED]

### Frontend Design install count
- was: `[DISPUTED]` Install figures now conflict across aggregators — ≥277k (Magier), ~829k (June 2026 analysis), and 1.1M+ (ClaudeLog) — with no primary count. Anthropic's own catalog page (claude.com/marketplace/plugins) shows **no install counts at all** as of 2026-10-09, so the number cannot be grounded.
- now: `[VENDOR]` Anthropic's catalog shows **1,134,112 installs** on the Frontend Design detail page (2026-10-12). The detail page also marks it "Anthropic verified" and "Made by Anthropic." The grid page at /marketplace/plugins shows no counts, but each plugin's detail page does, and Anthropic's docs say the web catalog "shows install counts." So the claim that there is no primary count is wrong. On ranking: Frontend Design has more installs than every other detail page checked (Superpowers 1,009,371; Code Review 438,525; Context7 417,801). Not all 342 listings were checked, so keep "most-installed" as `[REPORTED]`.
- source: https://claude.com/marketplace/plugins/frontend-design , https://code.claude.com/docs/en/plugins/anthropic-marketplaces , https://claude.com/marketplace/plugins/superpowers
- confidence: [VENDOR]

### Official marketplace count
- was: `[VENDOR]` The official web catalog lists **341 plugins** (claude.com/marketplace/plugins, "341 plugins" header, 2026-10-09).
- now: `[VENDOR]` The official web catalog lists **342 plugins** (claude.com/marketplace/plugins header, 2026-10-12). Treat the number as drifting. The docs still say the catalog "changes often, so this page doesn't list it."
- source: https://claude.com/marketplace/plugins
- confidence: [VENDOR]

### obra/superpowers star count
- was: `[DISPUTED]` star count. Sources cite 94k, 232k, and 288k. See `evidence-ledger.md` — do not quote a precise figure.
- now: `[VERIFIED]` ~298k GitHub stars (297,960 from the GitHub API on 2026-10-12; repo not archived, last push 2026-10-10, MIT). This is a primary source, so the dispute is settled as of this date. The figure is still rising, so quote it with its date. The official catalog also lists Superpowers at `[VENDOR]` 1,009,371 installs, with no "Anthropic verified" badge.
- source: https://api.github.com/repos/obra/superpowers , https://claude.com/marketplace/plugins/superpowers
- confidence: [VERIFIED]

### Langfuse-observability description
- was: **Langfuse-observability** — official tracing plugin
- now: **Langfuse-observability** — a tracing plugin made by Langfuse and listed in the official marketplace. It does not have the "Anthropic verified" badge. `[VENDOR]` 575 installs (2026-10-12). "Official" should mean "in the official marketplace," not "made by Anthropic." At this install count, its place in "Standouts" is weak.
- source: https://claude.com/marketplace/plugins/langfuse-observability
- confidence: [VENDOR]

## Status changes

### GSD (get-shit-done) archived and moved
- was: | gstack, GSD, Ay-Skills | community frameworks | |
- now: `[VERIFIED]` `gsd-build/get-shit-done` was archived by its owner on 2026-06-26 and is read-only. Its README ("GSD Has Moved") names **open-gsd/gsd-core** as the active home. That repo is live: created 2026-05-22, last push 2026-10-12, about 10.4k stars. This happened before 2026-10-09, so it is an existing error, not a new event. The file currently presents an archived project as live. gstack (`garrytan/gstack`) is live: not archived, last push 2026-10-12.
- source: https://github.com/gsd-build/get-shit-done , https://api.github.com/repos/gsd-build/get-shit-done , https://api.github.com/repos/open-gsd/gsd-core , https://api.github.com/repos/garrytan/gstack
- confidence: [VERIFIED]

All other named items are still live and listed in the official `marketplace.json`: `anthropics/skills`, `obra/superpowers`, frontend-design, pr-review-toolkit, security-guidance, pyright-lsp and the other `*-lsp` plugins, and langfuse-observability. No archive, rename or breaking change was found for any of them.

## New entries

### Anthropic's community and demo marketplaces
- now: `[VERIFIED]` Anthropic documents three general-purpose marketplaces:
  - official: `claude-plugins-official`
  - community: repo `anthropics/claude-plugins-community`, installed with `@claude-community`; holds third-party plugins their authors submitted to Anthropic
  - demo: repo `anthropics/claude-code`, installed with `@claude-code-plugins`

  Plugins in the demo marketplace mostly also exist in the official one; install those from official to avoid having two copies. Auto-update is on by default for official marketplaces and off for community and third-party ones.
- source: https://code.claude.com/docs/en/plugins/anthropic-marketplaces , https://code.claude.com/docs/en/discover-plugins
- confidence: [VERIFIED]
- why it clears the bar: The 2026-09-22 and 2026-10-09 patches both flagged this and it is still missing. The file's "Community marketplaces" line lists only third-party sites. Mixing up official, community and demo is a common cause of wrong install commands.

### Context-cost estimates for plugins
- now: `[VERIFIED]` Before you install a plugin from the official marketplace, its details pane shows two token estimates: **Every turn** and **When invoked**. After install, `claude plugin details <name>` reports **Always-on** tokens per session. The Installed tab also flags plugins under "Not used recently."
- source: https://code.claude.com/docs/en/discover-plugins
- confidence: [VERIFIED]
- why it clears the bar: This is the primary-source way to act on the file's own warning ("Check what a plugin bundles before installing"). Launch date not established; it may predate 2026-10-09.

### "Anthropic verified" badge in the catalog
- now: `[VENDOR]` The claude.com catalog marks some plugins **Anthropic verified**, for example Frontend Design and Code Review. Third-party listings such as Superpowers and Langfuse-observability don't have the badge.
- source: https://code.claude.com/docs/en/plugins/anthropic-marketplaces , https://claude.com/marketplace/plugins/frontend-design
- confidence: [VENDOR]
- why it clears the bar: This is the catalog's own trust signal. It replaces the Anthropic-built vs. partner-built split that the file says is no longer published.

## Could not verify

- **Ay-Skills:** A web search for "Ay-Skills" Claude Code returned only generic Skills guides. I found no repo, author or listing, so I can't confirm it exists or is live. Mark it [DISPUTED] or ask a human for the source URL.
- **"Most-installed official-marketplace plugin" for Frontend Design:** It beats the four detail pages checked. Confirming the ranking would need all 342 listings. Keep it as [REPORTED].
- **Official marketplace count, 342 (web) vs `marketplace.json`:** A partial count of the GitHub `marketplace.json` came to about 315 entries. The tool split the 190k-character file into two reads, so this count is approximate. The web catalog and the git catalog may simply be different sets. No clear conflict; quote the web header as [VENDOR] only.
- **New developments after 2026-10-09:** I searched for Claude Code plugin and marketplace news, Agent Skills spec updates, and skill/plugin security advisories. I found nothing dated after 2026-10-09. The newest security item is Datadog's research on malicious skills from 2026-05-11, which is outside the window.

## No longer relevant

none
