# 구조 먼저 그리기 연구실 03 · 얼굴 편 — 같은 기준선, 다른 얼굴

원 하나와 가로선 몇 줄로 정면 얼굴을 세우고, 남성과 여성의 윤곽·눈·부위 높이·귀·목이 어떻게 다른지 실험으로 익힌 뒤, 그 기준선을 AI 얼굴 문장과 가림 영역으로 옮겨 봅니다. 얼굴 그림 실패 8종 진단과 실전 연습장까지.

- 사이트: https://adminmrobo.github.io/drawing_lab_03/
- 글 · 안상선 ((주)M-Robo 대표) · [저자 소개](https://adminmrobo.github.io/who_am_i/who_am_i.html)

## 구성
| 부 | 페이지 | 내용 |
|---|---|---|
| 목차 | `index.html` | 세 줄 요약, 편 목록, 전체 흐름, 한눈에 보는 기준값, 등장인물, 원리와 출처 |
| 1부 | `01_front_female.html` | 정면 얼굴 — 기준선, 원 깎기, 눈 상자, 부위 다듬기 (모델 모아) |
| 2부 | `02_front_male.html` | 정면 남성 얼굴 — 원 + 장기말, 세 간격, 남녀 위치, 목과 어깨 (모델 박사) |
| 3부 | `03_profile.html` | 옆얼굴 — 기본 도형, 귀 위치, 코~턱 굴곡, 목 기울기 (시아·박사) |
| 4부 | `04_variation.html` | 변형과 점검 — 눈꺼풀, 안경, 정면 자세, 옆얼굴 점검 (하루·박사) |
| 5부 | `05_ai_face.html` | AI로 얼굴 고정하기 — 얼굴 문장, 각도별 기준선, 가림 영역, 화풍 |
| 6부 | `06_failure_lab.html` | 실패 사례 실험실 — 진단 순서, 실패 8종, 나이 쏠림 막기 |
| 7부 | `practice/index.html` | 실전 연습장 — 비율 작업대, 남녀 바꾸기판, 얼굴 문장 공방, 진단 데스크 |

## 원리와 출처
그리기 원리는 YANAMi 『男女の顔の描き分け 角度別・年齢別・表情別のキャラデッサン』(ホビージャパン, 2018) 1장을 참고해 정리했습니다. 책의 그림·문장·도식·구성 순서는 옮기지 않았고, 연구실 캐릭터와 직접 움직이는 실험으로 새로 구성했습니다. 책의 어린 인물 예시는 모두 성인 캐릭터로 바꿨습니다. 그 밖의 출처(Loomis 1956, Farkas 외 1985, RePaint 2022, 잠재 확산 모델 2022)는 각 페이지 바닥글에 있습니다. 비율 숫자는 모두 설명용 예시값입니다.

## 빌드와 점검
```
python3 build/build.py && python3 build/check_numbers.py && python3 build/make_og.py
python3 -m http.server 8765 &   # 아래 두 점검용
python3 build/check_pages.py && python3 build/check_missions.py
```
작성 방침: `docs/WRITING_POLICY.md` · 그림 36장(`assets/img/`, Genspark): 요청문 `docs/image_requests/`(본문·표지 24장), `docs/image_requests_make/`(비교 12장), 실제 그림 설명 `build/img_notes.py` · 페르소나 검사: `docs/persona_review.md`

캐릭터 이름·설정·그림은 저작권자 안상선의 허락 없이 사용할 수 없습니다. 캐릭터 그림: [fruitfly-lab-expressions](https://github.com/adminmrobo/fruitfly-lab-expressions).
