# Content & Publishing Workflow

## Repository role

- **GitHub**: Version-controls the Markdown drafts and AI-generated images.
- **Google Drive**: Backs up the same content deliverables for review and sharing.
- **Notion**: Manages the project and its weekly sprints.
- **Linear**: Manages the actual execution issues.
- **Slack**: Delivers draft-preparation, sync, and failure notifications.

## Weekly cycle

One draft is prepared per week. Each week follows the same six-step process tracked in Linear.

```
Pick a topic
   │
   ▼
Write the draft (Claude)
   │
   ▼
User review & feedback
   │
   ▼
Push to GitHub (feat branch → PR)
   │
   ▼
Merge PR (develop)
   │
   ▼
Publish on Velog (Korean) / Medium (English) & update the log
```

- AI-generated text and images are always reviewed by a human before publishing.
- Images are prepared separately and placed in the draft with a short lead-in sentence for context.
- The Korean draft (`index.ko.md`) is published on Velog; the English translation (`index.en.md`) is published on Medium. The English translation isn't required every week — it can be done selectively per installment.
- Publishing on either platform is done manually; the log (Notion Sprint Tracker) is updated right after.

## Branch integration

Reviewed changes are merged from a `feat/*` branch into `develop` through a pull request, then from `develop` into `main` through another pull request. See [Git branch strategy](GIT_WORKFLOW.md) for details.

## Tracking progress

- Linear: a parent issue per week plus 6 standard sub-issues track progress.
- Notion Sprint Tracker: each week is registered as one sprint with its objective, duration, and deliverables.
- Slack (#velog-automation): status notifications for draft prep, sync, and publish failures.
