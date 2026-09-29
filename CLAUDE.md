# blog-draft

Content pipeline for **codingnanyong**'s weekly technical blog, the **코딩 도감 / Codigdex** series. Drafts are written in Markdown here, reviewed by the user, and published every Monday to Velog (Korean) and Medium (English).

```text
주제 선정 (topic — user)
   → 초안 작성 (draft — Claude)                  ← skill: weekly-post, weekly-images
   → 사용자 검토 & 피드백 반영 (review — user, Claude revises)
   → GitHub 반영 (feat branch → Draft PR)        ← push only with the user's go-ahead
   → PR 병합 (develop → main)                    ← the user merges
   → Velog/Medium 발행 & 로그 업데이트 (user)    ← skill: publish-followup
```

The user decides when anything moves forward. Claude drafts, revises, and prepares; pushes, merges, tag moves, and publishing wait for the user.

## Where things live

| Folder | What | Loaded |
| --- | --- | --- |
| `.claude/rules/` | One topic per file: `authority`, `series-voice`, `post-files`, `images`, `git-pr-policy`, `tracking` | Automatically; path-scoped ones when matching files are touched |
| `.claude/skills/` | Procedures: `weekly-post`, `weekly-images`, `publish-followup`, `chapter-release` | On demand |
| `.claude/hooks/` | Hard guards wired in `.claude/settings.json`: no direct push to `develop`/`main`, no force push, no committing `.env`, confirm push/merge/release; no overwriting images, `NO.001` casing, confirm `status: published` | Every tool call |
| `.claude/agents/` | Long-output work: `post-checker` (one post folder), `tracker-auditor` (Git vs Linear vs Notion) | Delegated |
| `docs/kor`, `docs/eng` | Human-facing docs: `WORKFLOW`, `GIT_WORKFLOW`, `ROADMAP`, `PROJECT_STRUCTURE` | Read when needed |
| `AGENTS.md` | Entry point for Codex, which doesn't load `.claude/`; it points to the same rule files | Codex only |

When a rule changes, edit the file in `.claude/rules/` (and the docs if it's user-facing). Don't restate it here or in `AGENTS.md`.

## Frequent commands

```bash
# Tracker state (blog-only Linear issues + Notion sprints); needs .env
python .claude/skills/publish-followup/scripts/tracker.py status
# After the user reports week N published (parent issue COD-<n>)
python .claude/skills/publish-followup/scripts/tracker.py publish COD-<n> <N>

# Branch/PR state
git fetch --prune && git branch -a -vv
gh pr list --state open
git log --oneline origin/main..origin/develop     # anything waiting for a main sync?

# Post folders start with '#', so quote them
ls "posts/2026/09/#005_collaboration-workflow/images"
```

`.env` (gitignored) holds `LINEAR_API_KEY`, `NOTION_API_KEY`, `GH_PAT`, `SLACK_WEBHOOK_URL`, and more; never print or commit it.
