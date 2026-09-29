---
paths:
  - "posts/**"
  - "templates/**"
  - "docs/**/ROADMAP.md"
---

# Codigdex series voice

## Voice

- Treat development concepts, tools, errors, and debugging experiences as specimens that are discovered, observed, and recorded.
- Use an approachable first-person learning-log voice rather than textbook prose.
- Explain the mental model before listing commands.
- Keep headings, specimen information, observations, summary, and the closing Codigdex note consistent with nearby posts.
- Preserve continuity with the previous observation. Preview the next one only when the roadmap or the user confirms it.

## Naming and numbering

- Korean uses `코딩 도감`; English uses `Codigdex` — a localized coinage, never the transliteration "Coding Dogam" or "Coding Encyclopedia". The name was deliberated twice; do not propose a rename unless a concrete collision surfaces.
- A `#NN` series is a **chapter**; each week registers one **specimen** `NO.00x`.
- Write dex numbers uppercase as `NO.001` in Markdown. `No.001` renders oddly on Velog/Medium (enforced by a hook). Text baked into images may still read `No. 004`.
- Dex numbers follow the user's game repo (`github.com/codingnanyong/codigdex`, `web/lib/domain/chapters/*.ts` `dexNumber`). Git = NO.001–005, Linux = NO.006–010. Re-read the game repo before numbering later chapters, because unreleased chapters' numbers shift.
- The first bullet of `## 개체 정보` / `## Specimen info` is `- 도감 번호: NO.00N <이름>` / `- Dex number: NO.00N <English name>`. A chapter's final week registers its last specimen and frames it as completing the chapter.

## English localization

- Write `index.en.md` as a natural localization that preserves the Korean article's meaning, structure, code, and image sequence.
- Reuse the established vocabulary from `docs/eng/ROADMAP.md`: specimen (개체), encounter (조우/만남), observation (관찰), and "dex" as the common noun.
- Localize other coined Korean terms into natural English coinages rather than transliterations.
