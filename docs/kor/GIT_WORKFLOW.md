# Git 브랜치 전략

## 브랜치 흐름

```
feat/<slug> ── push ──> Linear 이슈 + GitHub 미러 이슈
                              │ 자동 Draft PR
                              ▼
                           develop
                              │ PR
                              ▼
                            main
```

`develop`과 `main`에 대한 직접 push는 지양하고, 항상 Pull Request를 통해 반영합니다.

## 브랜치 이름

- 기본 형식: `feat/<slug>`
- 예시: `feat/codigdex-git`
- 기존 Linear 이슈를 재사용할 때: `feat/cod-<linear-id>-<slug>`
- 하나의 브랜치는 하나의 주차(=하나의 Linear 서브이슈 묶음)에 대응합니다.

## Pull Request 규칙

- `feat/*` → `develop`
  - 최초 push 시 자동화가 Linear/GitHub 이슈 쌍과 Draft PR을 생성합니다.
  - PR 제목에는 관련 Linear 이슈 번호가 포함됩니다(예: `COD-41`).
  - PR 본문에는 `Closes COD-41`과 GitHub 미러 이슈의 `Closes #번호`가 포함됩니다.
- `develop` → `main`
  - 검토가 끝난 발행 준비 원고를 모아서 반영합니다.
  - 병합 후 Velog에 수동으로 발행하고, Notion Sprint Tracker에 발행 로그를 남깁니다.

## Linear 연동

- 각 주차는 Linear에 부모 이슈 + 6개 표준 서브이슈로 등록됩니다: 주제 선정 → 초안 작성 (Claude) → 사용자 검토 & 피드백 반영 → GitHub 반영 (feat 브랜치 → PR) → PR 병합 (develop) → Velog 발행 & 로그 업데이트.
- GitHub 브랜치/PR과 Linear 이슈는 서로 참조하여 추적성을 유지합니다.
- 자동화가 실패하면 Actions의 `Prepare feature PR`을 같은 브랜치로 다시 실행합니다. 이슈 생성은 저장소와 브랜치 조합을 기준으로 재사용됩니다.

## 이미지/바이너리 커밋 주의사항

바이너리 파일(이미지 등)은 텍스트 편집기 기반 커밋으로 손상될 수 있으므로, GitHub의 "Upload files" 업로드 화면(또는 동등한 바이너리 안전 경로)을 사용해 커밋합니다. 커밋 후에는 raw 파일의 시그니처를 확인해 손상 여부를 검증합니다.
