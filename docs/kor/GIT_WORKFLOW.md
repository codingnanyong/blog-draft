# Git 브랜치 전략

브랜치 흐름, 브랜치 이름, PR 규칙, Linear 연동 등 기본 정책은 [`.claude/rules/git-pr-policy.md`](../../.claude/rules/git-pr-policy.md)를 따릅니다 (repo-template과 공유하는 범용 정책이라 여기서 중복 설명하지 않습니다).

## 이 저장소 고유 사항

### PR 라벨·마일스톤·담당자

모든 PR(`feat/*` → `develop`, `develop` → `main`)에는 `.github/workflows/pr-metadata.yml`이 자동으로 메타데이터를 붙입니다. 붙일 수 없으면 체크가 실패합니다. 규칙 원문은 [`.claude/rules/git-pr-policy.md`의 PR metadata](../../.claude/rules/git-pr-policy.md#pr-metadata-automated)에 있습니다.

| 항목 | 규칙 |
| --- | --- |
| 타입 라벨 | PR 제목(`COD-<n>` 다음)의 접두사로 결정: `content:` `docs:` `feat:` `fix:` `ci:` `chore:` `test:` → `type: …` |
| 흐름 라벨 | `develop` 대상 `flow: feature`, `main` 대상 `flow: sync` |
| 마일스톤 | 진행 중인 챕터 = 열린 `코딩 도감 #NN <챕터명>` 중 마감일이 가장 가까운 것 (마감일 = 챕터 마지막 발행 월요일) |
| 담당자 | `codingnanyong` |

- 미러 GitHub 이슈에도 같은 타입 라벨, 마일스톤, 담당자가 붙습니다.
- 다음 챕터의 로드맵이 정해지면 마일스톤을 미리 만듭니다. 챕터 Release를 발행할 때 그 챕터의 마일스톤을 닫습니다.
- `feat/*` PR이 `develop`에 병합되면 워크플로가 head 브랜치를 삭제합니다. 저장소 전체 자동 삭제 설정은 `main` 동기화 PR 병합 때 `develop`까지 지우므로 켜지 않습니다.

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
- Release를 발행하거나 갱신하면 해당 챕터의 마일스톤을 닫습니다
