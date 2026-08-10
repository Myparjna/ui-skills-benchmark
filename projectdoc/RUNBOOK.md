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

本地文件回滚（误删/误改产出或展厅文件时）：

```bash
# 查看工作区改动
git status --short

# 丢弃未提交改动（谨慎，先确认无需要的改动）
git checkout -- "cloudflarepage展厅/index.html"

# 从历史版本恢复
git log --oneline
git checkout <commit-hash> -- "cloudflarepage展厅/pages/"
```

## 常见故障处置

| 症状 | 可能原因 | 处置步骤 |
|---|---|---|
| 展厅白屏 | index.html 部署失败或文件损坏 | 1. 检查 `cloudflarepage展厅/index.html` 是否完整 2. 重新部署 `npx wrangler pages deploy . --project-name=frontend-design-skills-showcase --branch=production` |
| 统计数字不正确 | index.html 中的数字未更新 | 编辑 `cloudflarepage展厅/index.html` header 区统计文本，重新部署 |
| 缩略图不显示 | webp 文件缺失或路径错误 | 1. 检查 `assets/thumbnails/` 目录 2. 重新运行截图脚本（Python 3.12） |
| 页面白屏（React+Babel） | importmap 缺失 `react/jsx-runtime` | 注入 importmap shim（`{"imports":{"react/jsx-runtime":"data:text/javascript,export const jsx=React.createElement;..."}}`）并给 `<script type="text/babel">` 加 `data-type="module"`，重截缩略图（历史修复脚本已清理，逻辑见交接文档） |
| 部署失败（403） | API Token 过期或权限不足 | 1. 在 Cloudflare Dashboard 重新生成 Token 2. 更新环境变量 `CLOUDFLARE_API_TOKEN` |
| CDN 缓存未更新 | Cloudflare 缓存 | 使用 `production.frontend-design-skills-showcase.pages.dev` 别名，或在 Dashboard 手动 Purge cache |
| 截图脚本报错 | 用了 WorkBuddy Python 3.13 而非系统 Python 3.12 | 改用绝对路径 `C:\Users\mypra\AppData\Local\Programs\Python\Python312\python.exe` |

## 密钥失效处理

| 密钥 | 失效现象 | 重新生成方式 | 更新位置 |
|---|---|---|---|
| `CLOUDFLARE_API_TOKEN` | 部署报 403 Forbidden | Cloudflare Dashboard → My Profile → API Tokens → 创建新 Token | 系统用户环境变量 |
