"""
Test the updated showcase index.html — verify M3 filter button works,
M3 cards render, page count updates.
"""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

ROOT = Path("C:/Users/mypra/Desktop/VibeCoding指南/skills测评项目/01-前端设计技能测评")
INDEX = ROOT / "05-报告" / "展厅" / "index.html"

CDP_URL = "http://127.0.0.1:9222"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp(CDP_URL)
        context = await browser.new_context(viewport={"width": 1440, "height": 900})
        page = await context.new_page()
        url = f"file:///{INDEX.as_posix()}"
        await page.goto(url, wait_until="domcontentloaded", timeout=20000)
        await page.wait_for_timeout(2000)

        # 1. Check model button exists
        m3_btn = await page.query_selector('button[data-model="m3"]')
        print(f"1. M3 button exists: {m3_btn is not None}")

        # 2. Check header text
        header = await page.text_content('p.text-\\[10px\\].text-\\[\\#666\\]')
        print(f"2. Header: {header}")

        # 3. Click M3 button
        if m3_btn:
            await m3_btn.click()
            await page.wait_for_timeout(1000)

        # 4. Count M3 cards visible
        cards = await page.query_selector_all('#gallery > div')
        print(f"3. M3 cards rendered (airline tab default): {len(cards)} (expect 14)")

        # 4b. Switch to "all products" tab
        all_tab = await page.query_selector('button[data-tab="all"]')
        if all_tab:
            await all_tab.click()
            await page.wait_for_timeout(1500)
        cards_all = await page.query_selector_all('#gallery > div')
        print(f"3b. M3 cards rendered (all products): {len(cards_all)} (expect 42)")

        # 5. Screenshot to verify visually
        await page.screenshot(path=str(ROOT / "TempScr" / "m3_filter_test.png"), full_page=False)
        print("4. Screenshot: TempScr/m3_filter_test.png")

        # 6. Switch to all + count total
        all_btn = await page.query_selector('button[data-model="all"]')
        if all_btn:
            await all_btn.click()
            await page.wait_for_timeout(1500)
            all_cards = await page.query_selector_all('#gallery > div')
            print(f"5. All-model cards rendered (all products): {len(all_cards)} (expect 264)")

        await context.close()
        await browser.close()

asyncio.run(main())
