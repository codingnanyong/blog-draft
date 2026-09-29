# blog-draft

Content pipeline for **codingnanyong**'s weekly technical blog, the **코딩 도감 / Codigdex** series. Drafts are written in Markdown here, reviewed by the user, and published every Monday to Velog (Korean) and Medium (English).

```text
주제 선정 (topic — user)
   → 초안 작성 (draft — Claude)                  ← skill: shared-weekly-post, shared-weekly-images
   → 사용자 검토 & 피드백 반영 (review — user, Claude revises)
   → GitHub 반영 (feat branch → Draft PR)        ← push only with the user's go-ahead
   → PR 병합 (develop → main)                    ← the user merges
   → Velog/Medium 발행 & 로그 업데이트 (user)    ← skill: shared-publish-followup
```

The user decides when anything moves forward. Claude drafts, revises, and prepares; pushes, merges, tag moves, and publishing wait for the user.

## Where things live

| Folder | What | Loaded |
| --- | --- | --- |
| `.agents/rules/` | Shared rules: `shared-authority`, `shared-series-voice`, `shared-post-files`, `shared-images`, `shared-git-pr-policy`, `shared-tracking` | Read before matching work |
| `.agents/skills/` | Shared procedures: `shared-weekly-post`, `shared-weekly-images`, `shared-publish-followup`, `shared-chapter-release` | On demand |
| `.agents/hooks/` | Shared guards wired in `.claude/settings.json`; the Claude adapter uses the `claude-` prefix | Every tool call |
| `.agents/agents/` | Claude subagents: `claude-post-checker`, `claude-tracker-auditor` | Delegated |
| `docs/kor`, `docs/eng` | Human-facing docs: `WORKFLOW`, `GIT_WORKFLOW`, `ROADMAP`, `PROJECT_STRUCTURE` | Read when needed |
| `AGENTS.md` | Shared entry point that points Codex and other agents to the same rule files | Codex and other agents |

Name shared support assets with `shared-` by default. Use `claude-` or `codex-` only for agent-specific assets. Keep required names such as `README.md` and `SKILL.md` unchanged.

When a rule changes, edit the file in `.agents/rules/` (and the docs if it's user-facing). Don't restate the rule content here or in `AGENTS.md`.

## Frequent commands

```bash
# Tracker state (blog-only Linear issues + Notion sprints); needs .env
python .agents/skills/shared-publish-followup/scripts/shared-tracker.py status
# After the user reports week N published (parent issue COD-<n>)
python .agents/skills/shared-publish-followup/scripts/shared-tracker.py publish COD-<n> <N>

# Branch/PR state
git fetch --prune && git branch -a -vv
gh pr list --state open
git log --oneline origin/main..origin/develop     # anything waiting for a main sync?

# Post folders start with '#', so quote them
ls "posts/2026/09/#005_collaboration-workflow/images"
```

`.env` (gitignored) holds `LINEAR_API_KEY`, `NOTION_API_KEY`, `GH_PAT`, `SLACK_WEBHOOK_URL`, and more; never print or commit it.
