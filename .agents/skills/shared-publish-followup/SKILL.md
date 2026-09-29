---
name: shared-publish-followup
description: Close out a week after the user reports its post is live on Velog/Medium — Linear, Notion, the Git status flip, main sync, chapter tag/milestone, and branch cleanup. Use whenever the user says a post was published ("발행했어") or that Linear/Notion don't reflect a publish.
---

# Publish follow-up

A merged PR does not mean the post is published. Do every step below in the same turn. Scope is blog-only (`.agents/rules/shared-tracking.md`).

1. **Check current state.**
   ```bash
   python .agents/skills/shared-publish-followup/scripts/shared-tracker.py status
   git fetch --prune && git branch -a -vv
   ```
2. **Linear and Notion.** Run this with the week's parent issue and sprint number (week N = Sprint N; e.g. week 5 → `COD-55 5`):
   ```bash
   python .agents/skills/shared-publish-followup/scripts/shared-tracker.py publish COD-<parent> <sprint>
   ```
   It sets the `Velog·Medium 발행 & 로그 업데이트` sub-issue and the parent to Done, and the Notion row to Completed / 100%.
3. **Git status flip.**
   - Set both `index.ko.md` and `index.en.md` to `status: published`, and set `date` to the real publish Monday.
   - Update the week's row in `docs/kor/ROADMAP.md` and `docs/eng/ROADMAP.md` to 발행 완료 / Published.
   - Commit on `feat/<slug>` with a `content:` title. Push only with the user's go-ahead; the push opens the PR.
4. **Sync to main.** After the user merges the feature PR, open `develop` → `main`:
   ```bash
   gh pr create --base main --head develop --title "content: sync <what> to main" --body "..."
   ```
   `pr-metadata.yml` adds `flow: sync`, the type label, and the chapter milestone.
5. **Chapter's final week only:** run the `shared-chapter-release` skill after the sync PR merges.
6. **Branches.** Check that no merged `feat/*` branch is left on the remote (the workflow deletes them) or locally (`git branch -d <branch>`). Switch back to an up-to-date `develop`.
7. **Report** what changed in each system, and any step that is waiting on the user (merges, tag push).
