# -*- coding: utf-8 -*-
"""用 GET 请求验证 jsdelivr 图标 URL 的真实状态码（HEAD 容易被 CDN 忽略）。"""
import os, re, urllib.request
from concurrent.futures import ThreadPoolExecutor

ROOT = r"C:\Users\mypra\Desktop\VibeCoding指南\skills测评项目\01-前端设计技能测评\03-产出\deepseek"
URL_RE = re.compile(r'https?://[^\s"\'<>\)\]]+\.(?:svg|png|jpg|jpeg|webp|woff2?|ttf|css|js|ico)')

def check(url):
    req = urllib.request.Request(url, method="GET", headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception:
        return -1

all_urls = set()
for fn in os.listdir(ROOT):
    if not fn.endswith(".html"):
        continue
    with open(os.path.join(ROOT, fn), encoding="utf-8") as f:
        all_urls.update(URL_RE.findall(f.read()))
# 只保留 jsdelivr 图标
icon_urls = sorted(u for u in all_urls if "tabler/icons" in u)
print(f"共 {len(icon_urls)} 个 jsdelivr 图标外链，GET 检查...", flush=True)

results = {}
with ThreadPoolExecutor(max_workers=16) as ex:
    for u, code in zip(icon_urls, ex.map(check, icon_urls)):
        results[u] = code

bad = {u: c for u, c in results.items() if c != 200}
print(f"非 200 项: {len(bad)}", flush=True)
for u, c in sorted(bad.items()):
    print(f"  [{c}] {u}", flush=True)