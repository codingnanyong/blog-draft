---
name: chapter-release
description: Cut or refresh a Codigdex chapter's git tag and GitHub Release once all its weeks are on main, and roll the chapter milestone. Use after a chapter's final week lands on main, or when a chapter's drafts land on main again.
---

# Chapter release

Weekly PRs have no release. One tag and one Release are published per chapter (`#NN`).

1. **Check it's time.** Every week's draft of the chapter is on `main` (drafts count; they need not be published).
2. **Tag.** Name it `codigdex-<NN>-<slug>` (e.g. `codigdex-02-linux`). It goes on the `main` merge commit that brought in the chapter's last change.
3. **Release title.** Korean: `코딩 도감 #NN <챕터명> — 챕터 등록 완료`; English: `Codigdex #NN <chapter> — Chapter Complete`.
4. **Release notes.** Keep the structure of the previous release (`gh release view codigdex-01-git`):
   - Table: slot `k/N` · `NO.00x` · specimen · trait · post link · publish date · 발행 완료/발행 예정.
   - Operating rules changed during the chapter, with PR numbers.
   - Next chapter preview.
   - Short English summary.
5. **Refresh.** When the chapter's drafts land on `main` again, move the tag to the new `main` merge commit and refresh the notes.
6. **Hand over the commands.** Write the notes to the scratchpad, then give the user the commands. Tag force-push and `gh release edit` are blocked for agents, so the user runs them:
   ```bash
   git fetch origin && git tag -f codigdex-<NN>-<slug> origin/main && git push -f origin codigdex-<NN>-<slug>
   gh release edit codigdex-<NN>-<slug> --notes-file <notes.md>    # or: gh release create ... --title ... --notes-file ...
   ```
7. **Roll the milestone.**
   - Close the chapter's `코딩 도감 #NN <chapter>` milestone.
   - Make sure the next chapter's milestone exists and is open, with due = its last publish Monday. Without it, `pr-metadata.yml` fails every PR.
   ```bash
   gh api -X PATCH repos/codingnanyong/blog-draft/milestones/<n> -f state=closed
   gh api repos/codingnanyong/blog-draft/milestones -f title="코딩 도감 #NN <chapter>" -f due_on=<YYYY-MM-DD>T23:59:59Z
   ```
