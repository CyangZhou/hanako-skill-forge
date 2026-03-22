---
name: hanako-skill-forge
description: 花子专用的技能元技能。用于新建、重构、维护、扩展、修复技能；默认把技能写成“只保留功能必要语句”的精简结构，并保留维护、扩展、自愈这三条后续改造链，让技能长期可修、可改、可恢复。
---

# 花子技能元技能

核心目标：把技能做成好用、精简、长期可改的资产，不做花哨堆料。

## 默认产出

- 只保留完成功能所需的语句；
- 删除花里胡哨、只起修辞作用、不能提升执行效果的内容；
- 用文档做主来源，用脚本做巡检和收口；
- 保留维护、扩展、自愈三条正式改造链，供以后修技能、扩技能、做自愈时使用；
- 不把“可维护、可扩展、可自愈”误写成技能每次执行时都要做的内部功能。

## 什么时候用

- 新建技能；
- 重构旧技能；
- 精简技能内容；
- 给技能补维护、扩展、自愈改造链；
- 统一技能结构和验收口径。

## 入口顺序

1. 先读 `modules/route/02-需求卡协议.md`
2. 再读 `modules/route/01-总控路由.md`
3. 按命中分支继续读：
   - 新建 / 重构：`modules/build/12-架构与落地协议.md`
   - 维护：`modules/maintenance/13-维护协议.md`
   - 扩展：`modules/extension/14-扩展协议.md`
   - 自愈：`modules/recovery/15-自愈协议.md`
   - 验收：`modules/review/16-验收与发布协议.md`
4. 需要模板时再读 `modules/templates/*`
5. 需要巡检时再调用 `scripts/main.py`

## 主路由优先级

**自愈 > 维护 > 扩展 > 新建 / 重构**

含义：
- 已坏先修；
- 失序先收口；
- 不够再扩；
- 最后再做新建或重构。

## 输出与脚本边界

输出模板：
- 需求卡：`modules/templates/31-需求卡模板.md`
- 技能蓝图：`modules/templates/32-技能蓝图模板.md`
- 交付摘要：`modules/templates/36-交付摘要模板.md`

巡检脚本：
- `python scripts/main.py --action module_index`
- `python scripts/main.py --action audit_refs`
- `python scripts/main.py --action audit_terms`
- `python scripts/main.py --action audit_skill`

脚本只做巡检、校验、收口，不承担技能主体表达。

## 使用纪律

- 先定需求卡，再动手；
- 先删无用语句，再补必要规则；
- 先保证主来源唯一，再谈扩展；
- 维护、扩展、自愈是后续改造能力，不是默认执行步骤；
- 没过验收，不算完成。
