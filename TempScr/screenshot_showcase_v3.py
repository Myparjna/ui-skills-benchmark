#!/usr/bin/env python
"""展厅现场截图 v3 — 等所有图片加载完再截（修复背景图空白 bug）"""
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


async def wait_fully_loaded(page, timeout=15000):
    """等网络空闲 + 所有图片加载完"""
    try:
        await page.wait_for_load_state("networkidle", timeout=timeout)
    except Exception as e:
        print(f"  [WARN] networkidle timeout: {e}")
    # 强制等所有 img.complete
    await page.evaluate("""
        () => Promise.all(
            Array.from(document.images).map(img =>
                img.complete && img.naturalWidth > 0
                    ? null
                    : new Promise(r => {
                        img.onload = img.onerror = r;
                        setTimeout(r, 8000);
                    })
            )
        )
    """)
    await page.wait_for_timeout(500)


async def click(page, sel, desc):
    try:
        await page.click(sel, timeout=3000)
        await page.wait_for_timeout(900)
        return True
    except Exception as e:
        print(f"  [WARN] click '{desc}': {e}")
        return False


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        ctx = await browser.new_context(viewport={"width": 1440, "height": 900}, device_scale_factor=2)
        page = await ctx.new_page()

        # 1. 默认视图（all 模型 / 官网）
        await page.goto(URL, timeout=30000)
        await page.evaluate("() => localStorage.clear()")
        await page.reload(timeout=30000)
        await wait_fully_loaded(page)
        await shot(page, "1_默认_全部模型_官网")

        # 2. M3 筛选 + 官网
        await click(page, 'button[data-model="m3"]', "M3")
        await wait_fully_loaded(page)
        await shot(page, "2_M3筛选_官网_14张")

        # 3. 全部模型 + 全部产品（看 7 模型跨产品对比）
        await click(page, 'button[data-model="all"]', "all model")
        await click(page, 'button:has-text("全部")', "全部产品")  # 产品 tab 里的"全部"
        await wait_fully_loaded(page)
        await shot(page, "3_全部模型_全部产品_262张")

        # 4. M3 + 后台（最有代表性的对比）
        await click(page, 'button[data-model="m3"]', "M3")
        await click(page, 'button:has-text("后台")', "后台")
        await wait_fully_loaded(page)
        await shot(page, "4_M3筛选_后台_fleet_ops")

        # 5. M3 + 小程序
        await click(page, 'button[data-model="m3"]', "M3")
        await click(page, 'button:has-text("小程序")', "小程序")
        await wait_fully_loaded(page)
        await shot(page, "5_M3筛选_小程序_ev_charging")

        # 6. M3 + 官网 + 单卡点击（看单页详情）
        await click(page, 'button[data-model="m3"]', "M3")
        await click(page, 'button:has-text("官网")', "官网")
        await wait_fully_loaded(page)
        # 点击第一张卡片打开单页预览
        first_card = await page.query_selector(".card, [data-card], a[href*='m3_']")
        if first_card:
            try:
                await first_card.click(timeout=3000)
                await page.wait_for_timeout(1500)
                await wait_fully_loaded(page)
                await shot(page, "6_M3_单页详情_打开状态")
                # 关闭单页（按 ESC）
                await page.keyboard.press("Escape")
                await page.wait_for_timeout(500)
            except Exception as e:
                print(f"  [WARN] open card: {e}")

        await browser.close()
        print("\n=== Done ===")


if __name__ == "__main__":
    asyncio.run(main())
