# 저장소 구조 & 작성 가이드

## 폴더 구조

```
posts/
  YYYY/
    MM/
      #NNN_post-slug/
        index.ko.md
        index.en.md
        images/
          thumbnail.png
          thumbnail.en.png
          01-body-image.png
          01-body-image.en.png
templates/
  post-template.ko.md
  post-template.en.md
```

각 글은 언어별 Markdown 파일(`index.ko.md` → Velog, `index.en.md` → Medium)과 언어별 이미지를 하나의 폴더에 함께 보관합니다. 폴더명은 해당 주차 개체의 코딩 도감 번호(세 자리, 게임 codigdex의 `dexNumber`와 동일)를 접두사로 붙인 `#NNN_post-slug` 형식을 사용합니다(예: `#001_git`). 셸에서는 경로를 따옴표로 감쌉니다. Markdown에서는 `./images/파일명` 형태의 상대 경로를 사용합니다.

## 에이전트 설정 (`.claude/`)

Claude Code가 이 저장소에서 따르는 규칙은 `CLAUDE.md`를 짧게 유지하기 위해 역할별 폴더로 나눠 둡니다. Codex는 `AGENTS.md`를 읽고, 거기서 안내하는 같은 규칙 파일을 따릅니다.

| 폴더 | 역할 | 예 |
| --- | --- | --- |
| `.claude/rules/` | 주제 하나당 파일 하나인 규칙 | `series-voice.md`, `images.md`, `git-pr-policy.md`, `tracking.md` |
| `.claude/skills/` | 순서가 있는 절차 | `weekly-post`, `weekly-images`, `publish-followup`, `chapter-release` |
| `.claude/hooks/` | 절대 어기면 안 되는 규칙을 코드로 차단 (`.claude/settings.json`에 연결) | `develop`/`main` 직접 push 차단, 기존 이미지 덮어쓰기 차단, `No.001` 표기 차단 |
| `.claude/agents/` | 출력이 긴 작업을 맡는 서브에이전트 | `post-checker`, `tracker-auditor` |

## 글 작성 가이드

새 글은 `templates/post-template.ko.md`(Velog 발행용)와 `templates/post-template.en.md`(Medium 발행용)를 각각 복사해서 시작합니다. Front matter는 다음 필드를 포함합니다.

- `title`, `description`, `tags`
- `date` (YYYY-MM-DD), `status` (`draft` → 발행 후 갱신)

본문 구성은 다음 순서를 기본으로 합니다.

1. **들어가며** — 글의 배경과 독자가 얻게 될 내용
2. **본문** — 실제 내용, 필요한 경우 이미지와 도입 문장을 함께 배치
3. **마치며** — 핵심 요약과 다음 행동/참고 자료
4. **References** — 참고 자료

## 시리즈 & 제목 규칙

여러 주차에 걸친 연재는 시리즈 번호를 제목에 명시합니다. 예: `코딩 도감 #01 — 코딩 도감을 시작하며`. 하나의 `#번호`는 하나의 "챕터(주제)"를 의미하며 여러 주차에 걸쳐 이어지고, 각 주차는 `NO.001`처럼 도감 번호가 붙은 개체 하나를 관찰해 글 마지막에 등록합니다. 시리즈 운영 방식은 [로드맵 / 시리즈 계획](ROADMAP.md)을 참고하세요.

## 이미지 규칙

- 이미지는 별도로 준비한 뒤 `images/` 폴더에 함께 커밋합니다.
- PNG 형식을 기본으로 사용합니다.
- 한국어 기본 이미지와 구도를 맞춘 영어 현지화 이미지는 같은 `images/` 폴더에 두고, 영어 파일명에 `.en.png` 접미사를 붙입니다.
- 각 이미지 삽입 전에는 문맥을 잇는 짧은 도입 문장을 작성합니다.
- 파일이 손상되지 않았는지(PNG 시그니처 등) 커밋 후 반드시 확인합니다.
