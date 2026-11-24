# 실전 연습장 미션 판정 점검 (로컬 서버 8765번 필요). 직접 조작하기 전에는 미션이 판정되지 않아야 하고, 조작하면 판정돼야 한다.
import asyncio
from playwright.async_api import async_playwright
async def setr(page,sc,name,v):
    await page.evaluate("([sc,n,v])=>{const e=document.querySelector('#'+sc+' [name='+n+']');if(e.type==='checkbox'){e.checked=v;}else e.value=v;e.dispatchEvent(new Event('input',{bubbles:true}));e.dispatchEvent(new Event('change',{bubbles:true}));}",[sc,name,v])
async def done(page,sc): return await page.evaluate("sc=>[...document.querySelectorAll('#'+sc+' .missions li')].map(l=>l.classList.contains('done'))",sc)
async def main():
    ok=True
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
        page=await b.new_page();await page.route('**/fonts.g*/**',lambda r: r.abort())
        await page.goto("http://localhost:8765/practice/index.html#bench");await page.wait_for_timeout(800)
        r0=await done(page,'bench');print('bench before',r0);ok&=not any(r0)
        for n,v in [('eye',50),('nose',25),('gap',110)]: await setr(page,'bench',n,v)
        await setr(page,'bench','sex','m')
        for n,v in [('eye',50),('nose',27),('mouth',33),('gap',100)]: await setr(page,'bench',n,v)
        r=await done(page,'bench');print('bench after',r);ok&=all(r)
        await page.click('.tabs button[data-t=swap]')
        r0=await done(page,'swap');print('swap before',r0);ok&=not any(r0)
        for t,vals in [('ms',dict(shape='shogi',eye='2',ear='high',neck='thick')),('fs',dict(shape='circle',eye='1',ear='low',neck='thin')),('fp',dict(shape='circle',eye='1',ear='mid',neck='thin')),('mp',dict(shape='shogi',eye='2',ear='back',neck='thick'))]:
            await setr(page,'swap','target',t)
            for n,v in vals.items(): await setr(page,'swap',n,v)
        r=await done(page,'swap');print('swap after',r);ok&=all(r)
        await page.click('.tabs button[data-t=workshop]')
        r0=await done(page,'workshop');print('workshop before',r0);ok&=not any(r0)
        for n,v in [('sex','m'),('shape','angular'),('eyes','almond'),('parts','std'),('view','side'),('age','adult')]: await setr(page,'workshop',n,v)
        for n,v in [('sex','f'),('shape','round'),('eyes','big'),('parts','std'),('view','front'),('age','adult')]: await setr(page,'workshop',n,v)
        r=await done(page,'workshop');print('workshop after',r);ok&=all(r)
        await page.click('.tabs button[data-t=desk]')
        SYM=['가운데로 몰려','이마는 좁고','턱이 뾰족','뒤로 크게 부풀어','턱이 앞으로 튀어나와','꺾인 직선','테 선이 눈동자','입 주변이 앞으로']
        CA=['눈 사이 좁음','부위가 위로 몰림','장기말이 김','뒤통수 부풂','턱이 튀어나온 각도','목을 직선으로 이음','안경 테가 눈을 가림','입술 기복 과다']
        r0=await done(page,'desk');print('desk before',r0);ok&=not any(r0)
        for _ in range(60):
            sym=await page.text_content('#desk .sym');k=[i for i,s in enumerate(SYM) if s in sym][0]
            await page.click(f"#desk .deskopts button:text-is('{CA[k]}')");await page.wait_for_timeout(560)
        r=await done(page,'desk');print('desk after',r);ok&=all(r)
        await b.close()
    print('미션 점검 통과' if ok else '미션 점검 실패')
asyncio.run(main())
