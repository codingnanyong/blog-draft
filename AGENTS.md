# Blog Draft Project Rules

This repository prepares a weekly technical-blog post, the **코딩 도감 / Codigdex** series. Each post is published in Korean on Velog and in English on Medium, every Monday. Every deliverable stays a reviewable draft until the user explicitly requests publication.

The detailed rules live in `.claude/rules/`, one topic per file. Claude Code loads them automatically; other agents (Codex) must **read the relevant file before starting** the task:

| Task | Read first |
| --- | --- |
| Anything | `.claude/rules/authority.md` |
| Writing or editing a post, templates, or roadmap | `.claude/rules/series-voice.md`, `.claude/rules/post-files.md` |
| Generating or replacing images | `.claude/rules/images.md`, then follow `.claude/skills/weekly-images/SKILL.md` |
| Branches, commits, PRs, releases | `.claude/rules/git-pr-policy.md` |
| Linear, Notion, Slack, Drive | `.claude/rules/tracking.md` |

Step-by-step procedures are in `.claude/skills/*/SKILL.md`:

- `weekly-post`: draft a week.
- `weekly-images`: produce the five images per language.
- `publish-followup`: close out a published week.
- `chapter-release`: tag a finished chapter.

## Rules that must never be broken

Claude Code enforces these with hooks (`.claude/hooks/`). Other agents are not covered by those hooks and must follow them by hand:

- Never publish, upload, push, open or merge a PR, move tags, or message external services without the user's explicit go-ahead.
- Never push directly to `develop` or `main`, force-push, commit `.env`, or skip git hooks.
- Never overwrite an existing image; save a versioned sibling such as `.v2.png`.
- Write dex numbers as uppercase `NO.001` in Markdown, never `No.001`.
- Keep `status: draft` until the user reports the post is live.
- Do not invent personal experiences or results. Keep unrelated user changes intact.
