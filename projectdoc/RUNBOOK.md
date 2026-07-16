---
document: RUNBOOK.md
generated: 2026-06-17
client_level: developer
---

# 运维手册 (Runbook)

## 紧急联系人

| 角色 | 联系方式 | 负责范围 |
|---|---|---|
| 项目负责人 | [需向交接人确认: 联系方式] | 整体项目决策 |
| Cloudflare 账号管理员 | [需向交接人确认: 联系方式] | 部署、域名、CDN |

## 回滚

```bash
# Cloudflare Pages 回滚到上一个版本
# 方法 1：CLI 回滚
npx wrangler pages deployment list --project-name=frontend-design-skills-showcase
npx wrangler pages deployment rollback --project-name=frontend-design-skills-showcase <deployment-id>

# 方法 2：Dashboard 回滚
# Cloudflare Dashboard → Pages → frontend-design-skills-showcase → Deployments → 找到目标版本 → Rollback to this deployment
```

## 常见故障处置

| 症状 | 可能原因 | 处置步骤 |
|---|---|---|
| 展厅白屏 | index.html 部署失败或文件损坏 | 1. 检查 `05-报告/展厅/index.html` 是否完整 2. 重新部署 `npx wrangler pages deploy . --project-name=frontend-design-skills-showcase --branch=production` |
| 统计数字不正确 | index.html 中的数字未更新 | 编辑 `05-报告/展厅/index.html` 第 26 行的统计文本，重新部署 |
| 截图不显示 | 截图文件缺失或路径错误 | 1. 检查 `assets/screenshots/` 目录 2. 重新运行截图脚本 |
| 部署失败（403） | API Token 过期或权限不足 | 1. 在 Cloudflare Dashboard 重新生成 Token 2. 更新环境变量 `CLOUDFLARE_API_TOKEN` |
| CDN 缓存未更新 | Cloudflare 缓存 | 使用 `production.frontend-design-skills-showcase.pages.dev` 别名，或在 Dashboard 手动 Purge cache |

## 密钥失效处理

| 密钥 | 失效现象 | 重新生成方式 | 更新位置 |
|---|---|---|---|
| `CLOUDFLARE_API_TOKEN` | 部署报 403 Forbidden | Cloudflare Dashboard → My Profile → API Tokens → 创建新 Token | 本地环境变量 |
