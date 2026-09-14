# Git Branch Strategy

The base policy — branch flow, branch naming, PR rules, Linear integration — follows [AGENTS.md's PR & issue policy](../../AGENTS.md#pr--issue-policy) (shared with repo-template, so it isn't duplicated here).

## What's specific to this repo

### A note on committing binaries

Binary files (images, etc.) can get corrupted through a text-editor-based commit, so they're committed through GitHub's "Upload files" screen (or an equivalent binary-safe path) instead. After committing, verify the raw file's signature to confirm it wasn't corrupted.

### `main` PRs and per-chapter releases

`develop` → `main` PRs collect reviewed drafts; weekly PRs have no release gate. After merging, the post is published on Velog/Medium manually and logged in the Notion Sprint Tracker.

A tag and GitHub Release are published once **every weekly draft of one chapter (`#number`) has landed on `main`**.

- Tag name: `codigdex-<two-digit chapter number>-<chapter slug>` (e.g. `codigdex-01-git`, `codigdex-02-linux`)
- Tag target: the `main` merge commit that brought in that chapter's last draft
- Release title: `Codigdex #NN <chapter> — Registration Complete`
- Release notes: each week's post folder and dex number, plus the next chapter preview
