---
name: weekly-post
description: Draft a week's Codigdex post (Korean first, then English), from topic confirmation through Drive backup and push. Use when the user gives or confirms the week's topic or asks to write/revise a weekly draft.
---

# Weekly post

Rules that apply throughout: `.claude/rules/series-voice.md`, `post-files.md`, `authority.md`.

1. **Confirm the topic.** The user supplies or confirms it. Read the roadmap row in `docs/kor/ROADMAP.md` for the chapter, week, and publish Monday.
2. **Look up the specimen.** Take the stage's `dexNumber` and name from the game repo (`github.com/codingnanyong/codigdex`, `web/lib/domain/chapters/*.ts`).
3. **Read before writing.** Read `docs/kor/WORKFLOW.md`, the templates in `templates/`, and the most recent post in the same chapter (both languages).
4. **Create the folder.** Create `posts/YYYY/MM/#NNN_<slug>/` from the templates and set `date` to the publish Monday and `status: draft`.
5. **Korean draft first** (`index.ko.md`). Write the mental model before commands; end with the registration section.
6. **English localization** (`index.en.md`). Keep the same structure, code, and image sequence.
7. **Check accuracy.** Verify every command and technical claim, and do not invent experiences.
8. **Images.** Run the `weekly-images` skill: five images per language.
9. **Review.** Delegate a mechanical check to the `post-checker` agent and fix what it reports. Then hand the draft to the user for review.
10. **After the user approves it for GitHub:**
    - Back up `index.ko.md` / `index.en.md` to Drive as plain Markdown (see `post-files.md`), and ask the user to drag `images/` over.
    - Commit on `feat/cod-<week parent n>-<slug>`.
    - Push only with the user's go-ahead. The push creates the Draft PR.
11. **After the draft PR merges:** reopen the week's Linear parent to In Progress and mark finished sub-issues Done (see `.claude/rules/tracking.md`).
