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

### 2. 部分模型截图可能缺失或白屏

- **现象**：早期模型（Kimi 2.5、Mimo V2 Omni、GLM）的部分页面截图可能存在空白；React+Babel 页面（design-taste-frontend 等）曾白屏
- **原因**：`file://` 协议下 CDN 资源加载超时；Babel 自动 JSX runtime 缺少 `react/jsx-runtime` 模块
- **临时绕过**：使用本地服务器 + Playwright 截图脚本重截；React+Babel 页面通过 importmap 注入修复（见 TempScr/retry-glm52-white.js）
- **相关文件**：`cloudflarepage展厅/assets/thumbnails/`

### 3. 展厅统计数字与实际文件数不一致

- **现象**：index.html 中的统计数字（484 个页面）与 pages/ 目录实际文件数（526）有偏差
- **原因**：手动添加/删除文件后未同步更新 index.html 中的统计数字；pages/ 含未注册的 gemini3.1pro 与历史残留
- **临时绕过**：编辑 `cloudflarepage展厅/index.html` 的统计文本（约在 header 区）
- **状态**：统计基准待确认（见 README.md 待确认问题）

## 未完成功能

- **Gemini 3.1 Pro 未集成展厅**（03-产出/gemini3.1pro/，9 页，中文命名）
  - [x] HTML 生成：9 页（星空航空官网 / 充电桩小程序 / 两轮后台，含重复变体）
  - [ ] 文件复制 → pages/（未做）
  - [ ] 截图入库（未做）
  - [ ] 展厅注册（index.html 无 gemini3.1pro 分支，未做）
  - [ ] 部署（未做）
- **Kimi K3 已集成**（03-产出/kimi-k3/，12 页）
  - [x] HTML 生成：12 页（4 skill × 3 场景：ui-ux-pro-max / design-taste-frontend / frontend-design / web-design-guidelines）
  - [x] 文件复制 → pages/（12 页已入库）
  - [x] 截图入库（12 张 webp 缩略图已生成）
  - [x] 展厅注册（index.html 已有 kimiK3 按钮 + getFileMap 分支）
  - [ ] 线上部署确认（本地已提交并推送 GitHub，但线上展厅未重新部署，需运行 wrangler deploy）
- **评审标准**：`04-评审/` 目录为空，评审标准文档待补充

## 技术债

### 1. 展厅 index.html 为单文件 SPA

- **位置**：`cloudflarepage展厅/index.html`（约 500 行）
- **问题**：所有模型配置、文件映射、渲染逻辑都在一个文件中，新增模型需要修改多处代码
- **建议**：新增模型时，需要修改 8 处代码（模型按钮、分类数组、文件映射、Badge颜色、过滤器、统计数字），考虑抽象为 JSON 配置 + 渲染引擎（模型数量继续增长时建议优化）

### 2. 文件命名不一致

- **位置**：`03-产出/` 各模型目录
- **问题**：不同模型的文件命名规则不统一（如 Kimi 用 `{skill}_{scene}.html`，Gemini 用 `gemini3_{skill}_{scene}.html`，Gemini 3.1 Pro 用中文命名）
- **影响**：展厅 `getFileMap()` 函数需要为每个模型写特殊的映射逻辑；`gemini3.1pro/` 中文命名导致无法纳入现有映射

### 3. 无自动化测试

- **问题**：展厅的筛选、渲染逻辑没有自动化测试
- **风险**：修改 index.html 时可能引入回归 bug（详见 REGRESSION-TEST.md）

### 4. 目录残留

- `03-产出/ScreenShot/`：截图残留目录（无 HTML）
- `03-产出/gemini35/`：1 页残留（已从展厅移除）
- `cloudflarepage展厅/pages/`：含未注册模型的 HTML 副本，与 index.html 统计口径不一致

## 安全注意项

本项目为纯静态 HTML 站点，无后端、无数据库、无用户认证。

- `CLOUDFLARE_API_TOKEN` 仅在部署时使用，不暴露在前端代码中
- 所有 HTML 页面通过 CDN 加载外部资源（Tailwind CSS、Google Fonts、图标库），无自有 API 调用
- **历史已处理：Mapbox token 泄露**（2026-08-10）：commit `fbf0fda` 中 `gemini3_modern-web-design_ev_charging.html` 第 33 行含 AI 生成的**假占位 token**（signature 部分为重复 `6Z6Z6Z...` 模式，非真实密钥），被 GitHub secret scanning 的 push protection 拦截。已用 `git filter-branch --tree-filter` 重写 `fbf0fda^..HEAD` 两个 commit，将 token 替换为 `YOUR_MAPBOX_TOKEN`，并清除 `refs/original` 备份、`reflog expire`、`gc --prune`。全历史搜索确认无残留。**教训**：AI 生成的页面含 mapbox/token 等字符串时应先用 `git grep` 检查再推送
