---
last_verified: 2026-09-22
volatility: high
verify_horizon_days: 7
primary_sources:
  - https://code.claude.com/docs/en/overview
---

# Competitive Landscape

Snapshot 2026-09-19. `[VOLATILE]` — this table dates faster than anything else in the bundle.

## Contents
- Status check before recommending
- The field
- 2026 shifts

## Status check before recommending

Four entries below changed status in 2026. Check this list before naming any tool:

| Tool | Status | Correct reference |
|---|---|---|
| **Roo Code** | `[VERIFIED]` archived May 2026 | successor is Roomote; migration target is Kilo Code |
| **Gemini CLI** | `[VERIFIED]` free/individual access retired 2026-06-18 | enterprise (Code Assist) only; Antigravity is the successor platform |
| **Continue** | v2.0 is final | maintenance only |
| **Claude Flow** | renamed | Ruflo — see `orchestration.md` |

## The field

| Tool | Category | Position relative to Claude Code |
|---|---|---|
| **OpenAI Codex CLI** | terminal agent | The autonomy champion — unattended multi-hour runs. `[VERIFIED]` native Windows support and its own sandbox as of March 2026. Default GPT-5.x. Best choice if already on a ChatGPT plan. |
| **Gemini CLI** | terminal agent | Enterprise-only now. 1M context is the differentiator. |
| **Google Antigravity / Jules** | agent platform / async | Antigravity is Gemini CLI's successor; Jules is an async GitHub agent |
| **Cursor** | AI IDE | Background agents in cloud VMs, `[REPORTED]` up to 8 parallel jobs. Acquired Graphite. The IDE-empire play. |
| **Cline** | OSS IDE extension | Governance and approval workflow focus |
| **Kilo Code** | OSS IDE + CLI | `[REPORTED]` the Cline→Roo→Kilo fork tree's resolution point. Rebuilt on OpenCode, 500+ models, worktree Agent Manager, ~1.5M users. |
| **OpenCode** | OSS terminal | `[REPORTED]` ~95–100k stars, 75+ providers, multi-session, privacy-first |
| **Amp** | agentic (Sourcegraph) | Semantic code graph, cross-repo reasoning. Shipped a desktop app Sept 2026. |
| **Factory Droid** | agent | `[VERIFIED]` raised $200M at $5B valuation 2026-09-15 |
| **Augment** | enterprise context | Whole-codebase Context Engine plus Slack and git history. `[VENDOR]` claims #1 on SWE-Bench Pro. Most expensive in the field. |
| **Aider** | OSS terminal | Git-native pair programmer, model-agnostic. Still the cleanest mental model for small changes. |
| **Pi** | terminal | Zechner/Ronacher. Sub-1k-token system prompt, "lazy skills." `[REPORTED]` 50k+ stars. Interesting as a minimalism argument. |
| **Crush** (Charm), **Forge**, **Goose**, **Devin**, **Zed**, **Warp**, **Amazon Q** | various | adjacent niches |

## 2026 shifts

Four things an experienced Claude Code user may not have tracked:

**The terminal became the battleground.** 2025's competition was IDE-shaped; 2026's is CLI-shaped. Claude Code, Codex CLI, and Gemini CLI/Antigravity are the serious entrants.

**Cross-tool standards emerged.** AGENTS.md and Agent Skills now work across vendors. This makes multi-tool setups genuinely practical for the first time and reduces lock-in in both directions — worth mentioning to anyone worried about committing.

**Consolidation and capital.** Factory at $5B, Cursor absorbing Graphite, Bloop shutting down, Roo archiving. The long tail is thinning.

**The fork tree resolved.** Cline → Roo Code → Kilo Code ended with Kilo as the live branch. Anyone still on Roo should be told it's archived.

## How to answer "should I switch?"

Usually: no, and the question is misframed. The differentiators are narrow and most practitioners run two tools rather than switching:

- Need unattended multi-hour autonomy → add Codex CLI
- Need a 1M-token context window → Gemini/Antigravity, enterprise only
- Need cross-repo semantic search → Amp or Augment
- Want IDE-native background agents → Cursor
- Want fully open-source and provider-agnostic → OpenCode or Kilo
- Want minimal surface area → Aider or Pi

Ask what specifically is failing before recommending a switch. Most "Claude Code isn't working" complaints resolve to context or gate problems covered in the other reference files, and survive a tool change intact.
