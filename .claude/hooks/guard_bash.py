"""PreToolUse(Bash) guard for git/gh commands that must not run unchecked.

deny: pushing to develop/main directly, force pushes, committing .env, skipping hooks.
ask:  pushing a feature branch (it creates the issue pair and Draft PR), merging PRs,
      creating/editing releases, moving or deleting tags.
"""

from __future__ import annotations

import json
import re
import shlex
import subprocess
import sys

PROTECTED = {"main", "develop"}


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


def current_branch(cwd: str | None) -> str:
    try:
        return subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=5,
        ).stdout.strip()
    except Exception:
        return ""


def segments(command: str) -> list[list[str]]:
    parts = re.split(r"&&|\|\||[;|\n]", command)
    result = []
    for part in parts:
        try:
            tokens = shlex.split(part, posix=True)
        except ValueError:
            tokens = part.split()
        # Drop leading env assignments such as GIT_TRACE=1.
        while tokens and re.match(r"^[A-Za-z_][A-Za-z0-9_]*=", tokens[0]):
            tokens.pop(0)
        if tokens:
            result.append(tokens)
    return result


def git_args(tokens: list[str]) -> list[str] | None:
    if not tokens or tokens[0] != "git":
        return None
    args = tokens[1:]
    # Skip global options like -C <dir> or -c key=value.
    while args and args[0].startswith("-"):
        args = args[2:] if args[0] in {"-C", "-c"} else args[1:]
    return args


def check_push(args: list[str], cwd: str | None) -> None:
    flags = [a for a in args if a.startswith("-")]
    if any(f in {"-f", "--force", "--force-with-lease", "--mirror", "--delete", "-d"} or f.startswith("--force") for f in flags):
        decide("deny", "Force/delete/mirror pushes are the user's to run (tags and history are never moved by an agent).")
    refs = [a for a in args[1:] if not a.startswith("-")]
    targets = [ref.split(":")[-1].removeprefix("+").removeprefix("refs/heads/") for ref in refs[1:]]
    if not refs[1:]:
        targets = [current_branch(cwd)]
    if any(target in PROTECTED for target in targets):
        decide("deny", "develop and main change only through PRs (feat/* → develop → main). Push a feat/* branch instead.")
    if "--tags" in flags or any(ref.startswith("refs/tags/") or ref.startswith("codigdex-") for ref in refs):
        decide("ask", "Pushing tags publishes a chapter release point. Confirm with the user.")
    decide("ask", "Pushing a feat/* branch creates the Linear/GitHub issue pair and a Draft PR. Push only with the user's go-ahead.")


def main() -> None:
    payload = json.load(sys.stdin)
    command = (payload.get("tool_input") or {}).get("command", "")
    cwd = payload.get("cwd")

    for tokens in segments(command):
        args = git_args(tokens)
        if args is not None and args:
            sub = args[0]
            if sub == "push":
                check_push(args, cwd)
            if sub in {"commit", "push", "merge", "rebase"} and "--no-verify" in args:
                decide("deny", "Do not skip git hooks (--no-verify); fix the underlying failure.")
            if sub == "add" and any(re.search(r"(^|/)\.env(\.[^/]*)?$", a) and not a.endswith(".example") for a in args[1:]):
                decide("deny", ".env holds API keys and must never be committed.")
            if sub == "tag" and any(a in {"-f", "--force", "-d", "--delete"} for a in args[1:]):
                decide("ask", "Moving or deleting a chapter tag changes a published release point. Confirm with the user.")
        if tokens[:2] == ["gh", "pr"] and len(tokens) > 2 and tokens[2] == "merge":
            decide("ask", "Merging is the user's decision. Confirm before merging a PR.")
        if tokens[:2] == ["gh", "release"] and len(tokens) > 2 and tokens[2] in {"create", "edit", "delete", "upload"}:
            decide("ask", "Releases are public chapter records. Confirm with the user.")
    sys.exit(0)


if __name__ == "__main__":
    main()
