---
name: weekly-images
description: Produce a week's five series images per language (thumbnail + 01–04) in the established pixel-art style, Korean first then English localization. Use when a weekly post needs its images generated, replaced, or localized.
---

# Weekly images

The visual rules, canonical references, and numbered templates are in `.claude/rules/images.md`.

1. **Read the drafts.** Read both `index.ko.md` and `index.en.md` and identify the exact paragraph each image supports.
2. **Confirm the numbers.** Get the specimen number (`NO.00x`), `Lv.<week>`, current/total chapter count (progress slots), and next topic from the roadmap.
3. **Plan all five images** (thumbnail, 01–04) before generating the first one, including every visible string verbatim.
4. **Look at the references.** Open the canonical approved images for each role; a prose description is not enough. Pass them to the image tool as strict references: their layout, whitespace, pixel density, characters, palette, typography, and UI structure are templates to preserve.
   - Codex: use the `imagegen` skill and `view_image`.
5. **Generate the Korean images,** one asset per call. Never batch different roles into one prompt.
6. **Inspect each Korean image.** Check the Hangul, specimen number, `Lv`, chapter fraction, progress slots, branch labels, and completion text. Reject and regenerate on any miss.
7. **Localize to English.** Make the English version as a text-localization edit of the accepted Korean image: change only the listed text and keep every other pixel. Save it as `<name>.en.png` and inspect it again.
8. **Save the accepted images** into the post's `images/`. Never overwrite an existing file; use `.v2.png` instead.
9. **Update both Markdown files** with the image paths and meaningful alt text.
10. **Verify:** each language has one thumbnail and exactly four numbered body images, and every reference resolves to a file. Let the `post-checker` agent confirm.
