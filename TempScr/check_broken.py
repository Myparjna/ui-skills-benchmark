# -*- coding: utf-8 -*-
"""检查线上展厅 deepseek 缩略图实际加载状态（img.complete + naturalWidth）"""
import asyncio
from playwright.async_api import async_playwright

CDP = "http://127.0.0.1:9557"
URL = "https://frontend-design-skills-showcase.pages.dev/"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp(CDP)
        ctx = browser.contexts[0] if browser.contexts else await browser.new_context()
        page = await ctx.new_page()
        await page.set_viewport_size({"width": 1600, "height": 900})

        # 收集 4xx 响应
        bad_resps = []
        async def on_resp(resp):
            if resp.status >= 400:
                bad_resps.append(f"{resp.status} {resp.url}")
        page.on("response", on_resp)

        await page.goto(URL, wait_until="networkidle", timeout=40000)
        await page.wait_for_timeout(1000)

        await page.click('button[data-model="deepseek"]')
        await page.wait_for_timeout(1500)

        # 检查所有缩略图 img 的加载状态
        result = await page.evaluate("""
            () => {
                const imgs = document.querySelectorAll('#gallery img');
                const out = [];
                imgs.forEach(img => {
                    out.push({
                        src: img.src.split('/').pop(),
                        complete: img.complete,
                        naturalWidth: img.naturalWidth,
                        naturalHeight: img.naturalHeight
                    });
                });
                return out;
            }
        """)
        broken = [r for r in result if not r['complete'] or r['naturalWidth'] == 0]
        print(f"缩略图总数: {len(result)}, 裂图: {len(broken)}")
        for b in broken[:20]:
            print("  BROKEN:", b['src'], "complete=", b['complete'], "nw=", b['naturalWidth'])

        print("\n4xx 响应数:", len(bad_resps))
        for r in bad_resps[:20]:
            print("  ", r[:150])

        await page.screenshot(path=r"C:\Users\mypra\Desktop\VibeCoding指南\skills测评项目\01-前端设计技能测评\ScreenShot\online-deepseek-thumbs.png")
        await page.close()
        await browser.close()

asyncio.run(main())
