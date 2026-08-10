# 交接文档生成计划（handoff-plan）

- 项目根目录：`C:\Users\mypra\Desktop\VibeCoding指南\skills测评项目\01-前端设计技能测评`
- 模式：**update**（用户通过 --intent update 显式指定）
- 受众级别：`developer`

## 文档清单

| 文档 | 动作 | 必需 | 原因 | focus |
|---|---|---|---|---|
| `README.md` | **generate** | 是 | 门禁必需文档 | 30 秒看懂项目 + 快速启动 + 速查卡；待确认问题全部汇总到顶部 |
| `USAGE.md` | **generate** | 是 | 门禁必需文档 | 从真实用户角色出发的核心业务流程，启动不等于使用 |
| `ARCHITECTURE.md` | **generate** | 是 | 门禁必需文档 | mermaid 架构图、数据流、技术选型理由、AI 工具链痕迹 |
| `MODULES.md` | **generate** | 是 | 门禁必需文档 | 按业务职责划分模块，至少两条真实调用链并引用源码路径 |
| `ENVIRONMENT.md` | **generate** | 是 | 门禁必需文档 | 每个变量的用途/获取方式/必需性/泄露影响，不遗漏、不写真实值 |
| `DEPLOYMENT.md` | **generate** | 是 | 门禁必需文档 | 按检测到的平台分章节写完整可复制的部署命令 |
| `INFRASTRUCTURE.md` | **generate** |  | 基础交接文档 | 域名/DNS/SSL/第三方账号清单与交接动作 |
| `REGRESSION-TEST.md` | **generate** | 是 | 门禁必需文档 | 区分检测到/已执行/已通过，写清测试缺口 |
| `KNOWN-ISSUES.md` | **generate** |  | 基础交接文档 | 宁可多写不可隐瞒：Bug、半成品功能、技术债 |
| `MAINTENANCE.md` | **generate** |  | 基础交接文档 | 看日志/看账单/查漏洞的精确入口 |
| `RUNBOOK.md` | **generate** |  | 基础交接文档 | 回滚命令、故障→处置对照表 |
| `AI-SERVICES.md` | **generate** |  | 检测到：模型名出现 | AI API 的调用点、模型、计费限额与降级行为 |
| `API.md` | **skip** |  | 未检测到相关事实，跳过 | 接口清单以扫描为准，鉴权方式读源码确认 |
| `DATABASE.md` | **skip** |  | 未检测到相关事实，跳过 | 数据模型、迁移流程、备份恢复命令 |
| `DESKTOP.md` | **skip** |  | 未检测到相关事实，跳过 | 构建打包命令、代码签名与自动更新现状 |

## 扫描范围

- 文件总数：1921，实际扫描：1288
- .handoff.yml 额外跳过目录：无
- 扫描完整，无需调整范围。

## 执行要求

- 先把本计划展示给用户确认（模式、文档清单、focus、范围），用户可编辑 plan 文件调整后再继续。
- generate_handoff.py 会读取本计划并跳过 action=skip 的文档。
- required=true 的文档是门禁硬要求，跳过会导致 verify 失败。
- update 模式下本计划只判定模式与缺失文档；具体章节影响仍以 compare_handoff.py 的更新建议为准。

> 请用户确认或修改本计划（可直接编辑 project-handoff-plan.json 中的 action/focus），
> 确认后再运行 generate_handoff.py。
