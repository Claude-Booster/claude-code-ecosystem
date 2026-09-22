---
last_verified: 2026-09-22
volatility: high
verify_horizon_days: 7
primary_sources:
  - https://code.claude.com/docs/en/model-config
---

# Evidence Ledger

Snapshot 2026-09-19. Read this before citing any number from this bundle.

## Contents
- Why this file exists
- Known fabrications
- Disputed figures
- Vendor-reported claims
- Verified primary sources
- Volatility index

## Why this file exists

The information layer around Claude Code is heavily polluted. A large share of "best Claude Code X in 2026" pages are SEO farms that fabricate star counts, invent model names, and restate vendor marketing as measurement. Two pages can cite the same repo with a 3× difference in stars.

The practical rule: **if a number matters to the user's decision, say where it came from and how confident it is.** If it doesn't matter, leave it out rather than sourcing it loosely.

## Known fabrications

Correct these if the user repeats them:

| Claim in circulation | Reality |
|---|---|
| "Opus 4.8 is the default model" | Stale. Defaults are plan-dependent; Opus 5 or Sonnet 5 depending on tier. |
| "Sonnet 4.6 is the current Sonnet" | Stale. Sonnet 5 since 2026-06-30. |
| "Anthropic Foundry" | Not a product. The real entity is Microsoft Foundry. |
| Precise install/star counts stated to three significant figures | Almost always invented or copied from a stale scrape. |

## Disputed figures

| Subject | Conflicting values | How to handle |
|---|---|---|
| `obra/superpowers` stars | 94k / 232k (v6.0 release notes) / ~288k | Say "one of the largest community skill collections." Don't pick a number. |
| Serena stars | ~19k–24k depending on snapshot | Range, or omit. |
| Official plugin marketplace size | ~100 curated; "thousands" third-party | The ~100 curated figure is firmer. |
| Code review catch rates | Greptile 82% vs CodeRabbit 44% `[VENDOR]`; Bugbot ~95.95% precision `[REPORTED]` | Both directions are real — one measures recall, one precision. Explain the trade-off rather than ranking. |

## Vendor-reported claims

Never present these as measurement. Always attribute.

- **Ruflo:** 84.8% SWE-bench solve rate, 75% cost savings. Self-reported, no independent reproduction found.
- **Augment:** #1 on SWE-Bench Pro. Self-reported.
- **Greptile:** the July 2025 50-PR benchmark, including the competitor numbers in it. Run by Greptile.

## Verified primary sources

These held up against official documentation or primary research. Safe to state as fact, with the snapshot date attached.

**Anthropic official:**
- Model lineup, pricing, and plan-dependent defaults (Claude Code model-config docs)
- Opus 5 release 2026-07-24 at $5/$25; Sonnet 5 release 2026-06-30 at $2/$10, made permanent 2026-08-10
- Hooks and permissions as the deterministic enforcement mechanism ("Steering Claude Code")
- Large-codebase context guidance — lean layered CLAUDE.md, subdirectory init
- GitHub Action v1 interactive vs automation modes
- Self-hosted runner beta for Team/Enterprise
- Supported enterprise paths: Bedrock, Vertex AI, Claude Platform on AWS, Microsoft Foundry, LLM gateways
- Agent Skills as an open standard, October 2025; plugin marketplace 2025-10-09
- OpenTelemetry in CLI and Agent SDK
- Cost figures: ~$13/developer/active-day, $150–250/developer/month
- 2026-04-04 policy blocking Pro/Max subscriptions with third-party agent frameworks

**Anthropic research, June 2026 — "How Claude Code is used in practice"** (~400,000 sessions, 235,000 users, Oct 2025–Apr 2026): 28–33% verified success rate at intermediate+ difficulty; 19% novice abandonment vs 5–7% for others. This is the best-powered study available on the question and is worth citing by name.

**Academic:** Hasan et al. 2025, arXiv:2506.13538 — 1,899 open-source MCP servers surveyed; 7.2% with general vulnerabilities, 5.5% with tool-poisoning vectors.

**Security guidance:** CSA research note July 2026 (IDE auto-execution of project MCP servers with dev privileges, no process isolation); NSA/CISA-adjacent guidance June 2026; Microsoft state-of-MCP-security 2026.

**CVEs:** CVE-2025-59536 (malicious hooks via repo `.claude/settings.json`), CVE-2026-21852 (API key exfiltration via `ANTHROPIC_BASE_URL`).

**Dated status changes:** Claude Code v2.1.277 AGENTS.md support (2026-09-18); v2.1.89 rate-limit consumption regression (March 2026); BloopAI shutdown (2026-04-10); Gemini CLI individual retirement (2026-06-18); Roo Code archived (May 2026); Factory $200M at $5B (2026-09-15); Cursor acquires Graphite (Dec 2025); Cowork GA (2026-04-09); Channels (2026-03-20, iMessage 2026-03-26).

**Third-party telemetry:** Faros AI "Acceleration Whiplash," ~22,000 developers / 4,000+ teams. Credible methodology, single vendor, directionally useful — tag `[REPORTED]`.

## Volatility index

How fast each area decays. Suggest a live check past the stated horizon.

| Area | Half-life | Check when |
|---|---|---|
| Model names, pricing, defaults | ~1 quarter | always |
| Rate limits and plan terms | ~1 quarter | always |
| Competitive landscape, funding, acquisitions | ~2 quarters | if naming a specific tool |
| Star counts, install counts | continuous | never cite precisely |
| Tool status (archived/renamed/shut down) | ~2 quarters | before every recommendation |
| MCP server availability and maintainership | ~2 quarters | before recommending |
| CLI feature surface | ~1 month for new features, stable for primitives | for anything experimental |
| Security research findings | slow | rarely |
| Anthropic best-practice guidance | slow | rarely |
| Structural principles (context is zero-sum, hooks enforce, skills before MCP) | durable | these are the safe core |

**When in doubt, fall back to the structural principles.** They have held across every model and tooling generation so far and are unlikely to be the thing that's wrong.
