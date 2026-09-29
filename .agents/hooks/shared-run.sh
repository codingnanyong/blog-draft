#!/bin/sh
# Runs a .agents/hooks adapter with whichever Python 3.9+ is available.
# Usage: sh .agents/hooks/shared-run.sh <adapter> [args...]
# Example: shared-run.sh claude-guard bash
# A missing Python must not block every tool call, so it warns and exits 0.
dir=$(cd "$(dirname "$0")" && pwd)
adapter=$1
shift
if [ ! -f "$dir/$adapter.py" ]; then
  echo "shared-run.sh: $dir/$adapter.py not found; skipping" >&2
  exit 0
fi
for py in python python3; do
  if "$py" -c "import sys; sys.exit(sys.version_info < (3, 9))" >/dev/null 2>&1; then
    exec "$py" -B "$dir/$adapter.py" "$@"
  fi
done
echo "shared-run.sh: Python 3.9+ not found; skipping the $adapter guard" >&2
exit 0
