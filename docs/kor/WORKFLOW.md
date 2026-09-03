# 콘텐츠 & 발행 워크플로

## 저장소 역할

- **GitHub**: Markdown 초안과 AI 생성 이미지를 버전 관리합니다.
- **Google Drive**: 동일한 콘텐츠 산출물을 백업하고 검토·공유합니다.
- **Notion**: 프로젝트와 주간 Sprint를 관리합니다.
- **Linear**: 실제 실행 Issue를 관리합니다.
- **Slack**: 초안 준비, 동기화 및 실패 알림을 전달합니다.

## 주간 사이클

매주 1개의 초안을 준비합니다. 각 주차는 Linear에 등록된 아래 6단계 표준 프로세스를 따릅니다.

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
GitHub 반영 (feat 브랜치 → PR)
   │
   ▼
PR 병합 (develop)
   │
   ▼
Velog 발행 & 로그 업데이트
```

- AI가 생성한 본문과 이미지는 발행 전에 반드시 사람이 검토합니다.
- 이미지는 별도로 준비되며, 문맥에 맞는 도입 문장과 함께 본문에 배치합니다.
- Velog 최종 발행은 수동으로 진행하며, 발행 후 로그(Notion Sprint Tracker)를 갱신합니다.

## 브랜치 반영

검토가 완료된 변경은 `feat/*` 브랜치에서 `develop`으로 Pull Request를 통해 반영하고, 이후 `develop`에서 `main`으로 다시 Pull Request를 통해 반영합니다. 자세한 규칙은 [Git 브랜치 전략](GIT_WORKFLOW.md)을 참고하세요.

## 진행 상황 추적

- Linear: 주차별 부모 이슈 + 6개 표준 서브이슈로 진행 상황을 관리합니다.
- Notion Sprint Tracker: 각 주차를 하나의 Sprint로 등록해 목표·기간·산출물을 관리합니다.
- Slack (#velog-automation): 초안 준비/동기화/발행 실패 등 상태 알림을 전달합니다.
