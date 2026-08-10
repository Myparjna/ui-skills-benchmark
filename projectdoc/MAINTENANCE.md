---
document: MAINTENANCE.md
generated: 2026-06-17
client_level: developer
---

# 日常维护

## 监控与日志

本项目无应用级监控/日志组件。

**Cloudflare Pages 访问日志**：
- Cloudflare Dashboard → Pages → frontend-design-skills-showcase → Analytics
- 可查看访问量、带宽、错误率

## 依赖更新

本项目无 npm/Python 依赖需要更新。

**截图脚本依赖**（可选）：
```bash
# 更新 Playwright（注意：使用系统 Python 3.12，非 WorkBuddy Python 3.13）
"C:\Users\mypra\AppData\Local\Programs\Python\Python312\python.exe" -m pip install --upgrade playwright
"C:\Users\mypra\AppData\Local\Programs\Python\Python312\python.exe" -m playwright install chromium
```

## 例行检查清单

| 频率 | 检查项 | 方法 |
|---|---|---|
| 每月 | Cloudflare Pages 是否正常 | 访问 https://frontend-design-skills-showcase.pages.dev |
| 每月 | 截图是否正常显示 | 随机打开 5 个模型的页面检查 webp 缩略图 |
| 每季度 | Cloudflare 账号余额/套餐 | Cloudflare Dashboard → Billing |
| 新模型加测时 | 展厅统计数字是否更新 | 编辑 `index.html` header 区统计文本 |
| 新模型加测时 | getFileMap() 是否新增分支 | 参考 `glm52`/`gpt56terra` 集成模式（见 KNOWN-ISSUES.md） |
| 新模型加测时 | 8 处注册点是否齐全 | 模型按钮 / `{model}Categories` / getFileMap / getAllItems / loadFilters / getCurrentCategories / modelBadgeColor / 统计数字 |

## 定期清理

- `TempScr/`：一次性截图脚本，任务完成后可清理
- `03-产出/ScreenShot/`：截图残留，可清理
- `cloudflarepage展厅/pages/`：未注册模型的 HTML 副本（如 gemini3.1pro），确认不展示后可删除
- 过时目录移入 `Trash/` 保留备份，不直接删除

## Git 工作流

- **仓库**：https://github.com/Myparjna/ui-skills-benchmark（分支 `master`）
- **大更新后主动提交**：本地 git commit 用中文写清改动（见项目约定）
- **推送**：用户明确要求时才推 GitHub；`git push -u origin master`
- **运行痕迹不提交**：`.gitignore` 已忽略 `.omc/`（OMC 运行状态）与 `.playwright-cli/`（日志）；`git add -A` 前可用 `git status --short` 确认无运行状态文件混入
- **推送被 secret scanning 拦截**：若 GitHub 拦截含疑似密钥的提交，先核实（可能是 AI 生成的假占位 token），确认后重写历史再推送（详见 KNOWN-ISSUES.md 安全注意项）
