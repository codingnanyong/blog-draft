# Repository Structure & Writing Guide

## Folder layout

```
posts/
  YYYY/
    MM/
      NN-post-slug/
        index.ko.md
        index.en.md
        images/
          thumbnail.png
          thumbnail.en.png
          01-body-image.png
          01-body-image.en.png
templates/
  post-template.ko.md
  post-template.en.md
```

Each post keeps its per-language Markdown files (`index.ko.md` for Velog, `index.en.md` for Medium) and localized images together in one folder. Folder names use the `NN-post-slug` format so posts sort in publication order within each month. Markdown references images with a relative path in the form `./images/filename`.

## Writing guide

Start a new post by copying `templates/post-template.ko.md` (for Velog) and `templates/post-template.en.md` (for Medium). The front matter includes:

- `title`, `description`, `tags`
- `date` (YYYY-MM-DD), `status` (`draft` → updated after publishing)

The body follows this default structure:

1. **Introduction** — background and what the reader will get out of the post
2. **Body** — the actual content, with images placed alongside a short lead-in sentence where needed
3. **Closing** — a summary of the key points plus next steps or references
4. **References** — supporting material

## Series & title convention

A multi-week series states its series number in the title, e.g. `Codigdex #01 — Starting the Codigdex`. One `#number` represents one "specimen" (topic) and can span several weeks. See [Roadmap / series plan](ROADMAP.md) for how a series is run.

## Image rules

- Images are prepared separately, then committed together under an `images/` folder.
- Use PNG as the default image format.
- Keep the Korean base image and its composition-matched English localization in the same `images/` folder, adding the `.en.png` suffix to the English filename.
- Write a short lead-in sentence before each image to keep the prose connected.
- Always verify the committed files aren't corrupted (e.g. check the PNG signature) after pushing.
