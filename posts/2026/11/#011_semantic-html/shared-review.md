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
| Registration | `images/04-structure-sprout-registration.v2.png` | `images/04-structure-sprout-registration.en.png` |

Korean registration v2 removes the handheld tool from the clean portrait. The original `.png` is retained as its predecessor. English was localized from v2.

## Remaining review

User review of the prose, English localization, and selected images. Before publication, open the complete HTML example in a browser and follow the keyboard checks. The branch upload is authorized for review. Drive/tracker follow-up, PR merge, and publication remain deferred; the weekly issue and children should be reused.

## Claude review (2026-11-10)

Prose revised in both languages: classification `문서 구조형` / `Document structure type` (aligned with Linux-chapter `…형` naming), frequency in the `매우 높음 (…)` form, the reader-facing note about bilingual editions removed, a warmer field-log voice in a few passages, and the closing registration line matched to earlier chapters. No next-week preview: week 2 is still only proposed in the roadmap.

Image follow-ups are done and linked: registration v3 / en.v2 (classification text), new `05-html-page-regions` after the Observation 3 landmark paragraph, new `06-link-vs-button` after the link/button code block. Method is recorded in `shared-image-prompts.md`. Optional: in `01`, the explorer's open book shows scribble glyphs; leave as is unless re-rolled.

`07-html-element-anatomy` added after the void-element sentence in Observation 1. Image order in both languages: thumbnail, 01, 07, 02, 05, 03, 06, 04; all references resolve.

Publish date: 2026-11-09 has passed. Adjust `date` to the actual publish Monday when the user decides.
