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
| Kimi K3 | 生成前端页面 HTML | 12 | 手动/AI 辅助工具 |
| DeepSeek V4 Flash0731 | 生成前端页面 HTML | 42 | 手动/AI 辅助工具 |
| Mimo V2 Omni | 生成前端页面 HTML | 37 | 手动/AI 辅助工具 |
| Mimo V2.5 | 生成前端页面 HTML | 42 | 手动/AI 辅助工具 |
| GLM 5.1（原 GLM 5.0） | 生成前端页面 HTML | 40 | 手动/AI 辅助工具 |
| GLM 5.2 | 生成前端页面 HTML | 42 | 手动/AI 辅助工具 |
| MiniMax M3 | 生成前端页面 HTML | 42 | 手动/AI 辅助工具 |
| Gemini 3 | 生成前端页面 HTML | 42 | 手动/AI 辅助工具 |
| Gemini 3.1 Pro | 生成前端页面 HTML | 9 | 手动/AI 辅助工具（未集成展厅） |
| GPT-5.6 Terra | 生成前端页面 HTML | 42 | 手动/AI 辅助工具 |
| Qwen 3.7 Plus | 生成前端页面 HTML | 42 | Task 子代理并行生成 |
| Hy3（助手自驱） | 生成前端页面 HTML | 42 | 14 个隔离 subagent 并行生成 |

**检测到的模型名引用**：扫描在 `cloudflarepage展厅/pages/kimi-k3-ui-ux-pro-max-airline.html` 检测到 `o1`/`o3` 字样（页面正文提及 OpenAI 模型名，属页面内容，非运行时 AI 调用）。

## 使用的 SDK

**无任何 AI SDK / API 客户端**。扫描结果（`analysis-report.json` `ai_services.sdks`）为空数组。

本项目运行时（展厅静态站点）不调用任何 AI API，不引入任何 SDK。AI 模型的生成能力通过各官方客户端/平台手动使用，无代码集成，因此不存在 SDK 版本管理、API key 注入或调用点维护的交接项。

## 计费与限额

不涉及。所有 AI 调用在内容生产阶段已完成，展厅运行时无 AI API 调用。

## 降级与故障

不涉及。展厅为纯静态站点，无 AI API 依赖，不存在降级场景。

## 与模型供应商的关联

本项目仅消费各模型的生成能力，未接入任何模型的 API 计费接口。模型供应商（Kimi/Moonshot、DeepSeek、GLM/Zhipu、Gemini/Google、Mimo、MiniMax、Qwen/Aliyun、GPT/OpenAI）均通过各自官方客户端或平台手动使用，无代码集成。
