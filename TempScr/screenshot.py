"""
M3 测评截图脚本：用 Playwright 自带 Chromium 批量截图。
支持 ev_charging 移动端 (390x844) / airline + fleet_ops 桌面端 (1440x900)。
收集 console/page 错误，输出到 05-报告/展厅/assets/screenshots/m3/。

用法：
    python TempScr/screenshot.py
"""
import asyncio
import sys
from pathlib import Path
from playwright.async_api import async_playwright

ROOT = Path("C:/Users/mypra/Desktop/VibeCoding指南/skills测评项目/01-前端设计技能测评")
SOURCE_DIR = ROOT / "03-产出" / "minimaxM3"
TARGET_DIR = ROOT / "05-报告" / "展厅" / "assets" / "screenshots" / "m3"

VIEWPORTS = {
    "ev_charging": {"width": 390, "height": 844},
    "airline": {"width": 1440, "height": 900},
    "fleet_ops": {"width": 1440, "height": 900},
}


def parse_scene(stem: str) -> str:
    parts = stem.split("_")
    if len(parts) >= 3 and parts[0] == "m3":
        return "_".join(parts[2:])
    return parts[-1]


async def screenshot_one(browser, html_path: Path, target_dir: Path):
    name = html_path.stem
    scene = parse_scene(name)
    viewport = VIEWPORTS.get(scene, {"width": 1440, "height": 900})

    target_dir.mkdir(parents=True, exist_ok=True)
    out_path = target_dir / f"{name}.png"

    context = await browser.new_context(viewport=viewport, device_scale_factor=2)
    page = await context.new_page()

    errors = []

    def on_pageerror(exc):
        errors.append(f"pageerror: {str(exc)[:200]}")

    def on_console(msg):
        if msg.type == "error":
            errors.append(f"console.error: {msg.text[:200]}")

    page.on("pageerror", on_pageerror)
    page.on("console", on_console)

    url = f"file:///{html_path.as_posix()}"
    status = "OK"
    try:
        await page.goto(url, timeout=20000, wait_until="domcontentloaded")
        try:
            await page.wait_for_load_state("networkidle", timeout=5000)
        except Exception:
            pass
        await page.wait_for_timeout(1500)
        await page.screenshot(path=str(out_path), full_page=False)
    except Exception as e:
        status = f"FAIL: {str(e)[:200]}"

    await context.close()
    return name, scene, status, out_path, errors


async def main():
    files = sorted(SOURCE_DIR.glob("m3_*.html"))
    print(f"Found {len(files)} HTML files in {SOURCE_DIR}")
    if not files:
        print("No files to screenshot. Exit.")
        return

    TARGET_DIR.mkdir(parents=True, exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        try:
            results = []
            for f in files:
                name, scene, status, out, errors = await screenshot_one(browser, f, TARGET_DIR)
                results.append((name, scene, status, out, errors))
                err_msg = f" | console_err={len(errors)}" if errors else ""
                print(f"  [{scene}] {status}: {name}{err_msg}")
        finally:
            await browser.close()

        all_errors = [(n, e) for n, _, _, _, errs in results for e in errs]
        if all_errors:
            print(f"\n=== Console/Page errors ({len(all_errors)} total, show first 30) ===")
            for n, e in all_errors[:30]:
                print(f"  [{n}] {e}")
        else:
            print("\nNo console/page errors detected.")

        ok = sum(1 for _, _, s, _, _ in results if s == "OK")
        fail = len(results) - ok
        print(f"\nDone. {ok} OK / {fail} FAIL. Screenshots: {TARGET_DIR}")

        if fail > 0:
            print("\n=== Failed files ===")
            for n, _, s, _, _ in results:
                if s != "OK":
                    print(f"  {n}: {s}")


if __name__ == "__main__":
    asyncio.run(main())
