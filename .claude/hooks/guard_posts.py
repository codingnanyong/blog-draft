"""PreToolUse(Write|Edit|MultiEdit) guard for post files.

deny: overwriting an existing image under posts/**/images/ (save a .v2 sibling instead);
      writing lowercase dex numbers (No.001) into Markdown (use NO.001).
ask:  switching a post to `status: published` (only after the user reports it is live).
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

LOWER_DEX = re.compile(r"\bNo\.\s?\d{3}\b")
PUBLISHED = re.compile(r"^status:\s*published\s*$", re.MULTILINE)


def decide(decision: str, reason: str) -> None:
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


def main() -> None:
    payload = json.load(sys.stdin)
    tool = payload.get("tool_name", "")
    tool_input = payload.get("tool_input") or {}
    raw_path = tool_input.get("file_path") or ""
    if not raw_path:
        sys.exit(0)

    path = Path(raw_path)
    root = Path(os.environ.get("CLAUDE_PROJECT_DIR") or payload.get("cwd") or ".")
    try:
        rel = path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        sys.exit(0)

    if rel.startswith("posts/") and "/images/" in rel and tool == "Write" and path.exists():
        decide("deny", f"{rel} already exists. Never overwrite an approved image; save a versioned sibling such as .v2.png.")

    if not rel.endswith(".md"):
        sys.exit(0)

    if tool == "Write":
        new_texts = [tool_input.get("content") or ""]
        old_texts = [path.read_text(encoding="utf-8", errors="replace")] if path.exists() else [""]
    elif tool == "Edit":
        new_texts = [tool_input.get("new_string") or ""]
        old_texts = [tool_input.get("old_string") or ""]
    else:
        edits = tool_input.get("edits") or []
        new_texts = [e.get("new_string") or "" for e in edits]
        old_texts = [e.get("old_string") or "" for e in edits]
    new_text = "\n".join(new_texts)
    old_text = "\n".join(old_texts)

    if rel.startswith(("posts/", "templates/", "docs/")):
        added = set(LOWER_DEX.findall(new_text)) - set(LOWER_DEX.findall(old_text))
        if added:
            decide("deny", f"Write dex numbers uppercase (NO.001); found {sorted(added)}. No.001 renders oddly on Velog/Medium.")

    if re.match(r"posts/.+/index\.[a-z]{2}\.md$", rel) and PUBLISHED.search(new_text) and not PUBLISHED.search(old_text):
        decide("ask", "Switching a post to status: published is only for posts the user has reported live on Velog/Medium.")

    sys.exit(0)


if __name__ == "__main__":
    main()
