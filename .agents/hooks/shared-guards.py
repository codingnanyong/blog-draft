"""Tool-neutral guard checks shared by every enforcement point.

Each check returns None (allow) or a (decision, reason) pair, where decision is
"deny" (never allowed) or "ask" (allowed only with the user's confirmation).
Adapters translate these into their host's protocol:

- claude-guard.py     Claude Code PreToolUse hooks (.claude/settings.json)
- shared-git-hook.py  git pre-commit / pre-push for any agent or human (.agents/hooks/git/)
"""

from __future__ import annotations

import re
import shlex
import subprocess
from pathlib import Path

PROTECTED_BRANCHES = {"main", "develop"}
LOWER_DEX = re.compile(r"\bNo\.\s?\d{3}\b")
PUBLISHED = re.compile(r"^status:\s*published\s*$", re.MULTILINE)
ENV_FILE = re.compile(r"(^|[\\/])\.env(\.[^\\/]*)?$")


def _is_env_file(path: str) -> bool:
    return bool(ENV_FILE.search(path)) and not path.endswith(".example")


# --- shell commands -------------------------------------------------------


def _branch(cwd: str | None) -> str:
    try:
        return subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            cwd=cwd or None,
            capture_output=True,
            text=True,
            timeout=5,
        ).stdout.strip()
    except Exception:
        return ""


def _segments(command: str) -> list[list[str]]:
    result = []
    for part in re.split(r"&&|\|\||[;|\n]", command):
        try:
            tokens = shlex.split(part, posix=True)
        except ValueError:
            tokens = part.split()
        while tokens and re.match(r"^[A-Za-z_][A-Za-z0-9_]*=", tokens[0]):
            tokens.pop(0)
        if tokens:
            result.append(tokens)
    return result


def check_push(args: list[str], cwd: str | None):
    flags = [a for a in args if a.startswith("-")]
    if any(f in {"-f", "--mirror", "--delete", "-d"} or f.startswith("--force") for f in flags):
        return "deny", "Force, delete, and mirror pushes are the user's to run; agents never rewrite remote history or tags."
    refs = [a for a in args[1:] if not a.startswith("-")]
    targets = [r.split(":")[-1].lstrip("+").removeprefix("refs/heads/") for r in refs[1:]] or [_branch(cwd)]
    if any(t in PROTECTED_BRANCHES for t in targets):
        return "deny", "develop and main change only through PRs (feat/* → develop → main). Push a feat/* branch instead."
    if "--tags" in flags or any(r.startswith(("refs/tags/", "codigdex-")) for r in refs):
        return "ask", "Pushing a tag publishes a release point. Confirm with the user."
    return "ask", "Pushing a feat/* branch creates the Linear/GitHub issue pair and a Draft PR. Push only with the user's go-ahead."


def check_command(command: str, cwd: str | None = None):
    for tokens in _segments(command):
        if tokens[0] == "cd" and len(tokens) > 1:
            cwd = str(Path(cwd or ".") / tokens[1])
            continue
        if tokens[0] == "git":
            args = tokens[1:]
            while args and args[0].startswith("-"):
                if args[0] == "-C" and len(args) > 1:
                    cwd = str(Path(cwd or ".") / args[1])
                args = args[2:] if args[0] in {"-C", "-c"} else args[1:]
            if not args:
                continue
            sub = args[0]
            if "--no-verify" in args or (sub == "commit" and "-n" in args):
                return "deny", "Do not skip git hooks (--no-verify); fix what the hook reported."
            if sub == "push":
                return check_push(args, cwd)
            if sub == "add" and any(_is_env_file(a) for a in args[1:]):
                return "deny", ".env holds API keys and must never be committed."
            if sub == "tag" and any(a in {"-f", "--force", "-d", "--delete"} for a in args[1:]):
                return "ask", "Moving or deleting a release tag changes a published release point. Confirm with the user."
        if tokens[:3] == ["gh", "pr", "merge"]:
            return "ask", "Merging is the user's decision. Confirm before merging a PR."
        if tokens[:2] == ["gh", "release"] and len(tokens) > 2 and tokens[2] in {"create", "edit", "delete", "upload"}:
            return "ask", "Releases are public records. Confirm with the user."
    return None


# --- file changes ---------------------------------------------------------


def check_file_change(rel: str, new_text: str, old_text: str, *, overwrites_existing: bool):
    """rel is the repo-relative POSIX path of a file being created or modified."""
    if _is_env_file(rel):
        return "deny", ".env files hold local secrets and never go through an agent or a commit."
    if rel.startswith("posts/") and "/images/" in rel and overwrites_existing:
        return "deny", f"{rel} already exists. Never overwrite an approved image; save a versioned sibling such as .v2.png."
    if not rel.endswith(".md"):
        return None
    if rel.startswith(("posts/", "templates/", "docs/")):
        added = sorted(set(LOWER_DEX.findall(new_text)) - set(LOWER_DEX.findall(old_text)))
        if added:
            return "deny", f"Write dex numbers uppercase (NO.001); found {added}. No.001 renders oddly on Velog/Medium."
    if re.match(r"posts/.+/index\.[a-z]{2}\.md$", rel) and PUBLISHED.search(new_text) and not PUBLISHED.search(old_text):
        return "ask", "Switching a post to status: published is only for posts the user has reported live on Velog/Medium."
    return None
