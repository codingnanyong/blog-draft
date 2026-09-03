# 저장소 구조 & 작성 가이드

## 폴더 구조

```
posts/
  YYYY/
    MM/
      post-slug/
        index.ko.md
        index.en.md
        images/
          cover.webp
          diagram-01.webp
templates/
  post-template.ko.md
  post-template.en.md
```

각 글은 언어별 Markdown 파일(`index.ko.md` → Velog, `index.en.md` → Medium)과 두 언어가 공유하는 이미지를 하나의 폴더에 함께 보관합니다. Markdown에서는 `./images/파일명` 형태의 상대 경로를 사용합니다.

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

여러 주차에 걸친 연재는 시리즈 번호를 제목에 명시합니다. 예: `코딩 도감 #01 — 코딩 도감을 시작하며`. 하나의 `#번호`는 하나의 "개체(주제)"를 의미하며, 여러 주차에 걸쳐 이어질 수 있습니다. 시리즈 운영 방식은 [로드맵 / 시리즈 계획](ROADMAP.md)을 참고하세요.

## 이미지 규칙

- 이미지는 별도로 준비한 뒤 `images/` 폴더에 함께 커밋합니다.
- 각 이미지 삽입 전에는 문맥을 잇는 짧은 도입 문장을 작성합니다.
- 파일이 손상되지 않았는지(PNG 시그니처 등) 커밋 후 반드시 확인합니다.
