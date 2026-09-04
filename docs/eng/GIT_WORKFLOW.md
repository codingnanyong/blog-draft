# Git Branch Strategy

## Branch flow

```
feat/<slug> ── push ──> Linear issue + GitHub mirror issue
                              │ automated draft PR
                              ▼
                           develop
                              │ PR
                              ▼
                            main
```

Direct pushes to `develop` and `main` are avoided; changes always land through a pull request.

## Branch names

- Default format: `feat/<slug>`
- Example: `feat/codigdex-git`
- To reuse an existing Linear issue: `feat/cod-<linear-id>-<slug>`
- One branch corresponds to one week (i.e. one set of Linear sub-issues).

## Pull request rules

- `feat/*` → `develop`
  - The first push automatically creates the Linear/GitHub issue pair and a draft PR.
  - The PR title includes the related Linear issue number (for example, `COD-41`).
  - The body includes `Closes COD-41` and `Closes #number` for the GitHub mirror issue.
- `develop` → `main`
  - Collects reviewed, publish-ready drafts.
  - After merging, the post is published on Velog manually and the publish log is recorded in the Notion Sprint Tracker.

## Linear integration

- Each week is registered in Linear as a parent issue plus 6 standard sub-issues: pick a topic → write the draft (Claude) → user review & feedback → push to GitHub (feat branch → PR) → merge PR (develop) → publish on Velog & update the log.
- GitHub branches/PRs and Linear issues reference each other to keep traceability.
- If automation fails, rerun `Prepare feature PR` for the same branch. Provisioned issues are reused by the repository-and-branch key.

## A note on committing binaries

Binary files (images, etc.) can get corrupted through a text-editor-based commit, so they're committed through GitHub's "Upload files" screen (or an equivalent binary-safe path) instead. After committing, verify the raw file's signature to confirm it wasn't corrupted.
