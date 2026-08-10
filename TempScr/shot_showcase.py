# -*- coding: utf-8 -*-
import asyncio
import os
from playwright.async_api import async_playwright

CDP = "http://127.0.0.1:9555"
SHOT = r"C:\Users\mypra\Desktop\VibeCoding指南\skills测评项目\01-前端设计技能测评\ScreenShot\deepseek-v4flash-20260806-rerun\showcase_deepseek.png"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp(CDP)
        ctx = browser.contexts[0] if browser.contexts else await browser.new_context()
        page = await ctx.new_page()
        await page.set_viewport_size({"width": 1440, "height": 900})
        errors = []
        page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
        page.on("pageerror", lambda e: errors.append(f"PAGEERROR: {e}"))
        await page.goto("http://127.0.0.1:8899/index.html", wait_until="networkidle", timeout=30000)
        await page.wait_for_timeout(800)
        # 点击 DeepSeek 模型按钮
        await page.click('[data-model="deepseek"]')
        await page.wait_for_timeout(1500)
        await page.screenshot(path=SHOT, full_page=False)
        n = await page.locator('.card').count()
        print(f"DeepSeek 卡片数={n} errors={errors[:5]}")
        await page.close()
        await browser.close()

asyncio.run(main())