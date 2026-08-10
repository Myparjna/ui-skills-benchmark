# -*- coding: utf-8 -*-
"""并发扫描 deepseek 产出目录全部 HTML 外链，报告非 200 状态码项。"""
import os, re, sys, urllib.request
from concurrent.futures import ThreadPoolExecutor

ROOT = r"C:\Users\mypra\Desktop\VibeCoding指南\skills测评项目\01-前端设计技能测评\03-产出\deepseek"
URL_RE = re.compile(r'https?://[^\s"\'<>\)\]]+\.(?:svg|png|jpg|jpeg|webp|woff2?|ttf|css|js|ico)')

def check(url):
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=8) as r:
            return 200
    except urllib.error.HTTPError as e:
        return e.code
    except Exception:
        return -1

# 收集所有文件的所有外链
file_urls = {}
all_urls = set()
for fn in sorted(os.listdir(ROOT)):
    if not fn.endswith(".html"):
        continue
    with open(os.path.join(ROOT, fn), encoding="utf-8") as f:
        content = f.read()
    urls = sorted(set(URL_RE.findall(content)))
    file_urls[fn] = urls
    all_urls.update(urls)

print(f"共 {len(file_urls)} 个文件, {len(all_urls)} 个唯一外链，开始并发检查...", flush=True)
results = {}
with ThreadPoolExecutor(max_workers=20) as ex:
    for u, code in zip(all_urls, ex.map(check, all_urls)):
        results[u] = code

all_bad = {}
for fn, urls in file_urls.items():
    bad = [(str(results[u]), u) for u in urls if results[u] != 200]
    if bad:
        all_bad[fn] = bad
    print(f"{fn}: {len(urls)} 外链" + (f", BAD={len(bad)}" if bad else " OK"), flush=True)

print("\n===== 汇总非 200 项 =====", flush=True)
for fn, bad in all_bad.items():
    print(f"\n=== {fn} ===", flush=True)
    for code, u in bad:
        print(f"  [{code}] {u}", flush=True)
if not all_bad:
    print("全部外链 200 OK", flush=True)