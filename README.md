# Velog Draft

매주 1개의 Velog 기술 블로그 글을 준비하고, 사람이 검토한 뒤 발행하기 위한 콘텐츠 저장소입니다.

## Repository role

- GitHub: Markdown 초안과 AI 생성 이미지를 버전 관리합니다.
- Google Drive: 동일한 콘텐츠 산출물을 백업하고 검토·공유합니다.
- Notion: 프로젝트와 주간 Sprint를 관리합니다.
- Linear: 실제 실행 Issue를 관리합니다.
- Slack: 초안 준비, 동기화 및 실패 알림을 전달합니다.

## Content structure

```text
posts/
  YYYY/
    MM/
      post-slug/
        index.md
        images/
          cover.webp
          diagram-01.webp
templates/
  post-template.md
```

각 글은 Markdown 파일과 해당 글에서 사용하는 이미지를 하나의 폴더에 함께 보관합니다. Markdown에서는 `./images/파일명` 형태의 상대 경로를 사용합니다.

## Publishing policy

- 매주 1개의 초안을 준비합니다.
- AI가 생성한 내용과 이미지는 발행 전에 사람이 검토합니다.
- Velog 최종 발행은 수동으로 진행합니다.
- 검토가 완료된 변경은 `develop`에서 `main`으로 Pull Request를 통해 반영합니다.
