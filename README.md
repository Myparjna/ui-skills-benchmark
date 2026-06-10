# 前端设计技能测评

> **测评领域**: 前端设计 (Frontend Design / Web Page)
> **测评日期**: 2026-04-17 (首版) / 2026-06-02 (M3 加测)
> **测评状态**: 已完成 (含 M3 加测)
> **线上展厅**: https://frontend-design-skills-showcase.pages.dev

---

## 项目概述

本项目横向对比 **7 个 AI 模型** 在 **前端设计 skill** 驱动下的页面生成效果。

- **测评目标**: 验证不同模型在使用相同/不同 design skill 时的页面生成质量差异
- **测评维度**: 视觉表现、设计系统一致性、响应式适配、代码质量
- **参与模型**: Kimi 2.5、Mimo V2 Omni、GLM、Gemini 3、Gemini 3.5、Mimo V2.5、MiniMax M3
- **测评技能数**: 14 款公共 design skill + 各模型独占 skill
- **测试场景**: 3 个产品场景（官网 / 小程序 / 后台）
- **总页面数**: 262 个 HTML 页面

---

## 快速导航

| 目录 | 内容 | 说明 |
|------|------|------|
| `00-计划/` | （本项目缺少独立的计划文档，信息见本 README） | — |
| `01-技能/` | 14 款公共 design skill + 版本锁定 | 已安装的技能文件 |
| `02-输入/` | 3 个产品的说明文档 | 测评用的产品需求 |
| `03-产出/` | 各模型的 HTML 页面产出 | `gemini3/` `gemini35/` `glm/` `kimi/` `mimoV2.5/` `mimoV2omni/` `minimaxM3/` |
| `04-评审/` | （待补充评审标准） | — |
| `05-报告/` | 测评报告 + 展厅网站 | `测评报告.md` + `M3-测评报告.md` + `展厅/index.html` |

---

## 核心结论

| 模型 | 页面数 | 公共 skill | 独占 skill | 备注 |
|------|--------|------------|------------|------|
| **Kimi 2.5** | 48 | 12 | 4 | Apple Inspired / Linear Inspired / 不使用skills / impeccable |
| **Mimo V2 Omni** | 46 | 12 | 3 | Apple Inspired / Linear Inspired / 不使用skills |
| **GLM** | 48 | 12 | 4 | Apple Inspired / Linear Inspired / impeccable / 不使用skills |
| **Gemini 3** | 39 | 12 | 1 | 不使用skills |
| **Gemini 3.5** | 33 | 12 | 1 | 不使用skills |
| **Mimo V2.5** | 42 | 14 | 4 | impeccable / taste-skill / modern-web-design / superdesign |
| **MiniMax M3** | 42 | 14 | 4 | impeccable / taste-skill / modern-web-design / superdesign |

- **最佳整体表现**: Kimi 2.5（页面数最多，独占 skill 效果好）
- **最佳反 LLM 审美**: MiniMax M3 (impeccable / taste-skill / design-taste-frontend 三款反 LLM skill 渲染质量最高，0 console error)
- **展厅部署**: 所有 262 页聚合展示于 Cloudflare Pages

---

## M3 加测（2026-06-02）

MiniMax M3 (minimax-m3-free) 加入横向对比，详细报告见 `05-报告/M3-测评报告.md`：

- 14 款公共 design skill × 3 场景 = 42 个 HTML
- 100% 截图通过率（42/42 OK，0 console error）
- fleet_ops 14 个 HTML 由 M3 Write 工具直接生成（subagent worker kimi-k2.6 5h 额度耗尽）
- 继承训练语料的设计品味（impeccable / taste-skill / design-taste-frontend 表现明显优于其他模型）

---

## 复现方法

```bash
# 1. 查看已安装的技能
打开 01-技能/已安装技能/

# 2. 查看产品需求输入
打开 02-输入/产品说明文档/

# 3. 对比各模型产出
打开 03-产出/kimi/ vs 03-产出/glm/ vs 03-产出/gemini3/ vs 03-产出/mimoV2omni/ vs 03-产出/mimoV2.5/ vs 03-产出/minimaxM3/

# 4. 打开展厅浏览所有页面
用浏览器打开 05-报告/展厅/index.html

# 5. 查看详细报告
打开 05-报告/测评报告.md
打开 05-报告/M3-测评报告.md  (M3 加测独立报告)

# 6. M3 截图复现
python TempScr/screenshot.py
```

---

## 分享与引用

- **本测评项目位置**: `C:\Users\mypra\Desktop\VibeCoding指南\skills测评项目\01-前端设计技能测评`
- **展厅在线地址**: https://frontend-design-skills-showcase.pages.dev
- **打包分享**: 直接打包整个 `01-前端设计技能测评/` 目录即可

---

*本测评项目使用标准化文件夹结构，参见根目录 `skills测评项目/README.md`*
