#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
展厅现场截图：4 个状态
1. 默认 all/airline 视图
2. M3 筛选 + airline tab
3. M3 筛选 + all products tab (42 张)
4. 展厅所有模型（all 模式 + all products）
5. 单页 M3 卡片详情
"""
import asyncio
import os
from playwright.async_api import async_playwright

URL = "http://127.0.0.1:8080/"
OUT = r"C:\Users\mypra\Desktop\VibeCoding指南\skills测评项目\01-前端设计技能测评\ScreenShot\展厅现场"
os.makedirs(OUT, exist_ok=True)


async def click_and_settle(page, selector, desc):
    """点击元素 + 等待动画"""
    try:
        await page.click(selector, timeout=3000)
        await page.wait_for_timeout(500)
        return True
    except Exception as e:
        print(f"  [WARN] click '{desc}' failed: {e}")
        return False


async def shot(page, name):
    path = os.path.join(OUT, f"{name}.png")
    await page.screenshot(path=path, full_page=False)
    print(f"  [SHOT] {name}.png ({os.path.getsize(path)} bytes)")


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        ctx = await browser.new_context(viewport={"width": 1440, "height": 900}, device_scale_factor=2)
        page = await ctx.new_page()
        page.on("pageerror", lambda e: print(f"  [PAGEERROR] {e}"))
        page.on("console", lambda m: print(f"  [CONSOLE.{m.type}] {m.text}") if m.type == "error" else None)

        # 0. 加载首页
        await page.goto(URL, wait_until="domcontentloaded", timeout=15000)
        await page.wait_for_timeout(1500)
        # 清 localStorage 保证从默认状态开始
        await page.evaluate("() => localStorage.clear()")
        await page.reload(wait_until="domcontentloaded")
        await page.wait_for_timeout(1500)
        await shot(page, "01_默认_all_airline")

        # 1. 切到 M3 筛选
        m3_btn = 'button[data-model="m3"]'
        if await page.locator(m3_btn).count() > 0:
            await click_and_settle(page, m3_btn, "M3 filter")
            await shot(page, "02_M3筛选_airline")
        else:
            print("  [WARN] M3 button not found!")

        # 2. M3 + all products tab
        all_products_tab = 'button:has-text("全部产品")'
        if await page.locator(all_products_tab).count() > 0:
            await click_and_settle(page, all_products_tab, "all products tab")
            await shot(page, "03_M3筛选_全部产品_42张")

        # 3. all 模型 + all products
        await click_and_settle(page, 'button[data-model="all"]', "all model")
        await click_and_settle(page, all_products_tab, "all products tab (stays)")
        await shot(page, "04_全部模型_全部产品")

        # 4. 切回 M3 + 点一张卡片看 iframe
        await click_and_settle(page, m3_btn, "M3 filter again")
        await page.wait_for_timeout(500)
        # 找第一张 card 点击
        first_card = ".card, [data-card], a[href*='view.html']"
        cards = await page.locator(first_card).count()
        print(f"  M3 airline cards: {cards}")
        if cards > 0:
            try:
                await page.locator(first_card).first.click(timeout=2000)
                await page.wait_for_timeout(2500)
                await shot(page, "05_M3单页详情")
                # 回到首页
                await page.go_back(wait_until="domcontentloaded")
                await page.wait_for_timeout(1500)
            except Exception as e:
                print(f"  [WARN] card click failed: {e}")

        # 5. M3 + fleet_ops tab
        fleet_tab = 'button:has-text("车队管理")'
        if await page.locator(fleet_tab).count() > 0:
            await click_and_settle(page, fleet_tab, "fleet tab")
            await shot(page, "06_M3筛选_车队管理_fleet_ops")

        # 6. 切到 fleet_ops 下的 impeccable skill chip
        chip = 'button:has-text("impeccable")'
        if await page.locator(chip).count() > 0:
            await click_and_settle(page, chip, "impeccable chip")
            await shot(page, "07_M3_fleet_impeccable单卡片")

        await browser.close()
        print("\n=== Done ===")


if __name__ == "__main__":
    asyncio.run(main())
