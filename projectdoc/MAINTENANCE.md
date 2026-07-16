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
# 更新 Playwright
pip install --upgrade playwright
python -m playwright install chromium
```

## 例行检查清单

| 频率 | 检查项 | 方法 |
|---|---|---|
| 每月 | Cloudflare Pages 是否正常 | 访问 https://frontend-design-skills-showcase.pages.dev |
| 每月 | 截图是否正常显示 | 随机打开 5 个模型的页面检查截图 |
| 每季度 | Cloudflare 账号余额/套餐 | Cloudflare Dashboard → Billing |
| 新模型加测时 | 展厅统计数字是否更新 | 编辑 `index.html` 第 26 行 |
| 新模型加测时 | getFileMap() 是否新增分支 | 参考 `glm5.2` 集成模式（详见 KNOWN-ISSUES.md） |
