---
document: KNOWN-ISSUES.md
generated: 2026-06-17
client_level: developer
---

# 已知问题与技术债

## 已知 Bug

### 1. Cloudflare CDN 缓存延迟

- **现象**：部署后主域名 `frontend-design-skills-showcase.pages.dev` 可能仍显示旧版本
- **影响**：用户看到旧的统计数字或旧的筛选逻辑
- **临时绕过**：使用 `production.frontend-design-skills-showcase.pages.dev` 别名访问
- **相关文件**：Cloudflare Pages 部署配置

### 2. 部分模型截图可能缺失

- **现象**：Kimi 2.5、Mimo V2 Omni、GLM 的部分页面截图可能存在空白
- **原因**：`file://` 协议下 CDN 资源加载超时（使用本地服务器截图可避免）
- **临时绕过**：使用 Playwright 截图脚本重新截取
- **相关文件**：`05-报告/展厅/assets/screenshots/`

### 3. 展厅统计数字与实际文件数不一致

- **现象**：index.html 中的统计数字（388 个页面）可能与 pages/ 目录实际文件数有偏差
- **原因**：手动添加/删除文件后未同步更新 index.html 中的统计数字
- **临时绕过**：编辑 `05-报告/展厅/index.html` 第 26 行的统计文本

## 未完成功能

- **评审标准**：`04-评审/` 目录为空，评审标准文档待补充
- **Gemini 3 截图**：部分补测页面（taste-skill / modern-web-design / superdesign）的截图可能未生成
- **GLM 5.2 集成（2026-06-17 补测）**：已完成集成部署 ✅
  - [x] 展厅集成：`05-报告/展厅/index.html` 新增 GLM 5.2 模型按钮（data-model="glm52"）、`getFileMap()` 的 `glm52` 分支、统计数字更新（388 → 430，9 → 10 模型）
  - [x] 文件复制：`03-产出/glm5.2/*.html` → `05-报告/展厅/pages/`（42 个文件）
  - [x] 截图入库：Playwright 截图脚本 `TempScr/screenshot-glm52.js`，airline/bikeops 使用 1920x1080（16:9），charging 使用 390x844（9:16）
  - [x] 部署：已通过 `npx wrangler pages deploy` 部署到 Cloudflare Pages
  - 注：GLM 5.2 与系统内置 GLM 5.0 是**两个独立版本**，展厅中并存展示

## 技术债

### 1. 展厅 index.html 为单文件 SPA

- **位置**：`05-报告/展厅/index.html`（约 500 行）
- **问题**：所有模型配置、文件映射、渲染逻辑都在一个文件中，新增模型需要修改多处代码
- **建议**：如模型数量继续增长，考虑拆分为 JSON 配置 + 渲染引擎

### 2. 文件命名不一致

- **位置**：`03-产出/` 各模型目录
- **问题**：不同模型的文件命名规则不统一（如 Kimi 用 `{skill}-{scenario}.html`，Gemini 用 `gemini3_{skill}_{scenario}.html`）
- **影响**：展厅 `getFileMap()` 函数需要为每个模型写特殊的映射逻辑

### 3. 无自动化测试

- **问题**：展厅的筛选、渲染逻辑没有自动化测试
- **风险**：修改 index.html 时可能引入回归 bug

## 安全注意项

未发现明显安全问题。本项目为纯静态 HTML 站点，无后端、无数据库、无用户认证。

- `CLOUDFLARE_API_TOKEN` 仅在部署时使用，不暴露在前端代码中
- 所有 HTML 页面通过 CDN 加载外部资源（Tailwind CSS、Google Fonts、图标库），无自有 API 调用
