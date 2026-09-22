#!/usr/bin/env python3
"""
check_refs.py - deterministic gate for the claude-code-ecosystem reference bundle.

Stdlib only. No network. No API calls. Safe to run in CI or a pre-commit hook.

Checks:
  FM01  frontmatter present and parseable
  FM02  required keys present
  FM03  last_verified is a valid ISO date, not in the future
  ST01  file is within its verify_horizon_days
  RT01  file appears in the SKILL.md routing table (no orphans)
  TG01  quantitative claims carry a confidence tag  (warning)

Exit codes:
  0  all checks pass
  1  one or more failures (or warnings when --strict)
  2  usage / unreadable bundle

Usage:
  python3 scripts/check_refs.py
  python3 scripts/check_refs.py --json
  python3 scripts/check_refs.py --strict
  python3 scripts/check_refs.py --root /path/to/claude-code-ecosystem
"""

import argparse
import datetime as dt
import json
import pathlib
import re
import sys

REQUIRED_KEYS = ("last_verified", "volatility", "verify_horizon_days")
VALID_VOLATILITY = {"high", "medium", "low"}
TAGS = ("[VERIFIED]", "[REPORTED]", "[VENDOR]", "[DISPUTED]", "[VOLATILE]")

# Lines carrying a number that a reader would act on.
CLAIM_PATTERNS = (
    re.compile(r"\d+(\.\d+)?\s*%"),          # percentages
    re.compile(r"\$\d"),                      # money
    re.compile(r"\b\d+(\.\d+)?[km]\b\s*(stars|installs|users)", re.I),
    re.compile(r"\bv?\d+\.\d+\.\d+\b"),      # versions
    re.compile(r"\b20\d{2}-\d{2}-\d{2}\b"),  # ISO dates
)
SUPPRESS = "<!-- notag -->"
WARN_FRACTION = 0.8  # warn once past 80% of the horizon


def parse_frontmatter(text):
    """Minimal YAML subset: key: value, and `key:` followed by `  - item` lists."""
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    raw = text[4:end]
    body = text[end + 5:]
    data, current_list = {}, None
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith((" ", "\t")) and line.lstrip().startswith("- "):
            if current_list is not None:
                data[current_list].append(line.lstrip()[2:].strip())
            continue
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        key, val = key.strip(), val.strip()
        if val == "":
            data[key], current_list = [], key
        else:
            data[key], current_list = val, None
    return data, body


def iter_claim_lines(body):
    """Yield (lineno, text) for claim-bearing lines outside fenced code blocks."""
    in_fence = False
    for i, line in enumerate(body.splitlines(), start=1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence or SUPPRESS in line:
            continue
        if any(p.search(line) for p in CLAIM_PATTERNS):
            yield i, line


def check(root, today):
    refs_dir = root / "references"
    skill_md = root / "SKILL.md"
    if not refs_dir.is_dir() or not skill_md.is_file():
        print(f"error: not a reference bundle: {root}", file=sys.stderr)
        sys.exit(2)

    routing = skill_md.read_text()
    results = []

    for path in sorted(refs_dir.glob("*.md")):
        name = path.name
        entry = {"file": name, "failures": [], "warnings": [], "days_since": None,
                 "horizon": None, "volatility": None}
        text = path.read_text()
        fm, body = parse_frontmatter(text)

        if fm is None:
            entry["failures"].append("FM01 missing or unparseable frontmatter")
            results.append(entry)
            continue

        missing = [k for k in REQUIRED_KEYS if k not in fm]
        if missing:
            entry["failures"].append(f"FM02 missing keys: {', '.join(missing)}")

        if fm.get("volatility") not in VALID_VOLATILITY:
            entry["failures"].append(
                f"FM02 volatility must be one of {sorted(VALID_VOLATILITY)}, "
                f"got {fm.get('volatility')!r}")
        entry["volatility"] = fm.get("volatility")

        verified = None
        if "last_verified" in fm:
            try:
                verified = dt.date.fromisoformat(str(fm["last_verified"]))
            except ValueError:
                entry["failures"].append(
                    f"FM03 last_verified not ISO date: {fm['last_verified']!r}")
            else:
                if verified > today:
                    entry["failures"].append(
                        f"FM03 last_verified is in the future: {verified}")

        horizon = None
        if "verify_horizon_days" in fm:
            try:
                horizon = int(fm["verify_horizon_days"])
            except (TypeError, ValueError):
                entry["failures"].append("FM02 verify_horizon_days not an integer")
        entry["horizon"] = horizon

        if verified and horizon:
            days = (today - verified).days
            entry["days_since"] = days
            if days > horizon:
                entry["failures"].append(
                    f"ST01 stale: {days}d since verification, horizon {horizon}d "
                    f"(over by {days - horizon}d)")
            elif days >= horizon * WARN_FRACTION:
                entry["warnings"].append(
                    f"ST01 approaching horizon: {days}/{horizon}d")

        if name not in routing:
            entry["failures"].append("RT01 not referenced in SKILL.md routing table")

        untagged = [(n, ln.strip()[:70]) for n, ln in iter_claim_lines(body)
                    if not any(t in ln for t in TAGS)]
        for lineno, snippet in untagged:
            entry["warnings"].append(f"TG01 L{lineno} untagged claim: {snippet}")

        results.append(entry)

    return results


def main():
    ap = argparse.ArgumentParser(description="Gate the reference bundle.")
    ap.add_argument("--root", default=str(pathlib.Path(__file__).resolve().parent.parent),
                    help="bundle root (default: parent of scripts/)")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--strict", action="store_true", help="treat warnings as failures")
    ap.add_argument("--quiet", action="store_true", help="only print failures")
    ap.add_argument("--today", help="override today's date (ISO) for testing")
    args = ap.parse_args()

    today = dt.date.fromisoformat(args.today) if args.today else dt.date.today()
    results = check(pathlib.Path(args.root), today)

    n_fail = sum(len(r["failures"]) for r in results)
    n_warn = sum(len(r["warnings"]) for r in results)
    stale = [r["file"] for r in results
             if any(f.startswith("ST01 stale") for f in r["failures"])]

    if args.json:
        print(json.dumps({
            "checked_at": today.isoformat(),
            "files": results,
            "stale_files": stale,
            "failures": n_fail,
            "warnings": n_warn,
        }, indent=2))
    else:
        for r in results:
            if args.quiet and not r["failures"]:
                continue
            age = (f"{r['days_since']}/{r['horizon']}d"
                   if r["days_since"] is not None else "?")
            status = "FAIL" if r["failures"] else ("WARN" if r["warnings"] else "ok")
            print(f"[{status:4}] {r['file']:34} {str(r['volatility'] or '?'):6} {age}")
            for f in r["failures"]:
                print(f"         ! {f}")
            if not args.quiet:
                for w in r["warnings"]:
                    print(f"         ~ {w}")
        print(f"\n{len(results)} files | {n_fail} failures | {n_warn} warnings")
        if stale:
            print(f"stale: {', '.join(stale)}")
            print("run: scripts/refresh.sh")

    if n_fail or (args.strict and n_warn):
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
