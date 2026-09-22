I've verified the file's volatile claims against the primary source and targeted searches. Here is my assessment.

The window under review is just three days (2026‑09‑19 → 2026‑09‑22). I checked the highest‑volatility claims:

- **Model names / defaults** — `code.claude.com/docs/en/model-config` (the file's primary source) still resolves defaults to Opus 5 (Max/Team Premium/Enterprise/API) and Sonnet 5 (Pro/Team Standard). Unchanged.
- **Pricing** — Opus 5 at $5/$25 and Sonnet 5 at $2/$10 (made permanent) both confirmed. Unchanged.
- **CVEs** — OpenCVE shows no Claude Code CVE published after 2026‑09‑19.
- **Tool status** (acquired/archived/shut down) — nothing new in the window. The SpaceX/Anysphere‑Cursor deal (closed 2026‑08‑14) and the Gemini CLI → Antigravity CLI transition (2026‑06‑18) both predate last verification, so they are out of scope for a refresh patch. Claude Code v2.1.278 (2026‑09‑19) shipped no breaking changes; v2.1.277/AGENTS.md remains accurately dated.
- **New entries** — the only in‑window items are minor CLI feature increments (gateway sign‑in, plugin/skill sync), which do not clear the bar for an evidence ledger of disputed/verified claims.

Every specific dated claim in the file still holds. Per the task's rule, that is a successful run:

```markdown
# Patch: evidence-ledger.md
verified_against: 2026-09-22
searches_run: 10
verdict: UNCHANGED
```
