# -*- coding: utf-8 -*-
"""Genspark 그림 요청 꾸러미(docs/image_requests) 생성. python3 build/make_requests.py
페이지의 '프롬프트로 직접 만들어 보기' A 프롬프트도 여기서 가져간다(이 파일이 원본)."""
import os, csv
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, "docs", "image_requests")
PIX = "Art style (required, always): 16-bit RPG style pixel art with clearly visible square pixels, limited palette, bold dark outline, 2–3 tone shading, small highlights; no smooth gradients, no painterly, vector, watercolor or 3D look.\nMatch the characters' proportions and colors of the attached reference images exactly, drawn in this same pixel-art style.\nBright daytime laboratory mood, soft natural sunlight through large windows, clean white walls, light lavender, mint and pink accents."
ANI = "Art style: high-quality anime illustration, clean confident lineart, two-tone cel shading, natural adult proportions.\nMatch the attached reference images exactly (face, hair, colors, accessories). All characters are adults in their twenties (the Professor is an adult man in his thirties); modest outfits exactly as described."
END = "No text, no letters, no numbers, no logos, no watermark, no revealing clothing, not childlike, no school uniform, not resembling any famous anime character."
ENDC = "No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands."
SAFE = "Composition: every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); bottom-left corner plain and bright."
CH = {
 "haru": "Haru (adult lab assistant, long straight pink hair with navy streaks and a thick navy streak down the center of the bangs, two round hair buns on top, small ahoge, big blue eyes)",
 "sia": "Sia (adult maid intern, long straight jet-black hair, no headdress, gray eyes, small silver earrings)",
 "moa": "Moa (adult maid intern, long ash-beige wavy hair, white frilled maid headband with a white ribbon over her LEFT ear, amber eyes)",
 "doctor": "the Professor (adult male scientist in his thirties, dark charcoal spiky hair with a white streak at the front, very thick black eyebrows, teal rectangular glasses)",
 "fly": "the Fruit Fly researcher (tiny cartoon fruit fly, large red compound eyes, retro dark blue helmet with a yellow-white stripe, colorful dangling cables, tiny white lab coat, translucent wings)",
 "bot": "AbaBot (boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes, short antenna topped with a red-brown abacus bead, gray segmented arms, small tank treads)",
 "judges": "three small cute dark navy silhouette judges with white dot eyes (one with a pink side-ponytail bow, one with a beret and teal round glasses, one with a cat-ear hood and yellow pompoms) holding blank score paddles",
}
OUT = {"haru": "lavender hoodie with white drawstrings over a white t-shirt, open white knee-length lab coat",
       "sia": "charcoal-black long-sleeved maid dress, large gray bow at the collar, long white frilled apron",
       "moa": "camel knit cardigan over a white blouse, red and navy plaid bow tie, white frilled apron",
       "doctor": "white lab coat over a black vest, white shirt and black tie"}
def who(k, outfit=None): return CH[k] + ", wearing " + (outfit or OUT[k])
def cover(file, page, part, alt, scene, chars, meta, mood):
    p = f"Website top cover illustration, wide 16:9.\n{PIX}\nScene: {scene}\nCharacters:\n  " + ";\n  ".join(chars) + f".\nVisual metaphor: {meta}\n{SAFE}\nMood: {mood}\n{ENDC}"
    return (file, page, part, alt, p, "pixel")
def body(file, page, part, alt, ratio, scene, extra=""):
    p = ("Illustration, " + ("vertical 2:3." if ratio == "2:3" else "wide 16:9.") + f"\n{ANI}\n{scene}\n" + (extra + "\n" if extra else "") + "Plain off-white studio background.\n" + END)
    return (file, page, part, alt, p, "anime")
C1 = [
 cover("cover_index", "index.html", "목차", "낮의 연구실 거울 벽 앞에서 하루·시아·모아·박사가 나란히 서고, 초파리와 주판봇이 이젤 앞에서 얼굴을 그리며, 평가단이 뒤에 앉은 장면",
   "a bright laboratory studio with a long wall mirror, two easels with canvases seen from the back, a small table with a ruler, a compass and tracing paper.",
   [who("haru") + ", in the center smiling at the mirror", who("sia") + ", standing in side view facing left", who("moa") + ", holding a round transparent sheet in front of her face", who("doctor") + ", at the back center with a clipboard",
    CH["fly"] + ", on the left facing right at the left easel", CH["bot"] + ", on the right facing left at the right easel", CH["judges"] + " sitting at a small table in the back right"],
   "a simple circle with a cross line drawn on the transparent sheet, lined up with Moa's face.", "cheerful, curious, the moment before a portrait session."),
 cover("cover_01", "01_front_female.html", "1부 정면 얼굴", "모아가 원과 십자선이 그려진 투명판을 얼굴 앞에 들고, 초파리가 가로선 세 줄을 긋는 장면",
   "a mirror corner in the lab studio with a tall standing mirror.",
   [who("moa") + ", in the center facing the viewer, holding a round transparent sheet with a circle and a cross line in front of her face", CH["fly"] + ", on the left facing right, drawing three horizontal lines on a small board with a teal marker", CH["bot"] + ", on the right facing left, drawing one huge eye on its canvas", who("doctor") + ", at the back nodding"],
   "a circle, a cross and three level lines.", "calm, focused."),
 cover("cover_02", "02_front_male.html", "2부 정면 남성 얼굴", "박사가 큰 장기말 모양 나무 블록을 들고 칠판 앞에 서고, 초파리가 원 아래에 오각형을 붙여 그리는 장면",
   "a classroom-like corner of the lab with a large white chalkboard.",
   [who("doctor") + ", in the center facing the viewer, holding a large wooden pentagon block shaped like a shogi piece (blank, no characters on it)", CH["fly"] + ", on the left facing right, drawing a circle with a pentagon attached below it on the board", CH["bot"] + ", on the right facing left, holding a small round mirror", who("haru") + ", at the back right taking notes"],
   "a circle with an upside-down pentagon below it.", "bright, a little playful."),
 cover("cover_03", "03_profile.html", "3부 옆얼굴", "창가에서 시아와 박사가 옆으로 서고, 초파리가 줄자로 이마에서 뒤통수까지 재는 장면",
   "a sunny window side of the lab, sheer curtains, a measuring tape.",
   [who("sia") + ", standing in side view facing left", who("doctor") + ", standing behind her also in side view facing left", CH["fly"] + ", hovering between them holding a long yellow measuring tape from forehead to the back of Sia's head", CH["bot"] + ", on the right facing left, looking puzzled"],
   "two side profiles in a row with the ears clearly behind the middle of the head.", "calm, airy."),
]
C2 = [
 cover("cover_04", "04_variation.html", "4부 변형과 점검", "연구실 안경점 놀이 — 하루가 큰 안경테를 대 보고, 박사가 어깨를 살짝 기울인 채 서 있는 장면",
   "a small eyewear corner set up in the lab: a stand of empty eyeglass frames, a round table mirror.",
   [who("haru") + ", in the center trying on large rectangular under-rim glasses, eyes half-closed with a confident smile", who("doctor") + ", on the right standing with shoulders slightly tilted, holding another frame", CH["fly"] + ", on the left facing right, holding a round magnifier", CH["bot"] + ", at the back wearing tiny glasses on its screen"],
   "one face, small changes: glasses, eyelids, a tilted shoulder.", "fun, light."),
 cover("cover_05", "05_ai_face.html", "5부 AI로 얼굴 고정하기", "연구실 조종 책상의 큰 모니터에 같은 얼굴이 정면·비스듬히·옆 세 장으로 떠 있고, 하루·시아·모아가 바라보는 장면",
   "the lab control desk with a big monitor showing three simple faces of the same person (front, three-quarter, side) aligned on one horizontal line, and a second monitor showing a face with a rectangle highlighted over the eyes and mouth.",
   [who("haru") + ", in the center pointing at the monitor", who("sia") + ", on the left", who("moa") + ", on the right", CH["bot"] + ", typing at the desk", CH["fly"] + ", hovering near the monitor", who("doctor") + ", at the back"],
   "the same face in three angles on one level line.", "focused, hopeful."),
 cover("cover_06", "06_failure_lab.html", "6부 실패 사례 실험실", "검수 책상 위에 어색한 얼굴 그림이 쌓이고, 초파리가 돋보기로 살피며 주판봇이 머리를 긁는 장면",
   "an inspection desk covered with sheets of simple portrait sketches, some with red circles (no readable text), a desk lamp.",
   [CH["fly"] + ", on the left facing right, holding a big magnifying glass over a sketch", CH["bot"] + ", on the right facing left, scratching its head with one arm", CH["judges"] + " at the back holding blank score paddles", who("haru") + ", sorting the sketches into piles"],
   "a pile of near-miss portraits being sorted from big shapes to small parts.", "playful, investigative."),
 cover("cover_07", "practice/index.html", "7부 실전 연습장", "연구실 조종 책상에 네 개의 작업대(비율 작업대·남녀 바꾸기판·문장 공방·진단 데스크)가 놓이고 모두가 둘러선 장면",
   "the lab control room with four small workstations in a row, each with a simple face diagram on its screen (no text).",
   [who("haru") + ", in the center at a workstation", who("doctor") + ", on the right with folded arms", CH["fly"] + ", on the left facing right", CH["bot"] + ", next to the fly, raising one arm in excitement", who("sia") + " and " + who("moa") + ", at the back"],
   "four stations, one face.", "energetic, final-stage feeling."),
]
C3 = [
 body("p1_moa_front_base", "01_front_female.html", "1부 1단계", "모아의 정면 얼굴 애니풍 그림 — 머리카락까지 그린 완성 얼굴과, 같은 얼굴의 밑그림(원과 십자선, 가로 기준선이 연하게 보이는 상태)을 나란히 놓은 그림", "16:9",
   "Two panels side by side of the same adult woman's face, front view, chest up: LEFT a clean construction sketch — a light circle with a vertical center line and a horizontal line through the upper eyelids at exactly half the head height, a faint line where the nose bottom sits one quarter above the chin, the face outline carved from the circle, no hair; RIGHT the finished portrait of " + who("moa") + " with the eyes, nose and mouth at exactly the same heights.",
   "Eyes spaced slightly more than one eye width apart. Construction lines are thin and pale gray. Light from the upper left."),
 body("p1_moa_cheek_compare", "01_front_female.html", "1부 2단계", "같은 20대 모아의 정면 얼굴 두 장 — 왼쪽은 볼이 입 높이 근처에서 불룩한 둥근 윤곽, 오른쪽은 볼이 그보다 위에서 불룩한 갸름한 윤곽", "16:9",
   "Two front-view portraits of the same adult woman in her late twenties, " + who("moa") + ", side by side, same expression and lighting: LEFT soft rounded face outline with the cheeks fullest at mouth level; RIGHT slim oval face outline with the cheeks fullest above mouth level. Both clearly adults.",
   "Only the face outline differs; hair, eyes, nose and mouth are identical. Light from the upper left."),
 body("p2_doctor_front_base", "02_front_male.html", "2부 1단계", "박사의 정면 얼굴 애니풍 그림 — 각진 턱과 청록 사각 안경을 쓴 완성 얼굴과, 같은 얼굴의 밑그림(원 아래 오각형이 연하게 보이는 상태)을 나란히 놓은 그림", "16:9",
   "Two panels side by side of the same adult man's face, front view, chest up: LEFT a clean construction sketch — a light circle with an upside-down pentagon attached slightly below its center forming a long face and a defined jaw with a square chin tip, faint horizontal lines for hairline, eyebrows and nose bottom at equal spacing; RIGHT the finished portrait of " + who("doctor") + ".",
   "Narrow almond eyes, eyes spaced one eye width apart, mouth one third of the way from nose to chin. Adult male proportions, not chibi. Light from the upper left."),
 body("p2_doctor_bust", "02_front_male.html", "2부 4단계", "박사의 정면 가슴 위 그림 — 흰 셔츠·검은 조끼·넥타이 차림, 목은 눈동자 사이만큼 굵고 어깨는 머리의 두 배 남짓인 성인 남성 체형", "16:9",
   "Front view, chest-up portrait of " + who("doctor", "white shirt, black vest and black tie, no lab coat") + ", standing straight, shoulders slightly tilted. Neck as wide as the distance between the pupils, shoulders about twice the head width, collarbones lightly indicated at the open collar.",
   "Adult male proportions, not chibi, modest. Light from the upper left."),
]
C4 = [
 body("p3_sia_doctor_profile", "03_profile.html", "3부 1·2단계", "왼쪽을 바라보는 시아(검은 긴 머리, 장식 없음)와 박사(청록 사각 안경)의 옆얼굴을 나란히 놓은 애니풍 그림 — 시아는 코끝이 작고 뾰족, 박사는 콧날이 곧고 턱이 단단한 성인 남성", "16:9",
   "Two side-profile portraits facing LEFT, chest up, side by side: LEFT " + who("sia") + " — small slightly upturned nose tip, simplified lips, soft chin, ear placed a little behind the middle of the head, neck tilted forward about five degrees with smooth curves; RIGHT " + who("doctor") + " — straight nose bridge going down diagonally from the eye, visible lip relief, defined jaw corner below the ear, ear placed well behind the middle of the head.",
   "Both eyes seen from the side as narrow tilted triangles. Adult proportions. Light from the upper left."),
 body("p4_haru_lids_glasses", "04_variation.html", "4부 1·2단계", "하루의 정면 얼굴 세 장 — 기본 얼굴, 위 눈꺼풀만 반쯤 내린 얼굴, 아래 테만 있는 안경을 쓴 얼굴. 세 장 모두 눈 크기와 자리는 같음", "16:9",
   "Three front-view chest-up portraits of the same adult woman " + who("haru") + " in a row: 1) neutral face; 2) only the upper eyelids lowered to half (a cool half-lidded look), eye size and position unchanged; 3) wearing large under-rim glasses (no top frame) whose lower frame stays below the eyes.",
   "Everything except the eyelids and glasses is identical across the three. Light from the upper left."),
 body("p5_sia_turnaround", "05_ai_face.html", "5부 2단계", "시아의 얼굴 세 장(정면·비스듬히·옆)을 한 줄로 나란히 놓은 애니풍 설정화 — 세 얼굴의 위 눈꺼풀이 같은 높이", "16:9",
   "Character turnaround sheet of " + who("sia") + ", head and shoulders: front view, three-quarter view, side profile facing left, in one row, same size. The upper eyelids of all three faces sit on the same horizontal level (a faint gray guide line across the sheet is allowed), as well as the nose bottoms and chins.",
   "Same person in all three, adult. Light from the upper left."),
 body("p5_moa_styles", "05_ai_face.html", "5부 4단계", "모아의 정면 얼굴 세 장 — 애니풍, 반실사, 실사풍(모아를 코스프레한 가상의 성인 모델). 세 얼굴 모두 흰 프릴 머리띠와 왼쪽 귀 위 흰 리본, 위 눈꺼풀 높이가 같음", "16:9",
   "Three front-view chest-up portraits of " + who("moa") + " in a row, rendered in three styles: 1) anime (large eyes about as tall as wide, nose as a small highlight, simplified lips); 2) semi-realistic 2.5D painting (eyes about 1:1.5, nose with a bridge line and soft shadow); 3) photorealistic studio photo of a fictional adult model in her late twenties cosplaying Moa (natural eyes, real nose and lips). The upper eyelids, nose bottoms and mouths are at the same heights in all three; the white frilled headband and the ribbon over her LEFT ear are kept.",
   "The photo panel must not resemble any real celebrity. Light from the upper left."),
]
FAILNOTE = "This is an intentional FAILURE example for a teaching page: draw the mistake described below clearly and convincingly, while everything else stays correct."
def fail(file, alt, scene, mistake):
    p = f"Illustration, vertical 2:3.\n{ANI}\n{FAILNOTE}\n{scene}\nIntentional mistake: {mistake}\nPlain off-white studio background.\n{END}"
    return (file, "06_failure_lab.html", "6부 실패", alt, p, "anime")
C5 = [
 fail("f1_eyes", "하루의 정면 얼굴인데 두 눈 사이가 눈 하나보다 좁아 가운데로 몰려 보이는 그림", "Front-view chest-up portrait of " + who("haru") + ".", "the two eyes are placed far too close together — the gap between them is clearly narrower than one eye width — so she looks cross-eyed."),
 fail("f2_long", "모아의 정면 얼굴인데 눈~코 사이가 길고 이마가 좁아 얼굴이 늘어져 보이는 그림", "Front-view chest-up portrait of " + who("moa") + ".", "the eyes are placed too high (well above half the head height) and the nose bottom is low, so the forehead is narrow and the midface between the eyes and the nose is stretched long."),
 fail("f3_chin", "박사의 정면 얼굴인데 장기말을 길게 그려 턱이 뾰족하고 얼굴이 지나치게 긴 그림", "Front-view chest-up portrait of " + who("doctor") + ".", "the lower face is stretched far too long and the chin comes to a sharp narrow point, so the face looks unbalanced and overly long."),
 fail("f4_back", "시아의 옆얼굴인데 뒤통수가 머리 크기 원 밖으로 크게 부풀어 머리가 둔해 보이는 그림", "Side-profile chest-up portrait facing left of " + who("sia") + ".", "the back of the head bulges far backward, much bigger than a natural skull, so the head looks heavy and bulky."),
]
C6 = [
 fail("f5_jaw", "박사의 옆얼굴인데 목이 가늘고 정면을 보는 각도라 턱이 앞으로 튀어나와 보이는 그림", "Side-profile chest-up portrait facing left of " + who("doctor") + ", with a thin stylized neck.", "the chin and lower jaw jut forward too much, so the jaw looks protruding."),
 fail("f6_neck", "시아의 옆모습인데 머리와 목이 직선으로 꺾여 붙고 목이 꼿꼿해 인형처럼 보이는 그림", "Side-profile chest-up portrait facing left of " + who("sia") + ".", "the neck is perfectly vertical and joins the head and the back with sharp straight corners instead of curves, like a doll's neck joint."),
 fail("f7_glasses", "하루가 안경을 썼는데 테 선이 눈동자 한가운데를 지나 눈이 가려진 그림", "Front-view chest-up portrait of " + who("haru") + ", wearing glasses.", "the glasses have small thin rims placed so that the frame line crosses right through the middle of both irises, hiding the eyes."),
 fail("f8_lips", "모아의 옆얼굴인데 입술 굴곡을 크게 넣어 입 주변이 앞으로 불룩해 보이는 그림", "Side-profile chest-up portrait facing left of " + who("moa") + ".", "the lips and the area around the mouth are drawn with strong realistic relief and pushed forward, so the mouth area bulges out of the simple anime profile."),
]
CONV = [("C01_covers_A", "표지 A (픽셀아트, 16:9)", "16:9", "refs 전부", C1), ("C02_covers_B", "표지 B (픽셀아트, 16:9)", "16:9", "refs 전부 + C01에서 받은 cover_index", C2),
        ("C03_part1_2", "1·2부 정면 얼굴", "16:9", "refs/moa_anime_base.png, refs/moa_sheet.png, refs/doctor_sheet.png", C3),
        ("C04_part3_5", "3·4·5부 옆얼굴·변형·AI", "16:9", "refs/sia_anime_base.png, refs/haru_anime_base.png, refs/moa_anime_base.png, refs/doctor_sheet.png", C4),
        ("C05_fail_A", "6부 실패 A", "2:3", "해당 캐릭터의 refs/*_anime_base.png 또는 *_sheet.png", C5), ("C06_fail_B", "6부 실패 B", "2:3", "해당 캐릭터의 refs/*_anime_base.png 또는 *_sheet.png", C6)]
HEAD_PIX = "웹페이지 맨 위에 거는 표지 그림을 한 장씩 차례로 만들어 줘.\n- 비율 16:9, 가로 1920px 이상\n- 그림체는 반드시 16비트 RPG풍 픽셀아트 (네모 픽셀이 보이게, 매끈한 일러스트·벡터·수채화·3D 금지)\n- 첨부한 참고 이미지의 캐릭터를 같은 외형으로 그릴 것\n- 그림 안에 글자·숫자·로고 금지\n- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게\n아래 영어 프롬프트를 하나씩 써 줘."
HEAD_ANI = "해설 페이지 본문에 넣을 그림을 한 장씩 차례로 만들어 줘.\n- 비율은 각 프롬프트 첫 줄을 따를 것(16:9는 가로 1920px 이상, 2:3은 세로 1536px 이상)\n- 첨부한 참고 이미지의 캐릭터 외형(얼굴·머리·색·장식)을 똑같이 지킬 것\n- 등장인물은 모두 20대 성인(박사는 30대 성인 남성). 노출·과장된 체형·교복 느낌·어려 보이는 얼굴 금지\n- 그림 안에 글자·숫자·로고 금지, 유명 애니 캐릭터와 닮으면 다시 만들 것\n아래 영어 프롬프트를 하나씩 써 줘."
PROMPTS = {it[0]: it for _c in CONV for it in _c[4]}
CONV_OF = {it[0]: _c[0] for _c in CONV for it in _c[4]}
ATTACH_OF = {_c[0]: _c[3] for _c in CONV}

README = """# 그림 요청 꾸러미 — 구조 먼저 그리기 연구실 03 · 얼굴 편

저장소: `adminmrobo/drawing_lab_03` (페이지는 완성 — 그림 자리는 '그림 준비 중'으로 비어 있음)
만드는 도구: Genspark 이미지 · 받은 그림은 zip으로 돌려주시면 됩니다(대화 단위로 나눠 여러 번 주셔도 됩니다).

## 1. 그림 규칙
| 항목 | 규칙 |
|---|---|
| 그림체 | **표지 8장은 16비트 픽셀아트**. **본문 그림은 애니풍(5부 화풍 비교만 반실사·실사풍 포함)** |
| 배경 | 흰색·밝은 낮 분위기 |
| 캐릭터 고정값 | 하루: 정수리 번 2개 + 앞머리 가운데 남색 줄 / 시아: 흑발·머리 장식 없음 / 모아: 흰 프릴 머리띠 + **왼쪽** 귀 위 흰 리본 / 박사: 흰 줄 있는 짙은 머리, 굵은 눈썹, 청록 사각 안경 |
| 나이·노출 | 모두 20대 성인(박사는 30대 성인 남성, 꼬마 체형 아님). **어려 보이는 얼굴·교복 느낌·노출 금지** |
| 글자 | 그림 안에 글자·숫자·로고 금지(연한 회색 기준선은 허용) |
| 실사풍 | 캐릭터를 코스프레한 **가상의 성인 모델**. 실존 인물과 닮으면 다시 생성 |

## 2. 요청 순서 (Genspark 대화 하나 = 파일 하나)
| 순서 | 파일 | 그림 수 | 비율 | 첨부 |
|---|---|---|---|---|
| 1 | `prompts/C01_covers_A.md` | 4 | 16:9 픽셀 | refs 전부 |
| 2 | `prompts/C02_covers_B.md` | 4 | 16:9 픽셀 | refs 전부 + C01의 cover_index |
| 3 | `prompts/C03_part1_2.md` | 4 | 16:9 | moa_anime_base, moa_sheet, doctor_sheet |
| 4 | `prompts/C04_part3_5.md` | 4 | 16:9 | sia·haru·moa anime_base, doctor_sheet |
| 5 | `prompts/C05_fail_A.md` | 4 | 2:3 | 해당 캐릭터 기준 그림 |
| 6 | `prompts/C06_fail_B.md` | 4 | 2:3 | 해당 캐릭터 기준 그림 |

## 3. 저장 이름
`checklist.csv`의 `file` 열 이름 그대로(png·jpg). 받으면 WebP로 바꿔 `assets/img/`에 넣습니다(표지 1600×900, 가로 1200×675, 세로 600×900).

## 4. 실패 그림 주의
도구가 실수를 자동으로 고쳐 그리면 두 번까지만 다시 시도해 주세요. 그래도 안 되면 그대로 주셔도 됩니다(페이지에서 '결과는 매번 다르다'는 사례로 설명합니다).
"""

if __name__ == "__main__":
    os.makedirs(os.path.join(D, "prompts"), exist_ok=True)
    rows = []; n = 0
    for cid, title, ratio, att, items in CONV:
        pix = items[0][5] == "pixel"
        md = f"# {cid[:3]} · {title} — " + ", ".join(i[0] for i in items) + f"\n\n**첨부:** {att}\n\n**Genspark에 먼저 붙여 넣기 ↓**\n```\n{HEAD_PIX if pix else HEAD_ANI}\n```\n"
        for k, (file, page, part, alt, prompt, style) in enumerate(items):
            n += 1; rows.append([n, cid[:3], file, page, part, "16:9" if "16:9" in prompt.split("\n")[0] else "2:3", style, ""])
            md += f"\n---\n## {k+1}) {file} — {part}\nalt: {alt}\n```\n{prompt}\n```\n"
        open(os.path.join(D, "prompts", cid + ".md"), "w").write(md)
    with open(os.path.join(D, "checklist.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["order", "conversation", "file", "page", "part", "ratio", "style", "status"]); w.writerows(rows)
    open(os.path.join(D, "README.md"), "w").write(README)
    print("prompts", len(CONV), "images", n)
