---
name: hanako-skill-forge
description: 花子专用的技能工程元技能。用于把零散提示词、旧技能、半成品结构或失序技能，收敛成文档主导、路由清楚、主来源唯一、可维护、可扩展、可自愈、可验收的长期技能资产。遇到“新建技能、重构技能、统一技能结构、给技能补维护/扩展/自愈链、清理技能冗余、建立技能验收口径、给技能补状态模板/检查点/交付链”时优先使用。若只是改单句文案、单文件微调、普通代码 bug、技能评测 benchmark，或只是泛化讨论 AI 工作流思路，则不要触发本技能。
---

# 花子技能元技能

核心目标：把技能做成精简、可验、可持续演进的资产。

## 默认产出

- 只保留完成功能所需的语句；
- 删除花哨修辞、重复解释、无执行价值的话；
- 用文档做主来源，用脚本做巡检、校验、收口；
- 保留维护、扩展、自愈三条正式改造链；
- 输出需求卡、蓝图、验收结果、交付摘要；
- 复杂改造需留下状态、检查点、验证证据。

## 什么时候用

- 新建技能；
- 重构旧技能；
- 精简技能内容；
- 给技能补维护、扩展、自愈改造链；
- 统一技能结构、主来源、验收口径；
- 处理技能失序、漂移、断链、历史残留。

## 什么时候不要用

- 只改单句文案；
- 单文件微调；
- 普通代码 bug；
- 只是讨论泛化 AI 工作流方案；
- 不涉及技能结构、路由、维护、验收的普通执行任务。

## 入口顺序

1. 先读 `modules/route/02-需求卡协议.md`
2. 再读 `modules/route/01-总控路由.md`
3. 需要边界判断时读 `guides/02-触发边界与相邻技能分工.md`
4. 按命中分支继续读：
   - 新建 / 重构：`modules/build/12-架构与落地协议.md`
   - 维护：`modules/maintenance/13-维护协议.md`
   - 扩展：`modules/extension/14-扩展协议.md`
   - 自愈：`modules/recovery/15-自愈协议.md`
   - 验收：`modules/review/16-验收与发布协议.md`
   - 评测与证据：`modules/review/17-评测与证据协议.md`
5. 需要模板时再读 `modules/templates/*`
6. 需要触发校准时读 `modules/review/18-触发评测样例集.md`
7. 需要巡检时再调用 `scripts/main.py`

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
- 能力注入：`modules/templates/33-能力注入模板.md`
- 自愈记录：`modules/templates/34-自愈记录模板.md`
- 维护检查：`modules/templates/35-维护检查清单模板.md`
- 交付摘要：`modules/templates/36-交付摘要模板.md`
- 任务状态：`modules/templates/37-任务状态模板.md`
- 检查点：`modules/templates/38-检查点模板.md`

巡检脚本：
- `python scripts/main.py --action module_index`
- `python scripts/main.py --action audit_refs`
- `python scripts/main.py --action audit_terms`
- `python scripts/main.py --action audit_skill`

脚本契约：
- `schemas/actions_contracts.json`

脚本只做巡检、校验、收口，不承担技能主体表达。

## 使用纪律

- 先定需求卡，再动手；
- 先删无用语句，再补必要规则；
- 先保证主来源唯一，再谈扩展；
- 维护、扩展、自愈是后续改造能力，不是默认执行步骤；
- 改造中要留下状态、检查点、证据；
- 没过验收，不算完成。
