#!/usr/bin/env python3
"""Sync every displayed date in the repo to the reference `last_verified` dates.

Run after apply_patches.py. Idempotent; writes a file only when a date changed.

- Each `references/<f>.md` body line `Snapshot <date>` → that file's own `last_verified`.
- Corpus-level surfaces → the newest (max) `last_verified`:
    * README badges `snapshot`/`verified` (shields.io escapes a literal dash as `--`,
      so an ISO date appears doubled in the badge URL but plain in alt text),
    * SKILL.md front-matter description (`snapshot <date>`) and body (`Snapshot: **<date>**`),
    * assets/banner.svg (`SNAPSHOT <date>`).
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def last_verified(text):
    m = re.search(r"^last_verified:\s*(\d{4}-\d{2}-\d{2})", text, re.M)
    return m.group(1) if m else None


changed = []
per_file = []
dates = []
for ref in sorted((ROOT / "references").glob("*.md")):
    text = ref.read_text(encoding="utf-8")
    d = last_verified(text)
    if d:
        per_file.append((ref, text, d))
        dates.append(d)

if not dates:
    print("update_dates: no last_verified dates found in references/", file=sys.stderr)
    sys.exit(1)

newest = max(dates)  # ISO dates sort lexicographically


def write_if_changed(path, new_text, old_text):
    if new_text != old_text:
        path.write_text(new_text, encoding="utf-8")
        changed.append(path.name)


# 1. Each reference body "Snapshot <date>" → that file's own last_verified.
for ref, text, d in per_file:
    write_if_changed(ref, re.sub(r"(?m)^(Snapshot )\d{4}-\d{2}-\d{2}", rf"\g<1>{d}", text), text)

# 2. SKILL.md — corpus date (description + body).
skill = ROOT / "SKILL.md"
st = skill.read_text(encoding="utf-8")
new = re.sub(r"(snapshot )\d{4}-\d{2}-\d{2}", rf"\g<1>{newest}", st)
new = re.sub(r"(Snapshot: \*\*)\d{4}-\d{2}-\d{2}(\*\*)", rf"\g<1>{newest}\g<2>", new)
write_if_changed(skill, new, st)

# 3. assets/banner.svg — corpus date.
banner = ROOT / "assets" / "banner.svg"
if banner.exists():
    bt = banner.read_text(encoding="utf-8")
    write_if_changed(banner, re.sub(r"(SNAPSHOT )\d{4}-\d{2}-\d{2}", rf"\g<1>{newest}", bt), bt)

# 4. README badges + alt text — corpus date.
readme = ROOT / "README.md"
rt = readme.read_text(encoding="utf-8")
dashed = newest.replace("-", "--")
new = re.sub(r"(badge/snapshot-)\d{4}--\d{2}--\d{2}(-)", rf"\g<1>{dashed}\g<2>", rt)
new = re.sub(r"(badge/verified-)\d{4}--\d{2}--\d{2}(-)", rf"\g<1>{dashed}\g<2>", new)
new = re.sub(r'(alt="snapshot )\d{4}-\d{2}-\d{2}(")', rf"\g<1>{newest}\g<2>", new)
new = re.sub(r'(alt="last verified )\d{4}-\d{2}-\d{2}(")', rf"\g<1>{newest}\g<2>", new)
write_if_changed(readme, new, rt)

if changed:
    print(f"update_dates: synced to {newest} — updated {', '.join(changed)}")
else:
    print(f"update_dates: all dates already at {newest}")
