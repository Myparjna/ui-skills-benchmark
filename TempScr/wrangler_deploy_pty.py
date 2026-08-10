# -*- coding: utf-8 -*-
"""
通过 ConPTY 包装 wrangler deploy，让 wrangler 检测到 TTY 从而复用 OAuth 登录态
（非交互 shell 下 wrangler 强制要求 CLOUDFLARE_API_TOKEN，而本机只有 wrangler login 的 OAuth）
"""
import sys
import time
from winpty import PtyProcess

CMD = [
    r"C:\Users\mypra\.workbuddy\binaries\node\versions\22.22.2\node.exe",
    r"C:\Users\mypra\AppData\Roaming\npm\node_modules\wrangler\bin\wrangler.js",
    "pages", "deploy", ".",
    "--project-name=frontend-design-skills-showcase",
    "--branch=main",
    "--commit-message=deepseek-v4flash: 重新生成 13 来源 x 3 场景共 39 页并更新缩略图",
]

CWD = r"C:\Users\mypra\Desktop\VibeCoding指南\skills测评项目\01-前端设计技能测评\05-报告\展厅"

def main():
    proc = PtyProcess.spawn(CMD, cwd=CWD, dimensions=(40, 200))
    buf = []
    last_data = time.time()
    while True:
        try:
            data = proc.read(4096, blocking=False)
            if data:
                buf.append(data)
                last_data = time.time()
                sys.stdout.write(data)
                sys.stdout.flush()
            else:
                if not proc.isalive():
                    break
                if time.time() - last_data > 300:
                    print("\n[超时 300s 无输出，终止]")
                    break
                time.sleep(0.3)
        except EOFError:
            break
        except Exception as e:
            if not proc.isalive():
                break
            time.sleep(0.3)
    try:
        code = proc.exitstatus
    except Exception:
        code = None
    print(f"\n[exit={code}]")

if __name__ == "__main__":
    main()
