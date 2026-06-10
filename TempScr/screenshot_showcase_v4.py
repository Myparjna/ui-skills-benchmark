#!/usr/bin/env python
"""展厅现场截图 v4 — 用真实 Chrome 通道 + 30s 等待（彻底修复背景图加载）"""
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


async def wait_fully_loaded(page, timeout_ms=30000):
    """等网络空闲 + 所有图片真的加载完成（含 background-image）"""
    # 1) 等 networkidle
    try:
        await page.wait_for_load_state("networkidle", timeout=timeout_ms)
    except Exception as e:
        print(f"  [WARN] networkidle: {e}")
    # 2) 等所有 <img>.complete
    await page.evaluate("""
        () => Promise.all(
            Array.from(document.images).map(img => {
                if (img.complete && img.naturalWidth > 0) return null;
                return new Promise(r => {
                    img.onload = img.onerror = r;
                    setTimeout(r, 10000);
                });
            })
        )
    """)
    # 3) 等 background-image: 拿一个 body 上的伪 background 图 loading 标志
    await page.evaluate("""
        () => Promise.all(
            Array.from(document.querySelectorAll('*')).map(el => {
                const bg = window.getComputedStyle(el).backgroundImage;
                if (bg && bg !== 'none' && bg.includes('url(')) {
                    const url = bg.match(/url\\([\"']?([^\"')]+)[\"']?\\)/)?.[1];
                    if (url) {
                        return new Promise(r => {
                            const i = new Image();
                            i.onload = i.onerror = r;
                            i.src = url;
                            setTimeout(r, 10000);
                        });
                    }
                }
                return null;
            })
        )
    """)
    await page.wait_for_timeout(800)


async def click(page, sel, desc):
    try:
        await page.click(sel, timeout=3000)
        await page.wait_for_timeout(1000)
        return True
    except Exception as e:
        print(f"  [WARN] click '{desc}': {e}")
        return False


async def main():
    async with async_playwright() as p:
        # 关键：channel="chrome" 走真实 Chrome；headless="new" 强制新 headless 引擎
        try:
            browser = await p.chromium.launch(headless=True, channel="chrome", args=["--disable-web-security", "--no-sandbox"])
            print("[INFO] using real Chrome channel")
        except Exception as e:
            print(f"[INFO] no Chrome channel, fallback to Chromium: {e}")
            browser = await p.chromium.launch(headless=True, args=["--no-sandbox"])
        ctx = await browser.new_context(viewport={"width": 1440, "height": 900}, device_scale_factor=2)
        page = await ctx.new_page()

        # 1. 默认视图
        await page.goto(URL, timeout=60000)
        await page.evaluate("() => localStorage.clear()")
        await page.reload(timeout=60000)
        await wait_fully_loaded(page)
        await shot(page, "1_默认_全部模型_官网")

        # 2. M3 筛选 + 官网
        await click(page, 'button[data-model="m3"]', "M3")
        await wait_fully_loaded(page)
        await shot(page, "2_M3筛选_官网_14张")

        # 3. 全部模型 + 全部产品
        await click(page, 'button[data-model="all"]', "all model")
        await click(page, 'button:has-text("全部")', "全部产品")
        await wait_fully_loaded(page)
        await shot(page, "3_全部模型_全部产品_262张")

        # 4. M3 + 后台
        await click(page, 'button[data-model="m3"]', "M3")
        await click(page, 'button:has-text("后台")', "后台")
        await wait_fully_loaded(page)
        await shot(page, "4_M3筛选_后台_fleet_ops")

        # 5. M3 + 小程序
        await click(page, 'button[data-model="m3"]', "M3")
        await click(page, 'button:has-text("小程序")', "小程序")
        await wait_fully_loaded(page)
        await shot(page, "5_M3筛选_小程序_ev_charging")

        await browser.close()
        print("\n=== Done ===")


if __name__ == "__main__":
    asyncio.run(main())
