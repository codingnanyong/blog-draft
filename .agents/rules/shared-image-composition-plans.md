# Durable image composition plans

Use this file with `shared-images.md`. It records the composition decisions that must survive across weeks; the post drafts remain authoritative for the exact teaching point and visible copy.

## Shared visual frame

- Korean is the master composition. English changes text only.
- Use sparse retro 16-bit pixel art, warm cream negative space, thick near-black outlines, burnt-orange accents, and restrained brown details.
- Keep every visible string explicit in the generation prompt. Do not invent small UI copy, pseudo-code, logos, or watermarks.
- The explorer wears an orange cap and jacket, has black hair and a backpack, and holds a field guide. The explorer appears only where the role plan calls for one.

## Role plans

### Thumbnail

- Canvas: wide landscape near `1.91:1` with safe card-crop margins.
- Layout: one large double-border title panel on the left or upper half; one clear explorer/specimen scene on the right or lower half.
- Information density: large series/topic copy only. The scene may be richer than body images but still keeps cream negative space.
- Avoid: tiny captions, crowded scenery, detailed rooms, bookshelves, or multiple competing diagrams.

### 01 — encounter

- Canvas: square `1:1`, sparse classic RPG battle screen.
- Upper left: specimen name, `Lv.<week>`, and exactly one HP bar.
- Stage: explorer at lower left; one specimen or the required specimen group at upper right; otherwise empty cream space.
- Bottom: one large double-border dialogue box containing the encounter line.
- Avoid: scenery, teaching diagrams, command menus, desks, and extra panels.

### 02 — first concept

- Canvas: square `1:1` teaching card.
- Top: one thin double-border title panel.
- Center: one simple two- or three-part comparison using large icons; a small explorer/specimen pair may guide the explanation.
- Bottom: one short takeaway panel.
- Avoid: a second battle screen, long prose, tiny labels, or decorative code.

### 03 — process or second concept

- Canvas: square `1:1` process card.
- Top: one framed title.
- Center: one dominant timeline, path, or flow diagram. The explorer may participate in the process.
- Bottom: one short takeaway panel.
- Keep arrows and states unambiguous; do not mix a battle UI into the diagram.

### 04 — registration

- Canvas: square `1:1` registration card with a thick black/orange frame.
- Header: black `코딩 도감 등록` panel or its English localization.
- Left: a clean specimen portrait containing only the registered specimen or specimen group, centered on a completely blank warm-cream field.
- The portrait window has no explorer, hands, notebook, backpack, hat, props, ground line, soil, grass, plants, rocks, scenery, or cast shadow.
- Right: number/name, type and trait panels, approval stamp, and exactly five progress slots with the current chapter count filled.
- Bottom: full-width black completion panel. Use the individual registration message each week and the whole-chapter completion message only in the final week.
- Never label the card as an observation log.

## Current composition registry

English assets reuse the same composition and replace text only. `thumbnail` files are publication covers even when older Markdown does not embed them in the body.

| Specimen | Thumbnail | 01 encounter | 02 concept | 03 process | 04 registration |
| --- | --- | --- | --- | --- | --- |
| NO.001 Git Sprout | First Git observation with explorer, field guide, and Git Sprout | Wild Git encounter | Working tree / staging / local repository | `add → commit → push` | Git Sprout alone on blank cream; 1/5 |
| NO.002 Branch Twins | Branch and merge topic cover | Branch and Merge appear together | Branch as parallel worlds from one starting point | Merge combines another timeline into the current branch | Branch Twins alone on blank cream; 2/5 |
| NO.003 Conflict Rewinder | Undo and merge-conflict topic cover | Undo tools and merge conflict appear | Compare `reset`, `revert`, and `restore` targets | The moment a merge conflict occurs | Conflict Rewinder group alone on blank cream; 3/5 |
| NO.004 Remote Rebaser | Remote repository and rebase topic cover | Remote and Rebase appear together | Compare `fetch`, `pull`, and `push` | Rebase moves the base point, before/after | Remote Rebaser pair alone on blank cream; 4/5 |
| NO.005 Workflow Guardian | Final Git observation and collaboration workflow | Team workflow encounter | Issue / Branch / Commit agreements | Feature → PR → Review → Main | Workflow Guardian alone on blank cream; all 5/5 filled, Git chapter complete |
| NO.006 Shell Scout | Shell Cave entrance; explorer meets Shell Scout | Shell Scout `Lv.1` RPG encounter | Terminal as input/output window vs shell as command interpreter | Filesystem location flow: `pwd → ls → cd` | Shell Scout alone on blank cream; Linux chapter 1/5 |

## Persistence and versioning

- Never overwrite an accepted asset. Save changes as the next sibling version, such as `.v2.png`; English uses `.en.v2.png`.
- Update both Markdown paths and meaningful alt text after accepting a new version.
- Inspect Korean first, then localize and inspect English. Reject malformed text, composition drift, incorrect specimen identity, or incorrect progress slots.
