# Repository Structure & Writing Guide

## Folder layout

```
posts/
  YYYY/
    MM/
      post-slug/
        index.ko.md
        index.en.md
        images/
          cover.webp
          diagram-01.webp
templates/
  post-template.ko.md
  post-template.en.md
```

Each post keeps its per-language Markdown files (`index.ko.md` for Velog, `index.en.md` for Medium) and the images they share together in one folder. Markdown references images with a relative path in the form `./images/filename`.

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

A multi-week series states its series number in the title, e.g. `Coding Dogam #01 — Starting the Coding Dogam`. One `#number` represents one "specimen" (topic) and can span several weeks. See [Roadmap / series plan](ROADMAP.md) for how a series is run.

## Image rules

- Images are prepared separately, then committed together under an `images/` folder.
- Write a short lead-in sentence before each image to keep the prose connected.
- Always verify the committed files aren't corrupted (e.g. check the PNG signature) after pushing.
