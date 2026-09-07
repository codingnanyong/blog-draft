# Roadmap / Series Plan

## The "Codigdex" series concept

Like a Pokédex, each series (`#number`) covers one technical "specimen." A specimen is learned step by step over several weeks, from the basics to practical use, and the final week wraps up by formally registering that specimen in the "Codigdex."

## #01 — Git (5-week plan)

| Week | Topic | Publish Date | Linear | Status |
| --- | --- | --- | --- | --- |
| Week 1 | Git basics — first encounter | 2026-09-03 | COD-41 | Published |
| Week 2 | Git branching and merging | 2026-09-07 | COD-42 | Published |
| Week 3 | Undoing changes & merge conflicts | 2026-09-14 | COD-53 | Drafted (awaiting publish) |
| Week 4 | Remote repositories & rebase | 2026-09-21 | COD-54 | Drafted |
| Week 5 | Collaboration workflow (wrap-up) | 2026-09-28 | COD-55 | Drafted |

Each week follows the same process defined in [Git branch strategy](GIT_WORKFLOW.md) and [Content & publishing workflow](WORKFLOW.md). Once week 5 wraps up, the Git specimen is formally registered in the Codigdex, and topic selection begins for the next specimen (`#02`).

## #02 — Docker (5-week plan, draft)

The user has picked Docker as the next specimen. Below is a proposed curriculum following the same "basics → applied → collaboration/real-world" three-stage structure as Git — not yet confirmed.

| Week | Topic | Publish Date | Linear | Status |
| --- | --- | --- | --- | --- |
| Week 1 | Docker basics — first encounter (images, containers, Dockerfile) | 2026-10-05 | TBD | Proposed |
| Week 2 | Building images & layers (writing a Dockerfile, layer caching, multi-stage builds) | 2026-10-12 | TBD | Proposed |
| Week 3 | Volumes & networking (data persistence, container-to-container communication) | 2026-10-19 | TBD | Proposed |
| Week 4 | Docker Compose (multi-container orchestration) | 2026-10-26 | TBD | Proposed |
| Week 5 | Real-world collaboration workflow (registries, CI/CD integration, wrap-up registration) | 2026-11-02 | TBD | Proposed |

Once this 5-week breakdown is confirmed, Linear issues (parent + standard sub-issues) and Notion sprints will be created.

## Criteria for picking the next specimen

- A technology or tool used repeatedly in practice, worth revisiting from the basics
- A topic with enough of a learning curve to split into roughly 4-5 weeks
- A topic that naturally splits into a "basics → applied → collaboration/real-world" three-stage structure, like Git

## Where it's tracked

- Linear: a parent issue per week (e.g. COD-42, COD-53-55) plus 7 standard sub-issues
- Notion Sprint Tracker: each week is registered as Sprint 02-05 with its objective, duration, and deliverables
