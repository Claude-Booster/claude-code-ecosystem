I have enough to compile the patch. Direct GitHub counts are the authoritative source and reveal the star figures have moved materially; the Ruflo benchmark claim now has an independent debunking.

```markdown
# Patch: orchestration.md
verified_against: 2026-09-22
searches_run: 14
verdict: CHANGED

## Changed

### Spec Kit star count
- was: `| **GitHub Spec Kit** | ... | ~87k | ...`
- now: ~138k stars `[REPORTED]` (a ~60% understatement — the largest stale number in the table)
- source: https://github.com/github/spec-kit
- confidence: [REPORTED]

### OpenSpec star count
- was: `| **OpenSpec** | ... | ~39k, `[REPORTED]` +863% over six months | ...`
- now: ~70k stars `[REPORTED]`; still the fastest-growing entry, so the "+863%" narrative holds but the absolute number nearly doubled
- source: https://github.com/Fission-AI/OpenSpec
- confidence: [REPORTED]

### BMAD-METHOD star count
- was: `| **BMAD-METHOD** | ... | ~44k | ...`
- now: ~53k stars `[REPORTED]`
- source: https://github.com/bmad-code-org/BMAD-METHOD
- confidence: [REPORTED]

### Task Master AI star count / license
- was: `| **Task Master AI** | ... | growth stalled, `[REPORTED]` ~+18% | Cursor-centric. MIT + Commons Clause ...`
- now: ~28k stars `[REPORTED]`; growth-stalled framing still fits. License unchanged: MIT + Commons Clause (may use commercially, may not sell/host it as a service) — the "check licensing for commercial use" caveat is still correct.
- source: https://github.com/eyaltoledano/claude-task-master
- confidence: [REPORTED]

### Ruflo SWE-bench claim now independently refuted (not merely unreproduced)
- was: `[VENDOR]` Ruflo claims an 84.8% SWE-bench solve rate and 75% cost savings. Self-reported; no independent reproduction found. Attribute explicitly if citing.
- now: `[DISPUTED]` Ruflo claims 84.8% SWE-bench and 75% cost savings; an independent audit found the figure is produced by `simulate_benchmarks.py`, which adds `random.uniform(-0.05, 0.05)` to hardcoded base rates rather than running the suite, and Ruflo does not appear on the official SWE-bench leaderboard. Do not cite the number as a benchmark result; if mentioned at all, mark it as fabricated/synthetic.
- source: https://github.com/ruvnet/ruflo/issues/1514 (independent audit); https://www.swebench.com/SWE-bench/ (leaderboard, absence)
- confidence: [DISPUTED]

### Omnara pricing
- was: `**Omnara** | YC S25, voice via LiveKit, `[REPORTED]` ~$9–20/mo`
- now: free tier (≤10 agent sessions/mo) + `[REPORTED]` $20/mo unlimited; the $9/mo figure was an earlier launch price no longer advertised
- source: https://www.ycombinator.com/launches/OCT-omnara-the-first-command-center-for-ai-agents-terminal-web-and-mobile
- confidence: [REPORTED]

## Status changes

### Ruflo star count (minor, no material change)
- was: `[REPORTED]` ~72k stars
- now: ~73k stars `[REPORTED]` — essentially unchanged; note that several aggregator blogs report ~31k, which is stale. GitHub is authoritative here.
- source: https://github.com/ruvnet/ruflo
- confidence: [REPORTED]

### Agent OS "publicly downsized" now has a concrete anchor
- was: `**Agent OS** | | stagnant | `[REPORTED]` publicly downsized. Do not recommend as current.`
- now: Confirmed and datable — Agent OS v3.0 (January 2026) explicitly retired the v2 implementation and orchestration phases and now defers to Claude Code plan mode, keeping only spec-shaping (`/shape-spec`). The "do not recommend as an orchestrator" guidance is correct; it is, however, still actively maintained as a spec-shaping layer, so "stagnant/defunct" would overstate it.
- source: https://buildermethods.com/agent-os/migration ; https://github.com/buildermethods/agent-os/discussions/310
- confidence: [VENDOR]

### Vibe Kanban / BloopAI shutdown — confirmed, no change
- The `[VERIFIED]` "BloopAI shut down 2026-04-10; community-maintained since" line holds exactly. Server functionality sunset ~30 days after; project continues Apache-2.0, fully local.
- source: https://www.vibekanban.com/blog/shutdown
- confidence: [VERIFIED]

### Subscription policy change — confirmed, no change
- The `[VERIFIED]` 2026-04-04 block on Pro/Max subscribers using third-party frameworks holds. Worth noting the flashpoint was the OpenClaw harness specifically; the policy generalized to most third-party frameworks.
- source: https://finance.biggo.com/news/202604050055_Anthropic-Claude-blocks-third-party-AI-agents-subscription
- confidence: [VERIFIED]

## New entries

### Claude Managed Agents (first-party)
- what: Anthropic's hosted agent service (launched 2026-04-08) — deploy agents on Anthropic's own sandbox/state/error-recovery infrastructure via API, no self-built harness.
- why it clears the bar: it landed four days after the subscription block and is Anthropic's own answer to "I need orchestration but can't run a third-party harness on my plan." It directly reshapes the "prior question" and the "subscription policy change" sections' recommendations. Caveat: per the file's own convention (first-party surfaces live in `core-surfaces.md`), this may belong there rather than here — flagging rather than placing.
- source: https://medium.com/@tentenco/anthropic-managed-agents-what-it-is-what-it-kills-and-why-the-timing-matters-0f70c1822f93 (secondary; primary Anthropic announcement should be located before merge)
- confidence: [REPORTED]

## Could not verify

### ECC / Everything Claude Code status
- The file lists ECC as an "agent-harness optimization system." Targeted verification of its current maintenance status / star count was not run within this pass; no contradicting evidence found either. Searched: primary source frontmatter (covers only Anthropic sub-agents docs) — ECC is not covered there. Recommend a dedicated check next cycle; leave the entry as-is for now (not downgrading absent evidence).

## No longer relevant

- none found. Every section still maps to a live category; recommend no deletions. (The star-count table remains worth its budget precisely because the numbers drifted this much in three days — but consider tagging the whole "stars" column `[VOLATILE]` so future readers treat single figures as snapshots.)
```

**Summary of what moved:** the spec-driven star counts were all materially understated (Spec Kit worst, ~87k → ~138k), and the Ruflo 84.8% SWE-bench claim has crossed from "unreproduced `[VENDOR]`" to "independently refuted as fabricated `[DISPUTED]`" — that tag change is the most consequential correction here. No category collapsed, so the verdict is `CHANGED`, not `NEEDS_HUMAN`.
