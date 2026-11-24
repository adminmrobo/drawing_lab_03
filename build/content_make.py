# -*- coding: utf-8 -*-
"""부마다 '프롬프트로 직접 만들어 보기' 실습. A 프롬프트는 make_requests.py(이 페이지 그림을 만드는 프롬프트)에서 가져온다.
res: 실제 결과 기록. 그림을 만들기 전에는 '아직 만들지 않음'을 그대로 적고, 그림이 들어오면 A·B를 나란히 보고 실제로 달라진 점을 적는다."""

PENDING = "실제 결과: 아직 그림을 만들지 않았습니다. A·B 그림이 들어오면 나란히 놓고 실제로 무엇이 달라졌는지(또는 달라지지 않았는지) 이 자리에 적습니다."

def T(key, title, goal, b_title, b_text, check, tip=None, b_key=None, res=PENDING):
    return dict(key=key, title=title, goal=goal, b_title=b_title, b_text=b_text, check=check, tip=tip, img=key, b_imgs=[b_key or key + "_b"], res=res)

MAKE = {
1: [
 T("p1_moa_front_base", "밑그림과 완성 얼굴을 한 장에", "원·십자선·기준선이 있는 밑그림과 완성 얼굴을 나란히 만들어, 기준선 위에 부위가 얹히는지 눈으로 확인합니다.",
   "B — 원리 빼기: 기준선 없이 눈을 위로", "Same image, keep the same framing. Change only: in both panels place the eyes high, about one third from the top of the head, and remove the horizontal guide lines. Still no text.",
   [("완성 얼굴의 위 눈꺼풀이 머리 높이의 한가운데에 걸리나", "#s1"), ("눈 사이가 눈 하나보다 조금 넓은가", "#s3"), ("B 결과에서 이마가 좁고 턱이 길어 다른 사람처럼 보이는지 비교", "#s1")]),
 T("p1_moa_cheek_compare", "볼 높이만 바꾼 두 얼굴", "같은 성인 모아의 볼 높이만 바꿔 인상이 어떻게 달라지는지 봅니다.",
   "B — 원리 빼기: 볼 높이를 같게", "Same image, keep the same framing. Change only: give both faces exactly the same outline with the cheeks fullest at mouth level. Still no text.",
   [("왼쪽은 둥근 인상, 오른쪽은 갸름한 인상인가", "#s2"), ("두 얼굴 모두 20대 성인으로 보이나(어려 보이면 다시 생성)", "06_failure_lab.html#drift"), ("B 결과에서 두 얼굴이 구별되지 않는 것을 확인", None)]),
],
2: [
 T("p2_doctor_front_base", "원 + 장기말 밑그림과 박사 얼굴", "원 아래 오각형을 붙인 밑그림이 완성 얼굴의 각진 턱으로 이어지는지 봅니다.",
   "B — 원리 빼기: 원 하나로 둥근 턱", "Same image, keep the same framing. Change only: build the face from a single circle like a soft rounded female face, with a short round chin. Still no text.",
   [("턱 끝이 평평하게 잘린 각진 턱인가", "#s1"), ("머리선~눈썹~코 밑~턱 세 간격이 같은가", "#s2"), ("B 결과가 앳되거나 다른 사람처럼 보이는지 비교", "#s3")]),
 T("p2_doctor_bust", "목과 어깨까지", "목 굵기와 어깨 너비가 머리를 받치는지 봅니다.",
   "B — 원리 빼기: 좁은 어깨와 가는 목", "Same image, keep the same framing. Change only: make the neck very thin and the shoulders only as wide as the head. Still no text.",
   [("목이 검은 눈동자 사이만큼 굵은가", "#s4"), ("어깨가 머리 너비의 2배 남짓인가", "#s4"), ("B 결과에서 머리가 떠 보이는지 비교", None)]),
],
3: [
 T("p3_sia_doctor_profile", "시아와 박사의 옆얼굴", "여성과 남성 옆얼굴의 귀 위치, 코·입술 굴곡, 목 기울기 차이를 한 장에서 봅니다.",
   "B — 원리 빼기: 귀를 한가운데로", "Same image, keep the same framing. Change only: move both ears forward to the exact middle of the head. Still no text.",
   [("시아 귀는 조금 뒤, 박사 귀는 꽤 뒤에 있나", "#s2"), ("시아 입술 굴곡은 작고, 박사는 콧날이 곧은가", "#s3"), ("B 결과에서 얼굴이 납작해 보이는지 비교", "#s2")]),
 T("p3_sia_doctor_profile", "같은 그림으로 목 바꿔 보기", "목을 똑바로 세우고 직선으로 이으면 어떻게 보이는지 같은 그림에서 비교합니다.",
   "B — 원리 빼기: 목을 수직·직선으로", "Same image, keep the same framing. Change only: make both necks perfectly vertical and join them to the head and back with sharp straight corners. Still no text.",
   [("A의 목은 5° 앞으로 기울고 곡선으로 이어졌나", "#s4"), ("목 너비가 시아 1/4, 박사 1/2 정도인가", "#s4"), ("B 결과가 인형처럼 굳어 보이는지 비교(6부 f6와 같은 실패)", "06_failure_lab.html#f6")],
   b_key="p3_sia_doctor_profile_b2"),
],
4: [
 T("p4_haru_lids_glasses", "한 곳만 바꾸기 — 눈꺼풀과 안경", "기본 얼굴에서 눈꺼풀만, 안경만 바꿔도 같은 하루로 보이는지 봅니다.",
   "B — 원리 빼기: 눈 자체를 작게", "Same image, keep the same framing. Change only: in the middle panel make the eyes smaller and narrower instead of lowering the eyelids. Still no text.",
   [("가운데 얼굴의 눈 크기와 자리가 첫 얼굴과 같은가", "#s1"), ("안경 아래 테가 눈 아래에 있어 눈동자를 가리지 않나", "#s2"), ("B 결과의 가운데 얼굴이 다른 사람처럼 보이는지 비교", None)]),
 T("p4_haru_lids_glasses", "안경 테 바꿔 보기", "작은 테로 바꾸면 눈이 가려지는지 같은 그림에서 비교합니다.",
   "B — 원리 빼기: 작고 가는 테", "Same image, keep the same framing. Change only: in the third panel use small thin full-rim glasses whose frame crosses the middle of the irises. Still no text.",
   [("A의 테는 눈동자를 가로지르지 않나", "#s2"), ("B 결과에서 표정이 읽히지 않는지 비교(6부 f7과 같은 실패)", "06_failure_lab.html#f7"), ("나머지 두 얼굴은 바뀌지 않았나", None)],
   b_key="p4_haru_lids_glasses_b2"),
],
5: [
 T("p5_sia_turnaround", "세 각도 설정화", "정면·비스듬히·옆 얼굴의 위 눈꺼풀이 같은 높이에 있는지 봅니다.",
   "B — 원리 빼기: 각도마다 따로 요청", "Make three separate images in three NEW conversations (one each: front view / three-quarter view / side profile of Sia), with no mention of shared guide lines. Then place the three results side by side.",
   [("A의 세 얼굴 위 눈꺼풀이 같은 높이인가 — 결과 위에 가로선을 그어 확인", "#s2"), ("세 얼굴이 같은 사람으로 보이나", "#s2"), ("B 세 장을 나란히 놓으면 눈 높이가 흔들리는지 비교", None)],
   tip="B는 일부러 따로 만든 세 장입니다. 한 번의 요청에 여러 변화를 넣지 않고, 차이가 약하면 새 대화에서 처음부터 다시 만들어 보세요."),
 T("p5_moa_styles", "화풍 세 가지", "화풍이 바뀌어도 높이 기준과 고정 장식이 남는지 봅니다.",
   "B — 원리 빼기: 비율까지 바꾸기", "Same image, keep the same framing. Change only: in the photorealistic panel, move the eyes higher, make the face longer and remove the headband and ribbon. Still no text.",
   [("세 얼굴의 위 눈꺼풀·코 밑 높이가 같은가", "#s4"), ("흰 프릴 머리띠와 왼쪽 리본이 셋 다 있나", "#s4"), ("실사풍이 실존 인물과 닮지 않았나(닮았으면 다시 생성)", None)]),
],
6: [
 T("f1_eyes", "몰린 눈 고치기", "실패 그림 f1을 고치는 문장 조각으로 다시 만들어, 진단이 맞았는지 확인합니다.",
   "B — 고치는 조각 넣기(부분 수정)", "Use the image edit / inpainting tool. Paint over only the eyes and eyebrows (not the hair). Prompt: eyes spaced slightly more than one eye width apart, symmetrical eye boxes on the eye line. Keep everything else unchanged.",
   [("눈 사이가 눈 하나보다 조금 넓어졌나", "01_front_female.html#s3"), ("머리카락·윤곽은 그대로인가(가림 영역이 알맞았나)", "05_ai_face.html#s3"), ("고친 눈과 얼굴이 따로 놀지 않나", None)], b_key="f1_fixed"),
 T("f7_glasses", "눈 가린 안경 고치기", "실패 그림 f7을 고치는 조각으로 다시 만들어 봅니다.",
   "B — 고치는 조각 넣기", "Same image, keep the same framing. Change only: replace the glasses with large rectangular under-rim glasses (no top frame) that do not cross the eyes.",
   [("테가 눈동자를 가로지르지 않나", "04_variation.html#s2"), ("얼굴의 다른 곳은 바뀌지 않았나", None), ("하루의 고정값(번 2개, 남색 줄)이 남았나", None)], b_key="f7_fixed"),
],
}
