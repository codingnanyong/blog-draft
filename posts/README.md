# Posts

글 하나당 하나의 폴더를 사용합니다. 언어별 버전(한국어 → Velog, 영어 → Medium)은 같은 폴더 안에서 파일만 나눕니다.

예시:

```text
posts/2026/09/#001_git/
├── index.ko.md
├── index.en.md
└── images/
    ├── thumbnail.png
    ├── thumbnail.en.png
    ├── 01-git-encounter.png
    └── 01-git-encounter.en.png
```

폴더명은 해당 주차 개체의 코딩 도감 번호(세 자리, 게임 [codigdex](https://github.com/codingnanyong/codigdex)의 `dexNumber`와 동일)를 접두사로 붙인 `#NNN_post-slug` 형식으로 작성합니다. 예: 1주차 깃새싹(NO.001) → `#001_git`. 셸에서는 `#`이 주석으로 해석되므로 경로를 따옴표로 감쌉니다(`"posts/2026/09/#001_git"`). 접두사 뒤의 슬러그는 영문 소문자와 하이픈을 사용합니다.

이미지는 PNG 형식을 기본으로 하고 해당 글의 `images/` 폴더에 보관합니다. 한국어 기본 이미지와 구도를 맞춘 영어 현지화 이미지는 같은 폴더에 두며, 영어 파일에는 `.en.png` 접미사를 사용합니다. Google Drive에도 같은 폴더 구조로 저장합니다.
