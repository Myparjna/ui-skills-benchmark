---
document: DEPLOYMENT.md
generated: 2026-06-17
client_level: developer
---

# 部署指南

## 部署方式

**Cloudflare Pages** — 静态站点托管

通过 Wrangler CLI 直接部署 `05-报告/展厅/` 目录到 Cloudflare Pages。

## 首次完整部署演练

### 前置条件

1. 安装 Node.js（v18+）
2. 安装 Wrangler CLI：`npm install -g wrangler`
3. 登录 Cloudflare：`wrangler login`
4. 确保 `CLOUDFLARE_API_TOKEN` 环境变量已配置（如未使用 `wrangler login`）

### 部署步骤

```bash
# 1. 进入展厅目录
cd "05-报告/展厅"

# 2. 部署到 Cloudflare Pages
npx wrangler pages deploy . --project-name=frontend-design-skills-showcase

# 3. 部署到生产分支（确保主域名更新）
npx wrangler pages deploy . --project-name=frontend-design-skills-showcase --branch=main
```

### 部署后验证

```bash
# 访问预览地址（部署命令输出中给出）
# 访问生产地址：https://frontend-design-skills-showcase.pages.dev
# 访问 main 别名：https://main.frontend-design-skills-showcase.pages.dev
```

### 注意事项

- Cloudflare Pages 有 CDN 缓存，部署后主域名可能需要几分钟更新
- 如遇缓存问题，优先使用 `production.frontend-design-skills-showcase.pages.dev` 别名
- 可在 Cloudflare Dashboard → Pages →frontend-design-skills-showcase → Purge cache 手动清除缓存
