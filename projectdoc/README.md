---
document: README.md
generated: 2026-06-17
client_level: developer
---

# 01-前端设计技能测评 — 项目交接文档

## 待确认问题

- [需向交接人确认: 展线上页面数/模型数的统计基准——本地 index.html 显示 484 页 / 13 模型，但 cloudflarepage展厅/pages/ 实际含 526 个文件（含未注册的 gemini3.1pro 与部分残留），线上部署版本以哪个为准？]
- [需向交接人确认: gemini3.1pro 的 9 页（03-产出/gemini3.1pro/，中文命名）是否计划纳入展厅？当前未注册（index.html 无对应分支）。]
- [需向交接人确认: Cloudflare 账号与 GitHub 仓库归属（见 INFRASTRUCTURE.md）。]
- [需向交接人确认: 展厅中 GLM 5.1 与 GLM 5.2 并行展示的定位是否清晰（均为独立模型按钮）]

## 项目简介

本项目是一个 **AI 前端设计技能横向测评平台**，用于对比多个主流 AI 模型在 14 款前端设计 skill 驱动下的页面生成效果。项目产出 484+ 个已集成 HTML 页面和配套 webp 缩略图，通过 Cloudflare Pages 部署为在线展厅，支持按模型、场景、技能三维度筛选浏览。

面向的用户是测评团队成员和关注 AI 前端设计能力的技术决策者。

## 核心功能

- **多模型横向对比**：当前展厅注册 13 个模型 — Kimi K3 / Kimi K2.6 / Kimi 2.5 / GLM 5.2 / GLM 5.1 / DeepSeek V4 Flash0731 / Mimo V2.5 / Mimo V2 Omni / MiniMax M3 / Gemini 3 / GPT-5.6 Terra / Hy3（助手自驱） / Qwen 3.7 Plus
  - 注：GLM 5.2 与 GLM 5.1（原 GLM 5.0 改名）为**两个不同版本**，已分别测评并集成进展厅
  - 注：Hy3 = 本项目 AI 助手自身作为一个"模型"参与横评，采用 14 个隔离 subagent 并行生成
  - 注：`03-产出/gemini3.1pro/`（9 页，中文命名）已生成但**未注册**进展厅
- **14 款公共 design skill**：frontend-design / stitch-design / web-design-guidelines / frontend-design-pro / ui-ux-pro-max / design-taste-frontend / modern-frontend-design / nuxt-ui / sleek-design-mobile-apps / shadcn / impeccable / taste-skill / modern-web-design / superdesign
- **3 个产品场景**：星空航空官网（airline）/ 电动车充电桩小程序（charging）/ 共享两轮运营后台（bikeops）
- **在线展厅**：支持按模型、场景、技能三维筛选，卡片式布局，webp 缩略图预览
- **单页预览器**：view.html 支持直接打开任意 HTML 页面进行全尺寸预览

## 技术栈

**框架**: 无框架（纯静态 HTML + Tailwind CSS CDN）

**UI 组件库**: Tailwind CSS（通过 CDN 引入）

**包管理器**: 无（项目无依赖）

**依赖规模**: 无 Node/Python 依赖（截图脚本需要 Playwright，非必需）

**运行时要求**: 任何现代浏览器 + 本地 HTTP 服务器（推荐 Python 或 npx serve）

## 快速启动

```bash
# 1. 进入展厅目录
cd "cloudflarepage展厅"

# 2. 启动本地 HTTP 服务器
python -m http.server 8766
# 或
npx serve .

# 3. 浏览器访问
# http://localhost:8766
```

**可用脚本**:
无 npm scripts（纯静态项目）；截图脚本见 `TempScr/shot_*.py`（如 `shot_showcase.py`、`shot_deepseek_v4flash.py`、`screenshot_kimi_k3_batch2.py`）

## 速查卡

| 项 | 值 |
|---|---|
| 在线展厅 | https://frontend-design-skills-showcase.pages.dev |
| 生产别名 | https://production.frontend-design-skills-showcase.pages.dev |
| 部署命令 | `cd cloudflarepage展厅 && npx wrangler pages deploy . --project-name=frontend-design-skills-showcase` |
| 本地预览 | `cd cloudflarepage展厅 && python -m http.server 8766` → http://localhost:8766 |
| 本地服务器端口 | 8766（展厅）/ 8080（产出） |
| 当前模型数 | 13（展厅 index.html 注册） |
| 当前缩略图 | 540 张 webp（`cloudflarepage展厅/assets/thumbnails/`） |
| 截图环境 | 系统 Python 3.12 + Playwright（`AppData\Local\Programs\Python\Python312\python.exe`） |
| GitHub 仓库 | https://github.com/Myparjna/ui-skills-benchmark |
| 部署 Token | `CLOUDFLARE_API_TOKEN`（Cloudflare Dashboard → My Profile → API Tokens） |
| Git 分支 | master |

## 文档导航

| 文档 | 内容 |
|---|---|
| [USAGE.md](./USAGE.md) | 使用说明与核心流程 |
| [ARCHITECTURE.md](./ARCHITECTURE.md) | 架构与技术选型 |
| [MODULES.md](./MODULES.md) | 模块职责与调用链 |
| [ENVIRONMENT.md](./ENVIRONMENT.md) | 环境变量 |
| [DEPLOYMENT.md](./DEPLOYMENT.md) | 部署 |
| [INFRASTRUCTURE.md](./INFRASTRUCTURE.md) | 域名/账号/第三方服务 |
| [KNOWN-ISSUES.md](./KNOWN-ISSUES.md) | 已知问题 |
| [MAINTENANCE.md](./MAINTENANCE.md) | 日常维护 |
| [RUNBOOK.md](./RUNBOOK.md) | 故障处置 |
| [REGRESSION-TEST.md](./REGRESSION-TEST.md) | 回归测试 |
| [AI-SERVICES.md](./AI-SERVICES.md) | AI 服务（本项目不涉及运行时 AI 调用） |

另有两份手工维护文档（不在本套件内）：`projectdoc/交接文档.md`（项目最核心交接记录）、`projectdoc/部署记录.md`。
