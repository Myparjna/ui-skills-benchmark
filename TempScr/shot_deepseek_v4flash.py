# -*- coding: utf-8 -*-
"""
DeepSeek V4 Flash 39 页全量截图验证
- 连接独立 CDP 端口 9555（headless Chrome）
- 桌面场景 1280x720；charging 场景 390x844 @2x（780x1688）
- 截图存 ScreenShot/deepseek-v4flash-20260806/
- 同时采集 console 错误
"""
import asyncio
import json
import os
import sys

from playwright.async_api import async_playwright

CDP = "http://127.0.0.1:9555"
ROOT = r"C:\Users\mypra\Desktop\VibeCoding指南\skills测评项目\01-前端设计技能测评"
PAGES_DIR = os.path.join(ROOT, "03-产出", "deepseek")
SHOT_DIR = os.path.join(ROOT, "ScreenShot", "deepseek-v4flash-20260806-rerun")

SKILLS = [
    "frontend-design", "web-design-guidelines", "ui-ux-pro-max",
    "frontend-design-pro", "design-taste-frontend", "stitch-design",
    "modern-frontend-design", "nuxt-ui", "shadcn", "impeccable",
    "modern-web-design", "superdesign", "sleek-design-mobile-apps",
]
SCENES = ["airline", "ev-charging", "bike-dashboard"]


async def main():
    os.makedirs(SHOT_DIR, exist_ok=True)
    results = []
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp(CDP)
        ctx = browser.contexts[0] if browser.contexts else await browser.new_context()
        for skill in SKILLS:
            for scene in SCENES:
                page = await ctx.new_page()
                fname = f"deepseek-{skill}-{scene}.html"
                src = os.path.join(PAGES_DIR, fname)
                url = "file:///" + src.replace("\\", "/")
                is_mobile = scene == "ev-charging"
                if is_mobile:
                    await page.set_viewport_size({"width": 390, "height": 844})
                else:
                    await page.set_viewport_size({"width": 1280, "height": 720})
                errors = []
                page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)
                page.on("pageerror", lambda exc: errors.append(f"PAGEERROR: {exc}"))
                try:
                    await page.goto(url, wait_until="networkidle", timeout=30000)
                    await page.wait_for_timeout(1200)
                    out = os.path.join(SHOT_DIR, fname.replace(".html", ".png"))
                    await page.screenshot(path=out, full_page=False)
                    size = os.path.getsize(out)
                    status = "OK" if size > 2000 and not errors else "CHECK"
                    results.append((status, fname, size, errors[:2]))
                    print(f"[{status}] {fname} {size}B {errors[:2]}")
                except Exception as e:
                    results.append(("FAIL", fname, 0, [str(e)[:120]]))
                    print(f"[FAIL] {fname}: {e}")
                finally:
                    await page.close()
        await browser.close()

    ok = sum(1 for r in results if r[0] == "OK")
    check = sum(1 for r in results if r[0] == "CHECK")
    fail = sum(1 for r in results if r[0] == "FAIL")
    print(f"\n完成: OK={ok} CHECK={check} FAIL={fail} / {len(results)}")
    for r in results:
        if r[0] != "OK":
            print("  ", r)


if __name__ == "__main__":
    asyncio.run(main())
