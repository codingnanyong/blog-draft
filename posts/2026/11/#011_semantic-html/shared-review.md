# NO.011 draft handoff

- Prepared by Codex on 2026-11-07 after the user confirmed semantic HTML. Claude did not author this week's draft.
- Publish Monday: 2026-11-09. Both manuscripts remain `status: draft`; user content and image review is pending.
- Existing recurring weekly parent: COD-441; six existing children COD-442–447. Local branch: `feat/cod-441-semantic-html`.
- Initial handoff on 2026-11-07: roadmaps reflected local draft readiness; external trackers were read only, with no upload, commit, push, PR, or publication.
- On 2026-11-09 the user authorized a branch upload for later review with Claude. Only Git branch upload is approved for this step; Drive backup and manual tracker updates are deferred. Both manuscripts remain drafts; neither merge nor publication is approved.

## Checks

Mechanical post checklist: **8/8 passed**.

- Required frontmatter in both languages; UTF-8 description lengths 112/116 bytes; scheduled date is a Monday.
- Folder and specimen number match NO.011; English vocabulary and language checked.
- Ten level-2 headings and six fenced code blocks match in count/order; code contents are identical.
- Each manuscript references thumbnail → 01 → 02 → 03 → 04, and ends with 04. All ten selected local image paths resolve.
- HTML example checked with a parser for tag nesting, unique IDs, fragment targets, one main, one h1, and two h2 elements. Browser, keyboard, and screen reader behavior was not exercised; the article includes the reader's manual checks.
- Technical descriptions checked against the linked WHATWG, W3C WAI, and MDN documentation. The comparison button is explicitly inert and absent from the complete runnable example.
- PNG signatures, chunk CRCs, compressed pixel streams, and aspect ratios checked for all eleven files, including the retained predecessor.
- Visual inspection: Korean spelling, English substitutions, Lv.1, NO.011, 1/5, exactly five slots with only the first filled, role layouts, and Korean/English composition checked.
- `git diff --check` passed. Existing untracked `.codex/` content was left intact.
- Checkout hook entrypoints lack executable bits. Shared guards were run directly against all 18 committed changes, and temporary executable wrappers invoke the unchanged shared pre-commit/pre-push entrypoints for this upload.

## Selected images

Built-in `image_gen` was used. Prompts and localization strings are in [shared-image-prompts.md](./shared-image-prompts.md).

| Role | Korean | English |
| --- | --- | --- |
| Cover | `images/thumbnail.png` | `images/thumbnail.en.png` |
| Encounter | `images/01-structure-sprout-encounter.png` | `images/01-structure-sprout-encounter.en.png` |
| Meaning | `images/02-html-meaning.png` | `images/02-html-meaning.en.png` |
| Process | `images/03-html-structure-flow.png` | `images/03-html-structure-flow.en.png` |
| Registration | `images/04-structure-sprout-registration.v3.png` | `images/04-structure-sprout-registration.en.v2.png` |
| Page regions | `images/05-html-page-regions.v2.png` | `images/05-html-page-regions.en.v2.png` |
| Links and buttons | `images/06-link-vs-button.v3.png` | `images/06-link-vs-button.en.v3.png` |
| Element anatomy | `images/07-html-element-anatomy.v3.png` | `images/07-html-element-anatomy.en.v3.png` |

Korean registration v2 removed the handheld tool from the clean portrait; the selected v3 / en.v2 also use the revised classification. Earlier assets are retained as predecessors. The table lists the current selected images; reading order is recorded below.

## Remaining review

User review of the prose, English localization, and selected images. Before publication, open the complete HTML example in a browser and follow the keyboard checks. The branch upload is authorized for review. Drive/tracker follow-up, PR merge, and publication remain deferred; the weekly issue and children should be reused.

## Claude review (2026-11-10)

Prose revised in both languages: classification `문서 구조형` / `Document structure type` (aligned with Linux-chapter `…형` naming), frequency in the `매우 높음 (…)` form, the reader-facing note about bilingual editions removed, a warmer field-log voice in a few passages, and the closing registration line matched to earlier chapters. No next-week preview: week 2 is still only proposed in the roadmap.

Image follow-ups are done and linked: registration v3 / en.v2 (classification text), new `05-html-page-regions` after the Observation 3 landmark paragraph, new `06-link-vs-button` after the link/button code block. Method is recorded in `shared-image-prompts.md`. Optional: in `01`, the explorer's open book shows scribble glyphs; leave as is unless re-rolled.

`07-html-element-anatomy` added after the void-element sentence in Observation 1. Image order in both languages: thumbnail, 01, 07, 02, 05, 03, 06, 04; all references resolve.

Publish date: the user decided on 2026-11-10 that NO.011 is a one-off late publication because of a business trip to China. Keep `date: 2026-11-09` as the scheduled Monday, and do not shift the roadmap: week 2 stays on 2026-11-16.

## Codex image improvement and character follow-up (2026-11-10)

The user's improvement request targets this week's NO.011. Six final replacements were made with built-in image_gen: 05 v2 / en.v2, 06 v2 / en.v2, and 07 v3 / en.v3. Korean masters were inspected before English text-localization. Exact prompt specifications and replacement strings are in shared-image-prompts.md.

- 05 now matches 02's pixel-art typography and frames. Two sibling sections stack vertically within article, within main; header/nav and footer remain outside main. Small explorer and Structure Sprout guide the diagram.
- 06 matches the same comparison-card style, distinguishes destination navigation from an in-place action, and explicitly says behavior requires implementation. Both characters remain present.
- 07 uses matching frames and typography, preserves literal code and the whole-element brace, and adds both characters below the code specimens at the user's request. The character-free v2 is retained as an intermediate predecessor; v3 is selected.
- Updated both manuscripts' image paths and meaningful alt text. The originals remain intact. No prose, frontmatter, headings, or code blocks changed.
- Visual checks passed for Korean spelling, English replacements, exact code punctuation, containment, arrow directions, character presence and Korean/English composition.
- Mechanical checks passed: eight paths per language resolve; PNG signatures and System.Drawing decoding succeed; body images are square; both orders are thumbnail → 01 → 07 → 02 → 05 → 03 → 06 → 04. Code blocks, frontmatter and headings match HEAD. `git diff --check` passed.

All selected revisions are local review drafts. User visual review remains pending. No commit, upload, push, tracker message or publication was performed in this improvement pass. No NO.010 file changes remain.

## User review corrections (2026-11-10)

All three requested corrections are applied in index.ko.md / index.en.md:

- 06 now selects `images/06-link-vs-button.v3.png` / `images/06-link-vs-button.en.v3.png`. Built-in image_gen edited Korean v2 first, then localized accepted v3 into English. The implementation note is fully inside the right-hand button panel; exactly one full-width takeaway remains at the bottom. Both characters and the comparison diagrams remain. Visual inspection confirmed exact text, note containment, one bottom summary and matching language compositions. All predecessors are retained. The complete prompt specification is under `06 v3` in shared-image-prompts.md.
- Observation 6's keyboard checklist now explains in both languages that short pages may not scroll and that the reader should check the address's `#observation` fragment.
- English labels now read `Encounter rate` and `First impression`, matching the preceding Linux posts.

Post checklist: **8/8 passed**. Both manuscripts have the required frontmatter, the roadmap's Monday date and draft status; NO.011 and English series vocabulary are correct; heading structure and code blocks match between languages; all sixteen image references resolve and decode; both orders remain thumbnail → 01 → 07 → 02 → 05 → 03 → 06 → 04; 04 is last; references use relative project paths. `git diff --check` passed. Browser/keyboard behavior was not exercised in this pass. Local review drafts remain pending user visual review; no external action was performed.

## Claude voice pass (2026-11-10)

At the user's request, added first-person misreadings and discoveries in Observations 1–4 and shifted impersonal instructions to field-log voice in both languages. Code blocks, headings, images and frontmatter were not changed. The first-person moments are authored for the series voice; user review pending.
