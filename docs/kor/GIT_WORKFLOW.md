# Git 브랜치 전략

브랜치 흐름, 브랜치 이름, PR 규칙, Linear 연동 등 기본 정책은 [AGENTS.md의 PR & issue policy](../../AGENTS.md#pr--issue-policy)를 따릅니다 (repo-template과 공유하는 범용 정책이라 여기서 중복 설명하지 않습니다).

## 이 저장소 고유 사항

### 이미지/바이너리 커밋 주의사항

바이너리 파일(이미지 등)은 텍스트 편집기 기반 커밋으로 손상될 수 있으므로, GitHub의 "Upload files" 업로드 화면(또는 동등한 바이너리 안전 경로)을 사용해 커밋합니다. 커밋 후에는 raw 파일의 시그니처를 확인해 손상 여부를 검증합니다.

### `main` PR에 release 게이트 없음

다른 repo-template 기반 저장소와 달리, 이 저장소는 버전 태그/릴리스 개념이 없습니다. `develop` → `main` PR은 검토가 끝난 발행 준비 원고를 모아서 반영하는 용도이며, 병합 후 Velog/Medium에 수동으로 발행하고 Notion Sprint Tracker에 로그를 남깁니다.
