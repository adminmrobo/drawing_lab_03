# 그림 요청 꾸러미 3 — '프롬프트 연습 과제' 예상 결과 (15장)

부마다 연습 과제 2개(모두 12개)의 **예상 결과 그림**입니다. 페이지의 과제 프롬프트와 이 요청문의 프롬프트는 같습니다(원본: `build/content_drill.py`).

## 요청 순서 (Genspark 대화 하나 = 파일 하나)
| 순서 | 파일 | 장수 | 첨부 |
|---|---|---|---|
| 1 | prompts/D01_part1.md | 3 | refs/moa_anime_base.png, refs/moa_sheet.png |
| 2 | prompts/D02_part2.md | 3 | refs/doctor_sheet.png |
| 3 | prompts/D03_part3_4.md | 4 | refs/sia_anime_base.png, refs/sia_sheet.png, refs/doctor_sheet.png, refs/haru_anime_base.png, refs/haru_sheet.png |
| 4 | prompts/D04_part5.md | 3 | refs/moa_anime_base.png, refs/moa_sheet.png, refs/sia_anime_base.png |
| 5 | prompts/D05_part6.md | 2 | f3_chin(사이트 assets/img/f3_chin.webp), refs/doctor_sheet.png, refs/moa_anime_base.png, refs/moa_sheet.png |

## 주의
- 두 장이 짝인 과제(d2·d4·d10)는 **같은 대화에서 차례로** 만듭니다. 둘째 그림은 적힌 것만 바뀌어야 합니다.
- d10_sia_smile은 그림 생성이 아니라 **부분 수정(영역 칠하기)** 기능으로 만듭니다. 칠하는 곳: 눈썹 위~입 아래, 두 눈 바깥까지(머리카락·목 제외).
- d11은 사이트의 실패 그림 `assets/img/f3_chin.webp`를 첨부해 고칩니다(꾸러미 안 `refs/f3_chin.webp`에 함께 넣음).
- d4_doctor_longmid는 연습용으로 일부러 만드는 실패 그림입니다. 도구가 고쳐 그리면 두 번까지만 다시 시도하고 그대로 주셔도 됩니다.
- 저장 이름은 `checklist.csv`의 `file` 열 그대로(png·jpg).
