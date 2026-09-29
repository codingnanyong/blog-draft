# Repository Structure & Writing Guide

## Folder layout

```
posts/
  YYYY/
    MM/
      #NNN_post-slug/
        index.ko.md
        index.en.md
        images/
          thumbnail.png
          thumbnail.en.png
          01-body-image.png
          01-body-image.en.png
templates/
  shared-post-template.ko.md
  shared-post-template.en.md
```

Each post keeps its per-language Markdown files (`index.ko.md` for Velog, `index.en.md` for Medium) and localized images together in one folder. Folder names use the `#NNN_post-slug` format, where `NNN` is the three-digit Codigdex dex number of that week's specimen (the same `dexNumber` as the codigdex game), e.g. `#001_git`. Quote these paths in a shell, since `#` otherwise starts a comment. Markdown references images with a relative path in the form `./images/filename`.

## Agent configuration (`.agents/`)

The rules shared by Claude and Codex are split by role under `.agents/`. Codex reads `AGENTS.md`, while Claude Code reads `CLAUDE.md`; both point to the same shared assets.

| Folder | Role | Examples |
| --- | --- | --- |
| `.agents/rules/` | Shared rules, one topic per file | `shared-series-voice.md`, `shared-images.md`, `shared-git-pr-policy.md`, `shared-tracking.md` |
| `.agents/skills/` | Shared step-by-step procedures | `shared-weekly-post`, `shared-weekly-images`, `shared-publish-followup`, `shared-chapter-release` |
| `.agents/hooks/` | Must-never rules blocked in code (wired in `.claude/settings.json`) | `shared-guards.py`, `shared-git-hook.py`, `claude-guard.py` |
| `.agents/agents/` | Claude-only subagents for long-output work | `claude-post-checker.md`, `claude-tracker-auditor.md` |

Shared support assets use `shared-<name>` by default; agent-specific assets use `claude-<name>` or `codex-<name>`. Skill and plugin prefixes belong on their subfolder names. Required entrypoint and manifest names such as `README.md` and `SKILL.md` stay unchanged.

## Writing guide

Start a new post by copying `templates/shared-post-template.ko.md` (for Velog) and `templates/shared-post-template.en.md` (for Medium). The front matter includes:

- `title`, `description`, `tags`
- `date` (YYYY-MM-DD), `status` (`draft` → updated after publishing)

The body follows this default structure:

1. **Introduction** — background and what the reader will get out of the post
2. **Body** — the actual content, with images placed alongside a short lead-in sentence where needed
3. **Closing** — a summary of the key points plus next steps or references
4. **References** — supporting material

## Series & title convention

A multi-week series states its series number in the title, e.g. `Codigdex #01 — Starting the Codigdex`. One `#number` represents one "chapter" (topic) spanning several weeks, and each week observes one dex-numbered specimen such as `NO.001` and registers it at the end of the post. See [Roadmap / series plan](ROADMAP.md) for how a series is run.

## Image rules

- Images are prepared separately, then committed together under an `images/` folder.
- Use PNG as the default image format.
- Keep the Korean base image and its composition-matched English localization in the same `images/` folder, adding the `.en.png` suffix to the English filename.
- Write a short lead-in sentence before each image to keep the prose connected.
- Always verify the committed files aren't corrupted (e.g. check the PNG signature) after pushing.
