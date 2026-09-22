# Content & Publishing Workflow

## Repository role

- **GitHub**: Version-controls the Markdown drafts and AI-generated images.
- **Google Drive**: Backs up the same content deliverables for review and sharing.
- **Notion**: Manages the project and its weekly sprints.
- **Linear**: Manages the actual execution issues.
- **Slack**: Delivers draft-preparation, sync, and failure notifications.

## Weekly cycle

One draft is prepared per week, and **publish day is every Monday**. Each week follows the same seven-step process tracked in Linear.

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
Push to GitHub (feat branch → PR) + Google Drive backup
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
- Set a draft's frontmatter `date` to the actual upcoming Monday it's scheduled to publish.
- **Google Drive backup**: at the same point content is pushed to GitHub, save that week's `index.ko.md`/`index.en.md` as plain markdown (not converted to Google Docs — conversion breaks markdown syntax) under `My Drive/Developer/Project/codigdex-blog/2026/09/<repo folder name>/`. Images are not uploaded by Claude directly due to size — drag the local `images/` folder into the same location by hand.

## Running on Linear cycles

The weekly repeating process runs on Linear cycles. Team `COD` uses one-week cycles that **start Monday 00:00 KST and end on Sunday**.

- **One cycle = one weekly post.** The week's parent issue and its sub-issues belong to the cycle in which the **draft is written**. Publish day (Monday) is the first day of the next cycle, so only the publish sub-issue carries over.
  - Example: `#005` (publishes 2026-09-28) belongs to Cycle 3 (09/21-09/27), and its `Publish on Velog/Medium` sub-issue is completed in Cycle 4.
- New issues land in whichever cycle is active when they are created. Issues created by the `Prepare feature PR` automation set the active cycle explicitly.
- Unfinished issues roll over to the next cycle when a cycle closes. A whole parent issue rolling over is the signal that the week slipped.
- Cycles are shared across team `COD`, so issues from other projects appear in the same cycle. Filter the cycle view by the `블로그 자동발행` project to see only blog progress.

## Branch integration

Reviewed changes are merged from a `feat/*` branch into `develop` through a pull request, then from `develop` into `main` through another pull request. See [Git branch strategy](GIT_WORKFLOW.md) for details.

## Tracking progress

- Linear: a parent issue per week plus its standard sub-issues track progress, and each week is assigned to a cycle.
- Notion Sprint Tracker: each week is registered as one sprint with its objective, duration, and deliverables.
- Slack (#codigdex-blog): status notifications for draft prep, sync, and publish failures.
