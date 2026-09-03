# Git Branch Strategy

## Branch flow

```
feat/cod-<linear-id>-<slug>
          │ PR
          ▼
       develop
          │ PR
          ▼
        main
```

Direct pushes to `develop` and `main` are avoided; changes always land through a pull request.

## Branch names

- Format: `feat/cod-<linear-id>-<slug>`
- Example: `feat/cod-41-coding-dogam-git`
- One branch corresponds to one week (i.e. one set of Linear sub-issues).

## Pull request rules

- `feat/*` → `develop`
  - The title includes the related Linear issue number (e.g. `COD-41`).
  - The body briefly summarizes the change: topic, images inserted, feedback applied.
- `develop` → `main`
  - Collects reviewed, publish-ready drafts.
  - After merging, the post is published on Velog manually and the publish log is recorded in the Notion Sprint Tracker.

## Linear integration

- Each week is registered in Linear as a parent issue plus 6 standard sub-issues: pick a topic → write the draft (Claude) → user review & feedback → push to GitHub (feat branch → PR) → merge PR (develop) → publish on Velog & update the log.
- GitHub branches/PRs and Linear issues reference each other to keep traceability.

## A note on committing binaries

Binary files (images, etc.) can get corrupted through a text-editor-based commit, so they're committed through GitHub's "Upload files" screen (or an equivalent binary-safe path) instead. After committing, verify the raw file's signature to confirm it wasn't corrupted.
