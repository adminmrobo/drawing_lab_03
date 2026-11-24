# -*- coding: utf-8 -*-
"""부마다 '프롬프트 연습 과제' 2개씩(모두 12개). 과제의 프롬프트는 예상 결과 그림을 실제로 만드는 프롬프트와 같다(이 파일이 원본).
python3 build/content_drill.py → docs/image_requests_drill/ 요청 꾸러미 생성."""
import os, sys, csv
sys.path.insert(0, os.path.dirname(__file__))
from make_requests import who, ANI, END, CH

def P(ratio, scene, extra=""):
    return ("Illustration, " + ("vertical 2:3." if ratio == "2:3" else "wide 16:9.") + f"\n{ANI}\n{scene}\n" + (extra + "\n" if extra else "") + "Plain off-white studio background.\n" + END)

# 과제 하나: id, title, goal, why, attach, steps, prompts[(라벨, 프롬프트, 결과 그림 key, 결과 그림 설명, 비율)], check[(문장, 링크)], expect, trouble[(문제, 대처)], more
DRILL = {
1: [
 dict(id="d1", title="기준선 세 줄을 문장으로 넣기", goal="1부의 높이 기준(위 눈꺼풀 1/2, 코 밑 1/4, 머리선 1/6)을 문장으로 적어 모아의 정면 얼굴을 만들고, 받은 그림 위에 직접 선을 그어 검사합니다.",
      why="AI는 '예쁜 얼굴'이라는 말로는 기준선을 지키지 않습니다. 기준선을 숫자 대신 '머리 높이의 한가운데' 같은 말로 적으면 그림마다 얼굴이 덜 흔들립니다.",
      attach="refs/moa_anime_base.png, refs/moa_sheet.png",
      steps=["Genspark에서 새 대화를 열고 참고 그림 두 장을 첨부합니다.", "아래 프롬프트를 그대로 붙여 넣어 그림 한 장을 만듭니다.",
             "받은 그림을 그림판·사진 편집 앱에서 열고, 머리 꼭대기와 턱 끝에 가로선을 긋습니다(머리카락은 빼고 이마 위 머리선 근처를 꼭대기로 봅니다).",
             "두 선 사이를 반으로 나눈 곳에 선을 하나, 그 아래 절반을 다시 반으로 나눈 곳에 선을 하나 긋습니다.",
             "위 눈꺼풀이 첫 선(1/2)에, 코 밑이 둘째 선(턱에서 1/4)에 걸리는지 봅니다. 벗어났으면 '확인할 것'의 링크로 돌아가 원리를 다시 보고, 같은 대화에 고칠 곳 하나만 적어 다시 요청합니다."],
      prompts=[("넣을 프롬프트", P("16:9", "Front view, chest-up portrait of " + who("moa") + ", gentle closed-mouth smile, looking at the viewer.",
               "Facial proportions: upper eyelids exactly at half the head height (top of the skull to the chin), nose bottom one quarter of the head height above the chin, hairline one sixth below the top of the skull, mouth halfway between the nose bottom and the chin, eyes spaced slightly more than one eye width apart. Light from the upper left."),
               "d1_moa_guides", "예상 결과 — 기준선 문장으로 만든 모아의 정면 얼굴. 위 눈꺼풀이 머리 높이의 한가운데, 코 밑이 턱에서 1/4쯤에 있음", "16/9")],
      check=[("위 눈꺼풀이 1/2 선에 걸리나(±머리 높이의 2%)", "#s1"), ("눈 사이가 눈 하나보다 조금 넓나", "#s3"), ("입이 코 밑과 턱의 가운데쯤인가", "#s4")],
      expect="머리카락까지 그린 보통의 정면 얼굴이 나옵니다. 겉보기엔 평범하지만, 선을 그어 보면 눈꺼풀이 한가운데에, 코 밑이 턱에서 1/4쯤에 놓입니다. 문장 없이 만든 그림보다 이마가 넓어 보이는 것이 정상입니다.",
      trouble=[("눈이 위로 올라가 이마가 좁다", "같은 대화에 'Same image. Change only: move the eyes down so the upper eyelids sit exactly at half the head height.'"),
               ("앞머리가 눈썹을 덮어 선을 긋기 어렵다", "꼭대기는 머리카락 위가 아니라 두개골 꼭대기(앞머리 시작보다 조금 위)로 잡습니다."),
               ("얼굴이 매번 달라진다", "참고 그림 두 장을 꼭 첨부하고, 한 대화에서 한 번에 하나만 바꿉니다.")],
      more="같은 문장의 'moa'만 시아나 하루로 바꿔 세 사람의 정면 얼굴을 만들고, 세 그림의 기준선 높이를 비교해 보세요."),
 dict(id="d2", title="눈 간격만 바꿔 두 번 만들기", goal="눈 사이를 '눈 하나'로 둔 그림과 '눈 하나보다 조금 넓게' 둔 그림을 차례로 만들어, 1부 3단계의 몰린 눈 원리를 실제 그림으로 확인합니다.",
      why="한 그림 안에 두 얼굴을 넣어 비교하면 AI가 두 얼굴을 비슷하게 맞춰 버리는 일이 많았습니다(1부 직접 만들기의 실제 결과). 그래서 같은 대화에서 한 장씩, 한 곳만 바꿉니다.",
      attach="refs/moa_anime_base.png, refs/moa_sheet.png",
      steps=["새 대화를 열고 참고 그림을 첨부합니다.", "프롬프트 ①로 첫 그림을 만듭니다(눈 사이 = 눈 하나).", "같은 대화에 프롬프트 ②를 이어 붙여 둘째 그림을 만듭니다(눈 간격만 바뀜).",
             "두 그림을 나란히 놓고, 눈 사이에 눈 하나가 몇 개 들어가는지 재 봅니다.", "둘째 그림이 첫 그림과 거의 같으면 새 대화에서 ②의 내용(눈 간격 문장)을 넣어 처음부터 다시 만듭니다."],
      prompts=[("① 눈 사이 = 눈 하나", P("2:3", "Front view, chest-up portrait of " + who("moa") + ", neutral soft smile, looking at the viewer.", "Her two eyes are spaced exactly one eye width apart, like a realistic face. Light from the upper left."),
                "d2_moa_gap_one", "예상 결과 ① — 눈 사이가 눈 하나 너비인 모아. 애니풍 큰 눈이라 두 눈이 가운데로 조금 몰려 보임", "2/3"),
               ("② 같은 대화에 이어서", "Same image, keep the same framing. Change only: space the eyes slightly more than one eye width apart (about 1.1 eye widths). Still no text.",
                "d2_moa_gap_wide", "예상 결과 ② — 눈 사이만 조금 넓힌 모아. 몰린 느낌이 줄고 시선이 편안해 보임", "2/3")],
      check=[("①에서 눈이 가운데로 몰려 보이나", "#s3"), ("②에서 눈 사이가 눈 1개보다 조금 넓어졌나", "#s3"), ("눈 말고 다른 곳(머리·옷·표정)은 그대로인가", None)],
      expect="①은 눈과 눈 사이가 좁아 조금 사시처럼 보이고, ②는 같은 얼굴인데 시선이 편안해 보입니다. 차이는 눈 반 개만큼이라 작지만, 두 장을 나란히 두면 분명합니다.",
      trouble=[("②가 ①과 똑같다", "새 대화에서 ①의 프롬프트 끝 문장을 'eyes spaced slightly more than one eye width apart'로 바꿔 처음부터 만듭니다."),
               ("눈 크기까지 바뀐다", "②에 'keep the eye size and shape'를 덧붙입니다."),
               ("눈동자가 코 쪽으로 쏠린다", "간격 문제가 아니라 시선 문제입니다. 'looking straight at the viewer, irises centered'를 덧붙입니다.")],
      more="1부 3단계 실험에서 눈 사이 막대를 100과 110에 놓고, 받은 두 그림과 비교해 보세요."),
],
2: [
 dict(id="d1", title="남성 신호 네 가지를 조립하기", goal="윤곽(각진 턱)·눈(1:2 가는 눈)·부위 위치(입은 코 쪽 1/3)·목과 어깨(머리 너비의 2배) 네 신호를 한 문장씩 넣어 박사의 정면 얼굴을 만듭니다.",
      why="남성 얼굴은 눈만 바꿔서는 나오지 않습니다(2부 3단계). 신호를 하나씩 문장으로 적으면, 어떤 신호가 빠졌을 때 무엇이 어색해지는지 찾기 쉽습니다.",
      attach="refs/doctor_sheet.png",
      steps=["새 대화를 열고 박사 설정 시트를 첨부합니다.", "프롬프트를 붙여 넣어 만듭니다. 네 신호가 각각 한 문장씩 들어 있습니다.",
             "받은 그림에서 네 신호를 하나씩 확인합니다(확인할 것).", "빠진 신호가 있으면 그 신호의 문장만 'Same image. Change only:' 뒤에 붙여 다시 요청합니다."],
      prompts=[("넣을 프롬프트", P("16:9", "Front view, chest-up portrait of " + who("doctor", "white shirt with rolled sleeves, black vest and black tie, no lab coat") + ", standing in front of a plain chalkboard-gray wall, calm confident smile.",
               "Signal 1 — face outline: long face with a defined angular jaw and a square chin tip.\nSignal 2 — eyes: narrow almond eyes about half as tall as they are wide, spaced one eye width apart.\nSignal 3 — features: nose bottom slightly above one quarter of the head height, mouth one third of the way from the nose to the chin, ears from the upper eyelid to the nose tip.\nSignal 4 — neck and shoulders: neck as wide as the distance between the pupils, shoulders about twice the head width. Light from the upper left."),
               "d3_doctor_signals", "예상 결과 — 네 신호를 넣은 박사의 정면 얼굴. 각진 턱, 가는 눈, 코 쪽으로 올라간 입, 넓은 어깨", "16/9")],
      check=[("턱 끝이 평평하게 잘린 각진 턱인가", "#s1"), ("눈이 가로로 긴 1:2 모양인가", "#s3"), ("어깨가 머리 너비의 두 배 남짓인가", "#s4")],
      expect="앞에서 본 박사가 셔츠·조끼 차림으로 서 있는 그림이 나옵니다. 턱이 각지고, 눈이 가늘고, 어깨가 넓어 한눈에 성인 남성으로 읽힙니다. 2부 본문 그림보다 어깨가 더 넓게 나오는 경우가 많습니다.",
      trouble=[("얼굴이 앳되다", "Signal 2의 눈이 커졌는지 봅니다. 'not large round eyes'를 덧붙이고, 'an adult man in his thirties'를 맨 앞에 넣습니다."),
               ("어깨가 잘려 안 보인다", "'chest-up, both shoulders fully visible'을 넣습니다."),
               ("안경이 바뀐다", "'keep the teal rectangular glasses exactly as in the reference'를 덧붙입니다.")],
      more="Signal 1 문장만 지우고 새 대화에서 다시 만들어, 턱 하나가 인상을 얼마나 바꾸는지 비교해 보세요."),
 dict(id="d2", title="세 간격을 재고, 긴 곳 하나만 고치기", goal="일부러 가운데(눈썹~코 밑)가 긴 박사 얼굴을 만들고, 세 간격을 재서 긴 곳을 찾은 뒤 한 문장으로 고칩니다.",
      why="그림이 어색할 때 '더 잘생기게'처럼 막연하게 고치면 다른 곳까지 바뀝니다. 재서 찾은 곳 하나만 고치는 연습입니다.",
      attach="refs/doctor_sheet.png",
      steps=["새 대화를 열고 박사 설정 시트를 첨부합니다.", "프롬프트 ①로 가운데가 긴 얼굴을 만듭니다(일부러 만든 연습용 실패).",
             "받은 그림에 머리선·눈썹·코 밑·턱 네 곳에 가로선을 긋고, 세 간격의 길이를 잽니다.", "가장 긴 간격(대개 눈썹~코 밑)을 확인하고, 프롬프트 ②를 같은 대화에 붙여 고칩니다.", "고친 그림에서 다시 재서 세 간격이 비슷해졌는지 확인합니다."],
      prompts=[("① 연습용 — 가운데가 긴 얼굴", P("2:3", "Front view, chest-up portrait of " + who("doctor") + ", neutral expression.", "Practice example: the midface is too long — a large distance between the eyebrows and the nose bottom, the nose long, the mouth and chin squeezed low. Everything else normal. Light from the upper left."),
                "d4_doctor_longmid", "예상 결과 ① — 눈썹~코 밑이 길어 얼굴이 늘어져 보이는 박사(연습용 실패)", "2/3"),
               ("② 같은 대화에 이어서", "Same image, keep the same framing. Change only: equal thirds — hairline to eyebrows, eyebrows to nose bottom, and nose bottom to chin are the same length; shorten the nose. Still no text.",
                "d4_doctor_thirds", "예상 결과 ② — 세 간격을 같게 고친 박사. 코가 짧아지고 얼굴이 짜여 보임", "2/3")],
      check=[("①에서 눈썹~코 밑이 가장 긴가", "#s2"), ("②에서 세 간격의 차이가 줄었나", "#s2"), ("눈·안경·머리는 그대로인가", None)],
      expect="①은 코가 길고 얼굴 가운데가 늘어져 멍해 보입니다. ②는 같은 박사인데 코가 짧아지고 입과 턱 사이에 여유가 생겨 단정해 보입니다.",
      trouble=[("①이 너무 멀쩡하게 나온다", "도구가 실수를 고쳐 그리는 경우입니다. 'exaggerate the long midface'를 덧붙이거나, 그대로 두고 ②만 비교해도 됩니다."),
               ("②에서 턱까지 짧아졌다", "'keep the jaw and chin shape'를 덧붙입니다."),
               ("길이를 재기 어렵다", "가로선 네 줄을 긋고, 종이를 대고 간격을 표시해 서로 겹쳐 보면 됩니다.")],
      more="2부 2단계 실험에서 눈썹·코 밑 막대로 ①과 비슷한 얼굴을 만든 뒤, 세 간격이 같아질 때까지 맞춰 보세요."),
],
3: [
 dict(id="d1", title="옆얼굴 — 방향과 귀 위치까지 적기", goal="시아의 옆얼굴을 왼쪽을 보는 방향으로, 귀는 머리 가운데보다 조금 뒤에, 눈은 기울어진 삼각김밥 모양으로 받습니다.",
      why="실제로 받은 그림 중에는 '왼쪽을 봄'을 적었는데도 오른쪽을 보는 옆얼굴이 있었습니다(5부 설정화). 방향과 귀 위치처럼 쉽게 무시되는 조건은 문장을 따로 세워 분명히 적습니다.",
      attach="refs/sia_anime_base.png, refs/sia_sheet.png",
      steps=["새 대화를 열고 참고 그림을 첨부합니다.", "프롬프트를 붙여 넣어 만듭니다.", "그림이 오른쪽을 보면, 같은 대화에 'Same image, mirrored: she faces LEFT.'를 붙이거나 그림을 좌우 반전합니다(반전해도 원리 확인에는 문제없습니다).",
             "이마 끝과 뒤통수 끝에 세로선을 긋고, 그 가운데보다 귀가 뒤에 있는지 봅니다."],
      prompts=[("넣을 프롬프트", P("2:3", "Strict side profile, the face pointing to the LEFT edge of the image, chest-up portrait of " + who("sia") + ".",
               "Profile rules: the ear placed a little behind the middle of the head (about 55% of the way from the forehead to the back of the head); the eye seen from the side as a narrow tilted triangle; small slightly upturned nose tip; simplified lips; soft chin; neck tilted forward about five degrees, joined to the head and back with smooth curves. Light from the upper left."),
               "d5_sia_profile_left", "예상 결과 — 왼쪽을 보는 시아의 옆얼굴. 귀가 머리 가운데보다 조금 뒤에 있고, 코끝이 작고 입술 굴곡이 적음", "2/3")],
      check=[("얼굴이 왼쪽을 보나", None), ("귀가 이마~뒤통수의 가운데보다 뒤인가", "#s2"), ("입 주변이 앞으로 불룩하지 않나", "#s3")],
      expect="왼쪽을 보는 시아의 옆모습이 나옵니다. 귀는 머리 한가운데보다 조금 뒤, 귀 아래로 긴 검은 머리가 흘러내립니다. 코끝은 작고 입술 굴곡은 거의 없습니다.",
      trouble=[("오른쪽을 본다", "가장 흔한 문제입니다. 좌우 반전으로 해결하거나 'mirrored, facing left'를 붙입니다."),
               ("비스듬한 얼굴(3/4)로 나온다", "'strict side profile, only one eye visible'을 덧붙입니다."),
               ("귀가 머리카락에 가려 안 보인다", "'ear visible, hair tucked behind the ear'를 덧붙입니다.")],
      more="같은 문장에서 sia를 doctor로 바꾸고 귀 위치를 'well behind the middle (about 66%)'로 바꿔, 남녀 귀 위치를 비교해 보세요."),
 dict(id="d2", title="목 — 5° 숙인 옆모습", goal="박사의 옆모습에서 목을 앞으로 약 5° 기울이고, 머리와 목·목과 등을 곡선으로 잇게 합니다. 목 너비는 머리 너비의 절반입니다.",
      why="실제로 받은 그림에서는 '목을 곧게, 직선으로'라는 비교 요청이 거의 반영되지 않았습니다(3부 직접 만들기 2). 반대로 자연스러운 목을 받는 문장을 연습하면 인형 같은 목을 피하는 법이 몸에 익습니다.",
      attach="refs/doctor_sheet.png",
      steps=["새 대화를 열고 박사 설정 시트를 첨부합니다.", "프롬프트를 붙여 넣어 만듭니다.", "머리 가운데에서 아래로 연필을 대 보고, 목이 똑바로 서지 않고 조금 앞으로 기울었는지 봅니다.",
             "턱 아래~목, 뒤통수~등이 꺾이지 않고 곡선으로 이어졌는지 봅니다."],
      prompts=[("넣을 프롬프트", P("16:9", "Strict side profile facing LEFT, waist-up, " + who("doctor", "white shirt, black vest and black tie, no lab coat") + ", reading a thin book held at chest height, head slightly lowered.",
               "Neck rules: the neck grows from the center of the head, tilted forward about five degrees; neck width about half the head width; smooth curves from the jaw into the throat and from the back of the head into the back; the throat slightly fuller under the jaw; the ear well behind the middle of the head. Light from the upper left."),
               "d6_doctor_neck", "예상 결과 — 왼쪽을 보며 책을 읽는 박사의 옆모습. 목이 조금 앞으로 기울고 머리·목·등이 곡선으로 이어짐", "16/9")],
      check=[("목이 앞으로 조금 기울었나(똑바로 서지 않았나)", "#s4"), ("목 너비가 머리 너비의 절반쯤인가", "#s4"), ("턱 아래와 뒤통수 아래가 곡선으로 이어졌나", "#s4")],
      expect="책을 읽느라 고개를 살짝 숙인 박사의 옆모습이 나옵니다. 목은 굵고 조금 앞으로 기울었으며, 뒤통수에서 등까지 부드럽게 이어집니다.",
      trouble=[("정면이나 비스듬한 얼굴로 나온다", "'strict side profile, only one eye visible'을 덧붙입니다."),
               ("책이 얼굴을 가린다", "'the book held low, the face fully visible'을 덧붙입니다."),
               ("목이 너무 가늘다", "'thick adult male neck, about half the head width'로 고칩니다.")],
      more="3부 4단계 실험에서 기울기 5°·너비 50%·곡선으로 잇기를 맞춘 화면과 받은 그림을 나란히 놓아 보세요."),
],
4: [
 dict(id="d1", title="표정 시트 — 눈꺼풀과 눈썹만 바꾸기", goal="하루의 같은 얼굴 세 개(기본 / 눈꺼풀 반쯤 내림 / 눈꺼풀 내림 + 눈썹 올림)를 한 장의 표정 시트로 만듭니다.",
      why="실제로 받은 그림에서 '눈을 작게'라는 비교 요청은 거의 반영되지 않았습니다. 바꿀 곳을 '눈꺼풀'과 '눈썹'으로 좁혀 적으면, 눈 크기와 자리를 지킨 채 표정만 바뀝니다.",
      attach="refs/haru_anime_base.png, refs/haru_sheet.png",
      steps=["새 대화를 열고 참고 그림을 첨부합니다.", "프롬프트를 붙여 넣어 만듭니다.", "세 얼굴의 눈 위치·크기가 같은지 봅니다(투명 종이를 대거나 가로선을 긋습니다).",
             "가운데와 오른쪽 얼굴에서 바뀐 것이 눈꺼풀·눈썹뿐인지 확인합니다."],
      prompts=[("넣을 프롬프트", P("16:9", "Expression sheet: three front-view head-and-shoulders portraits of the same adult woman " + who("haru") + " in a row, identical size and position.",
               "1) neutral face; 2) only the upper eyelids lowered to half, eyebrows unchanged — a sleepy, bored look; 3) upper eyelids lowered to half AND eyebrows raised at the outer ends with a small confident smile — a bold, self-assured look. The eye size and the eye positions are identical in all three; only the eyelids, eyebrows and mouth change. Light from the upper left."),
               "d7_haru_sheet", "예상 결과 — 하루의 표정 세 개. 기본, 눈꺼풀을 내린 나른한 얼굴, 눈꺼풀을 내리고 눈썹을 올린 자신만만한 얼굴", "16/9")],
      check=[("세 얼굴의 눈 자리와 크기가 같은가", "#s1"), ("가운데 얼굴은 눈꺼풀만 내려왔나", "#s1"), ("오른쪽 얼굴은 눈썹이 올라갔나", "#s1")],
      expect="같은 하루가 세 번 나란히 그려진 표정 시트가 나옵니다. 가운데는 졸린 듯 시큰둥하고, 오른쪽은 같은 눈꺼풀인데 눈썹 덕분에 자신만만해 보입니다.",
      trouble=[("세 얼굴의 각도·크기가 다르다", "'identical size, position and head angle'을 덧붙입니다."),
               ("가운데 얼굴이 눈을 감아 버린다", "'eyes still open, irises half visible'을 덧붙입니다."),
               ("머리 번이 사라진다", "'two round hair buns on top, navy streak in the bangs'를 다시 적습니다.")],
      more="4부 1단계 실험의 눈꺼풀·눈썹 막대를 받은 그림의 세 얼굴에 맞춰 움직여 보세요."),
 dict(id="d2", title="언더림 안경을 정확히 받기", goal="'언더림(위 테가 없는 안경)'을 그림 도구가 알아듣는 말로 풀어 적어, 테가 눈을 가리지 않는 하루의 안경 얼굴을 받습니다.",
      why="실제로 'under-rim glasses'라고만 적었을 때는 위 테가 있는 둥근 안경이 나왔습니다(4부 직접 만들기, 6부 f7). 낱말 하나에 기대지 말고 모양을 문장으로 풀어 써야 합니다.",
      attach="refs/haru_anime_base.png, refs/haru_sheet.png",
      steps=["새 대화를 열고 참고 그림을 첨부합니다.", "프롬프트를 붙여 넣어 만듭니다.", "렌즈 위쪽에 테가 없는지, 아래 테가 눈동자 아래를 지나는지 봅니다.",
             "위 테가 생겼으면 같은 대화에 'Same image. Change only: remove the frame above the lenses.'를 붙입니다."],
      prompts=[("넣을 프롬프트", P("2:3", "Front view, chest-up portrait of " + who("haru") + ", smiling softly, wearing glasses.",
               "Glasses description (important): semi-rimless rectangular glasses; a thin dark-navy metal frame runs ONLY along the bottom edge of each lens; NO frame above the lenses; the lenses are wider and taller than her eyes; the bottom frame passes below the irises and never crosses the eyes; thin temples going back to the ears. Light from the upper left."),
               "d8_haru_underrim", "예상 결과 — 위 테 없이 아래 테만 있는 안경을 쓴 하루. 눈동자가 테에 가리지 않음", "2/3")],
      check=[("렌즈 위쪽에 테가 없나", "#s2"), ("아래 테가 눈동자 아래를 지나나", "#s2"), ("렌즈가 눈보다 크게 그려졌나", "#s2")],
      expect="아래 테만 있는 네모 안경을 쓴 하루가 나옵니다. 눈썹과 눈매가 그대로 보이고, 아래 테가 눈 밑을 가볍게 받쳐 지적인 인상이 됩니다.",
      trouble=[("여전히 위 테가 있다", "'NO frame above the lenses'를 문장 맨 앞으로 옮기고, 'half-rim glasses with the rim on the bottom'도 함께 적습니다."),
               ("안경이 얼굴보다 너무 크다", "'the lenses slightly wider than her eyes'로 줄입니다."),
               ("렌즈에 빛 반사가 많아 눈이 안 보인다", "'clear lenses with no glare'를 덧붙입니다.")],
      more="4부 2단계 실험에서 언더림을 켜고 림 높이를 바꿔, 아래 테가 눈동자를 지나지 않는 범위를 찾아보세요."),
],
5: [
 dict(id="d1", title="세 각도 설정화 — 방향과 기준선까지 지정", goal="모아의 정면·비스듬히·옆 얼굴을 한 장에 받되, 옆얼굴이 왼쪽을 보고 세 얼굴의 눈이 한 가로선 위에 오게 합니다.",
      why="5부 설정화의 실제 결과에서 눈 높이는 잘 맞았지만 옆얼굴의 방향이 요청과 반대로 나왔습니다. 방향·크기·기준선을 따로따로 문장으로 적는 연습입니다.",
      attach="refs/moa_anime_base.png, refs/moa_sheet.png",
      steps=["새 대화를 열고 참고 그림을 첨부합니다.", "프롬프트를 붙여 넣어 만듭니다.", "그림 위에 세 얼굴의 위 눈꺼풀을 잇는 가로선을 긋고, 코 밑·턱도 같은 높이인지 봅니다.",
             "리본이 세 얼굴 모두 왼쪽 귀 위에 있는지(정면에서는 그림의 오른쪽) 확인합니다."],
      prompts=[("넣을 프롬프트", P("16:9", "Character turnaround sheet of " + who("moa") + ", head and shoulders, three views in one row, same size: 1) front view; 2) three-quarter view turned toward the LEFT edge of the image; 3) strict side profile facing the LEFT edge of the image.",
               "One faint gray horizontal guide line runs across the whole sheet at the height of the upper eyelids; the upper eyelids, nose bottoms and chins of all three faces sit at the same heights. The white ribbon is always over her LEFT ear (on the right side of the image in the front view). Light from the upper left."),
               "d9_moa_turnaround", "예상 결과 — 모아의 정면·비스듬히·옆 얼굴 설정화. 세 얼굴이 모두 왼쪽을 향하고, 눈꺼풀이 한 가로선 위에 있음", "16/9")],
      check=[("옆얼굴이 왼쪽을 보나", None), ("세 얼굴의 위 눈꺼풀이 한 가로선 위에 있나", "#s2"), ("리본이 셋 다 왼쪽 귀 위에 있나", "#s4")],
      expect="세 얼굴의 크기와 높이가 고른 설정화가 나옵니다. 정면에서는 리본이 그림 오른쪽에 보이고, 비스듬한 얼굴과 옆얼굴은 왼쪽을 보며 리본이 뒤쪽(귀 위)에 걸립니다.",
      trouble=[("옆얼굴이 오른쪽을 본다", "그 얼굴만 좌우 반전하거나, 부분 수정으로 옆얼굴만 다시 그립니다. 반전하면 리본 위치도 함께 확인하세요."),
               ("세 얼굴 크기가 다르다", "'identical head size' 문장을 맨 앞으로 옮깁니다."),
               ("리본이 오른쪽 귀로 간다", "'ribbon over her LEFT ear'를 각 얼굴마다 따로 적습니다.")],
      more="5부 2단계 실험에서 '1/2 선 지키기'를 켜고 끄며, 받은 설정화의 가로선과 비교해 보세요."),
 dict(id="d2", title="가림 영역으로 표정만 바꾸기", goal="시아의 정면 그림에서 눈·눈썹·입만 칠해(가림 영역) 웃는 얼굴로 바꾸고, 머리카락과 옷은 그대로 둡니다.",
      why="표정 하나를 바꾸려고 그림 전체를 다시 만들면 머리 모양과 옷까지 바뀝니다. 5부 3단계에서 계산한 것처럼 얼굴 부위만(전체의 몇 %) 가리면 나머지는 지킬 수 있습니다.",
      attach="refs/sia_anime_base.png (①을 만든 뒤에는 ① 결과 그림)",
      steps=["새 대화를 열고 참고 그림을 첨부해 프롬프트 ①로 기본 그림을 만듭니다.", "받은 그림에서 도구의 '부분 수정(영역 칠하기)' 기능을 엽니다.",
             "눈썹 위에서 입 아래까지, 좌우는 두 눈 바깥까지 칠합니다. 머리카락과 목은 칠하지 않습니다.", "프롬프트 ②를 넣어 칠한 곳만 다시 그립니다.", "①과 ②를 나란히 놓고, 머리·귀걸이·옷이 그대로인지 봅니다."],
      prompts=[("① 기본 그림", P("2:3", "Front view, chest-up portrait of " + who("sia") + ", calm neutral expression, mouth closed, looking at the viewer.", "Light from the upper left."),
                "d10_sia_neutral", "예상 결과 ① — 담담한 표정의 시아 정면 그림(부분 수정 전)", "2/3"),
               ("② 부분 수정 — 칠한 곳에만", "Inside the painted area only: a bright happy smile with eyes gently closed in upward curves (smiling eyes), eyebrows relaxed and slightly raised, mouth open in a small smile. Keep the eye positions, the face outline, the hair, earrings and clothes unchanged.",
                "d10_sia_smile", "예상 결과 ② — 눈·눈썹·입만 다시 그려 웃는 얼굴이 된 시아. 머리와 옷은 ①과 같음", "2/3")],
      check=[("가림 영역이 눈썹~입 아래, 두 눈 바깥까지였나(머리카락 제외)", "#s3"), ("머리·귀걸이·옷이 ①과 같나", "#s3"), ("웃는 눈의 위치가 ①의 눈 위치와 같은가", "01_front_female.html#s1")],
      expect="①과 ②를 나란히 놓으면 표정만 바뀐 같은 그림으로 보입니다. 웃는 눈은 ①의 눈과 같은 높이에서 휘어지고, 머리카락 한 올까지 그대로입니다.",
      trouble=[("머리 모양이 바뀌었다", "칠한 영역이 앞머리까지 덮었는지 봅니다. 영역 위쪽을 눈썹 위로 내립니다."),
               ("고친 곳의 경계가 어색하다", "영역을 조금 넓히고 가장자리를 부드럽게(브러시 흐림) 칠합니다."),
               ("부분 수정 기능이 없다", "같은 대화에 'Same image, keep everything identical. Change only the facial expression: …'로 요청합니다. 다른 곳이 조금 바뀔 수 있습니다.")],
      more="5부 3단계 실험에서 받은 그림에 칠한 영역의 크기를 넣어, 전체의 몇 %를 다시 그렸는지 계산해 보세요."),
],
6: [
 dict(id="d1", title="실패 그림을 진단하고 한 문장으로 고치기", goal="6부 실패 그림 f3(뾰족한 턱)을 진단 순서대로 보고, 처음 걸린 항목(① 큰 틀)에 맞는 고치는 조각 한 문장으로 고칩니다.",
      why="실패를 보면 여러 곳을 한꺼번에 고치고 싶어집니다. 진단 순서에서 처음 걸린 곳 하나만 고쳐야 무엇이 원인이었는지 알 수 있습니다.",
      attach="assets/img/f3_chin.webp(6부 실패 카드 f3 그림을 내려받아 첨부), refs/doctor_sheet.png",
      steps=["6부 실패 카드 f3 그림을 내려받습니다(그림을 길게 눌러 저장).", "6부 1단계 진단 실험에서 f3를 골라 점검표를 위에서부터 눌러, 처음 걸리는 항목을 확인합니다(① 큰 틀).",
             "새 대화에 f3 그림과 박사 설정 시트를 첨부하고 프롬프트를 붙여 넣습니다.", "고친 그림에서 얼굴 길이 ÷ 폭이 1.6 안팎인지, 턱 끝이 평평한지 봅니다."],
      prompts=[("넣을 프롬프트", "Same character, same pose, framing, clothes and lighting as the attached image. Change only the face outline: shorten the lower face; a defined angular jaw with a square chin tip; face length about 1.6 times its width. Keep the eyes, glasses, eyebrows and hair unchanged. All characters are adults. No text, no letters, no numbers, no logos.",
                "d11_doctor_chin_fixed", "예상 결과 — f3의 뾰족한 턱을 고친 박사. 턱 끝이 평평하고 얼굴 길이가 알맞아짐", "2/3")],
      check=[("진단 실험에서 ① 큰 틀에서 처음 걸렸나", "#s1"), ("턱 끝이 평평하게 잘린 각진 턱이 됐나", "02_front_male.html#s1"), ("눈·안경·머리는 f3와 같은가", None)],
      expect="f3와 같은 박사가 같은 옷·자세로 나오되, 길고 뾰족하던 아래 얼굴이 짧아지고 턱 끝이 평평해집니다. 다른 곳을 건드리지 않았으니 '원인은 윤곽 도형'이었다는 것이 그대로 보입니다.",
      trouble=[("얼굴 전체가 새로 그려졌다", "첨부한 f3 그림을 기준으로 삼으라는 첫 문장을 지웠는지 봅니다. 부분 수정 기능으로 턱 아래만 칠해도 됩니다."),
               ("턱이 너무 짧아 둥글다", "'face length about 1.6 times its width'를 유지하고 'not round'를 덧붙입니다."),
               ("안경이 바뀌었다", "'keep the teal rectangular glasses exactly'를 덧붙입니다.")],
      more="같은 방법으로 f2(늘어진 가운데)를 진단하고, 이번에는 '② 높이 기준선'에 맞는 고치는 조각으로 고쳐 보세요."),
 dict(id="d2", title="나이 쏠림을 막는 문장", goal="둥근 볼·큰 눈처럼 앳된 신호를 쓰고 싶을 때, 성인 나이와 성인 비율을 함께 적어 모아를 20대 성인으로 받습니다.",
      why="6부에서 본 것처럼 둥근 볼·아주 큰 눈·낮은 부위가 겹치면 성인 캐릭터가 어려 보이는 쪽으로 쏠립니다. 이 시리즈는 그런 그림을 만들지 않으므로, 처음부터 막는 문장을 연습합니다.",
      attach="refs/moa_anime_base.png, refs/moa_sheet.png",
      steps=["새 대화를 열고 참고 그림을 첨부합니다.", "프롬프트를 붙여 넣어 만듭니다. 나이·비율 문장이 맨 앞에 있는 것을 확인하세요.",
             "받은 그림이 20대 성인으로 보이는지 봅니다. 목 길이, 어깨 너비, 얼굴 길이를 확인합니다.", "어려 보이면 그 그림은 쓰지 않고, 확인할 것의 링크로 돌아가 신호를 하나 줄여 새 대화에서 다시 만듭니다."],
      prompts=[("넣을 프롬프트", P("2:3", "An adult woman in her late twenties with adult proportions: " + who("moa") + ", working at a laptop at a desk, looking up with a warm smile.",
               "Age safeguards (important): adult face length with a defined chin, adult neck length and shoulder width, upper eyelids at half the head height; soft cheeks are fine but keep the jaw visible; large expressive eyes are fine but not oversized; mature, professional posture; modest clothing. Light from the upper left."),
               "d12_moa_adult", "예상 결과 — 노트북 앞에서 웃는 20대 성인 모아. 볼은 부드럽지만 턱선·목·어깨가 성인 비율", "2/3")],
      check=[("20대 성인으로 보이나(목·어깨·얼굴 길이)", "06_failure_lab.html#drift"), ("위 눈꺼풀이 머리 높이 1/2에 있나", "01_front_female.html#s1"), ("턱선이 보이나(머리카락이 다 가리지 않나)", "03_profile.html#s2")],
      expect="노트북 앞에서 고개를 든 모아가 나옵니다. 볼은 부드럽고 눈도 크지만, 턱선이 보이고 목과 어깨가 성인 비율이라 20대 연구원으로 자연스럽게 읽힙니다.",
      trouble=[("그래도 어려 보인다", "그 그림은 쓰지 않습니다. 'large expressive eyes' 문장을 지우고 'slim oval face'로 바꿔 신호를 하나 줄입니다."),
               ("교복처럼 보인다", "리본 타이와 앞치마가 학교 옷처럼 보이면 'maid-style lab apron over a cardigan, office setting'으로 장소와 소재를 적습니다."),
               ("노트북이 얼굴을 가린다", "'laptop low on the desk, face fully visible'을 덧붙입니다.")],
      more="5부 1단계 얼굴 문장 실험에서 둥근 볼 + 큰 눈 + 낮은 부위를 고르고, '나이·금지'를 넣었다 뺐다 하며 경고가 어떻게 바뀌는지 보세요."),
],
}

CONV_D = [("D01_part1", "1부 연습 과제", "refs/moa_anime_base.png, refs/moa_sheet.png", ["d1_moa_guides", "d2_moa_gap_one", "d2_moa_gap_wide"]),
          ("D02_part2", "2부 연습 과제", "refs/doctor_sheet.png", ["d3_doctor_signals", "d4_doctor_longmid", "d4_doctor_thirds"]),
          ("D03_part3_4", "3·4부 연습 과제", "refs/sia_anime_base.png, refs/sia_sheet.png, refs/doctor_sheet.png, refs/haru_anime_base.png, refs/haru_sheet.png", ["d5_sia_profile_left", "d6_doctor_neck", "d7_haru_sheet", "d8_haru_underrim"]),
          ("D04_part5", "5부 연습 과제", "refs/moa_anime_base.png, refs/moa_sheet.png, refs/sia_anime_base.png", ["d9_moa_turnaround", "d10_sia_neutral", "d10_sia_smile"]),
          ("D05_part6", "6부 연습 과제", "f3_chin(사이트 assets/img/f3_chin.webp), refs/doctor_sheet.png, refs/moa_anime_base.png, refs/moa_sheet.png", ["d11_doctor_chin_fixed", "d12_moa_adult"])]
HOW = {"d2_moa_gap_wide": "d2_moa_gap_one을 만든 같은 대화에 이어서", "d4_doctor_thirds": "d4_doctor_longmid를 만든 같은 대화에 이어서",
       "d10_sia_smile": "d10_sia_neutral 결과에서 '부분 수정(영역 칠하기)' — 눈썹 위~입 아래, 두 눈 바깥까지만 칠하기",
       "d11_doctor_chin_fixed": "f3_chin 그림을 첨부해 새 대화에서(또는 턱 아래만 칠해 부분 수정)"}

def items():
    out = {}
    for no, ds in DRILL.items():
        for d in ds:
            for lab, prompt, key, alt, ar in d["prompts"]:
                out[key] = (no, d["title"], lab, prompt, alt, ar)
    return out

if __name__ == "__main__":
    ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    D = os.path.join(ROOT, "docs", "image_requests_drill"); os.makedirs(os.path.join(D, "prompts"), exist_ok=True)
    IT = items(); rows = []; n = 0
    HEAD = ("해설 페이지의 '프롬프트 연습 과제' 예상 결과 그림을 한 장씩 차례로 만들어 줘.\n- 비율은 각 프롬프트 첫 줄을 따를 것(16:9는 가로 1920px 이상, 2:3은 세로 1536px 이상)\n"
            "- 첨부한 참고 이미지의 캐릭터 외형(얼굴·머리·색·장식)을 똑같이 지킬 것\n- 등장인물은 모두 20대 성인(박사는 30대 성인 남성). 노출·과장된 체형·교복 느낌·어려 보이는 얼굴 금지\n"
            "- 그림 안에 글자·숫자·로고 금지(연한 회색 기준선은 허용)\n- '같은 대화에 이어서'라고 적힌 그림은 바로 앞 그림을 바탕으로 적힌 것만 바꿀 것")
    for cid, title, att, keys in CONV_D:
        md = f"# {cid[:3]} · {title} — " + ", ".join(keys) + f"\n\n**첨부:** {att}\n\n**Genspark에 먼저 붙여 넣기 ↓**\n```\n{HEAD}\n```\n"
        for k in keys:
            no, dt, lab, prompt, alt, ar = IT[k]; n += 1
            how = HOW.get(k, "새로 만들기")
            rows.append([n, cid[:3], k, f"0{no}", dt, lab, ar.replace("/", ":"), how, ""])
            md += f"\n---\n## {k} — {no}부 「{dt}」 {lab}\n방법: {how}\nalt: {alt}\n```\n{prompt}\n```\n"
        open(os.path.join(D, "prompts", cid + ".md"), "w").write(md)
    with open(os.path.join(D, "checklist.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["order", "conversation", "file", "part", "drill", "prompt", "ratio", "how", "status"]); w.writerows(rows)
    open(os.path.join(D, "README.md"), "w").write(f"""# 그림 요청 꾸러미 3 — '프롬프트 연습 과제' 예상 결과 ({n}장)

부마다 연습 과제 2개(모두 12개)의 **예상 결과 그림**입니다. 페이지의 과제 프롬프트와 이 요청문의 프롬프트는 같습니다(원본: `build/content_drill.py`).

## 요청 순서 (Genspark 대화 하나 = 파일 하나)
| 순서 | 파일 | 장수 | 첨부 |
|---|---|---|---|
""" + "".join(f"| {i+1} | prompts/{c[0]}.md | {len(c[3])} | {c[2]} |\n" for i, c in enumerate(CONV_D)) + """
## 주의
- 두 장이 짝인 과제(d2·d4·d10)는 **같은 대화에서 차례로** 만듭니다. 둘째 그림은 적힌 것만 바뀌어야 합니다.
- d10_sia_smile은 그림 생성이 아니라 **부분 수정(영역 칠하기)** 기능으로 만듭니다. 칠하는 곳: 눈썹 위~입 아래, 두 눈 바깥까지(머리카락·목 제외).
- d11은 사이트의 실패 그림 `assets/img/f3_chin.webp`를 첨부해 고칩니다(꾸러미 안 `refs/f3_chin.webp`에 함께 넣음).
- d4_doctor_longmid는 연습용으로 일부러 만드는 실패 그림입니다. 도구가 고쳐 그리면 두 번까지만 다시 시도하고 그대로 주셔도 됩니다.
- 저장 이름은 `checklist.csv`의 `file` 열 그대로(png·jpg).
""")
    print("drill images", n)

# ---------------- 다시 시도(1차 실패·부분 성공 과제) ----------------
# 1차 결과에서 배운 것: 같은 대화의 작은 변화는 무시되기 쉽다 → 바뀌어야 할 곳만 칠하는 '부분 수정'으로 범위를 좁힌다.
# 방향은 낱말 하나보다 '무엇이 화면 어느 쪽에 있는지'로 적는다.
NOTEXT = " Do not change anything outside the painted area. All characters are adults. No text, no letters, no numbers, no logos."
RETRY = {
 "1-d2": dict(why="같은 대화에서 '눈 간격만 조금 넓게'는 반영되지 않았습니다. 눈과 눈썹만 칠해 다시 그리게 하고, 간격을 '눈 하나보다 확실히 넓게'로 키워 적습니다.",
   items=[("다시 시도 — 눈 사이 넓히기", "부분 수정: d2_moa_gap_one 그림에서 두 눈과 두 눈썹을 칠하기(눈 바깥으로 눈 반 개씩 더 넓게 칠함, 앞머리·코는 빼기)",
           "Inside the painted area only: redraw both eyes and both eyebrows placed farther apart, so the gap between the eyes is about 1.3 eye widths — clearly wider than one eye. Keep the eye size, eye shape, amber eye color, eyelashes and the gaze looking straight at the viewer." + NOTEXT,
           "r1_moa_gap_wide", "다시 시도 — 눈과 눈썹만 다시 그려 눈 사이를 넓힌 모아", "2/3", "눈 사이에 눈 하나가 넉넉히 들어가고, 머리·옷·표정은 ①과 같으면 성공")]),
 "2-d2": dict(why="연습용 실패(가운데가 긴 얼굴)부터 도구가 고쳐 그렸습니다. 코와 입 주변만 칠해 일부러 길게 만든 뒤, 같은 곳을 다시 칠해 세 간격을 맞춥니다.",
   items=[("다시 시도 ① — 가운데를 길게(연습용 실패)", "부분 수정: d4_doctor_longmid 그림에서 눈 아래~턱 끝(코·입·턱)을 칠하기, 안경과 귀는 빼기",
           "Practice failure for a teaching page. Inside the painted area only: make the nose clearly longer so the nose bottom sits much lower, and push the mouth down close to the chin, so the distance from the eyebrows to the nose bottom looks stretched and too long. Keep the jaw outline width." + NOTEXT,
           "r2_doctor_longmid", "다시 시도 ① — 코를 길게, 입을 턱 가까이 내려 가운데가 늘어진 박사(연습용 실패)", "2/3", "눈썹~코 밑이 코 밑~턱보다 눈에 띄게 길면 성공"),
          ("다시 시도 ② — 세 간격 맞추기", "부분 수정: 바로 앞 ① 결과에서 같은 곳(눈 아래~턱 끝)을 다시 칠하기",
           "Inside the painted area only: equal thirds — hairline to eyebrows, eyebrows to nose bottom, and nose bottom to chin are the same length. Shorten the nose and move the mouth up to one third of the way from the nose bottom to the chin." + NOTEXT,
           "r2_doctor_thirds", "다시 시도 ② — 코를 줄이고 입을 올려 세 간격을 맞춘 박사", "2/3", "①보다 코가 짧고, 세 간격 차이가 줄면 성공")]),
 "3-d1": dict(why="'LEFT'를 따로 적어도 오른쪽을 봤습니다. 방향을 낱말 대신 '화면 왼쪽 끝의 화분을 본다'처럼 무엇이 어디에 있는지로 적습니다. 그래도 반대로 나오면 좌우 반전이 가장 확실합니다(시아는 좌우가 같은 장식이라 반전해도 됩니다).",
   items=[("다시 시도 — 화면 왼쪽의 화분을 보는 시아", "새 대화: refs/sia_anime_base.png, refs/sia_sheet.png 첨부",
           P("2:3", "Composition (most important): a small potted plant sits on a shelf at the far LEFT edge of the image, and " + who("sia") + " looks at it in strict side profile. Her nose points toward the LEFT edge; the back of her head and her long black hair are on the RIGHT side of the image. Only her left side is visible; only one eye is visible.",
             "Profile rules: the ear a little behind the middle of the head; the eye seen from the side as a narrow tilted triangle; small slightly upturned nose tip; simplified lips; soft chin; neck tilted forward about five degrees with smooth curves. Light from the upper left."),
           "r3_sia_profile_left", "다시 시도 — 화면 왼쪽의 화분을 바라보는 시아의 옆얼굴", "2/3", "코끝이 그림의 왼쪽을 향하면 성공(아니면 좌우 반전)")]),
 "4-d1": dict(why="세 번째 얼굴의 눈썹이 거의 올라가지 않았습니다. 그 얼굴의 눈썹만 칠해 다시 그리고, '바깥 끝을 높이 올린 아치'로 분명히 적습니다.",
   items=[("다시 시도 — 세 번째 얼굴의 눈썹만", "부분 수정: d7_haru_sheet 그림에서 오른쪽(세 번째) 얼굴의 두 눈썹만 칠하기(앞머리에 가린 부분 포함, 눈꺼풀은 빼기)",
           "Inside the painted area only: eyebrows clearly raised and arched high, the outer ends lifted noticeably — a bold, self-assured look. Keep the half-lowered eyelids, the eyes, the bangs and the other two faces unchanged." + NOTEXT,
           "r4_haru_brows", "다시 시도 — 세 번째 얼굴의 눈썹만 높이 올린 하루의 표정 시트", "2/3", "세 번째 얼굴의 눈썹이 가운데 얼굴보다 분명히 높으면 성공")]),
 "4-d2": dict(why="언더림을 문장으로 풀어 적어도 위 테가 생겼습니다. 새로 만들지 말고, 렌즈 위의 테만 칠해 지웁니다. 지울 곳이 작고 분명해서 가장 확실한 방법입니다.",
   items=[("다시 시도 — 위 테 지우기", "부분 수정: d8_haru_underrim 그림에서 두 렌즈 위쪽 테(가는 띠)와 두 렌즈 사이 다리 위쪽만 칠하기",
           "Inside the painted area only: remove the glasses frame here and show what is behind it — her eyebrows, skin and bangs. The lenses now have no frame on the top edge. Keep the bottom frame, the side temples and the eyes unchanged." + NOTEXT,
           "r4_haru_underrim", "다시 시도 — 위 테를 지워 아래 테만 남은 안경을 쓴 하루", "2/3", "렌즈 위쪽에 테가 없고, 아래 테가 눈동자 아래를 지나면 성공")]),
 "5-d2": dict(why="부분 수정 결과 ②를 아직 받지 않았습니다. 같은 방법으로 다시 요청합니다.",
   items=[("다시 요청 — 부분 수정으로 웃는 얼굴", "부분 수정: d10_sia_neutral 그림에서 눈썹 위~입 아래, 좌우는 두 눈 바깥까지 칠하기(앞머리·귀걸이·목은 빼기)",
           "Inside the painted area only: a bright happy smile with eyes gently closed in upward curves (smiling eyes), eyebrows relaxed and slightly raised, mouth open in a small smile. Keep the eye positions and the face outline." + NOTEXT,
           "d10_sia_smile", "예상 결과 ② — 눈·눈썹·입만 다시 그려 웃는 얼굴이 된 시아. 머리와 옷은 ①과 같음", "2/3", "머리·귀걸이·옷이 ①과 같고 표정만 바뀌면 성공")]),
 "6-d1": dict(why="아래 얼굴은 짧아졌지만 턱 끝이 여전히 뾰족했습니다. 턱만 칠해 다시 그리고, 턱 끝의 너비를 '입 너비쯤'처럼 비교할 대상으로 적습니다.",
   items=[("다시 시도 — 턱만 칠해 각진 턱으로", "부분 수정: d11_doctor_chin_fixed 그림에서 입 바로 아래~턱 끝 아래, 좌우는 양쪽 턱 모서리까지 칠하기(입·목·옷깃은 빼기)",
           "Inside the painted area only: a shorter lower face with a wider, defined angular jaw; the chin tip is flat and square, about as wide as the mouth; clear jaw corners below the ears. Keep the mouth, the neck and the collar unchanged." + NOTEXT,
           "r6_doctor_chin", "다시 시도 — 턱만 다시 그려 턱 끝이 평평하고 각진 박사", "2/3", "턱 끝이 입 너비쯤으로 평평하고, 얼굴 길이 ÷ 폭이 1.6 안팎이면 성공")]),
}
BASE_OF = {"r1_moa_gap_wide": "d2_moa_gap_one", "r2_doctor_longmid": "d4_doctor_longmid", "r2_doctor_thirds": "r2_doctor_longmid(바로 앞 결과)", "r3_sia_profile_left": None,
           "r4_haru_brows": "d7_haru_sheet", "r4_haru_underrim": "d8_haru_underrim", "d10_sia_smile": "d10_sia_neutral", "r6_doctor_chin": "d11_doctor_chin_fixed"}

def make_retry_pack():
    ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    D = os.path.join(ROOT, "docs", "image_requests_retry"); os.makedirs(D, exist_ok=True)
    md = """# 그림 요청 꾸러미 4 — 연습 과제 다시 시도 (8장)

1차 결과에서 실패했거나 반만 된 과제 7개(+ 아직 받지 않은 1장)를 다시 요청합니다. 1차 결과 그림은 페이지에 '1차 시도'로 그대로 남기고, 이 결과는 '다시 시도' 자리에 넣습니다.

## 이번에 바꾼 요청 방법
- **같은 대화의 작은 변화는 무시되기 쉬웠습니다** → 바뀌어야 할 곳만 칠하는 **부분 수정(영역 칠하기)** 으로 범위를 좁힙니다(8장 중 7장).
- **방향은 낱말 하나로 잘 안 지켜졌습니다** → '화면 왼쪽 끝의 화분을 본다'처럼 무엇이 어디에 있는지로 적습니다.
- 칠하는 곳은 각 항목의 '방법'에 적었습니다. 칠할 바탕 그림은 꾸러미 `base/` 폴더에 있습니다.
- 성공 기준을 각 항목에 적었습니다. 기준에 못 미치면 같은 방법으로 한 번 더 시도하고, 그래도 안 되면 그대로 주셔도 됩니다(페이지에 있는 그대로 적습니다).

## 공통 안내(Genspark에 먼저 붙여 넣기)
```
해설 페이지 연습 과제의 '다시 시도' 그림을 만들어 줘.
- '부분 수정'이라고 적힌 그림은 새로 만들지 말고, 첨부한 바탕 그림에서 칠한 곳만 다시 그릴 것
- 칠한 곳 밖(머리·옷·배경·다른 얼굴)은 바꾸지 말 것
- 등장인물은 모두 20대 성인(박사는 30대 성인 남성). 노출·교복 느낌·어려 보이는 얼굴 금지
- 그림 안에 글자·숫자·로고 금지
```
"""
    rows = []; n = 0
    for k, r in RETRY.items():
        no, did = k.split("-")
        for lab, how, pr, key, alt, ar, ok in r["items"]:
            n += 1; base = BASE_OF.get(key)
            rows.append([n, f"0{no}", did, key, base or "새로 만들기", ar.replace("/", ":"), ok, ""])
            md += f"\n---\n## {n}) {key} — {no}부 「{[d for d in DRILL[int(no)] if d['id'] == did][0]['title']}」 {lab}\n- 왜 다시: {r['why']}\n- 방법: {how}\n- 바탕 그림: {('base/' + base + '.png') if base and not base.startswith('r2') else (base or '없음(새 대화)')}\n- 성공 기준: {ok}\n```\n{pr}\n```\n"
    open(os.path.join(D, "README.md"), "w").write(md)
    with open(os.path.join(D, "checklist.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["order", "part", "drill", "file", "base", "ratio", "success", "status"]); w.writerows(rows)
    return n

if __name__ == "__main__":
    print("retry images", make_retry_pack())

# ---------------- 3차 시도(새 대화 + 과장) ----------------
# 2차의 부분 수정은 작은 변화에서 반영되지 않았다(바탕 그림이 그대로 돌아옴). 3차는 새 대화에서 바뀐 모습을 처음부터, 크게 과장해 요청한다.
RETRY3 = {
 "1-d2": dict(why="부분 수정으로는 눈 간격이 바뀌지 않았습니다. 새 대화에서 눈 사이를 눈 1.5개로 과장해 처음부터 만들고, 1차 ①(d2_moa_gap_one)과 나란히 비교합니다.",
   items=[("3차 — 새 대화, 눈 사이 1.5개", "새 대화: refs/moa_anime_base.png, refs/moa_sheet.png 첨부",
           P("2:3", "Front view, chest-up portrait of " + who("moa") + ", neutral soft smile, looking straight at the viewer, irises centered.",
             "Eye spacing (most important): WIDE-SET EYES — the gap between her two eyes is about one and a half eye widths, clearly and obviously wider than one eye. The face outline is a normal width. Light from the upper left."),
           "t1_moa_gap_wide", "3차 — 새 대화에서 눈 사이를 눈 1.5개로 넓혀 만든 모아", "2/3", "1차 ①과 나란히 두었을 때 눈 사이가 한눈에 더 넓으면 성공")]),
 "2-d2": dict(why="2차에서 코 길이 차이는 조금 보였지만 '가운데가 늘어진 얼굴'은 나오지 않았습니다. 새 대화 두 개에서 ①은 크게 과장한 연습용 실패로, ②는 세 간격이 같은 짜인 얼굴로 따로 만듭니다.",
   items=[("3차 ① — 새 대화, 가운데를 과장해 길게", "새 대화 A: refs/doctor_sheet.png 첨부",
           P("2:3", "Practice failure for a teaching page. Front view, chest-up portrait of " + who("doctor") + ", neutral expression.",
             "Deliberately exaggerated proportions: a VERY long midface — the distance from the eyebrows to the nose bottom is about twice the distance from the nose bottom to the chin; a long nose; the mouth placed low, close to the chin; short chin. Everything else normal. Light from the upper left."),
           "t2_doctor_longmid", "3차 ① — 새 대화에서 가운데를 과장해 길게 만든 박사(연습용 실패)", "2/3", "눈썹~코 밑이 코 밑~턱보다 확실히 길면 성공"),
          ("3차 ② — 새 대화, 세 간격이 같은 얼굴", "새 대화 B(①과 다른 대화): refs/doctor_sheet.png 첨부",
           P("2:3", "Front view, chest-up portrait of " + who("doctor") + ", neutral expression.",
             "Proportions: equal thirds — hairline to eyebrows, eyebrows to nose bottom, and nose bottom to chin are exactly the same length; a short nose; the mouth one third of the way from the nose bottom to the chin; a compact, well-balanced face. Light from the upper left."),
           "t2_doctor_thirds", "3차 ② — 새 대화에서 세 간격을 같게 만든 박사", "2/3", "①과 나란히 두었을 때 코가 짧고 얼굴이 짜여 보이면 성공")]),
 "4-d1": dict(why="세 얼굴이 든 표정 시트에서는 한 얼굴의 눈썹만 바꾸기 어려웠습니다. 새 대화에서 세 번째 표정 하나만 크게 과장해 한 장으로 만들고, 1차 시트의 가운데 얼굴(눈꺼풀만 내린 얼굴)과 비교합니다.",
   items=[("3차 — 새 대화, 자신만만한 표정 한 장", "새 대화: refs/haru_anime_base.png, refs/haru_sheet.png 첨부",
           P("2:3", "Front view, chest-up portrait of " + who("haru") + ", a bold, smug, self-assured expression.",
             "Expression (most important): upper eyelids lowered to half (half-lidded eyes, still open); BOTH eyebrows raised very high above the eyes and strongly arched, the outer ends lifted far up, one eyebrow slightly higher than the other; a small confident one-sided smirk. Eye size and position as in the reference. Light from the upper left."),
           "t4_haru_brows", "3차 — 새 대화에서 눈꺼풀을 내리고 눈썹을 높이 올린 하루의 자신만만한 얼굴", "2/3", "눈썹이 1차 시트의 가운데 얼굴보다 확실히 높고 아치가 크면 성공")]),
 "4-d2": dict(why="'위 테 없음'을 적어도, 칠해 지우게 해도 위 테가 남았습니다. 그림 도구가 잘 아는 '테 없는 안경(rimless)'으로 바꿔 요청합니다. 테가 렌즈 위를 지나지 않는다는 원리(눈을 가리지 않음)는 같습니다.",
   items=[("3차 — 새 대화, 테 없는 안경", "새 대화: refs/haru_anime_base.png, refs/haru_sheet.png 첨부",
           P("2:3", "Front view, chest-up portrait of " + who("haru") + ", smiling softly, wearing rimless glasses.",
             "Glasses (most important): RIMLESS glasses — clear rectangular lenses with NO frame around them at all, held only by a tiny thin bridge between the lenses and thin temples at the outer edges; the lenses are slightly larger than her eyes; nothing crosses the eyes or the eyebrows; clear lenses with no glare. Light from the upper left."),
           "t4_haru_rimless", "3차 — 새 대화에서 테 없는 안경을 쓴 하루", "2/3", "렌즈 위아래에 테가 없고 눈·눈썹이 다 보이면 성공")]),
 "6-d1": dict(why="턱만 칠해 고치게 해도 턱이 그대로였습니다. 새 대화에서 f3와 같은 옷·구도로, 넓고 각진 턱을 과장해 처음부터 만들고 f3와 나란히 비교합니다.",
   items=[("3차 — 새 대화, 넓고 각진 턱", "새 대화: refs/doctor_sheet.png 첨부(f3 그림은 첨부하지 않음 — 첨부하면 뾰족한 턱을 따라 그리기 쉬움)",
           P("2:3", "Front view, chest-up portrait of " + who("doctor", "white lab coat over a black vest, white shirt and black tie") + ", calm neutral expression.",
             "Face outline (most important): a SHORT lower face with a VERY WIDE, strongly angular jaw; clear jaw corners right below the ears; the chin tip is flat and broad, about as wide as the mouth; the face is only about 1.4 times as long as it is wide. Not pointed, not narrow. Light from the upper left."),
           "t6_doctor_chin", "3차 — 새 대화에서 넓고 각진 턱으로 만든 박사", "2/3", "f3와 나란히 두었을 때 턱 끝이 평평하고 넓으며 얼굴이 짧으면 성공")]),
}

def make_retry3_pack():
    ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    D = os.path.join(ROOT, "docs", "image_requests_retry3"); os.makedirs(D, exist_ok=True)
    md = """# 그림 요청 꾸러미 5 — 연습 과제 3차 시도 (6장)

2차 다시 시도에서 실패 4개, 부분 성공 1개가 나온 과제를 한 번 더 요청합니다. 1차·2차 결과는 페이지에 그대로 남기고, 이 결과는 '3차 시도' 자리에 넣습니다.

## 이번에 바꾼 방법
- 2차의 **부분 수정은 작은 변화에서 반영되지 않았습니다**(받은 그림이 바탕 그림과 거의 같았음). 그래서 이번에는 부분 수정을 쓰지 않습니다.
- **항목마다 새 대화**를 열고, 바뀐 모습을 **처음부터 크게 과장해** 요청합니다(눈 사이 1.5개, 가운데 길이 2배, 눈썹 아치 크게, 테 없는 안경, 아주 넓은 턱).
- 2부 ①·②는 **서로 다른 새 대화**에서 따로 만듭니다(같은 대화면 ②가 ①을 따라 그리기 쉬움).
- 6부 턱은 f3 그림을 **첨부하지 않습니다**(첨부하면 뾰족한 턱을 따라 그림).
- 성공 기준에 못 미치면 같은 대화에서 'Make the change much stronger.' 한 줄만 덧붙여 한 번 더 해 보고, 그래도 안 되면 그대로 주세요(페이지에 있는 그대로 적습니다).

## 공통 안내(Genspark 새 대화마다 먼저 붙여 넣기)
```
해설 페이지 연습 과제의 '3차 시도' 그림을 한 장 만들어 줘.
- 첨부한 참고 그림의 캐릭터 외형(얼굴·머리·색·장식)을 똑같이 지킬 것
- 프롬프트에 'most important'로 적힌 부분을 가장 먼저, 분명하게 지킬 것(과장해도 됨)
- 등장인물은 모두 20대 성인(박사는 30대 성인 남성). 노출·교복 느낌·어려 보이는 얼굴 금지
- 그림 안에 글자·숫자·로고 금지
```
"""
    rows = []; n = 0
    for k, r in RETRY3.items():
        no, did = k.split("-")
        title = [d for d in DRILL[int(no)] if d["id"] == did][0]["title"]
        for lab, how, pr, key, alt, ar, ok in r["items"]:
            n += 1
            rows.append([n, f"0{no}", did, key, how, ar.replace("/", ":"), ok, ""])
            md += f"\n---\n## {n}) {key} — {no}부 「{title}」 {lab}\n- 왜 다시: {r['why']}\n- 방법: {how}\n- 성공 기준: {ok}\n```\n{pr}\n```\n"
    open(os.path.join(D, "README.md"), "w").write(md)
    with open(os.path.join(D, "checklist.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["order", "part", "drill", "file", "how", "ratio", "success", "status"]); w.writerows(rows)
    return n

if __name__ == "__main__":
    print("retry3 images", make_retry3_pack())
