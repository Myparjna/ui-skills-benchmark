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

无需自定义域名，使用 Cloudflare Pages 默认域名。

## 第三方服务账号清单

| 服务 | 用途 | 账号归属 | 交接动作 |
|---|---|---|---|
| Cloudflare | 展厅托管（Pages） | [需向交接人确认: 账号归属] | 确保 API Token 有效，或在新账号创建 Pages 项目 |
| GitHub | 代码托管 | [需向交接人确认: 账号归属] | 仓库地址：https://github.com/Myparjna/ui-skills-benchmark |

## 服务器/托管资源

无服务器。全部使用 Cloudflare Pages（serverless 静态托管）。

## 部署历史

| 日期 | 内容 | 页面数 |
|---|---|---|
| 2026-06-10 | 首次部署 + Kimi K2.6 加测 | 349 |
| 2026-06-16 | 新增 Qwen 3.7 Plus | 391 |
| 2026-06-16 | 移除 Gemini 3.5 | 349 |
| 2026-06-17 | Gemini 3 补测完成 + 移除"不使用skills"基线 | 388 |
| 2026-06-17 | GLM 5.2 补测 HTML 生成完毕（42 页，待集成部署，未上线） | 388（在线）/ 430（含未集成） |

## GLM 版本说明

| 版本 | 目录 | 状态 | 备注 |
|---|---|---|---|
| GLM 5.0 | `03-产出/glm/` | 已上线 | 系统内置版本，40 页，旧命名规则（`{style}_{scene}.html`） |
| GLM 5.2 | `03-产出/glm5.2/` | 待集成 | 2026-06-17 补测，42 页，新命名规则（`glm5.2-{skill}-{scene}.html`，沿用 qwen3.7-plus 标准） |

> 两个版本需在展厅中并存展示，便于横向对比。GLM 5.2 集成时需在 `index.html` 新增独立的模型按钮（建议 data-model="glm52"），不要覆盖现有 GLM 5.0 入口。
