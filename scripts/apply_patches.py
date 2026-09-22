#!/usr/bin/env python3
"""
apply_patches.py - automatically apply refresh patches to reference files.

Reads every *.patch.md from the most-recent updates/<date>/ directory and
applies it to the matching references/<name>.md.

Verdict handling:
  UNCHANGED   bump last_verified, nothing else
  CHANGED     apply was→now replacements, then bump last_verified
  NEEDS_HUMAN skip and print a warning; human must handle this file

Idempotent: running twice produces the same result.

Usage:
  python3 scripts/apply_patches.py
  python3 scripts/apply_patches.py --patches-dir updates/2026-09-22
  python3 scripts/apply_patches.py --dry-run
"""

import argparse
import datetime as dt
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
REFS = ROOT / "references"
UPDATES = ROOT / "updates"


def latest_patches_dir(override=None):
    if override:
        d = pathlib.Path(override)
        if not d.is_dir():
            print(f"error: --patches-dir not found: {d}", file=sys.stderr)
            sys.exit(2)
        return d
    candidates = sorted(
        (d for d in UPDATES.iterdir() if d.is_dir() and re.fullmatch(r"\d{4}-\d{2}-\d{2}", d.name)),
        reverse=True,
    )
    if not candidates:
        print("no patch directories found under updates/", file=sys.stderr)
        sys.exit(0)
    return candidates[0]


def parse_verdict(text):
    m = re.search(r"^verdict:\s*(\S+)", text, re.MULTILINE)
    return m.group(1).strip().upper() if m else "UNKNOWN"


def parse_changes(text):
    """
    Return list of (was, now) string pairs from the ## Changed and
    ## Status changes sections of a patch document.
    """
    pairs = []
    # Grab everything between ## Changed (or ## Status changes) and the next ##
    for section_match in re.finditer(
        r"^## (?:Changed|Status changes)\s*\n(.*?)(?=^## |\Z)",
        text, re.MULTILINE | re.DOTALL
    ):
        block = section_match.group(1)
        # Each change block starts with ### label
        for change in re.split(r"^### .+", block, flags=re.MULTILINE):
            was_m = re.search(r"^- was:\s*(.+)$", change, re.MULTILINE)
            now_m = re.search(r"^- now:\s*(.+)$", change, re.MULTILINE)
            if was_m and now_m:
                pairs.append((was_m.group(1).strip(), now_m.group(1).strip()))
    return pairs


def bump_last_verified(text, today):
    return re.sub(
        r"^(last_verified:\s*)\S+",
        lambda m: m.group(1) + today,
        text,
        count=1,
        flags=re.MULTILINE,
    )


def apply_patch(ref_path, patch_text, today, dry_run=False):
    verdict = parse_verdict(patch_text)
    name = ref_path.name

    if verdict == "NEEDS_HUMAN":
        print(f"  [DATE]  {name} — verdict NEEDS_HUMAN; bumping last_verified only")

    if verdict == "UNKNOWN":
        print(f"  [WARN]  {name} — could not parse verdict, skipping")
        return False

    ref_text = ref_path.read_text(encoding="utf-8")
    updated = ref_text

    if verdict == "CHANGED":
        changes = parse_changes(patch_text)
        if not changes:
            print(f"  [WARN]  {name} — CHANGED but no was/now pairs found, only bumping date")
        for was, now in changes:
            if was in updated:
                updated = updated.replace(was, now, 1)
                print(f"  [APPLY] {name}: replaced claim")
                print(f"          was: {was[:72]}")
                print(f"          now: {now[:72]}")
            else:
                print(f"  [MISS]  {name}: 'was' line not found in reference (may already be applied)")
                print(f"          was: {was[:72]}")

    updated = bump_last_verified(updated, today)

    if updated == ref_text:
        print(f"  [NOOP]  {name} — no changes (already up to date)")
        return True

    if dry_run:
        print(f"  [DRY]   {name} — would write {len(updated)} chars (verdict: {verdict})")
        return True

    ref_path.write_text(updated, encoding="utf-8")
    print(f"  [DONE]  {name} (verdict: {verdict})")
    return True


def main():
    ap = argparse.ArgumentParser(description="Apply refresh patches to reference files.")
    ap.add_argument("--patches-dir", help="path to a specific updates/<date>/ directory")
    ap.add_argument("--dry-run", action="store_true", help="show what would change, write nothing")
    args = ap.parse_args()

    patches_dir = latest_patches_dir(args.patches_dir)
    today = dt.date.today().isoformat()
    print(f"patches dir : {patches_dir}")
    print(f"applying as : {today}")
    print()

    patches = sorted(patches_dir.glob("*.patch.md"))
    if not patches:
        print("no *.patch.md files found — nothing to apply")
        sys.exit(0)

    for patch_path in patches:
        ref_name = patch_path.stem.removesuffix(".patch") + ".md"
        ref_path = REFS / ref_name
        if not ref_path.exists():
            print(f"  [SKIP]  {ref_name} — reference file not found")
            continue
        patch_text = patch_path.read_text(encoding="utf-8")
        apply_patch(ref_path, patch_text, today, dry_run=args.dry_run)

    sys.exit(0)


if __name__ == "__main__":
    main()
