#!/usr/bin/env bash
# refresh.sh - drive headless Claude Code to re-verify stale reference files.
#
# Produces review patches in updates/<date>/. Never edits references/ directly.
# Merging is a human step; see --help.

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REFS="$ROOT/references"
PROMPT="$ROOT/prompts/refresh.md"
TODAY="$(date +%F)"
OUTDIR="$ROOT/updates/$TODAY"
MODEL="${REFRESH_MODEL:-opus}"
TARGETS=()
MODE="stale"

usage() {
  cat <<'EOF'
refresh.sh - re-verify reference files against live sources.

  ./scripts/refresh.sh              refresh files the gate reports as stale
  ./scripts/refresh.sh --all        refresh every reference file
  ./scripts/refresh.sh --file X.md  refresh one file
  ./scripts/refresh.sh --dry-run    show what would run, run nothing

Env:
  REFRESH_MODEL   model alias passed to claude -p (default: opus)

Output lands in updates/<date>/<name>.patch.md. Nothing under references/ is
touched. To merge a patch:

  1. Read the patch. Check that every `now:` line has a working source URL.
  2. Apply the changes you accept, by hand or with Claude Code in the repo.
  3. Bump `last_verified` in that file's frontmatter to today.
  4. Run scripts/check_refs.py to confirm the gate passes.

Step 3 is the one that is easy to forget and silently defeats the whole loop.
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --all)     MODE="all"; shift ;;
    --file)    MODE="one"; TARGETS+=("$2"); shift 2 ;;
    --dry-run) MODE="dry"; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "unknown arg: $1" >&2; usage; exit 2 ;;
  esac
done

command -v claude >/dev/null 2>&1 || {
  echo "error: 'claude' not on PATH. Install Claude Code first." >&2; exit 2; }
command -v python3 >/dev/null 2>&1 || {
  echo "error: python3 required." >&2; exit 2; }

# Resolve the target list.
if [[ "$MODE" == "stale" || "$MODE" == "dry" ]]; then
  mapfile -t TARGETS < <(
    python3 "$ROOT/scripts/check_refs.py" --root "$ROOT" --json \
      | python3 -c 'import json,sys; print("\n".join(json.load(sys.stdin)["stale_files"]))'
  )
elif [[ "$MODE" == "all" ]]; then
  mapfile -t TARGETS < <(cd "$REFS" && ls *.md)
fi

if [[ ${#TARGETS[@]} -eq 0 ]]; then
  echo "nothing stale. gate is green."
  exit 0
fi

echo "targets (${#TARGETS[@]}): ${TARGETS[*]}"
[[ "$MODE" == "dry" ]] && { echo "(dry run, stopping)"; exit 0; }

mkdir -p "$OUTDIR"

for name in "${TARGETS[@]}"; do
  target="$REFS/$name"
  [[ -f "$target" ]] || { echo "skip, no such file: $name" >&2; continue; }

  last_verified="$(sed -n 's/^last_verified: *//p' "$target" | head -1)"
  out="$OUTDIR/${name%.md}.patch.md"

  echo "--> $name (last verified ${last_verified:-unknown})"

  task="$(sed \
    -e "s|{{TARGET_PATH}}|$target|g" \
    -e "s|{{TARGET_NAME}}|$name|g" \
    -e "s|{{LAST_VERIFIED}}|${last_verified:-unknown}|g" \
    -e "s|{{TODAY}}|$TODAY|g" \
    "$PROMPT")"

  # Claude prints the patch to stdout; stderr goes to the log.
  # Write tool excluded — no file-write permission needed.
  if claude -p "$task" \
      --model "$MODEL" \
      --allowedTools "WebSearch,WebFetch,Read" \
      --permission-mode bypassPermissions \
      > "$out" 2>"$OUTDIR/${name%.md}.log"; then
    if [[ -s "$out" ]]; then
      verdict="$(sed -n 's/^verdict: *//p' "$out" | head -1)"
      echo "    ${verdict:-NO_VERDICT} -> $out"
    else
      echo "    empty response (see ${name%.md}.log)" >&2
      rm -f "$out"
    fi
  else
    echo "    run failed (see ${name%.md}.log)" >&2
    rm -f "$out"
  fi
done

echo
echo "patches in $OUTDIR"
echo "review, merge what you accept, bump last_verified, then:"
echo "  python3 scripts/check_refs.py"
