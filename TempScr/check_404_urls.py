# -*- coding: utf-8 -*-
"""扫描指定 HTML 文件中的所有 http(s) 外链 URL，报告状态码非 200 的项。"""
import re
import sys
import urllib.request

ROOT = r"C:\Users\mypra\Desktop\VibeCoding指南\skills测评项目\01-前端设计技能测评\03-产出\deepseek"
FILES = [
    "deepseek-stitch-design-ev-charging.html",
    "deepseek-modern-frontend-design-airline.html",
    "deepseek-modern-web-design-airline.html",
    "deepseek-modern-web-design-ev-charging.html",
    "deepseek-modern-web-design-bike-dashboard.html",
]

URL_RE = re.compile(r'https?://[^\s"\'<>\)\]]+\.(?:svg|png|jpg|jpeg|webp|woff2?|ttf|css|js|ico)')

def check(url):
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception as e:
        return f"ERR:{type(e).__name__}"

for fn in FILES:
    path = f"{ROOT}\\{fn}"
    with open(path, encoding="utf-8") as f:
        content = f.read()
    urls = sorted(set(URL_RE.findall(content)))
    bad = []
    for u in urls:
        code = check(u)
        if code != 200:
            bad.append((str(code), u))
    print(f"\n=== {fn} (共 {len(urls)} 个外链) ===")
    if bad:
        for code, u in bad:
            print(f"  [{code}] {u}")
    else:
        print("  全部 200 OK")