---
document: REGRESSION-TEST.md
generated: 2026-08-10 15:18
client_level: developer
---

# 回归测试说明

## 测试现状

- 测试配置: 未检测到
- 测试目录: 未检测到
- 测试文件数: 0
- 自动化测试: **无**。项目为纯静态 HTML + 单文件 SPA 展厅，无任何单元/集成/E2E 测试框架，无 npm scripts。

扫描结果（`projectdoc/analysis-report.json` `testing` 字段）确认 0 个测试文件。展厅筛选/渲染逻辑（`index.html` 约 500 行单文件）无自动化测试覆盖，新增模型时依赖人工验证。

## 回归范围

| 业务流程/模块 | 风险 | 验证方式 | 通过标准 | 证据位置 |
|---|---|---|---|---|
| 展厅筛选逻辑（模型/场景/skill 组合） | 高（单文件 SPA，8 处注册点） | 浏览器人工点选 | 13 个模型按钮均可切换，组合筛选无空结果 | `cloudflarepage展厅/index.html` |
| 单页预览器（view.html iframe） | 中 | 浏览器打开任意页面 | iframe 正常渲染，无空白 | `cloudflarepage展厅/view.html` |
| 缩略图显示 | 中 | 浏览器浏览展厅卡片 | 540 张 webp 全部可加载 | `cloudflarepage展厅/assets/thumbnails/` |
| 页面 HTML 渲染（无白屏） | 高 | 截图脚本 + 浏览器检查 | 桌面 1280×720 / 移动 390×844 无白屏 | 截图脚本输出 |
| 部署 | 中 | wrangler deploy + 线上访问 | 线上页面与本地一致 | Cloudflare Pages |
| 新模型注册 | 高 | 按 8 处注册点核对 | 模型按钮出现、分类可筛、文件可映射 | `cloudflarepage展厅/index.html:48-58,183,301,334-385,481-492` |

## 自动化测试

```bash
# 未检测到任何自动化测试命令。
# 项目无 npm scripts、无 pytest、无 test 目录。
# 以下为"存在但属一次性截图脚本，非测试"（脚本在 TempScr/ 下）：
"C:\Users\mypra\AppData\Local\Programs\Python\Python312\python.exe" "TempScr/shot_showcase.py"
```

**执行情况**：截图脚本仅生成缩略图，不校验功能正确性，不作为自动化测试依据。任何自动化测试均**未执行过**。

## 人工与真实软件验证

以下为新增模型/改动展厅时必须执行的浏览器人工验证（本项目唯一有效验证手段）：

1. **启动本地服务器**：`cd cloudflarepage展厅 && python -m http.server 8766`，访问 http://localhost:8766
2. **模型切换**：逐个点击 13 个模型按钮，确认卡片与缩略图正确显示
3. **组合筛选**：模型 + skill + 场景任意组合筛选，确认无空结果、无重复
4. **单页预览**：点击卡片预览，确认 iframe 加载对应 HTML，无白屏（尤其 React+Babel 页面，需 importmap 修复）
5. **截图完整性**：新模型 42 张（或实际数量）缩略图全部非零字节
6. **线上验证**：部署后访问主域名 + production 别名，确认无 CDN 缓存旧版本

## 测试数据与环境

- 测试浏览器：系统 Chrome（`C:\Program Files\Google\Chrome\Application\chrome.exe`）+ Playwright（chromium）
- 截图环境：系统 Python 3.12（`C:\Users\mypra\AppData\Local\Programs\Python\Python312\python.exe`），**非** WorkBuddy 托管 Python 3.13
- 测试账号：无（展厅公开，无需登录）
- 外部依赖：所有测试页面依赖 CDN（Tailwind / Google Fonts / 图标库），无网或 CDN 慢会表现为白屏，非代码缺陷

## 发布前最小回归清单

- [ ] 展厅在本地 HTTP 服务器可正常打开（非 file:// 协议）
- [ ] 13 个模型按钮全部可切换，卡片正确显示
- [ ] 组合筛选（模型 × skill × 场景）无空结果
- [ ] view.html 单页预览可正常 iframe 加载
- [ ] 全部缩略图（540 张）非零字节、可加载
- [ ] 新模型页面 3 个场景 HTML 可正常渲染（无白屏/无 console 报错）
- [ ] `index.html` 统计数字与 pages/ 实际文件数一致
- [ ] 部署后主域名 + production 别名验证通过

## 已知测试缺口

1. **无自动化测试**：展厅筛选/渲染逻辑无单测/E2E，风险集中在 index.html 单文件。建议：模型数量继续增长时引入 Playwright E2E 或抽取配置为 JSON + 快照测试
2. **白屏回归**：React+Babel 页面白屏问题（importmap 修复）无自动检测，需人工打开每页确认
3. **CDN 依赖**：页面依赖外部 CDN，离线环境无法验证真实渲染，与线上表现可能有差异
4. **截图脚本属一次性**：无法覆盖模型重复、文件映射错误等逻辑回归
