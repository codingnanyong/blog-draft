# Git Branch Strategy

The base policy — branch flow, branch naming, PR rules, Linear integration — follows [AGENTS.md's PR & issue policy](../../AGENTS.md#pr--issue-policy) (shared with repo-template, so it isn't duplicated here).

## What's specific to this repo

### PR labels, milestones, and assignees

`.github/workflows/pr-metadata.yml` adds metadata to every PR (`feat/*` → `develop` and `develop` → `main`). If it cannot, the check fails. The canonical rule lives in [AGENTS.md's PR metadata](../../AGENTS.md#pr-metadata).

| Item | Rule |
| --- | --- |
| Type label | From the title prefix after `COD-<n>`: `content:` `docs:` `feat:` `fix:` `ci:` `chore:` `test:` → `type: …` |
| Flow label | `flow: feature` into `develop`, `flow: sync` into `main` |
| Milestone | The chapter in progress: the open `코딩 도감 #NN <chapter>` milestone with the nearest due date (due = the chapter's last publish Monday) |
| Assignee | `codingnanyong` |

- The mirrored GitHub issue gets the same type label, milestone, and assignee.
- Create the next chapter's milestone as soon as its roadmap is set. Close a chapter's milestone when its chapter release is cut.
- When a `feat/*` PR merges into `develop`, the workflow deletes its head branch. Repository-wide auto-delete stays off, because it would also delete `develop` when a sync PR merges into `main`.

### A note on committing binaries

Binary files (images, etc.) can get corrupted through a text-editor-based commit, so they're committed through GitHub's "Upload files" screen (or an equivalent binary-safe path) instead. After committing, verify the raw file's signature to confirm it wasn't corrupted.

### `main` PRs and per-chapter releases

`develop` → `main` PRs collect reviewed drafts; weekly PRs have no release gate. After merging, the post is published on Velog/Medium manually and logged in the Notion Sprint Tracker.

A tag and GitHub Release are published once **every weekly draft of one chapter (`#number`) has landed on `main`**.

- Tag name: `codigdex-<two-digit chapter number>-<chapter slug>` (e.g. `codigdex-01-git`, `codigdex-02-linux`)
- Tag target: the `main` merge commit that brought in that chapter's last draft
- Release title: `Codigdex #NN <chapter> — Chapter Complete`
- Release notes: a table of each week's registered specimen (dex number `NO.00x`, name, trait, post title, folder, publish date, status), operating rules that changed during the chapter, the next chapter preview, and a short English summary
- If drafts from the same chapter land on `main` again after tagging, move the tag to the latest `main` merge commit and refresh the release notes too
- Close the chapter's milestone when the release is published or refreshed
