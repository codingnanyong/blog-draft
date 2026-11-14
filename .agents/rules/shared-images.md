---
paths:
  - "posts/**/images/**"
  - "references/**"
---

# Series image rules

The step-by-step generation procedure is the `shared-weekly-images` skill. This file holds the rules every image must meet. The durable role-by-role layout decisions and current specimen registry are in `shared-image-composition-plans.md`.

## Visual identity

- Preserve the established sparse retro 16-bit pixel-art identity: warm cream background, generous negative space, thick near-black pixel outlines, burnt Git-orange accents, restrained brown details, and simple black-and-cream RPG interface panels.
- Preserve the recurring explorer: orange cap, orange jacket, backpack, black hair, usually seen from behind or in profile while holding a field guide.
- Preserve the recurring Git specimen language: a simple friendly burnt-orange creature with white eyes and branch-node antennae. Adapt its silhouette to the week's concept without replacing it with a different art direction. `references/codigdex-monsters/` is character reference only, not a layout template.
- Keep subjects simple and readable at blog width. Match the relatively flat, clean compositions of the approved references.
- Avoid photorealism, glossy 3D, neon colors, gradients, dramatic lighting, painterly rendering, dense textures, oversized monsters, detailed rooms, bookshelves, crowded desks, elaborate landscapes, and unnecessary props.
- Never add corporate logos, watermarks, decorative pseudo-code, or tiny unreadable interface copy.

## Canonical references (Git chapter)

When a later image is explicitly approved by the user, it becomes an additional reference for the same numbered role.

- Thumbnail: the most recently approved `thumbnail*.png` plus `posts/2026/09/#001_git/images/thumbnail.v2.png`.
- `01`: `posts/2026/09/#001_git/images/01-git-encounter.v2.png`, `posts/2026/09/#002_branch-merge/images/01-branch-merge-encounter.png`.
- `02`: `posts/2026/09/#001_git/images/02-git-three-areas.v2.png`, `posts/2026/09/#002_branch-merge/images/02-branch-parallel-worlds.png`.
- `03`: `posts/2026/09/#001_git/images/03-git-basic-flow.v2.png`, `posts/2026/09/#002_branch-merge/images/03-merge-timelines.png`.
- `04`: `posts/2026/09/#001_git/images/04-git-sprout-registration.v2.png`, `posts/2026/09/#002_branch-merge/images/04-branch-twins-registration.v2.png`.

## Numbered templates

- `thumbnail`: wide landscape near `1.91:1`. A large readable series/topic title and one clear scene, with safe margins for Velog and Medium cards. It may be more detailed than body images but uses the same characters and palette.
- `01 — encounter`: square `1:1`, intentionally sparse classic RPG battle screen. Specimen name, `Lv.<week>`, and one HP bar at the upper left; explorer at the lower left; one or two simple topic specimens at the upper right; one large double-border dialogue box across the bottom. No scenery, infographic, command menu, desk, or extra panels.
- `02 — first concept`: square `1:1` teaching card. One thin double-border title panel at the top, a simple two- or three-part comparison in the center, one short caption panel at the bottom. Large icons, a small explorer/specimen pair, generous cream space.
- `03 — second concept or process`: square `1:1` timeline or flow scene. One framed title at the top, one large central timeline/process diagram with the explorer participating, one short takeaway panel at the bottom. Instructional, not another battle screen.
- `04 — registration card`: square `1:1`; ends every weekly post. Thick black/orange outer frame, black `코딩 도감 등록` header (or its English localization), specimen window on the left, number/name plus type and trait panels on the right, an approval stamp, a progress bar with exactly the current number of chapter slots filled, and a full-width black bottom panel declaring that week's registration complete (the whole chapter on the final week). The specimen window is a clean portrait: only the registered specimen or specimen group, centered on a blank warm-cream field, with no explorer, props, ground, grass, rocks, scenery, or cast shadow. Every `NO.00x` is an individual registered specimen; never label it an observation log. Next-topic previews belong in the prose before this image.
- `05+ — explanatory`: optional and unlimited, added wherever a picture makes the prose easier to follow (a step sequence, a before/after, a common pitfall). Square `1:1`, built like `02` or `03`: one framed title, one comparison or flow using the post's own example names and commands, one short takeaway panel. Number them in reading order from `05`; they sit before the `04` registration card. Use the series' own terms exactly (e.g. 셸, never 셀).

## Game character verification

- Before generating a specimen, resolve its actual `assetKey` in the current game source and inspect that asset. Compare it against the blog reference; a copied reference is not proof of game fidelity.
- NO.012 audit (2026-11-14): the local game asset `packages/game-assets/files/monsters/ch03.html-css/style-shell-lv2.png` differs from `references/codigdex-monsters/ch03.html-css/style-shell-lv2.png`. The game asset has a small pale triangular trowel, an uncovered head, and no mallet, helmet, blueprint, swatch chart, or large square buckle. Use the byte-identical `references/codigdex-monsters/ch03.html-css/shared-style-shell-lv2.game.png` snapshot (SHA-256 `17ae044c5cccf51528c69e003d5a5a6041952fc702dcc66f45dcf58e7cfd3c0a`). The older unprefixed reference and mallet correction are divergent; never treat them as canonical. Game classification is `HTML/CSS 학습형` / `HTML/CSS learning type`, trait is the four-layer calculation from `careerMonsterQuizzes.ts`.
- NO.011 audit (2026-11-14): use `references/codigdex-monsters/ch03.html-css/shared-structure-sprout-lv1.game.png`, byte-identical to the game asset (SHA-256 `c2f7e9d0c4218d0528064bc7343d234f49691cb126b9fd11ca2825c65c369ffb`). Structure Sprout has an orange bare chest/neck, a small brick shell with crenellated top, and a small pale triangular trowel. Do not add the older reference's cream collar or shield-shaped chest bib; do not strip the actual trowel from registration. Type is `HTML/CSS 학습형` / `HTML/CSS learning type`; trait is using HTML elements matching content meaning.
- Preserve game identity and fixed equipment across roles, including registration. Exclude unrelated scene props from registration portraits.

## Text and localization

- The Korean asset comes first. The English asset is a text-localization edit of the accepted Korean image that changes only the requested text and preserves every other design decision.
- List every visible string verbatim in the prompt and require no other readable text. Keep captions to one short sentence or phrase.
- Reject and regenerate when text is misspelled, Hangul is malformed, the English composition drifts from Korean, the wrong number of progress slots is filled, or the numbered template is not followed.
