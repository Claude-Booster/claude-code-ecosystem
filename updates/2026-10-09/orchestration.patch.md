I now have enough to compile the patch. Let me cross-check the Ruflo rename discrepancy against the authoritative GitHub repo and the subscription policy primary detail is already confirmed. Compiling the patch now.

```markdown
# Patch: orchestration.md
verified_against: 2026-10-09
searches_run: 15
verdict: CHANGED

## Changed

### GitHub Spec Kit star count
- was: | **GitHub Spec Kit** | ... | ~87k | Teams needing auditable process. ... |
- now: Spec Kit is at ~141k stars `[REPORTED]` (GitHub live count 140.5k). The ~87k figure is badly stale; by Aug 14 2026 it was already ~128k. This is the clear leader by star count, not a near-peer of the others.
- source: https://github.com/github/spec-kit
- confidence: [REPORTED]

### OpenSpec star count and growth figure
- was: | **OpenSpec** | ... | ~39k, `[REPORTED]` +863% over six months | Fastest-growing. ... |
- now: OpenSpec is at ~71k stars `[REPORTED]` (GitHub live count 71.4k). The "~39k" number is stale. The "+863% over six months" figure is historical and no longer current; it should be dropped or re-dated, not presented as a live rate. OpenSpec is still growing fast but is now well behind Spec Kit (~141k), so "Fastest-growing" is no longer safe to assert without a fresh rate comparison.
- source: https://github.com/Fission-AI/OpenSpec
- confidence: [REPORTED]

### Ruflo star count (minor)
- was: ~73k stars `[REPORTED]` — essentially unchanged; note that several aggregator blogs report ~31k, which is stale.
- now: ~74k stars `[REPORTED]` (GitHub live count 74.2k). "Essentially unchanged" still holds; the ~31k aggregator figure remains stale. Only the headline number needs a nudge.
- source: https://github.com/ruvnet/ruflo
- confidence: [REPORTED]

### Omnara pricing
- was: | **Omnara** | YC S25, voice via LiveKit, `[REPORTED]` ~$9–20/mo | relay sees your code ... |
- now: Omnara is a free tier (10 agent sessions/mo) + $20/mo unlimited `[REPORTED]`; when agents run in your own environment you use your existing Pro/Max subscription with no extra token charge. The "~$9" lower bound is not substantiated — current structure is free or $20/mo.
- source: https://www.ycombinator.com/companies/omnara
- confidence: [REPORTED]

## Status changes

### Agent OS — not stagnant/defunct; actively maintained (v3)
- was: | **Agent OS** | | stagnant | `[REPORTED]` publicly downsized. Do not recommend as current. |
- now: Agent OS shipped **v3** (repositioned Jan 2026): Builder Methods deliberately stripped ~70% of the framework and now defers spec-writing to Plan Mode, keeping a thin standards-injection layer (`/shape-spec`, profiles, mission/roadmap/tech-stack files). It is **actively maintained**, not stagnant or defunct. The "publicly downsized" observation is correct, but "Do not recommend as current" is wrong — it is current, just leaner. (The repositioning predates the 2026-09-22 snapshot, so this is a standing mischaracterization rather than fresh drift, but it is a live-tool-painted-as-dead error and worth correcting.) This also softens the related claim in "The prior question" that lists Agent OS as a casualty of frontier models absorbing scaffolding — the direction is right, the "downsized out of relevance" implication is not.
- source: https://buildermethods.com/agent-os/v2/concepts (v3 release/migration notes)
- confidence: [REPORTED]

### Conductor — no longer accurately "macOS only"
- was: | **Conductor** | native macOS app (Melty Labs, YC S24) | active | ... macOS only. |
- now: Conductor desktop is still Mac-first, but Conductor launched **Conductor Cloud** (microVM cloud workspaces, multiplayer, public API) on 2026-07-30, with iOS listed as "soon." "macOS only" is no longer accurate — there is a browser/API path and mobile is in flight. (Cloud launch predates the 2026-09-22 snapshot, so this is a standing inaccuracy, not post-snapshot drift.)
- source: https://www.ycombinator.com/companies/conductor
- confidence: [REPORTED]

Other tools checked and unchanged: Vibe Kanban (BloopAI shutdown 2026-04-10 confirmed, community-maintained — holds), Sculptor/Imbue (active, no acquisition found — holds), Task Master AI (still MIT + Commons Clause, growth still roughly flat at ~25k — holds), subscription policy change (2026-04-04 Pro/Max third-party block confirmed by multiple outlets — holds).

## New entries

### First-party "agent teams" / swarm mode (candidate; likely belongs in core-surfaces.md)
- was: (absent from the swarm-orchestrators section)
- now: Anthropic shipped native **agent teams** (a.k.a. swarm mode) — coordinated multi-session teams the main agent spawns and supervises, plus background agents and cross-session messaging via `SendMessage`, documented in the primary sub-agents page. Argument for inclusion: it is first-party, directly competes with the third-party swarm orchestrators in this file's "Swarm orchestrators" category, and reinforces the file's own "check first-party first" thesis.
- source: https://code.claude.com/docs/en/sub-agents
- confidence: [VERIFIED]
- note: This is first-party, so it most likely belongs under the existing `core-surfaces.md` pointer rather than the third-party swarm table — flagging as a gap, not prescribing placement. No net-new *third-party* orchestrator clearing the inclusion bar appeared after 2026-09-22 (swarm-code, codec-swarm, Zerg exist but are early-stage/pre-snapshot and low-signal).

## Could not verify

### Ruflo rename date and trademark justification
- claim in file: `[VERIFIED]` "Renamed January 2026 to avoid Anthropic trademark conflict."
- what I searched: Ruflo/claude-flow rename date and reason, plus the GitHub repo itself.
- what I found: The rename (ruvnet/claude-flow → ruvnet/ruflo) is real and confirmed. But the **month conflicts** across sources — some say January 2026, others tie it to the v3.5 stable release dated 2026-02-27. The **trademark reason is secondary-sourced**: the project's own README presents the new name as a stylistic choice ("named by rUv, who loves Rust, flow states…"), not a trademark action, and I found no primary Anthropic statement. The GitHub repo states "Claude Flow is now Ruflo" with no date. Recommend downgrading from `[VERIFIED]` to `[DISPUTED]`: the rename is verified, but "January 2026" and "to avoid Anthropic trademark conflict" are not.
- source: https://github.com/ruvnet/ruflo

## No longer relevant
none found
```

That's the patch. Summary of what I changed and why:

- **CHANGED verdict**, not UNCHANGED — the two spec-driven star counts drifted hard (Spec Kit ~87k→~141k, OpenSpec ~39k→~71k), Omnara's pricing was wrong, and two tool-status lines (Agent OS "stagnant/do not recommend", Conductor "macOS only") no longer match reality.
- The **highest-severity items**: Agent OS is painted as dead but is actively maintained (v3), and the Ruflo rename's `[VERIFIED]` date/reason doesn't survive scrutiny → downgrade to `[DISPUTED]`.
- The file's **structure still fits** (categories intact, subscription-policy anchor confirmed), so no `NEEDS_HUMAN`.
- Every `now:` line carries a primary GitHub/YC/vendor URL; the one unsourceable item (Ruflo date) went to *Could not verify*, not *Changed*.
