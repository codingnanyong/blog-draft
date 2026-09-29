"""git pre-commit / pre-push adapter for shared-guards.py.

Applies to every committer (Claude, Codex, any other agent, and humans) once
The hook installer points core.hooksPath at
.agents/hooks/git. Git cannot prompt, so only "deny" results block here. A human
can bypass a deliberate exception with --no-verify; agents are denied that flag
by their own adapters and by .agents/rules/shared-authority.md.
"""

from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path

_GUARDS_PATH = Path(__file__).with_name("shared-guards.py")
_SPEC = importlib.util.spec_from_file_location("shared_guards", _GUARDS_PATH)
if _SPEC is None or _SPEC.loader is None:
    raise ImportError(f"Cannot load shared guards from {_GUARDS_PATH}")
guards = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(guards)

ZERO = "0" * 40


def git(*args: str) -> str:
    return subprocess.run(["git", *args], capture_output=True, text=True, encoding="utf-8").stdout


def pre_commit() -> list[str]:
    problems = []
    for line in git("diff", "--cached", "--name-status", "--no-renames").splitlines():
        status, _, rel = line.partition("\t")
        if status.startswith("D"):
            continue
        is_md = rel.endswith(".md")
        new_text = git("show", f":{rel}") if is_md else ""
        old_text = git("show", f"HEAD:{rel}") if is_md and status.startswith("M") else ""
        result = guards.check_file_change(rel, new_text, old_text, overwrites_existing=status.startswith("M"))
        if result and result[0] == "deny":
            problems.append(f"{rel}: {result[1]}")
    return problems


def pre_push() -> list[str]:
    problems = []
    for line in sys.stdin.read().splitlines():
        _local_ref, local_sha, remote_ref, remote_sha = line.split()
        if not remote_ref.startswith("refs/heads/"):
            continue  # tags are released by the user by hand
        branch = remote_ref.removeprefix("refs/heads/")
        if branch in guards.PROTECTED_BRANCHES:
            problems.append(f"{branch}: changes only through PRs (feat/* → develop → main).")
        elif local_sha != ZERO and remote_sha != ZERO:
            ancestor = subprocess.run(["git", "merge-base", "--is-ancestor", remote_sha, local_sha])
            if ancestor.returncode != 0:
                problems.append(f"{branch}: non-fast-forward (force) push rewrites shared history.")
    return problems


if __name__ == "__main__":
    stage = sys.argv[1]
    problems = pre_commit() if stage == "pre-commit" else pre_push()
    if problems:
        print(f"[{stage}] blocked by .agents/hooks:", file=sys.stderr)
        for problem in problems:
            print(f"  - {problem}", file=sys.stderr)
        sys.exit(1)
