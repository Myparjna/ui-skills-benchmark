---
document: USAGE.md
generated: 2026-08-10 15:18
client_level: developer
---

# 项目使用说明

## 适用角色与入口

本项目是一个 **AI 前端设计 skill 横向测评平台**，面向三类角色：

| 角色 | 入口 | 前置权限 |
|---|---|---|
| **测评浏览者** | 在线展厅 https://frontend-design-skills-showcase.pages.dev （本地入口 `05-报告/展厅/index.html`） | 无，公开可访问 |
| **测评执行者**（新模型加测） | 本地 `01-前端设计技能测评/` 目录 + 各模型在 03-产出 的输出目录 | 本机已安装：Claude Code、Playwright（系统 Python 3.12）、Cloudflare Wrangler CLI |
| **部署维护者** | 本地 `05-报告/展厅/` + Cloudflare Dashboard | `CLOUDFLARE_API_TOKEN` 或 `wrangler login` 登录态 |

## 核心使用流程

### 流程一：浏览展厅对比各模型表现（测评浏览者）

1. **打开展厅**：浏览器访问在线地址，或本地 `cd 05-报告/展厅 && python -m http.server 8766` 后访问 http://localhost:8766
2. **选择模型**：点击顶部模型按钮（共 13 个：Kimi K3 / Kimi K2.6 / Kimi 2.5 / GLM 5.2 / GLM 5.1 / DeepSeek V4 Flash0731 / Mimo V2.5 / Mimo V2 Omni / MiniMax M3 / Gemini 3 / GPT-5.6 Terra / Hy3 / Qwen 3.7 Plus）
3. **按 skill 或场景筛选**：点击分类 chip 过滤（全部模型）或保持 `全部模型` 查看混合对比
4. **查看卡片**：每张卡片为「模型 × skill × 场景」组合，显示 webp 缩略图
5. **全尺寸预览**：点击卡片右上角「预览」在 view.html 中打开完整 HTML
   - 失败表现：页面打不开或缩略图空白 → 页面文件缺失或 CDN 资源加载失败，见 KNOWN-ISSUES.md

### 流程二：新模型加测（测评执行者）

1. **准备输出目录**：在 `03-产出/` 新建 `{模型名}/`，按 `{模型}-{skill}-{场景}.html` 命名（场景：airline / charging / bikeops）
2. **生成页面**：用目标模型在对应 design skill 驱动下为 3 个场景生成 HTML（生成规范文件已在 02-输入/ 清理，可按既有产出文件的命名与结构复刻规范）
3. **复制到展厅**：`cp 03-产出/{模型}/*.html 05-报告/展厅/pages/`，文件名加模型前缀避免冲突
4. **截图**：运行对应 Playwright 截图脚本（桌面 1280×720 / 移动 390×844@2x），输出 webp 到 `05-报告/展厅/assets/thumbnails/`
5. **注册进展厅**：编辑 `05-报告/展厅/index.html` 的 8 处（模型按钮、分类数组、getFileMap 分支、getAllItems、loadFilters、getCurrentCategories、modelBadgeColor、统计数字）
6. **本地验证**：启动 HTTP 服务器，检查图片与链接
7. **部署**：`npx wrangler pages deploy . --project-name=frontend-design-skills-showcase --branch=production`

### 流程三：部署更新（部署维护者）

1. **本地验证**：在 `05-报告/展厅/` 启动本地服务器，确认改动无回归
2. **部署**：`cd 05-报告/展厅 && npx wrangler pages deploy . --project-name=frontend-design-skills-showcase`
3. **验证线上**：访问 https://frontend-design-skills-showcase.pages.dev，如缓存未更新用别名 https://production.frontend-design-skills-showcase.pages.dev
   - 失败表现：403 → token 失效（RUNBOOK.md）；旧版本 → CDN 缓存未清（KNOWN-ISSUES.md）

## 启动与停止

**开发/本地预览（展厅）**：

```bash
cd "05-报告/展厅"
python -m http.server 8766      # 或 npx serve .
# 访问 http://localhost:8766
# 停止：Ctrl+C
```

**开发/本地预览（源产出）**：

```bash
cd "03-产出"
python -m http.server 8080      # 浏览原始 HTML，避免 file:// 协议 CDN 加载失败
```

**截图脚本**：单次运行，无常驻进程，用系统 Python 3.12 绝对路径执行（脚本位于 `TempScr/`，如 `TempScr/shot_showcase.py`、`TempScr/shot_deepseek_v4flash.py`、`TempScr/screenshot_kimi_k3_batch2.py`）：

```bash
"C:\Users\mypra\AppData\Local\Programs\Python\Python312\python.exe" "TempScr/shot_showcase.py"
```

## 数据与文件

- **输入**：`02-输入/产品说明文档/` 3 份产品文档（星空航空官网 / 充电桩小程序 / 两轮运营后台）
- **输出**：`03-产出/{模型}/*.html`（源产出）→ 复制到 `05-报告/展厅/pages/`
- **命名规则**：各模型略有差异（见 MODULES.md「命名规则」表）；统一建议 `{模型}-{skill}-{airline|charging|bikeops}.html`
- **截图**：`05-报告/展厅/assets/thumbnails/*.webp`（540 张，2026-07 起从 png 改为 webp）
- **保留周期**：无自动清理；过时目录移入 `Trash/` 保留备份
- **数据所有权**：产出文件为测评核心数据，删除前先备份

## 权限与安全边界

- **公网边界**：展厅为公开静态站点，无登录、无后台
- **敏感操作**：`wrangler pages deploy` 会覆盖线上生产版本，部署前必须在本地验证
- **禁止**：生产环境直接编辑 `05-报告/展厅/pages/` 下的文件而不同步源产出；随意删除 `03-产出/` 下历史模型数据
- `CLOUDFLARE_API_TOKEN` 不写入任何前端文件或提交到 git

## 常见使用问题

| 问题 | 解决 |
|---|---|
| 展厅打不开 / 缩略图空白 | 本地访问需走 HTTP 服务器，勿用 file:// 协议；线上访问检查 Cloudflare CDN 缓存（KNOWN-ISSUES.md） |
| 新增模型后展厅不显示 | `index.html` 的 8 处注册点缺漏，逐一核对（见流程二步骤 5） |
| 截图白屏 | React+Babel 页面需 importmap 注入修复（注入 `react/jsx-runtime` shim + 加 `data-type="module"`） |
| 部署 403 | token 失效，重新生成并更新 `CLOUDFLARE_API_TOKEN`（RUNBOOK.md） |
