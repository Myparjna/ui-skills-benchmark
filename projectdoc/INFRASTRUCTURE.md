---
document: INFRASTRUCTURE.md
generated: 2026-06-17
client_level: developer
---

# 基础设施与账号

## 域名与 DNS

| 域名 | 用途 | DNS 托管 | SSL |
|---|---|---|---|
| `frontend-design-skills-showcase.pages.dev` | 展厅主域名 | Cloudflare Pages 自动分配 | Cloudflare 自动 SSL |
| `production.frontend-design-skills-showcase.pages.dev` | 生产分支别名 | Cloudflare Pages 自动分配 | Cloudflare 自动 SSL |
| `main.frontend-design-skills-showcase.pages.dev` | main 分支别名（已废弃分支，仅历史遗留） | Cloudflare Pages 自动分配 | Cloudflare 自动 SSL |

无需自定义域名，使用 Cloudflare Pages 默认域名。

## 第三方服务账号清单

| 服务 | 用途 | 账号归属 | 控制台 | 关联密钥 | 交接动作 |
|---|---|---|---|---|---|
| Cloudflare | 展厅托管（Pages） | [需向交接人确认: 账号归属] | https://dash.cloudflare.com | `CLOUDFLARE_API_TOKEN` | 确保 API Token 有效，或在新账号创建 Pages 项目并重部署 |
| GitHub | 代码托管 | [需向交接人确认: 账号归属] | https://github.com | 无 | 仓库地址：https://github.com/Myparjna/ui-skills-benchmark |

## 服务器/托管资源

无服务器。全部使用 Cloudflare Pages（serverless 静态托管）。

## 部署历史

| 日期 | 内容 | 页面数 |
|---|---|---|
| 2026-06-10 | 首次部署 + Kimi K2.6 加测 | 349 |
| 2026-06-16 | 新增 Qwen 3.7 Plus | 391 |
| 2026-06-16 | 移除 Gemini 3.5 | 349 |
| 2026-06-17 | Gemini 3 补测完成 + 移除"不使用skills"基线 | 388 |
| 2026-06-18 | GLM 5.2 补测集成部署 | 430 |
| 2026-07 | Hy3 集成 + 缩略图改版（png→webp） | 484（本地）/ 526（pages 实有） |
| 2026-08-10 | 目录重组（05-报告/ → cloudflarepage展厅/）+ kimi/glm 重命名 + 交接文档同步，已推送 GitHub；Mapbox 假 token 历史重写修复 | — |

## GLM 版本说明

| 版本 | 目录 | 状态 | 备注 |
|---|---|---|---|
| Kimi 2.5 | `03-产出/kimi2.5/` | 已上线 | 系统内置版本，45 页，旧命名规则（`{skill}_{scene}.html`） |
| GLM 5.1（原 5.0） | `03-产出/glm5.1/` | 已上线 | 系统内置版本，40 页，旧命名规则；展厅已改名「GLM 5.1」 |
| GLM 5.2 | `03-产出/glm5.2/` | 已上线 | 2026-06-17 补测，42 页，新命名规则（`glm5.2-{skill}-{scene}.html`） |

> 两个版本在展厅中并存展示，便于横向对比。GLM 5.2 使用独立模型按钮（data-model="glm52"），未覆盖 GLM 5.1 入口。

## 未托管资产

- `03-产出/gemini3.1pro/`（9 页，中文命名）：已生成但未注册进展厅，未部署。
- `03-产出/gemini35/`（1 页残留）：已从展厅移除。
