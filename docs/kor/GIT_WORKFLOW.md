# Git 브랜치 전략

브랜치 흐름, 브랜치 이름, PR 규칙, Linear 연동 등 기본 정책은 [AGENTS.md의 PR & issue policy](../../AGENTS.md#pr--issue-policy)를 따릅니다 (repo-template과 공유하는 범용 정책이라 여기서 중복 설명하지 않습니다).

## 이 저장소 고유 사항

### 이미지/바이너리 커밋 주의사항

바이너리 파일(이미지 등)은 텍스트 편집기 기반 커밋으로 손상될 수 있으므로, GitHub의 "Upload files" 업로드 화면(또는 동등한 바이너리 안전 경로)을 사용해 커밋합니다. 커밋 후에는 raw 파일의 시그니처를 확인해 손상 여부를 검증합니다.

### `main` PR과 챕터 단위 Release

`develop` → `main` PR은 검토가 끝난 원고를 모아서 반영하는 용도이며, 주차별 PR에는 release 게이트가 없습니다. 병합 후 Velog/Medium에 수동으로 발행하고 Notion Sprint Tracker에 로그를 남깁니다.

태그와 GitHub Release는 **하나의 챕터(`#번호`)의 모든 주차 원고가 `main`에 반영됐을 때** 한 번 발행합니다.

- 태그 이름: `codigdex-<챕터 번호 두 자리>-<챕터 슬러그>` (예: `codigdex-01-git`, `codigdex-02-linux`)
- 태그 대상: 해당 챕터의 마지막 원고가 반영된 `main` 병합 커밋
- Release 제목: `코딩 도감 #NN <챕터명> — 챕터 등록 완료`
- Release 본문: 주차별 등록 개체 표(도감 번호 `NO.00x`·개체명·특성·글 제목·폴더·발행일·발행 상태), 챕터를 거치며 바뀐 운영 규칙, 다음 챕터 예고, 짧은 영어 요약
- 태그를 만든 뒤 같은 챕터의 원고가 다시 `main`에 반영되면, 태그를 최신 `main` 병합 커밋으로 옮기고 Release 본문도 함께 갱신합니다
