---
paths:
  - "posts/**"
  - "templates/**"
---

# Post folders, frontmatter, and image files

## Folders

- One folder per week: `posts/YYYY/MM/#NNN_<slug>/` where `NNN` is the dex number (e.g. `#005_collaboration-workflow`). Quote these paths in shell commands, because `#` starts a comment.
- Create a week's folder from `templates/shared-post-template.ko.md` / `.en.md` only when that week's draft actually starts. Do not pre-create placeholder folders from the roadmap.
- Each folder holds `index.ko.md` (Velog), `index.en.md` (Medium), and `images/`.

## Frontmatter

- Fields: `title`, `description`, `tags`, `date`, `status`.
- `date` is the Monday the post is scheduled to publish; posts publish every Monday. After a confirmed publish, `date` is the real publish Monday.
- `status` stays `draft` until the user reports the post is published (switching to `published` asks for confirmation through a hook).

## Images

- Every weekly post has five images per language: one thumbnail plus four numbered body images (`01`–`04`). English assets use the same filename with `.en.png`.
- Store images in the post's own `images/` directory; never leave a referenced final asset only in a temporary directory.
- Never overwrite an existing image (enforced by a hook). Save a replacement as a versioned sibling such as `.v2.png`.
- After adding images, update the Markdown image paths and meaningful alt text, and confirm every image reference resolves to an existing file.
- Commit binaries through a binary-safe path and check the raw file signature afterwards.

## Google Drive backup

- When a post is ready to push, back up `index.ko.md` / `index.en.md` as plain Markdown (never converted to Google Docs) to `My Drive/Developer/Project/codigdex-blog/<YYYY>/<MM>/<post folder name>/`, matching the repo folder name exactly.
- Do not upload `images/` yourself; it is too large for the tool payload. Ask the user to drag the local folder into the same Drive location.
