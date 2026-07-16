---
document: AI-SERVICES.md
generated: 2026-06-17
client_level: developer
---

# AI 服务

## 说明

本项目 **不涉及运行时 AI 调用**。AI 模型在项目中仅作为"内容生产工具"使用——即由 AI 模型生成 HTML 页面，然后作为静态文件部署。

展厅本身不需要任何 AI API 即可运行。

## AI 模型使用情况（内容生产阶段）

以下为各模型在生成 HTML 页面时的使用情况，供参考：

| 模型 | 用途 | 生成页面数 | 调用方式 |
|---|---|---|---|
| Kimi 2.5 | 生成前端页面 HTML | 45 | 手动/AI 辅助工具 |
| Kimi K2.6 | 生成前端页面 HTML | 42 | 手动/AI 辅助工具 |
| DeepSeek V4 | 生成前端页面 HTML | 42 | 手动/AI 辅助工具 |
| Mimo V2 Omni | 生成前端页面 HTML | 37 | 手动/AI 辅助工具 |
| Mimo V2.5 | 生成前端页面 HTML | 42 | 手动/AI 辅助工具 |
| GLM | 生成前端页面 HTML | 40 | 手动/AI 辅助工具 |
| MiniMax M3 | 生成前端页面 HTML | 42 | 手动/AI 辅助工具 |
| Gemini 3 | 生成前端页面 HTML | 42 | 手动/AI 辅助工具 |
| Qwen 3.7 Plus | 生成前端页面 HTML | 42 | Task 子代理并行生成 |

## 计费与限额

不涉及。所有 AI 调用在内容生产阶段已完成，展厅运行时无 AI API 调用。

## 降级与故障

不涉及。展厅为纯静态站点，无 AI API 依赖，不存在降级场景。
