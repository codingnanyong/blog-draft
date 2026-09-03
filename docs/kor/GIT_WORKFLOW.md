# Git 브랜치 전략

## 브랜치 흐름

```
feat/cod-<linear-id>-<slug>
          │ PR
          ▼
       develop
          │ PR
          ▼
        main
```

`develop`과 `main`에 대한 직접 push는 지양하고, 항상 Pull Request를 통해 반영합니다.

## 브랜치 이름

- 형식: `feat/cod-<linear-id>-<slug>`
- 예시: `feat/cod-41-coding-dogam-git`
- 하나의 브랜치는 하나의 주차(=하나의 Linear 서브이슈 묶음)에 대응합니다.

## Pull Request 규칙

- `feat/*` → `develop`
  - 제목에 관련 Linear 이슈 번호를 포함합니다 (예: `COD-41`).
  - 본문에 변경 내용(주제, 삽입된 이미지, 반영된 피드백)을 간단히 정리합니다.
- `develop` → `main`
  - 검토가 끝난 발행 준비 원고를 모아서 반영합니다.
  - 병합 후 Velog에 수동으로 발행하고, Notion Sprint Tracker에 발행 로그를 남깁니다.

## Linear 연동

- 각 주차는 Linear에 부모 이슈 + 6개 표준 서브이슈로 등록됩니다: 주제 선정 → 초안 작성 (Claude) → 사용자 검토 & 피드백 반영 → GitHub 반영 (feat 브랜치 → PR) → PR 병합 (develop) → Velog 발행 & 로그 업데이트.
- GitHub 브랜치/PR과 Linear 이슈는 서로 참조하여 추적성을 유지합니다.

## 이미지/바이너리 커밋 주의사항

바이너리 파일(이미지 등)은 텍스트 편집기 기반 커밋으로 손상될 수 있으므로, GitHub의 "Upload files" 업로드 화면(또는 동등한 바이너리 안전 경로)을 사용해 커밋합니다. 커밋 후에는 raw 파일의 시그니처를 확인해 손상 여부를 검증합니다.
