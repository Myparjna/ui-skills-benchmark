# -*- coding: utf-8 -*-
"""批量修复 deepseek 产出中的 Tabler 404 图标名，替换为真实存在的图标。"""
import os

ROOT = r"C:\Users\mypra\Desktop\VibeCoding指南\skills测评项目\01-前端设计技能测评\03-产出\deepseek"

# 404 图标名 -> 正确 Tabler 图标名（精确匹配 /icons/NAME.svg）
MAP = {
    "wrench": "tool",
    "zap": "bolt",
    "eiffel-tower": "tower",
    "building-eiffel-tower": "tower",
    "building-airport": "building-skyscraper",
    "seat": "armchair",
    "wave": "wave-sine",
    "plane-depart": "plane-departure",
    "clock-hour-1": "clock-hour-1",  # 兜底，本身有效
    "clock-hour": "clock-hour-1",
    "sliders": "adjustments-horizontal",
    "slider": "adjustments-horizontal",
    "file-receipt": "receipt",
    "battery-charge-2": "battery-charging-2",
    "battery-charge": "battery-charging",
    "battery-full": "battery-4",
    "battery-low": "battery-1",
    "boundaries": "border-all",
    "layer": "layers-union",
    "layers": "layers-union",
    "no-parking": "parking-circle",
    "banknote": "cash-banknote",
    "signal-5": "signal-5g",
    "signal": "cell-signal-4",
    "smart-phone": "device-mobile",
    "utensils": "tools-kitchen",
    "bounding-box": "box-model",
    "roll": "rotate-2",
    "qr-code": "qrcode",
    "ticket-2": "ticket",
    "airport": "building-airport",
    "plane-landing": "plane-arrival",
    "swapping": "arrows-shuffle",
    "leaves": "leaf",
    "trend-down": "trending-down",
    "trend-up": "trending-up",
    "file-refund": "receipt-refund",
}

def replace_fname(content, old, new):
    return content.replace(f"/icons/{old}.svg", f"/icons/{new}.svg")

total = 0
for fn in sorted(os.listdir(ROOT)):
    if not fn.endswith(".html"):
        continue
    path = os.path.join(ROOT, fn)
    with open(path, encoding="utf-8") as f:
        content = f.read()
    orig = content
    for old, new in MAP.items():
        if old == new:
            continue
        content = replace_fname(content, old, new)
    if content != orig:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        total += 1
        print(f"已修复: {fn}", flush=True)

print(f"\n共修复 {total} 个文件。")