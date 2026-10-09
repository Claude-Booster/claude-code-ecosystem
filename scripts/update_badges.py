#!/usr/bin/env python3
"""Bump the README snapshot/verified badges to the newest reference last_verified date.

Run after apply_patches.py. Idempotent: writes README.md only when a date changed.
The shields.io static-badge message escapes a literal dash as a double dash, so an
ISO date 2026-10-09 appears as 2026--10--09 in the badge URL but 2026-10-09 in alt text.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
README = ROOT / "README.md"

dates = []
for ref in sorted((ROOT / "references").glob("*.md")):
    m = re.search(r"^last_verified:\s*(\d{4}-\d{2}-\d{2})", ref.read_text(encoding="utf-8"), re.M)
    if m:
        dates.append(m.group(1))

if not dates:
    print("update_badges: no last_verified dates found in references/", file=sys.stderr)
    sys.exit(1)

newest = max(dates)  # ISO dates sort lexicographically
dashed = newest.replace("-", "--")  # shields.io escapes a literal '-' as '--'

text = README.read_text(encoding="utf-8")
original = text
# Badge URL: .../badge/<label>-<message>-<color>?...  (message = the date, dashes doubled)
text = re.sub(r"(badge/snapshot-)\d{4}--\d{2}--\d{2}(-)", rf"\g<1>{dashed}\g<2>", text)
text = re.sub(r"(badge/verified-)\d{4}--\d{2}--\d{2}(-)", rf"\g<1>{dashed}\g<2>", text)
# Alt text (plain ISO date)
text = re.sub(r'(alt="snapshot )\d{4}-\d{2}-\d{2}(")', rf"\g<1>{newest}\g<2>", text)
text = re.sub(r'(alt="last verified )\d{4}-\d{2}-\d{2}(")', rf"\g<1>{newest}\g<2>", text)

if text != original:
    README.write_text(text, encoding="utf-8")
    print(f"update_badges: README badges set to {newest}")
else:
    print(f"update_badges: README badges already at {newest}")
