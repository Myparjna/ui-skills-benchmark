#!/usr/bin/env python
"""展厅现场精简版截图：4 个关键状态"""
import asyncio
import os
from playwright.async_api import async_playwright

URL = "http://127.0.0.1:8080/"
OUT = r"C:\Users\mypra\Desktop\VibeCoding指南\skills测评项目\01-前端设计技能测评\ScreenShot\展厅现场"
os.makedirs(OUT, exist_ok=True)


async def shot(page, name):
    path = os.path.join(OUT, f"{name}.png")
    await page.screenshot(path=path, full_page=False)
    print(f"  [SHOT] {name}.png ({os.path.getsize(path)//1024} KB)")


async def click(page, sel, desc):
    try:
        await page.click(sel, timeout=3000)
        await page.wait_for_timeout(700)
        return True
    except Exception as e:
        print(f"  [WARN] click '{desc}': {e}")
        return False


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        ctx = await browser.new_context(viewport={"width": 1440, "height": 900}, device_scale_factor=2)
        page = await ctx.new_page()

        await page.goto(URL, wait_until="domcontentloaded", timeout=15000)
        await page.evaluate("() => localStorage.clear()")
        await page.reload(wait_until="domcontentloaded")
        await page.wait_for_timeout(1500)

        # 1. 默认 all / airline
        await shot(page, "1_默认_全部模型_官网")

        # 2. 切到 M3
        await click(page, 'button[data-model="m3"]', "M3")
        await shot(page, "2_M3筛选_官网_14张")

        # 3. M3 + 全部产品
        await click(page, 'button:has-text("全部")', "全部产品")
        await shot(page, "3_M3筛选_全部产品_42张")

        # 4. 全部模型 + 全部产品（看 7 模型对比）
        await click(page, 'button[data-model="all"]', "all model")
        await shot(page, "4_全部模型_全部产品_262张")

        # 5. M3 + 后台
        await click(page, 'button[data-model="m3"]', "M3")
        await click(page, 'button:has-text("后台")', "后台")
        await shot(page, "5_M3筛选_后台_fleet_ops")

        # 6. M3 + 后台 + impeccable chip
        await click(page, 'button:has-text("impeccable")', "impeccable")
        await shot(page, "6_M3_后台_impeccable_单卡")

        # 7. M3 + 小程序
        await click(page, 'button[data-model="m3"]', "M3")
        await click(page, 'button:has-text("小程序")', "小程序")
        await shot(page, "7_M3筛选_小程序_ev_charging")

        await browser.close()
        print("\n=== Done ===")


if __name__ == "__main__":
    asyncio.run(main())
