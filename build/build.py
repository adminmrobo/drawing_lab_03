# -*- coding: utf-8 -*-
"""구조 먼저 그리기 연구실 03 · 얼굴 편 — 페이지 빌드.
python3 build/build.py 로 index.html, 01~06 페이지, practice/index.html 을 다시 만든다.
그림 파일(assets/img/{키}.webp)이 있으면 넣고, 없으면 '그림 준비 중' 자리만 둔다."""
import json, os, html, sys
sys.path.insert(0, os.path.dirname(__file__))
from content_a import P1, P2, P3
from content_b import P4, P5, P6
from content_make import MAKE
from make_requests import PROMPTS, CONV_OF, ATTACH_OF

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VER = "v1.0"
DATE = "2026-11-24"
SITE = "https://adminmrobo.github.io/drawing_lab_03/"
PREV_SITE = "https://adminmrobo.github.io/structure_first_drawing_lab_01/"
FIRST_SITE = "https://adminmrobo.github.io/adminmrobo-structure_first_drawing_lab/"
REPO = "https://github.com/adminmrobo/drawing_lab_03"
AUTHOR_URL = "https://adminmrobo.github.io/who_am_i/who_am_i.html"
RENDER = "https://adminmrobo.github.io/ai_rendering/"
CHARREPO = "https://github.com/adminmrobo/fruitfly-lab-expressions"
SERIES = "구조 먼저 그리기 연구실 03 · 얼굴 편"
E = html.escape
PARTS = [P1, P2, P3, P4, P5, P6]

CH = {
 "doctor": ("박사", "해설 + 남성 모델(2부, 3·4부 손님). 짙은 머리의 흰 줄, 굵은 눈썹, 청록 사각 안경"),
 "haru": ("조수 하루", "모델(4부) + 수식 상자 담당. 어려운 식을 대신 묻는다"),
 "sia": ("시아", "인턴1 · 모델(3부 옆얼굴). 흑발, 머리 장식 없음"),
 "moa": ("모아", "인턴2 · 모델(1부 정면 얼굴). 흰 프릴 머리띠와 왼쪽 귀 위 흰 리본"),
 "jupanbot": ("주판봇", "화가 A. 눈부터, 결과부터 서두른다 — 흔한 실수 담당"),
 "fruitfly": ("초파리 연구원", "화가 B. 원과 기준선부터 의심한다. \"이걸 눌러 봐\""),
 "x1": ("X1", "평가단. 닮음을 본다"),
 "x2": ("X2", "평가단. 원리를 본다"),
 "x3": ("X3", "평가단. 자연스러움을 본다"),
}
COLOR = {"doctor": "doc", "haru": "asst", "fruitfly": "fly", "jupanbot": "robo", "sia": "sia", "moa": "moa", "x1": "x", "x2": "x", "x3": "x"}

def face(k, e="e13", pre="", cls=""):
    n = CH[k][0]
    return f'<img src="{pre}assets/chars/{k}_{e}.webp" alt="{E(n)}" width="96" height="96" loading="lazy"{(" class=%s" % cls) if cls else ""}>'

def has_img(key):
    return os.path.exists(os.path.join(ROOT, "assets", "img", key + ".webp"))

def art(key, alt, ar="16/9", cap=None, pre="", cls=""):
    cap_html = f"<figcaption>{E(cap)}</figcaption>" if cap else ""
    if has_img(key):
        return f'<figure class="art {cls}" data-img="{key}"><img src="{pre}assets/img/{key}.webp" alt="{E(alt)}" loading="lazy" decoding="async">{cap_html}</figure>'
    return (f'<figure class="art {cls}" data-img="{key}"><div class="ph-art" style="--ar:{ar}" role="img" aria-label="{E(alt)}">'
            f'<b>그림 준비 중 · {key}</b><span>{E(alt)}</span></div>{cap_html}</figure>')

def head(title, desc, og, path, pre=""):
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta property="og:type" content="article"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}">
<meta property="og:image" content="{SITE}assets/og/{og}"><meta property="og:url" content="{SITE}{path}"><meta name="twitter:card" content="summary_large_image">
<meta name="author" content="안상선">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{pre}assets/lab.css">
</head>
<body data-root="{pre}">
<div id="prog"></div>
"""

def nav(links, pre=""):
    a = "".join(f'<a href="{h}">{E(t)}</a>' for h, t in links)
    return f'<nav class="top"><div class="row"><a class="logo" href="{pre}index.html">구조 먼저 그리기 <i>· 얼굴 편</i></a><div class="links">{a}</div></div></nav>\n'

def cover(key, cap, cast, pre=""):
    if has_img(key):
        return f'<div class="cover"><div class="frame" data-img="{key}"><img class="art" src="{pre}assets/img/{key}.webp" alt="{E(cap)}" width="1600" height="900" fetchpriority="high" decoding="async"></div></div>\n'
    # 그림이 오기 전 픽셀 대체 표지: 네모 격자 + 상자·원기둥 마네킹(픽셀 블록) + 픽셀 캐릭터
    cells = []
    for x in range(0, 1600, 40):
        for y in range(0, 900, 40):
            if (x // 40 + y // 40) % 2 == 0:
                cells.append(f'<rect x="{x}" y="{y}" width="40" height="40" fill="#f3f6fa"/>')
    px = []
    import math as _m
    for gx in range(1040, 1400, 20):
        for gy in range(120, 600, 20):
            dx, dy = gx + 10 - 1220, gy + 10 - 330
            if abs(_m.hypot(dx, dy * 1.0) - 170) < 11 and gy < 400 or (gy >= 400 and abs(abs(dx) - (170 - (gy - 400) * 0.85)) < 11 and gy < 580):
                px.append(f'<rect x="{gx}" y="{gy}" width="20" height="20" fill="#1e2f6e"/>')
    for gy in range(140, 580, 20): px.append(f'<rect x="1210" y="{gy}" width="20" height="20" fill="#e0337f" opacity=".55"/>')
    for gx in range(1060, 1380, 20): px.append(f'<rect x="{gx}" y="330" width="20" height="20" fill="#e0337f" opacity=".55"/>')
    bl = "".join(px)
    easel = '<rect x="240" y="180" width="300" height="380" fill="#ffffff" stroke="#8a5a2b" stroke-width="12"/><rect x="270" y="560" width="20" height="260" fill="#8a5a2b"/><rect x="490" y="560" width="20" height="260" fill="#8a5a2b"/>' + \
            "".join(f'<rect x="{300+i*40}" y="{240+j*40}" width="40" height="40" fill="{c}"/>' for i, j, c in [(1,0,"#d8c09a"),(2,0,"#d8c09a"),(0,1,"#d8c09a"),(1,1,"#f8e3d3"),(2,1,"#f8e3d3"),(3,1,"#d8c09a"),(1,2,"#4a3b5c"),(2,2,"#4a3b5c"),(0,2,"#f8e3d3"),(3,2,"#f8e3d3"),(1,3,"#f8e3d3"),(2,3,"#f8e3d3"),(1,4,"#f8e3d3"),(2,4,"#f8e3d3")])
    imgs = "".join(face(k, e, pre) for k, e in cast)
    return f"""<div class="cover"><div class="frame" data-img="{key}"><svg class="grid" viewBox="0 0 1600 900" preserveAspectRatio="xMidYMid slice" aria-hidden="true" shape-rendering="crispEdges">{''.join(cells)}{easel}{bl}</svg>
<span class="cap">{E(cap)}</span><span class="badge">표지 그림 준비 중 · {key}</span><div class="cast" style="image-rendering:pixelated">{imgs}</div></div></div>
"""

def three(a, b, c, abbr):
    dl = "".join(f"<dt>{E(x)}</dt><dd>{E(y)}</dd>" for x, y in abbr)
    return f"""<div class="three"><h2>처음 오신 분께 — 세 줄 요약</h2><ul>
<li><b>무엇을</b>: {E(a)}</li><li><b>왜 알아야 하나</b>: {E(b)}</li><li><b>어디에 쓰나</b>: {E(c)}</li></ul>
<p>그림 실력·코드·수식을 몰라도 됩니다. 실험을 눌러 보며 따라오세요.</p>
<details class="abbr"><summary>낱말·약어 풀이 (펼치기)</summary><dl>{dl}</dl></details></div>\n"""

ABBR = [("기준선", "얼굴 높이를 나누는 가로선. 위 눈꺼풀 1/2, 코 밑은 턱에서 1/4, 머리선은 꼭대기에서 1/6"), ("머리 높이", "머리 꼭대기에서 턱 끝까지(머리카락 제외)"),
        ("장기말(오각형)", "남성 턱을 그릴 때 원 아래에 거꾸로 붙이는 오각형. 일본 장기 말 모양"), ("세 간격", "머리선~눈썹, 눈썹~코 밑, 코 밑~턱. 같을 때 짜인 얼굴"),
        ("눈 상자", "눈을 그려 넣는 네모. 여성 세로:가로 약 1:1, 남성 약 1:2"), ("눈머리", "눈의 코 쪽 끝. 애니풍 여성 눈은 이 부분을 생략한다"),
        ("데포르메", "실제 모양을 줄이거나 과장해 단순하게 그리는 것"), ("늘어진 얼굴", "부위 사이가 길어 얼굴이 길고 멍해 보이는 상태(일본어 間延び)"),
        ("림·언더림", "림은 렌즈 테, 언더림은 위 테가 없는 안경"), ("흉쇄유돌근", "귀 뒤에서 쇄골 가운데로 비스듬히 내려가는 목 근육"),
        ("설정화(턴어라운드)", "한 캐릭터를 정면·비스듬히·옆·뒤로 나란히 그린 기준 그림"), ("가림 영역(마스크)", "AI가 다시 그릴 부분을 표시한 영역"),
        ("부분 수정(인페인팅)", "가림 영역만 다시 그리고 나머지는 그대로 두는 AI 기능")]

def talk(lines, pre=""):
    out = []
    for k, e, t in lines:
        side = " r" if k in ("moa", "sia") else ""
        out.append(f'<div class="line{side}">{face(k, e, pre)}<div class="bub"><b style="color:var(--c-{COLOR[k]})">{E(CH[k][0])}</b>{E(t)}</div></div>')
    return '<div class="talk">' + "".join(out) + "</div>"

def quiz(q, opts, ans, ok, no):
    b = "".join(f'<button type="button">{E(o)}</button>' for o in opts)
    return f'<div class="quiz" data-ans="{ans}"><div class="qq">확인 퀴즈 — {E(q)}</div><div class="opts">{b}</div><div class="fb" aria-live="polite"></div><span class="qok" hidden>{E(ok)}</span><span class="qno" hidden>{E(no)}</span></div>'

def panel(no, i, p):
    return (f'<div class="panel"><div class="ph"><b>실험 {no}-{i}</b><small>{E(p["note"])}</small></div>'
            f'<div id="pp-{p["key"]}" data-panel="{p["key"]}"></div><div class="ctrl">{p["ctrl"]}</div><div class="readout" aria-live="polite"></div></div>')

def mathbox(m):
    tries = "".join(f"<div>{E(t)}</div>" for t in m["tries"])
    pcs = "".join(f"<tr><td class='m'>{E(a)}</td><td>{E(b)}</td></tr>" for a, b in m["pieces"])
    return f"""<div class="box mathbox"><h4>수식이 어려운 조수가 대신 묻습니다</h4>
<div class="q">{face('haru','e04')}<div><b>조수</b> {E(m['ask'])}</div></div>
<div class="easy"><b>말로 하면</b> — {E(m['words'])}</div>
<div class="try"><b>숫자로 한 번 해 보기</b>{tries}</div>
<p><b>학교 수학으로 보면</b> — {E(m['school'])}</p>
<div class="fx">{E(m['formula'])}</div>
<table><thead><tr><th>식 조각</th><th>뜻</th></tr></thead><tbody>{pcs}</tbody></table>
<div class="q">{face('haru','e16')}<div><b>조수</b> {E(m['comment'])}</div></div></div>"""

def step(P, i, s):
    no = P["no"]
    labels = ["무엇이 문제인가", "그냥 하면 막히는 곳", "이렇게 푼다"]
    why = "".join(f"<li><b>{labels[k]}</b> — {E(x)}</li>" for k, x in enumerate(s["why"]))
    whybox = f'<div class="box why"><h4>왜 이렇게 하나</h4><ol>{why}</ol><div class="easy"><b>쉽게 말하면</b> — {E(s["easy"])}</div></div>'
    calm = talk([("doctor", "e08", "여기서 한 번 멈춰도 괜찮아요. 식이 낯설면 건너뛰고 아래 실험부터 눌러 보세요. 숫자는 실험이 대신 계산해 줍니다.")])
    duo = f'<div class="duo">{whybox}{mathbox(s["math"])}</div>{calm}' if s.get("math") else f'<div style="margin:16px 0">{whybox}</div>'
    solve = "".join(f"<p>{E(x)}</p>" for x in s["solve"])
    extra = ""
    img = art(s["img"][0], s["img"][1], s["img"][2], s["img"][1], cls="tall" if s["img"][2] == "2/3" else "") if s.get("img") else ""
    q = s["quiz"]
    return f"""<section class="room" id="{s['id']}"><div class="wrap">
<div class="roomno">{no}부 · {i}단계</div>
<h2>{E(s['title'])}</h2><p class="muted">{E(s['sub'])}</p>
<div class="tags"><span class="tag how">{E(s['how'])}</span><span class="tag day">{E(s['day'])}</span></div>
{duo}
<div class="pair"><div class="box"><h4>일상으로 치면</h4><p>{E(s['daily'])}</p></div><div class="box ml"><h4>그림·VFX 현장에서는</h4><p>{E(s['field'])}</p></div></div>
{talk(s['talk'])}
{panel(no, i, s['panel'])}
<div class="solve"><h4>풀이</h4>{solve}</div>
{extra}{img}
<div class="solve"><h4>AI 결과, 그대로 써도 될까?</h4><p>{E(s['ai'][0])}</p><details class="code"><summary>답 보기</summary><p>{E(s['ai'][1])}</p></details></div>
<div class="limit"><b>주의할 점</b> — {E(s['limit'])}</div>
{quiz(q[0], q[1], q[2], q[3], q[4])}
</div></section>
"""

def judge(J):
    rows = ""
    for idx, item in enumerate(J["items"]):
        a, b = J["a"][1][idx], J["b"][1][idx]
        mx = 8 if "8개" in item else 10
        rows += f'<span>{E(item)}</span><span class="bar" title="{J["a"][0]} {a}"><i style="width:{a/mx*100:.0f}%"></i></span><span class="bar" title="{J["b"][0]} {b}"><i style="width:{b/mx*100:.0f}%;background:var(--teal)"></i></span>'
    sa, sb = sum(J["a"][1]), sum(J["b"][1])
    tbl = "".join(f"<tr><td>{E(it)}</td><td>{J['a'][1][k]}</td><td>{J['b'][1][k]}</td></tr>" for k, it in enumerate(J["items"]))
    return f"""<section class="room" id="judge"><div class="wrap"><div class="roomno">평가단 채점</div><h2>{E(J['title'])}</h2>
{talk(J['setup'])}
<div class="judge"><h4>평가단 X1·X2·X3 채점</h4>
<div class="score"><span></span><b>{E(J['a'][0])}</b><b>{E(J['b'][0])}</b>{rows}</div>
<div class="tbl" style="margin-top:10px"><table><thead><tr><th>항목</th><th>{E(J['a'][0])}</th><th>{E(J['b'][0])}</th></tr></thead><tbody>{tbl}<tr><th>합계</th><th>{sa}</th><th>{sb}</th></tr></tbody></table></div>
{talk(J['comments'])}</div>
{talk(J['result'])}
<p class="hint">점수는 이야기 속 예시입니다. 실제 그림을 평가한 값이 아닙니다.</p>
</div></section>
"""

def summary(P):
    rows = "".join(f"<tr><td>{E(a)}</td><td>{E(b)}</td><td>{E(c)}</td></tr>" for a, b, c in P["summary"])
    return f"""<section id="sum"><div class="wrap"><h2>{P['no']}부 정리</h2>
<div class="tbl"><table><thead><tr><th>주제</th><th>한 줄</th><th>작업에서는</th></tr></thead><tbody>{rows}</tbody></table></div></div></section>
"""

def outro(P):
    return f"""<section id="outro"><div class="wrap"><h2>다음으로</h2>{talk(P['outro'])}
<div class="next"><a href="{P['prev'][0]}">{E(P['prev'][1])}</a><a href="{P['next'][0]}">{E(P['next'][1])}</a></div></div></section>
"""

def failcard(f):
    note = f'<p class="hint">{E(f["note"])}</p>' if f.get("note") else ""
    return f"""<div class="failcard" id="{f['key'].split('_')[0]}"><h3>{E(f['title'])}</h3><div class="failgrid">
{art(f['key'], f['alt'], f['ar'])}
<div><p><span class="chip">증상</span>{E(f['symptom'])}</p>
{quiz(f['q'], f['opts'], f['ans'], f['ok'], f['no'])}
<p><span class="chip">연결된 원리</span><a href="{f['link'][0]}">{E(f['link'][1])}</a></p>
<div class="promptbox"><b>고치는 프롬프트 조각</b><pre>{E(f['fix'])}</pre></div>{note}</div></div></div>"""

# ---------------- 지식 색인
KG = [
 ("method/guide-lines", "Method", "높이 기준선", "Facial guide lines", "01_front_female.html", "#s1", "위 눈꺼풀 = 머리 높이 1/2, 코 밑 = 턱에서 1/4, 머리선 = 꼭대기에서 1/6"),
 ("method/carve-circle", "Method", "원 양옆 깎기", "Carving the face outline from a circle", "01_front_female.html", "#s2", "깎이는 초승달을 보며 윤곽을 만들고, 볼이 가장 불룩한 높이로 인상을 고른다"),
 ("concept/eye-box", "Concept", "눈 상자와 간격", "Eye boxes and spacing", "01_front_female.html", "#s3", "여성 눈 사이 ≈ 눈 너비 × 1.1, 가장자리 ≈ 0.4"),
 ("method/part-shift", "Method", "부위 함께 내리기", "Lowering facial features together", "01_front_female.html", "#s4", "늘어져 보이면 눈·코·입을 머리 높이의 1~2.5% 함께 내린다"),
 ("method/shogi-jaw", "Method", "원 + 장기말", "Circle plus inverted pentagon jaw", "02_front_male.html", "#s1", "원 중심 조금 아래에 거꾸로 세운 오각형을 붙여 남성 턱을 만든다"),
 ("concept/facial-thirds", "Concept", "세 간격", "Facial thirds", "02_front_male.html", "#s2", "(머리 높이 − 꼭대기~머리선) ÷ 3"),
 ("concept/sex-differences", "Concept", "남녀 부위 위치 차이", "Feature placement by sex", "02_front_male.html", "#s3", "남성은 코 밑이 조금 높고 입은 코 쪽 1/3, 귀가 높고 눈은 1:2"),
 ("concept/neck-shoulder", "Concept", "목과 어깨 너비", "Neck and shoulder width", "02_front_male.html", "#s4", "남: 목 = 눈동자 사이, 어깨 = 머리 너비 × 2.1 / 여: 목 = 눈 사이, 어깨 × 1.15"),
 ("method/profile-shapes", "Method", "옆얼굴 기본 도형", "Profile construction shapes", "03_profile.html", "#s1", "여: 원 + L자, 남: 상자 + 기울어진 컵 + 눕힌 달걀, 눈은 기울어진 삼각김밥"),
 ("concept/ear-position", "Concept", "옆얼굴 귀 위치", "Ear position in profile", "03_profile.html", "#s2", "이마~뒤통수의 여 55%, 남 66% 안팎"),
 ("concept/profile-relief", "Concept", "코~턱 굴곡의 양", "Amount of relief from nose to chin", "03_profile.html", "#s3", "여성은 입술 굴곡을 줄이고, 남성은 세 간격과 곧은 콧날"),
 ("concept/neck-tilt", "Concept", "목 기울기와 잇기", "Neck tilt and connection", "03_profile.html", "#s4", "목 끝 밀림 = 목 길이 × tan(5°), 곡선으로 잇는다"),
 ("method/eyelid-change", "Method", "눈꺼풀만 바꾸기", "Changing only the eyelids", "04_variation.html", "#s1", "눈 크기·자리는 그대로, 위 눈꺼풀만 내린다"),
 ("method/glasses-rim", "Method", "눈을 가리지 않는 안경", "Glasses that keep the eyes visible", "04_variation.html", "#s2", "림을 키우거나 언더림, 옆에서는 다리를 끊는다"),
 ("method/natural-front", "Method", "정면 자세 풀기", "Relaxing a front pose", "04_variation.html", "#s3", "얼굴은 정면, 어깨 5~8° 기울이고 살짝 비틀기"),
 ("method/profile-check", "Method", "옆얼굴 점검", "Profile check", "04_variation.html", "#s4", "머리 크기 원 → 턱 방향 → 눈·코"),
 ("method/face-prompt", "Method", "얼굴 문장", "Structured face prompt", "05_ai_face.html", "#s1", "성별·윤곽·눈·부위 높이·각도·성인 나이와 금지"),
 ("method/turnaround-line", "Method", "각도별 기준선 공유", "Shared eye line across angles", "05_ai_face.html", "#s2", "정면·비스듬히·옆의 위 눈꺼풀을 같은 가로선 위에"),
 ("method/face-inpaint", "Method", "얼굴 부위 가림 영역", "Inpainting facial features", "05_ai_face.html", "#s3", "바뀌는 비율 = 가린 넓이 ÷ 전체 넓이, 눈썹~입 아래만"),
 ("method/style-keep", "Method", "화풍별로 남길 것", "What to keep across styles", "05_ai_face.html", "#s4", "높이 기준은 그대로, 눈 모양·코·입술 표현만 바꾼다"),
 ("method/face-diagnosis", "Method", "얼굴 그림 진단 순서", "Face drawing diagnosis order", "06_failure_lab.html", "#s1", "큰 틀 → 높이 기준선 → 눈 상자 → 코·입·귀 → 목·어깨"),
 ("application/face-failures", "Application", "얼굴 그림 실패 8종", "Eight face drawing failures", "06_failure_lab.html", "#fails", "몰린 눈·늘어진 가운데·뾰족한 턱·부푼 뒤통수·튀어나온 턱·인형 목·눈 가린 안경·불룩한 입"),
 ("open/age-drift", "OpenQuestion", "나이가 어려 보이는 쏠림", "Apparent age drift", "06_failure_lab.html", "#drift", "둥근 볼·큰 눈·낮은 부위가 겹치면 어려 보인다. 성인 나이와 비율을 적어 막는다"),
 ("application/practice", "Application", "실전 연습장", "Practice simulator", "practice/index.html", "#bench", "비율 작업대·남녀 바꾸기판·얼굴 문장 공방·진단 데스크"),
 ("analogy/picture-frames", "Analogy", "액자 걸기", "Hanging picture frames on a level line", "01_front_female.html", "#s1", "높이 선부터 그으면 액자를 바꿔 걸어도 줄이 맞는다"),
 ("analogy/ice-cream-cone", "Analogy", "아이스크림 콘", "Ice cream cone", "02_front_male.html", "#s1", "공 하나에 콘을 붙이면 둥근 머리와 갸름한 아래가 생긴다"),
 ("analogy/blinds", "Analogy", "블라인드", "Window blinds", "04_variation.html", "#s1", "반쯤 내려도 창문 크기는 그대로"),
 ("analogy/melody", "Analogy", "같은 노래 다른 편곡", "Same melody, different arrangement", "05_ai_face.html", "#s4", "높이 기준이 멜로디, 화풍은 편곡"),
]
KG_EDGES = [("method/guide-lines","motivates","method/carve-circle"),("method/carve-circle","motivates","concept/eye-box"),("concept/eye-box","motivates","method/part-shift"),
 ("method/part-shift","motivates","method/shogi-jaw"),("method/shogi-jaw","motivates","concept/facial-thirds"),("concept/facial-thirds","motivates","concept/sex-differences"),("concept/sex-differences","motivates","concept/neck-shoulder"),
 ("concept/neck-shoulder","motivates","method/profile-shapes"),("method/profile-shapes","motivates","concept/ear-position"),("concept/ear-position","motivates","concept/profile-relief"),("concept/profile-relief","motivates","concept/neck-tilt"),
 ("concept/neck-tilt","motivates","method/eyelid-change"),("method/eyelid-change","motivates","method/glasses-rim"),("method/glasses-rim","motivates","method/natural-front"),("method/natural-front","motivates","method/profile-check"),
 ("method/profile-check","motivates","method/face-prompt"),("method/face-prompt","motivates","method/turnaround-line"),("method/turnaround-line","motivates","method/face-inpaint"),("method/face-inpaint","motivates","method/style-keep"),
 ("method/style-keep","motivates","method/face-diagnosis"),("method/face-diagnosis","usedIn","application/face-failures"),("method/face-prompt","explains","open/age-drift"),("method/carve-circle","explains","open/age-drift"),
 ("method/guide-lines","explains","method/turnaround-line"),("method/guide-lines","explains","method/style-keep"),("concept/eye-box","explains","method/glasses-rim"),("concept/neck-tilt","explains","application/face-failures"),
 ("analogy/picture-frames","explains","method/guide-lines"),("analogy/ice-cream-cone","explains","method/shogi-jaw"),("analogy/blinds","explains","method/eyelid-change"),("analogy/melody","explains","method/style-keep"),
 ("method/face-prompt","usedIn","application/practice"),("method/guide-lines","usedIn","application/practice")]
REFS = [
 dict(id="yanami_2018_face", title="男女の顔の描き分け 角度別・年齢別・表情別のキャラデッサン", author="YANAMi", year=2018, note="ホビージャパン. 1장 「基本の顔を描き分けよう」(정면·옆얼굴의 남녀 그리기 나누기)의 원리를 참고. 책의 그림·문장·도식·구성 순서는 옮기지 않고 연구실 캐릭터와 실험으로 새로 구성"),
 dict(id="loomis_1956_head", title="Drawing the Head and Hands", author="Andrew Loomis", year=1956, note="Viking Press — 구(원)에서 옆을 잘라 내고 턱을 붙여 머리를 짓는 방법, 얼굴 높이를 나누는 기준선"),
 dict(id="farkas_1985_canons", title="Vertical and horizontal proportions of the face in young adult North American Caucasians: revision of neoclassical canons", author="L. G. Farkas, J. C. Kolar, I. R. Munro et al.", year=1985, note="Plastic and Reconstructive Surgery 75(3) — 얼굴 세 간격 같은 고전 비율 기준이 실제 사람에게는 근사치임을 보인 연구(이 페이지의 비율은 그림용 예시)"),
 dict(id="lugmayr_2022_repaint", title="RePaint: Inpainting using Denoising Diffusion Probabilistic Models", author="Andreas Lugmayr et al.", year=2022, note="CVPR 2022. arXiv:2201.09865 — 가림 영역만 다시 그리는 방식"),
 dict(id="rombach_2022_ldm", title="High-Resolution Image Synthesis with Latent Diffusion Models", author="Robin Rombach et al.", year=2022, note="CVPR 2022. arXiv:2112.10752 — 글 지시로 그림을 만드는 확산 모델(부분 수정 포함)"),
 dict(id="prev_01", title="구조 먼저 그리기 연구실 01 · 옷장 편", author="안상선", year=2026, note="앞 편. 옷 주름·그림자와 AI·VFX. https://adminmrobo.github.io/structure_first_drawing_lab_01/"),
 dict(id="prev_series", title="구조 먼저 보는 캐릭터 그리기 연구실", author="안상선", year=2026, note="첫 시리즈. 구조·빛·주름 기초와 확산 모델·프롬프트 기초. https://adminmrobo.github.io/adminmrobo-structure_first_drawing_lab/"),
]

def kg_block(page, pages):
    nodes = [dict(id="lab:" + i, type=t, label=dict(ko=ko, en=en), page=p, anchor=a, definition=dict(ko=d), source="lab:work/structure_first_drawing_03")
             for i, t, ko, en, p, a, d in KG if p in pages]
    ids = {n["id"] for n in nodes}
    edges = [dict(s="lab:" + s, p=p, o="lab:" + o) for s, p, o in KG_EDGES if "lab:" + s in ids and "lab:" + o in ids]
    raw = dict(version="1.3", page=page, series=SERIES, nodes=nodes, edges=edges)
    ld = {"@context": {"@vocab": "urn:lab:", "skos": "http://www.w3.org/2004/02/skos/core#", "schema": "https://schema.org/"},
          "@graph": [{"@id": "urn:" + n["id"], "@type": n["type"], "skos:prefLabel": [{"@value": n["label"]["ko"], "@language": "ko"}, {"@value": n["label"]["en"], "@language": "en"}],
                      "skos:definition": n["definition"]["ko"], "schema:url": SITE + n["page"] + n["anchor"]} for n in nodes]}
    meta = dict(title=page, series=SERIES, creator=[dict(name="안상선", role="author", affiliation="(주)M-Robo")], date=DATE, version=VER, license="캐릭터·그림 무단 사용 금지")
    J = lambda o: json.dumps(o, ensure_ascii=False).replace("</", "<\\/")
    return f"""<section id="kg"><div class="wrap"><h2>지식 색인 — 이 페이지의 낱말 찾기</h2>
<p class="muted">이 페이지에 나온 개념·방법·비유·쓰임을 모았습니다. 검색하고, "설명 보러 가기"로 본문에 돌아갑니다.</p><div id="kg-mount"></div></div></section>
<section id="export"><div class="wrap"><h2>온톨로지·서지 꾸러미 내려받기</h2>
<p class="muted">지식 색인을 출처와 함께 파일로 내려받습니다. 서지 관리는 BibTeX·RIS, 온톨로지 편집은 Turtle, 그래프 도구는 CSV, 여러 페이지 합치기는 kg.json입니다.</p><div id="export-mount"></div></div></section>
<script type="application/json" id="kg-raw">{J(raw)}</script>
<script type="application/ld+json" id="kg-ld">{J(ld)}</script>
<script type="application/json" id="refs-csl">{J(REFS)}</script>
<script type="application/json" id="page-meta">{J(meta)}</script>
"""

FOOT_LINKS = [("index.html", "목차")] + [(P["file"], f"{P['no']}부") for P in PARTS] + [("practice/index.html", "7부 실전 연습장")]

def footer(pre=""):
    links = " · ".join(f'<a href="{pre}{h}">{E(t)}</a>' for h, t in FOOT_LINKS) + f' · <a href="{REPO}">저장소</a>'
    refs = "".join(f"<tr><td>[{i+1}]</td><td>{E(r['author'])} ({r['year']}). {E(r['title'])}</td><td>{E(r['note'])}</td></tr>" for i, r in enumerate(REFS))
    return f"""<footer><div class="wrap">
<h3>출처·참고</h3>
<div class="tbl"><table><thead><tr><th>#</th><th>자료</th><th>어디에 썼나</th></tr></thead><tbody>{refs}</tbody></table></div>
<h3>예시값·설명용 숫자</h3>
<p>기준선 비율(1/2·1/4·1/6), 눈 간격 배수, 장기말 비율, 귀 위치 %, 목·어깨 배수, 기울기 각도, 가림 영역 크기, 딱딱함 지수, 평가단 점수는 모두 원리를 보이기 위한 예시값입니다. 실제 사람과 화풍마다 다릅니다.</p>
<p>등장인물은 모두 성인 연구원입니다(하루·시아·모아는 20대, 박사는 30대 성인 남성). 실사풍 그림은 캐릭터를 코스프레한 가상의 성인 모델이며 실존 인물이 아닙니다. 다른 작품의 캐릭터를 닮은 그림은 만들지 않습니다.</p>
<p>캐릭터 이름·설정·그림은 저작권자 안상선의 허락 없이 사용할 수 없습니다. 캐릭터 그림: <a href="{CHARREPO}">fruitfly-lab-expressions</a>.</p>
<p>글 · 안상선 ((주)M-Robo 대표) · <a href="{AUTHOR_URL}">저자 소개</a> · {DATE} · {VER}</p>
<p>{links}</p>
</div></footer>
<script src="{pre}assets/panels.js"></script>
</body></html>
"""

REFS_DL = ["haru_anime_base.png", "sia_anime_base.png", "moa_anime_base.png", "haru_sheet.png", "sia_sheet.png", "moa_sheet.png", "doctor_sheet.png", "fruitfly_sprites_6.png", "jupanbot_ref_genspark_v0.png", "pixel_style_ref_prev_cover.png"]
def make_section(P):
    tasks = MAKE.get(P["no"])
    if not tasks:
        return ""
    refs = " · ".join(f'<a href="assets/refs/{f}" download>{f.replace(".png", "")}</a>' for f in REFS_DL)
    out = f"""<section class="room" id="make"><div class="wrap"><div class="roomno">{P['no']}부 · 직접 만들기</div><h2>프롬프트로 직접 만들어 보기</h2>
<div class="box"><p>이 부에서 배운 원리를 그림 생성 AI(Genspark 등)로 직접 확인합니다. <b>A</b>는 이 페이지 그림을 만드는 프롬프트, <b>B</b>는 원리를 하나 빼거나 바꾼 비교용 문장입니다.</p>
<ol style="margin:6px 0 0;padding-left:20px"><li>새 대화를 열고 아래 '첨부'에 적힌 참고 그림을 올립니다.</li><li>A를 붙여 넣어 만들고, 확인표로 결과를 점검합니다.</li><li>같은 대화에 B를 이어 붙여 다시 만들고, A 결과와 나란히 비교합니다. 구도가 흔들리면 'keep the same framing'을 덧붙입니다.</li><li>같은 대화에서 차이가 약하면 새 대화에서 처음부터 만들어 보세요. 결과는 매번 다릅니다.</li></ol>
<p class="hint" style="margin-top:8px">참고 그림 내려받기: {refs}</p></div>"""
    for i, t in enumerate(tasks, 1):
        A = PROMPTS[t["key"]][4]
        att = ATTACH_OF[CONV_OF[t["key"]]]
        ar = "16/9" if "16:9" in A.split("\n")[0] else "2/3"
        alt = PROMPTS[t["img"]][3]
        chk = "".join(f'<li>{E(c)}' + (f' <a href="{l}">원리 보기</a>' if l else "") + "</li>" for c, l in t["check"])
        k = t["b_imgs"][0]
        bbox = f'<div class="promptbox"><b>{E(t["b_title"])}</b><pre>{E(t["b_text"])}</pre><button type="button" class="btn copy">복사하기</button></div>'
        bpart = f'<div class="pair">{bbox}<div>{art(k, "비교 결과 — " + t["b_title"], ar, "B 결과")}</div></div>'
        res = f'<p style="background:#fff7ec;border-left:4px solid var(--orange);padding:8px 12px;border-radius:6px">{E(t["res"])}</p>' if t.get("res") else ""
        tip = f'<p class="hint">{E(t["tip"])}</p>' if t.get("tip") else ""
        out += f"""<div class="failcard" id="make{i}"><h3>실습 {i} · {E(t['title'])}</h3><p>{E(t['goal'])}</p>
<div class="pair"><div class="promptbox"><b>A — 이 페이지 그림을 만드는 프롬프트</b><p class="hint">첨부: {E(att)}</p><pre>{E(A)}</pre><button type="button" class="btn copy">복사하기</button></div>
<div>{art(t['img'], alt, ar, "A 결과 — Genspark로 만든 그림")}</div></div>
{bpart}<h4>결과에서 확인할 것</h4><ol>{chk}</ol>{res}{tip}</div>"""
    return out + "</div></section>"

def build_part(P):
    t = f"{SERIES} {P['no']}부 — {P['title']}"
    s = head(t, P["desc"], P["og"], P["file"])
    navl = [(f"#{x['id']}", f"{k+1}단계") for k, x in enumerate(P["steps"])]
    if P.get("fails"): navl += [("#fails", "실패 8종")]
    navl += [("#make", "직접 만들기"), ("#judge", "평가"), ("#sum", "정리"), (P["next"][0], "다음 →")]
    s += nav(navl)
    s += cover(P["cover_key"], P["cover_cap"], P["cover_cast"])
    s += f"""<header class="hero"><div class="wrap"><span class="kicker">{E(P['kicker'])}</span><h1>{E(P['title'])}</h1><p class="lead">{E(P['lead'])}</p>
<p class="byline">글 · 안상선 ((주)M-Robo 대표) · <a href="{AUTHOR_URL}">저자 소개</a> · {DATE} · {VER}</p></div></header>
<section><div class="wrap">{three(*P['three'], ABBR)}</div></section>
<section><div class="wrap"><h2>오늘의 과제</h2>{talk(P['intro'])}{flow_strip(P['no'])}</div></section>
"""
    for k, st in enumerate(P["steps"]):
        s += step(P, k + 1, st)
    if P.get("fails"):
        s += '<section class="room" id="fails"><div class="wrap"><div class="roomno">6부 · 2단계</div><h2>얼굴 그림 실패 8종 진단</h2><p class="muted">그림마다 증상을 보고 처음 걸리는 점검 항목을 고른 뒤, 연결된 원리와 고치는 프롬프트 조각을 확인합니다.</p>'
        s += "".join(failcard(f) for f in P["fails"])
        d = P["drift"]
        s += f'<div class="failcard" id="drift"><h3>{E(d["title"])}</h3>' + "".join(f"<p>{E(x)}</p>" for x in d["body"]) + '<p><span class="chip">연결된 원리</span><a href="05_ai_face.html#s1">5부 1단계 얼굴 문장</a> · <a href="01_front_female.html#s2">1부 2단계 볼 높이</a></p></div></div></section>'
    s += make_section(P)
    s += judge(P["judge"]) + summary(P) + outro(P)
    s += kg_block(P["file"].replace(".html", ""), [P["file"]])
    s += footer()
    open(os.path.join(ROOT, P["file"]), "w").write(s)

FLOW = [
 (1, "정면 얼굴", "눈부터 그리면 그릴 때마다 얼굴이 달라진다", "원·기준선·눈 상자·부위 다듬기"),
 (2, "정면 남성 얼굴", "여성 얼굴을 키우거나 눈만 바꾸면 남성으로 보이지 않는다", "장기말·세 간격·남녀 위치·목과 어깨"),
 (3, "옆얼굴", "정면 기준만으로는 귀·코·턱·목이 정해지지 않는다", "기본 도형·귀 위치·굴곡·목 기울기"),
 (4, "변형과 점검", "기본 얼굴을 바꿀 때마다 새로 그리면 다른 사람이 된다", "눈꺼풀·안경·자세·옆얼굴 점검"),
 (5, "AI로 얼굴 고정하기", "AI는 기준선을 모른다. 문장과 영역으로 알려 줘야 한다", "얼굴 문장·각도별 기준선·가림 영역·화풍"),
 (6, "실패 사례 실험실", "문장을 써도 얼굴은 틀릴 수 있다", "진단 순서와 고치는 조각, 나이 쏠림"),
 (7, "실전 연습장", "배운 것을 한 화면에서 함께 다뤄 본다", "비율 작업대·남녀 바꾸기·문장 공방·진단"),
]
def flow_strip(cur=None, pre=""):
    files = {P["no"]: P["file"] for P in PARTS}
    files[7] = "practice/index.html"
    cells = []
    for n, t, _, _ in FLOW:
        mark = ' style="border-color:var(--orange);background:var(--orange-soft)"' if n == cur else ""
        cells.append(f'<a href="{pre}{files[n]}"{mark}><b>{n}부</b>{E(t)}</a>')
    return '<div class="flowgrid" style="grid-template-columns:repeat(auto-fit,minmax(130px,1fr));margin-top:16px">' + "".join(cells) + "</div>"

def build_index():
    t = f"{SERIES} — 같은 기준선, 다른 얼굴"
    d = "원과 기준선에서 시작해 정면·옆얼굴의 남녀 차이를 실험으로 익히고, 그 기준선을 AI 얼굴 문장·가림 영역으로 옮겨 봅니다. 얼굴 그림 실패 8종 진단까지."
    s = head(t, d, "og_index.jpg", "index.html")
    s += nav([("#howto", "읽는 법"), ("#parts", "편 목록"), ("#map", "전체 흐름"), ("#cast", "등장인물"), ("#source", "원리와 출처")])
    s += cover("cover_index", "연구실 거울 벽 · 화가 둘, 모델 넷, 평가단 셋", [("fruitfly", "e09"), ("haru", "e01"), ("sia", "e13"), ("moa", "e19"), ("doctor", "e16"), ("jupanbot", "e16")])
    s += f"""<header class="hero"><div class="wrap"><span class="kicker">연구실 특별편 · 그리기와 렌더링 · 세 번째 편</span>
<h1>구조 먼저 그리기 연구실 03<br>얼굴 편 — 같은 기준선, 다른 얼굴</h1>
<p class="lead">옷장 편에서 옷의 주름을 다뤘다면, 이번에는 얼굴입니다. <b>원 하나와 가로선 몇 줄</b>로 정면 얼굴을 세우고, 남성과 여성의 윤곽·눈·귀·목이 어떻게 다른지 실험으로 봅니다. 마지막에는 그 기준선을 <b>AI에게 말과 영역으로 알려 주는 법</b>까지 갑니다.</p>
<p class="byline">글 · 안상선 ((주)M-Robo 대표) · <a href="{AUTHOR_URL}">저자 소개</a> · {DATE} · {VER}</p></div></header>
<section><div class="wrap">{three("정면·옆얼굴을 원과 기준선에서 시작해 그리는 순서와, 남녀 얼굴의 윤곽·눈·부위 높이·귀·목의 차이를 실험으로 익히고, AI 얼굴 문장과 가림 영역으로 옮깁니다.", "얼굴은 몇 픽셀 차이로 다른 사람이 됩니다. 기준선이 없으면 그릴 때마다, AI에게 요청할 때마다 얼굴이 흔들립니다.", "캐릭터 얼굴 설정, 남녀 캐릭터 함께 설계하기, 표정 시트, AI 얼굴 그림의 검수와 부분 수정에 씁니다.", ABBR)}</div></section>
<section id="howto"><div class="wrap"><h2>읽는 순서와 시간</h2><div class="box"><ul style="margin:0;padding-left:20px">
<li><b>처음부터 차례로</b>(권장): 부마다 실험을 눌러 보며 20~30분, 전체 3시간 안팎입니다.</li>
<li><b>앞 편을 안 봤다면</b>: 바로 읽어도 됩니다. 낱말은 다시 설명합니다. 빛·그림자 기초는 <a href="{FIRST_SITE}">구조 먼저 보는 캐릭터 그리기 연구실</a>, 옷은 <a href="{PREV_SITE}">01 옷장 편</a>에 있습니다.</li>
<li><b>손 그림 원리만</b>: 1~4부. <b>AI가 급하다면</b>: 5부 → 6부 → 7부, 막히는 낱말은 각 단계의 링크로 되짚어 보세요.</li>
<li>각 부 끝의 <b>평가단 채점</b>은 이야기 속 예시 점수입니다. 확인 퀴즈와 실전 연습장 미션으로 스스로 점검하세요.</li></ul></div></div></section>
<section id="parts"><div class="wrap"><h2>편 목록</h2>
<p class="muted">모델은 모아(1부)·박사(2부)·시아와 박사(3부)·하루(4부)·모두(5부), 화가는 주판봇과 초파리, 평가단은 X1·X2·X3, 해설은 박사입니다. 부마다 두 화가가 겨루고 평가단이 점수를 매깁니다.</p>
<div class="cards">
<a class="card" href="01_front_female.html">{face("moa","e01")}<span class="n">1부 · 모델 모아</span><h3>정면 얼굴</h3><p>원과 기준선, 원 양옆 깎기, 눈 상자와 간격, 부위 다듬기.</p></a>
<a class="card" href="02_front_male.html">{face("doctor","e01")}<span class="n">2부 · 모델 박사</span><h3>정면 남성 얼굴</h3><p>원 + 장기말, 세 간격, 남녀 부위 위치, 목과 어깨.</p></a>
<a class="card" href="03_profile.html">{face("sia","e13")}<span class="n">3부 · 모델 시아 · 손님 박사</span><h3>옆얼굴</h3><p>기본 도형과 옆 눈, 귀 위치, 코~턱 굴곡, 목 기울기.</p></a>
<a class="card" href="04_variation.html">{face("haru","e19")}<span class="n">4부 · 모델 하루 · 손님 박사</span><h3>변형과 점검</h3><p>반쯤 감은 눈, 안경, 정면 자세, 옆얼굴 점검.</p></a>
<a class="card" href="05_ai_face.html">{face("moa","e19")}<span class="n">5부 · 모델 모두</span><h3>AI로 얼굴 고정하기</h3><p>얼굴 문장, 각도별 기준선, 가림 영역, 화풍별 남길 것.</p></a>
<a class="card" href="06_failure_lab.html">{face("jupanbot","e20")}<span class="n">6부 · 의도적 실패 8종</span><h3>실패 사례 실험실</h3><p>증상 → 처음 걸린 곳 → 원리 → 고치는 조각. 나이 쏠림 막기.</p></a>
<a class="card" href="practice/index.html">{face("x2","e16")}<span class="n">7부 · 마지막 장</span><h3>실전 연습장</h3><p>비율 작업대·남녀 바꾸기판·얼굴 문장 공방·진단 데스크.</p></a>
</div></div></section>
<section id="map"><div class="wrap"><h2>전체 흐름 — 1부부터 7부까지 이어지는 순서</h2>{flow_strip()}
<div class="tbl" style="margin-top:16px"><table><thead><tr><th>부</th><th>제목</th><th>이 부를 배우는 까닭</th><th>핵심</th></tr></thead><tbody>
{''.join(f"<tr><td>{n}</td><td>{E(t)}</td><td>{E(a)}</td><td>{E(b)}</td></tr>" for n, t, a, b in FLOW)}</tbody></table></div>
<h3 style="margin-top:22px">한눈에 보는 얼굴 기준값 (머리 높이 24 기준, 예시값)</h3>
<div class="tbl"><table><thead><tr><th>항목</th><th>여성(애니풍)</th><th>남성(애니풍)</th><th>배우는 곳</th></tr></thead><tbody>
<tr><td>윤곽</td><td>원 양옆을 깎기</td><td>원 + 거꾸로 붙인 장기말</td><td><a href="01_front_female.html#s2">1부 2단계</a> · <a href="02_front_male.html#s1">2부 1단계</a></td></tr>
<tr><td>위 눈꺼풀</td><td>12 (1/2)</td><td>12 (1/2)</td><td><a href="01_front_female.html#s1">1부 1단계</a></td></tr>
<tr><td>코 밑(턱에서)</td><td>6 (1/4)</td><td>약 6.5 (조금 높게)</td><td><a href="02_front_male.html#s3">2부 3단계</a></td></tr>
<tr><td>입(턱에서)</td><td>3 (코~턱 가운데)</td><td>약 4.3 (코 쪽 1/3)</td><td><a href="02_front_male.html#s3">2부 3단계</a></td></tr>
<tr><td>눈 세로:가로 · 눈 사이</td><td>1:1 · 눈 1개보다 조금 넓게</td><td>1:2 · 눈 1개</td><td><a href="01_front_female.html#s3">1부 3단계</a></td></tr>
<tr><td>옆얼굴 귀(이마~뒤통수)</td><td>55% 안팎</td><td>66% 안팎</td><td><a href="03_profile.html#s2">3부 2단계</a></td></tr>
<tr><td>목 너비(옆, 머리 너비 대비)</td><td>1/4</td><td>1/2</td><td><a href="03_profile.html#s4">3부 4단계</a></td></tr>
</tbody></table></div>
<p class="hint">이 편은 정면과 옆얼굴이 중심입니다. 비스듬한 얼굴(3/4)을 처음부터 그리는 방법, 올려다보기·내려다보기, 표정별 변화는 자세히 다루지 않습니다(5부에서는 비스듬한 얼굴을 기준선 맞추기 용도로만 씁니다).</p>
<p class="muted" style="margin-top:12px">같은 시리즈: <a href="{PREV_SITE}">01 옷장 편(옷 주름·그림자)</a> · <a href="{FIRST_SITE}">구조 먼저 보는 캐릭터 그리기 연구실(구조·빛·확산 모델)</a> · <a href="{RENDER}">AI 렌더링 연구실</a></p></div></section>
<section id="cast"><div class="wrap"><h2>등장인물</h2><div class="cast-grid">{''.join(f'<div class="who">{face(k, "e01" if k in ("haru","sia","moa") else "e13")}<b>{E(CH[k][0])}</b><span>{E(CH[k][1])}</span></div>' for k in ["doctor","haru","sia","moa","jupanbot","fruitfly","x1","x2","x3"])}</div>
<p class="hint" style="margin-top:10px">하루·시아·모아는 20대 성인 연구원, 박사는 30대 성인 남성입니다. 얼굴 비율 실험에서도 모두 성인 얼굴을 기준으로 합니다.</p></div></section>
<section id="source"><div class="wrap"><h2>원리와 출처</h2>
<p>1~4부의 그리기 원리(원과 기준선, 원 양옆 깎기, 원 + 장기말, 남녀 부위 위치, 옆얼굴의 귀·목, 반쯤 감은 눈과 안경, 옆얼굴 점검)는 일반적인 얼굴 데생 원리이며, YANAMi의 작법서 『男女の顔の描き分け 角度別・年齢別・表情別のキャラデッサン』(ホビージャパン, 2018) 1장 「基本の顔を描き分けよう」를 참고해 정리했습니다. 책의 그림·문장·도식·구성 순서는 옮기지 않았고, 연구실 캐릭터와 직접 움직이는 실험으로 새로 구성했습니다. 책에서 어린 인물을 예로 든 부분은 모두 성인 캐릭터로 바꿔 다뤘습니다.</p>
<p>원에서 머리를 짓는 방법은 Loomis(1956), 세 간격 같은 비율 기준이 실제 사람에게는 근사치라는 점은 Farkas 외(1985), 가림 영역 다시 그리기는 확산 모델 연구를 바탕으로 쉽게 풀었습니다(아래 출처). 페이지의 그림(표지 8장은 픽셀아트, 본문은 애니풍·반실사·실사풍)은 Genspark로 만들며, 그림이 오기 전에는 '그림 준비 중' 자리로 둡니다. 실험 패널은 모두 페이지 안에서 직접 계산해 그립니다.</p></div></section>
"""
    s += kg_block("index", [P["file"] for P in PARTS] + ["practice/index.html"])
    s += footer()
    open(os.path.join(ROOT, "index.html"), "w").write(s)

def build_practice():
    pre = "../"
    t = f"{SERIES} 7부 — 실전 연습장"
    d = "비율 작업대(기준선), 남녀 바꾸기판(윤곽·눈·귀·목), 얼굴 문장 공방(AI 문장), 진단 데스크(실패 맞히기) 네 곳을 직접 운영하며 1~6부를 함께 연습합니다."
    s = head(t, d, "og_07.jpg", "practice/index.html", pre)
    s += nav([("#bench", "비율 작업대"), ("#swap", "남녀 바꾸기"), ("#workshop", "공방"), ("#desk", "진단 데스크"), ("#wrap", "마무리")], pre)
    s += cover("cover_07", "연구실 조종 책상 · 실전 연습장", [("haru", "e19"), ("doctor", "e16"), ("fruitfly", "e09"), ("jupanbot", "e16")], pre)
    s += f"""<header class="hero"><div class="wrap"><span class="kicker">7부 · 마지막 장</span><h1>실전 연습장</h1>
<p class="lead">네 곳의 작업대를 직접 운영합니다. <span style="color:var(--green)">초록 조작판</span>은 주어진 환경, <span style="color:var(--blue)">파랑 조작판</span>은 내 결정입니다. 미션은 직접 조작해야 판정됩니다.</p>
<p class="byline">글 · 안상선 ((주)M-Robo 대표) · <a href="{AUTHOR_URL}">저자 소개</a> · {DATE} · {VER}</p></div></header>
<section id="practice"><div class="wrap">
<div class="tabs" role="tablist"><button type="button" data-t="bench">비율 작업대</button><button type="button" data-t="swap">남녀 바꾸기판</button><button type="button" data-t="workshop">얼굴 문장 공방</button><button type="button" data-t="desk">진단 데스크</button></div>
"""
    def sc(id_, title, situ, env, me, missions, back, extra_g1=""):
        ms = "".join(f"<li>{E(m)}</li>" for m in missions)
        bk = " · ".join(f'<a href="{pre}{h}">{E(t)}</a>' for h, t in back)
        return f"""<div class="scene" id="{id_}"><h2>{E(title)}</h2><div class="box"><b>상황</b> — {E(situ)}</div>
<div class="panel"><div class="ph"><b>조작판</b><small>초록 = 환경 · 파랑 = 내 결정</small></div>
<div class="ctrl ctl-env">{env}</div><div class="ctrl ctl-me">{me}</div>
<div class="board" aria-live="polite"></div>
<div class="pair"><div class="g1">{extra_g1}</div><div class="g2"></div></div>
<div class="talk"></div>
<h4>미션</h4><ol class="missions">{ms}</ol></div>
<p class="muted">배운 곳 다시 보기: {bk}</p></div>
"""
    s += sc("bench", "비율 작업대 — 기준선 맞추기", "그릴 얼굴(여성·남성)은 주어집니다. 위 눈꺼풀·코 밑·눈 사이·입 위치를 정해 기준에 맞춥니다.",
            '<label>그릴 얼굴 <select name="sex"><option value="f" selected>여성 정면</option><option value="m">남성 정면</option></select></label>',
            '<label>위 눈꺼풀(%) <input type="range" name="eye" min="35" max="65" step="1" value="42"></label><label>코 밑(턱에서 %) <input type="range" name="nose" min="15" max="35" step="1" value="31"></label><label>눈 사이(눈 너비 %) <input type="range" name="gap" min="60" max="170" step="5" value="80"></label><label>입(코 밑~턱 %) <input type="range" name="mouth" min="20" max="70" step="1" value="60"></label>',
            ["여성 정면: 위 눈꺼풀 12/24, 코 밑 6/24 맞추기", "남성 정면으로 바꿔 눈꺼풀·코 밑·입(코 쪽 1/3)까지 맞추기", "눈꺼풀을 맞춘 채 눈 사이를 기준(여 1.1·남 1)에 맞추기"],
            [("01_front_female.html#s1", "1부 1단계 기준선"), ("01_front_female.html#s3", "1부 3단계 눈 상자"), ("02_front_male.html#s3", "2부 3단계 남녀 위치")])
    s += sc("swap", "남녀 바꾸기판 — 신호 네 개 맞추기", "목표 얼굴(정면·옆, 여성·남성)이 주어집니다. 윤곽·눈 비율·귀 위치·목 굵기 네 신호를 골라 목표에 맞춥니다.",
            '<label>목표 <select name="target"><option value="ms" selected>남성 정면</option><option value="fs">여성 정면</option><option value="fp">여성 옆얼굴</option><option value="mp">남성 옆얼굴</option></select></label>',
            '<label>윤곽 <select name="shape"><option value="circle" selected>원에서 깎기</option><option value="shogi">원 + 장기말</option></select></label><label>눈 세로:가로 <select name="eye"><option value="1" selected>1:1</option><option value="2">1:2</option></select></label><label>귀 <select name="ear"><option value="low" selected>눈 가운데~코 밑(정면)</option><option value="high">눈꺼풀~코끝(정면)</option><option value="mid">1/2보다 조금 뒤(옆)</option><option value="back">1/2보다 꽤 뒤(옆)</option></select></label><label>목 <select name="neck"><option value="thin" selected>가늘게</option><option value="thick">굵게</option></select></label>',
            ["남성 정면의 신호 네 개 모두 맞추기", "여성 옆얼굴의 신호 네 개 모두 맞추기", "목표 네 가지를 모두 한 번씩 완성하기"],
            [("02_front_male.html#s3", "2부 3단계 남녀 위치"), ("03_profile.html#s2", "3부 2단계 귀 위치"), ("03_profile.html#s4", "3부 4단계 목")])
    s += sc("workshop", "얼굴 문장 공방 — 요청서 조립", "요청 상황에 맞춰 얼굴 문장을 조립합니다. 점검표 6조각을 채우고, 상황에 꼭 필요한 조각을 넣습니다.",
            '<label>요청 상황 <select name="job"><option value="sheet">기준 얼굴(눈·부위 높이 중요)</option><option value="turn">세 각도 설정화(각도·부위 높이 중요)</option><option value="goods">굿즈 그림(나이·윤곽 중요)</option></select></label>',
            '<div class="ow" style="width:100%"></div>',
            ["점검표 6 / 6을 충돌 경고 없이 채우기", "남성 + 각진 턱 + 가는 눈 + 옆얼굴로 남성 옆얼굴 문장 만들기", "여성 + 둥근 볼 + 큰 눈을 고르되 성인 나이를 적어 쏠림 경고 없애기"],
            [("05_ai_face.html#s1", "5부 1단계 얼굴 문장"), ("06_failure_lab.html#drift", "6부 나이 쏠림")],
            '<div class="promptbox"><b>조립된 얼굴 문장</b><pre aria-live="polite"></pre><button type="button" class="btn copy">복사하기</button></div>')
    s += sc("desk", "진단 데스크 — 원인 맞히기", "얼굴 그림 실패의 증상이 하나씩 들어옵니다. 원인을 고르세요. 순서: 큰 틀 → 높이 기준선 → 눈 상자 → 코·입·귀 → 목·어깨.",
            '<span class="hint">환경: 증상은 무작위로 들어옵니다.</span>',
            '<div style="width:100%"><p class="sym" style="font-weight:600"></p><div class="opts deskopts"></div></div>',
            ["3개 연속 정답", "8종 원인을 모두 한 번 이상 맞히기", "틀리지 않고 5개 맞히기"],
            [("06_failure_lab.html#s1", "6부 진단 순서"), ("06_failure_lab.html#fails", "6부 실패 8종")])
    s += f"""</div></section>
<section id="wrap"><div class="wrap"><h2>마무리 — 네 작업대를 하나로 묶으면</h2>
<div class="box"><p>비율 작업대에서 맞춘 기준선은 공방의 '부위 높이' 조각이 되고, 남녀 바꾸기판의 네 신호는 '성별·윤곽·눈' 조각이 됩니다. 진단 데스크에서 틀린 원인은 대부분 앞의 두 곳 중 하나가 빠진 경우입니다. 얼굴 그림은 결국 <b>원 하나와 가로선 몇 줄 위에, 남녀 신호를 골라 얹는 일</b>입니다.</p>
<p><b>실제 그림으로 이어 가기</b> — 얼굴 문장 공방에서 조립한 문장을 복사해 그림 생성 AI에 넣어 보세요. 결과는 각 부의 '프롬프트로 직접 만들어 보기' 확인표로 점검합니다: <a href="{pre}01_front_female.html#make">1부</a> · <a href="{pre}02_front_male.html#make">2부</a> · <a href="{pre}03_profile.html#make">3부</a> · <a href="{pre}04_variation.html#make">4부</a> · <a href="{pre}05_ai_face.html#make">5부</a> · <a href="{pre}06_failure_lab.html#make">6부</a></p>
<p class="hint">주의할 점: 이 연습장의 기준값(1/2·1/4, 눈 사이 1.1·1, 귀 위치)은 애니풍 기본 얼굴의 예시입니다. 판정 범위는 원리를 보이기 위해 정한 값이며, 실제 사람과 화풍마다 다릅니다.</p></div>
<div class="next"><a href="{pre}06_failure_lab.html">← 6부 실패 사례 실험실</a><a href="{pre}index.html">목차로</a></div></div></section>
"""
    s += kg_block("practice_index", ["practice/index.html"])
    s += footer(pre)
    open(os.path.join(ROOT, "practice", "index.html"), "w").write(s)

if __name__ == "__main__":
    JS = ["js_base.js", "js_practice_util.js", "js_face.js", "js_tail.js"]
    os.makedirs(os.path.join(ROOT, "practice"), exist_ok=True)
    open(os.path.join(ROOT, "assets", "panels.js"), "w").write("".join(open(os.path.join(ROOT, "build", f)).read() for f in JS))
    build_index()
    for P in PARTS:
        build_part(P)
    build_practice()
    print("built", len(PARTS) + 2, "pages")
