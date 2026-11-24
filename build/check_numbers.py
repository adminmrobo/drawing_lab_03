# -*- coding: utf-8 -*-
"""본문 '숫자로 한 번 해 보기'·대화·퀴즈 숫자와 평가 점수 검산. python3 build/check_numbers.py"""
import math, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from content_a import P1, P2, P3
from content_b import P4, P5, P6
ok = True
def chk(name, got, want, tol=0.01):
    global ok
    good = abs(got - want) <= tol
    ok &= good
    print(("OK " if good else "XX "), name, round(got, 4), "기대", want)
# 1부
chk("1-1 눈꺼풀", 24 / 2, 12); chk("1-1 코 밑", 24 / 4, 6); chk("1-1 머리선", 24 / 6, 4); chk("1-1 입(턱에서)", 6 / 2, 3)
chk("1-3 눈 사이", 4 * 1.1, 4.4); chk("1-3 가장자리", 4 * 0.4, 1.6); chk("1-3 합계", 4 + 4.4 + 4 + 3.2, 15.6)
chk("1-3 패널 가장자리 배수", (1.72 - 0.88 - 1.1 * 0.44) / 2 / 0.44, 0.40, 0.01)
# 2부
r = 1.0; H = r * (1 + 0.1 + 1.3 + 0.7); chk("2-1 길이÷폭", H / (2 * 0.97 * r), 1.6, 0.01)
chk("2-2 머리선", 26 * 0.17, 4.4, 0.03); chk("2-2 한 간격", (26 - 4.4) / 3, 7.2); chk("2-2 눈썹", 4.4 + 7.2, 11.6); chk("2-2 코 밑", 4.4 + 14.4, 18.8)
chk("2-3 남 코 밑(턱에서)", 24 * 0.27, 6.5, 0.03); chk("2-3 남 입(턱에서)", 24 * 0.27 * 2 / 3, 4.3, 0.03)
chk("2-4 어깨", 10 * 2.1, 21); chk("2-4 삼각 높이", 13 / 3, 4.3, 0.04); chk("2-4 가슴", 13 * 1.5, 19.5)
# 3부
chk("3-2 가운데", 20 * 0.5, 10); chk("3-2 여 귀", 20 * 0.55, 11); chk("3-2 남 귀", 20 * 0.66, 13.2)
chk("3-4 tan5", math.tan(math.radians(5)), 0.087, 0.001); chk("3-4 밀림", 10 * math.tan(math.radians(5)), 0.87, 0.005); chk("3-4 여 목", 20 / 4, 5); chk("3-4 남 목", 20 / 2, 10)
# 4부
chk("4-3 딱딱함", 100 - 6 * 6 - 10 * 2.5, 39)
# 5부
chk("5-3 전체", 512 * 768, 393216); chk("5-3 가림", 200 * 120, 24000); chk("5-3 비율", 24000 / 393216, 0.061, 0.0005)
for P in (P1, P2, P3, P4, P5, P6):
    J = P["judge"]; sa, sb = sum(J["a"][1]), sum(J["b"][1]); txt = J["result"][0][2]
    good = f"{sb} : 주판봇 {sa}" in txt; ok &= good
    print(("OK " if good else "XX "), P["no"], "부 평가", sb, ":", sa, txt[:22])
print("전체 통과" if ok else "검산 실패"); sys.exit(0 if ok else 1)
