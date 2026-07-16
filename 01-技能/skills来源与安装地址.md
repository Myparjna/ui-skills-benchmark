# 12 款公共 Design Skills 来源与安装地址

> 最后更新: 2026-06-01
> 状态: 12 个已安装到 `已安装技能/skills/`
> 变更: 已移除 design-md、canvas-design、taste-skill、frontend-design-pro；保留 modern-web-design、impeccable、superdesign

---

## 汇总表

| 序号 | 技能名 | GitHub 仓库 | skills.sh 链接 | 安装命令 | 来源类型 | 备注 |
|------|--------|------------|----------------|---------|---------|------|
| 1 | stitch-design | [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) | [skills.sh](https://skills.sh/google-labs-code/stitch-skills/stitch-design) | 本地已有，无需重装 | Google Labs | 原版 |
| 2 | web-design-guidelines | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | [skills.sh](https://skills.sh/vercel-labs/agent-skills/web-design-guidelines) | `npx skills add vercel-labs/agent-skills@web-design-guidelines -g -y` | Vercel 官方 | 原版 |
| 3 | sleek-design-mobile-apps | [sleekdotdesign/agent-skills](https://github.com/sleekdotdesign/agent-skills) | [skills.sh](https://skills.sh/sleekdotdesign/agent-skills/sleek-design-mobile-apps) | `npx skills add sleekdotdesign/agent-skills@sleek-design-mobile-apps -g -y` | Sleek 官方 | 原版 |
| 4 | shadcn | [shadcn/ui](https://github.com/shadcn-ui/ui) | [skills.sh](https://skills.sh/shadcn-ui/ui/shadcn) | 本地已有，无需重装 | shadcn 官方 | 原版 |
| 5 | design-taste-frontend | [evgyur/design-taste-frontend](https://github.com/evgyur/design-taste-frontend) | [skills.sh](https://skills.sh/evgyur/design-taste-frontend) | `npx skills add evgyur/design-taste-frontend@design-taste-frontend -g -y` | 个人仓库 | 原版 |
| 6 | frontend-design | [anthropics/skills](https://github.com/anthropics/skills) | [skills.sh](https://skills.sh/anthropics/skills/frontend-design) | `npx skills add anthropics/skills@frontend-design -g -y` | Anthropic 官方 | 原版 |
| 7 | modern-frontend-design | [deveshpunjabi/modern-frontend-skill](https://github.com/deveshpunjabi/modern-frontend-skill) | [skills.sh](https://skills.sh/deveshpunjabi/modern-frontend-skill/modern-frontend-design) | `npx skills add deveshpunjabi/modern-frontend-skill@modern-frontend-design -g -y` | 个人仓库 | 替代版，原版仓库未找到 |
| 8 | nuxt-ui | [nuxt/ui](https://github.com/nuxt/ui) | [skills.sh](https://skills.sh/nuxt/ui/nuxt-ui) | `npx skills add nuxt/ui@nuxt-ui -g -y` | Nuxt 官方 | 原版 |
| 9 | ui-ux-pro-max | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | [skills.sh](https://skills.sh/nextlevelbuilder/ui-ux-pro-max-skill/ui-ux-pro-max) | `npx skills add nextlevelbuilder/ui-ux-pro-max-skill@ui-ux-pro-max -g -y` | 个人仓库 | 原版 |
| 10 | impeccable | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | [skills.sh](https://skills.sh/pbakaus/impeccable/impeccable) | `npx skills add pbakaus/impeccable@impeccable -g -y` | pbakaus | Med Risk |
| 11 | modern-web-design | [freshtechbro/claudedesignskills](https://github.com/freshtechbro/claudedesignskills) | [skills.sh](https://skills.sh/freshtechbro/claudedesignskills/modern-web-design) | `npx skills add freshtechbro/claudedesignskills@modern-web-design -g -y` | 个人仓库 | 原版 |
| 12 | superdesign | [superdesigndev/superdesign-skill](https://github.com/superdesigndev/superdesign-skill) | [skills.sh](https://skills.sh/superdesigndev/superdesign-skill/superdesign) | `npx skills add superdesigndev/superdesign-skill@superdesign -g -y` | 个人仓库 | Snyk Critical Risk |

---

## 按来源分类

### 官方/知名仓库 (6 个)
| 技能名 | 来源 | Stars |
|--------|------|-------|
| frontend-design | Anthropic | - |
| stitch-design | Google Labs (Stitch) | ~5.8K |
| web-design-guidelines | Vercel | ~27K |
| sleek-design-mobile-apps | Sleek Design | ~413 |
| shadcn | shadcn/ui | ~115K |
| nuxt-ui | Nuxt | ~6.6K |

### 个人/社区仓库 (6 个)
| 技能名 | 来源 | 安装量 |
|--------|------|--------|
| design-taste-frontend | evgyur | - |
| modern-frontend-design | deveshpunjabi | 250 (skills.sh) |
| ui-ux-pro-max | nextlevelbuilder | 4.7K (skills.sh) |
| impeccable | pbakaus | Med Risk |
| modern-web-design | freshtechbro | - |
| superdesign | superdesigndev | Snyk Critical Risk |

---

## 批量安装命令

```bash
# 一键安装全部 12 个（跳过已有的，需代理：export HTTPS_PROXY=http://127.0.0.1:7897）
npx skills add google-labs-code/stitch-skills@stitch-design -g -y
npx skills add vercel-labs/agent-skills@web-design-guidelines -g -y
npx skills add sleekdotdesign/agent-skills@sleek-design-mobile-apps -g -y
npx skills add shadcn-ui/ui@shadcn -g -y
npx skills add evgyur/design-taste-frontend@design-taste-frontend -g -y
npx skills add anthropics/skills@frontend-design -g -y
npx skills add deveshpunjabi/modern-frontend-skill@modern-frontend-design -g -y
npx skills add nuxt/ui@nuxt-ui -g -y
npx skills add nextlevelbuilder/ui-ux-pro-max-skill@ui-ux-pro-max -g -y
npx skills add pbakaus/impeccable@impeccable -g -y
npx skills add freshtechbro/claudedesignskills@modern-web-design -g -y
npx skills add superdesigndev/superdesign-skill@superdesign -g -y
```

---

## 已知问题

1. **modern-frontend-design**: 原版仓库未找到，当前使用 deveshpunjabi 的替代版本（250 安装量）
2. **stitch-design**: `npx skills add` 报名找不到，但本地已有原版文件
3. **ui-ux-pro-max**: 安全评估为 High Risk（Gen 平台），使用时注意审查

---

## 已移除的技能

| 技能名 | 移除原因 |
|--------|---------|
| design-md | 文档格式规范技能，非前端页面设计技能 |
| canvas-design | 静态视觉艺术/海报设计，非前端页面设计技能 |
| Apple Inspired | 基于 design.md 的自定义版本，已过时 |
| Linear Inspired | 基于 design.md 的自定义版本，已过时 |
