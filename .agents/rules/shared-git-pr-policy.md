# Branches, PRs, and issues

This policy is shared with `codingnanyong/repo-template` and is CI-enforced by `.github/workflows/pr-policy.yml` and `pr-metadata.yml`.

## Branch flow

- `feat/<slug>` → `develop` → `main`. `main` accepts PRs only from `develop`. Never push directly to `develop` or `main` (enforced by a hook).
- Work that belongs to the week in progress goes on `feat/cod-<n>-<slug>`, so `Prepare feature PR` reuses that week's Linear issue. Only work independent of the week uses a bare `feat/<slug>`.
- Publishing to Velog/Medium is the release and stays manual.

## Issue pair (automated)

1. Pushing `feat/*` runs `.github/workflows/prepare-feature-pr.yml`. It finds or creates a Linear issue in team `COD`, project "블로그 자동발행", assigned to the active cycle.
2. The workflow finds or creates the mirrored GitHub issue, then opens a Draft PR into `develop`.
3. PR title starts with `COD-<n>`; body contains `Closes COD-<n>` and `Closes #<github-issue>`.
4. On merge into `develop`, CI closes the mirrored GitHub issue and Linear moves the issue to Done.

- Provisioning is keyed by `repository:branch`, so a push or rerun reuses records after a partial failure. If automation fails, rerun `Prepare feature PR` with the existing branch. Never create a second issue pair for the same branch.
- If it fails at "Ensure Linear issue" with `USAGE_LIMIT_EXCEEDED`, the Linear free plan's 250 active-issue cap was hit. Archive finished issues, then rerun.
- Secrets: `LINEAR_API_KEY`, `GH_PAT` (reads contents, writes issues/PRs; creating the PR with it lets PR checks start).

## PR metadata (automated)

`.github/workflows/pr-metadata.yml` applies these on every PR and fails the check when it cannot:

- **Type label** from the title prefix after `COD-<n>`: `content:` → `type: content`, `docs:` → `type: docs`, `feat:` → `type: feature`, `fix:` → `type: fix`, `ci:` → `type: ci`, `chore:` → `type: chore`, `test:` → `type: test`. Sync PR titles follow the same rule (e.g. `content: sync week 5 published status to main`).
- **Flow label**: `flow: feature` into `develop`, `flow: sync` into `main`.
- **Milestone**: the chapter in progress — the open `코딩 도감 #NN <chapter>` milestone with the nearest due date (due = the chapter's last publish Monday). Create the next chapter's milestone when its roadmap is set.
- **Assignee**: `codingnanyong`.
- The mirrored GitHub issue gets the same type label, milestone, and assignee.
- A merged `feat/*` branch is deleted by the workflow. Repository-wide auto-delete stays off, because it would delete `develop` when a sync PR merges.

## Chapter release

Weekly PRs have no release. When every week of a chapter is on `main`, tag `codigdex-<NN>-<slug>` on that `main` merge commit and publish a GitHub Release. Then close the chapter milestone. The `shared-chapter-release` skill has the procedure.

## Commits and PR text

- End commit messages and PR descriptions with the attribution lines the harness provides.
