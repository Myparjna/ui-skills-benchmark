---
document: MODULES.md
generated: 2026-08-10 15:18
client_level: developer
---

# 模块说明

## 模块总览

```mermaid
graph LR
    subgraph 输入层
        A1[02-输入/产品说明文档] -->|产品需求| G[AI 模型生成 HTML]
        A2[01-技能/已安装技能] -->|design skill 约束| G
    end
    subgraph 生产层
        G --> H1[03-产出/{模型}/源产出]
        H1 -->|复制| H2[05-报告/展厅/pages/展厅副本]
        H1 -->|截图脚本 Playwright| H3[05-报告/展厅/assets/thumbnails/缩略图]
    end
    subgraph 展厅层
        H2 --> I[index.html 主页面]
        H3 --> I
        I -->|iframe| V[view.html 单页预览]
    end
    I -->|wrangler deploy| J[Cloudflare Pages]
```

**主执行链路**：产品文档 + design skill → AI 模型生成 HTML → 源产出 → 展厅副本 + 缩略图 → index.html 聚合 → 部署上线。本项目无运行时后端，所有"模块"均为静态文件与脚本。

## 模块职责矩阵

| 模块 | 职责 | 入口文件 | 上游 | 下游 | 关键配置 | 测试 |
|---|---|---|---|---|---|---|
| **技能库** | 提供 14 款 design skill 定义 | `01-技能/已安装技能/skills/` | 外部 GitHub 仓库 | AI 模型生成时参考 | `01-技能/版本锁定.json`（哈希锁定） | 无 |
| **输入产品文档** | 3 个测评场景的产品需求 | `02-输入/产品说明文档/*.md` | — | AI 模型生成时参考 | 星空航空官网 / 充电桩小程序 / 两轮运营后台 | 无 |
| **模型产出** | 各模型生成的 HTML（测评核心数据） | `03-产出/{模型}/` | AI 模型 + skill + 产品文档 | 展厅副本、缩略图 | 命名规则因模型而异（见下） | 无 |
| **展厅页面副本** | 供展厅 iframe 加载的 HTML | `05-报告/展厅/pages/` | 03-产出 复制 | index.html | 文件名加模型前缀 | 无 |
| **缩略图生成** | 截图脚本 | `TempScr/shot_*.py`、`TempScr/screenshot_*.py` | 03-产出 HTML | `assets/thumbnails/*.webp` | Python 3.12 + Playwright | 无 |
| **展厅主页面** | 聚合展示与筛选 | `05-报告/展厅/index.html` | pages/ + thumbnails/ | Cloudflare Pages | 13 个模型配置 + getFileMap 映射 | 无 |
| **单页预览器** | 全尺寸预览单页 | `05-报告/展厅/view.html` | pages/ 任意 HTML | 浏览器 | URL 参数指定页面 | 无 |

## 关键目录

| 目录 | 用途 | 变更约束 |
|---|---|---|
| `01-技能/已安装技能/skills/` | 14 款 skill 的 SKILL.md | **只读参考**，不随测评修改；版本由 `版本锁定.json` 记录 |
| `02-输入/产品说明文档/` | 3 个测评场景需求文档 | 修改会改变所有模型产出，需先确认 |
| `03-产出/{模型}/` | 各模型源产出 | **核心数据**，删除前备份；新增模型在此建新目录 |
| `05-报告/展厅/pages/` | 展厅 HTML 副本 | 与 03-产出 同步维护 |
| `05-报告/展厅/assets/thumbnails/` | webp 缩略图 | 由截图脚本生成，可随时重截 |
| `05-报告/展厅/index.html` | 展厅主页面 | 新增模型需同步 8 处注册点 |
| `05-报告/展厅/view.html` | 单页预览器 | 少改动 |
| `TempScr/` | 临时截图脚本 | 一次性脚本，可清理 |
| `ScreenShot/` | 开发验证截图 | 运营残留，可清理 |

### 各模型产出目录与命名规则

| 模型 | 目录 | 页面数 | 命名规则 |
|---|---|---|---|
| Kimi 2.5 | `kimi2.5/` | 45 | `{skill}_{scene}.html` |
| Kimi K2.6 | `kimi-k2.6/` | 42 | `kimi-k2.6-{skill}-{scene}.html` |
| Kimi K3 | `kimi-k3/` | 12 | `kimi-k3-{skill}-{scene}.html` |
| DeepSeek V4 Flash0731 | `deepseek/` | 42 | `deepseek-{skill}-{scene}.html` |
| Mimo V2 Omni | `mimoV2omni/` | 37 | `{catId}-{scene}.html`（特殊映射） |
| Mimo V2.5 | `mimoV2.5/` | 42 | `mimoV25-{skill}-{scene}.html` |
| GLM 5.1 | `glm5.1/` | 40 | `{缩写}_{scene}.html`（apple/linear/fd/mfd 等） |
| GLM 5.2 | `glm5.2/` | 42 | `glm5.2-{skill}-{scene}.html` |
| MiniMax M3 | `minimaxM3/` | 42 | `m3_{skill}_{scene}.html` |
| Gemini 3 | `gemini3/` | 42 | `gemini3_{skill}_{scene}.html` |
| Gemini 3.1 Pro | `gemini3.1pro/` | 9 | `gemini3.1pro-{中文场景}.html`（未集成展厅） |
| GPT-5.6 Terra | `gpt5.6-terra/` | 42 | `gpt5.6-terra-{skill}-{scene}.html` |
| Hy3（助手自驱） | `hy3/` | 42 | `hy3-{skill}-{scene}.html` |
| Qwen 3.7 Plus | `qwen3.7-plus/` | 42 | `qwen3.7-plus-{skill}-{scene}.html` |

> `{scene}` 对应：airline（官网）/ charging（小程序）/ bikeops（后台）。Gemini 3 早期版本用 `skystar_airline`/`ev_charging`/`fleet_ops`。`gemini35/` 目录仅剩 1 页（已从展厅移除）。`03-产出/ScreenShot/` 为截图残留目录（无 HTML）。

## 关键调用链

1. **新模型加测**：产品文档（`02-输入/产品说明文档/`）+ design skill（`01-技能/已安装技能/skills/`）→ AI 模型生成 → `03-产出/{模型}/{模型}-{skill}-{scene}.html` → 复制到 `05-报告/展厅/pages/` → `index.html` `getFileMap()`（`05-报告/展厅/index.html:183`）映射 → `buildItems()`（`:301`）→ 展厅卡片
2. **缩略图生成**：`03-产出/{模型}/*.html` → Playwright 脚本（`TempScr/shot_showcase.py` / `TempScr/screenshot_kimi_k3_batch2.py`，桌面 1280×720 / 移动 390×844@2x）→ `05-报告/展厅/assets/thumbnails/{模型}-*.webp`
3. **展厅浏览**：`index.html` 模型按钮（`:48-58`）→ `getCurrentCategories()`（`:377-385`）→ `renderGallery()` → iframe 加载 `pages/{file}` 或 `view.html?src=...`

## 共享状态与数据边界

- **无数据库、无缓存服务**。唯一共享"状态"是文件系统：`03-产出/` 与 `05-报告/展厅/pages/` 是**冗余副本**，需保持同步（复制操作完成后再截图/部署）。
- `index.html` 内部的 `categories` 数组是**唯一事实来源**，决定展厅展示哪些 skill；新增模型必须同步 8 处注册点，否则页面不显示。
- 截图脚本依赖 Chrome 路径 `C:\Program Files\Google\Chrome\Application\chrome.exe`（环境特定，非可移植）。
- 并发约束：多个 subagent 并行生成时使用不同输出目录，避免文件冲突（Hy3 曾用 14 个隔离 subagent）。

## 扩展与替换点

- **新增模型**：`03-产出/` 建新目录 → 复制到 `pages/` → 编辑 `index.html` 8 处注册点（模型按钮、`{model}Categories`、`getFileMap()`、`getAllItems()`、`loadFilters()`、`getCurrentCategories()`、`modelBadgeColor()`、统计数字）
- **替换截图方案**：现有 Playwright 截图脚本统一为 Python 版，位于 `TempScr/`（`shot_showcase.py`、`shot_deepseek_v4flash.py`、`screenshot_kimi_k3_batch2.py`），输出统一 webp；新模型截图按需新建同风格脚本
- **无正式插件/适配器接口**；展厅为单文件 SPA，扩展靠改 `index.html`。若模型数量继续增长，建议将模型配置抽象为 JSON（见 KNOWN-ISSUES.md 技术债）
