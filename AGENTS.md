# Blog Draft Project Rules

## Project purpose

This repository prepares a weekly technical-blog post for publication in Korean on Velog and in English on Medium. Keep every deliverable as a reviewable draft until the user explicitly requests publication.

## Weekly workflow

1. The user supplies or confirms the week's topic.
2. Before writing, inspect the relevant roadmap, workflow documentation, templates, and the most recent post in the same series.
3. Create or update the Korean draft first unless the user asks for a different order.
4. Create or update the English version as a natural localization, preserving the Korean article's meaning, structure, code, and image sequence.
5. Check technical claims and commands for accuracy. Do not invent personal experiences or results that the user did not provide.
6. Keep `status: draft` until the user explicitly approves publication.
7. When the post is ready to push to GitHub, also back it up to Google Drive: save `index.ko.md`/`index.en.md` as plain markdown (not converted to Google Docs — conversion breaks markdown syntax) under `My Drive/Developer/Project/Blog/2026/09/<repo folder name>/`, matching the repo's folder name exactly. Do not upload the `images/` folder yourself (each post's images are tens of MB combined, too large for this tool's per-call payload) — tell the user to drag the local `images/` folder into the same Drive location instead.

## Codigdex series voice

- Treat development concepts, tools, errors, and debugging experiences as specimens that are discovered, observed, and recorded.
- Use an approachable first-person learning-log voice rather than textbook prose.
- Explain the mental model before listing commands.
- Keep headings, specimen information, observations, summary, and the closing Codigdex note consistent with nearby posts.
- Korean naming uses `코딩 도감`; English naming uses `Codigdex`.
- Preserve continuity with the previous observation and preview the next one only when the roadmap or user confirms it.

## Image deliverables

Every weekly post requires five images per language: one thumbnail plus four numbered body illustrations (`01` through `04`). Do not interpret this as four images including the thumbnail.

### Mandatory reference workflow

- Use the `imagegen` skill for every series image.
- Before generating anything, inspect the approved images from the preceding weeks with `view_image`. Do not rely on a prose-only description of the style.
- Pass the matching approved images as strict visual references when generating each numbered asset. State in the prompt that their layout, whitespace, pixel density, recurring characters, palette, typography, and UI structure are templates to preserve rather than loose inspiration.
- Prefer these canonical references while the Git series is active:
  - Thumbnail: the most recently approved `thumbnail*.png` plus `posts/2026/09/01-codigdex-01-git/images/thumbnail.v2.png`.
  - `01`: `posts/2026/09/01-codigdex-01-git/images/01-git-encounter.v2.png` and `posts/2026/09/02-codigdex-01-branch-merge/images/01-branch-merge-encounter.png`.
  - `02`: `posts/2026/09/01-codigdex-01-git/images/02-git-three-areas.v2.png` and `posts/2026/09/02-codigdex-01-branch-merge/images/02-branch-parallel-worlds.png`.
  - `03`: `posts/2026/09/01-codigdex-01-git/images/03-git-basic-flow.v2.png` and `posts/2026/09/02-codigdex-01-branch-merge/images/03-merge-timelines.png`.
  - `04`: `posts/2026/09/01-codigdex-01-git/images/04-git-observation-1-of-5.v2.png` and `posts/2026/09/02-codigdex-01-branch-merge/images/04-observation-2-of-5.png`.
- When a later image is explicitly approved by the user, treat it as an additional reference for the same numbered role.

### Visual identity

- Preserve the established sparse retro 16-bit pixel-art identity: warm cream background, generous negative space, thick near-black pixel outlines, burnt Git-orange accents, restrained brown details, and simple black-and-cream RPG interface panels.
- Preserve the recurring explorer: orange cap, orange jacket, backpack, black hair, usually seen from behind or in profile while holding a field guide.
- Preserve the recurring Git specimen language: a simple friendly burnt-orange creature with white eyes and branch-node antennae. Adapt its silhouette to the week's concept without replacing it with a different art direction.
- Keep subjects simple and readable at blog width. Match the relatively flat, clean compositions of the approved references.
- Avoid photorealism, glossy 3D, neon colors, gradients, dramatic lighting, painterly rendering, dense textures, oversized monsters, detailed rooms, bookshelves, crowded desks, elaborate landscapes, and unnecessary props.
- Never add corporate logos, watermarks, decorative pseudo-code, or tiny unreadable interface copy.

### Numbered image templates

- `thumbnail`: wide landscape near `1.91:1`. Use a large readable series/topic title and one clear scene. Preserve safe margins for Velog and Medium cards. A thumbnail may be more detailed than the body images, but it must use the same characters and palette.
- `01 — encounter`: square `1:1` and intentionally sparse. Reproduce the classic RPG battle screen: specimen name, `Lv.<week>`, and one HP bar at the upper left; explorer at the lower left; one or two simple topic specimens at the upper right; one large double-border dialogue box across the bottom. Do not add scenery, an infographic, a command menu, a desk, or extra panels.
- `02 — first concept`: square `1:1` teaching card. Use one thin double-border title panel at the top, a simple two- or three-part comparison in the center, and one short caption panel at the bottom. Use large icons, a small recurring explorer/specimen pair, and generous cream space.
- `03 — second concept or process`: square `1:1` timeline or flow scene. Use one framed title at the top, one large central timeline/process diagram with the explorer participating, and one short takeaway panel at the bottom. Keep it instructional and uncluttered rather than turning it into another battle screen.
- `04 — observation log`: square `1:1` and must reproduce the established Codigdex registration UI. Use a thick black/orange outer frame, black header with `관찰 기록 <week>/<total>` or its English localization, specimen window on the left, type and result panels on the right, a progress bar with exactly the current number of slots filled, the explorer recording notes, and a full-width black bottom panel that previews the confirmed next topic.

### Localization and text validation

- Generate the Korean asset first. Then create the English version as a `text-localization` edit of the accepted Korean image so composition, characters, icons, and spacing remain unchanged.
- For a localization edit, explicitly instruct the image tool to change only the requested text and preserve every other pixel-level design decision.
- Use the same filenames with `.en.png` for English assets.
- List every visible string verbatim in the prompt. Require no other readable text.
- Verify every result visually before saving. Check Hangul, English spelling, punctuation, series number, `Lv` number, observation fraction, progress slots, branch labels, and next-topic text.
- Reject and regenerate an image when text is misspelled, Hangul is malformed, the English composition drifts from Korean, the wrong number of progress slots is filled, or the numbered template is not followed.
- Keep captions short enough to fit the established pixel typography. Prefer one concise sentence or phrase over dense explanatory copy.

### Generation and acceptance sequence

1. Read the Korean and English drafts and identify the exact paragraph each image supports.
2. Confirm the week number, total observation count, and next topic from the roadmap.
3. Plan the thumbnail and all four numbered images before generating the first asset.
4. Generate one distinct asset per image-generation call; do not substitute a single batch prompt for different roles.
5. Inspect each Korean output, localize the accepted version to English, and inspect the localized output again.
6. Save only accepted outputs into the post's `images/` directory and update both Markdown files.
7. Confirm that each language has one thumbnail and exactly four numbered body-image references, unless the user explicitly requests a different count.

## Image files and Markdown

- Store images in the post's local `images/` directory; never leave a referenced final asset only in a generated-image or temporary directory.
- Follow filenames already referenced by the Markdown. For English-localized assets, use the existing `.en.png` convention.
- Do not overwrite an existing image unless the user explicitly requests replacement. Use a versioned sibling such as `.v2.png` when preserving the original.
- After generating images, update the relevant Markdown image paths and meaningful alt text.
- Confirm that every Markdown image reference resolves to an existing file.

## PR & issue policy

Every PR into `develop` is gated by CI (`.github/workflows/pr-policy.yml`) and requires a mirrored Linear/GitHub issue pair. The normal path is automated:

1. Create a branch named `feat/<slug>` and push it to `origin`.
2. `.github/workflows/prepare-feature-pr.yml` finds or creates a Linear issue in team `COD`, project "블로그 자동발행".
3. The workflow finds or creates the matching GitHub issue, then opens a Draft PR into `develop`.
4. The PR title starts with `COD-<n>`. Its body contains both `Closes COD-<n>` and `Closes #<github-issue-number>`.
5. `.github/workflows/pr-policy.yml` validates the branch flow and issue pair without creating or editing them.
6. `main` only accepts PRs from `develop`. Publishing to Velog/Medium is the release and remains manual.

Automation uses `LINEAR_API_KEY` and `GH_PAT` repository secrets. `GH_PAT` must be able to read contents and write issues/pull requests; using it to create the PR lets PR checks start automatically. Provisioning is keyed by `repository:branch`, so another push or a manual rerun reuses completed Linear/GitHub records after a partial failure. A branch named `feat/cod-<n>-<slug>` reuses that existing Linear issue when it belongs to the configured team and project.

If automation fails, rerun `Prepare feature PR` with the existing branch. Manual repair remains supported: create the Linear issue, create an open GitHub issue whose title starts with the same `COD-<n>`, then open a PR with both closing references. Do not create a second issue pair for the same branch.

On merge into `develop`, CI auto-closes the mirrored GitHub issue; Linear's native GitHub integration then auto-transitions the Linear issue to Done. No manual status update needed after merge.

## Editing constraints

- Preserve frontmatter fields, document language, heading structure, and intentional links unless the requested task requires changing them.
- Do not publish, upload, create a pull request, merge branches, or message external services without explicit user authorization.
- Keep unrelated user changes intact.
- At handoff, report the changed document paths, generated image paths, and any remaining review items.
