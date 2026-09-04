# Claude's Role in This Repository

This repo is a content pipeline for **codingnanyong**'s weekly technical blog: draft in Markdown here, human review, then publish to Velog (Korean) and Medium (English).

@AGENTS.md

The rules above (`AGENTS.md`) are the single source of truth for how any agent — Claude or Codex — should operate in this repo: weekly workflow steps, Codigdex series voice, image deliverables, and editing constraints. Keep that file up to date rather than duplicating its content here; this file only adds Claude-specific framing that doesn't belong in a tool-agnostic rules file.

## Where Claude fits in the pipeline

Per [docs/kor/WORKFLOW.md](docs/kor/WORKFLOW.md) / [docs/eng/WORKFLOW.md](docs/eng/WORKFLOW.md), each week is tracked in Linear as 6 sub-issues. Claude's job is step 2:

```
주제 선정 (topic selection — human)
   → 초안 작성 (draft writing — Claude)
   → 사용자 검토 & 피드백 반영 (user review & feedback — human, with Claude revising)
   → GitHub 반영 (feat branch → PR)
   → PR 병합 (develop)
   → Velog/Medium 발행 & 로그 업데이트 (publish — human, manual)
```

Branch naming and PR conventions for step 4 are in [docs/kor/GIT_WORKFLOW.md](docs/kor/GIT_WORKFLOW.md) (`feat/<slug>` → automated Draft PR → `develop` → `main`). As `AGENTS.md` states, pushing the branch (which triggers PR creation), merging, and publishing still require the user's explicit go-ahead — Claude drafts and revises, the user decides when it moves forward.

## Other AI tooling

Codex (OpenAI's CLI) is also used in this repo; it reads `AGENTS.md` directly (its cache is gitignored at `.codex-tmp/`). Claude Code does not read `AGENTS.md` automatically on its own — the `@AGENTS.md` import above is what pulls those rules into Claude's context.
