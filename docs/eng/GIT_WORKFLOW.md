# Git Branch Strategy

The base policy — branch flow, branch naming, PR rules, Linear integration — follows [AGENTS.md's PR & issue policy](../../AGENTS.md#pr--issue-policy) (shared with repo-template, so it isn't duplicated here).

## What's specific to this repo

### A note on committing binaries

Binary files (images, etc.) can get corrupted through a text-editor-based commit, so they're committed through GitHub's "Upload files" screen (or an equivalent binary-safe path) instead. After committing, verify the raw file's signature to confirm it wasn't corrupted.

### No release gate on `main` PRs

Unlike other repo-template-based repos, this one has no version-tag/release concept. `develop` → `main` PRs collect reviewed, publish-ready drafts; after merging, the post is published on Velog/Medium manually and logged in the Notion Sprint Tracker.
