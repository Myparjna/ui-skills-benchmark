# 交接文档增量更新建议

- 项目根目录：`C:\Users\mypra\Desktop\VibeCoding指南\skills测评项目\01-前端设计技能测评`
- 上次扫描基线：存在

## 关键文件变化

- 新增：`01-技能/已安装技能/skills/impeccable/reference/live.md`, `01-技能/已安装技能/skills/impeccable/scripts/context.mjs`, `01-技能/已安装技能/skills/impeccable/scripts/critique-storage.mjs`, `01-技能/已安装技能/skills/impeccable/scripts/detector/engines/browser/detect-url.mjs`, `01-技能/已安装技能/skills/impeccable/scripts/live-commit-manual-edits.mjs`, `01-技能/已安装技能/skills/impeccable/scripts/live-server.mjs`, `01-技能/已安装技能/skills/impeccable/scripts/palette.mjs`, `05-报告/展厅/index.html`, `05-报告/展厅/pages/kimi-k3-ui-ux-pro-max-airline.html`, `README.md`
- 修改：无
- 删除：无

## 自上次验收基线以来的 Git 变更

- 范围：`--since=2026-06-17T05:31:32Z`，另有 202 个未提交变更
- Commit 列表（最多 50 条）：
  - `fbf0fda 2026-07-17 chore: 整理技能展厅与移动端截图`
  - `18db920 2026-06-18 docs: 更新交接文档 - GLM 5.2 集成、Kimi K2.6 截图修复、复制按钮、部署分支修正`
  - `70a98c3 2026-06-18 fix: 重新截取 Kimi K2.6 全部 42 张截图（修复白屏问题）`
  - `77542fb 2026-06-18 fix: 修复 design-taste-frontend 白截图 + 展厅功能增强`
  - `0ff3c12 2026-06-18 feat: 完成 GLM 5.2 展厅集成并部署上线`

## 文档建议

| 文档 | 动作 | 原因 | 变化字段 |
|---|---|---|---|
| `AI-SERVICES.md` | update | 相关扫描事实发生变化 | `ai_services`, `external_resources`, `native_embedded_ai` |
| `ARCHITECTURE.md` | update | 相关扫描事实发生变化 | `directory_tree`, `external_resources`, `native_embedded_ai` |
| `DEPLOYMENT.md` | update | 相关扫描事实发生变化 | `deployment_targets` |
| `ENVIRONMENT.md` | update | 相关扫描事实发生变化 | `environment_variables` |
| `INFRASTRUCTURE.md` | update | 相关扫描事实发生变化 | `external_resources`, `git` |
| `KNOWN-ISSUES.md` | update | 相关扫描事实发生变化 | `scan_completeness`, `testing` |
| `MAINTENANCE.md` | update | 相关扫描事实发生变化 | `git` |
| `MODULES.md` | create | 当前 ProjectDoc 中缺少该文档 | `directory_tree`, `native_embedded_ai` |
| `README.md` | update | 相关扫描事实发生变化 | `git` |
| `REGRESSION-TEST.md` | create | 当前 ProjectDoc 中缺少该文档 | `testing` |
| `RUNBOOK.md` | update | 相关扫描事实发生变化 | `ai_services` |
| `USAGE.md` | create | 当前 ProjectDoc 中缺少该文档 | - |

## AI 执行要求

- 先阅读旧文档和 changed key files，再补充语义层面的影响说明。
- 只原地修改 action=create/update/review 的文档；action=preserve 的文档不得重写。
- 人工补充、历史决策和运维经验默认保留；只有新证据明确推翻时才修改。
- 完成后运行 verify_handoff.py，不得把本计划当作已完成的更新。

> 这是机器差异建议。AI 必须结合旧文档和源码补充真实影响，不能仅凭修改时间更新文档。
