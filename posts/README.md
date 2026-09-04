# Posts

글 하나당 하나의 폴더를 사용합니다. 언어별 버전(한국어 → Velog, 영어 → Medium)은 같은 폴더 안에서 파일만 나눕니다.

예시:

```text
posts/2026/09/01-codigdex-01-git/
├── index.ko.md
├── index.en.md
└── images/
    ├── thumbnail.png
    ├── thumbnail.en.png
    ├── 01-git-encounter.png
    └── 01-git-encounter.en.png
```

폴더명은 월 안에서 글의 순서가 보이도록 두 자리 숫자 접두사를 붙인 `NN-post-slug` 형식으로 작성합니다. 접두사 뒤의 슬러그는 영문 소문자와 하이픈을 사용합니다.

이미지는 PNG 형식을 기본으로 하고 해당 글의 `images/` 폴더에 보관합니다. 한국어 기본 이미지와 구도를 맞춘 영어 현지화 이미지는 같은 폴더에 두며, 영어 파일에는 `.en.png` 접미사를 사용합니다. Google Drive에도 같은 폴더 구조로 저장합니다.
