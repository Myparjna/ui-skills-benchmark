# -*- coding: utf-8 -*-
import asyncio
import os
from playwright.async_api import async_playwright

CDP = "http://127.0.0.1:9555"
ROOT = r"C:\Users\mypra\Desktop\VibeCoding指南\skills测评项目\01-前端设计技能测评"
PAGES = os.path.join(ROOT, "03-产出", "deepseek")
SHOT = os.path.join(ROOT, "ScreenShot", "deepseek-v4flash-20260806-rerun")

async def main():
    browser = await async_playwright().call_subclass if False else None
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp(CDP)
        ctx = browser.contexts[0] if browser.contexts else await browser.new_context()
        page = await ctx.new_page()
        await page.set_viewport_size({"width": 390, "height": 844})
        errors = []
        page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
        page.on("pageerror", lambda e: errors.append(f"PAGEERROR: {e}"))
        fname = "deepseek-web-design-guidelines-ev-charging.html"
        url = "file:///" + os.path.join(PAGES, fname).replace("\\", "/")
        await page.goto(url, wait_until="networkidle", timeout=30000)
        await page.wait_for_timeout(1200)
        out = os.path.join(SHOT, fname.replace(".html", ".png"))
        await page.screenshot(path=out, full_page=False)
        print(f"size={os.path.getsize(out)}B errors={errors[:3]}")
        await page.close()
        await browser.close()

asyncio.run(main())