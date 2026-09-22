I've verified every claim carrying a confidence tag against the primary sources plus the official changelog and CVE database, filtering for anything dated after the last-verified date of 2026-09-19.

Findings from that window (2026-09-19 → 2026-09-22):
- **Models/routing:** `model-config` confirms the exact default-per-plan table (Opus 5 for Max/Team Premium/Enterprise/API; Sonnet 5 for Pro/Team Standard; Sonnet 4.5 for Microsoft Foundry), Fable 5.1 as newest-but-never-default, and legacy Opus/Sonnet pinnability. No pricing or default change surfaced after the horizon.
- **GitHub Action:** `@v1`, auto-detected interactive/automation modes, `/install-github-app` — all confirmed unchanged.
- **Changelog:** latest release is v2.1.278 on 2026-09-19 (auto-mode server-side classifier); nothing lands in the 09-20→09-22 window, and the auto-mode change touches a surface the file doesn't cover.
- **CVEs / status:** the additional CVEs that surfaced (25724, 24887, 39861, etc.) all publish Feb–earlier 2026, predating last verification — not changes within the window. No named tool went archived/renamed/defunct.
- **Anthropic news:** most recent item is 2026-09-18; nothing after the horizon.

The file holds up. Per the task's rules, an UNCHANGED verdict with nothing else is the correct output.

```markdown
# Patch: core-surfaces.md
verified_against: 2026-09-22
searches_run: 7
verdict: UNCHANGED
```
