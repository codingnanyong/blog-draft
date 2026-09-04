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

## Codigdex series voice

- Treat development concepts, tools, errors, and debugging experiences as specimens that are discovered, observed, and recorded.
- Use an approachable first-person learning-log voice rather than textbook prose.
- Explain the mental model before listing commands.
- Keep headings, specimen information, observations, summary, and the closing Codigdex note consistent with nearby posts.
- Korean naming uses `코딩 도감`; English naming uses `Codigdex`.
- Preserve continuity with the previous observation and preview the next one only when the roadmap or user confirms it.

## Image deliverables

- Every weekly post requires four images per language by default: one thumbnail and three body illustrations.
- If an existing draft already contains a different number of explicit image slots, follow the draft rather than removing or inventing slots.
- When both Korean and English posts exist, create matching localized image sets. Keep composition and visual meaning consistent while localizing only the visible copy.
- Generate raster artwork with the `imagegen` skill and use existing series images as visual references.
- Preserve the established visual identity: crisp retro 16-bit pixel art, warm cream background, near-black outlines, burnt Git-orange accents, restrained brown details, and a nostalgic RPG field-guide mood.
- Preserve recurring character continuity: the orange specimen creature and the pixel-art explorer should remain recognizable across posts.
- Thumbnails must use a wide landscape composition, large readable title text, strong hierarchy, and safe margins suitable for Velog and Medium cards.
- Body illustrations should explain or dramatize the nearby section rather than repeat the thumbnail.
- Avoid photorealism, glossy 3D, neon colors, gradients, corporate logos, watermarks, tiny decorative copy, and unnecessary interface clutter.
- Treat all visible image text as exact copy. Verify Korean spelling, English spelling, punctuation, series number, observation number, and next-topic labels before accepting an image.

## Image files and Markdown

- Store images in the post's local `images/` directory; never leave a referenced final asset only in a generated-image or temporary directory.
- Follow filenames already referenced by the Markdown. For English-localized assets, use the existing `.en.png` convention.
- Do not overwrite an existing image unless the user explicitly requests replacement. Use a versioned sibling such as `.v2.png` when preserving the original.
- After generating images, update the relevant Markdown image paths and meaningful alt text.
- Confirm that every Markdown image reference resolves to an existing file.

## Editing constraints

- Preserve frontmatter fields, document language, heading structure, and intentional links unless the requested task requires changing them.
- Do not publish, upload, create a pull request, merge branches, or message external services without explicit user authorization.
- Keep unrelated user changes intact.
- At handoff, report the changed document paths, generated image paths, and any remaining review items.
