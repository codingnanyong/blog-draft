"""Blog tracker helper for Linear (project 블로그 자동발행) and the Notion Sprint Tracker.

Usage (from the repo root, which holds .env):
  python .claude/skills/publish-followup/scripts/tracker.py status
  python .claude/skills/publish-followup/scripts/tracker.py publish COD-55 5

`status` lists open blog Linear issues and the blog Notion sprint rows.
`publish <parent> <sprint>` marks the week's publish sub-issue and its parent Done,
and sets Notion "Sprint 0<sprint>" to Completed / 100%.
"""

from __future__ import annotations

import json
import sys
import urllib.request
from pathlib import Path

PROJECT = "블로그 자동발행"
SPRINT_DB = "72756ff399a8827694c20166e4c780e8"
PUBLISH_SUBISSUE = "Velog·Medium 발행"


def load_env() -> dict[str, str]:
    env = {}
    for line in Path(".env").read_text(encoding="utf-8").splitlines():
        if "=" in line and not line.lstrip().startswith("#"):
            key, value = line.split("=", 1)
            env[key.strip()] = value.strip().strip('"')
    return env


ENV = load_env()


def linear(query: str, variables: dict | None = None) -> dict:
    request = urllib.request.Request(
        "https://api.linear.app/graphql",
        json.dumps({"query": query, "variables": variables or {}}).encode(),
        {"Content-Type": "application/json", "Authorization": ENV["LINEAR_API_KEY"]},
    )
    body = json.load(urllib.request.urlopen(request, timeout=30))
    if body.get("errors"):
        raise SystemExit(f"Linear API errors: {body['errors']}")
    return body["data"]


def notion(method: str, path: str, payload: dict | None = None) -> dict:
    request = urllib.request.Request(
        f"https://api.notion.com/v1/{path}",
        json.dumps(payload).encode() if payload else None,
        {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {ENV['NOTION_API_KEY']}",
            "Notion-Version": "2022-06-28",
        },
        method=method,
    )
    return json.load(urllib.request.urlopen(request, timeout=30))


def sprint_rows() -> list[dict]:
    rows = notion(
        "POST",
        f"databases/{SPRINT_DB}/query",
        {"filter": {"property": "Project", "rich_text": {"contains": PROJECT}}},
    )["results"]
    result = []
    for row in rows:
        props = row["properties"]
        title = "".join(
            part["plain_text"]
            for prop in props.values()
            if prop["type"] == "title"
            for part in prop["title"]
        )
        status = (props["Status"]["select"] or {}).get("name")
        result.append({"id": row["id"], "title": title, "status": status, "pct": props["Completion %"]["number"]})
    return sorted(result, key=lambda row: row["title"])


def status() -> None:
    issues = linear(
        """query($p: String!) { issues(first: 100, filter: {
             project: { name: { eq: $p } }, state: { type: { nin: ["completed", "canceled"] } } }) {
             nodes { identifier title state { name } cycle { number } parent { identifier } } } }""",
        {"p": PROJECT},
    )["issues"]["nodes"]
    print(f"Linear open issues in {PROJECT}: {len(issues)}")
    for issue in sorted(issues, key=lambda i: int(i["identifier"].split("-")[1])):
        parent = (issue["parent"] or {}).get("identifier") or "-"
        cycle = (issue["cycle"] or {}).get("number")
        print(f"  {issue['identifier']:8} {issue['state']['name']:12} cycle={cycle} parent={parent}  {issue['title']}")
    print("Notion sprints:")
    for row in sprint_rows():
        print(f"  {row['status'] or '-':12} {row['pct']}  {row['title']}")


def publish(parent_id: str, sprint: int) -> None:
    states = linear('{ teams(filter: { key: { eq: "COD" } }) { nodes { states { nodes { id name } } } } }')
    done = next(s["id"] for s in states["teams"]["nodes"][0]["states"]["nodes"] if s["name"] == "Done")
    parent = linear(
        """query($id: String!) { issue(id: $id) { identifier title
             children(includeArchived: true) { nodes { identifier title } } } }""",
        {"id": parent_id},
    )["issue"]
    targets = [c["identifier"] for c in parent["children"]["nodes"] if PUBLISH_SUBISSUE in c["title"]]
    if not targets:
        raise SystemExit(f"{parent_id} has no '{PUBLISH_SUBISSUE}' sub-issue")
    for identifier in [*targets, parent_id]:
        issue = linear(
            """mutation($id: String!, $s: String!) { issueUpdate(id: $id, input: { stateId: $s }) {
                 issue { identifier state { name } } } }""",
            {"id": identifier, "s": done},
        )["issueUpdate"]["issue"]
        print(f"Linear {issue['identifier']} -> {issue['state']['name']}")

    label = f"Sprint {sprint:02d}"
    rows = [row for row in sprint_rows() if label in row["title"]]
    if len(rows) != 1:
        raise SystemExit(f"Expected one Notion row for {label}, found {[r['title'] for r in rows]}")
    notion(
        "PATCH",
        f"pages/{rows[0]['id']}",
        {"properties": {"Status": {"select": {"name": "Completed"}}, "Completion %": {"number": 1}}},
    )
    print(f"Notion {rows[0]['title']} -> Completed / 100%")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    if sys.argv[1:2] == ["status"]:
        status()
    elif sys.argv[1:2] == ["publish"] and len(sys.argv) == 4:
        publish(sys.argv[2].upper(), int(sys.argv[3]))
    else:
        raise SystemExit(__doc__)
