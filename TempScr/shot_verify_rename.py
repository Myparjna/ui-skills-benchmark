# -*- coding: utf-8 -*-
"""线上验证 DeepSeek 模型名已改为 V4 Flash0731"""
import asyncio
from playwright.async_api import async_playwright

CDP = "http://127.0.0.1:9555"
URL = "https://frontend-design-skills-showcase.pages.dev/"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe")
        ctx = await browser.new_context()
        page = await ctx.new_page()
        await page.set_viewport_size({"width": 1440, "height": 900})
        await page.goto(URL, wait_until="networkidle", timeout=60000)
        await page.wait_for_timeout(1500)
        btn = page.locator("button[data-model='deepseek']").first
        print("BUTTON TEXT:", await btn.text_content())
        await btn.click()
        await page.wait_for_timeout(1500)
        # 检查卡片徽章文本
        badges = page.locator(".card-badge, [class*='badge']").all_text_contents() if False else []
        # 渲染后检查第一个 deepseek 卡片的模型标签
        txt = await page.locator("body").inner_text()
        print("HAS_V4_FLASH0731_ON_BODY:", "DeepSeek V4 Flash0731" in txt)
        print("HAS_OLD_NAME:", "DeepSeek V4 Flash\n" in txt and "0731" not in txt.split("DeepSeek V4 Flash")[-1][:5])
        await page.screenshot(path=r"c:\Users\mypra\Desktop\VibeCoding指南\skills测评项目\01-前端设计技能测评\ScreenShot\online_deepseek_renamed.png")
        await browser.close()

asyncio.run(main())