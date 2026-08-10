# -*- coding: utf-8 -*-
"""将 deepseek 最新产物同步到展厅：
1) 复制 03-产出/deepseek/*.html -> 展厅/pages/
2) 把最新 PNG 截图转成 webp 缩略图 -> 展厅/assets/thumbnails/"""
import os, shutil
from PIL import Image

ROOT = r"C:\Users\mypra\Desktop\VibeCoding指南\skills测评项目\01-前端设计技能测评"
SRC_PAGES = os.path.join(ROOT, "03-产出", "deepseek")
SRC_SHOTS = os.path.join(ROOT, "ScreenShot", "deepseek-v4flash-20260806-rerun")
DST_PAGES = os.path.join(ROOT, "05-报告", "展厅", "pages")
DST_THUMBS = os.path.join(ROOT, "05-报告", "展厅", "assets", "thumbnails")

count_html = 0
count_webp = 0
missing_png = []
for fn in sorted(os.listdir(SRC_PAGES)):
    if not fn.endswith(".html"):
        continue
    # 1) 复制 HTML
    shutil.copy2(os.path.join(SRC_PAGES, fn), os.path.join(DST_PAGES, fn))
    count_html += 1
    # 2) 生成 webp 缩略图
    png = os.path.join(SRC_SHOTS, fn.replace(".html", ".png"))
    if not os.path.exists(png):
        missing_png.append(fn)
        continue
    out = os.path.join(DST_THUMBS, fn.replace(".html", ".webp"))
    with Image.open(png) as im:
        im.save(out, "WEBP", quality=85, method=6)
    count_webp += 1

print(f"HTML 复制: {count_html}")
print(f"webp 生成: {count_webp}")
if missing_png:
    print("缺少截图:", missing_png)