# 콘텐츠 & 발행 워크플로

## 저장소 역할

- **GitHub**: Markdown 초안과 AI 생성 이미지를 버전 관리합니다.
- **Google Drive**: 동일한 콘텐츠 산출물을 백업하고 검토·공유합니다.
- **Notion**: 프로젝트와 주간 Sprint를 관리합니다.
- **Linear**: 실제 실행 Issue를 관리합니다.
- **Slack**: 초안 준비, 동기화 및 실패 알림을 전달합니다.

## 주간 사이클

매주 1개의 초안을 준비하며, **발행일은 매주 월요일**입니다. 각 주차는 Linear에 등록된 아래 7단계 표준 프로세스를 따릅니다.

```
주제 선정
   │
   ▼
초안 작성 (Claude)
   │
   ▼
사용자 검토 & 피드백 반영
   │
   ▼
GitHub 반영 (feat 브랜치 → PR) + Google Drive 백업
   │
   ▼
PR 병합 (develop)
   │
   ▼
Velog(한국어) / Medium(영어) 발행 & 로그 업데이트
```

- AI가 생성한 본문과 이미지는 발행 전에 반드시 사람이 검토합니다.
- 이미지는 별도로 준비되며, 문맥에 맞는 도입 문장과 함께 본문에 배치합니다.
- 한국어 원고(`index.ko.md`)는 Velog에, 영어 번역본(`index.en.md`)은 Medium에 발행합니다. 영어 번역은 매주 필수는 아니며, 회차별로 선별해 진행할 수 있습니다.
- 두 플랫폼 모두 최종 발행은 수동으로 진행하며, 발행 후 로그(Notion Sprint Tracker)를 갱신합니다.
- 초안 frontmatter의 `date`는 실제 발행 예정 월요일 날짜로 설정합니다.
- **Google Drive 백업**: GitHub에 반영하는 시점에 같은 주차의 `index.ko.md`/`index.en.md`를 `My Drive/Developer/Project/codigdex-blog/2026/09/<저장소 폴더명>/`에 원본 마크다운 그대로 저장합니다 (Google Docs로 변환하지 않음 — 변환 시 마크다운 문법이 깨짐). 이미지는 용량 문제로 Claude가 직접 업로드하지 않고, 로컬 `images/` 폴더를 같은 위치로 드래그하여 사람이 직접 옮깁니다.

## Linear Cycle 운영

주간 반복 프로세스는 Linear Cycle 위에서 굴립니다. 팀 `COD`의 Cycle은 1주 단위이며, **월요일 00:00 KST에 시작해 일요일에 끝납니다**.

- **1 Cycle = 1 주차 포스트.** 주차 부모 이슈와 하위 이슈는 그 포스트의 **초안을 작성하는 주의 Cycle**에 배정합니다. 발행일인 월요일은 다음 Cycle의 첫날이므로, 발행 하위 이슈만 다음 Cycle로 넘어갑니다.
  - 예: `#005`(발행 2026-09-28)는 Cycle 3(09/21~09/27)에 배정하고, `Velog·Medium 발행` 하위 이슈는 Cycle 4에서 완료합니다.
- 새로 만든 이슈는 생성 시점의 활성 Cycle에 배정됩니다. `Prepare feature PR` 자동화가 만드는 이슈도 활성 Cycle을 명시적으로 지정합니다.
- 미완료 이슈는 Cycle이 끝날 때 다음 Cycle로 이월됩니다. 주차 부모 이슈가 통째로 이월됐다면 그 주차가 밀렸다는 신호입니다.
- Cycle은 팀 `COD` 전체가 공유하므로 블로그 외 프로젝트 이슈도 같은 Cycle에 들어옵니다. 블로그 진행 상황만 보려면 Cycle 뷰를 프로젝트 `블로그 자동발행`으로 필터링합니다.

## 브랜치 반영

검토가 완료된 변경은 `feat/*` 브랜치에서 `develop`으로 Pull Request를 통해 반영하고, 이후 `develop`에서 `main`으로 다시 Pull Request를 통해 반영합니다. 자세한 규칙은 [Git 브랜치 전략](GIT_WORKFLOW.md)을 참고하세요.

## 진행 상황 추적

- Linear: 주차별 부모 이슈 + 표준 서브이슈로 진행 상황을 관리하고, 각 주차를 Cycle에 배정해 주간 흐름을 추적합니다.
- Notion Sprint Tracker: 각 주차를 하나의 Sprint로 등록해 목표·기간·산출물을 관리합니다.
- Slack (#codigdex-blog): 초안 준비/동기화/발행 실패 등 상태 알림을 전달합니다.
