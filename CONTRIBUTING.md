# Contributing

## 한국어

이 저장소는 codingnanyong 1인이 작성·검토하는 블로그 초안 저장소로, 외부 Pull Request는 받지 않습니다. 다만 오탈자, 깨진 링크, 기술적 오류를 발견하셨다면 Issue로 알려주시면 감사하겠습니다.

### 내부 작업 절차

`develop`으로 가는 모든 PR은 Linear·GitHub 미러 이슈 한 쌍을 요구합니다 (CI가 강제):

1. Linear `COD` 팀에 이슈 생성
2. 저장소에 `COD-<n> <제목>` 형식의 미러 GitHub 이슈 생성
3. `feat/cod-<n>-<slug>` 브랜치에서 작업
4. PR 제목은 `COD-<n>`으로 시작, 본문에 `Closes COD-<n>`과 `Closes #<n>` 포함
5. `main`은 `develop`에서만

자세한 내용은 [AGENTS.md](AGENTS.md#pr--issue-policy) 참고.

## English

This repository is a personal blog draft workspace written and reviewed solely by codingnanyong; external pull requests are not accepted. That said, if you spot a typo, a broken link, or a technical inaccuracy, please open an Issue — it's genuinely welcome.

### Internal workflow

Every PR into `develop` requires a mirrored Linear/GitHub issue pair (CI-enforced):

1. Create a Linear issue in the `COD` team
2. Create a mirrored GitHub issue titled `COD-<n> <title>`
3. Work on `feat/cod-<n>-<slug>`
4. PR title starts with `COD-<n>`; body includes both `Closes COD-<n>` and `Closes #<n>`
5. `main` only accepts PRs from `develop`

See [AGENTS.md](AGENTS.md#pr--issue-policy) for details.
