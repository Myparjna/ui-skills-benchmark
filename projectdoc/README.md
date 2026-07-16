---
document: README.md
generated: 2026-06-17
client_level: developer
---

# 01-前端设计技能测评 — 项目交接文档

## 项目简介

本项目是一个 **AI 前端设计技能横向测评平台**，用于对比 11 个主流 AI 模型在 14 款前端设计 skill 驱动下的页面生成效果。项目产出 472 个已集成 HTML 页面和配套截图，通过 Cloudflare Pages 部署为在线展厅，支持按模型、场景、技能三维度筛选浏览。（注：Hy3 的 42 页本地已集成，线上待下次部署后生效。）

面向的用户是测评团队成员和关注 AI 前端设计能力的技术决策者。

## 核心功能

- **多模型横向对比**：Kimi 2.5 / Kimi K2.6 / DeepSeek V4 / Mimo V2 Omni / Mimo V2.5 / GLM 5.0 / GLM 5.2 / MiniMax M3 / Gemini 3 / Qwen 3.7 Plus / Hy3（助手自驱）共 11 个模型
  - 注：GLM 5.2 与系统内置的 GLM 5.0 为**两个不同版本**，已分别测评并集成进展厅
  - 注：Hy3 = 本项目 AI 助手自身作为一个"模型"参与横评，采用 14 个隔离 subagent 并行生成
- **14 款公共 design skill**：frontend-design / stitch-design / web-design-guidelines / frontend-design-pro / ui-ux-pro-max / design-taste-frontend / modern-frontend-design / nuxt-ui / sleek-design-mobile-apps / shadcn / impeccable / taste-skill / modern-web-design / superdesign
- **3 个产品场景**：星空航空官网（skystar_airline）/ 电动车充电桩小程序（ev_charging）/ 共享两轮运营后台（fleet_ops）
- **在线展厅**：支持按模型、场景、技能三维筛选，卡片式布局，截图预览
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
cd "05-报告/展厅"

# 2. 启动本地 HTTP 服务器
python -m http.server 8766
# 或
npx serve .

# 3. 浏览器访问
# http://localhost:8766
```

**可用脚本**:
无 npm scripts（纯静态项目）

## 文档导航

| 文档 | 内容 |
|---|---|
| [ARCHITECTURE.md](./ARCHITECTURE.md) | 架构与技术选型 |
| [ENVIRONMENT.md](./ENVIRONMENT.md) | 环境变量 |
| [DEPLOYMENT.md](./DEPLOYMENT.md) | 部署 |
| [INFRASTRUCTURE.md](./INFRASTRUCTURE.md) | 域名/账号/第三方服务 |
| [KNOWN-ISSUES.md](./KNOWN-ISSUES.md) | 已知问题 |
| [MAINTENANCE.md](./MAINTENANCE.md) | 日常维护 |
| [RUNBOOK.md](./RUNBOOK.md) | 故障处置 |
| [AI-SERVICES.md](./AI-SERVICES.md) | AI 服务（本项目不涉及运行时 AI 调用） |
