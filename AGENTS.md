# Blog Draft Project Rules

This repository prepares a weekly technical-blog post, the **코딩 도감 / Codigdex** series. Each post is published in Korean on Velog and in English on Medium, every Monday. Every deliverable stays a reviewable draft until the user explicitly requests publication.

The detailed shared rules live in `.agents/rules/`, one topic per file. Every agent must **read the relevant file before starting** the task:

| Task | Read first |
| --- | --- |
| Anything | `.agents/rules/shared-authority.md` |
| Writing or editing a post, templates, or roadmap | `.agents/rules/shared-series-voice.md`, `.agents/rules/shared-post-files.md` |
| Generating or replacing images | `.agents/rules/shared-images.md`, `.agents/rules/shared-image-composition-plans.md`, then follow `.agents/skills/shared-weekly-images/SKILL.md` |
| Branches, commits, PRs, releases | `.agents/rules/shared-git-pr-policy.md` |
| Linear, Notion, Slack, Drive | `.agents/rules/shared-tracking.md` |

Step-by-step procedures are in `.agents/skills/*/SKILL.md`:

- `shared-weekly-post`: draft a week.
- `shared-weekly-images`: produce the five images per language.
- `shared-publish-followup`: close out a published week.
- `shared-chapter-release`: tag a finished chapter.

## Support asset naming

- Use `shared-<name>` for assets shared by Claude and Codex; this is the default.
- Use `claude-<name>` or `codex-<name>` only for agent-specific assets.
- Apply the prefix to ordinary files and to skill or plugin folder names.
- Keep required entrypoint and manifest names such as `README.md` and `SKILL.md` unchanged.

## Rules that must never be broken

Claude Code enforces these with shared hooks under `.agents/hooks/`, wired through `.claude/settings.json`. Other agents must also follow them directly:

- Never publish, upload, push, open or merge a PR, move tags, or message external services without the user's explicit go-ahead.
- Never push directly to `develop` or `main`, force-push, commit `.env`, or skip git hooks.
- Never overwrite an existing image; save a versioned sibling such as `.v2.png`.
- Write dex numbers as uppercase `NO.001` in Markdown, never `No.001`.
- Keep `status: draft` until the user reports the post is live.
- Do not invent personal experiences or results. Keep unrelated user changes intact.
