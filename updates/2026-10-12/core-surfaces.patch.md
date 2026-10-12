# Patch: core-surfaces.md
verified_against: 2026-10-12
searches_run: 19
verdict: CHANGED

## Changed

### Opus row: superseded by Opus 5.5
- was: `| Opus 5 | 2026-07-24 | $5 / $25 | hard multi-file reasoning, architecture |`
- now: `| Opus 5.5 | 2026-09-22 | $4 / $20 | hard multi-file reasoning, architecture |` `[VERIFIED]`. Opus 5 is now listed as legacy at $5 / $25 and can still be pinned as `claude-opus-5`. The `opus` alias moved to Opus 5.5 in Claude Code v2.1.280, which is also the minimum version.
- source: https://www.anthropic.com/news (dated "Introducing Claude Opus 5.5", Sep 22, 2026); https://claude.com/pricing; https://code.claude.com/docs/en/model-config (Version history)
- confidence: [VERIFIED]

### Sonnet row: superseded by Sonnet 5.5
- was: `| Sonnet 5 | 2026-06-30 | $2 / $10 | daily driver |`
- now: `| Sonnet 5.5 | 2026-09-28 | $2 / $10 | daily driver |` `[VERIFIED]`. Native 1M window. The `sonnet` alias moved to Sonnet 5.5 in v2.1.284. Sonnet 5 is now legacy, at the same $2 / $10.
- source: https://www.anthropic.com/news (dated "Introducing Claude Sonnet 5.5", Sep 28, 2026); https://claude.com/pricing; https://code.claude.com/docs/en/model-config
- confidence: [VERIFIED]

### Haiku row: superseded by Haiku 5.5, with tiered pricing
- was: `| Haiku 4.5 | 2025-10 | ~$1 / $5 | subagent fan-out, mechanical edits |`
- now: `| Haiku 5.5 | 2026-10-07 | $0.10 / $0.50 (≤100K-token prompts); $0.50 / $2.50 (>100K) | subagent fan-out, mechanical edits |` `[VERIFIED]`. Runs with a 1M window on every plan and has no `[1m]` suffix. The `haiku` alias moved to Haiku 5.5 on the Anthropic API in v2.1.293. Haiku 4.5 is now legacy at $1 / $5.
- source: https://www.anthropic.com/news (dated "Introducing Claude Haiku 5.5", Oct 7, 2026); https://claude.com/pricing; https://code.claude.com/docs/en/model-config
- confidence: [VERIFIED]

### Fable 5.1 pricing now published
- was: `| Fable 5.1 | Mythos tier | — | explicit selection only, never a default |`
- now: `| Fable 5.1 | Mythos tier | $10 / $50 | explicit selection only, never a default |` `[VERIFIED]`. The docs still say "Fable models are not the account-type default on any plan or provider." The new `best` alias resolves to Fable where it is available, and to `opus` otherwise.
- source: https://claude.com/pricing; https://code.claude.com/docs/en/model-config
- confidence: [VERIFIED]

### Default model per plan collapsed to one value
- was: `Max, Team Premium, Enterprise, and the Anthropic API default to Opus 5. Pro and Team Standard default to Sonnet 5. Microsoft Foundry defaults to Sonnet 4.5.`
- now: `[VERIFIED]` Pro, Max, Team, Enterprise, the Anthropic API, Claude Platform on AWS, Amazon Bedrock and Google Cloud's Agent Platform all default to Opus 5.5. Microsoft Foundry still defaults to Sonnet 4.5. Before v2.1.280, Pro and Team Standard defaulted to Sonnet 5. The "no single global default" headline still holds, but only because Foundry differs.
- source: https://code.claude.com/docs/en/model-config
- confidence: [VERIFIED]

### Alias resolution differs by provider (add under the models table)
- was: `Legacy Opus 4.5–4.8 and Sonnet 4.5/4.6 remain pinnable by model ID.`
- now: `[VERIFIED]` Legacy Opus 5, Sonnet 5, Haiku 4.5, Fable 5, Opus 4.5–4.8 and Sonnet 4.5/4.6 remain pinnable by model ID. The aliases lag on third-party providers:
  - Claude Platform on AWS: `sonnet` → Sonnet 4.6, `haiku` → Haiku 4.5.
  - Bedrock and Agent Platform: `sonnet` → Sonnet 4.5, `haiku` → Haiku 4.5.
  - Microsoft Foundry: `opus` → Opus 4.6.
  - `opus` → Opus 5.5 on every provider except Foundry.
- source: https://code.claude.com/docs/en/model-config; https://claude.com/pricing
- confidence: [VERIFIED]

### Stale-claims warning needs updating
- was: `[DISPUTED] Many blogs assert "Opus 4.8 is the default" or "Sonnet 4.6 is current." Both were briefly true earlier in 2026 and are now stale.`
- now: `[DISPUTED]` Blogs saying "Opus 4.8 is the default", "Sonnet 4.6 is current", or "Opus 5 / Sonnet 5 is current" are all stale. The 5.5 generation shipped between 2026-09-22 and 2026-10-07.
- source: https://code.claude.com/docs/en/model-config
- confidence: [VERIFIED]

## Status changes

### Dynamic workflows no longer labelled research preview
- was: `3. **Dynamic workflows** — research preview. Claude writes an orchestration script on the fly and fans out coordinated subagents.`
- now: `[VERIFIED]` The docs no longer carry a preview label. Dynamic workflows are "available on all paid plans, with Anthropic API access, and on Amazon Bedrock, Google Cloud's Agent Platform, and Microsoft Foundry." On Pro they are turned on from `/config`. Claude writes a workflow when the prompt contains the `ultracode` keyword or a direct request, or for every substantive task after `/effort ultracode`. `/deep-research` comes bundled. Saved workflows live in `.claude/workflows/`.
- source: https://code.claude.com/docs/en/workflows.md
- confidence: [VERIFIED]

## New entries

### Claude apps gateway (first-party self-hosted gateway)
- now: `[VERIFIED]` A self-hosted gateway ships inside the `claude` binary (`claude gateway --config gateway.yaml`, v2.1.195+).
  - Upstreams: Bedrock, Claude Platform on AWS, Google Cloud, Microsoft Foundry, or the Anthropic API.
  - Developers sign in with corporate SSO through `/login`. Model access and managed settings are enforced per IdP group, and usage is exported as OTLP.
  - Needs PostgreSQL.
  - Has no service-token flow, so CI pipelines can't authenticate through it.
  - Gateway sessions use the 5-minute cache TTL only.
  - The docs now split gateways into "Claude apps gateway" and "Other LLM gateways". For the second group: "Anthropic doesn't endorse, maintain, or audit other gateway products."
- source: https://code.claude.com/docs/en/gateways.md; https://code.claude.com/docs/en/claude-apps-gateway.md
- confidence: [VERIFIED]
- why: the Enterprise deployment section presents LiteLLM and third-party proxies as the only gateway path. A first-party gateway changes that recommendation.

### Opus 5.5 fast mode pricing
- now: `[VENDOR]` Opus 5.5 fast mode (up to 2.5x speed, in Claude Code and Claude Platform) costs $8 input / $40 output per Mtok. Thinking can no longer be switched off for Opus 5.5.
- source: https://www.anthropic.com/news/claude-opus-5-5
- confidence: [VENDOR]
- why: fast mode is a Claude Code surface and doubles the cost of the default model. It belongs in the models section.

### Additional high-severity CVE
- now: `[REPORTED]` CVE-2026-24887 (CVSS 8.8): a command-parsing flaw let attackers bypass the confirmation prompt through `find`. Fixed in 2.0.72. A second advisory, CVE-2026-46406 (medium), covers a `/copy` predictable `/tmp` path and is fixed in 2.1.128.
- source: https://advisories.gitlab.com/pkg/npm/@anthropic-ai/claude-code/CVE-2026-24887/; https://advisories.gitlab.com/npm/@anthropic-ai/claude-code/CVE-2026-46406/
- confidence: [REPORTED]
- why: the file's "Known CVEs" line lists two medium advisories and leaves out a higher-severity permission bypass. Both advisories predate 2026-10-09, but the file doesn't have them.

## Could not verify

### Agent Teams invoked with `/team`
- The agent-teams doc confirms "experimental and disabled by default" and `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`. It describes starting a team in natural language ("Spawn three teammates…") and never mentions a `/team` command. I found no source for `/team`. Mark the invocation clause `[DISPUTED]`. The env-var gate stays verified.
- searched: https://code.claude.com/docs/en/agent-teams.md, llms.txt index

### Cowork compliance gap ("as of May 2026")
- I found no source showing that Cowork has been added to Audit Logs, the Compliance API or Data Exports. The secondary sources disagree on the details: MintMCP says Cowork is fully excluded, while claudeforoperators.com (verified 2026-05-05) says usage metadata is logged but not content. I found no primary Anthropic doc that addresses Cowork specifically. The existing claim is probably still true, but its `[VERIFIED]` tag rests on sources from May.
- searched: "Cowork audit logs Compliance API data exports"; support.claude.com audit-log articles

### Sonnet 5.5 cache-read price cut
- Secondary coverage of the Haiku 5.5 launch says Sonnet 5.5 cache reads dropped from $0.20 to $0.10 per Mtok. The pricing page fetch didn't return cache rates, so this is unconfirmed. It isn't in the file today. Note it only if cache pricing is added.

## No longer relevant

- `Sonnet 5 pricing was made permanent 2026-08-10, cancelling a planned increase to $3/$15.`: delete. Sonnet 5 is now legacy and Sonnet 5.5 launched at the same $2 / $10, so the cancelled increase no longer affects any choice.
