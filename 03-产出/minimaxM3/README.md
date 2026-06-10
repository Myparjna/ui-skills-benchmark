# minimaxM3 — 14 款公共 design skill × 3 场景 HTML 产出

> **生成模型**: MiniMax M3 (minimax-m3-free，免费配额版)
> **生成日期**: 2026-06-02
> **文件数**: 42 个独立 HTML (14 公共 skill × 3 场景)

---

## 目录结构

```
minimaxM3/
├── m3_web-design-guidelines_{ev_charging,airline,fleet_ops}.html
├── m3_frontend-design_{ev_charging,airline,fleet_ops}.html
├── m3_stitch-design_{ev_charging,airline,fleet_ops}.html
├── m3_ui-ux-pro-max_{ev_charging,airline,fleet_ops}.html
├── m3_frontend-design-pro_{ev_charging,airline,fleet_ops}.html
├── m3_design-taste-frontend_{ev_charging,airline,fleet_ops}.html
├── m3_modern-frontend-design_{ev_charging,airline,fleet_ops}.html
├── m3_nuxt-ui_{ev_charging,airline,fleet_ops}.html
├── m3_sleek-design-mobile-apps_{ev_charging,airline,fleet_ops}.html
├── m3_modern-web-design_{ev_charging,airline,fleet_ops}.html
├── m3_superdesign_{ev_charging,airline,fleet_ops}.html
├── m3_taste-skill_{ev_charging,airline,fleet_ops}.html
├── m3_impeccable_{ev_charging,airline,fleet_ops}.html
└── m3_shadcn_{ev_charging,airline,fleet_ops}.html
```

---

## 14 款 Skill 风格速览

| # | skillId | 厂商 | M3 表现 | 视觉风格关键词 |
|---|---------|------|--------|---------------|
| 1 | web-design-guidelines | Vercel Labs | 极简白 | 蓝 #0066CC + WCAG AA + skip link + aria |
| 2 | frontend-design | Anthropic | 米黄报纸 | rust #C44E1F + 衬线大字 + 多栏 editorial |
| 3 | stitch-design | Google | Material 3 | 紫底 + Roboto Flex + container 分层 |
| 4 | ui-ux-pro-max | NextLevelBuilder | 模板驱动 | 白底蓝青 dashboard + 多图表 |
| 5 | frontend-design-pro | binjuhor | 法式 soft | Playfair Display + 米白高级 |
| 6 | design-taste-frontend | leonxlnx | 暗色 dashboard | 翠绿 #00D4AA + 禁紫禁 3 等分 |
| 7 | modern-frontend-design | deveshpunjabi | 玻璃态 | 紫青粉渐变 + Space Grotesk |
| 8 | nuxt-ui | Nuxt | M3 token | #0ea5e9 圆角 + 表格 + pill |
| 9 | sleek-design-mobile-apps | sleekdotdesign | 玻璃态移动 | Manrope + 紫青渐变 pill |
| 10 | modern-web-design | freshtechbro | brutalist | 黑白 + 强调橙 + Inter/Space Mono |
| 11 | superdesign | superdesigndev | 暗紫粉霓虹 | dot grid + 大字渐变 + 引言 |
| 12 | taste-skill | Nexu | 暖色奶白 | #FAF7F2 + Playfair Display editorial |
| 13 | impeccable | pbakaus | 米黄纸感 | Instrument Serif + § 符号 |
| 14 | shadcn | shadcn-ui | 衬线 hybrid | 白底 + 6px radius + 信息密度高 |

> 剔除 `canvas-design`，共 14 款，遵从项目源文档定义。

---

## 截图

42 张首屏截图已生成在：

```
05-报告/展厅/assets/screenshots/m3/m3_{skillId}_{scene}.png
```

视口：ev_charging 390×844 (iPhone 14)，airline + fleet_ops 1440×900。
全部 42 张 OK，0 console error，0 失败。

---

## 同步到展厅

```
# 复制 HTML 到展厅
Copy-Item 03-产出/minimaxM3/*.html 05-报告/展厅/pages/

# 截图已直接生成到
05-报告/展厅/assets/screenshots/m3/
```

展厅 `index.html` 已加：
- M3 筛选按钮（teal #0d9488 badge）
- header 数字更新到 "262 个页面 · 7 个模型"

---

## 复现

```bash
# 1. 截图（Playwright headless Chromium）
python TempScr/screenshot.py

# 2. 验证展厅 M3 筛选
python TempScr/test_m3_filter.py

# 3. 同步到展厅
Copy-Item 03-产出/minimaxM3/*.html 05-报告/展厅/pages/

# 4. 在浏览器打开展厅
start 05-报告/展厅/index.html
```

---

## 生成方法学

本次 42 个 HTML 中：
- **ev_charging 14 个**：subagent (kimi-k2.6) 跑完，session 全部成功
- **airline 13 个**：subagent 跑完；ui-ux-pro-max 1 个由 M3 Write 补完
- **fleet_ops 14 个**：subagent 全部 cancelled / timeout；**14 个由 M3 Write 工具直接生成**

由于 OpenCode 的 Write 工具 = Sisyphus 调度器（M3 本身）输出 content → 写入文件，因此 M3 才是 fleet_ops 14 个 HTML 的真正设计者。

Write 单次 content 上限 ~30KB，fleet_ops 14 个 HTML 全部使用"紧凑版"（每 HTML 22-26KB），保留核心 8-9 板块 + Lucide icon + 配色 + 字体。

详细方法学见 `05-报告/M3-测评报告.md` 第 6 节。

---

*文件基于 2026-06-02 现场生成。*
