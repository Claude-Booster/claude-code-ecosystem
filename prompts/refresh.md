# Reference Refresh Task

You are re-verifying one file in a dated technical reference bundle. The bundle's
value is that every claim carries an honest confidence tag. Your job is to find
what changed since it was written — not to rewrite it.

## Input

- Target file: `{{TARGET_PATH}}`
- Last verified: `{{LAST_VERIFIED}}`
- Today: `{{TODAY}}`
- Output: print patch to stdout (the shell captures it)
- Primary sources listed in the file's frontmatter

## Procedure

1. Read `{{TARGET_PATH}}` in full.
2. Fetch every URL in its `primary_sources` frontmatter. These are authoritative;
   prefer them over search results for anything they cover.
3. For each claim carrying `[VERIFIED]`, `[REPORTED]`, `[VENDOR]`, `[DISPUTED]`,
   or `[VOLATILE]`, search for changes dated after `{{LAST_VERIFIED}}`. Prioritize
   in this order: model names and pricing, plan and rate-limit terms, tool status
   (archived / renamed / shut down / acquired), version numbers, security advisories.
4. Search for named tools in the file that have gone archived, renamed, or
   defunct. A dead tool presented as live is the highest-severity error this
   bundle can contain.
5. Search for *new* entries that belong in the file's category and did not exist
   at last verification.

## Output

Print the patch document as your final response (it is captured from stdout by
the calling script — do not use the Write tool). Do not modify `{{TARGET_PATH}}`.
Do not reproduce unchanged sections. Use exactly this structure:

```markdown
# Patch: {{TARGET_NAME}}
verified_against: {{TODAY}}
searches_run: <integer>
verdict: CHANGED | UNCHANGED | NEEDS_HUMAN

## Changed
For each change:
### <short label>
- was: <the exact line or claim currently in the file>
- now: <the corrected claim, carrying its confidence tag>
- source: <URL>
- confidence: [VERIFIED|REPORTED|VENDOR|DISPUTED]

## Status changes
Tools that died, renamed, were acquired, or shipped a breaking change.
Same field structure. If none, write "none found".

## New entries
Things that now belong in this file and are absent. Same field structure,
plus a one-line argument for why it clears the bar for inclusion.

## Could not verify
Claims whose supporting source is gone, paywalled, or contradicted with no
clear winner. State what you searched and what you found. These become
[DISPUTED] on merge — do not silently drop them.

## No longer relevant
Claims that are still accurate but no longer worth the context budget.
Recommend deletion with a one-line reason.
```

## Rules

Every `now:` line needs a URL. A claim you cannot source does not go in
"Changed" — it goes in "Could not verify". This is the whole point of the
exercise; a patch full of unsourced corrections is worse than no patch.

Never upgrade a confidence tag without a primary source. A vendor blog post
supports `[VENDOR]`, never `[VERIFIED]`. Independent reproduction is what moves
`[VENDOR]` to `[REPORTED]`.

If a number now conflicts across sources, the correct output is `[DISPUTED]`
with both values, not a judgment call.

Set `verdict: NEEDS_HUMAN` if the file's structure no longer fits reality —
for example if a whole category collapsed or split. Structural rewrites are a
human decision, so describe the problem instead of restructuring.

Set `verdict: UNCHANGED` and write nothing else if the file holds up. That is a
successful run, not a failed one.

Be skeptical of SEO content farms, which are dense in this topic. A number
appearing on five aggregator blogs with no primary source is one claim, not five.
