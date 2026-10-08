# Linear, Notion, and Slack tracking

## Scope

Linear team `COD` cycles and the Notion Sprint Tracker are shared with other projects (the Codigdex game, 부산 IMD). In this repo, look only at Linear project **블로그 자동발행** and Notion rows named `블로그 자동발행 · Sprint …`. Do not report, move, or change the other projects' items.

## Linear

- Each week is one parent issue plus six standard sub-issues: 주제 선정 / 초안 작성 (Claude) / 사용자 검토 & 피드백 반영 / GitHub 반영 (feat 브랜치 → PR) / PR 병합 (develop) / Velog·Medium 발행 & 로그 업데이트. They come from the team template **주간 포스트 (코딩 도감)** through a recurring issue.
- Cycles are one week, starting Monday 00:00 KST. The weekly parent belongs to the cycle in which its draft is written. The publish sub-issue finishes in the next cycle.
- **Merge is not publish.** Merging the draft PR auto-closes the week's parent through Linear's GitHub integration while the post is still unpublished. Reopen the parent to In Progress and leave `Velog·Medium 발행 & 로그 업데이트` at Todo until the user reports publication.
- The free plan caps active issues at 250. Finished issues auto-archive after one month.
- API access: `LINEAR_API_KEY` in the local `.env` (GraphQL at `https://api.linear.app/graphql`).

## Notion Sprint Tracker

- Database `72756ff399a8827694c20166e4c780e8`. One row per week, named `블로그 자동발행 · Sprint 0N — 코딩 도감 #NN: <topic>`.
- `Status` (Planned / In Progress / Completed / Delayed) and `Completion %` (0–1) are **not synced** from Linear. Write them by hand: `Completion %` = done sub-issues / 6.
- API access: `NOTION_API_KEY` in `.env`, `Notion-Version: 2022-06-28`.

## Slack and Drive

- Merge notifications go to Slack **#codigdex-blog**. If a message landed there, delivery worked, and a missing ping is a notification setting.
- Drive backups: `My Drive/Developer/Project/codigdex-blog/<YYYY>/<MM>/<post folder>/`.

## After the user reports a post published

When the user accepts a draft for future manual publication, update the existing weekly issue's template title and scope, record completed preparation sub-issues, and create or update the matching Notion Sprint with its Project Record relation. Reflect the same readiness in both roadmaps. Keep the parent In Progress and publication Todo until publication is reported; keep the merge sub-issue open until the PR is actually merged. Compute Notion completion from the six standard sub-issues, and record any scheduled-date mismatch without guessing the actual publication date.

Run the `shared-publish-followup` skill in the same turn. It covers Linear, Notion, the Git status flip, the chapter tag and milestone, and the branch check.
