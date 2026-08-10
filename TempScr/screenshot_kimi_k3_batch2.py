# -*- coding: utf-8 -*-
"""
kimi-k3 新增 6 页（frontend-design / web-design-guidelines）缩略图截图脚本
沿用展厅既有规格：桌面场景 1280x720 webp，charging 移动场景 780x1688 webp (390x844 @2x)
"""
import os
import subprocess
import sys
import time
from PIL import Image

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PAGES_DIR = r"C:\Users\mypra\Desktop\VibeCoding指南\skills测评项目\01-前端设计技能测评\05-报告\展厅\pages"
THUMB_DIR = r"C:\Users\mypra\Desktop\VibeCoding指南\skills测评项目\01-前端设计技能测评\05-报告\展厅\assets\thumbnails"
TMP_DIR = r"C:\Users\mypra\Desktop\VibeCoding指南\skills测评项目\01-前端设计技能测评\TempScr\_shots"

FILES = [
    "kimi-k3-frontend-design-airline.html",
    "kimi-k3-frontend-design-charging.html",
    "kimi-k3-frontend-design-bikeops.html",
    "kimi-k3-web-design-guidelines-airline.html",
    "kimi-k3-web-design-guidelines-charging.html",
    "kimi-k3-web-design-guidelines-bikeops.html",
]

def shot_one(filename: str) -> str:
    name = filename.replace(".html", "")
    is_mobile = "charging" in filename
    if is_mobile:
        width, height, scale = 390, 844, 2
    else:
        width, height, scale = 1280, 720, 1

    src = os.path.join(PAGES_DIR, filename)
    png_out = os.path.join(TMP_DIR, name + ".png")
    webp_out = os.path.join(THUMB_DIR, name + ".webp")
    url = "file:///" + src.replace("\\", "/")

    cmd = [
        CHROME,
        "--headless",
        "--disable-gpu",
        "--hide-scrollbars",
        f"--window-size={width},{height}",
        f"--force-device-scale-factor={scale}",
        "--virtual-time-budget=8000",
        f"--screenshot={png_out}",
        url,
    ]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
    if not os.path.exists(png_out):
        print(f"[FAIL] {filename}: chrome 未产出截图\n{r.stderr[-500:]}")
        return ""

    img = Image.open(png_out)
    img.save(webp_out, "WEBP", quality=88)
    print(f"[OK] {filename} -> {name}.webp ({img.size[0]}x{img.size[1]})")
    return webp_out

def main():
    os.makedirs(TMP_DIR, exist_ok=True)
    os.makedirs(THUMB_DIR, exist_ok=True)
    ok = 0
    for f in FILES:
        try:
            if shot_one(f):
                ok += 1
        except Exception as e:
            print(f"[ERROR] {f}: {e}")
        time.sleep(0.5)
    print(f"\n完成 {ok}/{len(FILES)}")

if __name__ == "__main__":
    main()
