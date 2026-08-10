---
document: DEPLOYMENT.md
generated: 2026-06-17
client_level: developer
---

# 部署指南

## 部署方式

**Cloudflare Pages** — 静态站点托管

通过 Wrangler CLI 直接部署 `cloudflarepage展厅/` 目录到 Cloudflare Pages。部署目标分支为 **production**（线上生产版本），旧文档中的 `--branch=main` 已废弃。

## 首次完整部署演练

### 前置条件

1. 安装 Node.js（v18+）
2. 安装 Wrangler CLI：`npm install -g wrangler`
3. 登录 Cloudflare：`wrangler login`，或配置 `CLOUDFLARE_API_TOKEN`
4. 确保 `CLOUDFLARE_API_TOKEN` 环境变量已配置（系统用户环境变量，见 ENVIRONMENT.md）

### 部署步骤

```bash
# 1. 进入展厅目录
cd "cloudflarepage展厅"

# 2. 部署到 Cloudflare Pages 生产分支
npx wrangler pages deploy . --project-name=frontend-design-skills-showcase --branch=production
```

### 部署后验证

```bash
# 访问生产地址：https://frontend-design-skills-showcase.pages.dev
# 访问 production 别名：https://production.frontend-design-skills-showcase.pages.dev
# 部署命令输出中也会给出本次部署的唯一预览 URL
```

### CI/CD

未配置 GitHub Actions / 其他 CI。部署完全依赖本机 Wrangler CLI 手动执行。GitHub 仓库（https://github.com/Myparjna/ui-skills-benchmark）仅作代码托管，不触发自动部署。

### 注意事项

- Cloudflare Pages 有 CDN 缓存，部署后主域名可能需要几分钟更新
- 如遇缓存问题，优先使用 `production.frontend-design-skills-showcase.pages.dev` 别名
- 可在 Cloudflare Dashboard → Pages → frontend-design-skills-showcase → Purge cache 手动清除缓存
- 部署前必须本地验证（启动 HTTP 服务器 + 浏览器检查），避免线上回归

## 部署历史

| 日期 | 内容 | 页面数 |
|---|---|---|
| 2026-06-10 | 首次部署 + Kimi K2.6 加测 | 349 |
| 2026-06-16 | 新增 Qwen 3.7 Plus | 391 |
| 2026-06-16 | 移除 Gemini 3.5 | 349 |
| 2026-06-17 | Gemini 3 补测完成 + 移除"不使用skills"基线 | 388 |
| 2026-06-18 | GLM 5.2 补测集成部署 + Kimi K2.6 截图重截 | 430 |
| 2026-07 | Hy3 集成 + 缩略图改版（png→webp） | 484（本地 index 显示）/ 526（pages/ 实有） |
