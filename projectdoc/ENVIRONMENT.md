---
document: ENVIRONMENT.md
generated: 2026-06-17
client_level: developer
---

# 环境变量

> 本项目为纯静态 HTML 站点，无应用级环境变量。以下为部署和截图脚本所需的服务配置。

## 变量清单

| 变量名 | 用途 | 获取方式 | 必需性 | 使用场景 |
|---|---|---|---|---|
| `CLOUDFLARE_API_TOKEN` | Wrangler CLI 部署认证 | Cloudflare Dashboard → My Profile → API Tokens → 创建 Token（权限：Cloudflare Pages: Edit） | 部署时必需 | 本地部署到 Cloudflare Pages |

## 扫描到的变量（非项目使用）

以下变量由扫描脚本从 `01-技能/已安装技能/skills/` 目录下的 SKILL.md 文档中检测到，**不是本项目实际使用的环境变量**，仅为 skill 文档中的示例/说明文本：

| 变量名 | 来源 | 是否本项目使用 |
|---|---|---|
| `BP` | skill 文档 | 否 |
| `BRAND_COLOR_HOVER` | skill 文档 | 否 |
| `CI` | skill 文档 | 否 |
| `CSP_MARKER_ATTR` | skill 文档 | 否 |
| `CSS` | skill 文档 | 否 |
| `DESIGN_PANEL_WIDTH` | skill 文档 | 否 |
| `DP` | skill 文档 | 否 |
| `EASE` | skill 文档 | 否 |
| `EXTENSION_MODE` | skill 文档 | 否 |
| `FONT` | skill 文档 | 否 |
| `ICON_ATTRS` | skill 文档 | 否 |
| `IMPECCABLE_CONTEXT_DIR` | skill 文档 | 否 |
| `IMPECCABLE_CRITIQUE_META` | skill 文档 | 否 |
| `IMPECCABLE_LIVE_APPLY_EVENT_HARD_TIMEOUT_MS` | skill 文档 | 否 |
| `IMPECCABLE_LIVE_APPLY_EVENT_SOFT_DEADLINE_MS` | skill 文档 | 否 |
| `IMPECCABLE_LIVE_COPY_AGENT` | skill 文档 | 否 |
| `IMPECCABLE_LIVE_COPY_AGENT_TIMEOUT_MS` | skill 文档 | 否 |
| `IMPECCABLE_LIVE_DEBUG_EVENTS` | skill 文档 | 否 |
| `IMPECCABLE_NO_UPDATE_CHECK` | skill 文档 | 否 |
| `IMPECCABLE_PALETTE_SEED` | skill 文档 | 否 |
| `IMPECCABLE_UPDATE_CACHE` | skill 文档 | 否 |
| `IMPECCABLE_UPDATE_HOST` | skill 文档 | 否 |
| `JSON` | skill 文档 | 否 |
| `MONO` | skill 文档 | 否 |
| `MY_TOKEN` | skill 文档 | 否 |
| `NODE_ENV` | skill 文档 | 否 |
| `OUTLINE_COLOR` | skill 文档 | 否 |
| `PIN_MARKER` | skill 文档 | 否 |
| `PORT` | skill 文档 | 否 |
| `SLEEK_API_KEY` | skill 文档 | 否 |
| `TOKEN` | skill 文档 | 否 |
| `TYPE_LABELS` | skill 文档 | 否 |
| `UPDATE_HOST` | skill 文档 | 否 |
| `VALID_COMMANDS` | skill 文档 | 否 |
| `VAR` | skill 文档 | 否 |

## 注意事项

- 本项目 **没有** `.env` 文件、`.env.example` 或应用级环境变量
- `CLOUDFLARE_API_TOKEN` 仅在部署时需要，本地预览和开发不需要
