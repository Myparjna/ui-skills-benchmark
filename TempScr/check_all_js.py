# -*- coding: utf-8 -*-
"""提取所有 HTML 内联 <script> 并用 node --check 检查语法，报告错误文件与行号。"""
import os, re, subprocess, tempfile

ROOT = r"C:\Users\mypra\Desktop\VibeCoding指南\skills测评项目\01-前端设计技能测评\03-产出\deepseek"
SCRIPT_RE = re.compile(r'<script>(.*?)</script>', re.S)

for fn in sorted(os.listdir(ROOT)):
    if not fn.endswith(".html"):
        continue
    with open(os.path.join(ROOT, fn), encoding="utf-8") as f:
        content = f.read()
    # 也检查带属性/type 的 script 标签
    scripts = re.findall(r'<script[^>]*>(.*?)</script>', content, re.S)
    if not scripts:
        continue
    for i, js in enumerate(scripts):
        if not js.strip():
            continue
        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as tf:
            tf.write(js)
            tmp = tf.name
        r = subprocess.run(["node", "--check", tmp], capture_output=True, text=True)
        if r.returncode != 0:
            # 提取 node 报错的相对行号
            err = r.stderr.strip().splitlines()
            detail = err[-1] if err else ""
            print(f"FAIL {fn} [script#{i}]: {detail}")
        os.unlink(tmp)
print("完成")