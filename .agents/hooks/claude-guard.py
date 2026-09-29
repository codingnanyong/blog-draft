"""Claude Code PreToolUse adapter for shared-guards.py.

Wired in .claude/settings.json:
  sh .agents/hooks/shared-run.sh claude-guard bash   (matcher: Bash)
  sh .agents/hooks/shared-run.sh claude-guard edit   (matcher: Write|Edit|MultiEdit)
"""

from __future__ import annotations

import json
import importlib.util
import os
import sys
from pathlib import Path

_GUARDS_PATH = Path(__file__).with_name("shared-guards.py")
_SPEC = importlib.util.spec_from_file_location("shared_guards", _GUARDS_PATH)
if _SPEC is None or _SPEC.loader is None:
    raise ImportError(f"Cannot load shared guards from {_GUARDS_PATH}")
guards = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(guards)


def emit(result) -> None:
    if result:
        decision, reason = result
        print(
            json.dumps(
                {
                    "hookSpecificOutput": {
                        "hookEventName": "PreToolUse",
                        "permissionDecision": decision,
                        "permissionDecisionReason": reason,
                    }
                },
                ensure_ascii=False,
            )
        )
    sys.exit(0)


def on_bash(payload: dict) -> None:
    command = (payload.get("tool_input") or {}).get("command", "")
    emit(guards.check_command(command, payload.get("cwd")))


def on_edit(payload: dict) -> None:
    tool = payload.get("tool_name", "")
    tool_input = payload.get("tool_input") or {}
    raw_path = tool_input.get("file_path") or ""
    if not raw_path:
        emit(None)
    path = Path(raw_path)
    root = Path(os.environ.get("CLAUDE_PROJECT_DIR") or payload.get("cwd") or ".")
    try:
        rel = path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        emit(None)

    if tool == "Write":
        new_text = tool_input.get("content") or ""
        old_text = path.read_text(encoding="utf-8", errors="replace") if path.exists() and rel.endswith(".md") else ""
    elif tool == "Edit":
        new_text = tool_input.get("new_string") or ""
        old_text = tool_input.get("old_string") or ""
    else:
        edits = tool_input.get("edits") or []
        new_text = "\n".join(e.get("new_string") or "" for e in edits)
        old_text = "\n".join(e.get("old_string") or "" for e in edits)
    emit(guards.check_file_change(rel, new_text, old_text, overwrites_existing=tool == "Write" and path.exists()))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    payload = json.load(sys.stdin)
    {"bash": on_bash, "edit": on_edit}[sys.argv[1]](payload)
