# -*- coding: utf-8 -*-
"""线上展厅 DeepSeek V4 Flash 部分截图验证（走系统 Chrome CDP 9555）"""
import asyncio, os
from playwright.async_api import async_playwright

CDP = "http://127.0.0.1:9555"
ROOT = r"C:\Users\mypra\Desktop\VibeCoding指南\skills测评项目\01-前端设计技能测评"
SHOT_DIR = os.path.join(ROOT, "ScreenShot")
URL = "https://frontend-design-skills-showcase.pages.dev/"

async def main():
    os.makedirs(SHOT_DIR, exist_ok=True)
    errors = []
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp(CDP)
        ctx = browser.contexts[0] if browser.contexts else await browser.new_context()
        page = await ctx.new_page()
        page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
        page.on("pageerror", lambda e: errors.append(f"PAGEERROR: {e}"))
        await page.set_viewport_size({"width": 1440, "height": 900})
        await page.goto(URL, wait_until="networkidle", timeout=60000)
        await page.wait_for_timeout(1500)
        # 点击 DeepSeek V4 Flash 模型按钮
        btn = page.locator("button", has_text="DeepSeek V4 Flash").first
        await btn.click()
        await page.wait_for_timeout(2000)
        await page.screenshot(path=os.path.join(SHOT_DIR, "online_deepseek_section.png"))
        # 桌面视口下滚动到 DeepSeek 卡片区域并截图
        await page.evaluate("window.scrollBy(0, 600)")
        await page.wait_for_timeout(800)
        await page.screenshot(path=os.path.join(SHOT_DIR, "online_deepseek_cards.png"))
        # 打开一个 DeepSeek 页面（frontend-design 官网场景）
        card = page.locator("a[href*='deepseek']").first
        if await card.count() > 0:
            href = await card.get_attribute("href")
            print("OPEN PAGE:", href)
            await page.goto(href, wait_until="networkidle", timeout=60000)
            await page.wait_for_timeout(1500)
            await page.screenshot(path=os.path.join(SHOT_DIR, "online_deepseek_page.png"))
        await browser.close()
    print("CONSOLE_ERRORS:", len(errors))
    for e in errors[:20]:
        print("  -", e)

asyncio.run(main())